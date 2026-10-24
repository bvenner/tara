# MOAIWI-2

*Cleaned from `Audio/transcripts/MOAIWI-2.txt` (Deepgram nova-3, diarized). Speaker 0 = Nic, Speaker 1 = Brad. Consecutive statements merged; cross-speaker sentence splits rejoined; filler words, stutters, and pauses removed.*

## Nic

There we go. No.

## Brad

I will think about going to put a bird-safe shirt on.

## Nic

You can also just wear a hoodie. You can also just wear your protection hoodie or something. That I need water. That's what I need. I've been — I have in my water. That's what — I'm feeling shaky. Don't know why.

## Brad

The nice thing about semimodules over the p-adics also serves as a barometric space. Hey. Hey. Is that mom's? Oh, never mind. You're good. You may use that glass one. It's not here to — exactly.

## Nic

But anyway, one of the issues that I was encountering with this, Rich Lee, is that hypothetically you actually do want a bimodule over the reals or over the naturals because you explicitly have these discretized quantities. However, part of the issue with that is that — what — you're actually looking at, oh, well, what would be the numerical methods that you would use on a computer to go ahead and compute, like, natural boundaries — to compute solutions for functions between the natural numbers, like, to optimize natural-number-valued modules? But I don't think you need natural numbers. But do you want to know how you do that in the field? You maximize it over the reals, then you search in a — you essentially get — and then you create a dimension space where you essentially maximize over the reals using just gradient descent, and then you just search the discrete lattice around the solution to find the optimal point. Which essentially means you already need to implement — you essentially already need to say that every function of the reals comes from a very nice smooth function on the reals. So you might as well just go ahead and do everything on the reals and then have a final discretization step at the end.

## Brad

In conventional optimization software, there's a fair amount of this, where all the initial software is written over the reals, and then you added — so you had kind of classic optimization, constrained optimization. And then when you added in discrete constraints or discrete elements, now you're into integer programming. So I think that that's where you'd start. Because you don't want to totally — ultimately, you want to use the optimization engines that are already out there. And I think the only difference you're looking at is that you don't necessarily need some sort of scalar-valued quantity in order to optimize over. Or you can let that —

## Nic

Buddy. No. No. Keep talking. No. No.

## Brad

Or you can let that transformation be very dependent. You can customize your linear function for particular applications. So you keep it natively multidimensional, but then you're able to optimize for particular cases by collapsing it with a problem-specific map. And the difference between that and money is that you're at least being conscious about how your trade-offs are being made, and you're subjecting that decision to political processes. Now, Aaron Benanav has really done a lot of work on what he calls the multi-criteria economy. That's one sort of framework you could use if you're looking to just pull something off the shelf in the next month.

## Nic

One second. Sorry. I'm sorry about the —

## Brad

No. That's not food. Let me walk through the food and then walk on next to the curb.

## Nic

I should probably go in my backpack. There's actually somewhat important notes on there.

## Nic

Wait. What were you talking about in terms of something that I could get ready in the next month or so?

## Brad

So Aaron Benanav has developed this explicit model for a multi-criteria economy, and I think you could just repurpose that for multi-criteria impact investing. Sort of use his basic framework. And then that has a direct tie into an existing model for an alternate economy, but also something that could be directly used for impact investing.

## Nic

I should definitely look at that.

## Brad

The other one can look at it for you. Not suggesting you should read it. Let's be real. We got limited time.

## Nic

Look.

## Brad

I'm just saying if you wanted to pull an existing framework out, that would feel like impact investors can have their cake and eat it too. They're going to be like, oh, yeah, multi-criteria impact investing while still basically putting their monetary return back.

## Nic

Here's my kind of beyond situation. Which is that I think there is — the problem with money. This is part of the philosophy of money: the emphasis on the reduction to scalar values. The economy itself is a complicated object. And the thing that's hard is the reduction to scalar values about the economy in general.

## Brad

Well, that and, I think, the complexity of the production function. The limit of the production function is this incredibly complex object. But somehow that process is mediated by money, so that the resulting process that's mediated by money is way more complicated than money. So you get this sort of emergent complexity that you get in language as well.

## Nic

But importantly, the goal of software like this is to understand your impact, not reduce your — there is a difference between the goal of the software being for an investment fund to understand its impact and to reduce its impact to a single scalar. Well, I think for you, it might be your shirt. Cannot. Okay.

## Brad

They've already shit on my shirt.

## Nic

So it can't reduce to a scalar. But, yeah, I think the whole —

## Brad

But that's what he means by — that's what Benanav means by multi-criteria.

## Nic

Well, but the thing is, I don't think — the important thing is that you have multiple criteria, and you're reducing it to multiple scalars. That's not the — the whole part of it is that you can't —

## Brad

But I think you're thinking what you would want to do eventually, whereas I'm thinking what do you do to pitch this to investors. So I think that's the basic step from a single scalar quantity to multiple scalar quantities.

## Nic

But then there's always the more realistic measure — the question of how do I do this? I don't think it's possible to — the money scalar is a super powerful concept because it exists in the data itself. Everything has — at some point in time, in order to calculate a price, you can go ahead and do two things. You can go ahead and take all of the production functions across all of the economy, apply the management decisions that every single firm — that are somewhat optimized, also account for some kind of human error. And then cascade those through to the production chain until you can figure out exactly what is every single component of the price of a bell pepper at King Soopers. Or alternatively, you have a commodity like steel, you can go ahead and just go on the open market and see how much steel costs. You have a chunk of steel. You can go to the open market and see how much it costs. But there's a certain markup property to prices.

## Brad

And the reason that economists say it works is because of that markup property. You don't have to know what all the upstream components are. Everything that you need to know for you is summarized in the price of the — To me, you're looking at the difference between Markov and non-Markov processes. And I think a lot of the reinforcement learning — Markov, partially observable Markov decision process stuff — is essentially just capitalism. You're going with the same assumptions that capitalism uses, which really work pretty well. I think it's a first-order approximation. A partially observable Markov decision process is not a bad place to go. It just leads to problems. In some ways, the question is, could you use that math — the basic reinforcement learning math — without going full on into these obscure power dynamics. This would be the market socialist argument. It's not markets per se that are the problem; it's the political, the institutional structure that overlays those markets that is the problem. So that would be that, yes, we can use partially observable Markov decision processes and reinforcement learning, but we will do that in a much more conscious way and redesign our institutions so those are not captured by forces of people. Or it's the markup structure itself that's the problem. I don't know. My temptation is the latter, or that you should at least start with a mathematical framework that would allow a first-order approximation to POMDPs, whatever those are. But then you could also have these nonlinear — it's basically like a Taylor expansion. Your first-order process looks like a partially observable Markov decision process, but then you've got higher-order expansions past that that can capture some things that are not well captured by the Markov process. But I think that's too fancy for a minimum viable product in the next month.

## Nic

Well, the minimum viable product is also just — one of the things I was saying is a super minimum viable product is also being just —

## Brad

That would be the barely viable product.

## Nic

This is actually something that's even a totally different thing: all of these impact funds are explicitly trying to operate on relatively thin margins. So they don't necessarily have the $150,000 for the state-of-the-art capital management solutions that billion-dollar firms will use. And those solutions don't really work well with them. So they actually are in the market for a $10,000 a year financial services infrastructure contract that's mostly a self-serve SaaS product.

## Brad

So this is the pitch deck for your barely viable product.

## Nic

The barely viable product is me and Rachel, who are the two people who volunteered to go do this, will go ahead and do maybe two to three interviews with owners of these impact funds, figure out, hey, here's the list of all the software we need for that.

## Brad

You said impact funds.

## Nic

Oh, yes. Sorry. Impact investment funds. Go to two or three of them. Figure out the entire tech software stack that they need. Add those to Fortress, and then that's — and then specifically, the entire minimum viable thing is that, well, for that contract, you can either become a member of our cooperative, in which case everyone will contribute to make sure that maintenance on this is maintained, or we'll sell you a contract for like 10k a year or something.

## Brad

Well, I think that's a financial services contract plus maintenance. But I don't think that's going to meet their minimum viable product needs. They're looking for something special.

## Nic

But I'm saying that, in order for something that we could do in the next month that would get me some amount of funding to continue working on this, that would be it. Anything else I bring them is extra, but bringing them extra is good. That's the minimum I have to do. But importantly, if we're going to make this thing work, then having it do more than the minimum is a very valuable thing to do.

## Brad

I think starting out with —

## Nic

Wait. That's your water. My water's over there, and it was out of water. It's been a long couple of days.

## Brad

You did pretty well for somebody that ostensibly is an introvert.

## Nic

I can summon extrovert. One of the interesting things is that a lot of the tests I've actually gotten place me as an extrovert.

## Brad

I think you're a little bit like mom. It's easy to understand these things as extremes, but most people are probably in the middle, and that's probably where you are — in the middle.

## Nic

Like, I feel fine while I'm doing it. But at the end of the day, I'm like, oh my god. The entire weekend of socializing is hitting me very hard.

## Brad

Well, and I think mom is the same way. She just has a lot of energy, so she can go out and do all this.

## Nic

Oh, I think that's also a secondary part of it. I can talk forever. But it's also harder for me to talk at these events than it is to just shoot the shit with Miri, for example. Good. I'm going to lay down again. I'm going to lay down on the couch. Providing something else of value is important. And I do think there's an issue here, which is that things like value are subjective. Price is the only scalar reduction of the production function that is objective.

## Brad

But the thing is, Nic, that I don't agree with is that prices serve as a continuously variable language that has emergent properties. The fact that language itself is governing the process — it's not like there's some exterior process that's mapping to value. The flows are realized by value. So that's why I feel like it's like studying — you couldn't study a society by looking at their language. You have to look at the overall social process. And the sort of communications that the real-valued scalar allows is very different than what you're talking about. There's not some external viewpoint you have where you say the entire economy is trying to maximize a single scalar function.

## Nic

That's economy. Accounting says businesses are making individual local decisions about what's profitable. But — one second. I'm glad you brought this up because this is not necessarily what I am saying. What I'm saying is that the function of money in the economy makes price such a different quantity — it gives price mathematically unique properties that exist for no other value. So, importantly, let's say you're trying to calculate some other thing. For a specific product, you're trying to calculate what the labor hours are in the product. How many labor hours does it take to produce that Framework laptop? In order to figure that out, you need to computationally reduce it from the production function.

## Brad

But that's an external point of view. That's the economic point of view. The internal business point of view is actually way, way simpler than that. It's like each step has to be profitable.

## Nic

Each step has to be profitable, but importantly, if I want to know the price of that Framework laptop in particular, I do not need to do any functional production. I do not need to do anything regarding the production process. I can know the price of the Framework laptop and be blind to the entire production process by putting it on eBay and seeing what I can get for it. So that's one of the things. If, as an impact investment fund, you're wanting to calculate things like how many acres of forest are we saving through our impact fund investments — because that might be a number for that — you are guessing in every single number and then trying to back-propagate all those numbers forward. And importantly, because you don't have the entire production function, you are missing out on lots of detail. And they're needing to insert a bunch of estimates. But then at some point, the fact that you are inserting estimates and have no ground-based truth always means that it's like, well, how do you know how many acres of forest are saved? And the answer is like, oh, well, the researchers' analysis. But with accounting, there is a base floor: at some point in time, the value of your assets is determined by the market price of the assets.

## Brad

It's kind of, sort of. I think cost accounting is where the map between the real world and the accounting world is — the world of cost accounting. So those cost accounting functions are not observable.

## Nic

But on the other hand, they are potentially partially observable. The cost accounting of a business exists in the combination of the prices that the service makes and the revenues that flow out the door to investors. The black hole between both of those is the cost accounting, and that's why prices contain a lot of information about the cost accounting of the business. And there are really basic constraints, like the company is still in business,

## Brad

so that puts a constraint on their cost accounting. There are things you know just by observing. But I think there are things like financial statements and other things you can get about businesses that give you a much more detailed understanding of cost accounting, but it's always a partially — "partial" covers a big space, so it's extremely partially measured.

## Nic

And I do think that there is definitely a lot that you can do via applying all the sets of — how do I say this? All of the financial statements of every single company in the S&P 500 gives you a lot of financial constraints. And also the material constraints of physical — the physical reality of these production processes as they exist in patents also gives you a lot of other constraints. And at some point in time, you actually end up with an overconstrained problem. So you can probably eventually — I'm curious to what extent is that, if you actually have all of the financials of the company and a lot of information about the broader economy, including things like, oh, well, how much are they renting all of their different stores for? You actually probably can get — and you go ahead and also apply a lot of constraints based on, oh, yeah, well, at some point in time the market — you also have all of their financials. You have all the prices that they're doing their real estate for. If you have a business, you also have the prices of every single product that they're making because they're actively selling those products. And you also probably know the wages of their employees because you have at least a decent estimate of where all of the wages start. These things are for sure. Those two prices maybe don't exist, but you probably can get them with web scraping.

## Brad

Maybe. Or you just say, here's our total uncertainty. You can feel comfortable estimating each other. But I think you get a lot of — what is the predicate transformer view of probability? Which is: you've got an observation, now you're inferring states from those observations. So I think that's your base. It's not Bayesian because it's a Markov process, but it has that sort of reinforcement learning idea. So I feel like ultimately reinforcement learning algorithms are directly applicable to this problem.

## Nic

Well, that's the only way that you could solve constraints with billions of dimensions is using gradient descent. One of the things that's interesting about this product is that the math that you can use is limited by the numerical methods — the efficient numerical methods that exist in 2026.

## Brad

But there's lots of CPU-based — purely solving objective-constrained optimization problems. But there's also this more LLM kind of gradient descent, where it's more decentralized.

## Nic

Well, the thing is that gradient descent can essentially — the end result of a gradient descent model is you can encode a manifold inside of any space via a gradient descent function. You can encode a manifold inside any latent space with a gradient descent operation, rather. And you can also optimize and do results on those constrained optimization manifold problems using gradient descent very efficiently. So, yeah, the fact that gradient descent by neural networks essentially let you select manifold spaces and then let you do gradient descent on gradient descent essentially makes operation on those manifolds very numerically efficient. And I think that you can go and do this, which is why I definitely need to learn a lot more homotopy. But I don't think that's the place to start. I think that in general, knowing homotopy will make my decisions and my mathematical taste of this better. It'll improve my research taste is one of the things I'm trying to say. I'm skeptical.

## Brad

I'm still willing to say the ultimate solution is ∞-categories. I'm just not sure you don't want to go do the 2-category first and then look at the infinity.

## Nic

Importantly, what is — our main base is the R-module. And I think there's also a reason that the important basis is — or I shouldn't say — it's the R-module over rigs. Getting rid of inverses is very important. I think the reason that getting rid of inverses is very important is rigs. Or — what I should say is minimum order quantities.

## Brad

The good thing about this — the rig over the real numbers is it's a very straightforward generalization of the Boolean rig. So there's a lot of properties that you're generalizing for Boolean algebra. But the step from Boolean algebra to the partially observable Markov decision process is pretty small. So there's that potential to serve you using the same math from conventional probability theory, but making it work more in a metric space. Obviously, measurable functions is a very — that's a particular form of metricization, but that's still a metric space that's put on the Boolean algebras. The sort of probability are all basically just axioms of Boolean algebra with some specificity for how you proceed to infinity.

## Nic

But — well, let's go ahead and think about this from a perspective. Let's just look at the most basic thing. Let's say that you want to order a custom CNC part from China.

## Brad

And let's say that you go ahead and negotiate with the seller. But before you go too deep in the detail, I think you brought up an important point that's a counter to what I was saying, which is that as an impact investor, you're always taking that exterior view. The business has privileged information when they make their decisions, and as an impact investor, you're never going to have access to that privileged information in the monetary economy.

## Nic

Now, one of the things — you get access to a lot of that privileged information through due diligence.

## Brad

It's kind of — but I think one advantage of the cooperative economy is there's potentially a greater transparency. The transparency the impact investors have into the operations of the business just doesn't rely upon these black-box costings.

## Nic

And this is what was absolutely wild about that meeting. First off, if I had said something like, "Hey" — if I bought a bunch of headphones in the room — "Hey, I think all of you should share your books with each other," they would have killed me on the spot immediately. Like, do not pass go, do not collect $200. But I brought up the fact that it might be good for all of us to just go ahead and share our books and figure out some mathematical insights from this. And everyone was like, oh my god, that's such a good idea. There have been a couple of people who have been saying that we should do this for a couple of years. But no, this is a thing we should be absolutely doing right now. And the reason we haven't done it is mainly just because we haven't really had a quant on board who could do it.

## Brad

Say more about your process because I'm not totally following what you're —

## Nic

So what I'm saying — let me ask — sorry. Sure. Sorry. The investment companies that want to share books among themselves — the impact investors want to share books among themselves in a way that hedge funds would just never do. So that's an advantage already.

## Brad

That's a big advantage. Because they could share a calibrated impact model, and you can start proposing that as a standard. Here's our standard for measuring impact investing. You could potentially end up getting your solution adopted as a standard.

## Nic

Well, and there's also another thing, which is that if you're wanting more due diligence out of your fund, you can say that a requirement for making money from this is that you go ahead and use this tech stack. And this is even potentially good for you because it's a service we're providing you along with your investment — all of this financial software that we can also potentially use for taxes and other things like that. And that's also helpful for building the solidarity economy at this impact fund level.

## Brad

I think, again, that the visibility of the impact funds into the solidarity economy is still an open problem.

## Nic

It's not great. I'm not sure you'd need it. It's not great, but the thing is — how about this? The impact investors have power, which isn't money. They could force whoever they get results from to do whatever they want. And fundamentally, this is a small ask. And they can tell the solidarity economy what they need in terms of transparency in order to make their case for solidarity investing being more sustainable. And also, importantly, you get the solidarity economy data for every single person who is applying for your fund, not just the people who actually get your grants.

## Brad

I think that's a bigger ask for —

## Nic

Organizations will sell their souls for capital. Is this a bad — you have to be a little bit sensitive to the —

## Brad

No. You do have to be a little bit sensitive. I would say you're more interested in their operations data than their design data. But if they're willing to share their operations research with you?

## Nic

No. I don't give a shit about their operations research. I give a shit about what their financial flows and what their material flows in their company look like. But the bad news — the people applying to your fund don't know that yet. They don't know what their material flows are. They only have their stereotypical books you would need for normal tax accounting.

## Brad

They may not be a company yet. They're going to you, and they're asking for money. They're not at all inventions.

## Nic

Well, maybe. It's just that most of the time, the people who actually get the money already have a business that is already decently making money.

## Brad

And I think that you ask for sort of broad due diligence stuff that's consistent with what other impact investment funds were already asking rather than —

## Nic

For sure. But importantly, those internal company books are very valuable to feed into your thing. And importantly —

## Brad

But I don't think you have to force them to give you their —

## Nic

Well, how do I say this? If you're a very large company, Google has internal books that are not part of their due diligence process as part of a shareholder group. If Moon Shell went public, Moon Shell would not have enough — so if Moon Shell was wanting to do part of an M&A process, the books that would be required for them to turn over in an M&A would be all of the books that they have. Because if you're a small business, there are so many things you do not need to keep books on. But in every single merger and acquisition, they want at least the basic books. But importantly, if you're a small company, all of your books are basic books. You get what I'm saying.

## Brad

But you're confirming what I said. You're not asking for more than what is already the industry standard.

## Nic

Oh, yeah. But importantly, the industry standard for a small business is everything you have. Or at least, if you get to the second stage of the process, obviously you don't need to turn over everything at, hey, we would like money. The M&A process — by the time you're getting to the actual due diligence process, you're expecting the deal to close at least 70% of the time. But you're asked for it. If you get the money, we're asking you to use the tech stack and give us greater observability into your —

## Brad

If you get it.

## Nic

Yeah. And I think that's the big ask that we can potentially go ahead and work with. What we're trying to do is a good thing here. We need to not lose sight of the thing that we are trying. We are not trying to build a surveillance state inside of the movement. We are being very explicit that the observability is also trying to help you avoid taxes. Because, fundamentally, we're in the business of money laundering. But I think we can be very explicit about this. And I think that this is a thing we are trying to do as part of building the quantum economy. This is a very explicit part of what we're doing here. Hell, if it actually gets big enough, we will have voluntary sign-ups. I can be so sure of that.

## Brad

And again, I think you're looking for some way to split the dichotomy between an internal function of a larger corporation whose books are totally transparent to the rest of the organization, and two different firms whose books are totally opaque. You can have a gradual privacy unlearning — I'm not sure what to call it — where you reveal more of your information to your collaborators.

## Nic

I think that there's plenty of supply chain work already that's doing this. But also certain elements of shared books. But also there is an argument, especially among cooperatives, that sharing your books is not — I don't really know if there's any incentive for people to privatize — there is a culture in Silicon Valley for keeping your books private because keeping your books private is an essential part of building hype about your company. But even then, that's not the case because there's lots of companies that have been very successful that have had public books the entire time. But for some people, it's very good for you to release small screenshots from your books and have that become headline news. Like, if Anthropic's books were fully open, Ed Zitron wouldn't be Ed Zitron, and all of the newspaper columns would not be able to write op-eds about what exactly their profits are. The fact that their books are not transparent is a marketing strategy for a lot of companies. And especially in a backroom in Silicon Valley, it's essential if you're raising money to just screenshot, screenshot, screenshot. These are the investment figures we have. We're changing the world, and that creates buzz about your company. And then by the time the investors look at your books and they're just like, ugh. If you just open release your books to everyone, everyone just goes like, ugh, and you don't create the investor demand. In order to raise a good round, you must create FOMO among investors in Silicon Valley that if they don't get in on this round, they're going to lose the deal of a lifetime.

## Brad

But I don't think you need to bring that much. Let's say you want to double the impact investing amount under management. You're only raising an additional $50,000,000.

## Nic

Raising 50 mil is peanuts. It's a little bit like, seriously? That's what you got in there? I think that taking on market rate capital now is a bad idea. I would be worried about taking on market rate capital right now. But taking on market rate capital in like three years, when the ten-year is at like two percent, I think it's probably fine.

## Brad

It's ultimately going to be a little bit of an adversarial relationship with your monetary investors. You know it's going to be a fight with them because they're going to want more from you than you want to give. On the other hand, you want to give them enough that they feel like you're telling a truthful story.

## Nic

Oh, wait. Who are you talking about?

## Brad

So I'm saying — your funds under management that are going to be provided by investors, those investors want transparency.

## Nic

About what you're providing? I think you can provide that to some extent. Most of the donors you're offering money to are philanthropic ventures. If you're coming here to — what? Can you get your phone? Okay. Are you eating a shirt? Fucking —

## Brad

You're such a fucking asshole. Fuck it. Point.

## Nic

Go away. I feel bad. I scooted Mona off of the bed. Is this bird safe?

## Brad

Yeah. My shirt's in bad shape. So I think some areas of research are kind of existing functions for shared accounting in the cooperative space, because it sounds like there's — I know of at least one, and it sounds like there's several more. So I think that's something to look at in the next month. I think you kind of — looking at the basic, how to host your stack and what that stack looks like is another place you're going to have to do a little bit of research. And then how you think about the measurement problem. And if you don't — and then making the case for where investing in cooperatives is a more secure and reliable investment than investing in the monetary economy.

## Nic

Well, I feel like there's an understanding that cooperative investments are probably never going to give super good above market rate returns. But importantly, they don't really have to. But if they have greater resilience, then it's a hedge. But also importantly, if you're pretty confident that your cooperatives can generate like a 4% market return instead of like a 1% market rate return, you can count on philanthropic ventures. There are two scenarios here that are pretty important. Let's say that you have a philanthropic organization that is willing to invest in your portfolio — that is willing to do your impact investment fund. We could say, okay, then fine, we'll buy bonds for you at 3%. And let's say that all of your small businesses that you're wanting to get started could really only get started if you're offering — but you're not as committed to bond versus equity at this point with the dividend. Let's just say that all of the financial instruments that you would be selling to cooperatives have an expected return of like 0%. And after lots of conversation with your community, you have figured out that 0% is like the only way your fund can really achieve its mission objective is by giving loans at 0%. But you can only raise money at 3% return. How do you solve this?

## Brad

By grants.

## Nic

No. There's a way to solve this without grants. Well, yes, you can use grants to cover the difference in returns for sure. But how do you solve this? You're like, we're a Ponzi scheme, but we know we are. So there is absolutely a way to solve this with grants, and that's what they're saying at the table. There is a way to solve this without grants. Do you want me to do the rhetorical bullshit or just tell you what the answer is?

## Brad

Just tell me the answer.

## Nic

The answer for this is — I forgot to even tell you the answer — which is that treasuries yield 6%. So the answer for this is that you construct a portfolio that consists of 50% treasuries and then 50% zero-interest loans. So the entire bundle has a return rate of 3%. So then you're just done in that regard. Let's also just go ahead and say that maybe you have a bunch of grants. Let's maybe say that you have lots of grants. If you have the same situation, but you can't necessarily lend the money out — one of the things that you could do is borrow money, which is also probably going to be at like 9% or something similar, and then you can potentially go ahead and sell some of this out. This, on the table, just sounds extremely risky. No. I don't — because that will definitely wipe you out real quick. Or another thing you could do is also raise money from the community at potentially a lower rate too, and then use that to cover grants. But if you have grants — the entire point of this is that if you have a lot of grants, you might be able to get philanthropic money at a 5% level and then also lend it out at a 2% level. That's another thing that you can do, and then use grants to cover the return difference. Both of these methods are just ways to convert money now into money later, and to adjust the interest rate up and down. But importantly, if you're cooperatives —

## Brad

But even a 0% interest rate is still going to require a monetary payback from your cooperatives. So that's very impatient capital.

## Nic

Well, not necessarily. The payback time doesn't necessarily impact the expected rate of return. Now, admittedly, part of this is developing a kind of patient capital, but fundamentally, as long as you don't liquidate it on your books. The main thing that every single fund is trying to manage is every single fund is a bank, and every single fund can be dissolved via a bank run.

## Brad

You don't necessarily need to leverage your deposits in order to lend that money to your cooperatives, but you could.

## Nic

But I think you might have a higher requirement as an investment impact. Well, the thing is that when you lock this up — in every single hedge fund contract, it's like, you can invest money with us. You can draw it within any time. We also reserve the right at any point in time to pause people's withdrawals. That's the fine print in every single contract. So that's obviously just a nice convenient thing where it's like, if you want to withdraw your entire portfolio, you could withdraw your entire portfolio. But if the market is getting turbulent and everyone's requesting their max withdrawal, you could also maybe say, oh, well, you can withdraw maybe 10% of your portfolio a month or similar. And if you get a month where everyone's withdrawing their max withdrawal amount, you could just say, hey, a lot of these bonds — we have a lot of these very illiquid assets that we couldn't sell in the open market. We're just pausing withdrawals right now. This is leverage. This is not leverage. So ideally you want that to change. Everything above that line is not leveraged. Everything below this — everything above that line is not leveraged. And there's also the idea that — and obviously public banking or other potentially low-interest — this is actually one of the things they were talking about: the public banking people and these people need to collaborate a lot more. An advantage that Mobos has is a lot of context in the public banking space. And I think that this software could also be of a lot of potential use to them, especially because public banking has a similar thing of, oh, well, we have a big pool of below-market-rate interest money. How do we go ahead and allocate that efficiently? But you're still ultimately looking for investing in businesses that will eventually make a profit. But part of this is that you can ensure that those businesses will make a profit right off the gate through your market research. It's part of the idea for this. So, in most situations, you might go ahead and say, hey, we're expecting these cooperatives can really only make it off the ground if they have a 0% interest rate. But these cooperatives that we've essentially identified in this market segment will have customers right off the bat, and will have a decent pathway to profitability based on the economics of similar firms that we've analyzed in the area. We're pretty confident that they would be able to return a rate of like 3% to 4%. And you can get that by a combination of lower interest rate bonds plus equity. The whole point is that this is an expected rate of return. And the way that you get this without being damaging is you ask for equities. Because bonds have a fixed cap — bonds have unlimited downside and capped upside, and stocks have capped downside and unlimited upside. That's how those work. And they in turn get different stability. So if you're explicitly investing in businesses that you have done market research on that you think have the potential to perform extremely well, it makes sense for you as a financial company to ask for equity and not bonds. And if you think a company's going to do very badly, you want to ask for bonds and not equity.

## Brad

The other thing is that you're hoping that when you make investments and that company is taking capital —

## Nic

Are you Cheepy? Cheepy. Is he okay? He might have something stuck in his throat. He's on the planter. Oh, yeah. You have something stuck in your craw. Here. Uh-oh. Are you choking? Are you choking, Maria? Are you breathing? I can't tell. Okay. I think you're breathing. So I think that that's part of the idea for all this.

## Brad

I can see why they thought you were a quant.

## Nic

What?

## Brad

I can see why they thought you were a quant.

## Nic

Well, I am a quant.

## Brad

How I learned to stop worrying and become a quant. Says my journey from theoretical math to quant-hood.

## Nic

How to become a quant without selling your soul? I think that this is good shit. You guys read those stories about theoretical physicists who go work for Jane Street and make a gazillion dollars as a quant? That's me except without the bill. I am making barely enough to live in a 40-foot container in my parents' property.

## Brad

Your dream is — I live in a 20-foot RV on my parents' driveway. My dream is to be able to get a 40-foot container in some remote spot that still has internet access.

## Nic

That would potentially be a funny tagline for a book. But, yeah, no. I think that this is potentially valuable just because I know there's immediate market demand for this. At some point in time, we are probably going to have to take a gamble about, well, how would we actually implement this successfully? Because the fact that this doesn't exist right now is an indication that the problem is extremely hard.

## Brad

But conventional investing firms have these models.

## Nic

Conventional investing firms do not have these models. And the reason that they don't is because they are focused on maximizing a single scalar of value. The only firms who do not have this need are public banking firms and also impact investing firms. In some sense, not only do regular traditional investing firms not have these — it would be illegal for them to implement it if it existed, because they have fiduciary obligations.

## Brad

But a big part of what you're doing as a fund is you're looking for, what are your potential correlations? If you get a market downturn and half of your cooperatives go out of business —

## Nic

But that's a risk in every hedge fund. That's why it's a big — or volatile. But you're analyzing those risks. But I also think that that's going to be less likely for most businesses.

## Brad

Well, I think this is where you try to sell cooperatives as a resilient investment or as a hedge. That cooperatives rarely go out of business. They'll cut down hours. They'll do things that a regular business would —

## Nic

So, like, the fact is that, structurally, they make way less risky decisions than a regular business. They tend to not be over-leveraged. Like, a regular business would have no qualms about this, and I'm like, oh, that looks fucking scary. So, like, it's easier to go in one direction than the other. But I think that you could also maybe do some public banking stuff too. Public banks have the same problem, right? Because if you're just going to loan out money the same way that the conventional system does, what good are you doing? Whereas what you want to do with the public bank is actually not feel like you've got to maximize — just because you can use leverage doesn't necessarily mean you have to be risky. One of the existing ways the impact funds will do is they will raise grants, and then they will loan out those grants. But one of the things you could also do is maybe say, well, whatever money we raise in grants we'll add on an extra 10% of debt and then fund all that out.

## Brad

Well, and I think your goal is growth. You're actually trying to grow the solidarity economy as quickly as possible.

## Nic

And there's also a big part of that is that, in general, if we can get the average return on these funds' investments from growing at 0% to maybe growing at 3% to 4%, that's good for them because that means that their portfolios are growing 3% to 4% a year. And they're probably actually maybe even beating inflation at 3% to 4% a year.

## Brad

Well, you can promise 3%, but you want to overdeliver, obviously.

## Nic

Obviously. There is a part of me that's trying to not say, we're going to deliver you 10% returns. I'm definitely not trying to say we're going to deliver you 10% returns a year independent of market conditions.

## Brad

Oh, absolutely not. Because ultimately you're a fund. You're not saying you're never going to go negative.

## Nic

Well, every single firm goes negative at some point unless you're — the number one indication that you're a Ponzi scheme is that you're always positive.

## Brad

You guys mad at me for shooing you off. I'm gonna go hide in our cage with the heat lamp. Moon is like, this is the warmest spot in the entire house. There's two heaters — three heaters — the intersection of three heaters. Are you smart? Have you figured out the warmest spot in the house? I think the spot directly underneath the heat lamp is hotter. Oh, that could be. It could be that Ria's just being the selfish bastard that a rooster is.

## Nic

Are you resting? I think that spot — that spot's more comfortable than the top of the heater, though. That perch.

## Brad

I'm too warm. No. She's thirsty.

## Nic

But yeah, no. I think that that's — I should — that or lower the rope, because that's a bit of a reach to get the water.

## Brad

I was like, I will bask in the warmth of my heat lamp like the lizard that I am. Well, the good news is there's lots of people interested in working on the solidarity economy side of this. So is it stuff that can be very specialized as a layer over that?

## Nic

Well, one of the things that's valuable is that once this gets big enough so that the alternative currency is valuable, you will have so many people busting down your door to get in on this. But I wouldn't call it alternative — I would call it —

## Brad

It's not an alternative — you need a word for what this shared equity model is.

## Nic

Yeah. I need a word because you don't want to call it currency. It's like it's not — it's an alternative production model. You can go on Marxism and call it an alternative production model.

## Brad

It's a cooperative supply chain.

## Nic

It's a co-op — that's a good way. So once it actually gets to the point in time where it's a cooperative supply chain, people will be busting down your door. But the big issue for this — and I think the big issue that Bob had — is how do you go from a bottle of this bullshit to a cooperative supply chain? And the answer for that is that these impact investing firms are the middle step in that process. Possibly. I think it's an excellent idea. I think it could pay off. The idea of quality rating has been upgraded to excellence.

## Brad

No. I'm not saying excellent. But I do think, because you're going — the thing that mom likes about it is you're going where the money is. So this makes sense. Mel's whole group, she's calling it pirate communism. Which is you put on a cloak, and you go out to normies and you get their money, and then you use it to develop the cooperative economy. What you're doing is very much in that vein. You're going and presenting your proposal to normies who are out there, working in the conventional economy, and saying, do you want to get in on the cooperative economy here? The ground floor. So do you have a test for me today? Or —

## Nic

Well, yes. This got good enough after we did it for a while that we should probably go ahead and record it.

## Brad

I thought you were recording it.

## Nic

I am recording it, but it's good enough to keep now that we decided to record it.

## Brad

I also think we could write up a short prompt.

## Nic

Yeah, I agree. That doesn't need — but anyway, we should go ahead and pause this right now. One of the things that would be nice is if we also got a decent way of actually doing this shit. Or I should not say this shit. What I'm saying is a good way of actually transcribing these notes and things that is in my phone. So we might just want to go ahead and work on that flow. We could also go ahead and do some lean exploration, but —
