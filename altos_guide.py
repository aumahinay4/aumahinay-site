"""ALTOS Demo Guide: /tools/altos-demo-guide/ (drafted 2026-11-24, Butch said yes to drafting; held until his go).

A written, indexable page that explains each screen of the ALTOS demo (/tools/altos-demo/) in plain words, with
screenshots from the demo. It uses the normal site layout, so once AdSense approves the site, ads can appear HERE,
beside the demo, while the demo screens themselves stay ad-free and noindex.

Rules (project memory): ALTOS is for all Philippine local treasuries, never "built for" a named LGU; ALTOS is only
tested on the developer side, never claim it is used in actual treasury work; say "local governments", not "towns";
no "coming soon" or schedule lines; no Sources section (Butch, for AdSense). Deeper topics are left to the posts and
study notes, linked only while they are live, so this page does not repeat them.
Screenshots: static/altos-guide/*.jpg, taken from the demo with its made-up data (Sample Municipality).
"""

import tags as t
from altos_demo import DEMO_URL

GUIDE_URL = "/tools/altos-demo-guide/"
GUIDE_TITLE = "ALTOS Demo Guide"
GUIDE_DESCRIPTION = ("A plain-language guide to the ALTOS demo, screen by screen: official receipts (AF 51 and AF 56), "
                     "the RCD, the RAAF, deposits, the Cash Book, checks and the Activity Log of a Philippine local treasury.")

# (file, width, height) of each screenshot in static/altos-guide/
SHOTS = {
    "signin": (1536, 1020), "col-issue": (1536, 1020), "receipt": (780, 555), "col-rptcalc": (1536, 1020),
    "col-rcd": (1536, 1020), "col-raaf": (1536, 1020), "lo-refused": (1536, 1020), "lo-crcd": (1536, 1020),
    "lo-cashbook": (1536, 1020), "do-prepare": (1536, 1020), "do-checks": (1536, 1020),
    "sys-dashboard": (1536, 1020), "sys-log": (1536, 1020),
}


def _shot(name, alt, caption, small=False):
    from pages import asset_url  # imported here: pages.py imports this module
    w, h = SHOTS[name]
    return t.figure(
        t.img(src=asset_url(f"altos-guide/{name}.jpg"), alt=alt, width=str(w), height=str(h), loading="lazy"),
        t.figcaption(caption),
        class_="screenshot guide-shot" + (" small" if small else ""),
    )


def _try(screen, label):
    """'Try it' link straight to one screen of the demo."""
    return t.p(t.a(label + " →", href=f"{DEMO_URL}#{screen}"), class_="guide-try")


def _read_more(*links):
    """A 'Read more' line with only the posts and study notes that are live today (never a link to a hidden page)."""
    from pages import post_is_live, note_is_live
    from notes import NOTES, note_url
    live_notes = {note_url(n) for n in NOTES if note_is_live(n)}
    keep = [(label, url) for label, url in links
            if (url.startswith("/blog/") and post_is_live(url)) or url in live_notes]
    if not keep:
        return None
    out = [t.b("Read more: ")]
    for i, (label, url) in enumerate(keep):
        out += [", " if i else "", t.a(label, href=url)]
    out.append(".")
    return t.p(*out, class_="guide-more")


def guide_page():
    return {
        "title": GUIDE_TITLE, "active": GUIDE_URL, "url": GUIDE_URL, "og_type": "article",
        "seo_title": "ALTOS Demo Guide: A Local Treasury Day, Screen by Screen · Butch Mahinay",
        "description": GUIDE_DESCRIPTION,
        "body": [t.div(
            t.p("Free tools", class_="eyebrow"),
            t.h1("ALTOS Demo Guide: One Day in a Local Treasury, Screen by Screen"),
            t.p("The ALTOS demo lets you click through a working day in a Philippine local treasury: a receipt is "
                "issued, the day is closed, the money is counted and deposited, a check is written and released, and "
                "every step is logged. This guide explains what you see on each screen, in plain words, so that the "
                "forms and terms make sense even if you have never worked in a treasury.", class_="lead"),
            t.p(t.a("Open the ALTOS demo →", href=DEMO_URL, class_="btn primary")),
            t.div(
                t.p(t.b("A quick note before you start. "),
                    "Everything in the demo is made up: a sample municipality, sample officers, sample taxpayers and "
                    "sample amounts. It runs only in your browser, nothing you type is sent anywhere, and reloading "
                    "the page starts it fresh. The receipts and reports it shows are marked as samples and are not "
                    "valid documents. ALTOS itself has been tested only on the developer side; the demo shows how it "
                    "works, not an office that uses it."),
                class_="guide-note",
            ),

            t.h2("What ALTOS is"),
            t.p("ALTOS stands for Automated Local Treasury Operations System. It is software I designed for "
                "Philippine local treasuries, the offices of provinces, cities and municipalities that collect "
                "taxes and fees and pay the local government's bills. Its three movements are written on its sign-in "
                "page: Collect, Disburse, Report. Each screen in ALTOS starts from a paper form that treasury staff "
                "already know, from the Local Treasury Operations Manual (LTOM) of the Bureau of Local Government "
                "Finance and the rules of the Commission on Audit, so the screen and the paper tell the same story."),
            _read_more(("Why I Built ALTOS", "/blog/why-i-built-altos/")),

            t.h2("The four officers you can sign in as"),
            t.p("In a real office, each officer signs in with a username and password. In the demo you simply pick "
                "a role. Each role has its own page color and its own side menu, because each officer may only do "
                "the work assigned to them:"),
            t.ul(
                t.li(t.b("Collecting Officer (blue). "), "Issues official receipts at the window, closes the day "
                     "and turns the money over."),
                t.li(t.b("Liquidating Officer (green). "), "Receives the money and reports from the collecting "
                     "officers, counts the cash and deposits it in the bank."),
                t.li(t.b("Disbursing Officer (red). "), "Writes the checks that pay the local government's bills "
                     "and releases them to the payees."),
                t.li(t.b("System Administrator (violet). "), "Watches over the whole system: the dashboard, the "
                     "registers and the Activity Log."),
            ),
            t.p("Splitting the work this way is deliberate. The person who receives a peso is not the one who "
                "deposits it, and the one who deposits it is not the one who spends it, so every hand checks the "
                "hand before it."),
            _shot("signin", "The ALTOS demo sign-in page: the ALTOS logo on a blue panel, and a welcome card with a "
                  "Start the guided tour button and the four working pages.",
                  "The sign-in page. Start the guided tour, or tap one of the four working pages."),
            _read_more(("Principle 6: Separate the Hands", "/blog/altos-framework-separate-the-hands/")),

            t.h2("Step 1. Issue an official receipt"),
            t.p("Money paid at the treasury window begins with an official receipt, or OR. The demo has two kinds "
                "of receipt:"),
            t.ul(
                t.li(t.b("AF 51 (Accountable Form No. 51). "), "The general receipt, for business taxes, permit fees, "
                     "market rentals, certifications and other taxes, fees and charges."),
                t.li(t.b("AF 56 (Accountable Form No. 56). "), "The receipt for real property tax, the amilyar. It "
                     "names the property and shows the basic tax and the Special Education Fund (SEF) tax on "
                     "separate lines."),
            ),
            t.p("They are called accountable forms because each one carries a printed serial number, and the officer "
                "must account for every number, used or not. That is why the demo fills in the next OR number for "
                "you: receipts are issued strictly in serial order. You type the payor's name, choose the Nature of "
                "Payment, and the amount fills in from the local revenue code schedule. A tax with no fixed amount, "
                "such as a business tax, is typed in. Tap Issue OR and the receipt is recorded."),
            _shot("col-issue", "The Issue Official Receipt screen with tabs for AF 51 and AF 56, the next OR number, "
                  "the date, the payor's name, a Mayor's Permit Fee of 500 pesos and a total.",
                  "Issue Official Receipt, on the Collecting Officer page."),
            _shot("receipt", "A sample official receipt, Accountable Form No. 51, number 1234504, for a Mayor's Permit "
                  "Fee of 500 pesos, stamped SAMPLE ONLY, NOT VALID.",
                  "The receipt you just issued, under My Collections. It is stamped as a sample.", small=True),
            _try("col-issue", "Issue a receipt in the demo"),

            t.h2("Step 2. Check a property's tax with the RPT Tax Calculator"),
            t.p("When an owner comes to pay real property tax, the collecting officer first needs the amount due. "
                "On the RPT Tax Calculator screen you pick the property by its PIN (Property Index Number), and the "
                "demo shows the owner, the assessed value and the tax for each unpaid quarter. The tax is the basic "
                "tax plus the SEF tax, each a percentage of the assessed value: the Local Government Code allows a "
                "basic rate of up to 1 percent in a province and up to 2 percent in a city or a municipality in "
                "Metro Manila, plus 1 percent for the SEF."),
            t.p("Change the date of payment and watch the amount move. A quarter paid on time may earn the discount "
                "set by the local ordinance, while a late quarter adds interest of 2 percent a month, up to 36 months, "
                "as Section 255 of the Code provides. The owner then pays on an AF 56, the second tab of the Issue Official Receipt screen in Step 1."),
            _shot("col-rptcalc", "The RPT Tax Calculator: a property chosen by PIN, a date of payment, the assessed "
                  "value, and a table of quarters with the tax, the interest for a late quarter and the amount to pay.",
                  "The RPT Tax Calculator. The third quarter here is two months late, so 4 percent interest is added."),
            _try("col-rptcalc", "Try the RPT Tax Calculator"),
            _read_more(("How to Use the RPT Calculator", "/blog/how-to-use-the-rpt-calculator/"),
                       ("Paying real property tax: quarters, discounts and interest", "/study-notes/paying-real-property-tax/")),

            t.h2("Step 3. Close the day with the RCD"),
            t.p("At the end of the day, the collecting officer lists every receipt issued and hands over the money. "
                "The list is the Report of Collections and Deposits, or RCD. In the demo, My RCD gathers all your "
                "receipts that are not yet reported and makes one RCD for each bank account, because money for the "
                "General Fund and money for the Special Education Fund must never be mixed."),
            t.p("Scroll down to see the whole report, laid out like the printed form: the receipts by serial number, "
                "the accountability for accountable forms (which receipt numbers you started with, used and still "
                "hold), and the summary of collections and remittances. Tap Close the day and remit, and the RCD "
                "goes to the Liquidating Officer."),
            _shot("col-rcd", "The My RCD screen: a note that the unreported receipts make two RCDs, one per bank "
                  "account, and a sample Report of Collections and Deposits for the General Fund.",
                  "My RCD. One report for each bank account, in the layout of the printed form."),
            _try("col-rcd", "Close the day in the demo"),

            t.h2("Step 4. Report the receipt booklets with the RAAF"),
            t.p("Money is not the only thing a collecting officer answers for. Blank receipts are, too, since a "
                "missing booklet could be used to collect money that never reaches the treasury. Once a month, each "
                "officer prepares the Report of Accountability for Accountable Forms, or RAAF. It shows, for each "
                "kind of receipt, the serial numbers on hand at the start of the month, those received, those "
                "issued, and those left at the end."),
            t.p("In the demo, My RAAF fills itself in from the receipts you issued, and the Liquidating Officer's "
                "RAAF & CRAAF screen gathers every officer's RAAF into one consolidated report, the CRAAF. Both "
                "screens show the due date, and the CRAAF shows which officers have not yet handed theirs in."),
            _shot("col-raaf", "The My RAAF screen: a note on when the report is due and a sample Report of "
                  "Accountability for Accountable Forms in landscape layout.",
                  "My RAAF. The ending balance of receipts must match the serial numbers still in your hands."),
            _try("col-raaf", "See the RAAF in the demo"),

            t.h2("Step 5. Refuse a short remittance"),
            t.p("Now switch to the Liquidating Officer. One collecting officer in the demo, Luz Ramos, handed in "
                "₱50.00 less than her RCD says. ALTOS does not let the Liquidating Officer quietly accept the "
                "difference or fix the figure. Instead, the report is refused with a written reason and sent back "
                "to the collecting officer to correct. The refusal stays on record, so the shortage "
                "cannot simply disappear."),
            _shot("lo-refused", "The Refused Reports screen: RCD 2026-11-042 of Luz Ramos chosen, with the reason "
                  "Short by 50 pesos, and a Refuse this report button.",
                  "Refused Reports, on the Liquidating Officer page."),
            _try("lo-refused", "Refuse the short report in the demo"),

            t.h2("Step 6. Count the money and deposit it"),
            t.p("The Consolidated RCD screen is where the money from all the collecting officers comes together. "
                "The Liquidating Officer ticks the RCDs received for one bank account, counts the cash by "
                "denomination (how many ₱1,000 bills, how many ₱500 bills, and so on), and records the deposit "
                "slip. ALTOS will not accept the deposit until the count matches the reports to the last centavo."),
            _shot("lo-crcd", "The Consolidated RCD screen: tabs for the General Fund and the Special Education Fund, "
                  "a list of RCDs to tick, and a cash count by denomination from 1,000 pesos to 25 centavos.",
                  "Consolidated RCD. Tick the reports, count the money, then record the deposit."),
            _try("lo-crcd", "Count and deposit in the demo"),
            _read_more(("Collection and deposit", "/study-notes/collection-and-deposit/"),
                       ("From the Cash Box to the Bank", "/blog/deposits-cash-box-to-bank/")),

            t.h2("Step 7. Watch the deposit reach the Cash Book"),
            t.p("The Cash Book is the running record of money in the bank, one for each fund. A deposit is written "
                "under Debit, because money comes in; a check is written under Credit, because money goes out; and "
                "the Balance column keeps a running total after every line. After Step 6, your deposit is the newest "
                "line. The Collecting Officer and the Liquidating Officer also each have a My Cash Book, which shows "
                "the cash still in their own hands, called the balance on hand."),
            _shot("lo-cashbook", "The Cash Book of the General Fund: date, particulars, and Cash in Bank columns for "
                  "Debit, Credit and Balance, with deposits of collections and checks to suppliers.",
                  "The Cash Book. Deposits under Debit, checks under Credit, and the balance after each line."),
            _try("lo-cashbook", "Open the Cash Book in the demo"),

            t.h2("Step 8. Write a check"),
            t.p("Now sign in as the Disbursing Officer. On Prepare Check you choose the bank account, type the payee, "
                "what the payment is for, and the amount. The check number comes next in serial order from the check "
                "booklet, and each check carries the number of its disbursement voucher (DV), the approved document "
                "that allows the payment in the first place."),
            t.p("Try typing an amount larger than the Cash Book balance. ALTOS refuses it, because a check must never "
                "be written for money the account does not have."),
            _shot("do-prepare", "The Prepare Check screen: bank account, Cash Book balance, next check number, DV "
                  "number, payee, particulars and amount.",
                  "Prepare Check, on the Disbursing Officer page. The Cash Book balance is shown beside the account."),
            _try("do-prepare", "Write a check in the demo"),
            _read_more(("Disbursements: vouchers, checks and cash advances",
                        "/study-notes/disbursements-vouchers-checks-cash-advances/"),
                       ("From Budget to Check", "/blog/from-budget-to-check/")),

            t.h2("Step 9. Release the check"),
            t.p("A prepared check is not yet in the payee's hands. Check Issuance lists every check with its status. "
                "When the payee comes to receive it, tap Release, and the check changes from Prepared to Released, "
                "with the name of the person who received it."),
            _shot("do-checks", "The Check Issuance screen: a table of checks with number, date, account, payee, "
                  "amount and status, one marked Prepared with a Release button and the rest Released.",
                  "Check Issuance. One check is still waiting to be released."),
            _try("do-checks", "Release a check in the demo"),

            t.h2("Step 10. See the whole picture as System Administrator"),
            t.p("The System Administrator's Collections Dashboard sums up the collections of the day and of the year: "
                "by month, by source and by collecting officer. Every chart comes with a table, and all the figures "
                "come from the same receipts you issued earlier, so the dashboard cannot say something the records do "
                "not."),
            _shot("sys-dashboard", "The Collections Dashboard: tiles for collections today, this month, year to date "
                  "and waiting for deposit, and a bar chart of collections by month.",
                  "The Collections Dashboard. The figures come straight from the receipts."),
            t.p("Finally, open the Activity Log. Every action in the demo is there: who did it, as which officer, and "
                "when, including any receipt, refusal, deposit or check you made a few minutes ago. In "
                "ALTOS this log is sealed. No one can change or delete an entry, not even the System Administrator."),
            _shot("sys-log", "The Activity Log: a table of time, user and action, showing sign-ins and an issued "
                  "official receipt.",
                  "The Activity Log. What you do in the demo appears here, too."),
            _try("sys-log", "Read the Activity Log in the demo"),
            _read_more(("Principle 5: Every Record Has a Seal", "/blog/altos-framework-every-record-has-a-seal/")),

            t.h2("Questions people ask about the demo"),
            t.h3("Is any of this real?"),
            t.p("No. The local government, the officers, the taxpayers, the properties and every amount are made up. "
                "The receipts and reports are stamped as samples and are not valid documents."),
            t.h3("Is anything I type saved?"),
            t.p("No. The demo runs only in your browser, with no server and no database behind it. Reload the page "
                "and it starts fresh."),
            t.h3("Does the demo show all of ALTOS?"),
            t.p("No. It copies the look and the main steps of ALTOS, but each role shows only part of its menu. "
                "The demo is written separately from the real ALTOS code."),
            t.h3("Can my office use ALTOS?"),
            t.p("ALTOS has been tested only on the developer side. Using it in actual treasury work would first need "
                "the proper agreements and approvals, so the demo is for learning and for showing how the system "
                "works."),
            t.h3("Does it work on a phone?"),
            t.p("Yes. On a phone, the side menu becomes a row of tabs that you can swipe sideways, and wide tables "
                "turn into small cards."),
            t.p(t.a("Open the ALTOS demo →", href=DEMO_URL, class_="btn primary")),
            class_="guide",
        )],
    }
