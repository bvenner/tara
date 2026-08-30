## Message 1
Okay so I am working on this new project, which is trying to get some super preliminary basic time accounting and capital required to produce the essentials required to produce the daily essentials required for a life in america. (This is mostly with the goal of beginning a housing coop and getting all that to work)
## Message 2
So the first thing would probably be to do a super minimal research review to see if other things are done in this region. Specifically we would want to try and form cooperatives and local community groups that would try and meet some of these needs. But trying to reproduce all of the things an economy would need right out of the gate is obviously infeasible. So there is this question at the beginning of the process about which parts of the process are good to try and implement first. Specifically we are looking for components that are 1) feasible, and dont require a bunch of startup captial, or startup expertiece, and 2) actually provide economic savings over the same services being provided by the market. (One way to try and model this is by giving the internal system it's own internal currency, something like "CHours" for currency hours, so someone can either spend "CHours" making minimum wage to buy the thing directly, or make it themselves.) and 3) to what extent making that item gives the community more independence from the broader structures of the economy around it. (IE producing something like food or medicine inside the coop is more important then iphones, because we don't require them to live, and also food and medicine are flows, you need the items continuously to survive, but once you have one iphone you only need to buy a new one if the old one breaks). But in order to do all this analysis I need to have some ground foundations for what people actually spend their money on, and what labor is required to produce those things.  But before we try and pull things in we should talk through what we actually want to get started with for this project?

## Message 3
I can go ahead and kinda answer all of these 
1. Absolutely strict survivial for now, thats already a huge and massive research project and trying to expand the scope further is begging for failure. Plus its maybe a bit bad to be perscriptive about how and why humans should produce meaningful works of art or human fulfillment.
2 and 3. Hugely important questions I am considering below.
4. Right now the main groups that I am in communication with are already a community neighborhood network of 50-100, but the main reason I am wanting to try and do things at this size is to try and develop scalable approaches that would potentially be applicable to a bigger scale.
5. The big thing that I want right now is some kind of data framework that would be capable of answering personal highly specific numeric questions about how various local production processes are implemented.

As for how to start the programming project I think that doing everything in typescript w/ bun is a good idea just because it has data types right out of the gate which is likely going to be good for keeping me sane, and also it means I have a good pipeline for sharing it with other people.


As for the question services and how to exactly count labor hours, I feel like this is where things get fiendishly complicated. I have a bunch of thoughts about this, and we should absolutely talk through this, but lets go ahead and consider the most simple item we could think about analyzing with this method (All these numbers are real btw):

# Production Example
24x Heads of Iceberg Lettuce

is either going to break down as:

48 USD bought directly from king soopers

or if grown ourselves 

2 months of seedling tray time.
3 months of hydroponic tower time.
0.5 - 10 Unskilled LH (Labor Hours) - Very rough estimate, that is likely to be extremely variable depending on the scale you are operating at, more details below.
40 Gallons of Water
Electricity for Seedlings
Some quantity of Calcium Nitrate
Some quantity of Potassium Nitrate
Some quantity of Monopotassium Phosphate

// However each of these associated inputs have their own cost breakdowns:
# Other Quantities

Water                   - Purchased at 2.20 USD per 1k gallons
Electricity             - Purchased at 0.15 USD per kWH
Calcium Nitrate         - 3 USD per pound
Potassium Nitrate       - 6 USD per pound 
Monopotassium Phosphate - 6 USD per pound

// And stocks, like the implicit "3 months of hydroponic tower time" produce even more complicated breakdowns like 


1 Hydroponic Tower:

16 square feet of land

A pump, and tubing and other misc home depot equipment that can get collapsed to 40 USD - (I think this kinda ability is going to be helpful, just because there is a point where expanding out the production processes for pure stocks becomes less and less helpful )

And at this point either a 

1 Prebuilt hydroponic tower costing 720 USD 

or alternatively

6*23 Hours of 3d printer time. (Each of which cost 600USD, and probably cost 3-4 LH of setup and assembly). Also adjusting the print settings and speed to get this faster might be worth it.
4kg of Black PLA - Currently 11 USD per kg 
4 LH of "Technician Time" - (which itself can be kinda treated like a stock that takes 20 LH to become profficent in)

# Takeaways
And the current thing I am really struggling with is trying to figure out any kind of data structure that we could use to encode this information and network, and I am struggling a bit with that right now lmao. But on the plus side this system should also be flexible enough to encode things like "childcare for 24 kids" potentially without a seperate category for services.

However having done this I think there are a couple things to flag:

### Irreducible quantities 

So in this model when I went to analyze these components, I kept running into the following components that you can't really natively produce as part of a production process.

- Land (in the form of sq feet)
- LH (Labor Hours) 
- USD (Even though this is used to exchange for goods that are too complicated for our system to model the production of it is still a fundamentally irriducible quantity because the nation state you reside in requires you pay your taxes in their local currency. For more information see "Debt the First 5000 Years")

One of the things that is kind of naturally included in these processes is the "reduction" process, where you try to reduce the entire production process of other objects down using that one object. And interestingly enough depending on the one you choose you either get:
- "Production Value" if you choose to reduce everything via USD, which represents the cost to produce something in USD.
- "Labor Value" if you reduce using LH.
This entire relationship is reminding me a bit of the relationship between euler's number, and the infinite tower of homology groups and chain complexes. Namely if you have access to the homology groups you can recover euler's number somewhat trivially:
E(X) = \Sum_{i=1}^\infty (-1^n) |H_n(X)|
But the fact that you have this much more sophisticated algebraic structure, lets you generate these infinite famlies of topological invariants, and work over spaces in such a way that if you can prove if a map between spaces preserves all these invariants, you can show the spaces are homotopically equal via whitehad's theorem.

As for what exactly this "reduction relationship" looks like I am still thinking about it.  If you think about things categorically, its very natural to define a subcategory with the irreducible quantities you want to analyze (ie, "USD", "Labor", or "USD, Labor and Land"), and this comes attached with an inclusion functor into the bigger category. And maybe if this functor has an adjoint, its adjoint to the "reduction" operation. It also could be represented as some kinda category enriched over itself, in which case the reductions might be the representable enriched functors or something. IDK, its still a lot to think about but I think its probably still worth thinking about how this might want to be structured, even if we are almost certainly going to implement it in the computer with something that is much much much simpler.

### The "Time" operator 

So one of the phenomena that kept coming up is a special "Time" operator, for example in the hydroponic tower example, and the 3d printer example. So what are the properties of this exact thing? Well for one it seems to respect combining objects, for example 

T(Hydroponic Tower * 16 square feet of land ) \equiv T(Hydroponic Tower) * T(16 Square feet of land)

(I am using product notation for this right now, mainly because it feels a bit more producty then coproducty, but I am also totally fine to change it later)

The main question at this point in time is how to handle depreciation and repairs. There are tons of different things to think about but my main thing might just be to think of the "Time" operator as not including any element of depreciation or matinence from use. (Its essentially just the equivalent of "store it in a tempature controlled room for an hour"). So a "3d printer hour" might look like 

3d Printer Use Hour:
- 1 T(3d Printer)
- 0.03% chance of requiring a replacement nozzle valued at 40 USD
- Other replacement components requiring an amortized cost of 0.05 USD per print 
- 40 Wh of electricity

Also this lets us fully sidestep the division of things into "stocks vs flows", mainly because under the time operator we can have a really clean definition for a stock, namely:

DEF: An economic object "X" is a stock if the economic object "T(X)" has use value in production processes.

#### Horizontal and Vertical Semimodule Structures of Time.

So one of the things that has been kinda implicit this entire time, is that all of these economic objects, and their production chains have a semimodule (a module, but over a ring without additive inverses) structure associated on them, namely we can scale up and down production using multiples of any n \in N. 

However the operator T interacts with this multiplication in a somewhat 2 dimensional way. We have an ordinary "vertical"  (denoted by x or *) multiplication that parallel utilization. For example, if I need 10xSeedling Tray Base, that would involve 10*"3d Printer Hour", since I could hypothetically if I had 10 3d printers, print a seedling tray that takes a single hour to print. Or if I wanted a single hydroponic tower section that print would take a single printer 25 hours. And we can denote that with the horizontal scalar multiplication &, so that would take 25&"3d printer hour". And for instance if I wanted an entire hydroponic tower section, that would likely take 6 hydroponic tower sections for a total of 4*(25&("3d Printer Hour")).

Its also probably natural to introduce a horizontal composition, in addition to our vertical composition. For example, in the iceberg lettuce example (2 months in hours& "Seedling Tray Hour") cannot happen parallel to (3 months in hours & "Hydroponic Tower Hour"). So those need to be horizontally composed together.

(As for purely physical objects, since they don't have time components you can just collapse both forms of composition are identical, ie 3x"Calcium Nitrate" = 3&"Calcium Nitrate")

Keeping these seperate also gives 2 more invariants/simplifications we can apply the traditional economic simplification, which I can give the memorable name "the 9 women 1 baby simplification", that treats all horizontal and vertical multiplication for all objects as identical. (n*"X" = n&"X").

It also gives you the "shortest possible time" invariant, which essentially discards all the other information in a production process aside from "How long would it take me to get this thing assuming I just started making it now."



### The Labor Hour, and the inherent value of the human experience.

So in an ideal world, we could go ahead and define the Labor Hour, as something like "T(Human)", however the big issue with something like this is that Humans are different from everything else in this production process, in the sense that they incur ethical obligations (and one of the main formulations of those obligations can be worded as: "Always treat humans as ends unto themselves, and never as means", which seems bad considering this is a system for calculating and distributing means), and also this entire thing is set up as a cooperative, which under our formulation means that the voting power you get in the cooperative is directly proportional to how many labor hours you personally contribute, and all of these things lead me to think you need to have a bunch of custom logic/math for dealing with labor hours in particular.

There is always the option of ignoring them, but I think the entire premise of this system is that by trying to come up with a mathematical model that preserves details about the system, you can condense them and get details, invariants and insights into a system that is obscured by more traditional accounting/analysis. Furthermore, since we are studying the material flows of a society of humans, it's not super weird that human morality ends up embedded in some reduced form inside our framework.

However, all this being said it is still really important for our system that we track the material inputs necessary to preform human labor, since making sure those are met is a huge point of this project:

8x Labor Hours:
- 2,500 Nutritious Calories of Food
- 24 & T(Room or other Living Accommodations)
- 3 Liters of Water 
- Access to basic utilities like electricity, internet
- Some amount of Medical Care
- Some amount of USD to purchase other necessities of a good life.

So the main thing I am thinking about is introducing another irreducible unit underneath the labor hour material that kinda encodes the moral worth and democratic responsibility of serving in a cooperative. Maybe calling it something like an "HoL" short for "Hour of Life" that serves as a unit of account for it. So under this new framework 8x Labor Hours would have this production pathway:


8x Labor Hours:
- 8x HoL
- 2,500 Nutritious Calories of Food
- 24x T(Room or other Living Accommodations)
- ...continued...


We can also try to model academic credentials using a similar method, by saying that 

**Go to School**
50,000 USD
8,000 & LH 
=>
1 BS Degree


Then we can say that maybe an activity requires 

- 8 & LH
- 8 & T("BS Degree")

But this still feels pretty messy

### How to handle different production pathways.

Don't have a ton of interesting ideas here, aside from the fact that any reduction process is going to involve some amount of optimization and doing a path search across all different possible production pathways.

However, since we need to handle the analysis between different production chains, we can actually throw analysis of economies of scale under this, explicitly because out multiplication is given by a semiring/ring, and not an invinitely divisible field. So the minimum quantities in:

**Grocery Store Lettuce**
2 USD => 1x Lettuce


**Small Scale Hydroponic Lettuce**
- (2 Months & "Seedling Tray Time", followed by, 3 months & "Hydroponic Tower Time")
- 6 Unskilled LH, (more since there are fixed costs involved with managing resovours)
- ...enumeration continues...
=>
24x Lettuce 

**Large Scale Hydroponic Lettuce**
- 20x (2 Months & "Seedling Tray Time", followed by, 3 months & "Hydroponic Tower Time")
- 30 Unskilled LH
- ...other quantities scale linearly...
=>
480x Lettuce

Note: If we are thinking about ergonomics of this it might be a good idea to programatically declare some of these production processes, where we can put in the quantity of the production that we are wanting to run, and each item can take in a function of the amount of the economic object consumed. So for this instead of needing to manually specifiy you could use something like "F("run quantity") => consumes (5 + 2\sqrt(run quantity) + 0.5 * run quantity) labor hours."

Although I was thinking of this as more of a thing to help with pure ergonomics, fundamentally there is going to be a large numerical analysis problem trying to simultaneously solve all of these constraints, and while you could represent these as a large family of possible production methods, if it is possible to reduce a certain production method to a smooth curve with derivatives could let me introduce some optimizations that might make it easier to compute.

#### Sidenote on Organizational Structures and Building Something that works

After 3 years participating in an anarchist collective, and another 2 years running an ultimately unsuccessful software Delaware C startup, I feel like lots of the discourse online about the problems with organizational structure (especially from people on the left) are really missing the point. My thoughts on this are still really unstructured, but if they could be condensed into a single point:

**Conflict about leadership structure in an organization is almost always directly related to how well an organization is running.**

I am absolutely amazed at people's ability to tolerate (or at least not complain about) absolutely dictatorial and super hierarchical organizations when things are going really well, both financially, (ie steady cashflow, descent profits, and well compensated employees), and interpersonally, (ie, the work itself is meaning)

// Write more here about the importance of preserving a do-ocracy, and prioritizing working with cool people who you personally get along with.


So in some sense this entire project is trying to solve the governence problem by letting leftists actually work on a project that is going to acomplish it's goals. And do so with enough surplus that you don't require people continuously working themselves on an unsustainable level to accomplish those things. Also on most of these projects (particularly in leftist spaces) disagreements don't happen because of deep value's conflicts, its often because we live in an imperfect world with imperfect information, and people interpret this limited information differently. However, when dealing with discussions about resource allocation in cooperatives, there are limited situations where having this data could help resolve conflicts. 


##### Brief Aside on the tightness of markets.

So this might be a gross oversimplification, or just flat out wrong, but it is the framework I am using to interprete the viability of this project.

So in a super classical view of economics you can divide the economy into 2 parts, the market for labor, and the market for consumer goods. People produce labor and buy consumer goods. And companies buy labor and produce consumer goods. And to some extent both of these markets should perfectly balance supply and demand, but in general I think there tends to be a qualtitative oversupply of labor, and a qualtiative oversupply of consumer goods.

For the average consumer it is drastically easier to go ahead and spend hundreds of thousands of dollars buying consumer goods then it is to get any job, even a job that doesnt pay that much. This is also difficult regardless of price, if you look its super easy to end up paying less for consumer goods (its much easier to find cars for 1-2k as opposed to the average 48k for a new vehicle, or spend 80% less on food by buying in bulk and eating dry goods instead of eating out), then it is to raise your wage on the labor market.

Likewise for companies it is extremely rare for the labor market to be the limiting factor on a companies growth as opposed to the demand for the product the company is selling. In the world of startups getting to a point where you are limited by demand is the ever elusive "product market fit" and typically means your company should be valued at 50-100 times the revenue the company makes in a year. There are a few tiny situations in history where companies are fully limited by labor, oftentimes sole popriotirships where the individuals like doing the work themselves and aren't interested in becoming a manager. Or alternatively places where industries are growing rapidly (coding jobs in 2022, nursing in 2026), or the industry is gate kept by licensure programs (MDs, or JD's). 

This is almost certainly not an original observation, and I unfortunately haven't done a lot of reading on why this is the case. But if I had to guess, I think there is a component of it that is due to the fact that labor markets are much much more illiquid then consumer goods markets and it is really important for companies to be able to meet their labor demands in a liquid manner, which tends to result in economic policy that favors a "reserve army of the unemployed". There also might be factors relating to there is a lot more demand for jobs other then as a means to buy money to pay for consumer goods. Specifically around 30-50% of people's income goes towards real estate, either in the form of rent or morgatge payments. Which for the most part doesn't circulate back to labor, and goes into increasing the value held in real estate. Likewise, there is also a demand for people to save, which in turn exists because the prospect of being unable to afford life's basic necessities is a prospect that weighs heavily on people. Where companies (with the exception of REIT's) will often spend a greater proportion of their revenue on labor, either directly through their own wages or indirectly through buisness inputs or taxes. If you think of this as a markov chain, this imbalance could potentially be a reasfor the imbalance. 

But even though I am nowhere near smart enough to figure this out, it does mean that **if** it was possible for a buisness to have a gaurenteed way increase consumer demand for their products every time they hired a new employee that business would be extremely extremely happy.










## Why are we doing this, stability in the modern world, and foreign currency pumps 

One big worry I have doing all the accounting for this, is what happens if even after doing all the economic analysis there essentially nothing is going to meaningfully beat out the production mode of "take a job and then buy the commodity on the open market". And if that is the result, then what was exactly the point of this entire analysis? (Aside from the political goals of local economic independence, and giving the members a say in the structures that govern them?)

Well I think that lots of previous approaches have tried to go with the commune route, where the entire thing is started for and driven by ideological concerns. And the big problem with this is an inherent infeasibility of balancing accounts. Namely these enterprises always have these fundamental structures that cause your external currency USD to leak out of the commune:

- Buy things that would be completely uneconomical for your cooperative to produce. (Either industrial byproducts of existing systems, or things that require millions to billions in startup capital)
- Allowances/Distributions to cooperative members so they can pay for art, and participate in broader society in general
- Pay Taxes

And if you are going to try and build a system like this that actually wokrs, addressing this balance of payments problem really needs to be your first, second, third, fourth and fifth priority, if you actually want this to work.

So my main idea is that if this is really going to work it needs to grow out of a traditional worker's cooperative with decently healthy financials.

So in order to keep the balance stable you need something like a foreign currency pump that takes the raw resources that the coop has access to, primarially LH, and exchanges that for USD. In the unscalable current environment that often looks like early founders working jobs and donating that money to the cooperative. In the medium term that can also look like a situation where people live with us, and we produce and cover their living expenses 


# Short Term Goals

So I talked to a few founders of some local cooperatives and I think the best way to test it is to use it to model their own internal production processes using these methods and test and see if its worth internalizing things that might be immediately up the chain in their production process. (IE for example a bookstore having an addon that does custom printing to steal from an existing example.) This way we can hopefully develop it around the actual needs of existing buisneses and help them calculate their existing expansions and from there actually validate if trying to meet the needs of labor hours directly is feasible.

Another big benefit of this system could be to better model intra cooperative trades, also often referred to as the "solidarity economy". It turns out most people who found cooperatives tend to be extremely committed anti-capitalists, and really do prioritize trying to buy from other cooperatives in the same area to keep money flowing in a community and build alternatives to the capitalist mode of production. But this is almost always done on an ad hoc basis where sometimes the exact market rate is exchanged between the 2 companies, sometimes its done as an "at cost" transaction (which doesn't account for fixed costs like rent). So being able to do something like reduce all the inputs to their base level costs, subtract off all costs in USD and Land, then distribute the surplus among all the workers depending on their LH contributions could be helpful. Or even work out other ways of distribution where resources are distributed in different ways. The advantage of having the complete theory is that it enables you to have a lot more flexibility.

For this particular use case I do think that if I can go ahead and get a working demo of this working for a local coop in the next month or so, I can present the results to a board of local coops and see if I can also integrate their operations into this system.

# Why the fuck are we doing this?

Right now worker cooperatives encompass maybe 0.1% to 0.0001% of the economic output of the US economy. So why has the movement failed in this way?

I originally hypothesized that it was mostly due to lack of financing opportunities, but according to a close friend who has been really insturmental in setting up a bunch of cooperatives, and founded 2 himself. In the last couple years, more prominence and state+federal support have made getting funding for a worker coop from existing banks about as easy as it is for any standard LLC (if not slightly easier). His big hypothesis for the failure of cooperatives looks like 

- When you start a buisness you have the option of forming an LLC (which gives you full control of your buisness indefinetly, and also some tax advantages if you set it up as a passthrough), or a C-Corp (in which case you start off with 100% of the shares, and have all the exact same ways of raising money as an LLC, plus you have the **option** of selling shares to any investors in exchange for money). However, in a worker cooperative there is an expectation that the shares and more importantly voting power are going to be somewhat evenly distributed among employees (this isn't quite true since supervoting founding shares are totally a thing), meaning this is the only structure where you are encouraged to give up control of your business from the get go.




The approach of increasing the number of cooperatives found
