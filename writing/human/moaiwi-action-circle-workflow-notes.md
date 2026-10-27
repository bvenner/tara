# Brad's notes on the R.1 action-circle workflow (2026-10-25)

*Moved verbatim from `projects/moaiwi-network-poc/action-circle-workflow-2026-10-25.md` on 2026-10-26 at Brad's request, so the workflow document can be rewritten around them. The text below is unchanged. Decisions taken in response are recorded in the workflow document's revision record (2026-10-26); the research topic they generated is T18 "neurosymbolic knowledge engineering" in `projects/moaiwi-research-program/research-topics-v3.md`.*

## Making the glossary more conventional

I think the glossary is a good idea, but I think we should attempt to phrase it as closely as possible with conventional software engineering terms. I'm worried that the Castoriadis vocabulary could be off-putting for Nic & Rachel and the investors. So I think preliminary work on the mapping between Castoriadis' philosophical terms and more conventional systems/software engineering language would be valuable. For example, the difficulty of translating vague user needs into potentially formalizable requirements is the domain of requirements engineering in both systems and software engineering. We should leverage Castoriadis for critique of conventional approaches rather than adopting his terminology in it's entirety. This may require research work on Research Topic T13, appropriately modified so that Castoriadis' terms are also investigated.

## Surveying existing impact investing software

I don't see an attempt to survey the software that impact investors are actually using. This may be a very hard target and only obtainable in interviews, but I would like to make an effort to survey what is on the web as long as it's reasonably low cost (say an LLM budget of $20). This could be folded into the "language acquisition" phase but is probably worth identifying explicitly.

## Use of the current research process

The language acquisition process is clearly an instance of the Research meta-process. I don't see an explicit attempt to use the hypergraph in TARA to synthesize and develop the glossary. This may be a limitation in the current TARA realization, which was developed for the academic literature. I don't think adding this capability would be too hard for you to implement. I'd also like to think about how the hypergraph could be used to develop a "lower-order" structure like a glossary (or more formally an ontology). Are there tools in the higher-order network world that have already been developed to transform an arbitrary hypergraph into a lower-order graph? Is there any overlap with "defunctionalization", which transforms higher-order functions into a lower-order execution environment?

## Alternative approaches to knowledge aquisition

Is there anything to learn from the Elenchus system for generating knowledge bases, as developed in the paper by Bradley Allen at https://arxiv.org/pdf/2603.06974 and the system developed at https://github.com/bradleypallen/elenchus ? Although this is framed as a dialogue between a single user and an LLM, could it be extended to our situation to formulate a dialogue between two expert domains (impact investing and software engineering)? The paper states:

> The meaning of a sentence is given by its inferential role: what it follows from, what follows from it, and what it is incompatible with.

This is very close to the pre-condition/post-condition/invariant structure of Hoare logic and progeny that is implemented in tools like Verus.

The paper provides a case study in using the tool to for ontology engineering by developing a "material base" (defined in the paper).
