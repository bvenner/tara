# MOAIWI-3

*Cleaned from `Audio/transcripts/MOAIWI-3.txt` (Deepgram nova-3, diarized). Speaker 0 = Nic, Speaker 1 = Brad. Consecutive statements merged; cross-speaker sentence splits rejoined; filler words, stutters, and pauses removed.*

## Brad

That's okay. We can get started. It runs in like two minutes, in which case then I'm only saving myself two minutes. That's okay. But anyway, what is the main thing that we're thinking? I want you to just describe at a super high level what the goal of MOAIWI is.

## Nic

There's a couple of things for this, which is that this project has short term, medium term, and then long term goals. I think we can put all three of those on a pitch deck and yet have some deliverables that are just on the short term side. I'll go on and start with the short term side since that informs most of what we have to do. So in a month, there are going to be all of these financial services companies. I know when I say financial service companies, they are specifically impact investing funds, who are kind of looking for a method of financially analyzing their investments. Let's go ahead and put the phone closer to you because you're quieter. Part of the problem that these financial analyst firms have is that there is, in some sense, demand for software that does not exist regularly. Because if you, as a financial services company — a normal financial services company — you are obligated by your fiduciary duties to not consider anything other than stock returns or than the average geometric rate, like the geometric growth rate of your fund, essentially.

## Brad

Right. The return to capital.

## Nic

The return to capital. Thinking about anything else is basically illegal. Like, by law it is illegal, and you can go to jail if you consider other things. As such, pretty much all accounting software is very much designed around keeping track of money flows, and it's not designed to keep track of material flows, which is an opposite because all of your internal stuff is denominated in terms of dollars, and the only thing you really care about is the dollar return. So in some sense, your entire system can just be reduced to a single scalar-valued dollar. Impact investing funds have different needs because their big benchmarks for success are both monetary. In some sense, their requirement as a fund is satisfying a certain demand: they want the fund to not go bankrupt, and they want the fund to exist for a long time, like we do, which also means they need to pay back their existing bonds. Importantly, that is a satisficing demand on capital, not necessarily a maximizing demand on capital. And then the thing that they're optimizing for given that satisfactory demand is the material betterment of their community. And there's no existing software. So this is a problem: a lot of the existing tech stacks and solutions essentially don't work with this. If you're trying to figure out if an impact fund is having a good return on its investment, that's a thing that's very hard to calculate. There aren't really any good tools for calculating it, and that's a problem that they would like to fix.

## Brad

One short term goal for the LLM is to look at this notion of returns to impact investing, and we would like you to look broadly at impact investing and not just impact investing within the solidarity economy, because this is just one aspect of impact investing.

## Nic

One second, sorry. I'm in the middle of composing a text. I'm really sorry about this. There we go. I have successfully replied to my stuff.

## Brad

Since there is likely a fair amount of work that's been done on this problem — because impact investing is an idea that's been around a long time — chances are the value you can provide is not necessarily that particular tool.

## Nic

It's integrating that tool into a larger system, but I think there's also a secondary thing, which is that most impact investment funds are smaller than big funds. There's a couple things that make this work out in a valuable way. A regular fund can just scale up indefinitely. It just gets more and more capital, and it hires more and more managers. And those managers are judged based on whether it's a good thing or not in terms of investment returns. Impact funds have a really hard time scaling up because the whole point of an impact fund is that we have a bunch of people who are experts in the local community, and we can go ahead and figure out what to invest in that will benefit the local community the most. So in that way, if you go from managing $2,000,000 to managing $200,000,000 — the community will get a lot better, but where would you put all that capital anyway? The whole point of the community is to make the community significantly better for not necessarily that much investment income. So scaling them up to have a massive amount of investment income is not necessarily good considering that they're only able to apply that in their local expertise of their kind of local area. So in that way, most of the impact investment funds tend to be hyper local and very small. There is also a secondary problem with this, which is that most of the existing software suites that hedge funds will use to manage their portfolios typically have a yearly contract rate in the hundreds of thousands of dollars a year. And the rationale for this is that an impact fund managing $2,000,000 will be like, "no, we can't afford that." We have one part-time person we're paying a $20,000-a-year salary, and that's our entire back office budget spent.

## Brad

Which is good, because that's about 1% of 0.1% of the expenses on your funds managed, which is a very reasonable level of overhead.

## Nic

It's a very reasonable level of overhead. Is that right? 20,000 to 2,000,000. The LLM can do the math on that. And typically, they'll charge you some percentage of returns. But they don't necessarily have 300K to blow on a software stack. That's part of the issue. And this is also true of a lot of their other different kinds of tech stacks that they would be managing. So there is potentially a big demand for this kind of thing, at a very base level. If we're thinking about what we would be delivering in the next month or so, it would be a prototype version of that stack — an actual prototype of that stack. Plus glimpses of the future into this alternative finance thing.

## Brad

One area to do research in is what software hedge funds are using to manage their investment portfolios, and how are they justifying those costs? Obviously, what they're doing is they're saying you can make better financial decisions with the software, and that software will produce a positive ROI, because a hedge fund is only gonna look at its ROI. So there must be something in the tech stack used by a hedge fund that would produce that. The only technologically sophisticated hedge fund I know of is Jane Street, but there probably are other ones that are equally — But we want to focus on hedge funds that are not doing this by high frequency trading, but are doing it by good old-fashioned — what would be buy and hold in the modern era, which is to keep an asset for more than a day.

## Nic

A lot of this stuff is not necessarily complicated. The canonical answer for this would be something like Carta, which would be a very common thing for this — literally just like, "hey, here's a spreadsheet where you handle all your stuff." At some point in time, we're literally talking about, for a lot of these funds, a self-hosted version of QuickBooks and GnuCash would probably be sufficient. Something better would be nice, but it's like GnuCash in the form of a web app type thing.

## Brad

I've looked very briefly at the Rust accounting ecosystem stuff, and it seems like they're pretty obsessed with text-based ledger formats, which seems crazy to me. But I think you could potentially do that with some pretty simple format with a schema like JSON and make that a little bit more reliable. So one area of research is software that impact investors use. The other area of research is what software hedge funds use — in particular, what does their tech stack look like, and what could you provide to an impact investing fund that would give them the same sort of services that expensive software for a hedge fund would be, which I can imagine is back office stuff and is mostly financial decision making stuff, but maybe there's a case to be made that back office stuff is important. So I feel like that's reasonable on your short term goals. Do you have something you've thought of on medium term goals?

## Nic

The medium term goals are to really figure out what exactly the long term software stack for this looks like. The medium term is the long term goals.

## Brad

So should we have short term, long term?

## Nic

Yeah, it's short term and long term. I feel like the medium term goals is literally just the integration of the software product into the existing impact investing ecosystem, which is — that's definitely a thing that you can do. And luckily — how do I say this? — it is very fortuitous that Fortress is a software stack that exists and is good for this kind of thing. So the medium term is deployment and integration within the existing beta funds. That's the approach. Because the shared back office thing is an important thing that people can actually act on. In the short term, the benefits are tangible, and it's always good to choose tangible benefits over intangible benefits.

## Brad

Fortunately for you, it's not always that, because that's the value pitch of impact investing: that you can accept lower returns in order to get an intangible benefit. My thought is that — like, Mel talks a lot about pirate communism, which basically is a reverse flow from capitalism. You bring in capital by telling them it's about thing x, and it's really about thing y. But you produce enough of thing x that they don't realize that you're really about y. This is a hundred percent true. So I think a really important term out there is resilience. Resilience is a great pirate term because I think you can pitch to investors the resilience of the cooperative sector. Because cooperative sectors famously perform better in downturns — but they also perform worse in upturns most of the time. So that's why it's a hedge. It's slightly better than cash, but you're trying to classify it as a very low beta investment risk. So your low beta is used to justify your returns. But one thing that I thought of is if a big part of impact investing is to get grants, now you've got a different class of shareholders who are getting no returns on their investment—

## Nic

It's not necessarily no returns. In impact investing, there is a really big difference between capital raised at 0% interest, like interest-free bonds, and grants. Grants are money you literally do not expect to see. The return on that is: they are not expecting zero return, they are expecting to lose their entire portfolio. There are investors who are expecting a 100% loss. And that's it. It's almost more like revenue.

## Brad

But I feel like having the ability to have that second class of investors is pretty questionable when you're returning relatively good returns.

## Nic

Oh, for sure. How do I say this? If you're an impact investor, good returns are a good thing.

## Brad

But I'm saying that if you have good returns, but you're also using grants to provide revenue for your companies now, you — I think this idea that you've got two classes of citizens: slaves and free people. Slaves being the people — and free people being the people who get returns. So ultimately, you wanna fund this out of your difference between your actual returns and your—

## Nic

In order to do that, you need to have actual returns. Can I just talk for a bit?

## Brad

Sure.

## Nic

One of the things that we'll often get into with this is that, in general, the trade off between community investment and growth of the portfolio is a hard trade off to make because there's not a lot of data on that. You can explicitly say it's like, giving this person a longer term yield with a slower repayment schedule at a lower interest rate is going to be helping the community more than if we give them a super predatory loan, even though that will get us a higher return. But that's an investment that is hard for them to make, and there's this trend in the impact investing people that I was talking with that trying to do return maximization using conventional hedge fund return maximizing tactics or conventional credit capital maximizing return tactics leads to worse community outcomes than if you're just very generous with your money. And I feel like this is potentially an area where — Listen, I feel like this is a somewhat distracted thing. My thing about this is that this is a research product designed to keep hedge fund investors — like, the whole point is this is a hedge — this is a product—

## Brad

I would stop you for the sake of clarity for the LLM: "hedge fund" and "impact investing." They're not identical, or you're just gonna confuse context.

## Nic

So, impact investing funds. This is a product by design to help impact investing funds better make decisions about community impact — model the material outputs and the community impact of the companies they invest in, comparable to their models of the financial flows of the companies they're investing in. That's what we're trying to do, and that's the short term pitch. And if we're going to talk to both mom and the hedge funds, that is where you have to stop. Because the layer underneath this of how the model actually should work is extremely complicated. A comparable analogy for this would be when you and I were doing the open energy modeling thing, trying to explain to someone the internal workings of cBLAS or QBLAS or whatever it was called — I think it was just called BLAS. Trying to explain the internal workings of BLAS is not appropriate to explaining what we're both trying to do with the model and what the outputs of the model are.

## Brad

To me, the difference is very similar to what I've been working on in terms of the difference between agent-based modeling and multi-agent systems. And that one is a a scientific modeling approach, and the other is an engineering approach. So what you want the long term software to accomplish is actually to create these returns, because it's software you're giving to your cooperatives that are then using it to enhance the flows in the cooperative network. So your modeling software is also your engineering software. So we're trying to get over this dichotomy between thinking of agents as a modeling approach and thinking of agents as an engineering approach. So if you're going to create a super healthy, solidarity economy—

## Nic

But none of this is what we talked about. Our medium term pitch does not involve the word solidarity.

## Brad

I agree. But you said the medium pitch is to work on the long term pitch.

## Nic

No — I don't necessarily know if I said that. I think the medium term pitch is to integrate the short term pitch.

## Brad

Okay. So is there more to say about that?

## Nic

No. In the medium term, I don't think so.

## Brad

So are we on the long term?

## Nic

Yes. We're on the long term.

## Brad

That's where I thought we were. Okay. Cool.

## Nic

Importantly, if you're thinking about, well, our goal is to essentially get the software that will generate good returns. What an impact investing fund would want in research software that would help them make investments, which is ultimately what we're wanting to make, is good returns. And I don't mean like 3%. I'm saying the companies that you invest in are going to generate very good returns. Because the goal of every single company is to invest in companies that will give them great returns.

## Brad

But let me just say — I think you're confusing the intermediation layer that an impact investing fund does. People who invest in an impact investing fund are not investing in the companies. The impact investing vehicle is holding a portfolio of companies.

## Nic

But importantly, if the investment portfolio is generating high returns — is it good for an impact investing fund if it generates high returns? Traditionally—

## Brad

Let me just say that this whole thing makes me squeamish, because it very much sounds like what people were trying to do with microlending in the eighties and nineties. The rates of suicide among people who have got microlending grants is so high because they get convinced that they've got some idea and it fails. So the idea that you can hook someone up on a guaranteed financial flow to a creditor, in my mind, is potentially harmful to the people who receive those loans. So I think you have to figure out a way that you can say to people that you can go bankrupt and get out of this loan, and that it doesn't necessarily harm the fund.

## Nic

Importantly, this is why the fund needs to buy equities and not bonds.

## Brad

The reason for this is partially just bad financial instrumentation. But if you buy an equity in a company, you give them money. They go out and buy a food truck or something. The food truck goes bankrupt. You lose all that money. The fund needs to tolerate that. So the goal of the fund is to tolerate a rate of bankruptcy that is consistent with actually growing the overall rate of returns. And from my understanding, your thesis is the rate of returns are gained by the fact that you're getting gains from cooperation within the solidarity economy.

## Nic

Well, kind of. Part of the issue here is that the problem with the solidarity economy is that it's not an economy, or it's not an economy in the traditional way we think about economies.

## Brad

No. There's a harder core set of work around energy democracy that's more mathematical and rigorous. Or not energy democracy — let's see, it's economic democracy, which energy democracy is a subpart. It tends to be much more rigorous. Solidarity economy tends to be a little bit more on the self-organized spontaneous side.

## Nic

That's not what we're using. That's not, in my opinion, what the goal of this is.

## Brad

But anyway, I didn't say a goal, so why did you say what you thought my goal was?

## Nic

Oh, sure. Sorry. What's that? Could you restate what you just said?

## Brad

No. Okay. I said that I was trying to distinguish between economic democracy, which tends to be more rigorous and more like traditional economics, and solidarity economy, which tends to be more focused on self-organization. It fits my split down the left, which is between self-organization and self-governance. Self-governance tends to be more economic democracy people; self-organization tends to be more solidarity economy people. I think bridging that gap is really important.

## Nic

Yeah, I would agree with this. The thing that I was trying to say is that the goal of this project is to not do the solidarity economy bit. There are things that need to be produced in a society. And fundamentally, the job of a fund, in particular, is to figure out which things need to be produced and why.

## Brad

But this is why "resilience is a pirate term" is really important. So if you're saying you're increasing community resilience—

## Nic

Well, but no one cares about that. Or at least, I don't agree with—

## Brad

Important people who care about that are impact investors and governments.

## Nic

Governments might care about that, but importantly, that doesn't generate you returns.

## Brad

I don't agree.

## Nic

I don't think it generates you returns.

## Brad

I think you get grants from governments. This is where I feel like you don't necessarily have to tolerate two classes of investors who are both private — that you obtain grants from the government who are using them as grants, who are using them to increase community resilience. So your message to governments is that you're increasing community resilience.

## Nic

One second. Do you want to pause the conversation at this point? Because I feel like we might just want to discuss what we think the—

## Brad

No. These don't have to be nice. These conversations should probably not be nice. So if you want to push back against my—

## Nic

I am.

## Brad

Yeah, you should do that. And then the question is, how do we provide from a contentious conversation a uniform prompt to the LLM that's worth shit? That's a second problem. Let's focus on the first problem first, which is to get out—

## Nic

I don't feel like resiliency is — how do I say this? At some point in time, the problem with impact investing is lack of returns. And this is definitely not sustainable in the long run. I personally feel like having a part of the economy which is tethered to the real economy, which has over a sustained period of time very low capital returns leads to unhealthy things for that economy. One of the things that I am somewhat skeptical of is that if you're just saying that the returns to cooperatives are going to grow more slowly, and cooperatives are going to be way less capital efficient than firms in the real economy — you are on the struggle bus. Admittedly, in some sense, one could argue that it is actually impossible. It is impossible for cooperatives to succeed in such an environment. The only way that cooperatives succeed in that environment is by having a time period where you have a lot of revolutionary tendencies, which reduce the returns going to capital by a significant amount by engaging in all sorts of capital destruction, which the firms that you are in are somewhat insulated from. However, one of the things is that if a revolution happens, things will be good. Importantly, that means that when a revolution isn't happening, things are not necessarily going super well. So I think that one of the goals for this is to explicitly try to figure out a way to maximize financial returns. Or I shouldn't even say financial return. I think I should be saying material returns on a community's investment that can keep the fund going.

## Brad

So I think the big difference to me is you're going from, say, a spherical topology of a firm to a network topology of a cooperative network. But you still have internal accounting within the network economy. Because firms are keeping track of material flows within the boundaries of a firm. Outside of that firm boundary are these numerical things. But within that firm, they're doing these sort of material flow analyses. They've got cost accounting. They've got all the things that you do as part of a firm. So the goal is to extend that firm model from the spherical topology to a network topology. But you still have a notion of internal and external. So on the boundary of that cooperative network, you have financial flows because that's interacting with the regular economy. There, you have the same sort of cost accounting material flows you have in a regular firm, but you're now not doing it with the notion of a firm boundary with a single governance. So it looks more like an ecosystem or a supply chain rather than a single firm. So one source of inspiration here is actually looking at how capitalist firms do these supply chain contract managements. Because now you're talking about extending that notion of a supply chain from a single firm that's maximizing profit to a cooperative network that's maximizing resilience.

## Nic

And I think that most firms — it might not be that complicated. If your entire business is drop shipping Labubus — or whatever, stuffed plushies that are made in China — the entire approach is a relatively simple thing where you just find the cheapest provider, and then you have the cost of the thing from China. And then all you're trying to do is make a certain percentage revenue on top of that. If you're trying to look at something more complicated for this, you're probably looking at some kind of logistics management for relatively complicated electronics. One of the things that I would really like to see — one of the software they'd be interested in for this is potentially what internal software do PCB manufacturers use for sourcing their own components if they have models for that. Because those are systems where you have potentially thousands or tens of thousands of different material inputs for every single process, which is also more complicated and potentially overkill for what a single shop would do. But importantly, the number of connections and external inputs that a PCB manufacturer has, even though it's way, way bigger than the average company, is potentially comparable in number to the number of external connections that an entire cooperative network would have.

## Brad

The traditional capitalist model is you take something that looks like a hypergraph or symmetric monoidal category where you have production processes with multiple inputs, multiple outputs, and you condense that down — your cost accounting model condenses that down to more of a single-channel accounting model. Because accounting models don't really — they look more like conventional graphs than they do like symmetric monoidal category networks or hypergraphs. So you almost have a hypergraph-to-graph model that condenses down your production process to this model of financial flows. And that's a very lossy process. But in order to justify your capitalist investors, you have to have that map. So that map from a production process to an accounting model is what they call cost accounting. That's why cost accounting is the single most important target, because that's where the map between material flows, energy flows at one level and financial flows at the next level happens. And doing that in a way that's sound, where you can actually improve your material and energy flows and gain higher returns based upon increased efficiency in your material energy space — not just by efficiency, but by growing firms. Like, if you wanna run — You're making Labubus. One of the things you might wanna do is have cooperative farms that grow a lot of hemp. You use that hemp to create plastic precursors, and you make a completely biodegradable Labubu. Would that be 10 times more expensive than China? Yes. Is there a market for a 100% biodegradable Labubu out there in the world? Maybe. That's the sort of research — doing that sort of research. How can you justify higher returns in your products? Because they're more sustainable or they're more locally sourced or they're more compassionate, whatever that is. You're willing to make those changes.

## Nic

I think that you could do that. I also think there's a component to this where maybe it actually — manufacturing in the US is going to by necessity generate lower returns than companies elsewhere — there's a certain narrative that it's financially feasible to produce things in the US, and the narrative that it's financially impossible to produce things in the US is part of the reason why it's financially impossible to produce things in the US.

## Brad

But what they're lacking is the detailed cost model. They would need to really justify that. Exactly. So you've got financial people looking at this graph, and they're trying to make inferences about their hypergraph, and they have no idea what they're talking about.

## Nic

And the thing is that these hypergraphs are very valuable. Importantly, because China is no longer a cheap country to make things in. If you're looking for the cheap country to make things in, you go to Indonesia or Vietnam or India. China's doing the same thing the US did. Indonesia is to China what China was to the US — or I should say, what China in the 1960s was to us.

## Brad

Right. Even later than that.

## Nic

No, I'm not even saying even later than that. But wages have not gone up that quickly. Well, Chinese wages — yeah, Chinese wages haven't gone up that quickly. But importantly, the efficiency and automation of their internal systems are about what the US in the 60s was to the rest of the world economy, in terms of the level of lead the US production system had over other countries. And that's important. That's enough to deal with relatively high wages in a country. So if you're going to be designing production processes, you need to be able to design production processes very efficiently. You need to, in some sense, be able to engineer the slop out of a lot of production processes. Second of all, how do I say this?—

## Brad

But it's not just engineering, though. I totally agree with you, but it's growing companies.

## Nic

Yeah, it's growing companies. But I also think that the reason I'm interested in returns and think that returns are absolutely something you really need to analyze is — The entire world hates returns. Returns to capital are a very — I could even call it an unnatural concept. Especially above-average returns are an extremely unnatural concept. So I like to think about it like this: every single hedge fund has an internal model where they're beating the market by at least 30 points a year.

## Brad

Every traditional — none of these financial models have been tested in a widespread deflationary environment.

## Nic

But I don't think it's good to gamble all of the investment funds on an extended deflationary environment. And I think that this is also what a bet on resilience is — even our minor deflationary environment, which was highly located around housing prices in 2008, was enough to bring down inflation. The government took a lot of work to get rid of that deflationary environment as fast as possible by printing gazillions of dollars. The government just printed money — rather than taking the losses, it reinflated. But importantly, the reason I'm scared about a bet on resilience is that a bet on resilience is a fundamentally bearish bet on the — you are tying the success of your entire portfolio to a bearish bet on the overall economy.

## Brad

But it's a countercyclical investment. When you're getting positive returns, you're putting that into growing the resilience of your system so that during a negative time, you have lower downside. That's why I feel like a countercyclical strategy is a legitimate investment target.

## Nic

I don't think so. And I think the reason for that is — first off, the reason that I don't necessarily know if that's a good investment portfolio is because there do exist investments today that are countercyclical investments. You can think of the whole growth versus value stocks as like a version of a countercyclical investment trend. But you could also just do regular market analysis where there are certain companies like tourism companies or a lot of B2B SaaS companies that are going to do very badly in a recession. And there's lots of companies like payday loan centers or Dollar General that are going to do very well in a recession. And Dollar General and all those other companies market themselves as countercyclical investments, but just because you slap a label of "we're a countercyclical investment" on your thing does not necessarily guarantee you investors. Importantly, the fact that an investment is countercyclical means that it is bad when it is procyclical. I think the rationale for this is that let's say that you had been a total idiot and listened to me three years ago when I said, "NVIDIA is at $2,000,000,000,000 right now. Now would be a good time to exit NVIDIA" — and then not do that. And you very wisely took the time doing that and were able to get in. I think you guys sold it at like 3.5 to $4,000,000,000,000 total valuation. And then since then, it's actually stayed relatively flat. So that was a very good time to get out at that point. But importantly, if you make a fundamentally countercyclical investment, you might be thinking, "this investment pays off really well if the economy goes into a tailspin. And if it goes into a tailspin, I'll make millions. Hoorah." But importantly, if the economy does really well, you lose very badly. And that in and of itself is a bad thing. The reason that most hedge funds call themselves hedge funds in particular is because every single hedge fund has some internal algorithm inside of their company which is somehow designed to pick good companies from bad companies. That might be employing a lot of researchers to do individual analysis. It might be some high frequency trading thing or something. But one of the things that the history of finance in New York has borne out is that these strategies just by themselves tend to make companies go bankrupt. Because importantly, you're not ideally a hedge fund. A hedge fund is exposed to the risk of, well, what if their investment decision making machine is wrong and all the companies they think are gonna succeed fail and all the companies they think are going to fail succeed. But then there's also the whole other thing: what happens if you're doing a bunch of margin lending and just broader swings of the entire economy just bring your entire portfolio up and down like a boat? Broader market swings have nothing to do with the reason you selected a certain portfolio of stocks. They can essentially wipe out your entire fund because you're only actually accounting for the differences between different funds. You actually don't really have any broader way of predicting market trends. So the reason that they call them hedge funds is that a hedge fund will analyze a portfolio of companies in a specific sector of the economy. We'll say, do all the analysis: "these are the companies that we think are going to succeed, and these are all the companies that we think are going to fail," and they buy exposure to the companies that they think are going to succeed and get short exposure on the companies that they think are going to fail. And explicitly, if you balance this entire thing correctly, the entire point of it is that if the market crashes, you make money on your shorts. And if the market rallies, you make money on the stocks that you actually hold portfolios in. But importantly, none of those really pay you big because the market going up or down will make and lose you money in equal amounts, so it just goes into filling the other hole. The only thing that really makes you a lot of money is if the companies that you think will go bankrupt in a specific sector go bankrupt, and the companies in that same type that you think are going to do well do really well. At that point in time, you made money on your shorts, and you made money on your gains. Or maybe you just didn't lose any money on your shorts. You made a lot of money on your gains or vice versa.

## Brad

I'm gonna say what a lot of people are gonna say when they hear this pitch. If your idea is to try to be as parasitic as possible and pull as much money out of the solidarity economy as you can or return it to investors, I'm not interested. You need a much, much better pitch — maybe you're just talking out of your ass here, but you need a much, much better pitch.

## Nic

I know. Well, I'm trying to—

## Brad

No. You're saying you want to maximize returns to capital. I just think that's crazy to say as someone who's trying to tout an impact investing pitch.

## Nic

But importantly, I'm trying to maximize returns for the fund itself. The point of impact investing is that the fund itself is owned by the community. If an impact investing fund makes a lot of money, that money goes directly back into the community. That money does not get paid out to investors. The entire point of fundraising and especially fundraising through grants is that if you get a bunch of grants and then you lend out those grants to the financial economy and then you generate a very good return on those grants, your reward for generating that high return is more people get to invest in that space. I do not think the goal of this is to pay the investors of your fund back. This is one of the things Siobhan said that I absolutely agree with him — finally got the name right — which is that an impact investing fund that prioritizes returns to investors is not an impact investing fund, categorically.

## Brad

Okay. Totally. I totally agree with that.

## Nic

But the reason that I'm bringing this up is that despite all of these tricks, most hedge funds do not make above average market returns. Hedge funds striving their best, rowing as hard as they possibly can against the current, make average returns. And one of the things that I'm worried about with impact investing is that you have the option of opting out of the market and just buying the passive index fund. That will generate you a market return that will be better statistically than any fund you would have picked. But importantly, if you actually decide to do active trading in the market or you decide to start trying to make active investments, especially with loans or investing in private companies that other investors would have passed on, you are intentionally entering the maelstrom. And if you aren't spending a lot of your time and energy thinking about paddling towards getting high returns, you'll eventually get sucked into the bucket of very, very negative returns, is one of the things that I am worried about. But I also think that there's a secondary point to this: how do you get high returns? And the answer is—

## Brad

A firm is gonna distinguish between internal and external returns. So I highly suggest for clarity for the LLM that you talk about internal returns, which are working on your cost accounting side, and external returns, which are working on your external—

## Nic

The best thing for this is that every single company has a model of trying to get better internal returns. Every single company tries to have a way to get good internal returns. But importantly, most of them don't make it. But if you're trying to maximize internal returns, there are good and bad ways. This is one of the things I was talking about. I think that this is also one of the reasons why debt is a bad investment vehicle for this kind of thing. Debt investment in particular is dangerous because — how do I say this? The investment returns first — I'm sorry, I'm getting very distracted at this point because there's just a lot of relatively base financial concepts that I'm trying to weave together in this. So I can talk about the difference between — is there a difference between investing in stocks versus investing in bonds when it comes to the solidarity economy, and how to make sure the ecosystem stays healthy?

## Brad

I think you need to be careful about just importing concepts from the existing economy and whether they apply without loss of generality to the solidarity economy. I caution you to avoid fixing your concepts so clearly in advance so that you feel like you got every single economic category you need to—

## Nic

We definitely don't. But there is also some danger in importing existing concepts. I would even argue that this is maybe not even the way that we should think about this investment portfolio, but there is a difference between stocks and bonds. And thinking about how exactly do traditional investment vehicles manage — how do they differ in managing funds? How do they differ, companies that will buy stock in early companies versus companies that will buy debt in small companies? And importantly, with debt, your return is capped. So no matter if you buy Anthropic bonds, and Anthropic becomes 90% of world GDP, you do not actually really get anything out of that. You actually get the same exact return on your bond as if Anthropic was barely staying profitable, firing a bunch of its employees, staying at the threshold of being bankrupt, which is your 9% whatever the loan is offered at. So in this sense, a bond has a lower maximum return, but it does this for a much more stable return. All a company needs to do is barely survive, and a bondholder gets paid back. This is at some level somewhat bad because the bond investor has no material interest in seeing the company succeed. All it has an interest in is the company not failing, or even if the company does fail, making sure that it fails with enough capital so that it's able to make itself whole. It doesn't really want a super dramatic failure where the company is just unable to pay anything. In fact, this is also why bond investors have a bit of a reputation as a vulture because they would rather kill you while you still have fat on you as opposed to if you survive for a little bit longer and are losing some of the fat on you. This is why bond investors are typically portrayed as evil: the financial incentives mean they really have no interest in making the companies they invest in good or healthy. This leads to super toxic loss avoidant behavior. But importantly, a bond investor will not necessarily super care about a super high growth rate. A bond investor will not be super pissed at you that your revenue is growing 5% a year instead of 20% a year. For a company that has relatively decent margins, growing 5% a year is a good thing. But if you're a stock investor, that company is bad. So importantly, when you're stock investing, your upside is literally the exact reverse of bonds. Stocks have unlimited upside. The canonical example of this is if you were really smart and bought NVIDIA in 1968 — in 1998. Even though you probably lost some money to begin with, you ultimately have a return on your investment of around 139,000% or whatever it is.

## Brad

I can tell you from experience that if you bought NVIDIA in 1998, that made up for the fact that every single other one of your investments absolutely sucked out shit because you still made a ton of money.

## Nic

But that's exactly the thing: the reason that you were able to make money despite all the other investments doing poorly is because if you buy a stock, the only value that you lose is the value of the stock itself. If you bought a $100 stock in pets.com, your floor on the investment is limited because you've only actually lost $100. This also leads to another set of toxic behavior, which is that stock investors will be very forgiving if you're almost bankrupt. If you're almost bankrupt, they will say, "you have the energy to keep going. You could go ahead and turn this business around. And if it does fail, that's okay. Ultimately, we are willing to tolerate a certain level of risk because we are comfortable to make up for that in other areas." So if you're doing badly, you really want to have stock investors. But this also means that there is a certain amount of uber toxicity that comes around growth rates. If you're a stock investor and you're at another example of a company that's growing 5% a year, this company will be like, "do whatever you can to juice revenue as fast as you can. Get up to 20%. Hire more people. Hire more and more and more and more people." Even that is ultimately unhealthy for the people currently involved right now who will eventually leave the company going bankrupt. A bond investor would not be interested in having a company potentially overhire a bunch of people that in a financial downturn will lead that company's bankruptcy because that would hurt the bond investor. But importantly, if you're a company in a portfolio who's doing somewhat well to a stock investor, that stock investor is fully dependent on you becoming a bajillion — is fully dependent on you becoming a unicorn or a decacorn or whatever the current term is. They are dependent on you doing extremely, extremely well to pay for the rest of your portfolio. So they will absolutely want you to gamble the success of the company and the success of all your employees on becoming a decacorn. Both of those are bad. But every single time you introduce capital, your company provides a bunch of adverse incentives, and they both provide very different adverse incentives. That's the thing that I'm trying to say right there.

## Brad

The main thing that you need to break down is this notion of a company being something that's run as a hierarchical firm that has a single person in control dictating things. So a network firm. Or a solidarity economy does not rely upon governance as its primary form of coordination. But then what you're doing as an impact investing fund is you're like a company in terms of your internal projects. You have transparency and visibility into the cost accounting for every one of your subsidiaries within your company. But you're not running that network in a traditional hierarchical command and control top down approach. So again, that's where I feel like it's needing both self management and self governance approaches to be successful. And I think you have to say that this kind of cooperative network can produce higher returns than a traditional hierarchical top down command and control approach. To me, that's the bet you're making. Because you're investing into this idea, and that idea is that command and control top down hierarchical corporations are antiquated in the current age. The relations of production, which is this hierarchical managed corporations, is no longer a good match for the forces of production, which are highly distributed ability to produce at very local levels and hyper local levels. So I think that's ultimately what I think you're trying to create. The impact investment vehicle now looks more like the East India Company than it does look like a traditional hedge fund. You're inextricably involved in running your cooperative network.

## Nic

And I think that this is the explicit thing. The way that I'm thinking about this is that there is an element to stock investing which is tolerant of failure in a very human way. If you have persons in your company who invest stock, they are not going to beat you to death with billy clubs when your company goes bankrupt. They might potentially meet you with a billy club if you don't grow fast enough, which is very odd. In some sense, one of the big things in Silicon Valley is that investors are actually way more tolerant of bankruptcy than they are of slow sustainable growth. It's very weird. But there is a part of this where it's like, well, in some sense, you're dead — there's not a lot they could do to save you. But if you're growing slowly — if they beat you with a billy club, you might grow faster, and that will actually generate a lot more towards positive returns.

## Brad

But we can go down a list and look at firms that have made terrible decisions about subsidiaries, and those have not brought down the entire firm. And as a network firm, you're going to have subsidiaries that—

## Nic

They fail. But also importantly, there are so many reasons that businesses fail that are totally incomprehensible. I think even if you're looking at my Carriza, for example — at the beginning it was unclear that the reason that the company would fail, at least in the beginning, was that me and Yuri were bad programmers who didn't necessarily take our problem seriously enough. If the two of us had individually made better decisions about literally just how we approach the technical implementation of our product — and even just not necessarily made different decisions, but been aware that the problem was actually a lot harder than we thought it was — we would have been fine. How does an investor model that in a spreadsheet to see if the company's gonna succeed or not? And the answer is you can't, so you just need to be tolerant of a certain level of bankruptcy. And I feel like if you're going to be investing in early stage companies and you're trying to grow the cooperative network, you need a system for investing in small businesses where you are not beating them to death with billy clubs when they go bankrupt.

## Brad

Well, not only that — those founders, the people who have gone through the process and failed, have now learned something. So they are part of your cooperative network whether or not their particular business failed. Unless they've committed fraud or something like that, if they fail out of a good faith attempt, they are now a huge asset that you wanna keep in your network rather than forcing them to go work at Home Depot.

## Nic

For better or worse, this is one very strong component of Silicon Valley culture. But in the same breath — Silicon Valley culture is deeply evil. But again, one of the reasons that I think it's valuable having this conversation about existing financial instruments is that nothing is completely good. Nothing is completely bad. If you're going to make things better, a part of that is going to involve disassembling things which are mostly bad and picking out the good pieces.

## Brad

This is why a lot of what they talked about at the conference was this concept of dual power, which was very much like putting struggle first. You have to develop a completely independent process from the existing economy. And I don't think that's a realistic model for growing the solidarity economy. You're growing up in the ruins of the old, and you cannot do a purity test and say, "we need something that's totally independent." So you're always gonna have flows to the capitalist sector of the economy. But I think that the duality comes from this boundary of the firm. You actually have an internal process, and you keep a boundary up and running. So you're a viable system. Your boundary with the capitalist economy is regulated in such a way so that you're not completely destroyed by the environment, in a way that a living system maintains a very highly porous and open boundary and yet still maintains resilience or viability. And I think there's a way to do this — you can make the body analogy.

## Nic

Which is that — a solidarity economy is like a living organism, and the individual firms inside that company are like organs. A solidarity economy is a person; the companies inside of that company are organs. If you map the traditional — let's say the organism needs a new liver for some reason. Again, I know the analogy is tortured.

## Brad

It's not tortured. It's actually a very deep analogy — that is actually something that the solidarity economy really needs to wrestle with. Is a solidarity economy an organism? Is it an ecosystem? Is it a community? Is it a society? Is it a firm? There's probably no existing metaphor that's perfect. So it's like sketches of an elephant. You have all these metaphors for what the solidarity economy is, and none of them really describe what the solidarity economy is. So don't take any of our metaphors too seriously.

## Nic

Oh, for sure. So I think there's an example for this where let's say you're the solidarity economy organism incorporated. You're wanting to fund the production of a new company organ called a liver or something.

## Brad

Let me just say, you have to be incorporated. Because you have to take advantage of the existing capitalist law that makes you a person.

## Nic

Oh, exactly. You have to run as a corporation. And also for all of your internal flows, you do need to do the thing that I described where you just encapsulate them in enough financial instruments and swap contracts and stuff so that it just stops being taxed. Importantly, you are fulfilling your end of the Hobbesian social contract by making society better. We talked about this earlier in one of our existing conversations.

## Brad

But you look like a firm selling equities more than anything. The single closest model of what you're doing is a firm selling equities.

## Nic

It's a firm selling equities for sure. But importantly, there's a secondary part to this: let's say that you're a firm who's selling bonds. This is arguably the worst outcome because as soon as it ever looks like the company might be in really deep shit — let's say that you grow a liver organ and you're successfully thriving, and then the organism just slams back like 20 beers one night, and the liver is like, "oh, no. I'm looking like there might be some trouble here. There are rumors on the horizon of a liver bankruptcy in like three years." If you're funding the liver with bonds — and that's a very tortured analogy — the bondholders will be like, "oh my god. This liver might go bankrupt. Let's go ahead and drastically do a huge capital strike against this company by jacking up their rates so high that they eventually enter an interest debt spiral, and then the entire liver will collapse." There's definitely not gonna be a "well, you pounded back 30 beers in one night — if you just don't drink alcohol for another couple months, you're gonna be fine." But again, there's the concept of "this might fail," and then there's a worry that this might fail. So you essentially just get a run on the bonds of the company. There's this tendency for bondholders where as soon as it ever looks like the liver isn't doing perfectly, your immediate thing is just stabbing it as soon as you possibly can. Or an emergency liver transplant. "Look at our metrics on our liver today. Oh my god. The entire liver is gonna collapse. Emergency liver transplant. Rush him to the hospital." "No, no, I just had a night of heavy drinking." "No, no, you're not. You're gonna die." So that's obviously bad. And importantly, that impacts the health of the circulatory system with this approach of, the company was doing fine — it was still contributing to the health of the circulatory system even though it was looking like it might be in trouble. You hurt the health of the product community by taking this approach of, as soon as things ever look moderately bad, you start immediately dicing things up and selling them off to the highest bidder. If you're selling equities, you get the cancerous growth problem: if the liver is doing badly, that's fine. We'll still support it if you drink 40 beers in one night. But we're also gonna demand that even if you're doing well, the liver needs to grow by at least 5% a month. Until eventually it starts to encapsulate the entire body and kills you from stage four liver cancer. Both of those are bad analogies. But I think the reason this actually is helpful is that you want to fund the construction of new organs, but you also don't want the organs themselves to be responsible for delivering back your returns. The best example of this is that, "hey, legs. You're eating so much more oxygen. There has been an unfair exchange of oxygen between you and the lungs of the body. You guys are being bad organs, and we're going to hit you with a hammer until you start contributing more oxygen." Part of the reason that a lot of these financial structures are bad for the overall economy is because they are dependent on the organs themselves to generate enough returns to fund the construction of the organs themselves. So ideally, if you're trying to take this tortured analogy even further, you would want to do it the same way the body does: a new organ is going to be funded by the energy of the entire circulatory system. And the entire energy of the circulatory system is going to increase because you have an organ — a liver that's actually filtering blood and destroying toxins. And because of that, the entire circulatory system health is going to improve, then that's going to be the source of energy that you use to fund the construction of new things, so on and so forth. You would sometimes want to give the company money directly, but then you want your returns to come out of the broader circulatory system. And you need some way to do that. But taking funds out of the circulatory system is dangerous because, again, with the organ example, if you withdraw too much from a person, you just kill the entire person. Which is bad. And then under this metric, a company is judged. Under this metric, capital is always going to have some degree of an antagonistic relationship with workers and the managers of the company. I don't really think there's any way to get around that. But importantly, at least under this model — if you're somehow able to say, "hey, we have this financial model where we are measuring the returns that you're making — essentially, we're measuring the extent that you're contributing to the health of the broader cooperative community. And we want you to increase the way that you are helping the rest of the cooperative community. Because the degree to which this company is helping the rest of the cooperative community is the extent to which their investors get a return."

## Brad

Well, I think you're gonna have to have a contract with your equity investors where you can buy them out at any time, and they don't get the valuation on the internal thing. All of that — what I've been talking about so far — is internal investing. Are you talking about external?

## Nic

No — yeah. So now I'm talking about external investors.

## Brad

Okay. You bought an equity share in your company. The company has grown a lot, but it's grown a lot within these internal metrics. But you have enough surplus you've created in dollars, by extracting that from the whole circulatory system, that you actually want to start freeing yourself from your external investors. So the long term goal of your firm is to not rely upon any external equity investors, to replace that with internal.

## Nic

But importantly, what you need to have in order to buy out your equity investors is higher internal rates of return than external rates of return. And if you have the reverse, things are going to go very badly for you, and you're going to have to sell more of your company to make that. There's also a reason why I'm apprehensive about the idea that internal rates of return don't matter. Internal rates of return really do matter. External rates of return — you should always be trying to minimize your rate of external return, always. Internal rates of return, a little bit different.

## Brad

And that's the persistent struggle between the managers and workers of a firm and the capital investors in that firm. And you're trying to find some sort of balance, some sort of Treaty of Detroit where your external and internal investors are not at war, fighting over how much of the pie they're gonna get. No, really. But you can't just buy labor peace. You're gonna have to accept a certain amount of tension always. When you accept external investors, you're now accepting a struggle for them to try to extract as much as they can. So you've now created a potential parasitic relationship with your external investors.

## Nic

It's also good for your external investors to be grant organizations or public banks or philanthropic investors that are maybe giving you a below-market bond or maybe a 2% bond or something like that. First off, it's also at some level good to have capitalist investors whose management is at least on board and thinks what you're doing is a good idea. Because, admittedly, capital always does roll downhill towards behaving in an evil and exploitative way, but there's a lot of variation in how antisocially and how evil your external capital behaves, depending on who you actually take it from. But importantly, the main thing that you want in this situation is you want to have a big choice about who you actually take money from. In order to have a choice about who you wanna take money from, you need to have a good thesis for why you're offering high rates of — if you're offering very low rates of return, you're gonna have two people who are gonna be willing to give you money, and both those people are going to suck.

## Brad

Okay. I think this is a good place to stop. I think if you can bring in these three conversations and transcribe them.

## Nic

I will. But I also think that there's a secondary point to this, which is that if you're going to be trying to do this — there's one thing which I am unaware of a good solution for — there's this whole idea of your returns come out of the circulatory system. How exactly does that work? I think is a very open question at this point.

## Brad

Well, obviously, one huge piece of prior art is how Mondragon does things. Mondragon is both a cooperative network on the inside and a firm on the outside. And Mondragon has probably taken on external investors. So I think a lot of things that Mondragon has done are probably apposite to what this overall thing is doing. And I think, you obviously have some buy-in from cooperators like Sid. They would view what Mondragon has done as really important prior art. And there's a lot of literature on this.

## Nic

I think there's also a secondary thing which is valuable: one of the things I think you definitely want to do with cooperatives in the cooperative ecosystem is that cooperatives in the cooperative ecosystem have revenue that they are making and want to invest those returns somewhere — that gets invested in the main institution. Your ultimate source of capital is other organs in the network or other organs in the ecosystem.

## Brad

And there's — I know David Ellerman did a lot of work with internal capital accounts that are held by workers within a cooperative. That's also, I think, important prior art in terms of thinking about how you — Because it's very much like the relationship between a gros and a petit topos. Your firm is operating within a — it's an object in a category of firms. But it also has this internal structure like a petit topos. So you're ultimately looking at constructions like functor of points or other things that are important for thinking about how do you have this internal structure and yet still have this observable structure of an object within a category of firms. So your firm is an object in a category of firms, but it also has this important internal structure that you don't just neglect. And then how do you measure that structure? What are your test spaces within the gros topos that let you understand what's going on within that object where you don't have to have privileged access to look inside the object. So I think there's a lot of good category theory prior art here as well.

## Nic

I think there's a lot of good category theory prior art, but I also think that prior art is important for a secondary reason: if you, as a funder, are giving equity investments to new members of the cooperative economy, and your explicit payout is how well those cooperatives actually make the health of the economic relations inside the cooperative better — you need to model something. You don't have the option of just modeling every single firm as an investment portfolio. You don't have the option of just doing everything in terms of a financial analysis. I do think that there's a rationale for this. Let's go back to the organism analogy for a bit. You can definitely combine a single metric for blood health, where if you score high on a single blood health metric, your blood is healthy. And if you score badly on it, it's not healthy. You can probably combine it into a single health score. But importantly, that is also not very helpful if you're planning on improving the blood health. So for example, this blood is otherwise pretty oxygenated, has enough red blood cells, etcetera, but is also accumulating a lot of these very long proteins that are damaging the other organs. So under this financial model, a company that would go out and extract value from how they improve the circulatory system would want to fund the construction of new livers so that the proteins in the blood would be cleaned up. It's like a rationale for this.

## Brad

But I think managing internal conflict here is gonna be really important. Because if you're saying, some part of your body might say, "you know what? Let's go independent. Let's get out of this network, because we're returning way more than all these leeches who are bringing down these below-market returns, and we're healthy enough that we could split off and become a viable business operating within the conventional economy." So in that way, it's more like an ecosystem because you have viability of these — it's not an organ. An organ is completely dependent, whereas a person in a community can leave that community and go someplace else. So in that way, it's more like a community, except your communities are communities of internal firms. So finding ways to manage the conflict — like, if you wanna grow using returns from profitable parts of your network in order to grow the network itself, you're gonna be facing conflict with workers that don't wanna see their internal equity shares drawn down.

## Nic

Oh, yeah. And I feel like there's always going to be a big issue with this, Brad, which is that — let's think about this from a secondary perspective: I think this is also a reason why it's important to not value everything in dollars, why actually having a single scalar irreducible is pretty bad. Let's just say that you went ahead and did this in the model of co-ops.

## Brad

But firms have a diversity of capital. Firms have workers. Firms have offices. Firms have productive processes. Firms don't have a single scalar notion of value.

## Nic

They don't — but fundamentally they do reduce the value to a single scalar.

## Brad

The only time you need to reduce that is when you go to investors.

## Nic

Well — and also when you pay taxes, and also when you use any accounting software in existence.

## Brad

Again, most accounting software doesn't do cost accounting. What you're looking at in terms of a market out there is that what's sold to you as GnuCash, which uses double entry accounting, is not cost accounting. Cost accounting is this reduction of a hypergraph to a graph.

## Nic

For sure. But part of the rationale for this is that if you're explicitly doing everything on a pure dollar reduction basis, the reason that this isn't going to work is that you're going to have some firms that are going to be like, "well, hey — you put a market price on our outputs and you compensate for that internally, and you're doing all of your internal accounting in dollars. You're actually forcing us to sell our products at below market prices and forcing us to buy above average market inputs." Because it's just a system where you're essentially having a central router that decides distribution or something like that. And the problem with such an approach is that that company's gonna be like, "wait a second. Since you value everything in dollars, we can't just go independent." Now, having other currencies aside from dollars is great because it comes with all the advantages of being able to decide your own currency and being able to intentionally inflate or deflate its value for the overall health of the community itself. That's very valuable. But importantly, if you're doing every single thing in dollars, you also make it very obvious and super easy for companies to break away. There is a part of this where using an alternative internal system of accounting — using something that's maybe richer than money, like the same way that homology groups extend Euler's number. Kind of bringing back that analogy. Using something like that internally indicates to some degree a certain amount of community buy-in on everyone involved. I do think there is a certain component to this where you are going to need to actively reward the firms that are doing well and punish the firms — or I don't wanna say punish — but at some point in time, how do I say this? The entire system cannot be a charity case taking from coffers that are successful and feeding into coffers that are unsuccessful. Because that is going to just lead to lots of resentment. The whole point of this is that it's designed to improve the health of the ecosystem for everyone that should benefit, and it's not designed to play favorites or adjudicate disputes between cooperatives and neoliberalism. You're going to have to do a lot of that, but trying to explicitly say, "this is not necessarily a role we are taking on" would be great.

## Brad

And I also think you're not having shares that you can just withdraw. You have an equity stake, and that equity stake in the firm is valued in the internal chart of accounts. And if you said "I wanna leave," you're not necessarily gonna pull out the capital. You might say, "okay, we'll give you an annuity, paying out of this based upon your equity stake." So an employee that leaves now starts to have a similar relationship to an external investor. They're getting a cash return from the overall system, but it's not necessarily going to be — there's this conversion rate between external and internal that you can just pull out and say, "well, now I'm gonna pull out money. I'm gonna cash out my stake."

## Nic

Well, you can't cash out your stake. All you can do is get a return on that equity. And I think there's also a secondary important thing: no amount of deflation of stock price can bankrupt the company. Your equity investors can pull out and do everything that they can do to you, but you cannot declare bankruptcy. No amount of downward pressure on a company's equity can force a company to go bankrupt. Only bonds could cause companies to go bankrupt. Because if they wanna pull out their equity stake, you say, "well, currently, your equity stake is worth pennies on the dollars that you invested. We're happy to give you the pennies. But you knew the downside risk when you came in and that this was a risk." So, it sucks to be you. But bondholders have the ability to force the company into bankruptcy if their returns are not given. But they also don't have control over the company. A traditional equity investor would be like, "oh, well, you're not maximizing returns. I will just go ahead and make the decisions. I will coordinate with the other investors who want high returns to force you out and put someone else new in management." And you also obviously don't want that. That's a similar — where the liver decides it doesn't wanna grow any bigger. The liver's management gets replaced with new management that decides to turn into stage four cancer.

## Brad

Okay. I think we're good. I'm sorry. I need to stop for a couple reasons. One is I don't have all day, because I've got cleaning to do. I've gotta go to the store. We've got the debrief for Resist and Build at four. So it's 10:30 already. So I need at least two hours of cleaning time, maybe more like three. So I've got maybe two and a half hours left to work on this project for the day. So I do think it's important to get the overall process started today since I'm taking the day off. So my request to you is if you can get the transcripts made from the phone, that would be awesome.

## Nic

I will try.

## Brad

If you can't, that's okay. I think we can do something.

## Nic

I think at this point, the best thing to do might be — I will go ahead and put those three — I'm still working on getting a good self-hosted thing for this setup. I do want to do that at some point in time. But one of the things I might recommend for you to do is just be like, "hey, this is definitely a thing you could pay money for to just solve."

## Brad

Alright, let's do that then.

## Nic

I totally think time is money at this point.

## Brad

I agree with that. So maybe the only thing I really need you to do is pull the transcripts off the phone and send them to me.

## Nic

Okay. We should stop recording so this embedded discussion isn't on the transcript itself, but I will do that.
