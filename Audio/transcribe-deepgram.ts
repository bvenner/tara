import { mkdir, readdir, readFile, stat, writeFile } from "node:fs/promises";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import path from "node:path";

const run = promisify(execFile);

// Load ../.env when present (e.g. DEEPGRAM_API_KEY), without overriding real env vars.
try {
  process.loadEnvFile(path.resolve("..", ".env"));
} catch {
  // no .env at repo root; rely on the process environment
}

const apiKey = process.env.DEEPGRAM_API_KEY;
if (!apiKey) throw new Error("Set DEEPGRAM_API_KEY (in ../.env or the environment).");

const inputDir = "./recordings";
const outputDir = "./transcripts";

const model = "nova-3";
const language = "en"; // set to null to auto-detect (Nova-3 multilingual)
const pricePerHour = 0.26; // Nova-3 monolingual pre-recorded, PAYG
const requestTimeoutMs = 600_000;
const maxAttempts = 3;
const retryableStatus = new Set([429, 500, 502, 503, 504, 529]);

const mimeByExt: Record<string, string> = {
  m4a: "audio/mp4",
  mp4: "audio/mp4",
  mp3: "audio/mpeg",
  wav: "audio/wav",
  flac: "audio/flac",
  ogg: "audio/ogg",
  webm: "audio/webm",
};

type Utterance = {
  start: number;
  end: number;
  speaker?: number;
  transcript: string;
  confidence?: number;
};

type DeepgramResponse = {
  metadata?: { duration?: number; channels?: number };
  results?: {
    channels?: Array<{ alternatives?: Array<{ transcript?: string }> }>;
    utterances?: Utterance[];
    detected_language?: string;
  };
};

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function estimateCost(durationSeconds: number): number {
  return (durationSeconds / 3600) * pricePerHour;
}

async function transcribeFile(audioPath: string): Promise<DeepgramResponse> {
  const ext = path.extname(audioPath).slice(1).toLowerCase();
  const contentType = mimeByExt[ext] ?? "application/octet-stream";
  const audio = await readFile(audioPath);

  const params = new URLSearchParams({
    model,
    smart_format: "true",
    punctuate: "true",
    diarize: "true",
    utterances: "true",
    ...(language ? { language } : {}),
  });

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    let response: Response;
    try {
      response = await fetch(`https://api.deepgram.com/v1/listen?${params}`, {
        method: "POST",
        headers: {
          Authorization: `Token ${apiKey}`,
          "Content-Type": contentType,
        },
        body: audio,
        signal: AbortSignal.timeout(requestTimeoutMs),
      });
    } catch (err) {
      console.warn(`  attempt ${attempt}: network error (${String(err)})`);
      if (attempt === maxAttempts) throw err;
      await sleep(2_000 * attempt);
      continue;
    }

    if (response.ok) return (await response.json()) as DeepgramResponse;

    const detail = await response.text();
    if (retryableStatus.has(response.status)) {
      console.warn(`  attempt ${attempt}: ${response.status} ${detail.slice(0, 200)}`);
      if (attempt === maxAttempts) break;
      await sleep(2_000 * attempt);
      continue;
    }
    throw new Error(`${response.status} ${detail}`);
  }
  throw new Error(`transcription failed after ${maxAttempts} attempts`);
}

// Transcribe one recording with diarization and write:
//   transcripts/<base>.txt          — "Speaker N: ..." per utterance (timestamped)
//   transcripts/<base>.verbose.json — utterances with start/end/speaker + metadata
async function processFile(file: string): Promise<{ seconds: number; cost: number }> {
  const baseName = file.replace(path.extname(file), "");
  const audioPath = path.join(inputDir, file);
  const txtPath = path.join(outputDir, `${baseName}.txt`);
  const jsonPath = path.join(outputDir, `${baseName}.verbose.json`);
  console.log(`\n=== ${file} ===`);

  try {
    await readFile(jsonPath);
    console.log(`  ${jsonPath} exists; skipping (delete it to re-transcribe)`);
    const cached = JSON.parse(await readFile(jsonPath, "utf8")) as {
      usage?: { seconds?: number; cost?: number };
    };
    return { seconds: cached.usage?.seconds ?? 0, cost: cached.usage?.cost ?? 0 };
  } catch {
    // not cached yet
  }

  const result = await transcribeFile(audioPath);
  const utterances = result.results?.utterances ?? [];
  const seconds = result.metadata?.duration ?? 0;
  const cost = estimateCost(seconds);
  const speakers = [...new Set(utterances.map((u) => u.speaker))].sort();

  await mkdir(outputDir, { recursive: true });

  const lines = utterances.map((u) => {
    const t0 = u.start.toFixed(1);
    const t1 = u.end.toFixed(1);
    return `[${t0}s–${t1}s] Speaker ${u.speaker ?? "?"}: ${u.transcript}`;
  });
  await writeFile(txtPath, lines.join("\n") + "\n", "utf8");

  await writeFile(
    jsonPath,
    JSON.stringify(
      {
        file,
        model,
        language,
        speakers,
        utterances,
        full_text: result.results?.channels?.[0]?.alternatives?.[0]?.transcript ?? "",
        usage: { seconds, cost },
      },
      null,
      2,
    ),
    "utf8",
  );

  console.log(`  ${utterances.length} utterance(s), speakers: ${speakers.join(", ") || "none"}`);
  console.log(`  ${seconds.toFixed(0)}s billed (~$${cost.toFixed(4)})`);
  console.log(`  saved ${txtPath} and ${jsonPath}`);
  return { seconds, cost };
}

// One cheap request on a 90s clip: verifies the API key and that diarization
// returns speaker labels before committing to the full run.
async function smokeTest(): Promise<void> {
  const files = (await readdir(inputDir)).filter((f) => /\.(wav|mp3|m4a|flac)$/i.test(f)).sort();
  if (files.length === 0) throw new Error(`no audio files in ${inputDir}`);
  const source = path.join(inputDir, files[0]);

  await mkdir("./chunks", { recursive: true });
  const clip = "./chunks/smoke-deepgram.m4a";
  await run("ffmpeg", ["-y", "-ss", "0", "-t", "90", "-i", source, "-c", "copy", clip]);

  const result = await transcribeFile(clip);
  const utterances = result.results?.utterances ?? [];
  const speakers = [...new Set(utterances.map((u) => u.speaker))].sort();

  console.log("smoke test OK");
  console.log(`  duration: ${result.metadata?.duration}s  utterances: ${utterances.length}  speakers: ${speakers.join(", ") || "none"}`);
  console.log(`  estimated cost: $${estimateCost(result.metadata?.duration ?? 0).toFixed(4)}`);
  console.log(`  text preview: ${utterances.map((u) => `Speaker ${u.speaker}: ${u.transcript}`).join(" | ").slice(0, 400)}`);
}

const isSmoke = process.argv.includes("--smoke");
const audioFilePattern = /\.(wav|mp3|m4a|flac)$/i;

// Positional args (e.g. `node transcribe-deepgram.ts Moaiwi-4.m4a`) select
// specific recordings; with none, every audio file in ./recordings is used
// (already-transcribed ones are still skipped via the .verbose.json cache).
async function selectFiles(): Promise<string[]> {
  const requested = process.argv.slice(2).filter((arg) => !arg.startsWith("-"));
  if (requested.length === 0) {
    const all = (await readdir(inputDir)).filter((file) => audioFilePattern.test(file)).sort();
    if (all.length === 0) throw new Error(`no audio files in ${inputDir}`);
    return all;
  }

  const selected = requested.map((arg) => path.basename(arg));
  for (const file of selected) {
    if (!audioFilePattern.test(file)) {
      throw new Error(`${file}: unsupported extension (expected wav, mp3, m4a, flac)`);
    }
    try {
      await stat(path.join(inputDir, file));
    } catch {
      throw new Error(`${file}: not found in ${inputDir}`);
    }
  }
  return selected;
}

if (isSmoke) {
  await smokeTest();
} else {
  const files = await selectFiles();

  let seconds = 0;
  let cost = 0;
  const failures: string[] = [];
  for (const file of files) {
    try {
      const totals = await processFile(file);
      seconds += totals.seconds;
      cost += totals.cost;
    } catch (err) {
      console.error(`${file}: FAILED — ${String(err)}`);
      failures.push(file);
    }
  }

  console.log(`\ndone: ${files.length - failures.length}/${files.length} file(s), ${seconds.toFixed(0)}s billed, ~$${cost.toFixed(4)}`);
  if (failures.length > 0) {
    console.error(`failed: ${failures.join(", ")}`);
    process.exitCode = 1;
  }
}
