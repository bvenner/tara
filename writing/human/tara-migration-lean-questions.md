# tara-migration-lean — clarifying questions

*Composed by the agent (GLM) for Brad, 2026-10-18. Working title: `tara-migration-lean` — a certified program-synthesis harness combining LeetProof (`/home/brad/Projects/LeetProof`, paper: [arXiv:2604.16584](https://arxiv.org/pdf/2604.16584)) with the agent-harness-poc ideas (`projects/agent-harness-poc`). The new harness formalizes agent coordination (spec'd in plumbing, migrated to Lean) and the hypergraph knowledge representation (also in Lean) for context/state management and resource ingestion.*

Answer inline under each question. Anything not answered will be recorded as an open decision in the project plan.

---

## Scope & architecture

### 1. What gets migrated, exactly?

"Formal specification of agent coordination developed in plumbing, migrated to Lean": does this mean

- (a) formalize plumbing's semantics (typed morphisms, exact-typed `exec` boundaries, multi-agent routing, tool-calling agent loops) as a Lean model and prove harness properties against it, or
- (b) port a *subset* — e.g. the workload manifests / researcher-prefetch coordination pattern from M6/M7 — as Lean specs?

Context: full plumbing semantics in Lean is a research project on its own (it's an interpreter with agent/tool machinery); a subset-first approach mirrors what worked in M6 ("workloads as data").

**Your answer:**

For the rest of this document, I will use the term vericoding as a synonym for the term "certified program synthesis" in the arxiv document.

Long term, I would like to have the functionality of the plumbing system formalized in lean. This is in order for the vericoding harness to inspect it's own agent coordination architecture and to integrate continuous improvement in this architecture. LeetProof develops the agent coordination framework outside of the vericoding system and thus cannot continously improve.

Another goal would be to support vericoding for multi-paradigm programming language that can include object-oriented, functional and imperative programming styles. The object-oriented paradigm would be dual to the functional paradigm, as described in the paper https://arxiv.org/pdf/2403.06707. I have a related research program beginning to explort this duality at https://github.com/bvenner/codata-agda.

&nbsp;

### 2. What does Lean certify?

Candidate load-bearing certs (pick/extend):

- typed-contract conformance of orchestrator↔worker calls (the "extra input key is fatal" class of failure);
- evidence-trace validity as an inductive/thin invariant on hypergraph operations;
- workflow manifests satisfying coordination safety/liveness properties (e.g. budget compliance — plumb scored 0% budget compliance in M7 slice 2).

**Your answer:**

I answered this in question 1. The harness is intended for Lean to be able to develop certified programs written in a muli-paradigm style using some combination of object-oriented, functional and imperative styles.

&nbsp;

### 3. What gets synthesized?

Is the harness itself to be synthesized in Lean via LeetProof's pipeline (Lean program + proof, Python orchestrator à la LeetProof), or does the Python/pydantic glue layer survive while only the *spec and proofs* live in Lean? Put differently: vericoding *of* the agent harness, or certified *metatheory* about it?

**Your answer:**

Yes, the goal is to allow Lean to generate certified multi-agent systems that use compile-time checks to ensure properly-shaped data across seams. So the harness would be able to certify the shape of it's own pipelines. 

&nbsp;

### 4. Hypergraph in Lean — spec or runtime?

Does Lean *replace* the SQLite/graph runtime, or does it specify the data model and operations while execution stays in the existing pipelines? Reimplementing the docstore/pipeline machinery in Lean is a big translation effort; interpreting Lean-spec'd contracts against the existing runtime is much cheaper.

**Your answer:**

One of plumbing's strengths is its EIO-based runtime written in Ocaml. Since this would be a large effort to rewrite in Lean, it probably makes sense to keep the plumbing language and runtime. So the Lean system would generate plumb files that would use the exising plumbing runtime.

I anticipate developing a formal specification for hypergraphs implemented in Lean and using mathlib, but with an eye to usability by implementing a content-addressable hypergraph system as described in https://arxiv.org/html/2604.10435v1.

Hopefully this answered the question.

&nbsp;

---

## Project hygiene

### 5. Relationship to open threads

agent-harness-poc has open items (M7 disposition of opencode, post-M7). Does tara-migration-lean

- (a) supersede it,
- (b) consume it (workloads/scorer as fixtures for the Lean-certified harness), or
- (c) run in parallel?

And should it live at `projects/tara-migration-lean/` with the standard AGENTS.md resume path, per workspace conventions?

**Your answer:**

I'd like to keep the existing harness for now, as this proposed migration may fail. So please keep this new project strictly in parallel for now.

&nbsp;

### 6. Reverse the name

The name "tara-migration-lean" suggests the eventual goal is migrating TARA itself (knowledge repository, pipelines) to Lean, with this project as the first slice. Is that the intent, or is the name just a standing label?

**Your answer:**

Yes, that is the intent, so I suggest we keep the name.

&nbsp;

### 7. Deliverable

Paper, Master's thesis sub-problem, or internal infrastructure for the rest of the program? This changes what a "v1" looks like.

**Your answer:**

If successful, this would be foundational architecture for developing multi-agent systems and simulating them in agent-based models. It would touch all existing research projects.

&nbsp;

---

## Environment

### 8. Lean toolchain on this box

LeetProof's artifact ships as Docker images (amd64/arm64 tarballs in the repo). Do we run it via Docker, or a local elan/Lean install? Is Docker working on this machine?

(Note: no GPU here; frontier-prover API access is OpenRouter-only — some Lean provers (e.g. DeepSeek-Prover-V2, Goedel-Prover) are reachable that way, but a raw `lake` interaction loop against them is untested.)

**Your answer:**

A local Lean install would be best.

&nbsp;

### 9. LLM budget

LeetProof's experiments burned real API spend (`gpt-stats.json`, `opus-stats.json` in the repo). Budget posture: OpenRouter GLM tier only, or open to Anthropic/OpenAI spend for prover traffic?

**Your answer:**

Let's see. Since we would be adding new functionality to LeetProof, there should be no need to reimplement these proofs. However, I understand that this is a big project and that it may entail a substantial use of LLM resources. Let's develop a preliminary scope before making this decision.

&nbsp;
