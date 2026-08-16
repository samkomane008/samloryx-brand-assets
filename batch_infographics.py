#!/usr/bin/env python3
"""Samloryx infographic series, 17 Aug to 15 Sep 2026. One post a day, LinkedIn + Facebook.

Every card is built from advice, a comparison or a process. None of them carry a statistic,
because there is no verified source for one (global rule 4). Topics are checked against
everything published 26 Jul to 16 Aug so nothing repeats.

Run: python3 batch_infographics.py <outdir>
"""
import sys
from pathlib import Path

import make_infographic
from cards_september import CARDS_SEP

CARDS = [
    {
        "date": "2026-08-17", "slug": "own-before-final-invoice",
        "spec": {
            "eyebrow": "Before you pay", "layout": "checklist", "seed": 17,
            "title": "Own these five things before the final invoice",
            "standfirst": "Ask while you still have leverage. A good supplier has them ready.",
            "items": [
                {"label": "The domain", "detail": "Registered to your business, registrar login in your hands."},
                {"label": "The DNS", "detail": "Or access to change it. This is what lets you move providers."},
                {"label": "The code", "detail": "In a repository your business controls, not only the developer."},
                {"label": "The mailboxes", "detail": "And the data in them, exportable."},
                {"label": "The running costs", "detail": "Where it runs, what it costs each month, written down."},
            ],
        },
        "linkedin": (
            "Before you pay the final invoice on any technology project, check that you own these five things.\n\n"
            "The domain, registered to your business, with the registrar login in your possession. Not \"managed by\" your supplier.\n\n"
            "The DNS, or at least access to change it. This is what lets you move providers without asking permission.\n\n"
            "The code, in a repository your business controls, with someone other than the developer able to log in.\n\n"
            "The mailboxes and their data, exportable.\n\n"
            "A written note of where it all runs and what it costs each month.\n\n"
            "None of this is unreasonable to ask, and a good supplier will have prepared it without being asked. "
            "If a request for the registrar login gets a vague answer, you have learned something useful while you still have leverage.\n\n"
            "#ClientEducation #SouthAfricanBusiness #TechnologyAdvice"
        ),
        "facebook": (
            "Before you pay the last invoice on a website or system, make sure you own these five things.\n\n"
            "The domain. The DNS. The code. The mailboxes and their data. A note of where it runs and what it costs monthly.\n\n"
            "All of it is fair to ask for. If the answer gets vague, that tells you something while you still have leverage."
        ),
    },
    {
        "date": "2026-08-18", "slug": "spreadsheet-vs-system",
        "spec": {
            "eyebrow": "When to switch", "layout": "compare", "seed": 18,
            "title": "A spreadsheet is fine, until it is not",
            "standfirst": "The switch is rarely about size. It is about who depends on it.",
            "left": {"heading": "Still fine as a spreadsheet", "points": [
                "One person maintains it", "Mistakes are visible and cheap",
                "Nobody else needs it live", "The rules rarely change"]},
            "right": {"heading": "Time for a system", "points": [
                "Two people edit the same file", "You keep a copy \"just in case\"",
                "Somebody rekeys it elsewhere", "A mistake reaches a customer"]},
        },
        "linkedin": (
            "Most businesses do not outgrow a spreadsheet because it got too big. They outgrow it the day a second person needs it.\n\n"
            "A spreadsheet is still the right tool when one person owns it, mistakes are obvious and cheap to fix, and the rules behind it barely change. "
            "Plenty of good businesses run that way for years, and there is nothing wrong with it.\n\n"
            "The signs it has stopped being the right tool are quite specific. Two people edit the same file and reconcile afterwards. "
            "Somebody keeps a private copy because they do not trust the shared one. The same numbers get retyped into another system. "
            "And the one that actually costs money: a mistake in it reaches a customer before anyone notices.\n\n"
            "That is the point where the spreadsheet is no longer a tool. It has quietly become a system, without any of the protections a system would have.\n\n"
            "#Operations #BusinessSystems #SmallBusiness"
        ),
        "facebook": (
            "You do not outgrow a spreadsheet because it got big. You outgrow it the day a second person needs it.\n\n"
            "Two people editing the same file. Someone keeping a private copy they trust more. The same numbers retyped somewhere else. "
            "A mistake that reaches a customer.\n\n"
            "At that point it is not a spreadsheet any more. It is a system without any of the protections a system would have."
        ),
    },
    {
        "date": "2026-08-19", "slug": "whatsapp-business-channel",
        "spec": {
            "eyebrow": "SA practical", "layout": "checklist", "seed": 19,
            "title": "WhatsApp is a business channel. Run it like one.",
            "standfirst": "Four fixes, roughly in order of effort.",
            "items": [
                {"label": "Use a number the company owns", "detail": "Not a personal SIM that walks out with the person."},
                {"label": "Record what was agreed", "detail": "A quote agreed in a chat and nowhere else is a dispute waiting."},
                {"label": "Set real hours", "detail": "An away message with honest hours beats a fast reply on Tuesday and silence on Thursday."},
                {"label": "Decide who covers leave", "detail": "Before the leave, not during it."},
            ],
        },
        "linkedin": (
            "In South Africa, WhatsApp is where the customer conversation actually happens. Most businesses still run it badly.\n\n"
            "The usual pattern: enquiries land on one employee's personal number. When they are on leave, the business is unreachable. "
            "When they resign, the history leaves with them, and sometimes the customer does too.\n\n"
            "Four fixes, roughly in order of effort. Move to a business number the company controls. "
            "Decide what gets recorded elsewhere, because a quote agreed in a chat that never reaches your system is a dispute waiting to happen. "
            "Set an expectation in the away message, since consistency beats speed. And agree who covers leave before somebody takes it.\n\n"
            "None of that needs a platform. It needs a decision that WhatsApp is a business channel, and then treating it like one.\n\n"
            "#CustomerService #SouthAfricanBusiness #Operations"
        ),
        "facebook": (
            "WhatsApp is where most South African customers want to talk to you. Most businesses run it off one person's personal phone.\n\n"
            "So when they are on leave, you are unreachable. When they leave the company, the chat history goes with them.\n\n"
            "Use a business number the company owns. Record anything agreed somewhere proper. Set an away message with your real hours. "
            "Agree who covers leave before someone takes it."
        ),
    },
    {
        "date": "2026-08-20", "slug": "where-ai-helps",
        "spec": {
            "eyebrow": "AI, realistically", "layout": "compare", "seed": 20,
            "title": "Where AI helps, and where it quietly costs you",
            "standfirst": "The question is not whether it can. It is what happens when it is wrong.",
            "left": {"heading": "Expensive", "points": [
                "Writing to financial records", "Changing customer details",
                "Sending on your behalf unreviewed", "Anything where being wrong is silent"]},
            "right": {"heading": "Genuinely useful", "points": [
                "Drafting a first version", "Summarising long documents",
                "Sorting and first-pass classification", "Pulling the relevant part out of forty pages"]},
        },
        "linkedin": (
            "A practical way to think about where AI agents help and where they cost you.\n\n"
            "They are good at work where being roughly right is useful and a person checks the output. "
            "Drafting, summarising, sorting, first-pass classification, pulling the relevant three paragraphs out of forty pages.\n\n"
            "They are expensive where being wrong is quiet. Anything that writes to your financial records, changes a customer's details, "
            "or sends something on your behalf without review. Not because the technology cannot do it, but because that kind of failure "
            "does not announce itself and you find out much later.\n\n"
            "So the design question is not \"can an agent do this\". It is \"what happens when it is confidently wrong, and who notices\".\n\n"
            "Put a person at the point of consequence. Automate everything up to it.\n\n"
            "#AI #Automation #TechnologyLeadership"
        ),
        "facebook": (
            "Where AI actually helps, and where it quietly costs you.\n\n"
            "Good at: drafting, summarising, sorting, finding the important part of a long document. Work where roughly right is useful and a person checks it.\n\n"
            "Risky at: anything that changes your records or reaches a customer without review, because that kind of mistake stays hidden.\n\n"
            "Put a person at the point of consequence, and automate everything up to it."
        ),
    },
    {
        "date": "2026-08-21", "slug": "roadmap-sprint-stages",
        "spec": {
            "eyebrow": "How it works", "layout": "flow", "seed": 21,
            "title": "What actually happens in a Roadmap Sprint",
            "items": [
                {"label": "Sit with the people doing the work", "detail": "Not only the managers describing it."},
                {"label": "Write the process down as it really runs", "detail": "Including the workarounds nobody mentions in meetings."},
                {"label": "Separate the fixes from the projects", "detail": "Some of it is a rule change, not software."},
                {"label": "Sequence it by payback", "detail": "Cheapest relief first, so the work funds itself."},
            ],
        },
        "linkedin": (
            "People ask what a Roadmap Sprint actually involves, so here it is without the brochure language.\n\n"
            "We sit with the people doing the work, not only the managers describing it. Those two accounts of a process are almost never the same, "
            "and the difference is usually where the money is going.\n\n"
            "We write down how the process really runs, workarounds included. Then we separate what is genuinely a software problem "
            "from what is a rule nobody has questioned in years. A surprising amount of it is the second kind, and that part is free to fix.\n\n"
            "What is left gets sequenced by payback, cheapest relief first, so the early work pays for the later work.\n\n"
            "You end up with a plan you could hand to another supplier. That is deliberate. If the plan only works with us, it was not a plan.\n\n"
            "#Consulting #Operations #DigitalTransformation"
        ),
        "facebook": (
            "What a Roadmap Sprint actually involves.\n\n"
            "We sit with the people doing the work, not only the managers describing it. We write down how the process really runs, workarounds included. "
            "Then we separate the software problems from the rules nobody has questioned in years, and sequence the rest cheapest relief first.\n\n"
            "You end up with a plan you could hand to another supplier. That is on purpose."
        ),
    },
    {
        "date": "2026-08-22", "slug": "questions-for-a-supplier",
        "spec": {
            "eyebrow": "Before you sign", "layout": "checklist", "seed": 22,
            "title": "Six questions worth asking any software supplier",
            "standfirst": "The answers matter less than how comfortable they are answering.",
            "items": [
                {"label": "Who owns the code when we are done?"},
                {"label": "What happens if we stop working together?"},
                {"label": "What does this cost to run each month?"},
                {"label": "Who else can support this if you cannot?"},
                {"label": "What is deliberately not included?"},
                {"label": "What would make you tell us not to build it?"},
            ],
        },
        "linkedin": (
            "Six questions worth asking any software supplier before you sign anything.\n\n"
            "Who owns the code when we are done. What happens if we stop working together. What does this cost to run every month, "
            "separately from what it costs to build. Who else could support this if you could not. What is deliberately not included. "
            "And the one that tells you the most: what would make you advise us not to build this at all.\n\n"
            "The answers matter less than how comfortable someone is answering them. A supplier who has thought about the end of the "
            "relationship as carefully as the start is usually a safer bet than one who has only prepared the optimistic version.\n\n"
            "We would rather be asked these early. It saves a difficult conversation later.\n\n"
            "#Procurement #SoftwareDevelopment #BusinessAdvice"
        ),
        "facebook": (
            "Six questions worth asking any software supplier before you sign.\n\n"
            "Who owns the code. What happens if we stop working together. What does it cost to run monthly. Who else could support it. "
            "What is deliberately not included. And what would make you tell us not to build it.\n\n"
            "How comfortable someone is answering tells you more than the answers do."
        ),
    },
    {
        "date": "2026-08-23", "slug": "one-week-technology-audit",
        "spec": {
            "eyebrow": "Costs a week", "layout": "steps", "seed": 23,
            "title": "The cheapest technology audit you will ever run",
            "standfirst": "No consultant required. A note on a phone will do.",
            "items": [
                {"label": "Ask everyone to note it down", "detail": "Any task they did that a computer could plausibly have done."},
                {"label": "Give it a week", "detail": "Nothing formal, no forms, no meetings about the exercise."},
                {"label": "Sort what comes back", "detail": "Daily repeats, gaps between systems, and work that is nobody's job."},
                {"label": "Start with the daily repeats", "detail": "They pay back fastest and prove the idea to everyone else."},
            ],
        },
        "linkedin": (
            "A short exercise worth doing before you spend anything on new technology this year.\n\n"
            "For one week, ask everyone to note down the tasks they did that a computer could plausibly have done. "
            "Not a formal study. A note on a phone is enough.\n\n"
            "By Friday you will have three lists without anyone setting out to make them. Things done more than once a day, which are worth "
            "automating first. Things that only exist because two systems do not talk to each other, which are integration work. "
            "And things that turn out to be nobody's job, which is a management conversation rather than a technology one.\n\n"
            "Most technology budgets get committed before anyone does this. It costs a week and nothing else, and it is usually more "
            "accurate than the requirements document that follows it.\n\n"
            "#BusinessEfficiency #Automation #PracticalAdvice"
        ),
        "facebook": (
            "Before you spend money on new systems this year, try this for one week.\n\n"
            "Ask everyone to jot down any task they did that a computer probably could have. Just a note on their phone.\n\n"
            "By Friday you will have three lists: things worth automating, things that only exist because two systems do not talk, "
            "and things that turn out to be nobody's job. That last one is not a technology problem.\n\n"
            "Costs a week and nothing else."
        ),
    },
    {
        "date": "2026-08-24", "slug": "process-in-one-head",
        "spec": {
            "eyebrow": "Key person risk", "layout": "checklist", "seed": 24,
            "title": "Five signs a process lives in one person's head",
            "standfirst": "None of this is about loyalty. It is about what the business can see.",
            "items": [
                {"label": "Work waits when they are on leave"},
                {"label": "Nobody else can explain the exceptions"},
                {"label": "Training happens by sitting next to them"},
                {"label": "The rules changed and nobody wrote it down"},
                {"label": "You cannot audit it without asking them"},
            ],
        },
        "linkedin": (
            "If a process lives in one person's head, it is not a process. It is a risk with a salary attached.\n\n"
            "Every business has that person. They know which invoices to hold back, which customer gets the special discount, "
            "and why the Wednesday export has to run before the Tuesday one. They are usually excellent, and they have usually "
            "never been asked to write any of it down.\n\n"
            "The problem is not loyalty. It is that a business cannot change a rule it cannot see, cannot train a second person, "
            "and cannot take that person's leave seriously.\n\n"
            "The fix starts small. Sit with them for an hour and write the rules down in plain language, in the order they actually happen. "
            "Half the time you will find a rule nobody can justify any more. That is the one worth deleting before you automate anything.\n\n"
            "#BusinessProcess #Operations #RiskManagement"
        ),
        "facebook": (
            "If a process only lives in one person's head, it is not a process. It is a risk.\n\n"
            "Work waits when they are on leave. Nobody else can explain the exceptions. Training happens by sitting next to them.\n\n"
            "Sit with them for an hour and get the rules on paper. Half the time you will find a rule nobody can justify any more."
        ),
    },
    {
        "date": "2026-08-25", "slug": "integration-middle-layer",
        "spec": {
            "eyebrow": "Integration", "layout": "compare", "seed": 25,
            "title": "Why the fifth integration costs more than the first four",
            "standfirst": "Connecting everything to everything grows faster than the business does.",
            "left": {"heading": "Point to point", "points": [
                "Fast for the first two", "Each new system touches all the others",
                "One change breaks several links", "Nobody can draw the picture"]},
            "right": {"heading": "One layer in the middle", "points": [
                "Slower to start", "New system connects once",
                "Changes stay in one place", "You can see what talks to what"]},
        },
        "linkedin": (
            "The fifth integration always costs more than the first four, and it catches people out.\n\n"
            "Connecting two systems directly is quick and sensible. So is the third. By the time you have five or six systems all wired "
            "to each other, you are maintaining a web nobody can draw on a whiteboard, and a small change in one place breaks something "
            "two systems away.\n\n"
            "The alternative is slower to start: everything talks to one layer in the middle, and each new system connects once rather than "
            "to everything already there. It feels like overhead on day one and pays for itself around the fourth connection.\n\n"
            "You do not need this on day one. You need to know roughly when you will, and not to be surprised by it.\n\n"
            "#Integration #SystemsArchitecture #APIs"
        ),
        "facebook": (
            "The fifth integration always costs more than the first four.\n\n"
            "Wiring two systems together directly is quick and sensible. By the fifth, you are maintaining a web nobody can draw, "
            "and a small change breaks something two systems away.\n\n"
            "The alternative is slower to start and much cheaper by the fourth connection: everything talks to one layer in the middle."
        ),
    },
    {
        "date": "2026-08-26", "slug": "enquiry-to-invoice",
        "spec": {
            "eyebrow": "The manual path", "layout": "flow", "seed": 26,
            "title": "From enquiry to invoice, the steps most businesses still do by hand",
            "items": [
                {"label": "Enquiry arrives", "detail": "Email, WhatsApp or a phone call somebody writes on paper."},
                {"label": "Someone retypes it", "detail": "Into a spreadsheet, or a quote template, or both."},
                {"label": "Quote goes out and waits", "detail": "Follow-up depends on whoever remembers."},
                {"label": "Job gets done", "detail": "Details live in a chat thread and one person's memory."},
                {"label": "Invoice gets rebuilt from scratch", "detail": "Using the same information, typed a third time."},
            ],
        },
        "linkedin": (
            "Draw the path an enquiry takes through your business, from the first message to the invoice. Count how many times "
            "the same information gets typed in by a person.\n\n"
            "In most businesses we see, it is three or four. Once when the enquiry is written down, once into a quote, once into whatever "
            "tracks the job, and once more when the invoice is raised. Each retype is a chance for a number to change, "
            "and none of it makes anything better for the customer.\n\n"
            "The useful part is that you do not need one big system to fix it. Removing a single retype, usually the one between quote and invoice, "
            "is often a small piece of work with an obvious payback.\n\n"
            "Start by drawing it honestly. The picture usually makes the decision for you.\n\n"
            "#Automation #Operations #SmallBusiness"
        ),
        "facebook": (
            "Draw the path an enquiry takes through your business, from first message to invoice. Count how many times a person retypes "
            "the same information.\n\n"
            "In most businesses it is three or four times. Every retype is a chance for a number to change, and none of it helps the customer.\n\n"
            "You do not need one big system to fix that. Removing a single retype is often a small job with an obvious payback."
        ),
    },
    {
        "date": "2026-08-27", "slug": "access-control",
        "spec": {
            "eyebrow": "Access", "layout": "checklist", "seed": 27,
            "title": "Who should have access to what",
            "standfirst": "Most access problems are not attacks. They are leftovers.",
            "items": [
                {"label": "Everyone has their own login", "detail": "Shared accounts make it impossible to tell who did what."},
                {"label": "Access ends when the job ends", "detail": "Check leavers on the day, not at the next audit."},
                {"label": "Admin rights are the exception", "detail": "Two people, not everyone, and not the daily-use account."},
                {"label": "Someone owns the list", "detail": "A person, by name, who reviews it quarterly."},
            ],
        },
        "linkedin": (
            "Most access problems in small businesses are not attacks. They are leftovers.\n\n"
            "An ex-employee whose email still works. A shared login three people use, so nobody can say who changed the price list. "
            "A supplier who was given admin rights for a project that ended last year.\n\n"
            "Four things worth fixing before anything more sophisticated. Everyone gets their own login. Access ends the day the job ends, "
            "not at the next audit. Admin rights go to two named people and are not the account anyone uses daily. And one person, "
            "by name, owns the list and reviews it every quarter.\n\n"
            "None of that costs money. It costs an afternoon, and it closes the gap most incidents actually come through.\n\n"
            "#Security #POPIA #SouthAfricanBusiness"
        ),
        "facebook": (
            "Most access problems in a small business are not attacks. They are leftovers.\n\n"
            "The ex-employee whose email still works. The shared login three people use, so nobody can say who changed what. "
            "The supplier still holding admin rights from a project that ended.\n\n"
            "Own logins for everyone, access ends when the job ends, admin rights for two named people, and one person who reviews the list. "
            "Costs an afternoon."
        ),
    },
    {
        "date": "2026-08-28", "slug": "fixed-vs-hourly",
        "spec": {
            "eyebrow": "How we price", "layout": "compare", "seed": 28,
            "title": "Fixed scope or hourly: who carries the uncertainty",
            "standfirst": "Both are honest. They just put the risk in different places.",
            "left": {"heading": "Hourly", "points": [
                "You carry the uncertainty", "Works when the work is genuinely open ended",
                "Needs trust you have not built yet", "You watch a clock you cannot read"]},
            "right": {"heading": "Fixed scope", "points": [
                "We carry the uncertainty", "Forces us to understand it before quoting",
                "Small, defined, easy to stop", "If we cannot price it, that is information"]},
        },
        "linkedin": (
            "Why we quote fixed scope for a first piece of work, even though hourly would earn us more when things run long.\n\n"
            "An hourly rate makes uncertainty the client's problem. You carry the risk of a discovery that takes longer than expected, "
            "and you are watching a clock you cannot read. That is a strange thing to ask of someone who has not worked with us before.\n\n"
            "Fixed scope forces us to understand the problem well enough to price it. If we cannot, that is worth knowing before you commit money.\n\n"
            "It also keeps us honest about size. Small, defined pieces of work with a clear end are easier to say yes to, easier to judge us on, "
            "and easier to stop if we are not the right fit.\n\n"
            "Hourly has its place, usually later, once both sides know how the other works. Trust gets built on delivery, not on a proposal.\n\n"
            "#Consulting #Pricing #BusinessAdvice"
        ),
        "facebook": (
            "Why we quote a fixed price on the first job, even though charging by the hour would often earn us more.\n\n"
            "Hourly makes the uncertainty your problem. You end up watching a clock you cannot read, for a company you have never worked with.\n\n"
            "A fixed price forces us to understand your problem well enough to price it. If we cannot, you should know that before you spend anything."
        ),
    },
    {
        "date": "2026-08-29", "slug": "handovers-where-work-is-lost",
        "spec": {
            "eyebrow": "Where it goes wrong", "layout": "steps", "seed": 29,
            "title": "Work does not get lost in the doing. It gets lost in the handing over.",
            "items": [
                {"label": "Sales to delivery", "detail": "What was promised is not quite what was written down."},
                {"label": "Delivery to support", "detail": "Nobody told support the thing exists until it broke."},
                {"label": "Support to finance", "detail": "Extra work was done and never billed."},
                {"label": "Person to person on leave", "detail": "The handover was a five minute conversation in a corridor."},
            ],
        },
        "linkedin": (
            "Work rarely goes missing while somebody is doing it. It goes missing in the gaps between people.\n\n"
            "Sales agrees something that does not quite match what gets written down, so delivery builds the written version. "
            "Delivery finishes and support hears about it when a customer phones. Support does extra work that finance never sees, so it is never billed. "
            "Someone goes on leave after a five minute corridor handover.\n\n"
            "Every one of those is a small failure of recording rather than effort. The people involved are all doing their jobs properly.\n\n"
            "If you want one place to look for lost margin, look at your handovers before you look at your team.\n\n"
            "#Operations #BusinessProcess #Efficiency"
        ),
        "facebook": (
            "Work rarely goes missing while someone is doing it. It goes missing in the gaps between people.\n\n"
            "Sales to delivery. Delivery to support. Support to finance. One person to whoever covers their leave.\n\n"
            "Every one of those is a recording problem, not an effort problem. If you are looking for lost margin, check your handovers before you check your team."
        ),
    },
    {
        "date": "2026-08-30", "slug": "what-to-back-up",
        "spec": {
            "eyebrow": "Backups", "layout": "checklist", "seed": 30,
            "title": "A backup you have never restored is a hope, not a backup",
            "standfirst": "Four things worth checking this month.",
            "items": [
                {"label": "You know what is backed up", "detail": "Files, database, email and the settings that make it all work."},
                {"label": "One copy is somewhere else", "detail": "A second copy on the same machine is not a second copy."},
                {"label": "Someone has actually restored one", "detail": "Restore a single file this week and time it."},
                {"label": "You know how much you would lose", "detail": "The gap between backups is the work you would redo."},
            ],
        },
        "linkedin": (
            "A backup nobody has ever restored is not a backup. It is a hope with a schedule.\n\n"
            "Four things worth checking this month. Do you know exactly what is being backed up, including email and the configuration "
            "that makes everything work, not only the obvious files. Is one copy somewhere other than the machine it came from. "
            "Has anyone actually restored something recently. And do you know how much work you would lose, "
            "because the gap between backups is the work your team would have to redo.\n\n"
            "The test is simple and takes twenty minutes. Pick one file, restore it, and time how long it took. "
            "If nobody is confident enough to try, you have your answer.\n\n"
            "#BusinessContinuity #Security #SmallBusiness"
        ),
        "facebook": (
            "A backup nobody has ever restored is not a backup. It is a hope.\n\n"
            "Do you know what is actually backed up, email and settings included? Is one copy somewhere other than the original machine? "
            "Has anyone restored anything recently?\n\n"
            "Pick one file, restore it, and time it. Twenty minutes, and you will know where you stand."
        ),
    },
    {
        "date": "2026-08-31", "slug": "forgotten-costs",
        "spec": {
            "eyebrow": "Budgeting", "layout": "steps", "seed": 31,
            "title": "Four costs people forget when budgeting a system",
            "standfirst": "The build price is the part everyone quotes. It is rarely the whole number.",
            "items": [
                {"label": "Running it", "detail": "Hosting, domains, certificates, licences, every month, forever."},
                {"label": "Getting the old data in", "detail": "Usually messier than the build itself."},
                {"label": "Teaching people to use it", "detail": "Including the ones who liked the old way."},
                {"label": "The year two changes", "detail": "The business will move. Budget for it or the system ages out."},
            ],
        },
        "linkedin": (
            "The build price is the number everyone quotes. It is rarely the whole cost.\n\n"
            "Four things that get left out. Running it, which is hosting, domains, certificates and licences every month for as long as you use it. "
            "Getting your existing data in, which is usually messier than the build itself, because real data is never as tidy as the spreadsheet suggests. "
            "Teaching people to use it, including the ones who preferred the old way. And the changes in year two, because the business will move "
            "and a system nobody is allowed to change starts ageing the day it launches.\n\n"
            "None of that is a reason not to build. It is a reason to ask for the monthly number alongside the project number, "
            "so the decision is made on the real figure.\n\n"
            "#Budgeting #TechnologyStrategy #BusinessAdvice"
        ),
        "facebook": (
            "The build price is the number everyone quotes. It is rarely the whole cost.\n\n"
            "Running it every month. Getting your old data in, which is usually messier than the build. Teaching people to use it. "
            "And the changes you will want in year two.\n\n"
            "Ask for the monthly number alongside the project number, so you are deciding on the real figure."
        ),
    },
]


CARDS += CARDS_SEP


def main():
    outdir = Path(sys.argv[1] if len(sys.argv) > 1 else "social/infographics")
    outdir.mkdir(parents=True, exist_ok=True)
    for card in CARDS:
        path = outdir / f"{card['date']}-{card['slug']}.png"
        make_infographic.build(card["spec"], str(path))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
