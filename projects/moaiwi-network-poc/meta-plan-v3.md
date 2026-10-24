---
title: "moaiwi-network-poc meta-plan v3"
date: 2026-10-24
kind: research-plan
project: moaiwi-network-poc
---

# Meta-plan v3 — a higher-order network of workplace cooperatives

*Drafted 2026-10-24 from scratch, per `writing/human/moaiwi-revision-proposal.md` (authoritative where anything conflicts; conflicts are noted in §8). Primary sources: `writing/human/MOAIWI-{1,2,3,4}.md` and `writing/human/Informatics1Readable.md`. The previous meta-plan (now `projects/moaiwi-network-poc/2026-10-21-moaiwi-network-poc-meta-plan.md`) is reviewable input only, not a tracked baseline.*

## 1. Purpose — the end in mind

This meta-plan begins with the end in mind, taking the value of any such attempt on faith. The end is **a higher-order network of workplace cooperatives that solves the problems that defeated previous attempts to scale cooperative networks**. The meta-plan is not itself the plan of work; it is the instrument by which more specific plans will be developed. Everything below is organized so that a specific plan can be read off it: a project, a phase of that project, and the meta-processes active during that phase.

## 2. Structure: two dimensions

The meta-plan is organized in two dimensions, loosely time and space.

- **Time — projects.** The development is a series of projects. Each project is composed of sub-projects, called **phases**. The projects are **Moaiwi**, **Hyphae**, and **Cooptopia**, in that order; each depends on the one before it.
- **Space — meta-processes.** Running during every phase of every project are four ongoing meta-processes: **Research**, **Develop**, **Deploy**, and **Reflect**. They always interact. They are not overhead around the "real" work; they *are* the working part of the organization, and they are themselves targets of technology development.

The success of the whole depends on the skill of the meta-processes. At any project stage, each meta-process must be realized as a collection of interacting agents — human or computational — linked together by exchange of resources over channels. The central generative capacity this plan demands is the ability to **dynamically generate realizations of the meta-processes appropriate to the project stage**.

| | Research | Develop | Deploy | Reflect |
|---|---|---|---|---|
| **Moaiwi** | sector + user research | Fortress → business server | first real deployment | imagine what the product is for |
| **Hyphae** | economy/network modeling | confederation technology | network pilots | imagine the confederation |
| **Cooptopia** | research-only | premature | premature | imagine past the 5% ceiling |

## 3. The projects (time dimension)

### 3.1 Project 1 — Moaiwi: a B2B product for impact investors

**What it is.** A business-to-business product serving the needs of impact investors associated with the [U.S. Solidarity Economy Network](https://ussen.org) (USSEN), hereafter USSEN. The project is organic growth from connections Nic made with several impact investors at the [Resist and Build conference, Denver, CO, 2026](https://resistandbuild.net/den-2026/). The working name is **Moaiwi**.

**Who builds it.** The developer is the workplace cooperative **proletariat.tech** (PT). The lead developer for PT is **Nic Venner** — pronouns **they/them**. PT currently has an alpha-stage business-to-consumer product, **Fortress** (source on this machine at `/home/brad/Projects/fortress`, and on Codeberg at <https://codeberg.org/proletariat/fortress>).

**Fortress is the basis for Moaiwi.** The goal is to make Fortress sufficiently configurable that the same code base can be used to specify either a home-network server or a business server. Fortress is already built on exactly this principle — every service is a declaratively enabled module, like Nix packages: what is not in the configuration does not exist in the source tree (MOAIWI-4) — so the Moaiwi work is the disciplined extension of an existing architecture, not a rewrite.

**Audience and revenue goal.** The initial target audience is impact investors in USSEN. The revenue goal is a sufficiently large collection of clients to produce **annual revenue of $50,000**, which would sustain Nic in the continued development of this meta-plan. Meeting it may require expanding the target audience to impact investors outside formal association with USSEN. Impact investors were chosen because they are aligned with the meta-plan's longer-term goals while having sufficient economic resources to meet the revenue targets.

**The value logic.** To meet the revenue target, Moaiwi must produce sufficient value that impact investors will pay for the software. This is done by a combination of (a) **replacing existing software expenditures** and (b) **facilitating the growth of the impact investment funds**. Consequently Moaiwi must meet or exceed the reliability targets of existing cloud-based services *and* offer new features not currently accessible to impact investors. Candidate features are described in the transcripts — e.g. research across multiple impact-investing funds, for which at least one interlocutor's community was already considering budgeting a person (MOAIWI-4); capital allocation across a portfolio with mixed instruments and returns (MOAIWI-1–3). Further features will be identified through **user interviews, pilot demonstrations, and literature review**. A market-side research project belongs here: surveying impact investing as a sector — which funds exist, what they do, which are growing — since growth beyond the warm-introduced circle means appealing to funds outside the cooperative space (MOAIWI-4).

**Commercial form (from the transcripts, not yet a decision).** Nic's working inclination (MOAIWI-4) is to charge for the business layer on top of the Fortress stack, offered under a strong copyleft or source-available license (GPL v3, BSL, or similar): self-hosting is free, the B2B addition is the product. This is a hypothesis to validate against the user interviews, not a locked choice.

**Phases.** The phases below are a **draft** — the revision proposal fixes the projects but not their decomposition, so this decomposition is my synthesis from the transcripts and is open to revision at review. The initial presentation Nic would give is, per MOAIWI-4, **a Fortress demo with the B2B client functionality plus a proposal for the research stack** — an expandable subset of existing functionality that can inflate up to the later mathematical abstractions — with vague long-term promises left deliberately vague.

- **Phase M1 — Ground truth and demonstration.** User interviews with USSEN-associated impact investors: back-office needs, existing tools, what they would want from a thing like this (listen to the complaints). Fortress configured as a business server, demo-ready. Sector survey of impact investing begins. The R&B DEN-2026 overview (see §8, open question) fits here if it is wanted.
- **Phase M2 — Pilots and first revenue.** Pilot demonstrations with warm-introduced funds; the paid cross-fund research service; the B2B addition to the Fortress stack sold as replacing existing software spend. Success metric: clients paying because the tool is worth paying for, not out of goodwill.
- **Phase M3 — Sustainability and expansion.** Annual revenue at or above $50,000. Expansion of the audience beyond USSEN association as needed. By the end of this phase Nic is sustained by the product, which is the condition for the rest of this meta-plan.

### 3.2 Project 2 — Hyphae: technology for a confederation of workplace cooperatives

**What it is.** Technology to facilitate a **confederation of workplace cooperatives**, working name **Hyphae**. Hyphae would allow greater cooperation between impact investors and cooperative networks: impact investors provide much-needed **equity capital** to cooperative networks; cooperative networks provide **measurable environmental, social, and financial impacts** that attract additional impact investors.

**How it would work.** Hyphae uses advanced modeling and analysis approaches to identify opportunities to develop a workplace cooperative that would provide a good or service that grows the cooperative network. It is grounded in a model of **the local economy and the cooperative network itself**. The operative move is **replacement**: a good or service currently procured in the conventional economy by cooperatives or their members is replaced by one provided by a cooperative in the network — and the replacement must **increase environmental, social, and/or financial value**. Done well, Hyphae develops a **synergy between investors and cooperators greater than either could achieve alone**.

**Contrast with prior art.** Mondragon started with an investment and brought investing in early; this program brings investing in later, on top of a network (MOAIWI-4). The financial mechanics the transcripts work out — non-voting equity shares, internal vs. external rates of return, buy-out of external investors, bonds vs. equity and their failure modes, portfolio construction with treasuries to hit blended returns (MOAIWI-1–3) — are the design space Hyphae's modeling has to formalize. The value-theoretic grounding for the modeling (value as a scalar-valued secondary function; the limits of price-denominated data; the internal chart of accounts) is in `writing/human/Informatics1Readable.md`.

**Phases.** Not yet decomposed; Hyphae begins after Moaiwi is on solid footing (Phase M3), because it needs both the deployed infrastructure and the investor relationships. A first phase will most plausibly be a **model**, not software: the local-economy-and-network model on which everything else is grounded.

### 3.3 Project 3 — Cooptopia: past the growth limits of the cooperative economy

**What it is.** Technology to facilitate the growth of the cooperative economy **past the current limits to its growth**. Even where cooperative networks have substantial presence — the Mondragon Corporation is the canonical case — such networks rarely exceed **~5% of total economic flows**. The working hypothesis is that these limits are not inherent to the cooperative economy but are limitations of **productive, organizational, and information technology**. The working name is **Cooptopia**.

**Status: research-only.** Because Cooptopia depends on Hyphae, it is premature to develop specific project goals. For now it is a research-only project: the 5%-ceiling hypothesis gets investigated (prior art: Mondragon and the literature on it; category-theoretic and network formulations), and nothing is promised beyond that.

## 4. The meta-processes (space dimension)

Each meta-process runs in every phase of every project, always interacting with the others. Each is also a target of technology development: the projects can only be executed as well as the meta-processes are skilled. At every project stage each must be realized as **interacting agents (human or computational) linked by exchange of resources over channels**, and the realizations must be **dynamically generated** as the project stage changes. Current realizations and development intentions follow; these too are the transcripts' program, condensed.

### 4.1 Research

**Current realization: the TARA project, in this repository.** TARA combines the implicit knowledge of a research question held within an LLM with an explicit knowledge representation developed from primary sources and collected in a hypergraph data model. Research duties in the near term: the impact-investing sector survey (§3.1), user-interview synthesis, literature review of prior art (Mondragon and beyond), and the modeling groundwork for Hyphae.

### 4.2 Develop

**Current realization:** Rust code specifying a collection of systemd processes linked by a declarative NixOS configuration file. The Rust code is developed by LLMs under Nic's supervision. For the Moaiwi project, the Develop process is based on the repository at <https://codeberg.org/proletariat/fortress> and continues in that repository (reading of an ambiguous sentence in the proposal — see §8).

**Development intention:** a **multi-agent vericoding harness** that uses [Verus](https://verus-lang.github.io/) to produce formalized Rust applications. The harness will be based on existing Verus projects such as **STARverus** or **KVerus**, and will use formalized multi-agent processes as anticipated in the **Plumbing language** in `projects/knowledge-repository-poc`, but written in Verus. The point is not verification theater: it is that a configuration which must run unattended as a home server or a business server cannot afford drift, and formalized development is how a two-person cooperative can promise cloud-grade reliability.

### 4.3 Deploy

**Current realization:** essentially none yet — which is informative. PT has not deployed Fortress, so **deploying Fortress is itself the construction of the deployment meta-process**, and that meta-process is what will later deploy Moaiwi. The requirement: technology developed by PT must be reliable not only when first introduced but sufficiently flexible to grow and change as users' needs change.

**Development intention:** some sort of **digital twin technology** to automate the continued relevance and reliability of deployed systems — the twin notices when the deployed system and the users' needs have drifted apart.

### 4.4 Reflect

**Current realization: none systematically.** The intention is to use the imagination and creativity of developers *and users* to imagine a better society and how advanced technology can help bring it about. The Reflect process will transcend the current limitation of technology development in which **only engineers imagine new products**. Reflect is where the end in mind (§1) is kept alive and revisited; it is deliberately named as underdeveloped rather than skipped.

## 5. Roles and participants

- **PT (proletariat.tech)** — the workplace cooperative that develops Moaiwi and operates the Develop/Deploy meta-processes.
- **Nic Venner** — lead developer at PT (they/them); presenter and gatekeeper of the work; the person the $50,000 revenue goal sustains.
- **Brad** — builds the plan and its artifacts through the Research meta-process (TARA).
- **Rachel** — impact-fund discovery interviews, with Nic.
- **USSEN impact investors** — the initial customers; also, later, users whose imagination feeds Reflect.
- **Resist and Build (Denver 2026)** — the origin of the connections; possibly an early audience (§8).

These participants are themselves agents within the meta-process realizations; the roles above say which realizations they appear in.

## 6. How the dimensions interact

Three feedback loops carry the meta-plan:

1. **Projects develop the meta-processes.** Deploying Fortress builds Deploy; running Moaiwi's research builds Research; building Moaiwi builds Develop. The projects are the training ground for the meta-processes.
2. **Meta-processes enable projects.** Only a working deployment meta-process makes Hyphae's network pilots possible; only Research's economic modeling makes Hyphae's replacement analysis possible.
3. **Later projects answer earlier ones.** Moaiwi asks "can this cooperative build software worth paying for?"; Hyphae asks "can the network and the investors make each other more than they are alone?"; Cooptopia asks "can the whole thing scale past 5%?". Each question presupposes the last.

The higher-order character of the network is here: a network of cooperatives developed by a network of meta-processes, each made of agents exchanging resources over channels, reconfigured at each stage.

## 7. Use of this document

This meta-plan informs the development of more specific plans; it is a plan for planning. Immediate next steps: **this document is reviewed**; after revision and review, `framing-memo-v3.md` is written. The fate of the existing `research-plans/` directory (B1–B4) is **undecided** and is not settled by this document.

## 8. Conflicts and open questions (noted, not silently resolved)

1. **The conference deliverable is unaccounted for.** The v2 meta-plan organized a 30-day combined sprint ending in a 5–10 minute overview plus a brief live demo for R&B DEN-2026 contacts (~2026-11-20). The revision proposal never mentions it and describes the conference only as the *origin* of the Moaiwi product. *Conflict noted.* My inclination (open to decision): keep the overview as a **milestone within Phase M1**, not as the organizing objective of the plan. Decision needed from Brad.
2. **Organizational scheme replaces the v2 scheme.** v2 was organized as one sprint with staggered gates and a three-horizon structure; v3 is organized as three projects × four meta-processes. The 2026-10-22 locked decisions (three horizons, register, instruments, etc.) governed the v2 documents; where they conflict with this document, this document wins — e.g. the "three horizons" are not carried forward as structure (Moaiwi/Hyphae/Cooptopia replace them), while the equity-only instrument decision is consistent with what the transcripts and this plan say (impact investors provide equity capital).
3. **Fortress framing.** Earlier material described Fortress as an idea source for Moaiwi with a common core extracted — "a span in a category", Fortress and Moaiwi as legs, the common core as apex. The revision proposal supersedes this: Fortress **is the basis** for Moaiwi, one configurable codebase. The span picture may describe the eventual architecture, but the operative plan is configuration, not extraction. *(Supersession noted.)*
4. **An ambiguous sentence, interpreted.** "For the Moaiwi project, the Develop process will be based on the repository at https://codeberg.org/proletariat/fortress and will continue in this repository." I read "this repository" as the fortress repository (Develop continues there), not TARA. If TARA was meant, §4.2 changes.
5. **mycor.io vs. proletariat.tech.** Brad stated on 2026-10-22 that Nic is lead developer at Mycorrhiza Cooperative (mycor.io); the revision proposal names the developer as PT. Both statements stand in the record; this document follows the proposal (authoritative) and notes that the relationship between mycor.io and PT is unconfirmed.
6. **Transcript names.** The transcripts' working names ("Moabee", "Haifa/Haifei", "Coaptopia") are rendered here as **Moaiwi**, **Hyphae**, **Cooptopia** per the proposal. The raw transcripts remain verbatim.
7. **Phases are synthesized.** The proposal defines "phase" but does not decompose the projects; §3.1's phases and §3.2's placeholder are my synthesis and the most likely place for revision at review.
8. **Commercial form is a hypothesis.** The license/charging model in §3.1 is Nic's working inclination from MOAIWI-4, not a settled decision.

## 9. Sources

- `writing/human/moaiwi-revision-proposal.md` — authoritative directive (2026-10-24).
- `writing/human/MOAIWI-1.md`, `MOAIWI-2.md`, `MOAIWI-3.md` — financial-architecture transcripts (equity, bonds, internal/external returns, portfolio construction, Mondragon prior art).
- `writing/human/MOAIWI-4.md` — product/organization transcript (names, USSEN, $50k goal, Fortress demo, research stack, commercial form).
- `writing/human/Informatics1Readable.md` — value-theoretic grounding for the modeling (value as scalar-valued function; price-denominated data limits).
- `projects/moaiwi-network-poc/2026-10-21-moaiwi-network-poc-meta-plan.md` — the v2 meta-plan (reviewable input only).
