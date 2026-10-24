# MOAIWI-4

*Cleaned from `Audio/transcripts/Moaiwi-4.txt` (timestamped, diarized — Speaker 0 = Brad, Speaker 1 = Nic; Nic is rendered "Nick" in the raw file). Consecutive statements merged; cross-speaker sentence splits rejoined; filler words, stutters, pauses and false starts removed. Recording of 23 October, roughly 06:36, paused at the end to start a separate long-term conversation.*

## Brad

Okay, beginning recording. It's 06:36 on October 23. I'm talking with Nic. We need to start saying that at the beginning of every transcript from here on out, unfortunately.

I'm working on developing a new plan for a series of products that Nic and I are sketching out. Because the other products are so much further out, they can be way more speculative. But this near-term project is the one I probably have the least grasp on, and Nic has the most grasp on. So we need to get some of this down.

I've called the three steps now Moabee, Haifei, and Coaptopia.

## Nic

Those names need some work. My approach with names is that every single project needs collaborators, and in order for collaborators to contribute well they need to feel some degree of investment in the project. This is why it's good to let collaborators name the project: it gives you complete control of the technical investment while giving them a large stake in something that is ultimately meaningless for the broad success of the project. It's an easy way to give up nothing and have them feel very involved.

## Brad

Yes — we have that in the audio archive already. The names are just meaningless collections of syllables to give the LLM a clear reference to something. But I guess the first-stage project is to develop this tool for impact investors.

## Nic

What is this tool in a sentence?

## Brad

What is this tool in a sentence? That's why I'm talking to you — I'm not sure I really have a clear picture of what this initial tool does or looks like. I put some revenue targets in the prompt, thinking about scaling the size of the market. For impact investors, that's very good. But it's just based on things you said — like that you'd like to be able to make $50,000 a year in order to support yourself. So we have to think about a tool that can scale to produce that sort of revenue, and that either replaces existing software purchases or enables impact investors to bring in more money.

## Nic

There's a secondary part to this, which is that as a researcher, research across multiple impact investing funds is a thing they would be willing to pay for, and it's a thing they want done. This is not a speculative need — one of the things they were talking about was, oh, this would be a great thing to do, we should probably go ahead and think about allocating budget for a person to work on this. After I brought it up, that's immediately what they said. That's promising. But those are the sort of conversations that are not clearly in the repository yet.

## Brad

They haven't been transferred to the repository yet — they're still in your head. So I need to pick at your head, in terms of what they said and what your ideas are. Some of it will be repetitive. To the extent that you have a sense for what this initial tool is going to do — because the initial tool is not pitched at all towards the cooperative-network side of it. The initial tool is pitched towards impact investors as they currently exist in the cooperative landscape.

## Nic

In the medium term it might be nice to have some kind of volunteer users, in the form of cooperatives and cooperative networks, or even have a cooperative network using us. But one of the things I'm very confident about is that this product is not going to be providing sufficient value to cooperative networks for them to dedicate money to it. They might be, in the broad scheme of things, free users but not paid users, and I think that's going to be the case for a long time.

The second project is geared towards unifying the cooperative network and the impact investor, which is quite different from how Mondragon did it — they started with an investment, and we're kind of bringing in investing later on. I think we've articulated fairly well how impact investors could use a cooperative network to produce greater returns by producing things more cooperatively. I think that's all second-project stuff, so I've lumped it under Haifa. This first project is something an impact investor would use that wouldn't necessarily provide any value to a cooperative network. If that's incorrect, let's clarify it, because that was my understanding.

## Brad

That's correct. So can you say a little bit more about the feedback you got from the impact investing community about what they wanted to see in this tool?

## Nic

There are a couple of things. The main demand is obviously for a fully done networking stack — there's clearly demand for that, and having demand for it would be very good.

## Brad

Can you say a little bit more about what that stack would include?

## Nic

The honest answer is that it didn't — the meeting brought it up for around a minute and then dropped it. Part of the rationale is that everyone seems to think, oh, having a shared back office, or a shared unified way of getting a software stack back office, is definitely a thing we could do that would save us all a bunch of money. Importantly, they're all spending a bunch of money on this. If they unified behind one approach, with one unified department handling it for all of the ten to twenty investment funds at the table, that would be good. That's the thing they would be interested in.

What that stack would entail, I did not get the information at that meeting to detail. So one of the things I'm going to have to do is actually reach out to Rachel soon, and potentially get her involved with actually doing reach-outs to all of the individual fund groups.

## Brad

So there are things that impact funds are doing already that they're using software for. Did they mention any particular tools that they're using that are expensive, or is this just generic? I assume they exist.

## Nic

Based on the context of the conversation, I assume they exist. This was also originally Rachel's suggestion — even though I was going to make it, we were just going around in a circle at the table.

And this being the unified back office, the unified back-office stack. The thing I specifically suggested was: all of you are funds, and all of you should be having some form of research or analytics that a larger fund might have, so that you can go ahead and not waste money on a hobby. If there's one clear and obvious pattern — every time you give money in this investment vehicle to this specific group of people, it always goes south and ends up having very poor outcomes for everyone involved — that might be data that's very hard to tease apart inside individual firms who might make two of those investments. But if the entire group has made thirty of those investments, it's very easy to pull that out from the data.

And that's the thing they said: yes, that's the thing we would 100% do. In order for us to do that, we would have to find the money for a staff member to work that full time, and that's the thing we should do as soon as we have a better vision for how that works out. That's where they left it.

Importantly, the whole point of that conversation is that, unlike every other group, I got the impression that there's gold in them hills. Any other group would be, oh, let's try to attract volunteer labor to do this for free, and they were immediately, okay, so this is a service we need, how would we allocate money to make sure this person can get paid? All of them were immediately on it. So first off, that's a sign that these people are going to be not shit-ass customers. It's important — and I may have some trauma about this — it's important to target customers that are actually willing to give you money. Very good signs on average.

The main thing I need to do for the combined back-office deck is really just have a lot of conversation with Rachel. You might want to join in on those, maybe not.

## Brad

One of the things I put in my write-up was that there's probably some sort of common core between Fortress and Moai that you would pull out, and then you would try to develop the business-to-consumer features on one end.

## Nic

I personally see this as maybe a closed-source extension — actually I don't even know if it needs to be closed source. I think we can say it's technically offered under a GPL v3 or a BSL or something similar. If you're wanting to run your own instance of it, you can go ahead. But essentially we're charging for that addition on top of the Fortress stack. That's the way I would probably run it.

## Brad

And you would give them the video and audio?

## Nic

Well, so the thing is that every single Fortress stack is an enabled thing, so there's a dashboard on there, and then you can enable or disable the dashboards. If something isn't enabled, it doesn't actually show up in your source tree at all. It's kind of like Nix packages: hypothetically every single Linux package installed could be on your machine, but it's not, because it's not in your config. That's how it works for all of the services. So you can literally add services ad infinitum and they're all declarative — the system will be the exact same if you add a service or delete a service.

There's a bit of lazy value there. The way NixOS does this is that technically every single package is on your system; you can run a command on any package. But it's lazily evaluated, so the program is under the impression that every single package is in the store at all times, while only those packages your system needs are actually installed. So you don't necessarily need to worry about whether we're introducing a bunch of tech debt: the service declarations exist on every single thing — here's what all the services could potentially be if they were invoked, and here are the names of them — but that's kind of the only overhead in that system.

I hate talking. I'll get some water. Actually, I need to get water — and I left a pseudoephedrine sheet in here somewhere.

## Brad

I did ask you to clean up your desk, so it's probably my fault. I'm going to pause this. No — keep going.

So I'm obviously most interested in the medium- and long-term projects, and I'm probably least able to help on the short-term project.

## Nic

That's probably true. The short-term project is more likely to be a me-and-Rachel thing, for sure. But I can research.

## Brad

If we are thinking about it — one of the things we talked about was a tool for measuring impact that would be a little bit different than generating impact on the cooperative-network side. Would you want to do something like, here's how we document and assess the impact that our investments have produced?

## Nic

For the beginning, for the initial tool, that is a thing we should experiment with, but it's not a service we should provide. We should explicitly tell them that — if we're talking about the impact fund investor — this is a feature we are currently working on, and maybe even going so far as to do user interviews for it. But ultimately, in terms of what we're providing them first, it's better to provide something that is well specced and suited to their expectations first; better to provide something that is well scoped and meets their expectations, as opposed to delivering something weird that might not meet their expectations, even if we manage to implement it very well.

There's an argument here where, at some level, it would need to do the stuff that a regular thing would be doing. It needs to be somewhat lossless — capable of replicating existing structures. That's both a user requirement, because there's a good chance they will be expecting financial software that looks and behaves, at least on the surface, like other financial software they interact with, and part of the broader point: even if you have a much more mathematically rich interior system, that interior still has to have a boundary with a system that is much smaller in dimension. You have a discontinuity going from a very complex internal modeling space — all of the production networks of a cooperative — to a very simple one-dimensional linear space.

## Brad

Let me clarify: I don't think the modeling, the cooperative stuff, is what the impact assessment tool would do. If you look at the stories they're telling about impact, probably very few of them relate to a cooperative network — I don't think any of them do. But what I think most of them have in common is how the investments that they make impact the material needs of people in their community.

That's kind of my big thing: what exactly is the benefit of more education inside a group? What exactly is the benefit of having fewer houses with lead paint? You could do the EPA thing, where a life equals $8.6 billion — or maybe it's higher now, maybe they updated it for inflation — and then figure out the financial impact of this. But fundamentally, that reduction of finances to good outcomes is part of the problem, potentially.

So I think one research project related to the first stage is researching impact investing as a sector: getting a good sense for what funds are out there, what people are doing, which funds are growing, where the whole field is. Because ultimately, one way to grow your business to where you can sustain yourself is to appeal to other impact investing funds that aren't necessarily in this cooperative space.

## Nic

I think that's true. If we can provide a service that works to these twenty funds and meets the $50,000 threshold criteria — the big issue is providing the customers that we have with something valuable, which is always a hard thing for any customer, especially customers as demanding as these people.

## Brad

I would be shocked if those companies are spending $2,500 a year on software.

## Nic

I don't think so. $2,500 a year is around $400 a month, which I think is very reasonable for a business that is probably a financial engineering business. For sure.

## Brad

That would be because they're using a tool that would be somewhat custom.

## Nic

Well, not even that. I'm saying that for just very standard accounting tools that hedge funds would use, that is a very low rate.

## Brad

That's still a somewhat custom piece of software — that's not something you're going to get up on Google Docs, or in Google Workspace. It's custom for the industry. One of the big R&D targets for this first phase is figuring out what they spend, what they spend it on, and what the names of those tools are — which is something you indicated you and Rachel will potentially be doing.

## Nic

Yeah. I need to talk her into it first, but I can probably manage.

## Brad

My guess is you will need a larger selection of funds.

## Nic

The thing is, my marketing strategy for this group of people — you can call it a marketing strategy — is that it's not B2C marketing. You can't go in there and say, oh, we want to go ahead and do this thing really well. The biggest problem with any B2B business is having an in. And we don't just have an in, we have twenty ins, and they're already kind of interested in doing a thing like this anyway.

Traditionally, once you have twenty or so customers, you go to every single customer and you beat them, then you take them to a base, and you beat them until they give you the list of all their contacts, then you get those contacts — or you spend a year making them really happy. But they'll only agree to give you contacts for other people if it's a thing they really like and it's worth doing, and mostly they will voluntarily share that information.

So importantly, we're at a point in time right now where we don't just have one customer, we have twenty. But it's also important that these customers are relatively big. There might only be two hundred impact investors, which means we have warm intros to 10% of all of our potential customers — which is a problem if we're trying to be very big. But I don't necessarily know if there's a lot of value in trying to get more customers until we provide something of value to the customers we already have.

## Brad

I agree. To me this looks like probably a year-long project before you would think about a phase two.

## Nic

Importantly, it's very important to have a vision for what you're doing, so you can actually make good decisions in the year-long term.

## Brad

I agree, and I'm more than happy to work on research on some of the longer-term things.

## Nic

At some point — I don't think most of the software that these hedge funds are using internally for their dashboards is that complicated. This could just be my relatively dim view of economists and finance people. Fundamentally, the services they're looking for are not that complicated.

There are two archetypes out there. There's the Apple interface: the iPhone settings menu isn't really doing anything complicated — if you wanted a shitty clone, you could probably mock one up in a couple of months — but part of what makes it complicated is that literal billions of dollars have gone into UI and polish, and a lot of that is interactive stuff that isn't immediately copyable. So you'd find yourself in a lot of trouble if you tried to do something like that. That has complexity, but a lot of the complexity is hidden in how it interacts.

And then there's another tool like GAP, the general computational library for all group theory. It's essentially a CLI where you name specific groups and solve specific problems in group theory. The UI is so simple that you could replicate the UI in a couple of days, and you could replicate the commands. But building the functionality in GAP has taken mathematicians literally around twenty years.

Financial engineering firms aren't doing anything anywhere near as complicated as GAP, or even something as complicated as a CAD program, which is very complicated but is still a thing you can prototype relatively quickly. And because it's a very small group of people selected, a small piece of software targeted to a select group, it's also not going to have the same UI polish that a product like Apple would have — which is true for a lot of enterprise software.

So a lot of really good software in this space comes from understanding exactly what the specific use cases of your clients are, then implementing those features, even if on the broad scale those features are not super technically complicated. So there's a part of it that is feasible in that regard. But we're also trying to give them something more.

## Brad

Right. But right now, how we give them something more is going to be very technically complex — and we don't know what that something more is. I have an idea of what that something more is, but I'm not sure you know enough about it right now to think about mocking something up for this initial presentation.

## Nic

For this initial presentation, no. The initial presentation should be basically a Fortress demo. If we're doing user interviews to figure out what the back-office needs are, we could also figure out what the existing tools are for existing hedge funds, and then ask them: if you were going to use something like this, what would be your use cases for it? And then listen to them complain about what they think their current use cases for a thing like this could be.

A lot of it is really simple: when you're making an investment decision — when you're making an uncertain investment decision — what part of that process is really painful, and what do you wish you had more info on? Listen and let them ramble on that. That might lead to a problem that's ultimately unsolvable, but there are a lot of nuggets you can get from that kind of very open-ended user interview process. Doing that's hard, but most of the stuff we're doing here is hard.

So I think it should be a demo of Fortress with the B2B client stuff, and a proposal for the research stack — just imitating, at this point in time, an expandable subset of what already currently exists. It's an expandable and inflatable subset of what already exists: you can inflate it up to the higher mathematical abstractions that we're wanting to do, but it can also get started as a small feature set of current functionality that people would actually want, and then grow from there. We can go and say, hey, this is what we're proposing. And then for longer-term business, we can make vague promises. Making vague promises is fine — no one ever went to jail for making vague promises.

## Brad

Okay. That's kind of my thing if I had to ramble about it a lot. I think this has been helpful — it will give the machine a little bit more to crunch on. But I do want it to focus on near-term stuff.

## Nic

But importantly, I also think maybe we should pause this conversation and resume another long-term conversation, so that the short- and long-term things are kind of separated in different files, potentially.

## Brad

Do you want to talk about the long-term stuff? I do. So let's pause this, save the recording, and then we'll start a long-term conversation.
