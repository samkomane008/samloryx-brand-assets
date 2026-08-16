"""Second half of the infographic series, 1 to 15 September 2026."""

CARDS_SEP = [
    {
        "date": "2026-09-01", "slug": "phasing-a-big-system",
        "spec": {
            "eyebrow": "Phasing", "layout": "flow", "seed": 41,
            "title": "Three ways to phase a system that is too big to build at once",
            "items": [
                {"label": "By process", "detail": "Take one end-to-end path and finish it properly, then the next."},
                {"label": "By team", "detail": "One department live and settled before you touch another."},
                {"label": "By risk", "detail": "The part that hurts most today, even if it is the awkward one."},
            ],
        },
        "linkedin": (
            "Most systems that fail were not badly built. They were built all at once.\n\n"
            "If a project is too big to deliver in one go, there are three sensible ways to cut it, and picking the wrong one is expensive.\n\n"
            "By process: take one path from start to finish, say enquiry to quote, and finish it properly before starting the next. "
            "People get something usable early and you learn how they really work.\n\n"
            "By team: one department live and settled before the next. Slower, but the support load stays manageable.\n\n"
            "By risk: start with whatever is hurting most, even if it is the awkward part. Least comfortable, best return when something is genuinely on fire.\n\n"
            "What does not work is slicing by technical layer, building the whole database first and the screens later. "
            "Nobody can use half of that, so nobody can tell you if it is right.\n\n"
            "#ProjectDelivery #SoftwareDevelopment #Operations"
        ),
        "facebook": (
            "Most systems that fail were not badly built. They were built all at once.\n\n"
            "Three sensible ways to cut a big project: by process, one path finished properly at a time; by team, one department settled before the next; "
            "or by risk, starting with whatever hurts most.\n\n"
            "What does not work is building the whole database first and the screens later. Nobody can use half of that."
        ),
    },
    {
        "date": "2026-09-02", "slug": "writing-a-requirement",
        "spec": {
            "eyebrow": "Getting what you asked for", "layout": "checklist", "seed": 42,
            "title": "How to write a requirement a developer can actually build",
            "standfirst": "Four things that turn a wish into something buildable.",
            "items": [
                {"label": "Say who it is for", "detail": "\"The credit controller\", not \"the user\"."},
                {"label": "Say what happens today", "detail": "The current workaround explains more than the request does."},
                {"label": "Give a real example", "detail": "One actual invoice, one actual customer, with the awkward details left in."},
                {"label": "Say what wrong looks like", "detail": "What must never happen is often the real requirement."},
            ],
        },
        "linkedin": (
            "\"We need better reporting\" is not a requirement. It is a feeling, and a developer cannot build it.\n\n"
            "Four things turn it into something buildable.\n\n"
            "Say who it is for by role: the credit controller, not the user. Say what happens today, because the current workaround usually "
            "explains the need better than the request does. Give one real example with the awkward details left in, a genuine invoice for a genuine "
            "customer rather than a tidy made-up one. And say what wrong looks like, because \"this must never show a credit note as revenue\" "
            "is often the actual requirement hiding underneath.\n\n"
            "You do not need to write a specification. Four honest sentences and one real example will get you most of the way, "
            "and they cost you fifteen minutes instead of a rebuild.\n\n"
            "#Requirements #SoftwareDevelopment #BusinessAnalysis"
        ),
        "facebook": (
            "\"We need better reporting\" is not a requirement. It is a feeling, and nobody can build it.\n\n"
            "Say who it is for, by role. Say what happens today, including the workaround. Give one real example with the awkward bits left in. "
            "And say what wrong looks like.\n\n"
            "Four sentences and one real example. Fifteen minutes now, instead of a rebuild later."
        ),
    },
    {
        "date": "2026-09-03", "slug": "cheap-now-vs-three-years",
        "spec": {
            "eyebrow": "Total cost", "layout": "compare", "seed": 43,
            "title": "Cheap now, or cheap over three years",
            "standfirst": "Both are valid choices. Make it on purpose.",
            "left": {"heading": "Cheap now", "points": [
                "Lowest quote wins", "Nobody asks about running costs",
                "One person can support it", "Changes need the original developer"]},
            "right": {"heading": "Cheap over three years", "points": [
                "Monthly cost known upfront", "Written down well enough to hand over",
                "More than one person could support it", "Changing it does not need a favour"]},
        },
        "linkedin": (
            "The cheapest quote and the cheapest system are usually not the same thing, and the gap shows up in year two.\n\n"
            "Cheap now looks like this: the lowest quote wins, nobody asks what it costs to run, and the person who built it is the only "
            "one who understands it. It works fine until you need a change and discover the price of that change is whatever they say it is.\n\n"
            "Cheap over three years looks duller. The monthly running cost is on the table before you sign. It is documented well enough "
            "that a second person could pick it up. Changing it does not depend on one person's goodwill.\n\n"
            "Sometimes cheap now is genuinely the right call, when you are testing an idea or the business might change direction entirely. "
            "The mistake is choosing it by accident because nobody asked the second set of questions.\n\n"
            "#TechnologyStrategy #Procurement #BusinessAdvice"
        ),
        "facebook": (
            "The cheapest quote and the cheapest system are usually not the same thing. The gap shows up in year two.\n\n"
            "Cheap now: lowest quote, no discussion of running costs, one person who understands it. Fine until you need a change.\n\n"
            "Sometimes cheap now is the right call. The mistake is choosing it by accident because nobody asked the second set of questions."
        ),
    },
    {
        "date": "2026-09-04", "slug": "how-we-run-a-project",
        "spec": {
            "eyebrow": "How we work", "layout": "flow", "seed": 44,
            "title": "How a project runs with us, start to finish",
            "items": [
                {"label": "Discovery", "detail": "We watch the work happen before we design anything."},
                {"label": "Scope and fixed price", "detail": "Written so you could hand it to somebody else."},
                {"label": "Build in visible pieces", "detail": "Something you can click on early, not a reveal at the end."},
                {"label": "Handover", "detail": "Logins, documentation and a second person who could support it."},
            ],
        },
        "linkedin": (
            "How a project actually runs with us, in four stages.\n\n"
            "Discovery, where we watch the work happen rather than design from a description of it. Scope and a fixed price, written plainly "
            "enough that you could take it to another supplier, which is deliberate. Then the build, in pieces you can click on as they land, "
            "because a reveal at the end is how everybody discovers the misunderstanding too late.\n\n"
            "Then handover, and this is the part people underestimate. Logins in your name, documentation written for somebody who was not in "
            "the room, and ideally a second person who could support it. A project is not finished when it works. It is finished when it "
            "would survive us disappearing.\n\n"
            "#Consulting #SoftwareDelivery #HowWeWork"
        ),
        "facebook": (
            "How a project runs with us.\n\n"
            "Discovery, where we watch the work happen instead of designing from a description. A scope and fixed price written plainly enough "
            "that you could take it elsewhere. A build you can see in pieces, not a reveal at the end. Then handover: logins in your name, "
            "documentation, and a second person who could support it.\n\n"
            "A project is finished when it would survive us disappearing."
        ),
    },
    {
        "date": "2026-09-05", "slug": "documentation-that-gets-used",
        "spec": {
            "eyebrow": "Documentation", "layout": "checklist", "seed": 45,
            "title": "Documentation nobody reads is a cost, not an asset",
            "standfirst": "Four pages worth more than forty.",
            "items": [
                {"label": "Where everything runs", "detail": "Hosting, domain, who to phone, what it costs."},
                {"label": "How to do the five common things", "detail": "The tasks people actually repeat, in order."},
                {"label": "What breaks and what to try first", "detail": "Written by whoever fixed it last."},
                {"label": "Who has access", "detail": "Names, systems, and when it was last checked."},
            ],
        },
        "linkedin": (
            "Most technical documentation is written once, filed, and never opened. That is not documentation, it is a receipt.\n\n"
            "Four pages that genuinely get used, in our experience.\n\n"
            "Where everything runs, including hosting, domain, who to phone and what it costs monthly. How to do the five things people "
            "actually repeat, written in order with no assumed knowledge. What tends to break and what to try first, written by whoever "
            "fixed it last, while they still remember. And who has access to what, with the date it was last checked.\n\n"
            "That is a morning's work and it covers the questions that actually get asked at seven in the evening when something is down.\n\n"
            "The forty page system specification can wait. It usually waits forever, and that is fine.\n\n"
            "#Documentation #Operations #ITSupport"
        ),
        "facebook": (
            "Most technical documentation is written once, filed, and never opened again.\n\n"
            "Four pages that actually get used: where everything runs and what it costs, how to do the five common tasks, "
            "what breaks and what to try first, and who has access.\n\n"
            "A morning's work, and it answers the questions people actually ask at seven in the evening when something is down."
        ),
    },
    {
        "date": "2026-09-06", "slug": "before-you-automate",
        "spec": {
            "eyebrow": "Before you automate", "layout": "steps", "seed": 46,
            "title": "Five questions to ask before automating anything",
            "items": [
                {"label": "Does this task need to exist?", "detail": "Automating something pointless makes it permanent."},
                {"label": "How often does it really happen?", "detail": "Count it for a week rather than guessing."},
                {"label": "What does it cost when it is wrong?", "detail": "That number decides how much checking you build in."},
                {"label": "Who owns it afterwards?", "detail": "Automation without an owner rots quietly."},
                {"label": "How will we know it stopped?", "detail": "The dangerous failure is the silent one."},
            ],
        },
        "linkedin": (
            "Five questions worth asking before you automate anything.\n\n"
            "Does this task need to exist at all. Automating something pointless does not remove it, it makes it permanent and gives it a maintenance cost.\n\n"
            "How often does it genuinely happen. Count for a week instead of guessing, because people reliably overestimate the annoying tasks "
            "and underestimate the frequent ones.\n\n"
            "What does it cost when it goes wrong. That number, not the technology, decides how much checking to build in.\n\n"
            "Who owns it once it is running. Automation without an owner rots quietly.\n\n"
            "And how will anyone know if it stops. The dangerous failure is not the loud one, it is the job that silently stopped running in March.\n\n"
            "#Automation #Operations #ProcessImprovement"
        ),
        "facebook": (
            "Five questions before you automate anything.\n\n"
            "Does this task need to exist? How often does it really happen? What does it cost when it is wrong? Who owns it afterwards? "
            "And how will you know if it stops?\n\n"
            "That last one matters most. The dangerous failure is not the loud one, it is the job that quietly stopped running in March."
        ),
    },
    {
        "date": "2026-09-07", "slug": "rebuild-or-refactor",
        "spec": {
            "eyebrow": "Old systems", "layout": "compare", "seed": 47,
            "title": "Rebuild it, or fix what is there",
            "standfirst": "Rewriting feels cleaner. It is usually slower than it looks.",
            "left": {"heading": "Fix what is there", "points": [
                "The business rules already work", "Users keep what they know",
                "Value arrives in weeks", "Harder to feel proud of"]},
            "right": {"heading": "Rebuild", "points": [
                "Nobody can safely change it", "The platform is out of support",
                "You will rediscover forgotten rules", "Budget for double the surprises"]},
        },
        "linkedin": (
            "Every old system eventually raises the same question: fix it, or start again.\n\n"
            "Rewriting feels cleaner, and it is usually slower than it looks. The old system contains years of business rules nobody "
            "wrote down, and you will rediscover them one at a time, generally through a complaint.\n\n"
            "Fixing what is there is the right answer more often than people expect. If the business rules work and the trouble is a "
            "clumsy screen or a slow report, that is a smaller job with value in weeks.\n\n"
            "Rebuild when nobody can safely change it any more, when the platform is out of support and creating real risk, "
            "or when the business has moved so far that the rules themselves are wrong.\n\n"
            "If you do rebuild, budget for double the surprises you expect. That is not pessimism, it is what the forgotten rules cost.\n\n"
            "#LegacySystems #SoftwareDevelopment #TechnologyStrategy"
        ),
        "facebook": (
            "Every old system eventually raises the same question: fix it, or start again.\n\n"
            "Rewriting feels cleaner and is usually slower than it looks, because the old system holds years of rules nobody wrote down. "
            "You rediscover them one complaint at a time.\n\n"
            "Rebuild when nobody can safely change it, or the platform is out of support. Otherwise, fixing what is there often wins."
        ),
    },
    {
        "date": "2026-09-08", "slug": "what-good-handover-looks-like",
        "spec": {
            "eyebrow": "Handover", "layout": "checklist", "seed": 48,
            "title": "What a proper handover looks like",
            "standfirst": "Test it by asking: could we carry on without them next week?",
            "items": [
                {"label": "Every login is in your name", "detail": "And you have logged in yourself at least once."},
                {"label": "Someone in-house has been shown", "detail": "Not sent a document. Actually shown."},
                {"label": "The monthly costs are listed", "detail": "With the renewal dates."},
                {"label": "There is a written way to raise a problem", "detail": "And you have used it once while they are still around."},
            ],
        },
        "linkedin": (
            "A useful test at the end of any project: if the supplier disappeared next week, could you carry on.\n\n"
            "That is what a handover is for, and it is more than a folder of documents.\n\n"
            "Every login should be in your business's name, and you should have logged in yourself at least once, because "
            "\"you have the credentials\" and \"the credentials work\" are different claims. Someone in-house should have been shown how it runs, "
            "not just sent a document. The monthly costs and renewal dates should be written down. And there should be a way to raise a problem "
            "that you have used once while the relationship is still warm.\n\n"
            "We would rather be replaceable. It tends to be why people stay.\n\n"
            "#Handover #ITSupport #BusinessContinuity"
        ),
        "facebook": (
            "A good test at the end of any project: if the supplier disappeared next week, could you carry on?\n\n"
            "Logins in your name, and you have used them. Someone in-house actually shown, not just sent a document. Monthly costs and renewal dates written down. "
            "A way to raise a problem that you have tried once already.\n\n"
            "We would rather be replaceable. It tends to be why people stay."
        ),
    },
    {
        "date": "2026-09-09", "slug": "saying-no-to-a-feature",
        "spec": {
            "eyebrow": "Scope", "layout": "steps", "seed": 49,
            "title": "When the right answer is no, not yet",
            "items": [
                {"label": "One person asked for it", "detail": "And they asked once, in passing."},
                {"label": "It describes a screen, not a problem", "detail": "Ask what they were trying to do when they thought of it."},
                {"label": "It duplicates something that exists", "detail": "Usually because nobody knew the first one was there."},
                {"label": "It only helps the exception", "detail": "Build for the ninety, handle the ten by hand."},
            ],
        },
        "linkedin": (
            "Saying no to a feature request is part of the job, and it is usually kinder than the alternative.\n\n"
            "Four signals that the answer is no, or at least not yet.\n\n"
            "One person asked, once, in passing. Real needs come back.\n\n"
            "The request describes a screen rather than a problem. Ask what they were trying to do when they thought of it, "
            "and you often find a simpler answer that already exists.\n\n"
            "It duplicates something the system already does, which normally means the first version was never explained properly. "
            "That is a training problem wearing a development costume.\n\n"
            "It only helps the exception. If ninety cases work one way and ten do not, build for the ninety and handle the ten by hand. "
            "Automating the exception is where systems become impossible to change.\n\n"
            "#ProductThinking #SoftwareDevelopment #Consulting"
        ),
        "facebook": (
            "Saying no to a feature request is part of the job, and it is usually kinder than the alternative.\n\n"
            "One person asked once in passing. It describes a screen instead of a problem. It duplicates something that already exists. "
            "Or it only helps the exception.\n\n"
            "If ninety cases work one way and ten do not, build for the ninety. Automating the exception is where systems become impossible to change."
        ),
    },
    {
        "date": "2026-09-10", "slug": "check-a-quote",
        "spec": {
            "eyebrow": "Reading a quote", "layout": "checklist", "seed": 50,
            "title": "Five things to check in a software quote",
            "standfirst": "The total is the least interesting number on the page.",
            "items": [
                {"label": "What is excluded", "detail": "The exclusions tell you more than the inclusions."},
                {"label": "The monthly figure", "detail": "Separate from the build price, for the next three years."},
                {"label": "Who does the data migration", "detail": "And whether cleaning it is included."},
                {"label": "What happens after go-live", "detail": "Support, for how long, at what cost."},
                {"label": "The assumptions", "detail": "Every quote rests on some. Ask for them in writing."},
            ],
        },
        "linkedin": (
            "The total is the least interesting number on a software quote.\n\n"
            "Five things worth more of your attention. What is excluded, because the exclusions describe the project more honestly than "
            "the inclusions do. The monthly running figure, separately from the build. Who is doing the data migration and whether cleaning "
            "the data is part of it, since that is where most overruns actually start. What happens after go-live, for how long and at what cost. "
            "And the assumptions the price rests on, in writing.\n\n"
            "A quote with clear exclusions and stated assumptions from a supplier who has thought it through beats a lower number with neither. "
            "The second one is not cheaper, it is just less specific about when it will cost more.\n\n"
            "#Procurement #SoftwareDevelopment #BusinessAdvice"
        ),
        "facebook": (
            "The total is the least interesting number on a software quote.\n\n"
            "Check what is excluded. Check the monthly figure, separately from the build. Check who cleans the data. Check what support looks like "
            "after go-live. And ask for the assumptions in writing.\n\n"
            "A lower number with none of that is not cheaper. It is just less specific about when it will cost more."
        ),
    },
    {
        "date": "2026-09-11", "slug": "one-system-or-five-tools",
        "spec": {
            "eyebrow": "Tooling", "layout": "compare", "seed": 51,
            "title": "One system, or five tools that nearly talk to each other",
            "standfirst": "Both are real choices. The failure is drifting into the second one.",
            "left": {"heading": "Five tools", "points": [
                "Each one is good at its job", "Cheap to start, easy to add",
                "Somebody reconciles them by hand", "Nobody owns the whole picture"]},
            "right": {"heading": "One system", "points": [
                "Fewer places for the truth to differ", "One login, one report",
                "Costs more upfront", "Needs someone to own it"]},
        },
        "linkedin": (
            "Most businesses do not choose five disconnected tools. They arrive at them, one sensible decision at a time.\n\n"
            "Each tool was the right call on its own. The accounting package, the scheduling app, the shared drive, the spreadsheet that "
            "somehow became the master list. Nobody decided the business should run on five systems that nearly talk to each other.\n\n"
            "The cost is easy to miss because it is paid in small amounts by whoever reconciles them at month end.\n\n"
            "Neither answer is universally right. Five good tools with one honest connection between them beats one mediocre system that "
            "does everything badly. But if nobody owns the whole picture, you are not choosing, you are drifting, and drifting gets expensive quietly.\n\n"
            "#Operations #BusinessSystems #Integration"
        ),
        "facebook": (
            "Nobody chooses to run their business on five disconnected tools. You arrive there, one sensible decision at a time.\n\n"
            "Each one was the right call on its own. The cost shows up in whoever reconciles them at month end.\n\n"
            "Five good tools with one honest connection can beat one mediocre system. But if nobody owns the whole picture, you are not choosing, you are drifting."
        ),
    },
    {
        "date": "2026-09-12", "slug": "manual-to-automated",
        "spec": {
            "eyebrow": "Sequence", "layout": "flow", "seed": 52,
            "title": "From manual to automated, in the order that actually works",
            "items": [
                {"label": "Write it down", "detail": "The real process, workarounds included."},
                {"label": "Delete what should not exist", "detail": "Usually a third of the steps."},
                {"label": "Standardise what is left", "detail": "One way of doing it, agreed by the people doing it."},
                {"label": "Then automate", "detail": "Now there is something worth automating."},
            ],
        },
        "linkedin": (
            "The order matters more than the tools.\n\n"
            "Write the process down as it actually runs, workarounds and all. Delete the steps that should not exist, which is often "
            "close to a third of them, and costs nothing. Standardise what is left so there is one agreed way of doing it, "
            "agreed by the people who do it rather than announced to them. Then automate.\n\n"
            "Most automation disappointment comes from starting at step four. You end up with software that faithfully reproduces "
            "a bad process, faster, and now it is much harder to change because it is written in code.\n\n"
            "The first three steps need no budget and no supplier. They are also where most of the improvement is.\n\n"
            "#Automation #ProcessImprovement #Operations"
        ),
        "facebook": (
            "The order matters more than the tools.\n\n"
            "Write the process down as it really runs. Delete the steps that should not exist, usually about a third. "
            "Agree one way of doing what is left. Then automate.\n\n"
            "Most automation disappointment comes from starting at the last step, and ending up with a bad process running faster."
        ),
    },
    {
        "date": "2026-09-13", "slug": "where-operations-time-goes",
        "spec": {
            "eyebrow": "Time", "layout": "steps", "seed": 53,
            "title": "Where operations time actually goes",
            "standfirst": "Rarely the work itself. Usually everything around it.",
            "items": [
                {"label": "Looking for information", "detail": "Which file, which version, who sent it."},
                {"label": "Retyping it somewhere else", "detail": "The same numbers, a second and third time."},
                {"label": "Checking whether something happened", "detail": "Chasing rather than doing."},
                {"label": "Fixing what went wrong quietly", "detail": "Work nobody planned and nobody counts."},
            ],
        },
        "linkedin": (
            "When people say they are busy, they usually are. What they are busy with is often not the work.\n\n"
            "Four things quietly take the day. Looking for information, which file and which version and who sent it. Retyping the same "
            "numbers into a second system. Checking whether something happened, which is chasing rather than doing. And fixing things that "
            "went wrong without anyone noticing until later.\n\n"
            "None of that appears on a job description. None of it gets counted, so none of it gets managed, and it is usually the "
            "largest single cost in an operations team.\n\n"
            "You can measure it in a week without any software. Ask people to mark which of those four a task belonged to. "
            "The pattern is normally obvious by Wednesday.\n\n"
            "#Operations #Productivity #BusinessEfficiency"
        ),
        "facebook": (
            "When people say they are busy, they usually are. What they are busy with is often not the work.\n\n"
            "Looking for information. Retyping the same numbers somewhere else. Checking whether something happened. "
            "Fixing what went wrong quietly.\n\n"
            "None of it is on anyone's job description, so none of it gets counted. It is usually the biggest cost in an operations team."
        ),
    },
    {
        "date": "2026-09-14", "slug": "before-you-hire-a-developer",
        "spec": {
            "eyebrow": "Hiring", "layout": "checklist", "seed": 54,
            "title": "Before you hire your first developer",
            "standfirst": "Five things to have ready, or the first six months go slowly.",
            "items": [
                {"label": "Know who reviews their work", "detail": "A developer with nobody to check the work is a risk to themselves."},
                {"label": "Decide what they own", "detail": "Building new, or keeping the existing running. Rarely both well."},
                {"label": "Have somewhere to put the code", "detail": "In the company's account, from day one."},
                {"label": "Agree what done means", "detail": "Tested, documented, deployed. Write it once."},
                {"label": "Plan for the bus", "detail": "One developer is a single point of failure. Say so out loud."},
            ],
        },
        "linkedin": (
            "Hiring your first developer changes what your business has to be good at, and most of that has nothing to do with code.\n\n"
            "Five things worth having ready. Someone who can review the work, because a developer with nobody checking is a risk to "
            "themselves as much as to you. A clear decision on whether they are building new things or keeping existing ones running, "
            "since very few people do both well at once. A repository in the company's account from day one, not a personal one. "
            "An agreed meaning for \"done\", written once. And an honest acknowledgement that one developer is a single point of failure.\n\n"
            "That last one is not a reason to avoid hiring. It is a reason to write things down from the first week rather than the day they resign.\n\n"
            "#Hiring #SoftwareDevelopment #SmallBusiness"
        ),
        "facebook": (
            "Hiring your first developer changes what your business has to be good at, and most of it is not about code.\n\n"
            "Who reviews the work. Whether they are building new things or keeping existing ones running. A repository in the company's account from day one. "
            "An agreed meaning for done. And an honest acknowledgement that one developer is a single point of failure.\n\n"
            "Write things down from week one, not the day they resign."
        ),
    },
    {
        "date": "2026-09-15", "slug": "report-someone-acts-on",
        "spec": {
            "eyebrow": "Reporting", "layout": "compare", "seed": 55,
            "title": "A report someone acts on, or one nobody opens",
            "standfirst": "The difference is not the chart. It is whether it asks for a decision.",
            "left": {"heading": "Nobody opens it", "points": [
                "Shows everything measurable", "Arrives on a schedule nobody chose",
                "No owner, no threshold", "Looks impressive in a meeting"]},
            "right": {"heading": "Someone acts on it", "points": [
                "Answers one question", "Goes to a named person",
                "Says what counts as too high", "Arrives when a decision is due"]},
        },
        "linkedin": (
            "The difference between a report someone acts on and one nobody opens is not the chart. It is whether it asks for a decision.\n\n"
            "Reports that get ignored tend to show everything measurable, arrive on a schedule nobody chose, and have no owner. "
            "They look impressive in a meeting and change nothing afterwards.\n\n"
            "Reports that get used answer one question, go to a named person, and say what counts as too high or too low, "
            "so the reader knows immediately whether to do anything. They arrive when a decision is actually due, "
            "which is often not the first of the month.\n\n"
            "If you have a report nobody opens, do not redesign it. Ask who it was for and what they were meant to do about it. "
            "Sometimes the honest answer is to stop sending it.\n\n"
            "#Reporting #Dashboards #BusinessIntelligence"
        ),
        "facebook": (
            "The difference between a report people act on and one nobody opens is not the chart. It is whether it asks for a decision.\n\n"
            "Answer one question. Send it to a named person. Say what counts as too high. Send it when a decision is actually due.\n\n"
            "If you have a report nobody opens, do not redesign it. Ask who it was for and what they were meant to do about it."
        ),
    },
]
