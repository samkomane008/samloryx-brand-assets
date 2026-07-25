#!/usr/bin/env python3
"""Generate the campaign-2 card set (26 Jul to 23 Aug) into the brand-assets repo."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_card import build

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "brandassets", "social", "campaign2")

CARDS = [
    ("2026-07-26-insights-live", "We write up the work we actually do.",
     "New Insights section, live on samloryxconsultancy.co.za"),
    ("2026-07-27-popia", "Where does your customer data physically live?",
     "POPIA starts with a question most businesses cannot answer in one sentence."),
    ("2026-07-28-api-promise", "An API is a promise.",
     "Most integration failures are broken promises, not broken code."),
    ("2026-07-29-dont-build", "Sometimes the answer is: don't build that.",
     "The most useful assessment finding is the one that saves the spend."),
    ("2026-07-30-boring-first", "Automate the boring work first.",
     "Predictable work is safe to automate. Start there, not with the moonshot."),
    ("2026-07-31-first-two-weeks", "The expensive mistakes happen in the first two weeks.",
     "Not during development. Before anyone has agreed on the problem."),
    ("2026-08-01-ds-attorneys", "DS Attorneys, Pretoria.",
     "Own domain, HTTPS enforced, email intact through the move, WhatsApp in one tap."),
    ("2026-08-02-report-by-hand", "Which report does someone still build by hand?",
     "Most businesses have at least one. Some have four."),
    ("2026-08-03-month-end", "A four-day month-end close is a report.",
     "It tells you the same numbers live in two places."),
    ("2026-08-04-definitions", "Not a data problem. A definitions problem.",
     "Sales, finance and support each count a customer differently."),
    ("2026-08-05-dashboards", "Most dashboards get opened twice.",
     "Once at launch. Once after something has already gone wrong."),
    ("2026-08-06-legacy", "An old system that works is not technical debt.",
     "It is a paid-off asset. Ask whether it still lets the business change."),
    ("2026-08-07-roadmap-sprint", "What a Roadmap Sprint actually gives you.",
     "A ranked list, an effort estimate, and an honest leave-this-alone."),
    ("2026-08-08-zenit", "Zenit Global Interlink, Centurion.",
     "Website, domain, branded email and quote forms that deliver. Handed over outright."),
    ("2026-08-09-womens-day", "9 August 1956.",
     "20,000 women marched to the Union Buildings. Women's Day."),
    ("2026-08-10-manually-for-now", "We'll just do it manually for now.",
     "The tell is when the temporary process gets a name."),
    ("2026-08-11-security", "Most incidents start with an account nobody closed.",
     "MFA, offboarding, tested backups, and one person accountable."),
    ("2026-08-12-cloud-bill", "Cloud bills grow from forty small decisions.",
     "Tag by project. Review the top three lines every month."),
    ("2026-08-13-buy-build", "Buy the commodity. Build the difference.",
     "Payroll is not how you compete."),
    ("2026-08-14-scoping", "Five questions before we connect two systems.",
     "If a vendor needs six weeks to answer them, you are paying for their process."),
    ("2026-08-15-ownership", "The client owns everything from day one.",
     "Domain, mailboxes, code. It costs us leverage, and that is the point."),
    ("2026-08-16-regret", "Which software decision do you regret most?",
     "The feature nobody used. The one that was cheap until year two."),
    ("2026-08-17-handover", "Five things to own before you pay the final invoice.",
     "Domain, DNS, code, mailboxes, and what it all costs monthly."),
    ("2026-08-18-one-head", "If it lives in one person's head, it is not a process.",
     "It is a risk with a salary attached."),
    ("2026-08-19-whatsapp", "WhatsApp is a business channel. Run it like one.",
     "A company number, a record of what was agreed, and honest hours."),
    ("2026-08-20-ai-wrong", "What happens when it is confidently wrong?",
     "That is the AI design question, not whether it can do the task."),
    ("2026-08-21-fixed-price", "Fixed price on the first job.",
     "An hourly rate makes the uncertainty your problem."),
    ("2026-08-22-one-week", "One week. A note on a phone.",
     "The cheapest technology audit your business can run."),
    ("2026-08-23-hand-one-task", "Hand one task to a system tomorrow. Which one?",
     "Not the strategic one. The small, annoying, recurring one."),
]

os.makedirs(OUT, exist_ok=True)
for slug, head, sub in CARDS:
    build(head, sub, os.path.join(OUT, f"{slug}.png"), "wide")
print(f"\n{len(CARDS)} cards written to {OUT}")
