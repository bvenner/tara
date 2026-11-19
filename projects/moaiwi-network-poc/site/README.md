---
title: "B1 — site skeleton (static, zero-dependency; build-system decision pending)"
date: 2026-11-06
kind: options
project: moaiwi-network-poc
---

# Site skeleton — v1

*Workflow B1: "a static build (Astro/Vite, unlisted hosting, screenshot fallbacks — pending decisions, not commitments)." This skeleton is plain HTML/CSS with no build step so the content (the critical path: site, questions, demo) can start now; porting into Astro/Vite later is mechanical. Unlisted hosting TBD. All working names are placeholders — naming is delegated to collaborators and the audience. Register: plain English; no internal program vocabulary; standing disclaimer lives with any numbers (none yet).*

## Content structure (six sections, verbatim from workflow B1)

0. **What we're building** — the Fortress-based business server; demo materials; what exists today vs. what is proposed.
1. **The research stack proposal** — the expandable-subset framing: start small and real; inflatable to larger abstractions later.
2. **The questions we bring** — the mutual-education core; our open questions, stated as questions.
3. **Concepts** — the glossary in public form: credited definitions, commitments, plain-English translation.
4. **What we don't know** — explicit unknowns, honestly listed.
5. **The exchange continues** — how to reach us; what happens after the meeting; the site updates after each circle meeting.

## File map

```
site/
├── index.html          # single page, six <section>s in order above
├── style.css           # small static stylesheet (no framework)
└── README.md           # this file
```

Content sources (mirror, don't import mechanically — public register applies):

- Section 0/1: workflow §2 B1/B2 + Fortress demo status from Nic (pending).
- Section 2: `../r1/questions-v1.md` §1 (final, merged list only).
- Section 3: `../r1/impact-investing-glossary.md` columns 1/3/4 only (credited definitions with attribution links).
- Section 4: seeded from the memo's verify-flags and the demo-scope unknowns; grows deliberately (principle 4).
- Section 5: consent + contact placeholders (decide at M−10→M−5 with naming/hosting).

Standing-question affordance (B3, window M−10→M−5): a recurring marked element (CSS class `standing-question`) is pre-registered in the stylesheet; every future metric/impact figure on the site must carry an instance of it. No such figures exist yet.

## Deliberately not decided here

Build system (Astro/Vite), hosting (unlisted-inherited), domain name (naming policy), analytics (none, probably none ever), contact surface. All are M−10→M−5 work with Nic.
