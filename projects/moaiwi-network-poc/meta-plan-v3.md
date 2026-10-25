---
title: "moaiwi-network-poc meta-plan v3"
date: 2026-10-24
kind: research-plan
project: moaiwi-network-poc
---

# Meta-plan v3 — a higher-order network of workplace cooperatives

*Drafted 2026-10-24 from scratch, per `writing/human/moaiwi-revision-proposal.md` (authoritative where anything conflicts; conflicts are noted in §8). Primary sources: `writing/human/MOAIWI-{1,2,3,4}.md` and `writing/human/Informatics1Readable.md`. The previous meta-plan (now `projects/moaiwi-network-poc/2026-10-21-moaiwi-network-poc-meta-plan.md`) is reviewable input only, not a tracked baseline.*

## 1. Purpose — the end in mind

This meta-plan begins with the end in mind, taking the value of any such attempt on faith. The end is **a higher-order network of workplace cooperatives that solves the problems that defeated previous attempts to scale cooperative networks**. The meta-plan is not itself the plan of work; it is the instrument by which more specific plans will be developed. Everything below is organized so that a specific plan can be read off it: a project, a phase of that project, and the meta-processes active during that phase. *Left to research plans (Brad, 2026-10-24): the inventory of what defeated previous attempts — and what would show this attempt is not repeating those failures — is a research-plan question under §7, not a claim settled here.*

## 2. Structure: two dimensions

The meta-plan is organized in two dimensions, loosely time and space.

- **Time — projects.** The development is a series of projects. Each project is composed of sub-projects, called **phases**. The projects are **Moaiwi**, **Hyphae**, and **Cooptopia**. The ordering is one of **dependency and readiness, not sequence**: each project leans on the one before it, but the development process is **not linear and not a waterfall methodology**. Projects overlap; later projects are inhabited early (mycor.io uses the developing Hyphae product to coordinate; Moaiwi seeds Hyphae's accounting tools — §3.1–3.2); earlier projects draw on later ones as those mature. "Time" marks where each project's *center of gravity* falls, not when it starts or stops.
- **Space — meta-processes.** Running during every phase of every project are four ongoing meta-processes: **Research**, **Develop**, **Deploy**, and **Reflect** (Research is called **"Explore"** in other elaborations of the four). They always interact. They are not overhead around the "real" work; they *are* the working part of the organization, and they are themselves targets of technology development.

The success of the whole depends on the skill of the meta-processes. At any project stage, each meta-process must be realized as a collection of interacting agents — human or computational — linked together by exchange of resources over channels. The central generative capacity this plan demands is the ability to **dynamically generate realizations of the meta-processes appropriate to the project stage**.

**Naming policy (from the transcripts, MOAIWI-4).** All the project names here are working names — deliberately "meaningless collections of syllables to give the LLM a clear reference," as are the product names. The philosophy behind this is that every project needs collaborators, and letting **collaborators name the project** gives them a large stake in something whose name is ultimately meaningless for the broad success of the project: an easy way to give up nothing and have them feel very involved. Naming is therefore delegated to collaborators and the audience; no name in this document is fixed.

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

**Audience and revenue goal.** The initial target audience is impact investors in USSEN. The revenue goal is annual revenue of **$50,000**, which would sustain Nic in the continued development of this meta-plan. Meeting it may require expanding the target audience to impact investors outside formal association with USSEN. Impact investors were chosen because they are aligned with the meta-plan's longer-term goals while having sufficient economic resources to meet the revenue targets.

**The arithmetic (hypothesis, to be tested in M1 and priced in M2).** The transcripts' market sketch (MOAIWI-4): roughly **200 impact investors** in total, with warm introductions to about **20** of them — ~10% of the addressable market, which is excellent for a first client base and a problem if we ever need to be large. $50,000 across 20 clients is **$2,500 per client per year**; 5–10 clients at $5k–10k/yr hits the same target with a heavier product. Which side of that range is real is exactly what the M1 interviews and the M2 pilots decide; the number to watch in interviews is what funds currently pay for software and research support, per year.

**Two metrics, deliberately separated.** (a) *Product success* — clients paying because the tool is worth paying for, not out of goodwill (the M2 metric). (b) *Sustenance* — the run-rate that frees Nic to work on this meta-plan full-time (the M3 metric). Neither substitutes for the other: $50k from one aligned patron is not product success, and $30k with delighted, retained clients is not failure.

**The value logic.** To meet the revenue target, Moaiwi must produce sufficient value that impact investors will pay for the software. This is done by a combination of (a) **replacing existing software expenditures** and (b) **facilitating the growth of the impact investment funds**. Consequently Moaiwi must meet or exceed the reliability targets of existing cloud-based services *and* offer new features not currently accessible to impact investors. *Risk noted:* for funds of sufficient size, software spend is small relative to their budgets — and the software budgets of the impact investors in the action circle are currently unknown, so M1 must establish what they actually are. If they are small, the (a) half underdelivers on its own and the (b) growth half carries the real pitch; the interviews must weigh both halves explicitly and be willing to hear that neither is worth paying for. Candidate features are described in the transcripts — e.g. research across multiple impact-investing funds, for which at least one interlocutor's community was already considering budgeting a person (MOAIWI-4); capital allocation across a portfolio with mixed instruments and returns (MOAIWI-1–3). Further features will be identified through **user interviews, pilot demonstrations, and literature review**. A market-side research project belongs here: surveying impact investing as a sector — which funds exist, what they do, which are growing — since growth beyond the warm-introduced circle means appealing to funds outside the cooperative space (MOAIWI-4).

**Positioning (from the transcripts, MOAIWI-1).** The one identified "shiny" for drawing investors in: present this as **quantitative finance for cooperative and impact investing** — a frame that reliably draws the quantitative-finance crowd ("oh, shiny") and that maps onto what funds already know how to evaluate. How far this register is used with the action-circle audience is a Phase M1 marketing question.

**Value logic for later projects.** Beyond revenue, Moaiwi carries seeds of the later projects: the **shared accounting and management tools** it develops for impact-investing clients are the seeds of the confederation process realized in Hyphae (§3.2, three-legged stool; Brad, 2026-10-24).

**Commercial form (from the transcripts, not yet a decision).** Nic's working inclination (MOAIWI-4) is to charge for the business layer on top of the Fortress stack, offered under a strong copyleft or source-available license (GPL v3, BSL, or similar): self-hosting is free, the B2B addition is the product. This is a hypothesis to validate against the user interviews, not a locked choice.

**Phases.** The phases below are a **draft** — the revision proposal fixes the projects but not their decomposition, so this decomposition is my synthesis from the transcripts and is open to revision at review. The initial presentation Nic would give is, per MOAIWI-4, **a Fortress demo with the B2B client functionality plus a proposal for the research stack** — an expandable subset of existing functionality that can inflate up to the later mathematical abstractions — with vague long-term promises left deliberately vague.

- **Phase M1 — Ground truth and demonstration.** User interviews with USSEN-associated impact investors: back-office needs, existing tools, what they would want from a thing like this (listen to the complaints). Fortress configured as a business server, demo-ready. Sector survey of impact investing begins. **Deliverable: the presentation to the initial meeting of the newly formed action circle "Finance and Community Capital" within the Resist and Build Network** — the 5–10 minute overview with a brief live demo (~2026-11-20, date TBD), a milestone of this phase rather than the organizing objective of the plan (decided 2026-10-24; see §8.1). **The Nov 20 date is a deadline within M1, not a gate and not the end of the phase** (Brad, 2026-10-24). M1 also encompasses ongoing presentations and feedback at future meetings of the action circle — part of this phase but not yet directly specifiable, as the circle is an unfolding process. Action circles are described at <https://resistandbuild.net/>.
- **Phase M2 — Pilots and first revenue.** Pilot demonstrations with warm-introduced funds; the paid cross-fund research service; the B2B addition to the Fortress stack sold as replacing existing software spend. Success metric (product success, §3.1): clients paying because the tool is worth paying for, not out of goodwill. Pricing is set here against what the M1 interviews found funds actually pay.
- **Phase M3 — Sustainability and expansion.** Annual revenue at or above $50,000 — the sustenance metric (§3.1), held separate from product success. Expansion of the audience beyond USSEN association as needed. By the end of this phase Nic is sustained by the product, which is the condition for the rest of this meta-plan. **Includes the impact-measurement research sub-project** (Brad, 2026-10-24): measuring environmental, social, and financial impact — the currency of Hyphae's three-legged stool (§3.2) — is a potential research sub-project here, informing the development of tools within Moaiwi. It is placed in M3 as premature to specify earlier; its plan is deliberately vague until its dependencies resolve (see §7).

### 3.2 Project 2 — Hyphae: technology for a confederation of workplace cooperatives

**What it is.** Technology to facilitate a **confederation of workplace cooperatives**, working name **Hyphae**. Hyphae would allow greater cooperation between impact investors and cooperative networks: impact investors provide much-needed **equity capital** to cooperative networks; cooperative networks provide **measurable environmental, social, and financial impacts** that attract additional impact investors.

**How it would work.** Hyphae uses advanced modeling and analysis approaches to identify opportunities to develop a workplace cooperative that would provide a good or service that grows the cooperative network. It is grounded in a model of **the local economy and the cooperative network itself**. The operative move is **replacement**: a good or service currently procured in the conventional economy by cooperatives or their members is replaced by one provided by a cooperative in the network — and the replacement must **increase environmental, social, and/or financial value**. Done well, Hyphae develops a **synergy between investors and cooperators greater than either could achieve alone**. (The word "measurable" in the paragraph above is the load-bearing one: impact measurement is treated as a research sub-project under Moaiwi Phase M3 — §3.1.)

**The three-legged stool.** Hyphae realizes a "three-legged stool" of **impact investors**, **cooperative networks**, and **technology developers** — each leg itself a confederation. **mycor.io** is the working name for a confederation of technology-worker cooperatives, the technology-developers leg, and plays a foundational role (Brad, 2026-10-24). Hyphae is the coordination technology among the three legs. Mycor.io will "eat its own dogfood" to the extent possible, using the developing Hyphae product to coordinate between them. The Hyphae development process is facilitated by the **Moaiwi product**, which contains the seeds of the confederation process by developing **shared accounting and management tools** for impact-investing clients.

**Contrast with prior art.** Mondragon started with an investment and brought investing in early; this program brings investing in later, on top of a network (MOAIWI-4). The financial mechanics the transcripts work out — non-voting equity shares, internal vs. external rates of return, buy-out of external investors, bonds vs. equity and their failure modes, portfolio construction with treasuries to hit blended returns (MOAIWI-1–3) — are the design space Hyphae's modeling has to formalize. The value-theoretic grounding for the modeling (value as a scalar-valued secondary function; the limits of price-denominated data; the internal chart of accounts) is in `writing/human/Informatics1Readable.md`.

**Phases.** Not yet decomposed. Hyphae's center of gravity falls after Moaiwi is on solid footing (Phase M3), because it needs both the deployed infrastructure and the investor relationships — though the dogfooding loop of the three-legged stool (above) puts parts of Hyphae in motion earlier, while it is still being developed. A first phase will most plausibly be a **model**, not software: the local-economy-and-network model on which everything else is grounded.

**A candidate research project: the vericoding harness.** The Develop-evolution example of §4.2 — a multi-agent [Verus](https://verus-lang.github.io/) vericoding harness based on **STARverus** or **KVerus**, with **Plumbing**-style formalized multi-agent processes (`projects/knowledge-repository-poc`) written in Verus — is placed here as a research project under Hyphae (Brad, 2026-10-24), whose implicit goal is to **recruit a larger development team**. It is aspiration, not critical path: Moaiwi's phases do not depend on it.

### 3.3 Project 3 — Cooptopia: past the growth limits of the cooperative economy

**What it is.** Technology to facilitate the growth of the cooperative economy **past the current limits to its growth**. Even where cooperative networks have substantial presence — the Mondragon Corporation is the canonical case — such networks rarely exceed **~5% of total economic flows**. The working hypothesis is that these limits are not inherent to the cooperative economy but are limitations of **productive, organizational, and information technology**. The working name is **Cooptopia**.

**Status: research-only.** Because Cooptopia depends on Hyphae, it is premature to develop specific project goals. For now it is a research-only project: the 5%-ceiling hypothesis gets investigated (prior art: Mondragon and the literature on it; category-theoretic and network formulations), and nothing is promised beyond that.

## 4. The meta-processes (space dimension)

Each meta-process runs in every phase of every project, always interacting with the others. Each is also a target of technology development: the projects can only be executed as well as the meta-processes are skilled. **A meta-process is itself a process, but it is abstract: it is not intended to be directly realized.** It is realized at each phase of each project as a concrete process — the Develop meta-process, say, is realized as that phase's *development* process — and each realization is a collection of **interacting agents (human or computational) linked by exchange of resources over channels**, dynamically generated as the project stage changes (Brad, 2026-10-24). Current realizations and development intentions follow; these too are the transcripts' program, condensed.

### 4.1 Research

**Current realization: the TARA project, in this repository.** TARA combines the implicit knowledge of a research question held within an LLM with an explicit knowledge representation developed from primary sources and collected in a hypergraph data model. Research duties in the near term: the impact-investing sector survey (§3.1), user-interview synthesis, literature review of prior art (Mondragon and beyond), and the modeling groundwork for Hyphae.

**Plans belong to Research.** Plans developed under this meta-plan fall under the Research meta-process (called **"Explore"** in other elaborations of the four meta-processes); gates and failure modes are more appropriately placed in plans of the Develop and Deploy meta-processes (Brad, 2026-10-24). Accordingly, one way to resolve the placement problem: **this meta-plan is part of the present realization of the explicit specification of the Research process** — it belongs to TARA's explicit knowledge representation and is maintained there.

**Development intention:** **meta-plans for Develop, Deploy, and Reflect** are themselves potential targets of a research project. Implementing this requires revisiting the current TARA architecture as a realization of the Research meta-process and aligning it with **repositories for Develop, Deploy, and Reflect that have yet to be created** (Brad, 2026-10-24).

### 4.2 Develop

**Current realization:** Rust code specifying a collection of systemd processes linked by a declarative NixOS configuration file. The Rust code is developed by LLMs under Nic's supervision. For the Moaiwi project, the Develop process is based on the repository at <https://codeberg.org/proletariat/fortress> and continues in that repository (Brad confirms: "this repository" = the fortress repository; see §8.4). Its task there is to develop the home-network server and the business server **from the same code base**, through a configuration process made sufficiently flexible for both (Brad, 2026-10-24; see §8.3).

**Development intention:** the Develop process evolves toward **formalized development** — multi-agent processes producing verified software — so that a configuration which must run unattended as a home server or a business server can promise cloud-grade reliability without drift. *Example, not a commitment* (kept explicitly marked because future planning agents may find a concrete picture valuable; Brad, 2026-10-24): one such evolution would be a **multi-agent vericoding harness** using [Verus](https://verus-lang.github.io/) to produce formalized Rust applications, based on existing Verus projects such as **STARverus** or **KVerus**, with the formalized multi-agent processes anticipated in the **Plumbing language** (`projects/knowledge-repository-poc`) written in Verus. The specific route belongs to a research project under Hyphae (§3.2), not to this meta-plan.

### 4.3 Deploy

**Current realization:** essentially none yet — which is informative. PT has not deployed Fortress, so **deploying Fortress is itself the construction of the deployment meta-process**, and that meta-process is what will later deploy Moaiwi. The requirement: technology developed by PT must be reliable not only when first introduced but sufficiently flexible to grow and change as users' needs change.

**Development intention:** the Deploy process evolves toward **automated stewardship of deployed systems** — reliability not only at introduction but continuing as users' needs change. *Example, not a commitment* (kept marked for the same reason as the Develop example, §4.2): **digital-twin technology** — a maintained model of each deployed system together with its users' needs, which notices when the two have drifted apart and automates the maintenance of continued relevance and reliability. The specific route belongs to a future **Deploy meta-plan/repository** (§4.1), not to this meta-plan.

### 4.4 Reflect

**Current realization: this drafting process.** The systems literature is weak on where Reflect (however named) belongs in the cycle: some formulations of the four-stage process place Reflect at the beginning, some at the end (Brad, 2026-10-24).

> *Every new beginning comes from some other beginning's end.* — Semisonic, "Closing Time"

One way to resolve the ambiguity: **the current drafting process is itself a realization of the Reflect meta-process, and this meta-plan is a product of the realized process** — which places Reflect as the **first step** in the cycle. (The lyric above is the ambiguity in one line: placed at the end of a cycle, Reflect is already the beginning of the next.) Beyond this realization, Reflect is not yet systematically developed. The intention is to use the imagination and creativity of developers *and users* to imagine a better society and how advanced technology can help bring it about. The Reflect process will transcend the current limitation of technology development in which **only engineers imagine new products**. Reflect is where the end in mind (§1) is kept alive and revisited.

**Development intention:** a potential research project is to **flesh out the four meta-processes by reviewing the relevant systems literature** (Brad, 2026-10-24) — which would also settle Reflect's placement in the cycle and the naming variants ("Explore" for Research, §2), and specify how Reflect is realized in phases other than this one.

## 5. Roles and participants

- **PT (proletariat.tech)** — the workplace cooperative that develops Moaiwi and operates the Develop/Deploy meta-processes.
- **mycor.io** — working name for a **confederation of technology-worker cooperatives**; the technology-developers leg of Hyphae's three-legged stool (§3.2). It eats its own dogfood by using the developing Hyphae product to coordinate the three legs.
- **Nic Venner** — lead developer at PT (they/them); presenter and gatekeeper of the work; the person the $50,000 revenue goal sustains.
- **Brad** — builds the plan and its artifacts through the Research meta-process (TARA).
- **Rachel** — impact-fund discovery interviews, with Nic.
- **USSEN impact investors** — the initial customers; also, later, users whose imagination feeds Reflect.
- **Resist and Build (Denver 2026)** — the origin of the connections; the audience for the Phase M1 presentation is the initial meeting of the R&B Network's newly formed **"Finance and Community Capital" action circle**, with ongoing updates anticipated at later meetings (§3.1).

These participants are themselves agents within the meta-process realizations; the roles above say which realizations they appear in.

## 6. How the dimensions interact

Three feedback loops carry the meta-plan:

1. **Projects develop the meta-processes.** Deploying Fortress builds Deploy; running Moaiwi's research builds Research; building Moaiwi builds Develop. The projects are the training ground for the meta-processes.
2. **Meta-processes enable projects.** Only a working deployment meta-process makes Hyphae's network pilots possible; only Research's economic modeling makes Hyphae's replacement analysis possible.
3. **Later projects answer earlier ones.** Moaiwi asks "can this cooperative build software worth paying for?"; Hyphae asks "can the network and the investors make each other more than they are alone?"; Cooptopia asks "can the whole thing scale past 5%?". Each question presupposes the one before it — and loops 1 and 2 make the dependency mutual, not one-way.

The higher-order character of the network is here: a network of cooperatives developed by a network of meta-processes, each made of agents exchanging resources over channels, reconfigured at each stage. The loops are also the reason the time dimension is a dependency ordering and not a schedule — this plan does not commit to a waterfall or any other linear methodology.

## 7. Use of this document

This meta-plan informs the development of more specific plans; it is a plan for planning. Plans developed under it are products of the **Research** meta-process (called "Explore" in other elaborations; §4.1), and this document is itself part of the present realization of Research's explicit specification. *(Update 2026-10-24: research plans are developed in `projects/moaiwi-research-program/` — clean-sheet files keyed to the research question, one directory per question; the existing `research-plans/` (B1–B4) are retained as history.)*

**Requirements on plans developed under this meta-plan.** Each such plan must state: the question it will answer or the decision it will inform; what it expects to produce; what resources and access it needs; what would count as an answer or closure; and where its results are recorded. *Scope note:* gates and failure-mode machinery are properly the business of plans under the **Develop** and **Deploy** meta-processes — their meta-plans do not yet exist (§4.1) — and are deliberately not imported here.

**How (sub-)project plans are developed.** Because every phase incorporates all four meta-processes (§2, §4), a plan for a phase or sub-project must include a **specific specification of how the meta-processes interact** in that phase — how the realizations hand resources to one another and what each produces for the others. The detail level is expected to track dependency resolution: **M1 can be specified concretely now; M3 stays vague until its dependencies resolve** (Brad, 2026-10-24) — premature precision on later phases is worse than acknowledged vagueness. Development is therefore incremental: read off this meta-plan as project → phase → meta-process realization, specify what is resolvable, and mark the rest as pending.

Immediate next steps: **this document is revised and reviewed**; after revision and review, `framing-memo-v3.md` is written. The fate of the existing `research-plans/` directory (B1–B4) is **undecided** and is not settled by this document.

## 8. Conflicts and open questions (noted, not silently resolved)

1. **The conference deliverable is unaccounted for.** The v2 meta-plan organized a 30-day combined sprint ending in a 5–10 minute overview plus a brief live demo for R&B DEN-2026 contacts (~2026-11-20). The revision proposal never mentions it and describes the conference only as the *origin* of the Moaiwi product. *Conflict noted.* **Resolved 2026-10-24 (Brad):** the overview is a **milestone within Phase M1**, not the organizing objective of the plan. The presentation is to the **initial meeting of the newly formed "Finance and Community Capital" action circle** within the Resist and Build Network (action circles: <https://resistandbuild.net/>); ongoing updates at later circle meetings are anticipated, as the process is still unfolding (see §3.1). The ~Nov 20 date is a **deadline within M1, not a gate and not the end of the phase**; ongoing presentations and feedback at future circle meetings belong to M1 but cannot yet be directly specified.
2. **Organizational scheme replaces the v2 scheme.** v2 was organized as one sprint with staggered gates and a three-horizon structure; v3 is organized as three projects × four meta-processes. The 2026-10-22 locked decisions (three horizons, register, instruments, etc.) governed the v2 documents; where they conflict with this document, this document wins — e.g. the "three horizons" are not carried forward as structure (Moaiwi/Hyphae/Cooptopia replace them), while the equity-only instrument decision is consistent with what the transcripts and this plan say (impact investors provide equity capital).
3. **Fortress framing.** Earlier material described Fortress as an idea source for Moaiwi with a common core extracted — "a span in a category", Fortress and Moaiwi as legs, the common core as apex. The revision proposal supersedes this: Fortress **is the basis** for Moaiwi, one configurable codebase. **Resolved 2026-10-24 (Brad):** the *current* Develop process develops the home server and the business server **from the same code base**, via a sufficiently flexible configuration process — the configuration route is not a prelude to extracting a common core, and the span picture is not the operative architecture.
4. **An ambiguous sentence, interpreted.** "For the Moaiwi project, the Develop process will be based on the repository at https://codeberg.org/proletariat/fortress and will continue in this repository." **Resolved 2026-10-24 (Brad):** "this repository" means the fortress repository — the interpretation §4.2 carries is correct.
5. **mycor.io vs. proletariat.tech.** Brad stated on 2026-10-22 that Nic is lead developer at Mycorrhiza Cooperative (mycor.io); the revision proposal names the developer as PT. **Resolved 2026-10-24 (Brad):** mycor.io is the working name for a **confederation of technology-worker cooperatives** — not a name for PT. It is the technology-developers leg of Hyphae's "three-legged stool" (impact investors, cooperative networks, technology developers), each leg a confederation; it uses the developing Hyphae product to coordinate the legs, and the Hyphae **development process** (the Develop meta-process realized in that project — the meta-processes are abstract and never directly realized, see §4) is facilitated by Moaiwi's shared accounting and management tools for impact-investing clients (see §3.2). The 2026-10-22 "lead developer at Mycorrhiza Cooperative" statement is thereby superseded.
6. **Transcript names.** The transcripts' working names ("Moabee", "Haifa/Haifei", "Coaptopia") are rendered here as **Moaiwi**, **Hyphae**, **Cooptopia** per the proposal. The raw transcripts remain verbatim. The naming philosophy behind all of these throwaway names is recorded in §2 (naming policy).
7. **Phases are synthesized.** The proposal defines "phase" but does not decompose the projects; §3.1's phases and §3.2's placeholder are my synthesis and the most likely place for revision at review.
8. **Commercial form is a hypothesis.** The license/charging model in §3.1 is Nic's working inclination from MOAIWI-4, not a settled decision.

## 9. Sources

- `writing/human/moaiwi-revision-proposal.md` — authoritative directive (2026-10-24).
- `writing/human/MOAIWI-1.md`, `MOAIWI-2.md`, `MOAIWI-3.md` — financial-architecture transcripts (equity, bonds, internal/external returns, portfolio construction, Mondragon prior art).
- `writing/human/MOAIWI-4.md` — product/organization transcript (names, USSEN, $50k goal, Fortress demo, research stack, commercial form).
- `writing/human/Informatics1Readable.md` — value-theoretic grounding for the modeling (value as scalar-valued function; price-denominated data limits).
- `projects/moaiwi-network-poc/2026-10-21-moaiwi-network-poc-meta-plan.md` — the v2 meta-plan (reviewable input only).
