import { mkdir, readdir, readFile, writeFile } from "node:fs/promises";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import path from "node:path";

const run = promisify(execFile);

const apiKey = process.env.OPENROUTER_API_KEY;
if (!apiKey) throw new Error("Set OPENROUTER_API_KEY.");

const inputDir = "./recordings";
const outputDir = "./transcripts";
const chunkDir = "./chunks";

const model = "mistralai/voxtral-small-transcribe-3-0";
const language = "en"; // set to null to auto-detect
const chunkSeconds = 600; // 10 minutes per chunk (keeps payloads under provider limits)
const chunkBitrate = "64k"; // mono mp3, ~4.8 MB per chunk
const requestTimeoutMs = 600_000;
const maxAttempts = 3;
const retryableStatus = new Set([429, 500, 502, 503, 504, 524, 529]);

type Segment = {
  start: number;
  end: number;
  text: string;
  speaker?: number | string;
  speaker_label?: string;
  chunk?: number;
  [key: string]: unknown;
};

type Transcription = {
  text: string;
  segments?: Segment[];
  language?: string;
  duration?: number;
  usage?: { seconds?: number; cost?: number; [key: string]: unknown };
  [key: string]: unknown;
};

type Chunk = { file: string; start: number };

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function probeDuration(file: string): Promise<number> {
  const { stdout } = await run("ffprobe", [
    "-v", "error",
    "-show_entries", "format=duration",
    "-of", "default=noprint_wrappers=1:nokey=1",
    file,
  ]);
  return Number(stdout.trim());
}

// Split one recording into <=10-minute mono mp3 chunks; returns each chunk's
// absolute start time within the recording (from measured chunk durations).
async function chunkAudio(sourcePath: string, baseName: string): Promise<Chunk[]> {
  const dir = path.join(chunkDir, baseName);
  await mkdir(dir, { recursive: true });
  await run("ffmpeg", [
    "-y",
    "-i", sourcePath,
    "-ac", "1",
    "-b:a", chunkBitrate,
    "-f", "segment",
    "-segment_time", String(chunkSeconds),
    "-reset_timestamps", "1",
    path.join(dir, "chunk-%03d.mp3"),
  ]);
  const names = (await readdir(dir))
    .filter((name) => /^chunk-\d+\.mp3$/.test(name))
    .sort();
  const chunks: Chunk[] = [];
  let start = 0;
  for (const name of names) {
    const file = path.join(dir, name);
    chunks.push({ file, start });
    start += await probeDuration(file);
  }
  return chunks;
}

async function postChunk(
  data: string,
  format: string,
  useDiarize: boolean,
): Promise<Transcription> {
  const body = {
    model,
    input_audio: { data, format },
    response_format: "verbose_json",
    timestamp_granularities: ["segment"],
    ...(language ? { language } : {}),
    ...(useDiarize ? { diarize: true } : {}),
  };

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    let response: Response;
    try {
      response = await fetch("https://openrouter.ai/api/v1/audio/transcriptions", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(requestTimeoutMs),
      });
    } catch (err) {
      console.warn(`  attempt ${attempt}: network error (${String(err)})`);
      if (attempt === maxAttempts) throw err;
      await sleep(2_000 * attempt);
      continue;
    }

    if (response.ok) return (await response.json()) as Transcription;

    const detail = await response.text();
    if (response.status === 400 && useDiarize) {
      console.warn("  diarize rejected by provider; retrying without it");
      return postChunk(data, format, false);
    }
    if (response.status === 413) {
      throw new Error(`payload too large: ${detail}`);
    }
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

async function transcribeChunk(chunkFile: string): Promise<Transcription> {
  const cachePath = chunkFile.replace(/\.mp3$/, ".json");
  try {
    const cached = JSON.parse(await readFile(cachePath, "utf8")) as Transcription;
    if (typeof cached.text === "string") {
      console.log(`  reusing ${cachePath}`);
      return cached;
    }
  } catch {
    // no usable cache; transcribe below
  }
  const audio = await readFile(chunkFile);
  const result = await postChunk(audio.toString("base64"), "mp3", true);
  await writeFile(cachePath, JSON.stringify(result, null, 2), "utf8");
  return result;
}

// Transcribe one recording: chunk it, transcribe each chunk (cached per chunk),
// then merge segments with absolute timestamps into transcripts/<base>.{txt,verbose.json}.
async function processFile(file: string): Promise<{ seconds: number; cost: number }> {
  const baseName = file.replace(path.extname(file), "");
  const audioPath = path.join(inputDir, file);
  console.log(`\n=== ${file} ===`);

  const chunks = await chunkAudio(audioPath, baseName);
  console.log(`  ${chunks.length} chunk(s) of <=${chunkSeconds}s`);

  const mergedText: string[] = [];
  const mergedSegments: Segment[] = [];
  let seconds = 0;
  let cost = 0;

  for (const [index, chunk] of chunks.entries()) {
    console.log(`  chunk ${index + 1}/${chunks.length} (start ${chunk.start.toFixed(1)}s)`);
    const result = await transcribeChunk(chunk.file);
    mergedText.push(result.text.trim());
    for (const segment of result.segments ?? []) {
      mergedSegments.push({
        ...segment,
        start: segment.start + chunk.start,
        end: segment.end + chunk.start,
        chunk: index,
      });
    }
    seconds += result.usage?.seconds ?? 0;
    cost += result.usage?.cost ?? 0;
  }

  await mkdir(outputDir, { recursive: true });
  await writeFile(
    path.join(outputDir, `${baseName}.txt`),
    mergedText.join(" "),
    "utf8",
  );
  await writeFile(
    path.join(outputDir, `${baseName}.verbose.json`),
    JSON.stringify(
      {
        file,
        model,
        language,
        chunkSeconds,
        chunks: chunks.length,
        segments: mergedSegments,
        usage: { seconds, cost },
      },
      null,
      2,
    ),
    "utf8",
  );
  console.log(`  saved ${outputDir}/${baseName}.txt and ${outputDir}/${baseName}.verbose.json`);
  return { seconds, cost };
}

// One cheap (~$0.01) request on a 90s clip: verifies auth, diarization support,
// and the response shape before committing to the full run.
async function smokeTest(): Promise<void> {
  const files = (await readdir(inputDir)).filter((f) => /\.(wav|mp3|m4a|flac)$/i.test(f)).sort();
  if (files.length === 0) throw new Error(`no audio files in ${inputDir}`);
  const source = path.join(inputDir, files[0]);

  await mkdir(chunkDir, { recursive: true });
  const clip = path.join(chunkDir, "smoke-clip.mp3");
  await run("ffmpeg", ["-y", "-ss", "0", "-t", "90", "-i", source, "-ac", "1", "-b:a", chunkBitrate, clip]);

  const audio = await readFile(clip);
  const result = await postChunk(audio.toString("base64"), "mp3", true);

  await mkdir(outputDir, { recursive: true });
  const outPath = path.join(outputDir, "smoke-test.json");
  await writeFile(outPath, JSON.stringify(result, null, 2), "utf8");

  const speakers = new Set(
    (result.segments ?? []).map((s) => s.speaker_label ?? s.speaker).filter((s) => s !== undefined),
  );
  console.log(`smoke test OK -> ${outPath}`);
  console.log(`  language: ${result.language ?? "(not returned)"}  segments: ${result.segments?.length ?? "(none)"}  speakers: ${speakers.size || "(none)"}`);
  console.log(`  usage: ${JSON.stringify(result.usage)}`);
  console.log(`  text preview: ${result.text.slice(0, 300)}`);
}

const isSmoke = process.argv.includes("--smoke");

if (isSmoke) {
  await smokeTest();
} else {
  const files = (await readdir(inputDir))
    .filter((file) => /\.(wav|mp3|m4a|flac)$/i.test(file))
    .sort();
  if (files.length === 0) throw new Error(`no audio files in ${inputDir}`);

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

  console.log(`\ndone: ${files.length - failures.length}/${files.length} file(s), ${seconds.toFixed(0)}s billed, $${cost.toFixed(4)}`);
  if (failures.length > 0) {
    console.error(`failed: ${failures.join(", ")} (completed chunks are cached in ${chunkDir}/; re-run to resume)`);
    process.exitCode = 1;
  }
}
