> OpenAlex full text (2026-08-23) — source: https://arxiv.org/pdf/1505.07835
> DOI: https://doi.org/10.1088/1751-8113/49/14/143001 · license: — · status: hybrid
# The role of quantum information in thermodynamics—a topical review

**Authors:** John Goold, Marcus Huber, Arnau Riera, Lídia del Rio, Paul Skrzypczyk
**Journal of Physics A Mathematical and Theoretical** · 2016
**DOI:** https://doi.org/10.1088/1751-8113/49/14/143001

## The role of quantum information in thermodynamics - a topical review

John Goold, 1 Marcus Huber, 2, 3, 4 Arnau Riera, 4 L´ ıdia del Rio, 5 and Paul Skrzypczyk 4, 5

1 The Abdus Salam International Centre for Theoretical Physics (ICTP), Trieste, Italy 2 Group of Applied Physics, University of Geneva, 1211 Geneva 4, Switzerland 3 Universitat Autonoma de Barcelona, 08193 Bellaterra, Barcelona, Spain 4 ICFO-Institut de Ciencies Fotoniques, The Barcelona Institute of Science and Technology, 08860 Castelldefels (Barcelona), Spain 5 H. H. Wills Physics Laboratory, University of Bristol, Bristol BS8 1TL, United Kingdom (Dated: August 29, 2016)

This topical review article gives an overview of the interplay between quantum information theory and thermodynamics of quantum systems. We focus on several trending topics including the foundations of statistical mechanics, resource theories, entanglement in thermodynamic settings, fluctuation theorems and thermal machines. This is not a comprehensive review of the diverse field of quantum thermodynamics; rather, it is a convenient entry point for the thermo-curious information theorist. Furthermore this review should facilitate the unification and understanding of different interdisciplinary approaches emerging in research groups around the world.

| CONTENTS                                                                                   |       | B. Correlations and entanglement in a thermodynamic background                           | 18    |
|--------------------------------------------------------------------------------------------|-------|------------------------------------------------------------------------------------------|-------|
| I. Introduction                                                                            | 2     | C. Thermodynamics under locality restrictions D. Entanglement resources in thermodynamic | 19    |
| Scope and other reviews                                                                    | 4     | tasks                                                                                    | 19    |
| II. Foundations of statistical mechanics                                                   | 5     | E. Using thermodynamics to reveal quantumness                                            | 20    |
| A. Equal a priori probabilities postulate as a consequence of typicality in Hilbert spaces | 5     | F. Outlook                                                                               | 20    |
| B. Equilibration. Maximum entropy principle from quantum dynamics                          | 6     | V. Quantum Fluctuation relations and quantum information                                 | 20    |
| C. Thermalization. Emergence of Gibbs states                                               |       | A. Introduction                                                                          | 20    |
| in local Hamiltonians D. Equilibration times                                               | 8     | B. Phase estimation schemes for extraction of quantum work and heat statistics           | 22    |
| E. Outlook                                                                                 | 9 9   | C. Fluctuation relations with feedback,                                                  |       |
|                                                                                            | 10    | measurement and CPTP maps                                                                | 22    |
| III. Resource theories                                                                     |       | D. Entropy production, relative entropy and                                              |       |
| A. Models for thermodynamics                                                               |       | correlations                                                                             | 23    |
| 1. Noisy and unital operations                                                             | 10 10 | E. Outlook                                                                               | 23    |
| 2. Thermal operations                                                                      | 11    | VI. Quantum Thermal Machines                                                             | 24    |
| 3. Gibbs-preserving maps                                                                   | 11    | A. Absorption refrigerators                                                              | 24    |
| 4. Coherence 5. Catalysts                                                                  | 11 12 | 1. Stationary behaviour                                                                  | 25    |
|                                                                                            |       | 2. Transient behaviour                                                                   | 26    |
| 6. Clocks                                                                                  | 13    | B. Reservoir engineering                                                                 |       |
| 7. Free states and passivity                                                               | 13    | C. Quantum thermodynamic signatures                                                      | 27 28 |
| 8. Different baths                                                                         | 14    | D. Stationary entanglement                                                               | 29    |
| 9. Finite-size effects                                                                     | 14    |                                                                                          |       |
| 10. Single-shot regime                                                                     | 14    | E. Outlook                                                                               | 29    |
| 11. Definitions of work                                                                    | 14    | VII. Final Remarks                                                                       | 29    |
| B. Generalizing resource theories                                                          | 15    |                                                                                          |       |
| 1. Starting from the pre-order                                                             |       |                                                                                          |       |
| 2. Starting from the set of free resources                                                 | 15 15 | Author contributions                                                                     | 30    |
| 3. In category theory                                                                      | 15    | Acknowledgements                                                                         | 30    |
| 4. Resource theories of knowledge C. Outlook                                               | 16 16 | References                                                                               | 30    |
| IV. Entanglement theory in thermodynamic settings                                          | 17    |                                                                                          |       |
| A. Correlations and entanglement under entropic restrictions                               | 17    |                                                                                          |       |

## I. INTRODUCTION

If physical theories were people, thermodynamics would be the village witch. Over the course of three centuries, she smiled quietly as other theories rose and withered, surviving major revolutions in physics, like the advent of general relativity and quantum mechanics. The other theories find her somewhat odd, somehow different in nature from the rest, yet everyone comes to her for advice, and no-one dares to contradict her. Einstein, for instance, called her 'the only physical theory of universal content, which I am convinced, that within the framework of applicability of its basic concepts will never be overthrown.'

Her power and resilience lay mostly on her frank intentions: thermodynamics has never claimed to be a means to understand the mysteries of the natural world, but rather a path towards efficient exploitation of said world. She tells us how to make the most of some resources, like a hot gas or a magnetized metal, to achieve specific goals, be them moving a train or formatting a hard drive. Her universality comes from the fact that she does not try to understand the microscopic details of particular systems. Instead, she only cares to identify which operations are easy and hard to implement in those systems, and which resources are freely available to an experimenter, in order to quantify the cost of state transformations. Although it may stand out within physics, this operational approach can be found in branches of computer science, economics and mathematics, and it plays a central role in quantum information theory-which is arguably why quantum information, a toddler among physical theories, is bringing so much to thermodynamics.

In the early twentieth century, information theory was constructed as the epitome of detachment from physics [7]. Its basic premise was that we could think of information independently of its physical support: a message in a bottle, a bit string and a sensitive phone call could all be treated in the same way. This level of abstraction was not originally conceived for its elegance; rather, it emerged as the natural way to address very earthly questions, such as 'can I reliably send a message through a noisy line?' and 'how much space do I need to store a picture?'. In trying to quantify the resources required by those tasks (for example, the number of uses of the noisy channel, or of memory bits), it soon became clear that the relevant quantities were variations of what is now generally known as entropy [8]. Entropy measures quantify our uncertainty about events: they can tell us how likely we are to guess the outcome of a coin toss, or the content of a message, given some side knowledge we might have. As such, they depend only on probability distributions over those events, and not on their actual content (when computing the odds, is does not matter whether they apply to a coin toss or to a horse race). Information theory has been greatly successful in this approach, and is used in fields from file compression to practical cryptography and channel coding [8].

But as it turned out, not all information was created equal. If we zoom in and try to encode information in the tiniest support possible, say the spin of an electron, we face some of the perplexing aspects of quantum physics: we can write in any real number, but it is only possible to read one bit out, we cannot copy information, and we find correlations that cannot be explained by local theories. In short, we could not simply apply the old information theory to tasks involving quantum particles, and the scattered study of quirky quantum effects soon evolved into the fully-fledged discipline of quantum information theory [9]. Today we see quantum theory as a generalization of classical probability theory, with density matrices replacing probability distributions, measurements taking the place of events, and quantum entropy measures to characterize operational tasks [10].

While quantum information theory has helped us understand the nature of the quantum world, its practical applications are not as well spread as for its classical counterpart. Technology is simply not there yet-not at the point where we may craft, transport and preserve all the quantum states necessary in a large scale. These technical limitations, together with a desire to pin down exactly what makes quantum special, gave rise to resource theories within quantum information, for instance theories of entanglement [13]. There, the rough premise is that entangled states are useful for many interesting tasks (like secret key sharing), but distributing entanglement over two or more agents by transporting quantum particles over a distance is hard, as there are always losses in the process [14]. Therefore, all entangled states become a precious resource, and we study how to distill entanglement from them using only a set of allowed operations, which are deemed to be easier to implement-most notoriously, local operations and classical communication [15].

Other resource theories started to emerge within quantum information-purity and asymmetry have also been framed as resources under different sets of constraints-and this way of thinking quickly spread among the quantum information community (see Ref. [16] for a review). As many of its members have a background in physics and an appetite for abstraction, it was a natural step for them to approach thermodynamics with such a framework in mind. Their results strengthen thermodynamics, not only by extending her range of applicability to small quantum systems, but also by revisiting her fundamental principles. The resource theory approach to thermodynamics is reviewed in Section III.

Each resource theory explores the limitations imposed by one specific physical constraint, like locality or energy conservation. In a realistic setting we could be bound to several of these constraints, a natural case that can be modelled by combining different resource theories, thus restricting the set of allowed operations. In Section IV we review and discuss attempts to combine thermodynamic and locality constraints. In particular, we look at the role of entanglement resources in thermodynamic

## FIG. 1: Maxwell's demon

<!-- image -->

An early puzzle in thermodynamics: imagine a box filled with a gas, with a partition in the middle. An agent (the demon) who can observe the microscopic details of the gas particles, controls a small gate in the partition, selectively opening it to let slow particles flow to the left and fast ones to the right. This creates a temperature differential between the two sides. The demon can exploit this difference to extract work, by letting the hot gas on the right expand. This apparent contradiction with the second law of thermodynamics can be easily explained from an information-theoretical viewpoint. The demon had access to much more information than the standard observer assumed in the derivation of traditional thermodynamics, who can only read a few macroscopic parameters of a gas and assumes a uniform distribution over all compatible micro-states. Therefore, it seems natural that the demon may extract more work than predicted by standard thermodynamics-and this insight motivates the need for thinking of thermodynamics as a subjective resource theory, and extending it to the quantum regime. In the larger picture, Bennett showed that the amount of work needed to erase the demon's memory at the end of the procedure (or equivalently, to prepare the memory to store the necessary information on the particles in the beginning) precisely makes up for the work extracted [1]. For reviews, see [2-6].

tasks, thermodynamic witnesses of non-classicality, and entanglement witnesses in phase transitions.

Information theory also shed light on fundamental issues in statistical mechanics - the mathematical backbone of thermodynamics. Perhaps one of the earliest significant contributions is the maximal entropy principle introduced by Jaynes [17, 18]. In these seminal works Jaynes addresses the issue of justifying the methods of statistical mechanics from microscopic mechanical laws (classical or quantum) using tools from information theory. In fact, deriving statistical mechanics, and hence thermodynamics from quantum mechanics is almost as old as quantum mechanics itself starting with the work of von Neumann [11, 19]. This is still very much and ongoing and active research area and in recent years has received significant attention from the quantum information community. The most significant contributions are reviewed in Section II.

In the past twenty years, the field of non-equilibrium statistical mechanics has seen a rapid development in the treatments of driven classical and quantum systems beyond the linear response regime. This has culminated in the discovery of various fluctuation theorems which relate equilibrium thermodynamic quantities to non-equilibrium ones, and led to a revision on how we understand the thermodynamics of systems far from equilibrium [20-24]. Although this approach is relatively recent from a statistical physics perspective, a crossfertilisation with concepts ubiquitous in quantum information theory has already started, including phase estimation techniques for extraction of work and heat statistics and feedback fluctuation theorems for Maxwell's demons. In Section V we identify these existing relationships and review areas where more overlap could be developed.

As ideas and concepts emerge and develop it is not surprising that quantum information theorists have started to turn towards the pragmatic goal of describing the advantages and disadvantages of machines which operate at and below the quantum threshold. Although ideas relating quantum engines have been around now for a surprising long time [25-27] - questions pertaining to the intrinsic quantumness in the functioning of such machines have been raised using the tools of quantum information theory only relatively recently. We review progress along these lines in Section VI. In summary, we will review landmark and recent articles in quantum thermodynamics, discuss different approaches and models, and peek

## FIG. 2: The thermodynamic origin of the von Neumann entropy

<!-- image -->

In 1932, von Neumann designed this thought experiment to determine the entropy of a density operator ρ [11]. The experiment accounts for the work cost of erasing the state of a gas of n atoms, initially in an ensemble ρ ⊗ n , with ρ = ∑ k p k | φ k 〉 〈 φ k | , by transforming it into a pure state | φ 1 〉 ⊗ n by means of a reversible process. It consists of 3 steps: 1. Separation of the species : the atoms in different states | φ 1 〉 ,. . . , | φ m 〉 inside a box of volume V are separated in different boxes of the same volume V by means of semi-permeable walls (from a to b and finally c). Note that no work has been done and no heat has been exchanged. 2. Compression : every gas | φ k 〉 is isothermally compressed to a volume V k = p k V (from c to d). The mechanical work done in that process is W k = np k ln( V k /V ) = p k ln p k . The total entropy increase per particle of that process is ∆ S = ∑ k p k ln p k . 3. Unitary transformation : every gas is put in the | φ 1 〉 state by applying different unitary transformations | φ k 〉 → | φ 1 〉 , which are taken for free (from d to e). As the entropy of the final state is zero, the entropy of the initial ensemble reads S ( ρ ) = -Tr( ρ ln ρ ).

Historically, it is remarkable that the Shannon entropy, which can be seen as a particular case of the von Neumann entropy for classical ensembles, was not introduced until 1948 [7], and Landauer's principle was proposed only in 1961 [12].

into future directions of the field.

## SCOPE AND OTHER REVIEWS

This review focuses on landmark and recent articles in the field of quantum thermodynamics with a special emphasis on contributions from quantum information theory. We place emphasis on current trending topics, discuss different approaches and models and peek into the future directions of the field. As the review is 'topical', we intend to focus our attention on the interplay of quantum information and thermodynamics and we have written such that interested readers from different communities will get a detailed overview of how their respective techniques have been successfully applied to provide a deeper understanding of the field.

As the vastness of possible topics could easily exceed the scope of a topical review, we refer to other review articles and books concerning questions that have already been covered by other authors:

- Equilibration and thermalization. Recovering statistical mechanics from the unitary evolution of a closed quantum system is an issue which is almost as old as quantum mechanics itself. This topic, far from being an academic issue, has seen an unprecedented revival of interest due mainly to advances in experimental ultra-cold atoms. We discus the topic in Section II, from a quantum information perspective. This topic is more extensively reviewed in Ref. [28]. For readers interested in this topic from a condensed matter perspective we recommend the review [29] and the special issue [30] for more recent developments.
- Thermal machines. As mentioned in the introduction viewing engine cycles from a fully quantum mechanical perspective is also not a new topic [2527]. Many results on quantum engines exist which are not directly related to quantum information processing we exclude them from Section VI and the interested reader may learn more in Refs. [3133].

- Maxwell's demon and Landauer's principle. Almost as old as thermodynamics itself is the Maxwell's demon paradox, briefly introduced in Figure 1 and Example 3. The demon paradox inspired the seminal work of Szilard to reformulate the demon as a binary decision problem [34]. The resolution of Maxwell demon paradox by Landauer cements the relationship between the physical and information theoretical worlds. This demon has been extensively investigated from both a quantum and classical perspective in Refs. [2-6].
- Quantum thermodynamics. The 2009 book [35] covers a range of topics regarding the emergence of thermodynamic behaviour in composite quantum systems.
- Entanglement and phase transitions in condensed matter. Entanglement is frequently used as an indicator of quantum phase transitions in condensed matter systems. We do not cover this particular setting but the interested reader may find a comprehensive review in Ref. [36].
- Resource theories. Examples and common features of resource theories (beyond quantum information theory) are discussed in Ref. [37]. In particular, different approaches to general frameworks are discussed in Section 10 of that work.
- Experimental implementations. Experiments with demons, thermal engines and work extraction are discussed in more depth in the perspective article [38].

## Definitions and notation

Conventions followed unless otherwise stated: States. Discrete Hilbert spaces ❈ d . States ρ are represented by Hermitian matrices (Tr( ρ ) = 1 and ρ ≥ 0). Subsystems are denoted by Roman subscripts, ρ A := Tr B ( ρ AB ).

Entropy. Von Neumann entropy with base 2 logarithm, S ( ρ ) = -Tr( ρ log 2 ( ρ )).

Mutual information. Measures correlations, I ( A : B ) ρ := S ( ρ A ) + S ( ρ B ) -S ( ρ AB ).

Energy. Hamiltonian H , average energy 〈 H 〉 ρ = Tr( ρH ), eigenvalues { E k } k , eigenvectors {| E k 〉} k , or { ∣ ∣ E i k 〉 } k,i if there are degeneracies, with energy projectors Π k = ∑ i ∣ ∣ E i k 〉 〈 E i k ∣ ∣ .

Thermal states. Gibbs state τ ( β ) = e -βH Z , with partition function Z = Tr( e -βH ) and inverse temperature β := 1 k B T .

Free energy. F β ( ρ ) := 〈 H 〉 ρ -1 ln(2) β S ( ρ ).

Linbladian. L ( ρ ) generates Markovian, timehomogeneous, non-unitary dynamics.

## II. FOUNDATIONS OF STATISTICAL MECHANICS

At first sight, thermodynamics and quantum theory are incompatible. While thermodynamics and statistical mechanics state that the entropy of the universe as a whole is a monotonically increasing quantity, according to quantum theory the entropy of the universe is constant since it evolves unitarily. This leads us to the question of to which extent the methods of statistical physics can be justified from the microscopic theory of quantum mechanics and both theories can be made compatible. Unlike classical mechanics, quantum mechanics has a way to circumvent this paradox: entanglement . We observe entropy to grow in physical systems because they are entangled with the rest of the universe. In this section we review the progress made on this topic in recent years which show that equilibration and thermalization are intrinsic to quantum theory.

## A. Equal a priori probabilities postulate as a consequence of typicality in Hilbert spaces

Let us consider a closed system that evolves in time restricted to some global constraint. The principle of equal a priori probabilities states that, at equilibrium, the system is equally likely to be found in any of its accessible states. This assumption lies at the heart of statistical mechanics since it allows for the computation of equilibrium expectation values by performing averages on the phase space. However, there is no reason in the laws of mechanics (and quantum mechanics) to suggest that the system explores its set of accessible states uniformly. Therefore, the equal a priori probabilities principle has to be put in by hand.

One of the main insights from the field of quantum information theory to statistical mechanics is the substitution of the Equal a priori probabilities postulate by the use of typicality arguments [39, 40]. To be more precise, let us consider a quantum system described by a Hilbert space H S ⊗H B where H S contains the degrees of freedom that are experimentally accessible and H B the ones that are not. In practice, we think of S as a subsystem that we can access, and B as its environment (sometimes called the bath). Concerning the global constraint, in classical mechanics, it is defined by the constants of motion of the system. In quantum mechanics, we model the restriction as a subspace H R ⊆ H S ⊗H B . Let us denote by d R , d S and d B the dimensions of the Hilbert spaces H R , H S and H B respectively.

The equal a priori probability principle would describe the equilibrium state as

<!-- formula-not-decoded -->

and would imply the state of the subsystem S to be

<!-- formula-not-decoded -->

In Ref. [39] it is shown that, if we look only at the subsystem S , most of the states in H R are indistinguishable from the equal a priori probability state, i. e. for most | ψ 〉 ∈ H R , Tr B | ψ 〉 〈 ψ | ≈ Ω S . More explicitly, if | ψ 〉 is randomly chosen in H R according to the uniform distribution given by the Haar measure, then the probability that Tr B | ψ 〉 〈 ψ | can be distinguished from Ω S decreases exponentially with the dimension of H R , d R

<!-- formula-not-decoded -->

where C is a constant and ‖·‖ 1 is the trace norm. The trace norm ‖ ρ -σ ‖ 1 measures the physical distinguishability between the states ρ and σ in the sense that a ‖ ρ -σ ‖ 1 = sup O ≤ ✶ | Tr( Oρ ) -Tr( Oσ ) | , where the maximization is made over all the observables O with operator norm bounded by 1. The proof of Eq. (3) relies upon concentration of measure and in particular on Levy's Lemma (see Ref. [39] for details). Let us mention that ideas in this spirit can be already found in S. Lloyd's Ph.D. thesis [41] published in 1991. In particular, he presents bounds on how the expectation values of a fixed operator taken over random pure states of a restricted subspace fluctuate.

The weakness of the previous result lies in that the use of typicality is made in the whole subspace H R and, as we will justify next, this is not a physical assumption. In nature, Hamiltonians have local interactions and systems evolve for times that are much smaller than the age of the universe. Most states in the Hilbert space simply cannot be generated by evolving an initial product state under an arbitrary time-dependent local Hamiltonian in a time that scales polynomially in the system size [42]. Therefore, sampling uniformly from the whole Hilbert space is not physically meaningful. There has been a strong effort to generalize the concept of typicality for different sets of states [43-45].

The first 'realistic' set of states in which typicality was studied was the set of matrix product states (MPS) [46, 47]. These type of states have been proven to describe ground states of one-dimensional gapped Hamiltonians. They are characterized by the rank of a bipartition of the state. This parameter quantifies the maximum entanglement between partitions of an MPS. The MPSs with fixed rank form a set of states with an efficient classical representation (they only require polynomial resources in the number of particles). In Ref. [43], it is proven that typicality occurs for the expectation value of subsystems observables when the rank of the MPS scales polynomially with the size of the system with a power greater than 2.

Another set recently considered in the literature has been the so called set of physical states which consists of all states that can be produced by evolving an initial product state with a local Hamiltonian for a time polynomial in the number of particles n . By Trotter decomposing the Hamiltonian, such a set can be proven to be equivalent to the set of local random quantum circuits , that is, quantum circuits of qubits composed of polynomially many nearest neighbour two-qubit gates [42]. In Ref. [48], it was shown that the local random quantum circuits form an approximate unitary 2-design, i. e. that random circuits of only polynomial length will approximate the first and second moments of the Haar distribution. In Ref. [44] the previous work was extended to poly( n )-designs. Finally, let us mention that the entanglement properties of typical physical states were studied in Ref. [45].

Let us mention that k -designs also appear naturally in the context of decoupling theorems in which a the subsystem S undergoes a physical evolution separated from the environment B , and one wonders under what conditions this evolution destroys all initial correlations between S and B . In particular, in Ref. [49] it is shown that almost-2-designs decouple the subsystem S from B independently of B 's size.

Another objection against typicality is that there are many physically interesting systems, e. g. integrable models, which, although their initial state belongs to a certain restricted subspace H R , their expectation values differ from the completely mixed state in R , ε R , as expected from typicality arguments. This is a consequence of the fact that their trajectories in the Hilbert subspace H R don't lie for the overwhelming majority of times on generic states (see Fig. 3). Hence, in practice, statements on equilibration and thermalization will depend on the dynamical properties of every system, that is, on their Hamiltonian. This leads us to the notion of dynamical typicality . In contrast to the kinematic typicality presented in this section, where an ensemble has been defined by all the states that belong to a certain subspace, in dynamical typicality the ensemble is defined by all states that share the same constants of motion given a Hamiltonian H and an initial state | ψ (0) 〉 . Studying whether typicality also holds in such a set will be precisely the problem addressed in the next section.

## B. Equilibration. Maximum entropy principle from quantum dynamics

In this context of deriving thermodynamics from quantum mechanics the first problem that needs to be addressed is equilibration , that is, understand how the reversible unitary dynamics of quantum mechanics make systems equilibrate and evolve towards a certain state where they remain thereafter.

Because of the unitary dynamics, equilibration is only possible if the set of observables is restricted. In this spirit, a set of sufficient conditions for equilibration towards the time averaged state has been presented for local observables [50, 51] and observables of finite precision [52, 53]. The two approaches are proven to be equivalent in Ref. [54] and it is remarkable that the conditions given are weak and naturally fulfilled in realistic situations.

Scheme of the restricted subspace H R with its untypical states forming little islands coloured in yellow. The left trajectory (dashed line) passes mostly on typical states while the right trajectory (solid line) has a nonnegligible support on states that are not typical.

<!-- image -->

For simplicity, let us here focus on equilibration of subsystems and, as above, identify in the total system a subsystem S and its environment B . The dynamics of the total system are governed by the Hamiltonian H with eigenvalues { E k } k and eigenvectors {| E k 〉} k . This leads to the time evolution | ψ ( t ) 〉 = e -iHt | ψ (0) 〉 and the reduced state of S is ρ S ( t ) = Tr B ρ ( t ) with ρ ( t ) = | ψ ( t ) 〉〈 ψ ( t ) | .

If equilibration happens, then it happens towards the time averaged state i. e. ω S := Tr B ω with

<!-- formula-not-decoded -->

with P k the projectors onto the Hamiltonian eigenspaces. The time averaged state is the initial state dephased in the Hamiltonian eigenbasis. For this reason it is also called diagonal ensemble .

In Ref. [50], a notion of equilibration is introduced by means of the average distance (in time) of the subsystem ρ S ( t ) from equilibrium. A subsystem S is said to equilibrate if

<!-- formula-not-decoded -->

where ‖ ρ S ( t ) -ω S ‖ 1 is the trace distance. If this average trace distance can be proven to be small, then the subsystem S is indistinguishable from being at equilibrium for almost all times.

Equilibration as a genuine property of quantum mechanics is shown in Ref. [50] by precisely proving that this average distance is typically small. More concretely, if the Hamiltonian that dictates the evolution of the system has non-degenerate gaps i. e. all the gaps of the Hamiltonian are different (an assumption which we will comment on below), then the average distance from equilibrium is bounded by

<!-- formula-not-decoded -->

where d eff ( ρ ) := 1 / Tr( ρ 2 ) is the effective dimension of ρ and ω B = Tr S ω . Roughly speaking, the effective dimension of a state tells us how many eigenstates of the Hamiltonian support such state. It can also be related to the 2-Renyi entanglement entropy by S 2 ( ρ ) = log d eff ( ρ ). Hence, equation (6) guarantees equilibration for Hamiltonians with non-degenerate energy gaps as long as the initial state is spread over many different energies.

Although the condition of having non-degenerate gaps may look very restrictive at first sight, note that Hamiltonians that do not fulfil it form a set of zero measure in the set of Hamiltonians, since any arbitrarily weak perturbation breaks the degeneracy of the gaps. In Ref. [51], the non-degenerate gaps condition was weakened by showing that equilibration occurs provided that no energy gap is hugely degenerate. This condition can be understood as a way of preventing the situation where there is a subsystem which does not interact with the rest.

Let us finally point out that the equilibrium state introduced in Eq. (4) is precisely the state that maximizes the von Neumann entropy given all the conserved quantities [55]. This observation turns the principle of maximum entropy into a consequence of the quantum dynamics. The principle of maximum entropy was introduced by Jaynes in Ref. [17] and states that the probability distribution which best represents the current state of knowledge of the system is the one with largest entropy given the conserved quantities of the system. We will come back in more detail to the Jaynes principle in the next section when the thermalization for integrable systems is discussed.

## C. Thermalization. Emergence of Gibbs states in local Hamiltonians

The next step in this program of justifying the methods of statistical mechanics from quantum mechanics is to tackle the issue of thermalization, i. e. to understand why the equilibrium state is usually well described by a Gibbs state, which is totally independent of the initial state of the system, except for some macroscopic constraints such as its mean energy. In Ref. [56], a set of sufficient conditions for the emergence of Gibbs states is presented for the case of a subsystem S that interacts weakly with its environment B through a coupling V . The Hamiltonian that describes such a situation is H = H S + H B + V . These conditions are a natural translation of the three ingredients that enter the standard textbook proof of the canonical ensemble in classical statistical physics:

1. The equal a priory probability postulate that has been replaced by typicality arguments in Section II A, and an equilibration postulate (such as the second law) that has been replaced by quantum dynamics in Section II B.
2. The assumption of weak-coupling . Here, the standard condition from perturbation theory, ‖ V ‖ ∞ ≪ gaps( H ), is not sufficient in the thermodynamic limit, due to the fast growth of the density of states and the corresponding shrinking of the gaps in the system size. Instead, it is replaced with a physically relevant condition, ‖ V ‖ ∞ ≪ k B T , which is robust in the thermodynamic limit.
3. An assumption about the density of states of the bath [57] , namely, that it grows faster than exponentially with the energy and that it can be locally approximated by an exponential.

Note that the weak-coupling condition will not be satisfied in spatial dimensions higher than one for sufficiently large subsystems, since the interaction strength typically scales as the boundary of the subsystem S . This will be the case regardless of the strength of the coupling per particle or the relative size between S and B . This should not be seen as a deficiency of the above results, but as a feature of strong interactions. Systems that strongly interact with their environment do not in general equilibrate towards a Gibbs state, in a similar way that the reduced state (of a part) of a Gibbs state need not have Gibbs form [58, 59]. In this context, the findings of Ref. [60] suggest that subsystems do not relax towards a local Gibbs state but to the reduction of the global Gibbs state; this is shown for translation-invariant quantum lattices with finite range but arbitrarily strong interactions. The eigenstate thermalization hypothesis (ETH)

[61, 62] gives further substance to this expectation. ETH has several formulations. Its simplest one is maybe the one introduced in Ref. [62]. It states that the expectation value 〈 E k | O | E k 〉 of a few-body observable O in an individual Hamiltonian eigenstate | E k 〉 equals the thermal average of O at the mean energy E k . Although ETH has been observed for some models, it is not true in general and it is well known to break down for integrable models (see [62] for an example with hard-core bosons and references in Ref. [28] for further examples).

In the same spirit, it has recently been proven that a global microcanonical state (the completely mixed state of a energy shell subspace spanned by the Hamiltonian eigenstates with energy inside a narrow interval) and a global Gibbs state are locally indistinguishable for short range spin Hamiltonians off criticality, that is, when they have a finite correlation length [63]. This represents a rigorous proof of the so called equivalence of ensembles . If the Hamiltonian is not translationally invariant, the local indistinguishability between canonical and microcanonical ensembles becomes a typical property of the subsystems, allowing for rare counterexamples.

Concerning the latter condition on the density of states of the bath, in Ref. [64] it has been proven that the density of states of translational invariant spin chains tends to a Gaussian in the thermodynamic limit, matching the suited property of being well approximated by an exponential. In Ref. [63], the same statement is proven for any short ranged spin Hamiltonian.

Let us finally point out that not all systems thermalize. For instance, integrable systems are not well described by the Gibbs ensemble. This is due to the existence of local integrals of motion, i. e. conserved quantities, Q α that keep the memory about the initial state. Instead, they turn to be described by the Generalized Gibbs Ensemble (GGE) defined as

<!-- formula-not-decoded -->

where the generalized chemical potential µ α is a Lagrange multiplier associated to the conserved quantity Q α such that its expectation value is the same as the one of the initial state. The GGE was introduced by Jaynes in Ref. [17] where he pointed out that statistical physics can be seen as statistical inference and an ensemble as the least biased estimate possible on the given information. Nevertheless, note that any system has as many conserved quantities as the dimension of the Hilbert space, e.g. Q α = | E α 〉 〈 E α | . If one includes all these conserved quantities into the GGE the ensemble obtained is the diagonal ensemble introduced in Eq. (4). Note that the description of the equilibrium state by the diagonal ensemble requires the specification of as many conserved quantities as the dimension of the Hilbert space, which scales exponentially in the system size, and becomes highly inefficient. A question arises here naturally, is it possible to provide an accurate description of the equilibrium state specifying only a polynomial number of conserved quantities? If so, what are these relevant conserved quantities Q α that allow for an accurate and efficient representation of the ensemble? This question is tackled in Ref. [65]. There, it is argued that the relevant conserved quantities are the ones that make the GGE as close as possible to the diagonal ensemble in the relative entropy distance D ( ω || τ GGE ), which in this particular case can be written as

<!-- formula-not-decoded -->

where we have used that the diagonal ensemble and the GGE have by construction the same expectation values for the set of selected conserved quantities, i. e. Tr( Q α τ GGE ) = Tr( Q α ω ). Equation (8) tells us that the relevant conserved quantities are the ones the minimize the entropy S ( τ GGE ). Note that in contrast to Jaynes approach, where entropy is maximized for a set of observables defined beforehand, here the notion of physically relevant is provided by how much an observable is able to reduce the entropy by being added into the set of observables that defines the GGE.

If instead of calculating the relative entropy between the diagonal ensemble and the GGE's we do it with respect to the set of product states, i. e.

<!-- formula-not-decoded -->

then we obtain a measure of the total (multipartite) correlations of the diagonal ensemble. In Ref. [66] the scaling with system size of the total correlations of the diagonal ensemble has been shown to be connected to ergodicity breaking and used to investigate the phenomenon of many-body localization.

## D. Equilibration times

Maybe the major challenge that is still open in the equilibration problem is to determine the equilibration timescale. It turns out that even if we know that a system equilibrates, there are no relevant bounds on how long the equilibration process takes. There could be quantum systems that are going to equilibrate, but whose equilibration times are of the order of magnitude of the age of the universe, or alternatively, some systems, like glasses, which do not relax to equilibrium at all, but have metastable states with long lifetimes. The problem of estimating equilibration timescales is thus essential in order to have a full understanding of thermalization.

So far, progress on this issue has taken place from two different approaches. On the one hand, rigorous and completely general bounds on equilibration times have been presented in Ref. [51]. Due to their generality, these bounds scale exponentially with the system size, leading to equilibration times of the age of the universe for macroscopic systems. On the other hand, very short equilibration times have been proven for generic observables [67], Hamiltonians [68-72], and initial states [73]. In nature, systems seem to equilibrate in a time that is neither microscopic nor exponential in the system size. A relevant open question is what properties of the Hamiltonians and operators lead to reasonable equilibration time. As a first step, in Ref. [74], a link between the complexity of the Hamiltonian's eigenvectors and equilibration time is presented. The result does not completely solve the question, since the given bounds are not fulfilled by all Hamiltonians but only by a fraction of them, and further research in this direction is needed.

## E. Outlook

The aim of this section has been to justify that thermal states emerge in Nature for generic Hamiltonians. To complete the picture presented here we recommend the article [28] where an extensive review of the literature on foundations of statistical mechanics is provided.

The main ideas presented here have also been widely studied in the context of condensed matter physics, in which systems are typically brought out of equilibrium by sudden (and slow) quantum quenches : the Hamiltonian of a system (that is initially in the ground state) is suddenly (or smoothly) changed in time. We recommend the review article [29] on non-equilibrium dynamics of closed interacting quantum systems.

Let us finish the section with a list of some of the open problems that we consider most relevant in the field:

- Typicality for symmetric states . Hamiltonians in nature are not generic but have symmetries. Hence, the notion of typicality should be extended to physical states that are produced by symmetric Hamiltonians.
- Quantum notion of integrability . One of the reasons why it is so difficult to extract strong statements on the equilibration and thermalization of many body quantum systems is the absence of a satisfactory quantum notion of integrability [75]. This leads first to some widespread confusion, since integrability is mentioned very often in the field of non-equilibrium dynamics, and second it does not allow us to classify quantum systems into classes with drastically different physical behaviour, like what occurs in classical mechanics.
- Equilibration times . Without bounds on the equilibration time scales, statements on equilibration become useless. As we have seen, the equilibration times are model dependent. We need then to understand how the equilibration times depend on the features of the Hamiltonian and the set of observables considered.
- Relative thermalization. It was highlighted in Ref. [76] that local thermalization of a subsystem S ,

as described here, is not enough to guarantee that S will act as thermal bath towards another physical system R . In other words, imagine that we want to perform quantum thermodynamics on a reference system R , using S as a thermal bath. To model a thermodynamic resource theory that recovers the laws of thermodynamics, it is not sufficient to demand that S be in a local Gibbs state τ S ( β ). Indeed we need S to be thermalized relative to R , that is the the two systems should be uncorrelated, in global state, τ S ( β ) ⊗ ρ R . If this does not hold, then we cannot recover the usual thermodynamic monotones (for instance, there could be anomalous heat flows against the temperature gradient). Therefore, the relevant question for resource theories of thermodynamics is not only 'does S thermalize locally after evolving together with an environment?', but rather 'does S thermalize relative to R after evolving together with an environment?', and the results discussed in this section should be generalized to that setting. First steps in this direction can be found in Ref. [76], where the authors use decoupling-a tool developed in quantum information theory-to find initial conditions on the entropies of the initial state that lead to relative thermalization.

## III. RESOURCE THEORIES

In the previous section we saw the progress that has been made in understanding how systems come to equilibrium, in particular thermal equilibrium, and as such a justification for the thermal state. In the rest of this review we will now take the thermal state as a given, and see what is the thermodynamics of quantum systems which start thermal or interact with thermal states. We will start from an operational point of view, treating the thermal state as a 'free resource', a view inspired by other resource theories from quantum information.

In this section we discuss the approach of thermodynamics as a resource theory in more detail. Let us start by introducing the basic ideas behind resource theories that can be found in the literature, entanglement theory being the paradigmatic example. The first step is to fix the state space S , which is usually compatible with a composition operation-for instance, quantum states together with the tensor product, in systems with fixed Hamiltonians. The next step is to define the set of allowed state transformations . For thermodynamics, these try to model adiabatic operations-like energypreserving reversible operations, and contact with a heat bath.

The set of allowed operations induces a structure on the state space: we say that ρ → σ if there is an allowed transformation from ρ to σ . The relation → is a preorder , that is, a binary relation that is both reflexive ( ρ → σ ) and transitive ( ρ → σ and σ → τ implies ρ →

τ ; this results from composing operations one after the other).

The task now is to find general properties of this structure. A paradigmatic example is looking for simple necessary and sufficient conditions for state transformations. The most general case are functions such that

- ρ → σ ⇒ f ( ρ, σ ) ≥ 0 (that is, f ( ρ, σ ) ≥ 0 is a necessary condition for state transformations), or
- f ( ρ, σ ) ≥ 0 ⇒ ρ → σ (that is, f ( ρ, σ ) ≥ 0 is a sufficient condition for state transformations).

Often, we try to find necessary and sufficient conditions as functions that can be written like f ( ρ, σ ) = g ( ρ ) -h ( σ ). In the special case where g = h for a necessary condition ( ρ → σ ⇒ g ( ρ ) ≥ g ( σ )), we call g a monotone of the resource theory. For example, in classical, largescale thermodynamics, the free energy is a monotone.

In order to quantify the cost of state transformations, we often fix a minimal unit in terms of a standard resource that can be composed. For example, in entanglement theory the standard resource could be a pair of maximally entangled qubits, and in quantum thermodynamics we could take a single qubit (with a fixed Hamiltonian) in a pure state. The question then is 'how many pure qubits do I need to append to ρ in order to transform it into σ ?' or, more generally, 'what is the cost or gain, in terms of this standard resource, of the transformation ρ → σ ?' [77-79].

One may also try to identify special sets of states. The most immediate one would be the set of free states : those that are always reachable, independently of the initial state. In standard thermodynamics, these tend to be what we call equilibrium states, like Gibbs states. Another interesting set is that of catalysts , states that can be repeatedly used to aid in transformations. We will revisit them shortly.

## A. Models for thermodynamics

Now that we have established the basic premise and structure of resource theories, we may look at different models for resource theories of thermodynamics, which vary mostly on the set of allowed operations. In the good 'spherical cow' tradition of physics, the trend has been to start from a very simple model that we can understand, and slowly expand it to reflect more realistic scenarios. In general there are two types of operations allowed: contact with a thermal bath and reversible operations that preserve some thermodynamic quantities. Each of those may come in different flavours.

## 1. Noisy and unital operations

In the simplest case, all Hamiltonians are fully degenerate, so thermal states of any temperature are just fully mixed states, and there are no special conserved quantities. In this setting, thermodynamics inherits directly from the theory of noisy operations [80]. We may model contact with a thermal bath as composition with any system in a fully mixed state, and reversible operations as any unitary operation. Furthermore, we assume that we can ignore, or trace out, any subsystem. Summing up, noisy operations have the form

<!-- formula-not-decoded -->

where A ′ is any subsystem of AB and U is a unitary matrix. Alternatively, we may allow only for maps that preserve the fully mixed state, T A → B : T A → B ( ✶ A | A | ) = ✶ B | B | , called unital maps (an example would be applying one of two isometries and then forgetting which one). The two sets-noisy operations and unital maps-induce the same pre-order structure in the state space. In this setting, majorization is a necessary and sufficient condition for state transformations [80]. Roughly speaking, majorization tells us which state is the most mixed. Let r = ( r 1 , r 2 , . . . , r N ) and s = ( s 1 , s 2 , . . . , s N ) be the eigenvalues of two states ρ and σ respectively, in decreasing order. We say that r majorizes s if ∑ k i =1 r i ≥ ∑ k i =1 s i , for any k ≤ N . In that case ρ → σ ; monotones for this setting are called Schur monotone functions , of which information-theoretical entropy measures are examples [79, 81-84]. For example, if ρ majorizes σ , then the von Neumann entropy of ρ , S ( ρ ) = -Tr( ρ log 2 ρ ), is smaller than S ( σ ). For a review, see [84].

## 2. Thermal operations

The next step in complexity is to let systems have nondegenerate Hamiltonians. The conserved quantity is energy, and equilibrium states are Gibbs states of a fixed temperature T . For instance for a system A with Hamiltonian H A , the equilibrium state is τ A ( β ) = e -βH A / Z . We can model contact with a heat bath as adding any system in a Gibbs state-this corresponds to the idealization of letting an ancilla equilibrate for a long time. A first approach to model physical reversible transformations is to allow for unitary operations U that preserve energy-either absolutely ([ U, H ] = 0) or on average (Tr( Hρ ) = Tr( H ( UρU † )) for specific states). Finally, we are again allowed to forget, or trace out, any subsystem. Together, these transformations are called thermal operations,

<!-- formula-not-decoded -->

where A ′ is any subsystem of AB and U is an energyconserving unitary [85]. The monotones found so far are different versions of the free energy, depending on the exact regime [83, 86-89] (see Example 1). It is worth mentioning we can build necessary conditions for state transformations from these monotones, but sufficiency results are only known for classical states (states that are block-diagonal in the energy eigenbasis) [83] and any state of a single qubit [90, 91]. In the limit of a fully degenerate Hamiltonian, we recover the resource theory of noisy operations.

## 3. Gibbs-preserving maps

Following the example of the theory of noisy operations, we could try to replace these thermal operations with so-called Gibbs-preserving maps, that is, maps such that T A → B ( τ A ( β )) = τ B ( β ). This constraint is easier to tackle mathematically, and the two resource theories induce the same pre-order on classical states, leading to a condition for state transformation called Gibbsmajorization (which is majorization after a rescaling of the eigenvalues) [88]. However, Gibbs-preserving maps are less restrictive than thermal operations for general quantum states [93]. For example, suppose that you have a qubit with the Hamiltonian H = E | 1 〉 〈 1 | , and you want to perform the transformation | 1 〉 → | + 〉 = ( | 0 〉 + | 1 〉 ) / √ 2. This is impossible through thermal operations, which cannot create coherence; yet there exists a Gibbs-preserving map that achieves the task. We may still use Gibbs-preserving maps to find lower bounds on performance, but at the moment we cannot rely on them for achievability results, as they are not operationally defined.

## 4. Coherence

The difference between thermal operations and Gibbspreserving maps is not the only surprise that quantum coherence had in store for thermodynamics enthusiasts. The question of how to create coherence in the first place led to an intriguing discovery. In order to achieve the above transformation | 1 〉 → | + 〉 through thermal operations, we need to draw coherence from a reservoir. A simple example of a coherence reservoir would be a doubly infinite harmonic oscillator, H = ∑ ∞ n = -∞ n ∆ | n 〉 〈 n | , in a coherent state like | Ψ 〉 = N -1 ∑ a + N n = a | n 〉 . Lasers approximate such reservoirs, which explains why we can use them to apply arbitrary transformations on quantum systems like ion traps. One may ask what happens to the reservoir after the transformation: how much coherence is used up? Can we use the same reservoir to perform a similar operation in a new system? The unexpected answer is that coherence is, in a sense, catalytic: while the state of the reservoir is affected, its ability to implement coherent operations is not [94]. What happens is that the state of the reservoir 'spreads out' a little with each use, but the property that determines the efficacy of the reservoir to implement operations stays invariant. In more realistic models for coherence reservoirs, where the Hamiltonian of the reservoir has a ground state, the catalytic properties hold for some iterations, until the state

## Example 1: Free energy as a monotone.

This is an example of finding monotones for the resource theory of thermal operations [86]. We are interested in finding the optimal rates of conversion between two states ρ and σ , in the limit of many independent copies,

<!-- formula-not-decoded -->

If both R ( ρ → σ ) , R ( σ → ρ ) &gt; 0, and these quantities represent optimal conversion rates, then the process must be reversible, that is, R ( ρ → σ ) = 1 /R ( σ → ρ ); otherwise we could build a perpetual motion engine, and the resource theory would be trivial. The idea is to use a minimal, scalable resource α as an intermediate step. We can think of α as a currency: we will sell n copies of ρ for a number of coins, and use them to buy some copies of σ . To formalize this idea, we define the selling and buying cost of a state ρ , or more precisely the distillation and formation rates,

<!-- formula-not-decoded -->

In the optimal limit we have the process

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We have reduced the question to finding the distillation rate, which depends on the choice of α . For example, take ρ , σ and α to be classical states (diagonal in the energy basis) of a qubit with Hamiltonian H = ∆ | 1 〉 〈 1 | . For the currency, we choose α = | 1 〉 〈 1 | . The distillation rate is found by use of information-compression tools [86]. It is given by the relative entropy between ρ and the thermal state τ ( β ),

<!-- formula-not-decoded -->

where F β ( ρ ) = 〈 E 〉 ρ -β -1 S ( ρ ) is the free energy of ρ at inverse temperature β . All in all, we find the conversion rate

<!-- formula-not-decoded -->

Now we can apply this result to find a monotone for a single-shot scenario: in order to have ρ → σ we need in particular that R ( ρ → σ ) ≥ 1. In other words, we require F β ( ρ ) ≥ F β ( ρ ), thus recovering the free energy as a monotone for the resource theory of thermal operations. If we work directly in the single-shot regime, we recover a whole family of monotones [83] based on quantum R´ enyi relative entropies [92], of which the free energy is a member.

spreads all the way down to the ground state. At that stage, the reservoir needs to be recharged with energy to pump up the state again. Crucially, we do not need to supply additional coherence. In the converse direction, we know that coherence reservoirs only are critical in the single-shot regime of small systems. Indeed, in the limit of processing many copies of a state simultaneously, the work yields of doing it with and without access to a coherence reservoir converge [95]

## 5. Catalysts

The catalytic nature of coherence raises more general questions about catalysts in thermodynamics. Imagine that we want to perform a transformation ρ → σ in a system S , and we have access to an arbitrary ancilla in any desired state γ . Now suppose that our constraint is that we should return the ancilla in a state that is ϵ -close to γ :

<!-- formula-not-decoded -->

The question is whether we can overcome the usual limits found in thermal operations by use of this catalyst. In

which gives us the relation other words, can we perform the above transformation in cases where ρ → σ would not be allowed? It turns out that if no other restrictions are imposed on the catalyst, then for any finite ϵ and any two states ρ and σ , we can always find a (very large) catalyst that does the job [83]. These catalysts are the thermodynamic equivalent of embezzling states in LOCC [96]. However, if we impose reasonable energy and dimension restrictions on the catalyst, we recover familiar monotones for state transformations [83, 97]. These restrictions and optimal catalysts result from adapting the concept of trumping relations on embezzling states [98, 99] to the thermodynamic setting. In particular, if we demand that ϵ ∝ n -1 , where n is the number of qubits in the catalyst, we recover the free energy constraint for state transformations [97]. A relevant open question, motivated by the findings of catalytic coherence, is what happens if we impose operational constraints on the final state of the catalyst. That is, instead of asking that it be returned ϵ -close to γ , according to the trace distance, we may instead impose that its catalytic properties stay unaffected. It would be interesting to see if we recover similar conditions for allowed transformations under these constraints.

## 6. Clocks

All of resource theories mentioned allow for energypreserving unitary operations to be applied for free. That is only the 'first order' approach towards an accurate theory of thermodynamics, though. Actually, in order to implement a unitary operation, we need to apply a time-dependent Hamiltonian to the systems involved. To control that Hamiltonian, we require very precise timekeeping-in other words, precise clocks, and we should account for the work cost of using such clocks. Furthermore, clocks are clearly out of equilibrium, and using them adds a source of free energy to our systems. Including them explicitly in a framework for work extraction forces us to account for changes in their state, and ensures that we do not cheat by degrading a clock and drawing its free energy. First steps in this direction can be found in [67]. There, the goal is to implement a unitary transformation in a system S , using a time-independent Hamiltonian. For this, the authors introduce an explicit clock system C hat runs continuously, as well as a weight W that acts as energy and coherence reservoir. The global system evolves under a time-independent Hamiltonian, designed such that the Hamiltonian applied on S depends on the position of the clock-which effectively measures time. The authors show that such a construction allows us to approximately implement any unitary operation on S , while still obeying the first and second laws of thermodynamics. Furthermore, the clock and the weight are not degraded by the procedure (just like for catalytic coherence). In particular, this result supports the idea behind the framework of thermal operations: that energy-conserving unitaries can approximately be implemented for free (if we neglect the informational cost of designing the global Hamiltonian). Note that this is still an idealized scenario, in which the clock is infinite-dimensional and moves like a relativistic particle (the Hamiltonian is proportional to the particle's momentum). A relevant open question is whether there exist realistic systems with the properties assigned to this clock, or alternatively how to adapt the protocol to the behaviour of known, realistic clocks. That direction of research can be related to the resource theory of quantum reference frames [90, 100-102]. An alternative direction would be to ask what happens if we do not have a clock at all-can we extract all the work from a quantum state if we are only allowed weak thermal contact? This question is studied (and answered in the negative, for general states) in Ref. [103].

## 7. Free states and passivity

It is now time to question the other assumption behind the framework of thermal operations: that Gibbs states come for free. There are two main arguments to support it: firstly, Gibbs states occur naturally under standard conditions, and therefore are easy to come by; secondly, they are useless on their own. The first point, typicality of Gibbs states, is essentially the fundamental postulate of statistical mechanics: systems equilibrate to thermal states of Gibbs form. This assumption is discussed and ultimately justified from first principles in Section II The second point is more subtle. Pusz and Woronowicz first introduced the notion of passive states, now adapted to the following setting [108-110]. Let S be a system with a fixed Hamiltonian H , in initial state ρ . We ask whether there is a unitary U that decreases the energy of S , that is

<!-- formula-not-decoded -->

If we can find such a unitary, then we could extract work from S by applying U and storing the energy difference in a weight system. If there is no U that achieves the condition above, then we cannot extract energy from ρ , and we say that the state is passive . The latter applies to classical states (i.e., diagonal in the energy basis) whose eigenvalues do not increase with energy. However, suppose that now we allow for an arbitrary number n many copies of ρ and a global unitary U gl . The question becomes whether

<!-- formula-not-decoded -->

where H gl is the global Hamiltonian, which is the sum of the independent local Hamiltonians of every system. If this is not possible for any n , we say that ρ is completely passive , and it turns out that only states of Gibbs form, ρ = τ ( β ) are completely passive. Moreover, Gibbs states are still completely passive if we allow each of the n subsystems to have a different Hamiltonian, as long as all

## Example 2: Heat engines

The extreme case where one of our resources is in itself a second heat bath is of particular interest. This is a very natural scenario in traditional thermodynamics: steam engines used a furnace to heat a chamber, and exploit the temperature difference to the cooler environment. The study of this limit led to landmark findings like trains, fridges and general heat engines, and to theoretical results on the efficiency of such engines. One might wonder whether these findings can also be applied at the quantum scale, and especially to very small systems composed only of a couple of qubits [25, 104]. The answer is yes: not only is it possible to build two-qubit heat engines, but they achieve Carnot efficiency [105, 106]. It is possible to build heat engines that do not require a precise control of interactions, in other words, that do not require a clock [105, 107].

the states correspond to the same inverse temperature β . This justifies the assumption that we may bring in any number and shape of subsystems in thermal states for free, because we could never extract work from them alone-another resource is necessary, precisely a state out of equilibrium. More formally, it was shown that if a resource theory allows only for energy-conserving unitaries and composition with some choice of free states, Gibbs states are the only choice that does not trivialize the theory [83, 111].

## 8. Different baths

The results outlined above suggest that thermodynamics can be treated as information processing under conservation laws, and so researchers began to experiment with other conserved quantities, like angular momentum [112114], using the principle of maximum entropy to model thermal momentum baths. The state of those baths has again an exponential Gibbs form, with operators like L replacing H . The same type of monotones emerged, and similar behaviour was found for more general conserved quantities [111, 115].

## 9. Finite-size effects

Another setting of practical interest is when we have access to a heat bath but may not draw arbitrary thermal subsystems from it. For instance, maybe we cannot create systems with a very large energy gap, or we can only thermalize a fixed number of qubits. In this case, the precision of state transformations is affected, as shown in [116], and we obtain effective measures of work cost that converge to the usual quantities in the limit of a large bath. The opposite limit, in which all resources are large heat baths, leads to the idea of heat engines (Example 2).

## 10. Single-shot regime

Some of the studies mentioned so far characterize the limit of many independent repetitions of physical exper- iments, and quantify things like the average work cost of transformations or conversion rates [86, 95]. The monotones found (like the von Neumann entropy and the usual free energy) are familiar from traditional thermodynamics, because this regime approximates the behaviour of large uncorrelated systems. As we move towards a thermodynamic theory of individual quantum systems, it becomes increasingly relevant to work in the single-shot regime. Some studies consider exact state transformations [77, 78, 114], while others allow for a small error tolerance [79, 81, 82, 87, 88, 111, 115, 117, 118]. The monotones recovered correspond to operational entropy measures, like the smooth max-entropy (see Example 3), and variations of a single-shot free energy that depend on the conservation laws of the setting; in general, they can be derived from quantum R´ enyi relative entropies [92] between the initial state and an equilibrium state [83, 119]. Single-shot results converge asymptotically to the traditional ones in the limit of many independent copies. The relation between single-shot and average regimes is studied via fluctuation theorems in [120].

## 11. Definitions of work

In classical thermodynamics, we can define work as some form of potential energy of an external device, which can be stored for later use. For instance, if a thermodynamic process results in the expansion of a gas against a piston, we can attach that piston to a weight, that is lifted as the gas expands. We count the gain in gravitational potential energy as work-it is well-ordered energy that can later be converted into other forms, according to the needs of an agent. A critical aspect is that at this scale fluctuations are negligible, compared to the average energy gain. In the regime of small quantum systems, this no longer holds, and it is not straightforward to find a good definition of work. Without a framework for resource theories of thermodynamics, a system for work storage is often left implicit. One option is to assume that we can perform any joint unitary operation U SB in a system S and a thermal bath B , and work is defined as the change in energy in the two systems manipulated, W := Tr( H SB ρ SB ) -Tr( H SB U SB ρ SB U † SB ), where H SB is the (fixed) Hamiltonian of system and bath, and

ρ SB the initial state [116]. Another example, inheriting more directly from classical thermodynamics, assumes that we can change the Hamiltonian of S and bring it in contact with an implicit heat bath [121]; work at a time t is then defined as

<!-- formula-not-decoded -->

To study fluctuations around this average value, we consider work to be a random variable in the single-shot setting-this is explored in Section V. Note that in these examples work is not operationally motivated; rather it is defined as the change of energy that heat cannot account for. Resource theories of thermodynamics, with their conservation laws, force us to consider an explicit system W for work storage. We act globally on S ⊗ W , and we can define work in terms of properties of the reduced state of W . One proposal for the quantum equivalent of a weight that can be lifted, for the resource theory of thermal operations, is a harmonic oscillator, with a regular Hamiltonian H W = ∑ n n ϵ | n 〉 〈 n | . The energy gaps need to be sufficiently small to be compatible with the Hamiltonian of S ; in the limit ϵ → 0 the Hamiltonian becomes H W = ∫ dx x | x 〉 〈 x | [87, 106]. Average work is defined as Tr( H W ρ fi nal W ) -Tr( H W ρ initial W ), and fluctuations can be studied directly in the final state of the work storage system, ρ W . This approach also allows us to observe other effects, such as the build up of coherences in W , and of correlations between W and S . Another advantage is that we can adapt the storage system to other resource theories: for instance, we can have an angular momentum reservoir composed of many spins, and count work in terms of polarization of the reservoir [113]. These approaches are critically analysed in Ref. [122]; in particular, it is highlighted that they do not distinguish work from heat. For instance, thermalizing the work storage system may result in an increase of average energy, which is indiscriminately labelled as 'average work'. In the same paper, an axiomatic approach to define work is proposed, based on concepts from resource theories and interactive proofs. There, work is seen as a figure of merit: a real function assigned to state transformations, W ( ρ → σ ). Starting from a couple of assumptions, the authors derive properties of acceptable work functions W : for instance, that they can be written as the difference between a monotone for initial and final state, W ( ρ → σ ) = g ( ρ ) -g ( σ ). The free energy is an example of such a valid work function.

## B. Generalizing resource theories

Let us now abstract from particular resource theories, and think about their common features, and how we may generalize them.

## 1. Starting from the pre-order

As mentioned before, the set of allowed transformations imposes a pre-order structure ( S, ≤ ) on the state space S . One direction towards exploring the concept of resource theories could be to start precisely from such a pre-order structure. That was the approach of Carath´ eodory, then Giles and later Lieb and Yngvason, who pioneered the idea of resource theories for thermodynamics [77, 78, 126, 127]. In their work, the set of allowed transformations is implicitly assumed, but we work directly with an abstract state space equipped with a preorder relation. They were largely inspired by classical, macroscopic thermodynamics, as one may infer from the conditions imposed on the state space, but their results can be applied to thermodynamics of small quantum systems [114]. Assuming that there exist minimal resources that can be scaled arbitrarily and act as 'currency', the authors obtain monotones for exact, single-shot state transformations. When applied to the pre-order relation on classical states that emerges from thermal operations, these monotones become single-shot versions of the free energy [114].

## 2. Starting from the set of free resources

In Ref. [119] general quantum resource theories are characterized based on the set of free resources of each theory. Assuming that the set of free states is wellbehaved (for instance, that it is convex, and that the composition of two free states is still a free state), they show that the relative entropy between a resource and the set of free states is a monotone. This is because the relative entropy is contractive (non-increasing under quantum operations); the same result applies to any contractive metric. Finally, they find an expression for the asymptotic value of a resource in terms of this monotone: the conversion rate between two resources is given by the ratio between their asymptotic value.

## 3. In category theory

Ref. [16], and more recently Ref. [37] have generalized the framework of resource theories to objects known as symmetric monoidal categories. These can represent essentially any resource that can be composed (in the sense of combining copies of different resources, like tensoring states in quantum theory). The authors consider both physical states and processes as possible resources. After obtaining the pre-order structure from a set of allowed operations, resource theories can be classified according to several parameters. For instance, the authors identify quantitative theories (where having more of a resource helps, like for thermal operations) and qualitative ones (where it helps to have many different resources). They find expressions for asymptotic conversion rates in

## Example 3: Landauer's principle

How much energy is needed to perform logical operations? What are the ultimate limits for heat dissipation of computers? These questions lie at the interface between thermodynamics and information theory, are of both foundational and practical interest. As Bennett realized, all computations can be decomposed into reversible operations followed by the erasure of a subsystem [123]. If we assume that the physical support of our computer is degenerate in energy, we recover the setting of noisy operations, in which unitaries are applied for free. That way, the thermodynamic cost of computation is simply the cost of erasure, which is defined as taking a system from its initial state ρ to a standard, predefined pure state | 0 〉 (like when we format a hard drive). Rolf Landauer first proposed that the work cost of erasing a completely unknown bit of information (think of a fully mixed qubit) in an environment of temperature T is k B T ln 2 [12]. That very same limit was also found for quantum systems, in the setting of thermal operations [116, 124], for the ideal case of an infinitely large heat bath and many operations; finite-size effects are analysed in Ref. [116].

Using Landauer's principle as a building block, we can approach the more general question of erasing of a system that is not in a completely unknown state, but rather about which we have partial information. For example, imagine that we want to perform an algorithm in our quantum computer, and then erase a subsystem S (which could be a register or ancilla). The rest of our computer may be correlated with S , and therefore we can use it as a memory M , and use those correlations to optimize the erasure of S . In short, we want to take the initial state ρ SM to | 0 〉 〈 0 | S ⊗ ρ M , erasing S but not disturbing M . It was shown [79, 82] that the optimal work cost of that transformation is approximately H ϵ max ( S | M ) ρ k B T ln 2, where ϵ parametrizes our error tolerance and H ϵ max ( S | M ) ρ is the smooth max entropy, a conditional entropy measure that measures our uncertainty about the state of S , given access to the memory M . It converges to the von Neumann entropy in the limit of many independent copies. In the special case where S and M are entangled, it may become negative-meaning that we may gain work in erasure, at the cost of correlations. Not incidentally, these results use quantum information processing techniques to compress the correlations between S and M before erasure; after all, 'information is physical' [125].

different regimes and, crucially, give varied examples of resource theories, within and beyond quantum theory, showing just how general this concept is.

## 4. Resource theories of knowledge

In Ref. [128], emphasis is given to the subjective knowledge of an observer. The framework introduced there allows us to embed macroscopic descriptions of reality into microscopic ones, which in turn lets us switch between different agents' perspectives, and see how traditional large-scale thermodynamics can emerge from quantum resource theories like thermal operations. It also allows us to combine and relate different resource theories (like thermodynamics and LOCC), and to infer the structure of the state space (like the existence of subsystems or correlations) from modularity and commutativity of transformations.

## C. Outlook

In the previous sections we identified several open problems. These can be grouped into two main directions:

- Quantumness: coherence, catalysis and clocks. It remains to find optimal coherent catalysts and clocks under realistic constraints (a generalization

of Ref. [97]). This would give us a better understanding of the thermodynamic power and limitations of coherent quantum states. It would also allow us to account for all costs involved in state transformations.

- Identifying realistic conditions. We have been very good at defining sets of allowed transformations that are analogous to those of traditional thermodynamics, and recover the same monotones (like the free energy) in the limit of large, uncorrelated systems. The original spirit of thermodynamics, however, was to find transformations that were easy and cheap to implement for experimenters-for instance, those whose cost did not scale with the relevant parameters. In order to find meaningful resource theories for individual quantum systems, it is again imperative to turn to concrete experimental settings and try to identify easy and cheap transformations and resources. At this stage, it is not yet clear whether these will correspond to thermal operations, time-independent Hamiltonians, or another model of quantum thermodynamics-in fact it is possible that they vary depending on the experimental realization, from superconducting qubits to ion traps.

## IV. ENTANGLEMENT THEORY IN THERMODYNAMIC SETTINGS

In the previous sections we have established how quantum information can be used to understand the very foundation of thermodynamics, from the emergence of thermal states to the resource theory of manipulating these with energy conserving unitaries. We have seen that phrasing thermodynamics as a resource theory can elucidate the meaning of thermodynamic quantities at the quantum scale, and how techniques originally developed for a resource theory of communication can facilitate this endeavour. The motivation behind this approach is a very practical one: finding the ultimate limitations of achievable transformations under restrictions that follow from the nature of the investigated system that naturally limits the set of operations we can perform. As quantum information processing is becoming increasingly applied, we also need to think about fundamental restrictions to quantum information itself, emerging from unavoidable thermodynamic considerations. There has thus been an increased interest in investigating scenarios of quantum information processing where thermodynamic considerations cannot be ignored. From fundamental limitations to the creation of QIP resources to their inherent work cost. In this section we try to give a brief overview over recent developments in this intersection with a focus on the paradigmatic resource of QIP: entanglement.

## A. Correlations and entanglement under entropic restrictions

Entanglement theory is in itself one of the most prominent examples of resource theories. Entanglement, a resource behind almost all tasks in quantum information processing, is hard to create and once distributed can only decrease. Thus in entanglement theory classically correlated states come for free and local operations are considered cheap, which singles out entanglement as the resource to overcome such limitations. These limitations and resources are of course very different to the resources and tasks explored in the previous sections. A comprehensive comparison between the principles behind these and more general resource theories is made in Ref. [129] and as examples of a more abstract treatment in Ref. [16].

Such resource theories are always designed to reflect specific physical settings, such as local operations and classical communication (LOCC) [130] as a natural constraint for communication. It is therefore unavoidable that when describing various physical circumstances these resource theories can be combined yielding hybrid theories. One natural example is the desire to process quantum information in a thermodynamic background. Ignoring limitations coming from available energies in a first step this leads to the task of producing resources for computation (such as entanglement or correlation) at a given entropy. Some of the first considerations in this direction were motivated by the prospect of using nuclear magnetic resonance (NMR) for quantum computation. Due to non-zero temperature, i.e. non-trivial restrictions on the entropy of the state, such systems would always be fairly close to the maximally mixed state.

In this context the most natural question to ask, is whether a unitary transformation is capable of entangling a given input state. As a precursor to studying the possibility of entangling multipartite states, the complete solution for two qubits was found in Ref. [131] and later decent bounds on bipartite systems of arbitrary dimension were presented in Ref. [132].

Another pathway was pursued by Refs. [133-135], where with NMR quantum computation in mind, volumes of separable states around the maximally mixed state were identified. These volumes imply that if any initial state is in close proximity of the maximally mixed state, there can be no chance of ever creating entanglement in such states, as the distance from the maximally mixed state is invariant under unitary transformations. Further improvements in terms of limiting temperatures were obtained in Ref. [136].

The question of whether a given state can be entangled under certain entropy restrictions clearly relies only on the eigenvalue spectrum of the considered state, as the best conceivable operation creating entanglement is a unitary one (which leaves eigenvalues unchanged). These questions were further pursued under the name of 'separability from spectrum in Refs. [137-139]. One of the main results important in the context of quantum thermodynamics is the following: A state with eigenvalues λ i , ordered by size, i.e. { λ i ≥ λ i +1 } can be entangled by an appropriate unitary if

<!-- formula-not-decoded -->

More importantly, for 2 × m dimensional states, this condition is not only sufficient, but also necessary [139].

Moving beyond the mere presence of entanglement in the unitary orbit of input states, one encounters an intrinsic difficulty of properly quantifying the entanglement created. There is a whole 'zoo of entanglement measures [143, 144] and only in the bipartite case there is a unique 'currency' known, i.e. a paradigmatic resource state from which all other states can be created via LOCC (although recent progress has been made in the four qubit case, where it has been shown that after exclusion of a measure zero set, such a set of resource states can indeed be identified [145]).

In any case one can at least study general correlations with a clear operational interpretation, such as the mutual information, which has been performed in Refs. [140, 146, 147]. In these papers the authors have, among other things, identified minimally and maximally correlated states in the unitary orbit of bipartite systems. It turns out that at least here the entropy poses only a rather trivial restriction and for any d -dimensional state

<!-- image -->

ρ a mutual information of I ρ ( A : B ) = 2 log 2 ( d ) -S ( ρ ) can be achieved via global unitary rotations.

Exploiting these results Ref. [141] continued to study the generation of correlations and entanglement under entropic restrictions for multipartite systems. Inspired by the idea of thermal states as a free resource, the authors consider a multipartite system initially in a thermal state. They ask what is the highest temperature T ent at which entanglement can still be created, it scales with the dimension of the partitions and quantify the inherent cost in terms average energy change (see example (4) for an exemplary two qubit energy cost). By introducing concrete protocols, i.e. unitary operations, the authors show that bipartite entanglement generation across all partitions of n -qubits is possible iff k B T/E &lt; n/ (2 ln(1+ √ 2)) and genuine multipartite entanglement across all parties can be created if k B T/E &lt; n/ (2 ln( n )) + O ( n/ ln( n ) 2 ).

## B. Correlations and entanglement in a thermodynamic background

In the context of thermodynamics the previous subsection can be viewed as a very special case of operating on closed systems with an unlimited external energy supply or a fully degenerate Hamiltonian. As elaborated in Section III of the review this does not encompass the whole potential of thermodynamic transformations. If the necessary correlating unitary does not conserve the total energy, we should account for the difference in average energy between initial and final states. Taking into account also the average energy cost reveals an intrinsic work value of correlations and entanglement in general. This fundamental fact was first quantified in Ref. [141]).

Accounting for the average energy change in the unitary orbit of initial quantum states however still does not encompass the whole potential of thermodynamic resource theories. Thermal operations on target states can also make use of a thermal bath at temperature T and thus can also reduce the entropy of the target system. Disregarding energy costs in this context of course yields the rather trivial result that any quantum information processing resource can be produced, simply by cooling the system (close) to the ground state and then performing the adequate global unitary operation on it. Taking into account the free energy costs of correlating transformations, Ref. [142] has shown that every bit of correlation embodies an intrinsic work value proportional to the temperature of the system. For mutual information this yields a relation akin to Landauer's principle for the work cost of creating correlations W cor ,

<!-- formula-not-decoded -->

and it implies a general free energy cost of entanglement that is bounded from above and below for the bipartite case in Ref. [142]. All previous considerations are illustrated in Fig. 4.

That extractable work can be stored in correlations is by no means a purely quantum phenomenon. Even classical correlations can store work in situations where local work extraction is impossible. In Ref. [148] the quantum vs. classical capacity for storing extractable work purely in correlations was compared. For two qubits twice as much work can be stored in entangled correlations as the best possible separable (or even classical, which turns out to be the same) correlations admit (a fact that is also mentioned in Ref. [76] in a different setting). However the difference between separably encoded work from correlations W sep and the maximally possible work in correlations W max scales as

<!-- formula-not-decoded -->

i.e. the quantum advantage vanishes in the thermodynamic limit of large systems.

Concerning the extractable work from correlations one can also find seemingly contrary results if the figure of merit changes. The above considerations apply only if Creating entanglement from thermal states will always cost some energy. For the simplest case of entangling two qubits with energy gap E at zero temperature one can find a closed expression, e.g. for the concurrence, in terms of the invested average energy ∆ E = W :

<!-- formula-not-decoded -->

the target is an extraction of average energy or standard free energy, partially neglecting the details of the work distribution arising in the receiving system (detailed considerations of such work distribution fluctuations will be discussed in section (V)). One can just as well be interested in a guaranteed amount of work. If that is the case one can arrive at more restrictions concerning work extraction as also recently demonstrated in [118]. Curiously in Ref. [149] it was shown, however, that these restrictions can be overcome by considering k initially uncorrelated catalysts that build up correlations in the process. In that context one can extract more deterministic work and can thus regard the stochastic independence of the input catalysts as a resource for work extraction, which is quite contrary to the case considered before and the thermodynamic limit.

A different, but very related, setting exploring work gain from correlations is studied in the context of quantum feedback control. Here the task is rather to quantify the inevitable work cost arising from information gain in the process of a measurement. As in order to measure a system one needs to correlate with the system in question it follows intuitively that this scenario will also always induce work cost related to bipartite correlations between the system and the memory storing the information gain about the system. Here the work cost coming purely from correlations was quantified in Ref. [147], building upon older results on the inevitable work cost of quantum measurements [150-153] and Landauer's principle. To model the necessary feedback control, the authors included a general model of a quantum memory upon which projective measurements can be performed. The authors also studied the possible work gain from bipartite quantum states in this context. Denoting the state of the memory as ρ M the authors find an upper bound on the work gain (defined as the work extracted from both subsystems minus the work cost of the measurements and subsequent erasure of the quantum memory) as

<!-- formula-not-decoded -->

## C. Thermodynamics under locality restrictions

In the previous subsections we have reviewed the prospect of creating quantum information processing re- sources in a thermodynamic background. The other obvious connection between the resource theories of entanglement and thermodynamics is taking the converse approach. Here one is interested in thermodynamic operations under additional locality restrictions.

In Ref. [154] the difference between the extractable work from bipartite quantum states in thermodynamics both with and without locality restrictions was studied. The resulting difference, called the work deficit , can be bounded via

<!-- formula-not-decoded -->

which for pure states coincides with entanglement of formation (or any other sensible choice of entanglement measure that all reduce to the marginal entropy in case of pure states). In the above equation it is assumed that bits which are sent down the communication channel are treated as classical in the sense that they are only dephased once, and not again in a second basis. This interplay led to subsequent investigations into the thermodynamic nature of entanglement in Ref. [154], where analogies between irreversible operations in thermodynamics and bound entanglement were drawn, and to concrete physical scenarios satisfying this bound in Ref. [121].

## D. Entanglement resources in thermodynamic tasks

Apart from resource theory inspired questions, one might study the role of informational quantities through their inevitable appearance in thermodynamic operations at the quantum level. For instance the role of entangling operations and entanglement generation in extracting work from multiple copies of passive states , i.e. states where no local work extraction is possible [108, 109], has attracted some attention recently. The implied fact that global unitary operations are required to extract work indicates some form of non-local resource being involved in the process.

In general passive states are always diagonal in the energy eigenbasis [108, 109], which implies that one starts and ends the protocols with diagonal states. In these scenarios the individual batteries from which work is to be extracted are considered non-interacting, directly implying the separability of initial and final states in these protocols. Nonetheless the fact that local unitaries can never extract any work from copies of passive states directly implies that entangling unitaries enable work extraction from such states [155]. In that sense entangling power of unitaries can be seen as a resource for work extraction purposes (which in conventional thermodynamic resource is of course considered a free operation).

In Ref. [156] the role of quantum resources in this context was further explored. While it is true that the ability to perform entangling unitaries is required for this particular work extraction problem, this does not imply that any entanglement is ever generated in the process. In fact the whole procedure can dynamically be implemented without ever generating the slightest bit of entanglement [156], however the most direct transformation can considerably entangle the systems in the process. In Ref. [157] it was demonstrated that if the work per unit time (power) is considered with cyclic operations in mind then a quantum advantage for charging power can be achieved.

## E. Using thermodynamics to reveal quantumness

That entanglement plays a special role in quantum many-body physics is a well established fact that has received adequate attention in numerous publications (see e.g. Ref. [158] and the extensive list of citations therein). In this topical review we want to at least mention a related question that connects quantum thermodynamics directly with entanglement theory: The possibility to use thermodynamic observables to reveal an underlying entanglement present in the system. At zero temperature it is already known that many natural interaction Hamiltonians have entangled ground states (in fact often many low energy eigenstates even of local Hamiltonians feature entanglement). This fact can be exploited to directly use the energy of a system as an entanglement witness, even at non-zero temperatures [159]. Intuitively this can be understood through the fact that a low average energy directly implies that the density matrix is close to the entangled ground state. If this distance is sufficiently small that can directly imply entanglement of the density matrix itself. The known results and open questions of this interplay including Refs. [160-167] are also discussed in the review Ref. [36]. Furthermore, other macroscopic thermodynamic quantities can also serve as entanglement witnesses through a similar intuition, such as e.g. the magnetic susceptibility [168] or the entropy [169].

## F. Outlook

Resource theories always have their foundation in what we believe to be hard/impossible to implement and what resources allow us to overcome such limitations. As such they always only capture one specific aspect of the physical systems under investigation. The results out- lined in this section emphasise the fact that thermodynamic constraints have drastic consequences for processing quantum information and that locality constraints will change thermodynamic considerations at the quantum scale. One path to explore could now be a consistent resource theory that adaptively quantifies possible resources from different restrictions. This would furthermore elucidate the exact role played by genuine quantum effects, such as entanglement, in thermodynamics.

## V. QUANTUM FLUCTUATION RELATIONS AND QUANTUM INFORMATION

## A. Introduction

The phenomenological theory of thermodynamics successfully describes the equilibrium properties of macroscopic systems ranging from refrigerators to black holes that is the domain of the large and many. By extrapolating backwards, from the domain of the 'many' to the 'few', we venture further from equilibrium into a regime where both thermal and quantum fluctuations begin to dominate and correlations proliferate. One may then ask the question - what is an appropriate way to describe this blurry world which is dominated by deviations from the average behaviour?

One way to describe the thermodynamics of small systems where fluctuations cannot be ignored is by using the framework of stochastic thermodynamics [170]. In this approach the basic objects of traditional statistical mechanics such as work and heat are treated as stochastic random variables and hence characterised by probability distributions. Over the last 20 years various approaches have lead to sets of theorems and laws, beyond the linear response regime, which have revitalised the already mature study of non-equilibrium statistical mechanics. Central to these efforts are the fluctuation relations that connect the non-equilibrium response of a system to its equilibrium properties. A wealth of results have been uncovered in both the classical and the quantum regimes and the interested reader is directed to the excellent reviews on the topics [21-23]. Here we focus on aspects of this approach that have been specifically influenced by concepts in quantum information, or show promise for symbiosis. We hope that by reviewing the existing contributions as well as suggesting possible research avenues, further cross fertilisation of the fields will occur.

To begin with, it is useful to illustrate how the probability distributions of a thermodynamic variable like work is defined. Consider a quantum system with a timedependent Hamiltonian H ( λ ( t )), parametrized by the externally controlled work parameter λ ( t ). The system is prepared in a thermal state by allowing it to equilibrate with a heat bath at inverse temperature β for a fixed value of the work parameter λ ( t &lt; t i ) = λ i . The initial state of the system is therefore the Gibbs state,

<!-- formula-not-decoded -->

At t = t i the system-reservoir coupling is removed and a fixed, reversible protocol is performed on the system taking the work parameter from its initial value λ i to the final value λ f at a later time t = t f . The initial and final Hamiltonians are defined by their spectral decompositions

<!-- formula-not-decoded -->

respectively, where | ψ n 〉 ( | φ m 〉 ) is the n th ( m th) eigenstate of the initial (final) Hamiltonian with eigenvalue E n ( λ i ), E m ( λ f ). The protocol connecting the initial and final Hamiltonians generates the unitary evolution operator U ( t f , t i ), which in general has the form

<!-- formula-not-decoded -->

where T → denotes the time-ordering operation. We stress here that, in this framework, one typically assumes that the system is initially prepared in a thermal state but after the unitary protocol the system is generally in a non-equilibrium state.

The work performed (or extracted) on (or from) the system as a consequence of the protocol is defined by the outcomes of two projective energy measurements [171]. The first, at t = t i , projects onto the eigenbasis of the initial Hamiltonian H ( λ i ), with the system in thermal equilibrium. The system then evolves under the unitary operator U ( t f , t i ) before a second projective measurement is made onto the eigenbasis of the final Hamiltonian H ( λ f ) at t = t f . The joint probability of obtaining the outcome E n ( λ i ) for the initial measurement followed by E m ( λ f ) for the final one is easily shown to be

<!-- formula-not-decoded -->

Accordingly, the quantum work distribution is defined as

<!-- formula-not-decoded -->

where δ is the Dirac delta function. For reasons which will become clear shortly we use the subscript F to denote 'forward' protocol. Physically, Eq. 17 states that the work distribution consists of the discrete number of allowed values for the work ( E m ( λ f ) -E n ( λ i )) weighted by the probability p ( n, m ) of measuring that value in a given realisation of the experiment. The quantum work distribution therefore encodes fluctuations in the measured work arising from thermal statistics (first measurement) and from quantum measurement statistics (second measurement).

In order to understand what is meant by a fluctuation theorem, we introduce a backward process which is the time reversed protocol of the forward one previously defined. Now P B ( W ) is the work distribution corresponding to the backward process , in which the system is prepared in the Gibbs state of the final Hamiltonian H ( λ f ) at t = 0 and subjected to the time-reversed protocol that generates the evolution Θ U ( t f , t i )Θ † , where Θ is the anti-unitary time-reversal operator. It turns out that the following theorem holds, the Tasaki-Crooks relation [172, 173],

<!-- formula-not-decoded -->

which shows that, for any closed quantum system undergoing an arbitrary non-equilibrium transformation, the fluctuations in work are related to the equilibrium free energy difference for the corresponding isothermal process between the equilibrium states τ ( λ i ) and τ ( λ f ),

<!-- formula-not-decoded -->

This relationship is further emphasized by a corollary to Eq. 18 known as the Jarzynski equality [174],

<!-- formula-not-decoded -->

which states that ∆ F (of the corresponding isothermal process) can be extracted from by measuring the exponentiated work. A straightforward application of Jensen's inequality for convex functions allows one the retrieve the expected expression 〈 W 〉 ≥ ∆ F . The average energetic deviation of a non-equilibrium process from the equivalent reversible isothermal process is known as dissipated work

<!-- formula-not-decoded -->

Due to the Jarzynski equality this quantity is positive, 〈 W 〉 diss ≥ 0. This can be also directly seen from the Crooks relation, taking the logarithm of both sides of the equality in Eq. 18 and integrating over the forward distribution we find

<!-- formula-not-decoded -->

where K is the classical Kullback Leibler divergence and we have introduced the average irreversible entropy change 〈 Σ 〉 corresponding to the dissipated work. Physically the irreversible entropy change, in this context, would be the internal entropy generated due to the nonequilibrium process which would manifest itself as an additional source of heat if an ideal thermal bath would be reconnected to the system at the end of the protocol. In Ref. [175] it was shown that the irreversible entropy change can also be expressed in terms of a quantum relative entropy

<!-- formula-not-decoded -->

where σ = U ( t f , t i ) τ ( λ i , β ) U † ( t f , t i ) is the out of equilibrium state at the end of the protocol. This is fully consistent with the open system treatment in [176].

## B. Phase estimation schemes for extraction of quantum work and heat statistics

Surprisingly, perhaps one of the most important contributions that ideas from quantum information have made to this field in statistical mechanics is the experimental acquisition of statistics of work. In the classical setting considerable progress has been made in the experimental extraction of the relevant stochastic thermodynamic distributions to explore and verify the fluctuation theorems [23]. Up until very recently, no such experimental progress had been made for quantum systems. A central issue is the problem of building the quantum work distribution as it requires to make reliable projective energy measurements on to the instantaneous energy eigenbasis of an evolving quantum system [22, 171]. It was proposed in Ref. [177] that these measurements could be reliably performed on a single trapped ion, an experiment that was recently performed [178].

Alternatives to the projective method have been proposed [179, 180], based on phase estimation schemes , well known in quantum information and quantum optics [181]. In these schemes, we couple our system to an ancillary system, and perform tomography on that system. The spirit is very similar to the DQC1 algorithm put forward in Ref. [182]. The characteristic function of the work probability distribution (Eq. 24) can be obtained from the ancilla, and the work statistics are then extracted by Fourier transform. The characteristic function is defined as

<!-- formula-not-decoded -->

The proposals to measure the characteristic function were first tested in the laboratory only quite recently in a Liquid state NMR setup [183]. This experiment is the first demonstration of the work fluctuation theorems and extraction of work quantum statistics, and is expected to inspire a new generation of experiments at the quantum level. Another interesting extension of these schemes is to go beyond the closed system paradigm and to study open system dynamics at and beyond the weak coupling limit. The first extensions have been proposed in Refs. [184186]. In Ref. [187] the proposal outlined in Ref. [186] to measure the statistics of dissipated heat was implemented in order to perform a study of the information to energy conversion in basic quantum logic gates at the fundamental Landauer Limit.

Another interesting suggestion made to access the quantum work statistics is the use the concept of a 'positive operator valued measure', or POVM [188], a wellknown concept within quantum information and quantum optics. A POVM is the most general way to describe a measurement in a quantum system, with the advantage that it can always be seen as a projective measurement on an enlarged system. In this work the authors show that by introducing an appropriate ancilla that the POVM description allows the work distribution to be efficiently sampled with just a single measurement in time. In this work it was suggested that the algorithm proposed could be used, in combination with the fluctuation theorems, to estimate the free energy of quantum states on a quantum computer. The scheme was recently extended and developed in Ref. [189] along with a promising implementation using ultra-cold atoms. This would be a promising avenue to explore work statistics in a many-body physics setting where the statistics of work can be shown to have universal behaviour at critical points [190].

## C. Fluctuation relations with feedback, measurement and CPTP maps

The relationship between thermodynamics and the information processing is almost as old as thermodynamics itself and is no where more dramatically manifested than by Maxwell's demon [2-6]. One way of understanding the demon paradox is by viewing the demon as performing feedback control on the thermodynamic system. In this case the framework for stochastic thermodynamics and the fluctuation theorems needs to be expanded. Building upon previous work [152, 153], Sagawa and Ueda have generalised the Jarzynski equality to incorporate the feedback mechanism [191, 192] for classical systems. This theoretical breakthrough allowed for an experimental demonstration of information to energy conversion in a system by means of of non-equilibrium feedback of a Brownian particle [193]. These feedback based fluctuation theorems were further modified to incorporate both initial and final correlations [194]. These works, in particular, highlight the pivotal role played by mutual information in non-equilibrium thermodynamics [6].

The Sagawa-Ueda relations were generalized to quantum systems in Ref. [195]. For reasons of pedagogy we will follow this approach here. In the work of Morikuni and Tasaki an isolated quantum system is considered where an external agent has control of the Hamiltonian parameters. The system is initialised in a canonical state, τ ( β ), and an initial projective measurement of the energy is made whose outcome is E 0 i . The Hamiltonian is then changed via a fixed protocol and evolves according to the unitary operator U . In the next stage a projective measurement is performed with outcomes j = 1 , . . . , n and described by a set of projection operators Π 1 , . . . , Π n . Now the time evolution is conditioned on the outcome j so the Hamiltonian is changed according to these outcomes. This is the feedback control stage. Finally, one makes a projective measurement of the energy of the final Hamiltonian with outcome E j k . In this setting it is shown that

<!-- formula-not-decoded -->

where W = W i,j,k = E 0 i -E j k is the work and ∆ F is the free energy difference between the initial state and the canonical state corresponding to the final value of the Hamiltonian H j . We see that in this feedback controlled scenario a new term enters on the right hand side. A straightforward calculation shows that this term evaluates as γ = ∑ j Tr[Π j U † j τ ( β ) U j Π j ]. This γ quantity is shown in Refs. [191, 195] to be related to the efficiency of the demon in making use of the information it acquires during the feedback process. When it becomes less than one it provides an example of a failed demon who did not make a good use of the information acquired. On the other hand it can become larger than one indicating that the feedback is working efficiently. Another relation discovered by Sagawa and Ueda and quantized by Morkikuni and Taskaki concerns almost the same protocol as just explained only now classical errors are made in the intermediate measurement stage. Again let the intermediate measurement be described by Π 1 , ..., Π n which yield the result j but the controller misinterprets the result as j ′ with a certain probability. In this framework another generalised fluctuation theorem can be derived,

<!-- formula-not-decoded -->

where I is the mutual information between the set of measurement outcomes the demon actually records and what is the true result of the projection. These feedback fluctuation theorems for quantum systems were further generalised to the situation when a memory system is explicitly accounted for in Ref. [147] and shed light on the amount of thermodynamic work which can be gained from entanglement. In addition to feedback, fluctuation theorems were investigated under continuous monitoring [196, 197] and analysed for general measurements [198, 199].

A recent series of papers have analysed fluctuationlike relations from the operational viewpoint employing the full machinery of trace-preserving completely positive maps. In Ref. [200] the formalism is used to give an alternative derivation of the Holevo bound [201]. In Ref. [202] an information-theoretical Jarzynski equality was derived. It was found that fluctuation relations can be derived if the map generated by the open dynamics obeys the unital condition. This has been connected to the breakdown of micro-reversibility for non-unital quantum channels [203-206]. In Ref. [207] the authors analysed the statistics of heat dissipated in a general protocol and found that the approach can be used to derive a lower bound on the heat dissipated for non-unital channels. Recently this bound has been used to investigate the connection with the build up of multipartite correlations in collisional models [208].

## D. Entropy production, relative entropy and correlations

With the surge of interest in the thermodynamics of quantum systems and the development of quantum fluctuation relations, research has been directed to microscopic expressions for entropy production. In formulating thermodynamics for non-equilibrium quantum sys- tems, the relative entropy plays a central role [192]. As first pointed out in Ref. [209] this is due to its close relationship with the free energy of a quantum state. The relative entropy also plays a central role in quantum information theory, in particular, in the geometric picture of entanglement and general quantum and classical correlations [210, 211]. In the non-equilibrium formulation of thermodynamics [22] it is omnipresent for the description of irreversible entropy production in both closed [175] and open driven quantum systems [212] (see also [213]). One may then wonder if there exists a relationship between the entropy produced by operations that generate or delete correlations in a quantum state and the measures for correlations in that state? Given the youthful nature of the field the question is largely unanswered but some progress in this direction has been made.

The relationship between the relative entropy of entanglement and the dissipated work was first proposed as an entanglement witness in Ref. [214]. Going beyond the geometric approach a functional relationship between the entanglement generated in a chain of oscillators and the work dissipated was explored in Ref. [215] and also later for more general quantum correlations [216]. In an open systems framework it was shown that the irreversible entropy production maybe attributed to the total correlations between the system and the reservoir [217] (we note that this derivation is entirely analogous to the formulation of the Landauer principle put forward by in Ref. [116]). The exchange fluctuation relation and the consequences for correlated quantum systems were studied in Ref. [218].

## E. Outlook

As fluctuation theorems are exact results, valid for arbitrary non-equilibrium dynamics, they are currently being used to understand the non-linear transport of energy, heat and even information in quantum technologies. This is a relatively new research avenue and the applications of quantum fluctuation theorems in other fields such as condensed matter physics, quantum optics and quantum information theory are in their infancy. Ultimately, the hope would be that they provide a unifying framework to understand the relationship between information and energy in non-equilibrium quantum systems. Ultimately one would like to form a picture of information thermodynamics of quantum systems under general non-equilibrium conditions.

As we have seen above, quantum phase estimation, a central protocol in quantum information theory, has been applied successfully to extract work statistics from a small non-equilibrium quantum system and perhaps other such unexpected interdisciplinary links will emerge. For example one wonders if existing experimental schemes could be modified to deal with situations dealing with non-passive initial states so as to study maximal work extraction problems and also to extend to more complicated many-body and open system scenarios.

In Refs. [120, 219, 220] the first steps towards unification of the work statistics and fluctuation theorems approach to thermodynamics and the single shot statistical mechanics approaches mentioned have been taken (see Sec. III). We are confident that other links will emerge between various approaches in the not so distant future.

## VI. QUANTUM THERMAL MACHINES

In this final brief section of the review we end by considering the area of quantum thermodynamics concerning quantum thermal machines, that is quantum versions of heat engines or refrigerators. We shall overview the extent to which quantum entanglement and correlations are relevant to their operation.

Whereas in almost all of the above the situation comprised of only one thermal bath and systems in contact with it, in this section our interest is in situations involving two (or more) thermal baths. Now, there are two regimes which one can focus on: the primary one is usually the cyclic behaviour of systems interacting with the baths, or alternatively the steady state behaviour that is characterised by the currents of heat or work that can be maintained in the long time limit. The second regime is the transient one, and how the system reaches stationarity.

One way to think of the present situation is that the second thermal bath is the system out of equilibrium with respect to the first bath, and the goal is to produce resources (work, or a steady state current out of a cold bath) at optimal rates. From this perspective, the quantum machine plays the role of the 'bridge' or the 'mediator' which facilitates the operation of the larger thermal machine.

The history of quantum thermal machines is a long one, going back to the sixties with the invention of the maser, which can be seen as a heat engine [221], and received much attention over the following decades. A complete overview of the literature in this direction is far beyond the scope of the present review; however excellent recent overviews can be found in Refs. [31-33]. In the present context, one important message from this body of work is that thermal machines comprised of as little as a single qutrit (3 level system), or of 2 or 3 qubits, can be constructed, that moreover can approach Carnot efficiency (the maximal possible efficiency of any machine). It is thus plausible that they may ultimately become important from the perspective of nanotechnology and implementations of quantum information processes devices. As such a full understanding of their quantum behaviour, including the correlations they can build up, is important. Here we review specifically those studies concerned with the role of entanglement and quantum coherence in the functioning of such small quantum thermal machines, both at the level of the machine, as well as in the bath, if pre-processing operations are allowed. We also look at the role of coherence in the transient behaviour when the refrigerator is first switched on. We review a recent proposal for a witness that quantum machines are provably outperforming their classical counterparts. Finally, we look at the idea of using thermal machines as a means of entanglement generation (switching the focus away from the traditions resources of work or heat currents).

A related idea is that of algorithmic cooling , which we summarise in Example 5, and which was recently reviewed in [222].

## A. Absorption refrigerators

The first machine we shall look at a quantum model of an absorption refrigerator, a refrigerator which is not run by a supply of external work (which is the situation most customarily considered), but rather run by a source of heat. An absorption refrigerator is thus a device connected to three thermal reservoirs; a 'cold' reservoir at temperature β C from which heat will be extracted; a 'hot' reservoir at inverse temperature β H , which provides the supply of energy into the machine; and finally a 'room temperature' reservoir at temperature β R into which heat (and entropy) will be discarded. The goal is to cool down the cold reservoir (i.e. extract heat from it).

There are a number of different figures of merit that one can consider to quantify the performance of the machine. The most commonly considered is the coefficient of performance COP = Q C /Q H , where Q C and Q H are respectively the heat currents flowing out of the cold the hot reservoirs (the COP is the analogous quantity to the efficiency for an absorption refrigerator; since the COP can be larger than 1 it cannot be thought of directly as an efficiency). The famous result of Carnot [223], a statement of the second law of thermodynamics, is that the efficiency (or COP) of all thermal machines is bounded as a function of the reservoir temperatures. In particular, for the specific case of an absorption refrigerator we have COP ≤ ( β R -β H ) / ( β C -β R ). Other relevant figures of merit are the power Q C (i.e. neglecting how efficient the process is), the COP when running at maximal power, and the minimal attainable stationary temperature β st C for a cold object in contact with the bath.

Below we give a brief outline of the model under consideration, full details of which can be found in Refs. [224, 225]. Consider three qubits, each one in thermal contact with one of the three thermal baths, with local Hamiltonians H i = E i | 1 〉 〈 1 | , for i = C , R , H chosen such that E R = E C + E H to ensure that the system has a degenerate subspace of energy E R formed by the states | 010 〉 and | 101 〉 (where we use the order C-R-H for the three qubits). In this subspace the interaction Hamiltonian H int = g ( | 010 〉 〈 101 | + | 101 〉 〈 010 | ) is placed, which mediates the transfer of energy. A schematic representation of this fridge can be found in Fig. 5.

## Example 5: Algorithmic cooling

Consider a collection of n qubits, all at inverse temperature β , with corresponding populations in the ground and excited states p and (1 -p ) respectively. The goal of algorithmic cooling is to bring m qubits to the ground state by an arbitrary unitary transformation. A fundamental upper bound can be placed on m , purely by entropic considerations. The initial entropy is nS ( τ ( β ) = nH ( p ), where H ( p ) = -p log 2 p -(1 -p ) log 2 (1 -p ) is the binary Shannon entropy . Since unitary transformations do not change the entropy, this easily leads to the upper bound on m ,

<!-- formula-not-decoded -->

which would be achieved if the remaining n -m qubits are all left at infinite temperature (maximally mixed state) with entropy S ( τ (0)) = 1. In [226] it was shown that as n tends to infinity this fundamental limit can be approached using an algorithm which uses O ( n log 2 n ) unitary gate operations. It was later realised that given access to an external bath this limit can be surpassed: the qubits which end this protocol at infinite temperature can be 'refreshed' to temperature β and the protocol can be run again on the remaining ( n -m ) qubits, for example [227]. This is referred to as heat-bath algorithmic cooling .

In order to understand the basic principle, one can focus instead on 3 qubits and assume that the first is the one which is to be cooled down (now not to zero temperature, but any colder temperature). Let us consider the populations of the two states | 100 〉 and | 011 〉 , which are p 2 (1 -p ) and p (1 -p ) 2 respectively. The state | 100 〉 , in which qubit one is excited (and therefore 'hot') has more population than the state | 011 〉 , where qubit one is in the ground state (and therefore 'cold'). Thus, by swapping the population of these two states the first qubit is cooled down. Indeed, after the application of such a unitary, the final population p ′ in the ground state of the first qubit is

<!-- formula-not-decoded -->

which is greater than p whenever (2 p -1) &gt; 0, i.e. whenever the first qubit was at a positive temperature. Finally, a unitary which implements | 011 〉 ↔ | 100 〉 whilst leaving all other energy eigenstates the same can easily be constructed from the CNOT and Toffoli gates as

<!-- image -->

A recent review giving many more details about algorithmic cooling can be found in Ref. [222]

## 1. Stationary behaviour

Assuming the weak coupling regime between the qubits and the baths, the dynamics can be modelled using a time-independent Lindblad Master equation ˙ ρ = L ( ρ ) (with L the Linbladian, i.e. the most general generator of time-homogeneous, Markovian dynamics). The stationary solution ρ st , satisfying L ( ρ st ) = 0, can be shown to correspond to an absorption refrigerator if the parameters are chosen appropriately, i.e. such that β st C &gt; β C , where β st C is the stationary inverse temperature of the cold qubit.

From the point of view of quantum information, the basic questions about this steady state are (i) whether quantum correlations (for example entanglement) are present in the stationary state, and (ii) if yes, whether they are important for the operation, or merely a by-product of quantum evolution. These questions were addressed in Refs. [224, 225].

In Ref. [225] quantum correlations in the form of discord were studied. The quantum discord D ( AB ) ρ := I ( A : B ) ρ -I ( A : B ) σ , with σ the state after a minimally disturbing measurement on Bob, is a form of quantum correlation weaker than entanglement [228, 229]. The authors studied quantum discord between numerous inequivalent partitions of the system. The most interesting results were obtained when the discord is calculated between the cold qubit (the qubit which is being cooled) and the relevant subspace of the two remaining qubits (that singled out by the interaction Hamiltonian H int ). They found that discord is always present, but they found no relationship between the amount of discord present and the rate at which heat was extracted from the cold bath. Specifically, to obtain this result they studied the behaviour of discord as a function of the energy spacing E C of the cold qubit. Whilst both quantities typically exhibited local maxima as E C was varied, these maxima failed to coincide.

In Ref. [224] the focus was instead on the entanglement

## FIG. 5: Three-qubit fridge

<!-- image -->

Schematic diagram of a three qubit autonomous refrigerator (inside circle), coupled to three thermal reservoirs. The interaction Hamiltonian is represented by the green and orange arrows.

maintained in the steady state. First, if the machine is operating close to the maximal Carnot limit then the state is necessarily fully separable, i.e. a convex combination of product states of the three qubits. Conversely, operating far from this regime every type of multipartite entanglement can be found in the stationary state. In particular, there are regimes where entanglement is generated across any fixed bipartition, and even genuine multipartite entanglement can be found, demonstrating that the state has no biseparable decomposition. Here it must be stressed that the amount of entanglement found was small, but that this should be expected due to the weak inter-qubit coupling.

Finally, it was also shown that there appears to be a link between the amount of entanglement generated in the partition R | CH and the so-called cooling advantage that entangled machines have compared to separable ones. In particular, the cooling advantage was defined as the difference between the minimal possible temperatures that could be achieved with either separable or entangled refrigerators. More precisely, by optimising the stationary temperature β st C of the cold qubit, varying the Hamiltonian of the machine qubits and their couplings to baths (at fixed temperatures). It was shown that arbitrary machines (i.e. ones allowed to be entangled) could outperform ones which were additionally constrained to be separable. Moreover, the advantage was found to be a function only of the amount of entanglement generated across the R | CH partition. One point of interest is that this is the bipartition of energy entering vs. energy leaving the machine, thus suggesting a connection between the transport properties of the machine and the entanglement.

## 2. Transient behaviour

Instead of looking at the steady state behaviour, one may also consider the transient behaviour. Such questions are relevant when one is interested in running a small number of cooling cycles in order to cool down the system as fast as possible. Alternatively, if one is thinking of initialising a system for some other use, the transient regime might also be of interest for quicker initialisation. Intuitively, since the evolution between the qubits is coherent, one might expect the local populations to undergo Rabi oscillations, and hence by running for precise times lower temperatures may be achievable in a transient regime (as the qubits continuous cool down and heat up).

This is precisely what was shown in Ref. [230, 231]. More precisely, in Ref. [231] the authors study the Markovian dynamics with weak inter-qubit coupling g (relative to the relaxation rates, as in the above subsection), while in Ref. [230] the authors considered additionally Markovian dynamics with strong inter-qubit coupling, and band-limited non-Markovian baths (modelled with a one-qubit memory for each machine qubit). Taking as the natural initial state the product state with qubit to be initially at the same temperature of the bath, both numerically study the transient behaviour of the temperature of the cold qubit as the system approaches stationarity. While in the weak interaction case no Rabi oscillations are observed (since the system is effectively over-damped), in the strong-interaction case Rabi oscillations indeed take place, with period approximately 2 π/g . This demonstrates that coherent oscillations offer an advantage for cooling. A more complicated behaviour due to memory effects is also observed in the non-Markovian case in [230], but nevertheless the system can be seen to pass through much colder temperatures during its transient behaviour. In Ref. [231] it was also shown that if the couplings are chosen appropriately, (in particular such that the weakest coupling is to the hot reservoir), then the system can quickly remains for a long time in a temperature below the stationary temperature, in particular without oscillating above it. This demonstrates a particular stable regime for the preparation of the system at temperatures below its stationary temperature.

In order to explore more the advantage offered by coherence, Ref. [230] also considered varying the initial state, by altering the coherence in the subspace where the Hamiltonian operates. Interestingly, with only a small amount of initial coherence even when considering case (a) of weak-interaction dynamics, oscillations in the temperature are seen, again allowing for cooling below the stationary temperature. In the other two cases, the magnitude of the oscillations is also seen to increase (i.e. the system achieves lower temperatures transiently), demonstrating an advantage in all situations.

Finally, in Ref. [231] the amount of entanglement that is generated in the transient regime was also studied. Focusing on either genuine multipartite entanglement, or entanglement across the partition R | CH, i.e. the one corresponding to energy-in vs. energy out (as studied in Ref. [224]), considerably more entanglement can be generated in the transient regime.

## B. Reservoir engineering

As we have seen in previous sections of the review, thermals states are naturally considered as a free resource which can be utilised and manipulated. Likewise, the ubiquity of thermal machines is that having access to two large thermal reservoirs can also be considered as something essentially free, and thermal machines consider ways of utilising these resources.

One interesting avenue is to consider that any transformation of a thermal reservoir which can 'easily' be carried out can also be considered to be free, as an idealisation, and this motivates the idea of considering thermal machines which run between engineered reservoirs , assuming that the engineering was an easy to perform transformation. In the present context, when one has sufficient control over (part of) the reservoir, then the engineering can be at the quantum level. Here again we are interested specifically in the role that quantum correlations engineered in the bath have on the functioning of quantum thermal machines.

In Refs. [232, 233] reservoir engineering in the form of squeezing is considered, since squeezing is relatively easy to carry out, and is furthermore known to offer quantum advantages in other contexts in quantum information. That is the reservoir, instead of consisting of a large collection of modes in thermal states at inverse temperature β H , are in fact squeezed thermal states (at the same temperature). More precisely, the squeezing operator is U sq = exp(( ra 2 -r ∗ a † 2 ) / 2) with a and a † the annihilation and creation operators respectively, and the squeezed thermal state (of a given mode, i.e. a harmonic oscillator) is U sq τ ( β ) U † sq . Whereas normally the variances of the quadratures ( x = ( a + a † ) / 2 and p = ( a -a † ) / 2 i ) are symmetric, the squeezed modes become asymmetric, with one the former amplified by the factor e r , and the latter shrunk by e -r . The important point is that a system placed in thermal contact with such a squeezed reservoir will not thermalize towards a thermal state at β , but rather to a squeezed thermal state, which has the same average number of photons as a thermal state at temperature β ( r ) &lt; β . That is, in terms of average number of photons, a squeezed thermal state appears 'hotter' than a thermal bath.

Starting first with Ref. [233], a model of an absorption refrigerators is considered, identical to the one outlined in the previous section. Here, in accordance with the above, in the weak coupling regime the effect of the reservoir engineering amounts to modifying the Linbladian L , such that the term corresponding to the hot reservoir L H transforms to L H ( r ), where this now generates dissipation towards the squeezed thermal state at β H ( r ) . They show that maximal COP that the refrigerator can approach becomes

<!-- formula-not-decoded -->

That is, the COP overcomes the Carnot limit that bounds the COP of any absorption refrigerator operating between baths at β C , β R and β H , if reservoir engineering is not carried out. Thus if reservoir engineering is more readily available than a hotter 'hot' bath, then this approach clearly provides an advantage in terms of COP.

In Ref. [232] a different model was considered, this time a quantum heat engine operating a quantum Otto cycle, a time dependent cycle, comprising two expansion stages (changing the Hamiltonian of the system) and two thermalization stages. This system considered comprised of a single harmonic oscillator, with initial spacing E 1 . While uncoupled to any environment, the first stage is an expansion, whereby E 1 → E 2 &gt; E 1 , i.e. the Hamiltonian is changed in time. In the second stage the system is then placed in contact with a squeezed hot reservoir (this is the stage which differs from a standard Otto cycle, where an unsqueezed hot reservoir is used). After disconnection, the third stage is a compression stage, bringing the spacing back to from E 2 to E 1 . Finally, the system is placed in contact with a cold (unsqueezed) reservoir, in order to thermalize at the cold temperature. This cycle is summarised in Fig. 6. The authors perform an analysis of the system and similarly show that the maximum efficiency of the engine exceeds the Carnot efficiency (of the Otto cycle, η = β H /β C ). Moreover, if one considers the efficiency at maximum power, then this can also be surpassed, and as the squeezing parameter becomes large, the efficiency at maximum power approaches unity.

Finally, we stress that these results do not constitute a violation of the second law, since they consider a scenario outside the regime of applicability of the Carnot limit (much in the same way that a regular car engine, consuming fuel, does not violate the second law, since it is also outside the regime of applicability). Conversely, it is interesting that the net effect of squeezing appears to be as if the hot reservoir has been heated to a temperature β H ( r ), and that the performance of the machines is bounded exactly by the Carnot limit with respect to this new temperature.

<!-- image -->

## C. Quantum thermodynamic signatures

One way to differentiate between a system which is genuinely using quantum effects and one which is only using the formal structure of quantum mechanics (the discreteness of energy levels, for example) is to devise signatures, or witnesses, for quantum behaviour. This is similar to what is done in entanglement theory, or in Bell nonlocality, where one finds witnesses which certify that entanglement was present, since no separable quantum state could pass a certain test. An interesting question is whether one can find analogous witnesses in a quantum thermodynamics setting. This is what was proposed in Ref. [234] in the form of Quantum thermo signatures .

In more detail, the main idea of Ref. [234] is to find a threshold on the power of a thermal machine which would be impossible to achieve for a machine which is 'classical'. The authors take as the minimal set of requirements for a machine to be considered classical (i) that it's operation can be fully described using population dynamics

(i.e. as a rate equation among the populations in the energy eigenbasis); (ii) that the energy level structure and coupling strengths are unaltered compared to quantum model under comparison; (iii) that no new sources of heat or work are introduced. A way to satisfy the above three constraints is to add pure de-phasing noise in the energy eigenbasis on top of the dissipative dynamics of the quantum model (arising from the interaction with the thermal reservoirs). One can then compare models with and without de-phasing noise, and ask whether the additional noise places an upper bound on the power of the machine.

For simplicity in presentation, in what follows we will focus here on the results obtained for the four-stage qubit Otto heat engine, similar to the one described in the previous subsection (except now with a qubit in place of a harmonic oscillator). We note that the authors show that the same results hold for a two-stage engine [235] and for continuous time engines [25], as well as for refrigerators and heat pumps. As an aside, the reason why the result holds for all three models is because Ref. [234] also proves that in the regime of weak-coupling to the bath, and weak driving, all three types of engine can be shown to be formally equivalent, producing the same transient and steady state behaviour at the level of individual cycles.

It is shown that a state independent bound can be placed on the power of a classical machine which is proportional to the duration of a single cycle of the engine τ cyc , as long as the so-called 'engine-action' s is small, where the engine action is the product of the duration τ and energy scale (as measured by the operator norm of each term appearing in the Master equation). They demonstrate that there is a regime where a quantum engine (i.e. one without additional dephasing) can provably outperform the corresponding classical machine, with powers an order of magnitude larger in the former case.

## D. Stationary entanglement

Entanglement is understood to be a fragile property of quantum states, that is one typically expects that noise will destroy the entanglement in a quantum state. Much effort has been invested in investigating and devising ways in which one can counter the effects of noise, and maintain entanglement in a system, such as quantum error correction, dynamical decoupling, decoherence free subspaces, to name but a few.

In the first subsection we saw that the non-equilibrium steady state of autonomous quantum thermal machines can be entangled. If one thus focuses not on their thermodynamic functioning, but rather on their entanglement functioning, we see that whenever a thermal machine reaches a steady state which is entangled, this constitutes a way of generating stead state entanglement, merely through dissipative interactions with a number of thermal environments at differing temperatures.

Furthermore, if the interest is only in steady state entanglement generation, then it is not even necessary that the machine perform any standard thermodynamic task, and can in fact simply be a bridge between two reservoirs, allowing the steady flow of heat from hot to cold such that the stationary state of the bridge is necessarily entangled. This is precisely the situation which was first considered in Ref. [236], where the minimal system of two qubits interacting with two baths at temperatures β H and β C was considered in the weak coupling (Markovian) regime. Numerous variants were then discussed: in Refs. [237-241] different aspects of the dynamical approach to the steady state were analysed (assuming nonMarkovian dynamics, the rotating wave approximation, etc); in Refs. [242, 243] a 3 qubit bridge was considered; in Ref. [244] the stationary discord was also studied; in Ref. [245, 246] geometric and dielectric properties of the environment were considered, and in Ref. [247] superconducting flux qubits and semiconductor double quantum dot implementations were explored.

Focusing on the simplest possible example, that of the two qubit bridge, the take home message of this line of investigation is that this is a viable means to generating stationary entanglement. In particular the implementations considered in Ref. [247] suggest that in experimentally accessible situations steady state entanglement can indeed be maintained at a level which might be usable to then later distill.

## E. Outlook

We have seen in this section a range of results concerning quantum thermal machines, focusing primarily on the quantum correlations and entanglement present in the machine, as well as other signatures of quantumness. Although we have focused on the progress that has been achieved so far, there are a number of directions which should be explored in further work to more fully understand the role of quantum information for quantum thermal machines.

First of all, the main playground of study in this section has been the weak-coupling regime, where the machine is in weak thermal contact with the thermal reservoirs. It is important and interesting to ask what happens outside of this regime, when the thermal baths are strongly coupled to the machine. On the one hand, intuition suggests that stronger coupling corresponds to more noise, which will be detrimental to fragile quantum correlations. On the other hand, stronger driving might lead to more pronounced effects. As such, the interplay between noise and driving needs to be better understood.

Second, we have seen that quantum signatures, either in terms of entanglement or coherence, can be constructed, which show that there is more to quantum thermal machines than just the discreteness of the energy levels. Here, it would be advantageous to have more examples of quantum signatures, applicable in as wide a range of scenarios as possible. An experimental demonstration of a quantum signature would also be a great development concerning the implementation of thermal machines.

Finally, thinking of cooling as a form of error correction, it is interesting to know if ideas from quantum thermal machines can be incorporated directly into quantum technologies as a way to fight de coherence. This would be as an alternative to standard quantum error correction ideas, and an understanding of how they fit alongside each other could be beneficial from both perspectives.

## VII. FINAL REMARKS

Ideas coming from quantum information theory have helped us understand questions, both fundamental and applied, about the thermodynamic behaviour of systems operating at and below the verge at which quantum effects begin to proliferate. In this review we have given an overview of these insights. We have seen that they have been both in the form of technical contributions, for example with new mathematical tools for old problems, such as the equilibration problem, and also in the form of conceptual contributions, like the resource theory approach to quantum thermodynamics.

Although quantum information is only one of the many fields currently contributing to quantum thermodynamics, we expect its role to become more important as the field grows and matures. Indeed, we believe that plac- ing information as a central concept, just as Maxwell did when his demon was born, will lead to a deeper understanding of many active areas of physics research beyond quantum thermodynamics.

## AUTHOR CONTRIBUTIONS

All authors contributed equally to this review. Sections I and III were adapted from LdR's PhD thesis [128].

## ACKNOWLEDGEMENTS

We thank Fernando Brandao, Aharon Brodutch, Nicolai Friis, Marti Perarnau-Llobet, Joe Renes, Raam Uzdin and Nicole Yunger-Halpern for helpful feedback on the manuscript. LdR thanks support from ERC AdG NLST

- [1] [C. H. Bennett, Int. J. Theor. Phys. 21 , 905 (1982).](http://link.springer.com/10.1007/BF02084158)
- [2] H. S. Leff and A. F. Rex, Maxwell's demon: Entropy, information, computing (Taylor and Francis, 1990).
- [3] M. B. Plenio and V. Vitelli, Contemp. Phys. 42 , 25 (2001).
- [4] H. S. Leff and A. F. Rex, Maxwell's demon 2: Entropy, classical and quantum information, computing (Taylor and Francis, 2002).
- [5] K. Maruyama, F. Nori, and V. Vedral, Rev. Mod. Phys. 81 , 1 (2009).
- [6] J. M. R. Parrondo, J. M. Horowitz, and T. Sagawa, Nature Phys. 11 , 131 (2015).
- [7] [Bell Syst. Tech. J. 27 , 379 (1948).](http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=6773024)
- [8] T. M. Cover and J. A. Thomas, Elements of information theory (John Wiley and sons, 2006).
- [9] M. L. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, 2000).
- [10] M. M. Wilde, Quantum Information Theory (Cambridge University Press, 2013).
- [11] J. von Neumann, Mathematical Foundations of Quantum Mechanics , Princeton landmarks in mathematics and physics series (1955) pp. xii + 445, translated from the German edition by Robert T. Beyer. Original first edition published in German in 1932.
- [12] [R. Landauer, IBM J. Res. Dev. 5 , 183 (1961).](http://dx.doi.org/10.1147/rd.53.0183)
- [13] R. Horodecki, H. Pawel, M. Horodecki, and K. Horodecki, Rev. Mod. Phys. 81 , 865 (2009).
- [14] S. B¨ auml, M. Christandl, K. Horodecki, and A. Winter, Nat. Commun. 6 , 6908 (2015).
- [15] C. H. Bennett, G. Brassard, S. Popescu, B. Schumacher, J. A. Smolin, and W. K. Wootters, Phys. Rev. Lett. 76 , 722 (1996).
- [16] B. Coecke, T. Fritz, and R. W. Spekkens, Inform. Comput. , (2016).
- [17] [E. Jaynes, Phys. Rev. 106 , 620 (1957).](http://link.aps.org/doi/10.1103/PhysRev.106.620)
- [18] [E. Jaynes, Phys. Rev. 108 , 171 (1957).](http://link.aps.org/doi/10.1103/PhysRev.108.171)
- [19] [J. von Neumann, Eur. Phys. J. H 35 , 201 (2010).](http://link.springer.com/10.1140/epjh/e2010-00008-5)

and EPSRC grant DIQIP. MH acknowledges funding from the Juan de la Cierva fellowship (JCI 2012-14155), the European Commission (STREP 'RAQUEL') and the Spanish MINECO Project No. FIS2013-40627-P, the Generalitat de Catalunya CIRIT Project No. 2014 SGR 966. MH furthermore acknowledges funding through the AMBIZIONE grant PZ00P2 161351 from the Swiss National Science Foundation (SNF). PS Acknowledges support from the European Union (Projects FP7-PEOPLE2010-COFUND No. 267229, ERC CoG QITBOX and ERC AdG NLST). AR thanks support from the Beatriu de Pinos fellowship (BP-DGR 2013), the EU (SIQS), the Spanish Ministry Project FOQUS (FIS2013-46768P), the Generalitat de Catalunya (SGR 874 and 875) and the Spanish MINECO (Severo Ochoa grant SEV2015-0522). All authors acknowledge the COST Action MP1209.

- [20] C. Jarzynski, Annu. Rev. Cond. Mat. Phys. 2 , 329 (2011).
- [21] [M. Esposito, Rev. Mod. Phys. 81 , 1665 (2009).](http://link.aps.org/doi/10.1103/RevModPhys.81.1665)
- [22] M. Campisi, P. H¨ anggi, and P. Talkner, Rev. Mod. Phys. 83 , 771 (2011).
- [23] [U. Seifert, Rep. Prog. Phys. 75 , 126001 (2012).](http://stacks.iop.org/0034-4885/75/i=12/a=126001)
- [24] P. H¨ anggi and P. Talkner, Nature Phys. 11 , 108 (2015).
- [25] H. Scovil and E. Schulz-DuBois, Phys. Rev. Lett. 2 , 262 (1959).
- [26] J. E. Geusic, E. O. Schulz-DuBios, and H. E. D. Scovil, Phys. Rev. 156 , 343 (1967).
- [27] [R. Alicki, J. Phys. A: Math. Gen. 12 , L103 (1979).](http://stacks.iop.org/0305-4470/12/i=5/a=007)
- [28] C. Gogolin and J. Eisert, Rep. Prog. Phys. 79 , 056001 (2016).
- [29] A. Polkovnikov, K. Sengupta, A. Silva, and M. Vengalattore, Rev. Mod. Phys. 83 , 863 (2011).
- [30] A. J. Daley, M. Rigol, and D. S. Weiss, New J. Phys. 16 , 095006 (2014).
- [31] [R. Kosloff, Entropy 15 , 2100 (2013).](http://dx.doi.org/10.3390/e15062100)
- [32] R. Kosloff and A. Levy, Annu. Rev. Phys. Chem. 65 , 365 (2014).
- [33] D. Gelbwaser-Klimovsky, W. Niedenzu, and G. Kurizki, Advances In Atomic, Molecular, and Optical Physics 64 , 329 (2015).
- [34] L. Szilard, Zeitschrift f¨ ur Physik 53 , 840 (1929).
- [35] J. Gemmer, M. Michel, and G. Mahler, Quantum thermodynamics (Lecture Notes in Physics vol 784) (Berlin, Heidelberg:Springer, 2009).
- [36] L. Amico, A. Osterloh, and V. Vedral, Rev. Mod. Phys. 80 , 517 (2008).
- [37] [T. Fritz, Mathematical Structures in Computer Science FirstView , 1 (2015).](http://dx.doi.org/10.1017/S0960129515000444)
- [38] J. Millen and A. Xuereb, New J. Phys. 18 , 011002 (2016).
- [39] S. Popescu, A. J. Short, and A. Winter, Nature Phys. 2 , 754 (2006).
- [40] S. Goldstein, J. L. Lebowitz, R. Tumulka, and N. Zangh` ı, Phys. Rev. Lett. 96 , 050403 (2006).

- [41] S. Lloyd, Black Holes, Demons and the Loss of Coherence: How complex systems get information, and what they do with it , Ph.D. thesis, Rockefeller University (1991).
- [42] D. Poulin, A. Qarry, R. Somma, and F. Verstraete, Phys. Rev. Lett. 106 , 170501 (2011).
- [43] S. Garnerone, T. R. de Oliveira, and P. Zanardi, Phys. Rev. A 81 , 032336 (2010).
- [44] F. G. S. L. Brand˜ ao, A. W. Harrow, and M. Horodecki, (2012), arXiv:1208.0692.
- [45] A. Hamma, S. Santra, and P. Zanardi, Phys. Rev. Lett. 109 , 040502 (2012).
- [46] I. Affleck, T. Kennedy, E. H. Lieb, and H. Tasaki, Commun. Math. Phys. 115 , 477 (1988).
- [47] [G. Vidal, Phys. Rev. Lett. 93 , 040502 (2004).](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.93.040502)
- [48] A. W. Harrow and R. A. Low, Commun. Math. Phys. 291 , 257 (2009).
- [49] O. Szehr, F. Dupuis, M. Tomamichel, and R. Renner, New J. Phys. 15 , 053022 (2013).
- [50] N. Linden, S. Popescu, A. J. Short, and A. Winter, Phys. Rev. E 79 , 061103 (2009).
- [51] A. J. Short and T. C. Farrelly, New J. Phys. 14 , 013063 (2012).
- [52] [P. Reimann, Phys. Rev. Lett. 101 , 190403 (2008).](http://prl.aps.org/abstract/PRL/v101/i19/e190403)
- [53] [P. Reimann, Phys. Scripta 86 , 058512 (2012).](http://stacks.iop.org/1402-4896/86/i=5/a=058512)
- [54] [A. J. Short, New J. Phys. 13 , 053009 (2011).](http://dx.doi.org/10.1088/1367-2630/13/5/053009)
- [55] C. Gogolin, M. P. M¨ uller, and J. Eisert, Phys. Rev. Lett. 106 , 040401 (2011).
- [56] A. Riera, C. Gogolin, and J. Eisert, Phys. Rev. Lett. 108 , 08040 (2012).
- [57] The density of states of the bath ϱ B ( E ) is the number of eigenstates of the bath with energy close to E .
- [58] A. Ferraro, A. Garc´ ıa-Saez, and A. Ac´ ın, EPL (Europhysics Letters) 98 , 10009 (2012).
- [59] M. Kliesch, C. Gogolin, M. J. Kastoryano, A. Riera, and J. Eisert, Phys. Rev. X 4 , 031019 (2014).
- [60] M. P. M¨ uller, E. Adlam, L. Masanes, and N. Wiebe, Commun. Math. Phys. 340 , 499 (2015).
- [61] [M. Srednicki, Phys. Rev. E 50 , 888 (1994).](http://dx.doi.org/10.1103/PhysRevE.50.888)
- [62] M. Rigol, V. Dunjko, and M. Olshanii, Nature 452 , 854 (2008).
- [63] F. G. S. L. Brand˜ ao and M. Cramer, (2015), arXiv:1502.03263.
- [64] J. P. Keating, N. Linden, and H. J. Wells, Commun. Math. Phys. 338 , 81 (2015).
- [65] D. Sels and M. Wouters, Phys. Rev. E 92 , 022123 (2015).
- [66] J. Goold, C. Gogolin, S. R. Clark, J. Eisert, A. Scardicchio, and A. Silva, Phys. Rev. B 92 , 180202 (2015).
- [67] A. S. L. Malabarba, L. P. Garc´ ıa-Pintos, N. Linden, T. C. Farrelly, and A. J. Short, Phys. Rev. E 90 , 012121 (2014).
- [68] S. Goldstein, J. L. Lebowitz, C. Mastrodonato, R. Tumulka, and N. Zanghi, Phys. Rev. E 81 , 011109 (2010).
- [69] F. G. S. L. Brand˜ ao, P. Awikliski, M. Horodecki, P. Horodecki, J. K. Korbicz, M. Mozrzymas, and P. ´ Cwikliski, Phys. Rev. E 86 , 031101 (2012).
- [70] Vinayak and M. Znidaric, J Phys. A: Math. Theor. 45 , 125204 (2012).
- [71] [M. Cramer, New J. Phys. 14 , 053051 (2012).](http://iopscience.iop.org/1367-2630/14/5/053051/article/)
- [72] S. Goldstein, T. Hara, and H. Tasaki, Phys. Rev. Lett. 111 , 140401 (2013).
- [73] A. Hutter and S. Wehner, Phys. Rev. A 87 , 012121 (2013).
- [74] L. Masanes, A. J. Roncaglia, and A. Ac´ ın, Phys. Rev. E 87 , 032137 (2013).
- [75] J.-S. Caux and J. Mossel, J. Stat. Mech. Theor. Exp. 2011 , P02023 (2011).
- [76] L. del Rio, A. Hutter, R. Renner, and S. Wehner, (2014), arXiv:1401.7997.
- [77] E. H. Lieb and J. Yngvason, Phys. Rep. 310 , 1 (1999).
- [78] [E. H. Lieb and J. Yngvason, Current Developments in Mathematics, 2001 , 89 (2002).](http://arxiv.org/abs/math-ph/0204007)
- [79] P. Faist, F. Dupuis, J. Oppenheim, and R. Renner, Nat. Commun. 6 , 7669 (2015).
- [80] M. Horodecki, P. Horodecki, and J. Oppenheim, Phys. Rev. A 67 , 062104 (2003).
- [81] O. C. O. Dahlsten, R. Renner, E. Rieper, and V. Vedral, New J. Phys. 13 , 053015 (2011).
- [82] L. del Rio, J. Aberg, R. Renner, O. Dahlsten, and V. Vedral, Nature 474 , 61 (2011).
- [83] F. G. S. L. Brand˜ ao, M. Horodecki, N. H. Y. Ng, J. Oppenheim, and S. Wehner, PNAS 112 , 3275 ((2015)).
- [84] G. Gour, M. P. M¨ uller, V. Narasimhachar, R. W. Spekkens, and N. Yunger Halpern, Phys. Rep. 583 , 1 (2015).
- [85] D. Janzing, P. Wocjan, R. Zeier, R. Geiss, and T. Beth, Int. J. Theor. Phys. 39 , 2717 (2000).
- [86] F. G. S. L. Brand˜ ao, M. Horodecki, J. Oppenheim, J. M. Renes, and R. W. Spekkens, Phys. Rev. Lett. 111 , 250404 (2013).
- [87] [J. Aberg, Nat. Commun. 4 , 1925 (2013).](http://dx.doi.org/10.1038/ncomms2712)
- [88] M. Horodecki and J. Oppenheim, Nat. Commun. 4 , 2059 (2013).
- [89] [J. M. Renes, The European Physical Journal Plus 129 , 153 (2014), 10.1140/epjp/i2014-14153-8.](http://dx.doi.org/10.1140/epjp/i2014-14153-8)
- [90] M. Lostaglio, K. Korzekwa, D. Jennings, and T. Rudolph, Phys. Rev. X 5 , 021001 (2015).
- [91] P. ´ Cwikli´ nski, M. Studzi´ nski, M. Horodecki, and J. Oppenheim, Phys. Rev. Lett. 115 , 210403 (2015).
- [92] M. Muller-Lennert, F. Dupuis, O. Szehr, S. Fehr, and M. Tomamichel, J. Math. Phys. 54 , 122203 (2013).
- [93] P. Faist, J. Oppenheim, and R. Renner, New J. Phys. 17 , 043003 (2015).
- [94] [J. ˚ Aberg, Phys. Rev. Lett. 113 , 150402 (2014).](http://dx.doi.org/10.1103/PhysRevLett.113.150402)
- [95] P. Skrzypczyk, A. J. Short, and S. Popescu, Nat. Commun. 5 , 4185 (2014).
- [96] D. Jonathan and M. Plenio, Phys. Rev. Lett. 83 , 3566 (1999).
- [97] N. H. Y. Ng, L. Maninska, C. Cirstoiu, J. Eisert, and S. Wehner, New J. Phys. 17 , 085004 (2015).
- [98] [M. Klimesh, (2007), arXiv:0709.3680.](http://arxiv.org/abs/0709.3680)
- [99] [S. Turgut, J. Phys. A: Math. Theor. 40 , 12185 (2007).](http://dx.doi.org/10.1088/1751-8113/40/40/012)
- [100] G. Gour and R. W. Spekkens, New J. Phys. 10 , 033023 (2008).
- [101] I. Marvian and R. W. Spekkens, Phys. Rev. A 90 , 062110 (2014).
- [102] M. F. Frenzel, D. Jennings, and T. Rudolph, Phys. Rev. E 90 , 052136 (2014).
- [103] H. Wilming, R. Gallego, and J. Eisert, Phys. Rev. E 93 , 042126 (2016).
- [104] [N. Ramsey, Phys. Rev. 103 , 20 (1956).](http://dx.doi.org/10.1103/PhysRev.103.20)
- [105] N. Linden, S. Popescu, and P. Skrzypczyk, Phys. Rev. Lett. 105 , 130401 (2010).
- [106] N. Brunner, N. Linden, S. Popescu, and P. Skrzypczyk, Phys. Rev. E , 051117 (2012).
- [107] [S. Popescu, (2010), arXiv:1009.2536.](http://arxiv.org/abs/1009.2536)

- [108] W. Pusz and S. L. Woronowicz, Commun. Math. Phys. 58 , 273 (1978).
- [109] [A. Lenard, J. Stat. Phys. 19 , 575 (1978).](http://dx.doi.org/10.1007/BF01011769)
- [110] [D. Janzing, J. Stat. Phys. 122 , 531 (2006).](http://www.springerlink.com/content/726x43802125748r/)
- [111] N. Yunger Halpern and J. M. Renes, Phys. Rev. E 93 , 022126 (2016).
- [112] S. M. Barnett and J. A. Vaccaro, Entropy 15 , 4956 (2013).
- [113] J. A. Vaccaro and S. M. Barnett, Proc. R. Soc. A 467 , 1770 (2011).
- [114] M. Weilenmann, L. Kr¨ amer, P. Faist, and R. Renner, (2015), arXiv:1501.06920.
- [115] N. Yunger Halpern, (2014), arXiv:1409.7845.
- [116] D. Reeb and M. M. Wolf, New J. Phys. 16 , 103011 (2014).
- [117] D. Egloff, O. C. O. Dahlsten, R. Renner, and V. Vedral, New J. Phys. 17 , 073001 (2015).
- [118] M. P. Woods, N. Ng, and S. Wehner, (2015), arXiv:1506.02322.
- [119] F. G. S. L. Brand˜ ao and G. Gour, Phys. Rev. Lett. 115 , 070503 (2015).
- [120] N. Y. Halpern, A. J. P. Garner, O. C. O. Dahlsten, and V. Vedral, New J. Phys. 17 , 095003 (2015).
- [121] R. Alicki, M. Horodecki, P. Horodecki, and R. Horodecki, Open Systems &amp; Information Dynamics (OSID) 11 , 205 (2004).
- [122] R. Gallego, J. Eisert, and H. Wilming, (2015), arXiv:1504.05056.
- [123] [C. H. Bennett, IBM J. Res. Dev. 17 , 525 (1973).](http://dx.doi.org/10.1147/rd.176.0525)
- [124] P. Skrzypczyk, A. J. Short, and S. Popescu, (2013), arXiv:1302.2811.
- [125] [R. Landauer, Physics Today 44 , 23 (1991).](http://scitation.aip.org/content/aip/magazine/physicstoday/article/44/5/10.1063/1.881299)
- [126] R. Giles, Mathematical foundations of thermodynamics , International series of monographs in pure and applied mathematics (Pergamon Press; [distributed in the Western Hemisphere by Macmillan, New York], 1964).
- [127] C. Caratheodory, Math. Ann. 67 , 355 (1909).
- [128] L. del Rio, Resource theories of knowledge , Ph.D. thesis, ETH Zurich (2015).
- [129] M. Horodecki and J. Oppenheim, Int. J. Mod. Phys. 27 , 1345019 (2012).
- [130] C. H. Bennett, H. J. Bernstein, S. Popescu, and B. Schumacher, Phys. Rev. A 53 , 2046 (1996).
- [131] F. Verstraete, K. Audenaert, and B. De Moor, Phys. Rev. A 64 , 012316 (2001).
- [132] T.-C. Wei, K. Nemoto, P. Goldbart, P. Kwiat, W. Munro, and F. Verstraete, Phys. Rev. A 67 , 022110 (2003).
- [133] L. Gurvits and H. Barnum, Phys. Rev. A 66 , 062311 (2002).
- [134] L. Gurvits and H. Barnum, Phys. Rev. A 68 , 042312 (2003).
- [135] L. Gurvits and H. Barnum, Phys. Rev. A 72 , 032322 (2005).
- [136] T. Yu, K. Brown, and I. Chuang, Phys. Rev. A 71 , 032341 (2005).
- [137] M. Ku´ s and K. ˙ Zyczkowski, Phys. Rev. A 63 , 032307 (2001).
- [138] [N. Johnston, Phys. Rev. A 88 , 062330 (2013).](http://dx.doi.org/10.1103/PhysRevA.88.062330)
- [139] S. Arunachalam, N. Johnston, and V. Russo, Quant. Inf. Comput. 15 , 0694 (2015).
- [140] S. Jevtic, D. Jennings, and T. Rudolph, Phys. Rev. Lett. 108 , 110403 (2012).
- [141] M. Huber, M. Perarnau-Llobet, K. V. Hovhannisyan, P. Skrzypczyk, C. Kl¨ ockl, N. Brunner, and A. Ac´ ın, New J. Phys. 17 , 065008 (2015).
- [142] D. E. Bruschi, M. Perarnau-Llobet, N. Friis, K. V. Hovhannisyan, and M. Huber, Phys. Rev. E 91 , 032118 (2015).
- [143] R. Horodecki, M. Horodecki, and K. Horodecki, Rev. Mod. Phys. 81 , 865 (2009).
- [144] C. Eltschka and J. Siewert, J. Phys. A: Math. Theor. 47 , 424005 (2014).
- [145] J. I. de Vicente, C. Spee, and B. Kraus, Phys. Rev. Lett. 111 , 110502 (2013).
- [146] S. Jevtic, D. Jennings, and T. Rudolph, Phys. Rev. A 85 , 052121 (2012).
- [147] K. Funo, Y. Watanabe, and M. Ueda, Phys. Rev. A 88 , 052319 (2013).
- [148] M. Perarnau-Llobet, K. V. Hovhannisyan, M. Huber, P. Skrzypczyk, N. Brunner, and A. Ac´ ın, Phys. Rev. X 5 , 041011 (2015).
- [149] M. Lostaglio, M. P. M¨ uller, and M. Pastena, Phys. Rev. Lett. 115 , 150402 (2015).
- [150] [H. J. Groenewold, Int. J. Theor. Phys. 4 , 327 (1971).](http://dx.doi.org/10.1007/BF00815357)
- [151] [M. Ozawa, J. Math. Phys. 25 , 79 (1984).](http://dx.doi.org/10.1063/1.526000)
- [152] T. Sagawa and M. Ueda, Phys. Rev. Lett. 100 , 080403 (2008).
- [153] T. Sagawa and M. Ueda, Phys. Rev. Lett. 102 , 250602 (2009).
- [154] J. Oppenheim, M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Rev. Lett. 89 , 180402 (2002).
- [155] R. Alicki and M. Fannes, Phys. Rev. E 87 , 042123 (2013).
- [156] K. V. Hovhannisyan, M. Perarnau-Llobet, M. Huber, and A. Ac´ ın, Phys. Rev. Lett. 111 , 240401 (2013).
- [157] F. C. Binder, S. Vinjanampathy, K. Modi, and J. Goold, New J. Phys. 17 , 075015 (2015).
- [158] M. Lewenstein, A. Sanpera, V. Ahufinger, B. Damski, A. Sen(De), and U. Sen, Adv. Phys. 56 , 243 (2007).
- [159] [V. Vedral, New J. Phys. 6 , 102 (2004).](http://dx.doi.org/10.1088/1367-2630/6/1/102)
- [160] M. Dowling, A. Doherty, and S. Bartlett, Phys. Rev. A 70 , 062113 (2004).
- [161] C. Brukner and V. Vedral, (2004), arXiv:quantph/0406040.
- [162] [G. T´ oth, Phys. Rev. A 71 , 010301 (2005).](http://dx.doi.org/10.1103/PhysRevA.71.010301)
- [163] O. G¨ uhne, G. T´ oth, and H. J. Briegel, New J. Phys. 7 , 229 (2005).
- [164] [O. G¨ uhne and G. T´ oth, Phys. Rev. A 73 , 052319 (2006).](http://dx.doi.org/10.1103/PhysRevA.73.052319)
- [165] J. Anders, D. Kaszlikowski, C. Lunkes, T. Ohshima, and V. Vedral, New J. Phys. 8 , 140 (2006).
- [166] [V. Vedral, (2009), arXiv:0905.3057.](http://arxiv.org/abs/0905.3057)
- [167] M. Wie´ sniak, V. Vedral, and v. Brukner, Phys. Rev. B 78 , 064108 (2008).
- [168] M. Wie´ sniak, V. Vedral, and v. Brukner, New J. Phys. 7 , 258 (2005).
- [169] S. B¨ auml, D. Bruß, M. Huber, H. Kampermann, and A. Winter, New J. Physics 18 , 015002 (2016).
- [170] K. Sekimoto, Stochastic Energetics (Springer, 2010) p. 322.
- [171] P. Talkner, E. Lutz, and P. H¨ anggi, Phys. Rev. E 75 , 050102 (2007).
- [172] [G. E. Crooks, Phys. Rev. E 60 , 2721 (1999).](http://link.aps.org/doi/10.1103/PhysRevE.60.2721)
- [173] [H. Tasaki, , 11 (2000), arXiv:cond-mat/0009244.](http://arxiv.org/abs/cond-mat/0009244)
- [174] [C. Jarzynski, Phys. Rev. Lett. 78 , 2690 (1997).](http://dx.doi.org/10.1103/PhysRevLett.78.2690)
- [175] S. Deffner and E. Lutz, Phys. Rev. Lett. 105 , 170402 (2010).

- [176] [H. Spohn, J. Math. Phys. , 1227 (1978).](http://dx.doi.org/10.1063/1.523789)
- [177] G. Huber, F. Schmidt-Kaler, S. Deffner, and E. Lutz, Phys. Rev. Lett. 101 , 070403 (2008).
- [178] S. An, J. J.-N. Zhang, M. Um, D. Lv, Y. Lu, J. J.-N. Zhang, Z.-Q. Yin, H. T. Quan, and K. Kim, Nature Phys. 11 , 193 (2014).
- [179] R. Dorner, S. R. Clark, L. Heaney, R. Fazio, J. Goold, and V. Vedral, Phys. Rev. Lett. 110 , 230601 (2013).
- [180] L. Mazzola, G. De Chiara, and M. Paternostro, Phys. Rev. Lett. 110 , 230602 (2013).
- [181] V. Giovannetti, S. Lloyd, and L. Maccone, Nature Photon. 5 , 222 (2011).
- [182] E. Knill and R. Laflamme, Phys. Rev. Lett. 81 , 5672 (1998).
- [183] T. B. Batalh˜ ao, A. M. Souza, L. Mazzola, R. Auccaise, R. S. Sarthour, I. S. Oliveira, J. Goold, G. De Chiara, M. Paternostro, and R. M. Serra, Phys. Rev. Lett. 113 , 140601 (2014).
- [184] M. Campisi, R. Blattmann, S. Kohler, D. Zueco, and P. H¨ anggi, New J. Phys. 15 , 105028 (2013).
- [185] L. Mazzola, G. De Chiara, and M. Paternostro, Int. J. Quantum Inf. 12 , 1461007 (2014).
- [186] J. Goold, U. Poschinger, and K. Modi, Phys. Rev. E 90 , 020101 (2014).
- [187] J. P. S. Peterson, R. S. Sarthour, A. M. Souza, I. S. Oliveira, J. Goold, K. Modi, D. O. Soares-Pinto, and L. C. C´ eleri, Proc. R. Soc. Lond. A 472 (2016).
- [188] A. J. Roncaglia, F. Cerisola, and J. P. Paz, Phys. Rev. Lett. 113 , 250601 (2014).
- [189] G. De Chiara, A. J. Roncaglia, and J. P. Paz, New J. Phys. 17 , 035004 (2015).
- [190] E. Mascarenhas, H. Bragan¸ ca, R. Dorner, M. Fran¸ ca Santos, V. Vedral, K. Modi, and J. Goold, Phys. Rev. E 89 , 062103 (2014).
- [191] T. Sagawa and M. Ueda, Phys. Rev. Lett. 104 , 090602 (2010).
- [192] T. Sagawa and M. Ueda, Phys. Rev. E 85 , 021104 (2012).
- [193] S. Toyabe, T. Sagawa, M. Ueda, E. Muneyuki, and M. Sano, Nature Phys. 6 , 988 (2010).
- [194] T. Sagawa and M. Ueda, Phys. Rev. Lett. 109 , 180602 (2012).
- [195] Y. Morikuni and H. Tasaki, J. Stat. Phys. 143 , 1 (2011).
- [196] M. Campisi, P. Talkner, and P. H¨ anggi, Phys. Rev. Lett. 105 , 140601 (2010).
- [197] M. Campisi, P. Talkner, and P. H¨ anggi, Phys. Rev. E 83 , 041114 (2011).
- [198] G. Watanabe, B. P. Venkatesh, and P. Talkner, Phys. Rev. E 89 , 052116 (2014).
- [199] G. Watanabe, B. P. Venkatesh, P. Talkner, M. Campisi, and P. H¨ anggi, Phys. Rev. E 89 , 032114 (2014).
- [200] [D. Kafri and S. Deffner, Phys. Rev. A 86 , 044302 (2012).](http://link.aps.org/doi/10.1103/PhysRevA.86.044302)
- [201] [A. Holevo, IEEE Trans. Inf. Theory 44 , 269 (1998).](http://ieeexplore.ieee.org/articleDetails.jsp?arnumber=651037)
- [202] [V. Vedral, J. Phys. A: Math. Theor. 45 , 272001 (2012).](http://stacks.iop.org/1751-8121/45/i=27/a=272001)
- [203] [A. E. Rastegin, J. Stat. Mech. , P06016 (2013).](http://stacks.iop.org/1742-5468/2013/i=06/a=P06016)
- [204] T. Albash, D. A. Lidar, M. Marvian, and P. Zanardi, Phys. Rev. E 88 , 032146 (2013).
- [205] A. E. Rastegin and K. ˙ Zyczkowski, Phys. Rev. E 89 , 012127 (2014).
- [206] J. Goold and K. Modi, (2014), arXiv:1407.4618.
- [207] J. Goold, M. Paternostro, and K. Modi, Phys. Rev. Lett. 114 , 060602 (2015).
- [208] S. Lorenzo, R. McCloskey, F. Ciccarello, M. Paternostro, and G. M. Palma, Phys. Rev. Lett. 115 , 120403 (2015).
- [209] [M. J. Donald, J. Stat. Phys. 49 , 81 (1987).](http://link.springer.com/10.1007/BF01009955)
- [210] [V. Vedral, Rev. Mod. Phys. 74 , 197 (2002).](http://link.aps.org/doi/10.1103/RevModPhys.74.197)
- [211] K. Modi, T. Paterek, W. Son, V. Vedral, and M. Williamson, Phys. Rev. Lett. 104 , 080501 (2010).
- [212] S. Deffner and E. Lutz, Phys. Rev. Lett. 107 , 140404 (2011).
- [213] F. Plastina, A. Alecce, T. J. G. Apollaro, G. Falcone, G. Francica, F. Galve, N. Lo Gullo, and R. Zambrini, Phys. Rev. Lett. 113 , 260601 (2014).
- [214] [J. Hide and V. Vedral, Phys. Rev. A 81 , 062303 (2010).](http://link.aps.org/doi/10.1103/PhysRevA.81.062303)
- [215] [F. Galve and E. Lutz, Phys. Rev. A 79 , 032327 (2009).](http://link.aps.org/doi/10.1103/PhysRevA.79.032327)
- [216] A. Carlisle, L. Mazzola, M. Campisi, J. Goold, F. Semiao, A. Ferraro, F. Plastina, V. Vedral, G. D. Chiara, and M. Paternostro, (2014), arXiv:1403.0629.
- [217] M. Esposito, K. Lindenberg, and C. Van den Broeck, New J. Phys. 12 , 013013 (2010).
- [218] S. Jevtic, T. Rudolph, D. Jennings, Y. Hirono, S. Nakayama, and M. Murao, Phys. Rev. E 92 , 042113 (2015).
- [219] O. Dahlsten, M. Choi, A. Garner, N. Yunger Halpern, and V. Vedral, (2015), arXiv:1504.05152.
- [220] S. Salek and K. Wiesner, (2015), 1504.05111.
- [221] J. E. Geusic, E. O. Schulz-DuBois, and H. E. D. Scovil, Phys. Rev. 156 , 343 (1967).
- [222] D. K. Park, N. A. Rodriguez-Briones, G. Feng, R. R. Darabad, J. Baugh, and R. Laflamme, (2015), arXiv:1501.00952.
- [223] S. Carnot, R´ eflections sur la Puissance Motrice du Feu et sur les Machines propres ` a D´ evelopper cette Puissance) (Paris: Bachelier, 1824).
- [224] N. Brunner, M. Huber, N. Linden, S. Popescu, R. Silva, and P. Skrzypczyk, Phys. Rev. E 89 , 032115 (2014).
- [225] L. A. Correa, J. P. Palao, G. Adesso, and D. Alonso, Phys. Rev. E 87 , 042131 (2013).
- [226] L. Schulman and U. Vazirani, in Proceedings of the 31st STOC (ACM Symposium on Theory of Computing) (ACM Press, New York, 1999).
- [227] P. O. Boykin, T. Mor, V. Roychowdhury, F. Vatan, and R. Vrijen, Proc. Natl. Acad. Sci. U.S.A. 99 , 3388 (2002).
- [228] H. Ollivier and W. H. Zurek, Phys. Rev. Lett. 88 , 017901 (2001).
- [229] L. Henderson and V. Vedral, J. Phys. A: Math. Gen. 34 , 6899 (2001).
- [230] M. T. Mitchison, M. P. Woods, J. Prior, and M. Huber, New J. Phys. 17 , 115013 (2015).
- [231] J. B. Brask and N. Brunner, Phys. Rev. E 92 , 062101 (2015).
- [232] J. Roßnagel, O. Abah, F. Schmidt-Kaler, K. Singer, and E. Lutz, Phys. Rev. Lett. 112 , 030602 (2014).
- [233] L. A. Correa, J. P. Palao, D. Alonso, and G. Adesso, Sci. rep. 4 , 3949 (2014).
- [234] R. Uzdin, A. Levy, and R. Kosloff, Phys. Rev. X 5 , 031044 (2015).
- [235] A. E. Allahverdyan, K. Hovhannisyan, and G. Mahler, Phys. Rev. E 81 , 051129 (2010).
- [236] L. Quiroga, F. J. Rodr´ ıguez, M. E. Ram´ ırez, and R. Par´ ıs, Phys. Rev. A 75 , 032308 (2007).
- [237] I. Sinaysky, F. Petruccione, and D. Burgarth, Phys. Rev. A 78 , 062301 (2008).
- [238] [M. Ban, Phys. Rev. A 80 , 032114 (2009).](http://link.aps.org/doi/10.1103/PhysRevA.80.032114)

- [239] E. Ferraro, M. Scala, R. Migliore, and A. Napoli, Phys. Scripta T140 , 014042 (2010).
- [240] F. Kheirandish, S. J. Akhtarshenas, and H. Mohammadi, The European Physical Journal D 57 , 129 (2010).
- [241] M. Scala, R. Migliore, A. Messina, and L. L. S´ anchezSoto, Euro. Phys. J. D 61 , 199 (2010).
- [242] X. L. Huang, J. L. Guo, and X. X. Yi, Phys. Rev. A 80 , 054301 (2009).
- [243] N. Pumulo, I. Sinayskiy, and F. Petruccione, Physics Letters A 375 , 3157 (2011).
- [244] [L.-A. Wu and D. Segal, Phys. Rev. A 84 , 012319 (2011).](http://link.aps.org/doi/10.1103/PhysRevA.84.012319)
- [245] B. Bellomo and M. Antezza, EPL (Europhysics Letters) 104 , 10006 (2013).
- [246] B. Bellomo and M. Antezza, New J. Phys. 15 , 113052 (2013).
- [247] J. B. Brask, G. Haack, N. Brunner, and M. Huber, New J. Phys. 17 , 113029 (2015).
