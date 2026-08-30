# Informatics1 — Readable Research Notes

**Source:** `writing/human/Informatics1.txt` (raw transcript, 683 lines), recorded as a conversation while gardening.
**Date:** session ~Aug 23, 2026 (file timestamps).
**Participants (mapped):**
- **Nicole** (= `SPEAKER_00`) — the researcher (TSSI/RET project).
- **Brad** (= `SPEAKER_01`) — physicist; familiar with TSSI literature, non-equilibrium thermodynamics, Metabolism of Cities.

**Formatting conventions used here:**
- Dialogue wording is preserved as close to verbatim as possible, with transcript fillers (`uh`, `um`, false starts, backchannel "yeah/right") trimmed where they carry no content.
- All garden/weeding chatter (peas, bindweed, towel, hats) has been **stripped**.
- Editorial annotations are given in blockquotes like this one.
- **Errata are applied inline and flagged** (notably the unemployment-mortality figure, below).

---

## 1. The value/transformation problem as a data-limitation problem

**Nicole:** My critique of the value problem, or of the transformation problem, is that it's a limitation of the kind of data you get for disciplines — a limitation on the data that you can actually measure. On a broad level in the economy, hypothetically you even have individual investor reports. Do economics professionals ever aggregate these investor reports into data? My understanding of most economics professionals — and this isn't necessarily a knock on them — is that they will just use the aggregated statistics provided to them by the Fed and other things.

**Brad:** Most economics has almost nothing to do with accounting, and they use completely different mathematical approaches. It's almost like they wouldn't even know what to do with accounting data, because it's so far from their usual understanding of what they're doing, which is this kind of weird econophysics thing.

**Nicole:** Notice that all of this data is in the form of monetary value and monetary prices. GDP is also in the form of prices, because it's the amount of goods transacted times the price for each good. So fundamentally, everything is price-valued at some point in time. All the numbers are in dollars and they're price-valued — they're valued on the price of something.

> **Editorial note.** This opening sets up the paper's core premise: *all measurable economic data is price-denominated*, so any theory that ingests only such data is structurally constrained. Note the immediate concession that this "isn't necessarily a knock" on economists — the limitation is in the data, not the practitioners.

---

## 2. Value as a scalar-valued function; the energy/entropy analogy

**Nicole:** Fundamentally, the thing that value proposes is that value is a secondary functor/function that's scalar-valued.

**Brad:** You can kind of think of it as the relationship between energy and entropy. You've got two scalar-valued, quasi-conserved functions. You do have energy conserved, but that means you get changes in entropy.

**Nicole:** Fun fact: entropy also isn't scalar-valued, which is weird in and of itself.

**Brad:** That proposal says you're going to have to do some non-trivial things with entropy. Do you want to extend the project?

> **Editorial note.** The "entropy isn't scalar-valued" remark anticipates the program's convention that "entropy" means *convex Lyapunov structure*, not thermodynamic entropy (see `program/research-program.md` §3). Brad's "do you want to extend the project?" is a direct hook into extending the RET framework's entropy construct.

---

## 3. The physics disanalogy: Lagrangians only work because physics has non-energy observables

**Nicole:** I think the physics is kind of a bad example here with how powerful Lagrangians are. In physics, you can figure out every observable aspect of a system by studying how one scalar variable interacts with the rest of it. But ultimately, that's also because physics has observables that are not energy. In physics you can measure the energy of an electron, not just the energy of an entire system. The economic equivalent would be if there were no measurement devices except an "energy-o-meter" that tells you the energy in a one-by-one-meter cube of space. Even if that volume were arbitrarily tiny, that would not be enough to let you do modern physics.

> **Editorial note.** This is the key disanalogy argument: Lagrangian/energy methods in physics succeed *because* energy is not the only observable. Economics lacks the analogue of "the energy of an electron" — every observable is price-like at the whole-system level. This motivates the search for observables that are *not* price.
> *Nicole's Note: This analogy is actually significantly stronger then I stated in this conversation. Taking a regular lagrangian in physics as an example, even though the system takes a single quantity like action and looks for paths that minimize/extermize said quantity. But in order to actually calculate this quantity and figure out the action you need to calculate the action given the exact rules of the physics in the system, you need so much more information then a single scalar quantity. For example in a super simple 1 particle dirac system you have 4 complex numbers of phase information that you need to know at every single point, and if you don't have some way of actually knowing these values, the lagrange tells you jack shit about how the system evolves. (This gets even worse as you add even more particles, where the extra data at every single point grows faster then C^(4^P) where P is your number of particles.)*
---

## 4. Value has the same type as price ⇒ conservation of information

**Nicole:** Because that's actually all that you have, you're kind of proposing the existence of an alternative scalar quantity that is not price. You're proposing an economic measurement that is not price, but also has the same type as price — scalar-valued, applicable to all objects. They're both intensive variables, exactly. And they also kind of exist on everything. Everything has a certain value. According to the labor theory of value, every single commodity that has a price also has a value.

The argument is that because you can only ever take prices into your theory, anything that is of the same type as a price is just going to look like some kind of thing done to a price. If you say "that's value," it's like, "oh well, that's just measuring price in a different way," or "that's price multiplied by 2," or "that's price after it goes through these seven different functions." You're not actually learning anything new by studying value — which is correct, but that's also because… At some point, Marxist economists just have to give up this point: that you can't actually learn anything by studying what value is, because your only inputs to economic models kind of have to be prices, just because those are the inputs that have been available. But this is also such a huge level of missing the point.

There's not an understanding that marginalists will admit labor value exists. Could you measure the value? Is every quantity associated with it…

**Brad:** In the TSSI literature it's called MELT — the monetary expression of labor time — which is kind of an intensive–extensive relationship, time being extensive. Labor time is an extensive variable, and its monetary expression is an intensive variable. You can translate between prices and this extensive variable of value — the amount of labor time you put in — through the vehicle of MELT. So you get quantity of labor multiplied by MELT, and that gives you the quantity of money. So value, in terms of how much labor goes into something, is related — like any two quantities — by a price.

**Nicole:** It is related by a price, but then there's the other thing: if you're just studying the behavior of prices, why aren't you studying the behavior of prices?

**Brad:** I think the fixation on prices is kind of related to… their models are actually flows of quantity.

**Nicole:** That's the marginalist critique — if you're studying prices indirectly, why not study prices directly?

> **Editorial note.** The "conservation of information" argument is the intellectual spine of the whole transcript: *a scalar-valued, intensive, universal quantity that enters through price-only data cannot produce information not already in the prices.* Brad's MELT interjection is the escape hatch — MELT is an explicit intensive–extensive conversion constant that lets value be measured *as labor time* (an extensive variable) rather than as a transform of price. This is exactly the TSSI bridge that `findings.md` formalizes.

---

## 5. Non-equilibrium formulation: capital flows as state variables

**Brad:** What's interesting about the proposal that the banker came up with is that it connects very closely to this problem of investment. It's got capital flows as kind of one of the main things in its non-equilibrium formulation. The whole point of formulating in these things is to actually bring in flows that aren't just completely scalar values of some other gradient. So you're already kind of ahead of the game.

That notion of flows between sectors — investment flows, capital flows between sectors — is actually something you're starting with as a state variable, rather than something that's derived from prices. If you follow this non-equilibrium formulation, it's kind of an interesting place to be, because now you're looking at: how do these capital flows change? You could actually think of it as a state variable. You could even think of doing measurements on that — some sort of integrated measure of how much capital is flowing from sector to sector. If you had sectors and regions, then it could be a little bit different.

**Nicole:** That in and of itself is a very interesting thing to think about. You kind of know that these sectors exist a priori. The sector-based analysis is also very interesting, because it also breaks down the data. But my argument is that this is also to some degree proving my point — because why can you do the sector-based analysis? Why did they choose to represent this as "you have these sectors where the traditional economic rules happen"?

**Brad:** The reason why you've got sectors is because those could be commodities in classic formulations. Sometimes they formulate them as sectors because people know that these high-level aggregates don't make sense as individual commodities. So now you've got an n-dimensional space where those n dimensions are your sectors. Instead of physical dimensions, you've got sectoral dimensions. The dimension of your problem is the number of sectors.

> **Editorial note.** This is the RET project's core move as stated in conversation: capital flows enter as *state variables*, not as derived price transforms. Brad confirms the natural reading — the state space dimension is the number of sectors (or commodities in classical formulations). 

---

## 6. Sector data and EIN codes: the cynical view, and the enrichment argument

**Nicole:** My response to that would be a lot more cynical. If you look at the data provided by FRED and company — in addition to providing earnings and GDP breakdowns by sector, or aggregates for the whole entire economy — every single company, when it submits its forms, has to submit a couple of forms: what was your total revenue, total sales, total earnings, et cetera. They also have this category they submit for tax purposes, which is a three-digit code that corresponds to what your company specializes in making. Because reporting that honestly gets you tax breaks, companies are incentivized to report them, which means that organizations like FRED can actually break down and do these kind of large aggregate statistics based on sectors.

But my response to this would be: that is not necessarily a theory of what the data actually is.

The transformation problem is fundamentally an underspecified thing. If all you're looking at is prices, then any output is going to be mathematical manipulations on prices — it is not going to contain new information that was not contained in the prices. If all of your study of the labor theory of value is dictated based on market prices, you are not going to get any information that you could not get by analyzing those market prices directly. It's kind of just a very basic conservation of information problem.

But there is also a secondary part of this, which is why I think that's clever: you can also take those EIN (actually NAICS) sector codes and use them to actually enrich the data on your theory. You essentially have a finite set combined with the sector analysis stuff, and that can let you do very interesting things. That's part of my response to why non-equilibrium thermodynamics is the economic model that is pursued and has literature written about it.

> **Editorial note.** The three-digit code is the NAICS code (Nicole says "EIN," mixing it with the Employer Identification Number). Key mechanism: *honest self-reporting is tax-advantaged*, so the sectoral decomposition is incentive-compatible data — it exists because firms are paid to report truthfully. This is offered as the data-side justification for sector-structured RET models. The cynicism: this tells you the *source* of sector data (incentives), not that sectors are a natural theoretical object.

---

## 7. Why non-equilibrium thermodynamics: processes on networks

**Brad:** One reason to do non-equilibrium thermodynamics is that if you want to look at the physics of processes on networks, that's where that's being studied right now. You can take some non-trivial results from physical processes on networks and say, what's the analogy with economic networks? I totally agree with you that connecting this to the metabolism revival project is the key thing. This was mostly a test — could the clanker actually come up with anything?

> **Editorial note.** "The banker" and "the clanker" are the LLM. Brad frames the whole RET program here as a transfer of results from network thermodynamics into economics, with the metabolism project (of islands/cities) as the empirical anchor. The transcript immediately segues into the AI/class-struggle tangent below; the research thread resumes with TSSI's time structure.

---

## 8. Tangent: AI, class struggle, and "His Master's Tools"

**Brad:** If you can actually get it to do important problems in Marxian economics, then aren't you heading towards the ability to actually implement socialism? It's a race. It's class struggle.

**Nicole:** It continues to be class struggle. If it's a race, we're also definitely losing. The only reason you were able to get those results with an LLM is because I specifically told you: here's an open-source provider, here's how you do it cheaply, here's the state-of-the-art model that came out a couple of weeks ago, and here's a service that lets you get ten times your input token price — it multiplies by 60 the amount of money you're spending on the model, just because hyperscalers are giving away money. Most of the leftists engaged in AI see it as an evil demon technology, because it is an evil demon technology, and choose to not engage with it. That means they do not get the power of said evil demon technology. But it can't be "because I have harnessed the power of the demons, I will be able to use it effectively against the demon army." The demon army is using it more effectively than we are.

**Brad:** This is why there's a really good book that I have not read — called *His Master's Tools* — which is about how socialists can use finance to work for socialism.

> **Editorial note.** Political tangent; retained for the record. "His Master's Tools" = the finance-for-socialism argument (likely referencing *His Master's Tools?* — not to be confused with Audre Lorde's "master's tools" essay; verify title before citing).
> Nicole Note: The master's tools quote comes from this absolutely fantastic andre lorde essay: 

> Those of us who stand outside the circle of this society’s definition of acceptable women; those of us who have been forged in the crucibles of difference—those of us who are poor, who are lesbians, who are Black, who are older—know that survival is not an academic skill. It is learning how to take our differences and make them strengths. For the master’s tools will never dismantle the master’s house. They may allow us temporarily to beat him at his own game, but they will never enable us to bring about genuine change. And this fact is only threatening to those women who still define the master’s house as their only source of support. 

> And I think that the there is always some degree of a dialectic between needing to use the techinques of the master to aqquire power and defeat them, while at the same time rejecting the tools so you do not accept the ideology inherent in said tools. (Funny Sidenote: This dillema is totally inherent to all the factions of Men in LOTR fighting over the one ring and the palantiri). But the original quote is helpful here since its explicitly denouncing something closer to lean in feminism as opposed to violent action against capital.


---

## 9. TSSI's time structure: production takes time; simultaneity is endogenous

**Brad:** The basic formulation is that production processes take time, and that you buy the inputs at one time and you sell the outputs at a later time, and those don't necessarily have the same price, because prices change. It's kind of a really basic thing. And the simultaneity stuff is also super endogenous in economics itself, because it is based upon thermodynamics and little modest extensions to thermodynamics.

> **Editorial note.** Direct statement of TSSI's temporal structure — inputs and outputs priced at different times — and a claim that "simultaneist" economics inherits its simultaneity assumption from thermodynamics. This is a condensed version of the program's temporalist-vs-simultaneist distinction; see `program/research-program.md` Track A.

---

## 10. The core hypothesis: available data determines the theory

**Nicole:** One of my big hypotheses for the metabolism of islands project is that the data that you have available to economically reason about determines what economic models you come up with, in a very basic way.

**Brad:** And that was what was known as science for a long time, until the economics came along and said we don't need that now. The idea that empirics should receive theory is kind of what most people think of as scientific philosophy. I totally am not disagreeing with that, but I do think that these two projects are related.

> **Editorial note.** This is the transcript's central methodological thesis: *measurement constrains theory*. Brad's gloss ("empirics should receive theory") ties it to the standard view of scientific method and flags the two projects (RET + metabolism) as two applications of the same principle.

---

## 11. Marginalism and Keynesianism as data-poor theories

**Nicole:** Traditional marginalism essentially says: we only have data about macroeconomic prices, so we're just going to try to figure out how to balance those prices. You even have all of Keynesianism, which is literally built on two scalar functions over time — how do you manage two scalar functions over time? That's all of Keynesianism, with absolutely no concept of value whatsoever.

> **Editorial note.** The "two scalar functions" of Keynesianism are presumably output (Y) and employment/interest rate dynamics — i.e., a 2-dimensional scalar theory. The point parallels §1: marginalism and Keynesianism are theories whose *shape* was fixed by the poverty of price-only, aggregate data.

---

## 12. The ML analogy: more measurement ⇒ better model

**Nicole:** My thinking about this is that the shape of your economic theory is determined by what you can measure, and the more you can measure, the more sophisticated and better the economic model will tend to model the actual system itself. Very machine-learning the way — if you want to get a lower loss, you train on more training data. You have marginalism, which is just essentially taking in certain bare-minimum price models, and then you have this non-equilibrium thermodynamics discipline, which is using the fact that you actually have extra richness in these aggregated factors.

> **Editorial note.** The training-data analogy is the positive side of the conservation-of-information argument: enrichment of inputs (sector codes, flows, non-price quantities) is what buys model sophistication. This frames the entire program as a data problem rather than a theory problem.

---

## 13. Non-equilibrium thermodynamics is a physical theory with a domain of validity

**Brad:** Non-equilibrium thermodynamics is a physical theory whose data is gotten from physical experiments, and it is used to describe systems where classical things break down. And that tends to be things where your characteristic scale length is closer to your continuum approximation length. It's kind of used in very specific domains of physics, and oftentimes, because they're the easiest ones to study, on human-built systems — polymers, nanoelectronics, things where conventional physics or conventional equilibrium doesn't work as well.

The idea of using that framework in economics to continue sort of the physics-ness of economics — that's a particular choice. By choosing this research topic, I'm not even saying that should be the choice. I'm more saying: if you're trying to get a master's degree in a field that's pretty well explored, you can borrow a lot of existing results from one domain to the other, which is one way to make rapid progress.

**Nicole:** I don't think coming up with a completely de novo approach to economics is valuable.

> **Editorial note.** Important scope-limitation caveat: RET is *not* being claimed as the uniquely correct framework — it is chosen for (a) its natural fit with flow/network phenomena and (b) the transferability of mature results (the master's-degree pragmatics). Nicole's agreement confirms the pragmatic framing: borrowing existing results beats de novo theorizing.

---

## 14. The transformer analogy: model complexity is not tied to system complexity

**Nicole:** There's this impression that the more complicated the thing you're trying to model, the more complicated your statistical model of the thing must be. I think what's interesting about machine learning is that it kind of shows to some extent that that is not true. The best model we have of all human language as a statistical model — the description of the architecture — can fit in seven pages. The model itself cannot fit in seven pages, but importantly, it doesn't necessarily matter that the transformer is capturing a lot of what makes human language valuable. What actually matters is that it works at the scale that you're trying to make it. Any model of human language that has a hundred billion free parameters and is trained on a hundred trillion token inputs, and that you can actually numerically solve for, is going to be almost as good as a transformer.

**Brad:** If transformers learn, stochastic gradient descent is a pretty important technique. There is a model of learning that comes from statistics that's basically used in machine learning — which is why it was statistical learning theory for a long time. But again, a lot of those basic ideas come from statistical physics. Statistical physics got there first, almost always. Modern Bayesian statistics, of which machine learning was an initial parasite, was all stolen from physics.

> **Editorial note.** Two distinct points folded together: (1) the *architecture* description of a transformer fits in seven pages (scaling hypothesis — model class matters less than scale + data); (2) the underlying statistical ideas were anticipated by statistical physics. The second point is the program's intellectual genealogy in miniature: physics → statistics → ML.

---

## 15. Granular economic data is hiding in plain sight — in the LLM's weights

**Nicole:** Right now you have a statistical model that models the distribution of human language, which is the most powerful statistical model ever, the most complicated statistical model ever created. A lot of the machine learning field and lots of stuff about the economy is trapped up in the distribution of human language — or, as the kids would say, in unstructured data.

**Brad:** It's only because you could, in theory, get access to the entire Visa transaction data, or supplement that with all the bank transactions and get close to 95% of the total flows of money in the economy, with some ability to label the different inputs and outputs that are in those transactions. The reason you don't have that is because capitalism has made that data inaccessible. And the use of privacy is oftentimes where the crime is hidden — if you're going to kill someone, don't kill them right out in the open; do it inside.

> **Editorial note.** The key empirical claim of the LLM era: the most complete granular dataset on how the economy actually runs is already encoded in a large model's weights (as trained on the entire written corpus). The transcript later quantifies this as "at least 100 gigabytes" (§20). Brad's point: transaction-level data exists but is privately held, and privacy is systematically used to hide the flows that matter.

---

## 16. Investment for well-being; capital flows "closed under a bunch of different laws"

**Brad:** The whole goal is to invest for well-being. Anything else you do needs to be a sub-goal. Your objective might be considerably more concrete, but your goal is always to ask: how do we weaken the notion of investment for profit — or, in these non-equilibrium frameworks, the flow of capital — and how do we replace that with some other thing?

If you show that these flows of capital are closed under a bunch of different laws, you can start saying: well, maybe we don't need to necessarily have markets allocate those flows of capital. Just including flows of capital in your model from the beginning.

> **Editorial note.** This is the normative payoff of the RET formulation: *if capital flows are provably governed by conservation/closure laws, market allocation becomes an optional coordination mechanism rather than a necessity.* The "closure" language is a direct import of conservation-law structure into economics — the normative core that the TSSI correspondence (`findings.md`) is meant to ground.

---

## 17. Why care about the economy: it represents something real

**Nicole:** The main reason I am interested in economic modeling is not actually because an economic model is an interesting thing. There's this thing called the economy, which exists in this abstract space, and this abstract space has these rules that behave about it. It's made of symbols in the same way that the number three does not exist on the blackboard.

**Brad:** I think now you're substituting the symbolic register of business processes for the actual processes. Business processes are creating the things of value that humans need to survive, all the time. Those things can also be produced without business processes — like this work in our garden, which technically is not really a business process, as indicated by the fact that I'm doing it on a Saturday where I'm not working for money. When small communities produced everything that they needed, say in the hunter-gatherer phase, you didn't have anything called the economy.

**Nicole:** You didn't have anything called the economy. But the economy, I would argue, was kind of a very classic hyperstition. There are a lot of economists who would say in some way that all of humanity is a computer, and this computer is currently running a physics simulation, and this physics simulation obeys these concrete rules the exact same way that you would expect physics in the real world to behave — and those are the laws that we try to uncover.

But one of the things I'm unsatisfied with is that economists never take it as a matter of fact — I don't care about the economy — or I care about the economy because of what it represents. Economists care about the economy because, oh, a 1% drop in unemployment is really bad. I care about the 1% drop in unemployment because if unemployment rises by 1%, a large number of people die. Actually, in the U.S. it was approximated as: a 1% increase in the unemployment rate for three years results in around 40,000 extra deaths.

> **Editorial note — erratum.** The transcript says "67,000 extra deaths" (and earlier "hundreds of thousands"); the figure most commonly cited for a 1-percentage-point rise in US unemployment is on the order of ~40,000 excess deaths, and it originates in older (Brenner-style) rule-of-thumb estimates. The ~40k figure is a widely repeated rule of thumb rather than a settled consensus; modern meta-analyses (e.g., Roelfs et al. 2011, "Losing Life and Livelihood," *Social Science & Medicine*) report elevated all-cause mortality risk for the unemployed at the individual level without endorsing a fixed population-level death count. Cite the popular source with that caveat if it appears in writing. (Popular reference: https://factually.co/fact-checks/economy/unemployment-increase-deaths-40000-correlation-ccf3c6)

**Brad:** [Discussion of Gaza/Israel excess-mortality analogy, omitted — political tangent, no research content.]

---

## 18. The layers of abstraction; what a socialist economy actually replaces

**Nicole:** The whole point of socialists is to eventually replace the system with something better. In a world where you are organizing production not based on markets but based on some other thing, how would that work?

**Brad:** But that some other thing is still going to be a symbol — or a system of symbols.

**Nicole:** You can think of the economy as existing in layers of abstraction. You have the raw physical production processes themselves. Then you have the firms and markets that coordinate those raw production processes. Then you have interactions between firms that cause a bunch of things. Then you have state regulation that exists on top of that. Then you have very large markets — the global US market for labor in a very abstract way. Then you also have all of these bickering groups between different groups of capital at the very top that kind of control everything. And you can argue that the political system is the thing that exists at the highest level of hierarchy and is determined by every single thing below it.

The problem with economic models is that the only thing that actually stays the same — most of what's staying the same — is the underlying production processes themselves. If you're trying to build a good socialist system, you're trying to figure out what abstractions — what is the second organizational layer you build on top of the raw production processes that results in the most well-being, because you can't really change the raw production processes. Just saying "change the raw production processes" is not economic management — that's technological development. But you can change the social organizations that determine what forms of production actually get made.

The worry about this is that thermodynamics doesn't necessarily tell you about how gluon fields interact with each other in a non-abelian way. Lots of economic theories are so high up from the production processes that they, in some sense, tell you actually no information about the production processes themselves. It's very hard to think about how to organize production processes if all of your theories are completely indifferent as to what the production processes actually are. If you're actually trying to run an economic model, you need one that measures a real social system down to a very high granular level of detail.

> **Editorial note.** This is the "granularity" argument: theory high above the production processes is information-poor about them. The political-system-as-highest-layer claim, determined by everything below it, is a functionalist reading of the state. The practical upshot: socialism is a question of choosing the *coordination layer*, not the physical production layer. This is the transcript's clearest statement of the normative motivation for the whole program.

---

## 19. High-fidelity production models as a necessary condition

**Brad:** I think it's very concrete: you're leading back into something like a super high-fidelity model of the production process as a necessary condition. It's probably not sufficient, but it seems like a necessary condition. I do think that social metabolism and other outgrowths of ecological economics are way more interested in the physical world than traditional economics, and I think that's a good place to start.

> **Editorial note.** Brad assigns the Metabolism projects their precise methodological role: *a necessary, not sufficient, condition* for the normative program. This frames the two projects' relationship — metabolism supplies the physical granularity; RET supplies the formal closure structure.

---

## 20. The LLM as a granular economic dataset; Metabolism of Cities/Islands

**Nicole:** My approach to this is: what data are you getting? You're mining the weights of a trillion-parameter model — you have terabytes of data in Kimi K3 about lots of things, but in there there's probably at least 100 gigabytes about how exactly the economy works, at a very granular level. It's both intentionally kept as a state secret and kept as a private secret. But you have lots of data about how the economy works at a granular level — I'm not necessarily saying it'll be at the full digital-twin level; it'll probably be a little bit slightly higher.

**Brad:** You're going to have different levels of fidelity in your local digital twin. The spatial built-environment stuff will be pretty high fidelity. But even if you have super high-fidelity models of your distribution network, you're not necessarily going to have super high-fidelity models of your flows on that.

**Nicole:** You can also just use those constraints, along with the general constraints of language and of the economy that exist in your very large LLM, to actually get reasonable guesses of what those production processes should look like. That's an input to your data process. In some sense, you're filling in the data with the fact that you have this massive model that encompasses all of human knowledge.

**Brad:** The Metabolism of Islands project is going to be a combination of a lot of different models. Some of them are going to be the static-topology type — buildings and such, which are pretty well possible to capture — and then there's a lot of things that are going to be flows underneath that are very hard to observe. There's a whole parallel project called Metabolism of Cities that you should definitely check out, because I kind of think doing both at the same time makes the most sense. Since you live in Denver, you can work on that there, and since Elena will be in Hawaii for at least a while, you can work on that one too. Islands have really natural closure laws — and custom checkpoints — so you can totally keep track of material flows in an island in a way that's really hard to do for a city.

**Nicole:** If you're looking at a West African bar and grill, you know where that's physically based. There's some set of Gaussians around there that correspond to what a house is, to what a restaurant is. You know the land value and what property tax they pay. Other than that, you know essentially nothing. But you also know that as a business they have two locations — that's information you can find on the internet. Assuming the restaurant is doing decently profitably, you can probably figure out how much revenue it's making every year, how much it costs to make every single year, and then what it's making. You're going to be off, but you're not going to be off by more than a factor of 10 in each direction.

**Brad:** You do have Epstein-style opacity, where the opacity is intentionally done to destroy that link between a real-world asset and who owns it. Governments are going to largely agree with the private sector's assessment of their need for privacy, because that's how the whole system works. The lack of transparency is a feature, not a bug. This was my big conclusion from the Excel stuff — they are so committed to making it seem like there's some really important privacy rule here that should not be violated, it's practically a natural law.

> **Editorial note.** The practical data strategy: combine (a) static spatial/tax data (high fidelity), (b) LLM-prior guesses for unobservable flows (order-of-magnitude), and (c) the natural closure/checkpoint structure of islands for validation. The "Gaussians" remark anticipates using the model's spatial/topological priors to constrain what a given physical footprint can be. The opacity remark frames privacy as the mechanism hiding flows — data's "feature, not a bug."

---

## 21. You'll end up in agent-based modeling; data before formalism

**Brad:** A more accurate physical digital twin with a less accurate economic flow model helps, because you can come up with constraints. But I still feel like it's ultimately still agent-based modeling — and maybe that's where you and I differ. I kind of feel like you're going to end up in agent-based modeling no matter what. That's why looking for places where you actually can develop a mathematical formalism is important, even though the details are going to be provided.

**Nicole:** The more I think about the mathematical formalisms for this, the more I would really like to have the data and see what kind of shape the data takes before I try to figure out how I should model it.

> **Editorial note.** The methodological fork in the road, stated explicitly: Brad anticipates that any real digital twin collapses into agent-based simulation, which is precisely why he values the RET formalism — as the place where analytic structure can still be imposed. Nicole's reply is the data-first position: obtain the data, observe its shape, then choose the formalism. This is an open tension the program must resolve (see `program/research-program.md`).

---

## 22. The Marxian audience; non-equilibrium economics as unfinished business

**Nicole:** Even working within the Marxian tradition means your audience is incredibly tiny. You could argue, why would I want to work in Marxian economics, when there's like 35 people in the world that care about it? But I always feel like right now those 35 people probably deserve to have their interests and various fixations pursued. Just because it's a small group does not necessarily mean it's not a worthwhile pursuit.

**Brad:** The thing I like about non-equilibrium thermodynamics is that you are working with expressions of physical constraints in the real world. There's a line in a book I really liked: because non-equilibrium economics aims to model the behavior of all macroscopic physical systems, it will never be finished. It's not that there's some final theory that's going to describe all of matter — it has this incredibly efficient…

**Nicole:** My issue with non-equilibrium thermodynamics, to the extent that I have one, is that it works a lot better as a theory when your constraints on your system are not hundreds of gigabytes. There's a part of me that feels like it's going to end up being a little bit more MLE — we're probably going to have tens of gigabytes of data constraints, at least like 10 to 100,000 [dimensions/variables]. So you're kind of already in the semi-MLE zone, or at least in the era of graph and database — things that take graph and database searches as their model primitives.

**Brad:** I totally agree, and I'm not even suggesting this is the best direction. But it seems like low-lying fruit — this is out there, and there are things you could say about Marxian economics that are non-trivial. It's still important, so it still seems like a good thing to have the clanker work on.

> **Editorial note.** Two opposed characterizations of the RET program sit side by side: Brad's "models all macroscopic physical systems, never finished" (universalist, physics-first) versus Nicole's "works best when your constraints are not hundreds of gigabytes" (data-first, MLE/graph-flavored). The unresolved question — is RET a universal formalism or a data-regime-dependent special case? — is the live tension of the whole conversation.

---

## 23. The LLM era raises the bar: originality and marginal value of model output

**Nicole:** In the age of LLMs, there's a good example in gaming. There was once a time when making a really quick demo in 3DJS about a walkable environment where you could fly a plane was kind of an impressive thing — you could put that on your resume and people would find it quite impressive. Now it's a thing that any second grader can do with ChatGPT. The bar for originality — what people will find interesting — has gone up with that. Just because it's a thing a clanker can do easily kind of means that what people expect a product to look like has increased in scope.

If you're thinking about marginalism, the marginal value of any clanker output is zero — clanker outputs are essentially free. There are ways you can make it actually hard — you can expand your scope. Expanding your scope is very possible, and maybe even a good thing.

**Brad:** First-principling stuff in the LLM era is increasingly easy, and it's possible that you can just strike out on your own.

**Nicole:** One of the things we can do is finish this conversation, plug it into the chat, and then Kimi can let us know all of the citations, all the literature that we missed, instead of just free-balling it. It's definitely possible to be randomly bullshitting with your friends around a campfire at night, record that conversation, and instantly get teleported to the academic literature that is talking about the thing you're talking about. So we can try that.

> **Editorial note.** Closing meta-point: in the LLM era the *marginal value of model output is zero* (it's free), so value shifts to (a) originality/scope and (b) the ability to route raw conversation into the literature automatically. The intended workflow — record conversation → LLM → citations — is the natural read of this very file's purpose.

---

## Summary: the transcript's argument chain

1. All measurable economic data is **price-denominated** (§1).
2. Value is a **scalar-valued, intensive, universal** quantity — same type as price (§2, §4).
3. Same-type inputs ⇒ any derived quantity is a **manipulation of price**; no new information (conservation of information) (§4).
4. MELT provides the **intensive–extensive bridge** that lets value be measured as labor time, not as a price transform (§4).
5. The RET formulation upgrades **capital flows to state variables**, and the sector structure gives the state space its **dimensions** (§5).
6. Sector data is **incentive-compatible** (tax breaks for honest NAICS reporting) — it exists because firms are paid to report truthfully (§6).
7. **Data determines theory**: marginalism/Keynesianism are data-poor; enriched data enables richer models (§10–§12).
8. RET is chosen **pragmatically** (network physics, transferable results), not as the uniquely true framework (§13).
9. The LLM contains a **granular economic dataset** in its weights; islands/cities provide closure for validation (§15, §20).
10. Normative payoff: if capital flows are **closed under laws**, market allocation becomes optional (§16), and socialism is the choice of the **coordination layer** above invariant production processes (§18).
11. Open tension: **universal RET formalism vs. data-first MLE/graph practice** (§21–§22); resolve after seeing the data.

---
