"""Data Analytics blog series (Butch 2026-11-13 PH): Part 1 live Nov 13, 2026 (Butch: "post this first part today"),
then one part every few days at 9 pm PH ("YYYY-MM-DD 21:00") in the daily blog rotation (Butch 2026-11-14).

The series teaches the whole craft in plain words, from asking a good question to acting on the answer,
with examples from local treasury work. Every number, office and taxpayer in an example is made up.
The wording is the blog's own, not the course's or the ALTOS book's. Facts are checked privately
before each part is approved; per Butch, posts show no Sources section and no "coming next" teaser.
Newest first, like BLOG in content.py.
"""

SERIES = "Data Analytics Series"

DATA_POSTS = [
    {
        "date": "January 31, 2027",
        "title": "Data Analytics Series, Part 17: Samples and Margin of Error, Checking 400 Receipts Instead of 12,000",
        "slug": "data-analytics-part-17-samples-margin-of-error",
        "category": "data",
        "summary": "You do not always have to check every record to know how many are wrong. This part explains "
                   "random samples, the margin of error and how to choose a sample size, with a treasury "
                   "example worked out step by step and a plain way to report the result.",
        "publish_on": "2027-01-31 21:00",
        "body": [
            "After the cleanup in Part 16, the head of office asks a fair question: how many of last year’s "
            "12,000 receipts have a wrong barangay code in the system? Checking every receipt against its "
            "paper copy would take two staff members several weeks.",
            "The analyst suggests another way. Check 400 receipts chosen at random, count the errors, and "
            "use that count to estimate the rate for all 12,000, with an honest statement of how far off the "
            "estimate could be.",
            "The head of office is doubtful. “Four hundred out of twelve thousand? That is barely three "
            "percent.” It is a reasonable worry, and this post answers it.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town or taxpayer is described.)",
            "Part 13 showed how the way data is collected can tilt a result. This part shows how a small, "
            "well-chosen sample can describe a large group. By the end of this post you will know what makes "
            "a sample random, how to draw one in a spreadsheet, what a margin of error means, how to choose a "
            "sample size, and how to report the result so nobody reads more into it than it holds.",
            ("photo", "blog/data-sampling.jpg", "Sampling: a random sample, a margin of error, a sample size "
             "and a careful report. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Population and Sample"),
            ("point", "Population", "Every record you want to know about: here, all 12,000 receipts from last "
             "year."),
            ("point", "Sample", "The records you actually check: here, 400 of them."),
            ("point", "Estimate", "A number worked out from the sample, used as a stand-in for the true "
             "number in the population, which nobody knows until every record is checked."),
            "Checking every record is called a census. A census has no sampling error, but it costs the "
            "most time. A sample costs far less, and in exchange you accept a known amount of uncertainty.",
            ("quote", "A sample does not give the exact answer. It gives a close one, with its limits written beside it."),
            ("h", "What Makes a Sample Random"),
            "In a simple random sample, every record in the population has the same chance of being chosen. "
            "That is what lets the sample speak for the whole.",
            ("point", "Not the first 400", "The first 400 receipts of the year come from January, which may "
             "have different encoders, workloads or errors than other months."),
            ("point", "Not the easy 400", "Receipts from the counter nearest the records room are easier to "
             "pull, but they may not be typical. This is the sampling bias described in Part 13."),
            ("point", "Not hand-picked", "Choosing receipts that “look normal” quietly removes the unusual "
             "ones, which may be where the errors are."),
            ("h", "Drawing a Random Sample in a Spreadsheet"),
            ("point", "1. Start with the full list", "One row per receipt, as in Part 12: all 12,000."),
            ("point", "2. Add a random number", "In a new column, type =RAND() and copy it down. In both Google "
             "Sheets and Excel, RAND returns a random number between 0 and 1."),
            ("point", "3. Freeze it", "RAND gives new numbers every time the sheet recalculates. Copy the "
             "column and paste it back as values only, so the sample stays the same."),
            ("point", "4. Sort and take the top", "Sort the whole list by the random column and take the first "
             "400 rows. That is your sample."),
            ("point", "5. Save the list", "Keep the 400 receipt numbers in their own file, so anyone can check "
             "the same receipts later."),
            ("h", "The Result, and How Sure We Can Be"),
            "Two clerks check the 400 receipts against the paper copies and find 24 with a wrong barangay "
            "code. That is 24 ÷ 400 = 6%.",
            "But a different random 400 could have given 5% or 7%. The margin of error says how far the "
            "estimate is likely to be from the true rate. For a percentage from a simple random sample, "
            "the usual formula at 95% confidence is:",
            ("point", "Margin of error", "1.96 × √( p × (1 − p) ÷ n ), where p is the sample rate as a "
             "decimal and n is the sample size."),
            ("point", "Worked out", "p = 0.06 and n = 400. Then 0.06 × 0.94 ÷ 400 = 0.000141. Its square root "
             "is about 0.0119. Times 1.96 gives about 0.023, or 2.3 percentage points."),
            ("point", "The range", "6% minus 2.3 points is 3.7%; 6% plus 2.3 points is 8.3%. Applied to 12,000 "
             "receipts, that is roughly 440 to 1,000 receipts with a wrong code."),
            "The 1.96 comes from the normal curve and goes with 95% confidence. The meaning of “95% "
            "confidence” is easy to misread. It means that if the office drew many random samples the same "
            "way and built a range from each, about 95% of those ranges would contain the true rate. It does "
            "not promise that this particular range is correct.",
            ("h", "How Big Should the Sample Be?"),
            "The same formula can be turned around to find the sample size for a margin of error you choose. "
            "When you have no idea what the rate will be, the cautious choice is p = 0.5, which gives the "
            "largest sample:",
            ("point", "Sample size", "n = 0.25 × (1.96 ÷ E)², where E is the margin of error you want, as a "
             "decimal. Round up."),
            ("point", "E = 5 points", "0.25 × (1.96 ÷ 0.05)² = 384.16, so 385 records."),
            ("point", "E = 3 points", "0.25 × (1.96 ÷ 0.03)² = 1,067.1, so 1,068 records."),
            ("point", "E = 2 points", "0.25 × (1.96 ÷ 0.02)² = 2,401 records."),
            "Notice the pattern: cutting the margin of error in half takes about four times as many records. "
            "Precision gets expensive quickly, so decide how precise the answer needs to be before choosing "
            "the size.",
            ("h", "Does the Population Size Matter?"),
            "Less than you might expect. The formula above has no population size in it at all. For smaller "
            "populations, a finite population correction trims the sample a little: n ÷ (1 + (n − 1) ÷ N), "
            "where N is the population size.",
            ("point", "For 12,000 receipts", "385 ÷ (1 + 384 ÷ 12,000) is about 373.1, so 374 records instead "
             "of 385."),
            "That is why 400 out of 12,000 is not “barely three percent” in the way the head of office feared. "
            "What sets the precision is mainly the number of records checked, not the share of the population "
            "they make up.",
            ("h", "What the Margin of Error Does Not Cover"),
            "The margin of error measures only one thing: the chance difference between a random sample and "
            "the whole population. It does not cover other problems.",
            ("point", "A sample that is not random", "If the 400 were hand-picked, the formula still produces "
             "a number, but the number means little."),
            ("point", "Checking mistakes", "If a clerk misreads a paper receipt, that error is not in the "
             "margin."),
            ("point", "Missing records", "Receipts never entered into the system cannot be sampled from it."),
            ("point", "Very few errors found", "The formula is an approximation. When a sample turns up only a "
             "handful of errors, or none, ask someone with statistics training before reporting a margin."),
            ("h", "Reporting the Result"),
            ("point", "Say how the sample was drawn", "“A random sample of 400 of last year’s 12,000 receipts.”"),
            ("point", "Give the estimate and the range", "“About 6% had a wrong barangay code, with a margin "
             "of error of about 2.3 percentage points at 95% confidence, or roughly 440 to 1,000 receipts.”"),
            ("point", "Say what it does not cover", "“This does not include receipts that were never entered.”"),
            ("point", "Keep the list", "Attach or file the list of sampled receipt numbers."),
            ("h", "The Receipts Check, Decided"),
            "The head of office accepted the estimate. A rate between about 4% and 8% was high enough to "
            "justify fixing the codes, so the office used a mapping table from Part 16 to correct them, then "
            "drew a fresh random sample of 400 to check the fix. That second sample found 2 errors, and the "
            "analyst, following the rule above, reported the count plainly instead of a margin.",
            ("h", "Mistakes to Avoid"),
            ("point", "Sampling the easy records", "Use a random number to choose, not convenience."),
            ("point", "Judging size by percentage", "The number checked matters more than the share of the "
             "population."),
            ("point", "Reporting one number alone", "Give the range and the confidence level with it."),
            ("point", "Treating the margin as the whole story", "It covers chance, not bias or checking errors."),
            ("h", "Key Takeaways"),
            ("point", "Random means equal chance", "Every record must have the same chance of being chosen."),
            ("point", "Margin of error", "1.96 × √(p(1 − p) ÷ n) at 95% confidence, for a rate from a random "
             "sample."),
            ("point", "Size from precision", "About 385 records for ±5 points; four times as many to halve "
             "that."),
            ("point", "Report honestly", "Estimate, range, how the sample was drawn, and what it leaves out."),
            ("h", "Your Part 17 Exercise"),
            "Pick one list in your office that is too long to check in full, such as receipts, permits or "
            "notices.",
            ("point", "Choose a margin", "Decide how precise the answer needs to be, and work out the sample "
             "size."),
            ("point", "Draw the sample", "Use RAND, freeze it, sort, and take the top rows."),
            ("point", "Check and calculate", "Count the problems, work out the rate and its margin of error."),
            "Then write the result in one sentence that a head of office could read without help, with the "
            "range included.",
            ("cta", "Read: Data Analytics Series, Part 13", "/blog/data-analytics-part-13-bias-in-data/"),
            ("cta", "Read: Data Analytics Series, Part 16", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Business Intelligence Series, Part 17", "/blog/business-intelligence-part-17-who-sees-what/"),
            ("ask", "Which list in your office has never been checked because it seemed too long to check?"),
        ],
    },
    {
        "date": "January 26, 2027",
        "title": "Data Analytics Series, Part 16: Dirty Data, the Usual Suspects and How to Spot Them",
        "slug": "data-analytics-part-16-dirty-data",
        "category": "data",
        "summary": "A sheet can look tidy and still count one barangay as three. This part lines up the usual "
                   "suspects in treasury data, from duplicates and stray spaces to numbers stored as text and "
                   "impossible amounts, with a quick test to spot each one and a ten-minute scan to run "
                   "before any analysis.",
        "publish_on": "2027-01-26 21:00",
        "body": [
            "The head of office asks a simple question: how many business permits were renewed in each "
            "barangay this year? The analyst opens the permits sheet, which three encoders filled in, and "
            "makes a quick count by barangay.",
            "The town has 24 barangays. The count shows 31. “Poblacion,” “Pob.” and “Pob” each have their "
            "own line, and several other barangays are split the same way. A few renewals also appear twice. "
            "The totals are wrong before any analysis has started.",
            "The data is not fake, and the encoders were not careless. It is dirty: correct in spirit, but "
            "not yet fit to count.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town or taxpayer is described.)",
            "Part 15 was about keeping data files safe. This part looks inside the file. By the end of this "
            "post you will know the usual kinds of dirty data, a quick test to spot each one in a "
            "spreadsheet, the first safe step to fix it, and a short scan to run before you trust any total.",
            ("photo", "blog/data-dirty-data.jpg", "The usual suspects in dirty data: duplicates, inconsistent "
             "names, stray spaces and numbers stored as text. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "What Makes Data Dirty"),
            "Dirty data is data that is incomplete, incorrect or inconsistent in ways that can mislead an "
            "analysis. Google’s Data Analytics Certificate groups it into types such as duplicate, outdated, "
            "incomplete, incorrect and inconsistent data.",
            "In a treasury spreadsheet, those types show up as a handful of familiar problems. Each one below "
            "comes with a test you can run in Google Sheets or Excel, and a first step that does not destroy "
            "anything.",
            ("quote", "Clean data is not data with no problems. It is data whose problems you have found."),
            ("h", "Suspect 1: Duplicates"),
            "The same record entered twice. It happens when two encoders type the same batch, when an export "
            "is pasted twice, or when a corrected row is added without removing the old one.",
            ("point", "How to spot it", "Use the record’s key, such as the receipt number with its series "
             "from Part 14. =COUNTIFS(A:A, A2, B:B, B2)>1 returns TRUE when the same number and series, in columns A and B, appear more than once."),
            ("point", "Look before removing", "Two rows with the same date, name and amount are not always "
             "duplicates. Two receipts can match by chance. Only the key, or the source document, can say."),
            ("point", "A note on the built-in tool", "Google Sheets has a Remove duplicates tool. Its help page "
             "notes that values that differ only in letter case are treated as duplicates. Check what it "
             "will remove, and work on a copy."),
            ("h", "Suspect 2: Inconsistent Names and Codes"),
            "The same thing written in more than one way: “Pob.” and “Poblacion,” “RPT” and “Real Property "
            "Tax,” or a collector’s name with and without a middle initial. Each version is counted as "
            "something different.",
            ("point", "How to spot it", "List the distinct values in the column with =UNIQUE(D2:D), sort the "
             "list, and read it. Near-twins sit next to each other."),
            ("point", "First step", "Make a small mapping table: each version found, and the standard name it "
             "should be. Add a column that looks up the standard name, instead of retyping the original."),
            ("point", "Stop it coming back", "Use a dropdown list for that column, as shown in Part 12."),
            ("h", "Suspect 3: Extra and Hidden Spaces"),
            "“Reyes” and “Reyes ” look the same on screen, but the second has a space at the end, and a "
            "spreadsheet treats them as different values. Lookups fail and counts split for no visible reason.",
            ("point", "How to spot it", "=LEN(C2)<>LEN(TRIM(C2)) returns TRUE when a cell has spaces at the "
             "ends or doubled inside."),
            ("point", "First step", "=TRIM(C2) in a new column removes them."),
            ("point", "The space TRIM misses", "Microsoft’s help explains that Excel’s TRIM removes the "
             "ordinary space character but not the non-breaking space, character 160, which can arrive in "
             "text copied from web pages. Google’s help for Sheets says the same of its TRIM. "
             "=TRIM(SUBSTITUTE(C2, CHAR(160), \" \")) handles both."),
            ("h", "Suspect 4: Numbers Stored as Text"),
            "An amount that looks like 1,250.00 may be stored as text, especially after an export or a paste "
            "from another program. A SUM can leave it out, and the total comes up short without any error.",
            ("point", "How to spot it", "=ISNUMBER(F2) returns FALSE for a number stored as text. Another "
             "clue: in both Excel and Google Sheets, numbers line up on the right by default, while text lines "
             "up on the left. A column of amounts with a few left-aligned cells deserves a look."),
            ("point", "First step", "=VALUE(F2) in a new column converts text that looks like a number into a "
             "real number."),
            ("point", "Check the total", "Compare =SUM of the original column with =SUM of the converted one. "
             "The difference is the money the first total was missing."),
            ("h", "Suspect 5: Mixed Date Formats"),
            "A date typed as 03/04/2026 can mean March 4 or April 3, depending on who typed it and how the "
            "spreadsheet is set up. Other dates arrive as text, for example from an export, and the spreadsheet cannot sort them by date.",
            ("point", "How to spot it", "Spreadsheets store real dates as numbers, so =ISNUMBER(B2) returns "
             "FALSE for a date that is only text. Sorting the column also helps: text dates gather in one "
             "block, apart from the real ones."),
            ("point", "First step", "Agree on one format for new entries, such as the year-month-day order "
             "from Part 15, and fix the old ones in a new column. Ambiguous dates go back to the source "
             "document, not to a guess."),
            ("h", "Suspect 6: Missing Values"),
            "A blank cell can mean “zero,” “not yet known,” “not applicable” or “forgot to type.” Those are "
            "four different facts, and a blank hides which one it is.",
            ("point", "How to spot it", "=COUNTBLANK(F2:F500) counts the blanks in a column. Also look for "
             "stand-ins such as “N/A,” “none,” a dash or 0 used to mean “unknown.”"),
            ("point", "First step", "Do not fill a blank amount with zero or an average just to make the sheet "
             "complete. Find the source document, or mark the row so it can be counted separately."),
            ("point", "Report it", "If 40 of 600 permits have no barangay, say so beside the chart, instead of "
             "leaving them out quietly."),
            ("h", "Suspect 7: Impossible or Unlikely Values"),
            "An amount with an extra zero, a payment dated in 2062, a negative tax due, or a permit fee far "
            "above any fee in the schedule. Some are typing errors. Some are real and unusual.",
            ("point", "How to spot it", "Sort each number and date column from smallest to largest, then the "
             "other way, and read both ends. =MIN and =MAX do the same for a quick look."),
            ("point", "Check, do not delete", "A large amount may be a large business paying its real tax. "
             "Compare the row with the receipt or the assessment before changing anything."),
            ("point", "Set limits", "Data validation can reject a date outside the year or an amount below "
             "zero at the moment it is typed."),
            ("h", "Suspect 8: Outdated Records"),
            "A business that closed last year still listed as active, or a taxpayer’s old address. Each value "
            "was correct once.",
            ("point", "How to spot it", "Add a “last updated” column, and sort by it. Records not touched in "
             "a long time are the ones to confirm first."),
            ("point", "First step", "Update the record in one place, as Part 14 suggested, so the change "
             "reaches every row that points to it."),
            ("h", "Keep a Cleaning Log"),
            "Every fix changes the data, so write it down. A short log, like the change log from Part 15, "
            "lists what was found, how many rows, and what was done: “Mapped 7 barangay spellings to the "
            "standard list. Removed 6 duplicate renewals after checking receipt numbers.”",
            "The log lets someone else repeat the cleaning next month, and it answers the question “Why does "
            "your total differ from the raw file?” before anyone asks it.",
            ("h", "A Ten-Minute Dirty-Data Scan"),
            ("point", "1. Keys", "Count duplicates in the key column."),
            ("point", "2. Text columns", "List the distinct values, sorted, and read them."),
            ("point", "3. Spaces", "Run the LEN and TRIM test on names and codes."),
            ("point", "4. Numbers and dates", "Run ISNUMBER on every amount and date column."),
            ("point", "5. Blanks", "Count blanks and stand-ins in each important column."),
            ("point", "6. Both ends", "Sort each number and date column both ways and read the extremes."),
            "Ten minutes is a rough guide for a sheet of a few hundred rows. The point is to run the same scan "
            "every time, before any total leaves the office.",
            ("h", "The Permits Sheet, Cleaned"),
            "The analyst ran the scan on a copy of the permits sheet. A mapping table turned seven spellings "
            "into the standard barangay names, and the count fell from 31 to 24. Six renewals appeared twice "
            "because two encoders had typed the same batch; the receipt numbers confirmed it. Twelve fees "
            "were stored as text and were missing from the first total.",
            "The new count went to the head of office with one line underneath: “Cleaned on January 26; "
            "cleaning log attached.”",
            ("h", "Mistakes to Avoid"),
            ("point", "Cleaning the original", "Work on a copy, and keep the raw file as it arrived."),
            ("point", "Deleting what looks odd", "Check unusual values against the source first."),
            ("point", "Filling blanks with guesses", "A blank is a question, not a zero."),
            ("point", "Cleaning without a log", "Write down every fix so it can be repeated and explained."),
            ("h", "Key Takeaways"),
            ("point", "Dirty is not fake", "Dirty data is real data that is not yet fit to count."),
            ("point", "Know the suspects", "Duplicates, inconsistent names, spaces, text numbers, dates, "
             "blanks, odd values and old records."),
            ("point", "Spot before you fix", "A quick formula test finds each one."),
            ("point", "Fix safely", "Work in new columns or copies, and keep a cleaning log."),
            ("h", "Your Part 16 Exercise"),
            "Take one spreadsheet your office uses for counting, such as permits, receipts or notices.",
            ("point", "Run the scan", "Go through the six steps above on a copy of the sheet."),
            ("point", "Count the suspects", "Write down how many rows each kind of problem affects."),
            ("point", "Fix one", "Pick the problem that changes the totals most, fix it in a new column, and "
             "log it."),
            "Then compare the total before and after. The gap shows how much the dirty data was hiding.",
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 15", "/blog/data-analytics-part-15-naming-versions-backups/"),
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("ask", "Which column in your office’s data has the most ways of spelling the same thing?"),
        ],
    },
    {
        "date": "January 21, 2027",
        "title": "Data Analytics Series, Part 15: Naming, Versions and Backups, Keeping Data Files Safe",
        "slug": "data-analytics-part-15-naming-versions-backups",
        "category": "data",
        "summary": "“Final,” “final2” and “final-REAL” are how good analysis gets lost. This part gives simple "
                   "rules for naming data files, keeping versions you can trust, and backing them up with the "
                   "3-2-1 rule, so you can find, and trust, the right file.",
        "publish_on": "2027-01-21 21:00",
        "body": [
            "The analyst needs last quarter’s cleaned collections file. The shared folder holds "
            "“collections.xlsx,” “collections final.xlsx,” “collections final2.xlsx,” “collections final "
            "USE THIS.xlsx” and “Copy of collections final2.xlsx.” Each one has slightly different totals. "
            "The person who made them has since moved to another office.",
            "Then the computer that held the only other copy stops starting up. The cleaned file the head of "
            "office approved is somewhere in that folder, or it is gone.",
            "Nothing in the analysis was wrong. The problem was how the files were named, saved and copied.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town or taxpayer is described.)",
            "Part 14 showed how to organize data inside a database. This part is about the files themselves. "
            "By the end of this post you will know a naming pattern that sorts itself, a simple way to keep "
            "versions, the 3-2-1 backup rule, and how to test that a backup actually works.",
            ("photo", "blog/data-file-safety.jpg", "Keeping data files safe: clear names, numbered versions, "
             "three copies and a restore test. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Names That Sort Themselves"),
            "A good file name tells you what is inside before you open it, and puts related files in a useful "
            "order when sorted by name.",
            ("point", "Date first, year-month-day", "Write dates as 2026-10-31, not 10-31-2026 or Oct 31. "
             "Written this way, files sort in calendar order by name alone, and nobody wonders whether 10-11 "
             "means October 11 or November 10. This order follows the ISO 8601 date standard."),
            ("point", "Then what it is", "A short, plain description: collections-q3, rpt-delinquent-list, "
             "business-permits."),
            ("point", "Then the stage", "raw, clean or report, so nobody mistakes an untouched export for a "
             "checked file."),
            ("point", "Then the version", "v01, v02, v03, with a leading zero so v10 sorts after v09."),
            ("point", "No spaces or special characters", "Use hyphens or underscores. Some systems and "
             "scripts handle spaces, slashes and symbols poorly."),
            "Put together: 2026-09-30_collections-q3_clean_v03.xlsx. Anyone in the office can tell what it "
            "is, when it is from and which version it is.",
            ("quote", "A file name is the first line of documentation."),
            ("h", "Versions You Can Trust"),
            "A file called “final” can still change the next day. Numbered versions are easier to follow.",
            ("point", "Raw stays raw", "Keep the original export untouched, named with the stage raw. All "
             "cleaning happens on copies. If a cleaning step goes wrong, you can start again from the raw "
             "file."),
            ("point", "Number every saved change", "When a change matters, save as the next version number "
             "instead of overwriting. Old versions stay available if a question comes up."),
            ("point", "Keep a short change log", "Add a sheet or a text file that lists each version, the "
             "date, who made it and what changed: “v03: removed 12 duplicate receipts, fixed barangay codes.”"),
            ("point", "Mark the approved one", "When the head of office approves a version, write that in the "
             "change log with the date. The approved version is a fact, not a guess based on the file name."),
            "Google Sheets files, and Excel files stored in OneDrive or SharePoint, keep a version "
            "history of their own, which helps. It does not replace clear names and a change log, because it records when a "
            "file changed, not why.",
            ("h", "Inside the File: Sheets and Columns"),
            "Good names matter inside the file too, not only on the file itself.",
            ("point", "Name every sheet", "Replace Sheet1 and Sheet2 with names such as Receipts, Lists, Notes "
             "and Summary, so formulas that point to them are easier to read."),
            ("point", "Name columns plainly", "Use short, clear headers such as receipt_no, date, barangay and "
             "amount. Avoid headers that only make sense to the person who wrote them."),
            ("point", "Keep the change log inside", "A sheet called Changes, at the end of the workbook, "
             "travels with the file wherever it is copied."),
            ("point", "Note the source", "On the Notes sheet, write where the raw data came from and the date "
             "it was exported, so the next person can trace it back."),
            ("h", "One Home for Each File"),
            ("point", "One shared folder", "Agree on one folder where the working files live, not on "
             "anyone’s desktop or phone."),
            ("point", "A simple folder layout", "For example: one folder per year, and inside it raw, clean "
             "and reports."),
            ("point", "Office accounts", "Keep shared files in an account that belongs to the office, so they "
             "stay when someone transfers or retires."),
            ("point", "Access to match the data", "Files with taxpayer names and amounts carry personal "
             "information. Share them only with the people who need them, as discussed in Part 6."),
            ("h", "The 3-2-1 Backup Rule"),
            "A well-known rule for backups, often credited to photographer Peter Krogh and adopted in "
            "guidance from the U.S. Cybersecurity and Infrastructure Security Agency, has three parts.",
            ("point", "3 copies", "Keep at least three copies of data that matters: the working copy and two "
             "backups."),
            ("point", "2 kinds of storage", "Keep the copies on at least two different kinds of storage, such "
             "as the office computer and an external drive, or a drive and a cloud account."),
            ("point", "1 copy elsewhere", "Keep at least one copy away from the office, or in a separate "
             "account, so a fire, flood or theft does not take every copy at once."),
            "For a small treasury office, this can be as simple as the working files in the shared folder, a "
            "weekly copy to an external drive kept in a locked cabinet, and a copy in a separate cloud account "
            "that belongs to the office. Ask your IT staff or data protection officer which services the "
            "office is allowed to use for personal data.",
            ("h", "Test the Restore, Not Just the Backup"),
            "A backup you have never restored is a hope, not a backup. Once a month, try it.",
            ("point", "Pick one file", "Choose a file at random from the backup."),
            ("point", "Restore it to a new place", "Copy it back to a test folder, never over the working "
             "copy."),
            ("point", "Open and check", "Does it open? Do its totals match the change log?"),
            ("point", "Write it down", "Note the date and the result. If the restore failed, fix the backup "
             "before you need it."),
            ("h", "The Collections Folder, Cleaned Up"),
            "The analyst gathered the five files, compared their totals with the approved report, and found "
            "that “collections final2.xlsx” matched. It was renamed 2026-09-30_collections-q3_clean_v02.xlsx, "
            "with a change log entry noting the approval date. The other files went into an archive folder "
            "with their own version numbers, instead of being deleted.",
            "The office then set up the 3-2-1 copies and a monthly restore test on the first working day of "
            "each month.",
            ("h", "Mistakes to Avoid"),
            ("point", "“Final” in the name", "Use version numbers, and record approval in the change log."),
            ("point", "Overwriting the raw export", "Clean a copy. Keep the original as it arrived."),
            ("point", "Backups in the same place", "A copy on the same computer is lost with the computer."),
            ("point", "Never testing", "Restore a file each month to prove the backup works."),
            ("h", "Key Takeaways"),
            ("point", "Names that sort", "Date first, then what, then stage, then version."),
            ("point", "Versions with a log", "Number each change and write down why."),
            ("point", "3-2-1", "Three copies, two kinds of storage, one elsewhere."),
            ("point", "Test the restore", "A backup counts only if it can be opened."),
            ("h", "Your Part 15 Exercise"),
            "Open the folder where your office keeps its most important data file.",
            ("point", "Count the copies", "How many versions of the same file are there, and can you tell "
             "which one was approved?"),
            ("point", "Rename one", "Rename the approved version using the date, what, stage and version "
             "pattern, and start a change log."),
            ("point", "Check 3-2-1", "Count the copies of that file and where they are kept."),
            "Then restore one backup copy to a test folder and open it. If you cannot, you have found the most "
            "important task for this week.",
            ("cta", "Read: Data Analytics Series, Part 14", "/blog/data-analytics-part-14-databases-101/"),
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("ask", "How many copies of your office’s most important data file exist, and where are they?"),
        ],
    },
    {
        "date": "January 16, 2027",
        "title": "Data Analytics Series, Part 14: Databases 101, Tables, Primary Keys and Foreign Keys",
        "slug": "data-analytics-part-14-databases-101",
        "category": "data",
        "summary": "A spreadsheet that repeats the same taxpayer’s name on every receipt is one typo away from "
                   "counting one person as two. This part explains, in plain words, how a database splits "
                   "data into linked tables using primary keys and foreign keys, with a three-table treasury "
                   "example you can sketch on paper.",
        "publish_on": "2027-01-16 21:00",
        "body": [
            "The collections sheet has a row for every receipt, and each row repeats the taxpayer’s full name "
            "and address. Over the year, one taxpayer appears as “Dela Cruz, Juan,” “Juan dela Cruz” and "
            "“Dela Cruz, Juan P.” A count of taxpayers who paid comes out higher than it should, because one "
            "person has become three.",
            "Then the taxpayer moves to a new address. The clerk updates it on the latest receipt row, but the "
            "older rows keep the old address. Now the sheet holds two addresses for the same person, and "
            "nobody can tell which one is current.",
            "Both problems have the same cause: the same fact is typed in many places. Databases are designed "
            "to avoid exactly that.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town or taxpayer is described.)",
            "Part 12 showed how to lay out one clean table. This part shows how several tables work together. "
            "By the end of this post you will know what a database table, a record and a field are, what "
            "primary and foreign keys do, how tables are linked, and how to sketch a small treasury database "
            "before anyone builds it.",
            ("photo", "blog/data-database-keys.jpg", "Three linked tables: taxpayers, receipts and "
             "collectors. Each receipt points to one taxpayer and one collector by their keys. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Words You Need"),
            ("point", "Database", "An organized collection of data. In the kind of database "
             "this post describes, the data is kept in tables that can be linked to each other."),
            ("point", "Table", "A set of rows and columns about one kind of thing: taxpayers, receipts or "
             "collectors. It follows the same rules as the clean sheet from Part 12."),
            ("point", "Record", "One row in a table: one taxpayer, one receipt."),
            ("point", "Field", "One column in a table: a name, a date, an amount."),
            "If you have kept a clean spreadsheet with one row per record, you already know most of this. What "
            "a database adds is the idea of keys.",
            ("h", "Primary Key: One Value, One Record"),
            "A primary key is a field whose value identifies exactly one record in its table. No two records may share it, and it should never be left blank.",
            ("point", "Taxpayers table", "A taxpayer ID such as T-00125. Names are a poor key because two "
             "people can share a name, and the same person can be written in different ways."),
            ("point", "Receipts table", "The official receipt number together with its series, since numbers "
             "are unique only within a series."),
            ("point", "Collectors table", "A collector ID such as C-04."),
            "A good primary key does not change. A name or an address can change; an ID assigned once and "
            "never reused is a safer key.",
            ("quote", "Give every record one value that belongs to it alone."),
            ("h", "Foreign Key: Pointing to Another Table"),
            "A foreign key is a field in one table that holds the primary key of a record in another table. "
            "It is how tables point to each other.",
            "In the receipts table, instead of typing the taxpayer’s name and address on every receipt, you "
            "type only the taxpayer ID. That ID is a foreign key: it points to one row in the taxpayers table, "
            "where the name and address are kept once.",
            ("point", "Receipt 004512", "Taxpayer ID T-00125, collector ID C-04, date, amount."),
            ("point", "Taxpayer T-00125", "Name, address, contact details, typed once."),
            ("point", "Collector C-04", "Name and assigned barangays, typed once."),
            "When the taxpayer moves, the address is changed in one row of the taxpayers table, and every "
            "receipt that points to T-00125 now leads to the new address.",
            ("h", "How Tables Relate"),
            ("point", "One-to-many", "One taxpayer can have many receipts, but each receipt belongs to one "
             "taxpayer. Receipts and taxpayers are linked this way."),
            ("point", "One-to-one", "One record matches exactly one record in another table, for "
             "example when sensitive details are kept in a separate table with tighter access."),
            ("point", "Many-to-many", "One taxpayer can own several properties, and one property can have "
             "several owners. This needs a third table in between, such as an ownership table with one row "
             "for each taxpayer–property pair."),
            ("h", "Why Split the Data at All?"),
            ("point", "Each fact once", "A name or address typed once cannot disagree with itself."),
            ("point", "Easier counting", "Counting taxpayers who paid means counting distinct taxpayer IDs, "
             "not guessing which spellings are the same person."),
            ("point", "Rules the database can enforce", "A database can refuse a receipt whose taxpayer ID "
             "does not exist in the taxpayers table, or a second record with the same primary key."),
            ("point", "Tighter access", "Personal details can sit in one table that fewer people can open, "
             "while the receipts can be analyzed by ID. This supports the Data Privacy Act duties discussed "
             "in Part 6."),
            ("h", "Sketching a Treasury Database on Paper"),
            "Before anyone installs anything, draw it. A sheet of paper is enough.",
            ("point", "1. List the things", "Write one box for each kind of thing you record: taxpayers, "
             "receipts, collectors."),
            ("point", "2. Choose the keys", "Under each box, write its primary key first."),
            ("point", "3. List the fields", "Add the fields that belong to that thing and to nothing else. The "
             "taxpayer’s address belongs in Taxpayers, not in Receipts."),
            ("point", "4. Draw the links", "Draw a line from each foreign key to the table it points to, and "
             "mark which side is the “many.”"),
            ("point", "5. Test with a question", "Pick a real question, such as “How much did each collector "
             "receive from taxpayers in San Isidro last month?” Trace on paper how the tables would answer "
             "it. If you cannot, a field or a link is missing."),
            ("h", "Does This Field Belong Here?"),
            "When you are unsure where a field goes, ask what it describes.",
            ("point", "It describes the taxpayer", "Name, address, contact number. It goes in Taxpayers, "
             "even if you first saw it on a receipt."),
            ("point", "It describes the payment", "Date, amount, revenue source, receipt number. It goes in "
             "Receipts."),
            ("point", "It describes the collector", "Name, assigned barangays. It goes in Collectors."),
            ("point", "It describes a pair", "The share of a property owned by one taxpayer describes the "
             "taxpayer and the property together, so it goes in the ownership table between them."),
            ("h", "Spreadsheet or Database?"),
            "A spreadsheet can be enough for one person working with one table. A database starts to make "
            "sense when several tables need to be linked, several people enter data at the same time, or "
            "rules such as unique receipt numbers must be enforced every time.",
            "A free way to learn is SQLite, a database engine that stores a whole database in a single "
            "ordinary file, with no server to set up.",

            ("h", "Mistakes to Avoid"),
            ("point", "Names as keys", "Use an ID that never changes and never repeats."),
            ("point", "Copying fields across tables", "If the taxpayer’s address appears in the receipts "
             "table, it can drift out of date. Keep it in one place."),
            ("point", "Reusing old IDs", "An ID given to a closed account should not be given to a new one."),
            ("point", "Building before sketching", "Draw the tables and test them with a question first."),
            ("h", "Key Takeaways"),
            ("point", "Tables, records, fields", "Rows and columns about one kind of thing."),
            ("point", "Primary key", "One value, one record, never blank, never repeated."),
            ("point", "Foreign key", "A pointer to a record in another table."),
            ("point", "Each fact once", "Splitting data into linked tables keeps it consistent."),
            ("h", "Your Part 14 Exercise"),
            "Take one spreadsheet your office uses that repeats the same names or addresses on many rows.",
            ("point", "Find the things", "List each kind of thing it records, such as taxpayers, receipts or "
             "permits."),
            ("point", "Choose the keys", "Write a primary key for each, and mark where a foreign key would "
             "replace a repeated name."),
            ("point", "Draw it", "Sketch the boxes and lines on paper, and test them with one real question."),
            "Count how many columns would disappear from the main sheet once each repeated fact lives in its "
            "own table. That number shows how much room there was for errors.",
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 13", "/blog/data-analytics-part-13-bias-in-data/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("ask", "Which name or address does your office type again and again that belongs in its own table?"),
        ],
    },
    {
        "date": "January 11, 2027",
        "title": "Data Analytics Series, Part 13: Bias in Data, and How to Catch It",
        "slug": "data-analytics-part-13-bias-in-data",
        "category": "data",
        "summary": "Data can be accurate and still lead to the wrong answer when it leans one way. This part "
                   "explains four kinds of bias, sampling, observer, interpretation and confirmation, with "
                   "treasury examples and a short checklist for catching each one.",
        "publish_on": "2027-01-11 21:00",
        "body": [
            "The office wants to know how taxpayers feel about its service, so it runs a short survey at the "
            "counter for two weeks. The results are excellent: nine out of ten say the service is fast and "
            "friendly. The report goes up with a confident headline.",
            "A month later, a councilor mentions that several residents have complained about long waits and "
            "unclear notices. How can both be true?",
            "Look at who answered. The survey reached only people who came to the counter, during the two "
            "quietest weeks of the year, and who had time to stay a few minutes after paying. The people who "
            "gave up waiting, who never came because the notice confused them, or who came during the January "
            "rush, were never asked. Every answer was real. The sample was not the whole picture.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town, councilor or taxpayer is described.)",
            "Part 11 tested whether a source can be trusted, and Part 12 put the data in a clean sheet. This "
            "part asks a different question: does the data, or the way we read it, lean one way? By the end "
            "of this post you will know four common kinds of bias, how each shows up in treasury work, and a "
            "simple check for each.",
            ("photo", "blog/data-bias.jpg", "Four kinds of bias: sampling, observer, interpretation and "
             "confirmation. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Bias Means Here"),
            "The Google Data Analytics course defines bias as a conscious or subconscious preference in favor "
            "of or against a person, group of people or thing. In data work, bias is any lean that pushes the "
            "result away from the truth in one direction.",
            "Bias is different from a random error. A typing mistake in one receipt may push a total up or "
            "down by chance. Bias pushes in the same direction "
            "again and again, so collecting more of the same data does not remove it. A bigger survey at the same counter in the same quiet weeks would only repeat the same "
            "lean with more confidence.",
            ("quote", "More data with the same lean is still leaning."),
            ("h", "1. Sampling Bias: Who Was Counted?"),
            "Sampling bias happens when the group you collected data from does not represent the whole group "
            "you want to describe. The counter survey above is one example.",
            ("point", "Treasury example", "Estimating how many businesses operate without a permit by "
             "checking only stores along the main road. The side streets and the barangays far from the town "
             "center may look very different."),
            ("point", "How to catch it", "Write down the whole group your question is about, such as “all "
             "taxpayers” or “all businesses in the municipality.” Then ask who in that group could not have "
             "ended up in your data."),
            ("point", "How to reduce it", "Choose from the full list rather than from whoever is nearby. One "
             "simple way is to take every tenth account from the complete list, so the sample is spread "
             "across the whole list."),
            ("h", "2. Observer Bias: Who Recorded It?"),
            "Observer bias happens when the expectations of the person collecting the data affect what gets "
            "recorded. Two people looking at the same thing can write it down differently.",
            ("point", "Treasury example", "Collectors marking visited accounts as “refused to pay” or “not "
             "home.” One collector who expects resistance may write “refused” for a door that simply was not "
             "answered. The count of refusals then depends on who visited, not only on what happened."),
            ("point", "How to catch it", "Compare the same measure across the people who record it. If one "
             "collector reports three times as many refusals as the others in similar areas, look closer "
             "before drawing conclusions."),
            ("point", "How to reduce it", "Write a short definition for each choice, such as “Refused: the "
             "taxpayer said they will not pay.” Train everyone on the same definitions, and use a dropdown "
             "with only those choices, as in Part 12."),
            ("h", "3. Interpretation Bias: How Was It Read?"),
            "Interpretation bias is the tendency to read unclear or neutral data in a way that fits what we "
            "already think. The numbers are fine; the reading leans.",
            ("point", "Treasury example", "Real property tax collections in March are lower than last March. "
             "One reader sees taxpayers becoming less willing to pay. Another notices that a discount "
             "deadline moved, shifting payments into February. The same number supports both readings until "
             "someone checks."),
            ("point", "How to catch it", "Before explaining a change, list at least two other possible causes. "
             "Check each one against the data: Did February rise by about the same amount? Did anything "
             "change in the calendar, the rules or the system?"),
            ("point", "How to reduce it", "Ask someone who was not involved to read the chart and explain it "
             "in their own words before you share your explanation."),
            ("h", "4. Confirmation Bias: What Did We Look For?"),
            "The Google course describes confirmation bias as the tendency to search for or interpret "
            "information in a way that confirms what we already believe. It affects which data we look at in "
            "the first place.",
            ("point", "Treasury example", "A staff member is sure that the new online payment option is "
             "lowering counter collections. They pull the three months where counter collections fell and "
             "stop there, without checking the months where counter collections rose after online payment "
             "started."),
            ("point", "How to catch it", "Ask: “What would I expect to see if I am wrong?” Then go and look "
             "for exactly that."),
            ("point", "How to reduce it", "Write down your question and how you will measure it before you "
             "open the data. Decide in advance which months, which accounts and which comparison you will "
             "use, and stick to them."),
            ("h", "Who Is Missing From the Data?"),
            "Some treasury records describe only the people who already deal with the office. A list of "
            "business taxpayers contains registered businesses. A list of payments contains people who paid. "
            "A complaint log contains people who knew how to complain.",
            "None of these lists is wrong. But a conclusion drawn from them describes only the people on them. "
            "Before saying “taxpayers think” or “businesses are,” check whether the data includes the people "
            "who are not yet on any list.",
            ("h", "A Five-Question Bias Check"),
            "Before sharing any finding, run through five questions. They take a few minutes.",
            ("point", "Who should be in this data?", "Name the whole group the question is about."),
            ("point", "Who could not be in it?", "Look for the people, places or periods that were left out."),
            ("point", "Who recorded it, and how?", "Check whether definitions were written down and shared."),
            ("point", "What else could explain it?", "List at least two other causes and check them."),
            ("point", "What would prove me wrong?", "Look for that evidence on purpose."),
            "Write the answers in a short note with the analysis. If a question cannot be answered, say so in "
            "the report: “The survey covered counter visitors only.” Readers can then judge the result fairly.",
            ("h", "The Survey, Done Again"),
            "The office ran the survey again. This time it chose every tenth taxpayer from the full list of "
            "property accounts, reached them by text message and by a short form at the barangay hall, and "
            "spread the survey across a busy month and a quiet one. The questions were written so they did not "
            "suggest an answer, for example “How long did you wait?” instead of “Was the service fast?”",
            "The results were more mixed and more useful. Most people still rated the staff well, but waiting "
            "time during the January rush and the wording of the notices stood out. Those became the two "
            "things the office set out to fix.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting size over fairness", "A large sample from the wrong group is still the wrong "
             "group."),
            ("point", "Undefined categories", "If “refused” is not defined, each person may define it differently."),
            ("point", "One explanation only", "A single explanation, checked against nothing, is a guess."),
            ("point", "Hiding the limits", "State who the data covers, so readers can judge the "
             "finding fairly."),
            ("h", "Key Takeaways"),
            ("point", "Bias leans one way", "More of the same data does not fix it."),
            ("point", "Four kinds", "Sampling, observer, interpretation and confirmation."),
            ("point", "Check who is missing", "Records describe only the people on them."),
            ("point", "Run the five questions", "And write the limits into the report."),
            ("h", "Your Part 13 Exercise"),
            "Pick one finding your office shared in the last year, such as a survey result, a trend or a "
            "comparison.",
            ("point", "Run the check", "Answer the five questions above for that finding."),
            ("point", "Name the lean", "Decide which of the four kinds of bias, if any, could have affected it."),
            ("point", "Write one line", "Draft the sentence that should have gone with it, such as “This "
             "covers only accounts that paid at the counter.”"),
            "If you find no possible bias at all, ask a colleague to try. A second pair of eyes is one of the "
            "simplest checks there is.",
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 11", "/blog/data-analytics-part-11-roccc-test/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("ask", "Which of your office’s numbers describes only the people who already come to the counter?"),
        ],
    },
    {
        "date": "January 6, 2027",
        "title": "Data Analytics Series, Part 12: Spreadsheets Done Right, One Row per Record",
        "slug": "data-analytics-part-12-one-row-per-record",
        "category": "data",
        "summary": "A spreadsheet can look neat to people and still be hard to sort, filter or total. This part "
                   "gives seven layout rules for treasury spreadsheets, from one header row to no merged cells "
                   "and dropdown lists, and shows a messy collections tracker fixed step by step.",
        "publish_on": "2027-01-06 21:00",
        "body": [
            "The revenue unit keeps a collections tracker that everyone in the office has added to over the "
            "years. It opens with a large title across the top, a merged heading that says “First Quarter,” "
            "and the barangays listed in groups, each followed by a bold subtotal row. Paid accounts are "
            "shaded green. A blank row separates each group so the sheet is easier on the eyes.",
            "One afternoon the head of office asks a simple question: which ten accounts paid the most this "
            "quarter? The analyst tries to sort the amounts. The spreadsheet refuses because of the merged "
            "cells. After unmerging them, the sort runs, but now the subtotal rows are mixed in with the "
            "accounts, and the biggest “account” on the list is a barangay subtotal. And no simple formula counts the green rows.",
            "The sheet was built to be looked at. It was not built to be worked with.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town, barangay or taxpayer is described.)",
            "Part 10 covered data types and the difference between wide and long tables. This part is about "
            "the layout of the sheet itself. By the end of this post you will know seven rules that make a "
            "spreadsheet easy to sort, filter and total, how to fix a messy tracker without losing data, and "
            "how to keep it clean once it is fixed.",
            ("photo", "blog/data-one-row.jpg", "A sheet you can work with: one row per record, one header row, facts in cells and the same codes every time. "
             "(Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What “One Row per Record” Means"),
            "A record is one thing you want to count: one receipt, one payment, one taxpayer, one permit. In a "
            "working sheet, each record gets exactly one row, and each fact about it gets its own column. A "
            "row for receipt 004512 holds its date, account, barangay, amount and collector, and nothing else "
            "sits in that row.",
            "Decide first what one row stands for, and write it down. “One row per official receipt” and “one "
            "row per taxpayer” are both fine, but a sheet that mixes the two can count some things twice.",
            ("quote", "Decide what one row stands for before you type the first row."),
            ("h", "Seven Rules for a Sheet You Can Work With"),
            ("point", "1. One header row", "Put the column names in the first row, one name per column, with "
             "no title above them. Move the title to the file name or to a separate notes sheet. Filters, sorting and pivot tables use the top row of the data as the column names."),
            ("point", "2. No merged cells", "Merged cells look tidy but get in the way of sorting, filtering "
             "and copying. Microsoft’s support page notes that Excel will not sort a range where only some of "
             "the cells are merged. If a heading needs to span columns, keep it in the printed report, not in "
             "the data."),
            ("point", "3. No blank rows or columns", "A blank row may be read as the end of the table, so a "
             "filter or a selection can stop halfway through the data. Use formatting or a separate report "
             "if you need space for the eyes."),
            ("point", "4. No totals inside the data", "Subtotal rows look like records to a formula or a "
             "sort. Keep the raw rows clean, and calculate totals in a separate summary or pivot table."),
            ("point", "5. One table per sheet", "Two tables side by side on one sheet are easy to break when "
             "one of them grows. Give each table its own sheet, with a clear sheet name."),
            ("point", "6. Facts in cells, not in colors", "Green shading for “paid” cannot be counted or "
             "filtered as easily as a column called Status with the word Paid in it. Color can still be "
             "used, but only to highlight a fact that is already written in a cell."),
            ("point", "7. The same code every time", "“Brgy. 1,” “Barangay 1” and “Poblacion 1” for the same "
             "place become three different places in a count. Choose one code per item and keep a list of "
             "the allowed codes."),
            ("h", "Dropdown Lists: Stopping Errors at the Door"),
            "Rule 7 is easier to keep when the spreadsheet does the checking. Both Google Sheets and Excel can "
            "limit a cell to a list of allowed values, shown as a dropdown.",
            ("point", "In Google Sheets", "Select the cells, then go to Data, Data validation, Add rule, and "
             "choose “Dropdown” or “Dropdown (from a range).” Google’s help page explains that entries not on "
             "the list are rejected unless you change the rule to show a warning instead."),
            ("point", "In Excel", "Select the cells, then go to Data, Data Validation, and under Allow choose "
             "List. Point the source to a range that holds the allowed values."),
            ("point", "Keep the list on its own sheet", "Put the allowed barangays, revenue sources and "
             "collectors on a sheet called Lists. When a new item is approved, add it there once. Then check that each dropdown’s source range includes the new row."),
            "A dropdown does not make a value correct. It only makes sure the value is one of the allowed "
            "choices. Someone can still pick the wrong barangay, so the checks in the next section still "
            "matter.",
            ("h", "Fixing the Collections Tracker, Step by Step"),
            "Never fix the only copy. Save a copy of the original file first, with the date in its name, and "
            "work on the copy.",
            ("point", "1. Write down what a row is", "Here, one row per official receipt."),
            ("point", "2. Move the title", "Delete the title rows above the headers and put the title in the "
             "file name."),
            ("point", "3. Unmerge and fill", "Unmerge every merged cell. Where a merged cell held a barangay "
             "name for a group of rows, type that name into every row of the group, so each row carries its "
             "own barangay."),
            ("point", "4. Remove blanks and subtotals", "Delete the blank rows and the subtotal rows. Before "
             "deleting the subtotals, write their values down; you will use them in step 7."),
            ("point", "5. Turn colors into a column", "Add a Status column and type Paid or Unpaid for each "
             "row, matching the old shading. Then clear the shading."),
            ("point", "6. Standardize the codes", "Sort by barangay, read down the list and correct the "
             "variations to one code each. Add dropdowns so the codes stay fixed."),
            ("point", "7. Check the totals", "Build a pivot table of amounts by barangay and compare it with "
             "the subtotals you wrote down in step 4. They must match. If one does not, find out why before "
             "you go on."),
            "Step 7 is the most important one. A cleanup that changes the totals has damaged the data, even "
            "if the sheet looks better.",
            ("h", "Keeping It Clean"),
            ("point", "A notes sheet", "Add a sheet called Notes that says what one row stands for, what each "
             "column means, where the data comes from and who maintains it."),
            ("point", "Raw data and reports apart", "Keep the working data on one sheet and build reports, "
             "charts and summaries on others. People can format the report sheet however they like without "
             "touching the data."),
            ("point", "Freeze the header", "Freeze the first row so the column names stay in view while "
             "scrolling. In Google Sheets it is under View, Freeze; in Excel, under View, Freeze Panes."),
            ("point", "A unique ID column", "Give each record a value that never repeats, such as the receipt "
             "number with its series. It makes duplicates easy to find."),
            ("h", "Mistakes to Avoid"),
            ("point", "Fixing the only copy", "Always work on a dated copy."),
            ("point", "Typing totals by hand", "A total typed into a cell does not update when a row changes. "
             "Let a formula or pivot table calculate it."),
            ("point", "Notes in the amount column", "Text such as “paid half, balance next week” turns an "
             "amount into text. Put remarks in a separate Remarks column."),
            ("point", "Hiding rows instead of deleting them", "Hidden rows still count in some formulas, so a "
             "total can include rows nobody can see."),
            ("h", "Key Takeaways"),
            ("point", "One row, one record", "Decide what a row stands for and keep to it."),
            ("point", "Clean layout", "One header row, no merged cells, no blank rows and no totals inside "
             "the data."),
            ("point", "Facts in cells", "Write the status in a column, and use dropdowns to keep codes the "
             "same."),
            ("point", "Prove the cleanup", "Totals before and after must match."),
            ("h", "Your Part 12 Exercise"),
            "Open one spreadsheet your office uses every month, and work on a copy.",
            ("point", "Name the record", "Write one sentence: “One row in this sheet is one…”"),
            ("point", "Check the seven rules", "Count how many of the seven rules the sheet breaks."),
            ("point", "Fix one rule", "Pick the easiest one, fix it on the copy, and check that the totals "
             "still match."),
            "If you cannot finish the sentence “One row in this sheet is one…”, that is the first thing to "
            "fix.",
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("cta", "Read: Data Analytics Series, Part 11", "/blog/data-analytics-part-11-roccc-test/"),
            ("cta", "Read: Data Analytics Series, Part 5", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Business Intelligence Series, Part 9", "/blog/business-intelligence-part-9-testing-the-pipeline/"),
            ("ask", "Which spreadsheet in your office would you clean up first, and which rule does it break most?"),
        ],
    },
    {
        "date": "January 1, 2027",
        "title": "Data Analytics Series, Part 11: Good Data or Bad Data? The ROCCC Test",
        "slug": "data-analytics-part-11-roccc-test",
        "category": "data",
        "summary": "Before you trust a data set, test it. This part explains the five ROCCC checks, reliable, "
                   "original, comprehensive, current and cited, scores two treasury data sets with them, and "
                   "shows what to do when a source fails.",
        "publish_on": "2027-01-01 21:00",
        "body": [
            "The revenue unit is preparing next year’s collection target for business tax. Two files are on "
            "the table. One is the office’s own record of business taxes paid over the last three years, "
            "taken from the official receipts. The other is a summary someone received in a seminar handout, "
            "showing “average business tax growth for towns like ours.” It has no date and no author.",
            "The handout’s number is higher, and it would make a more impressive target. Before anyone uses "
            "it, the analyst asks a simple question: how do we know this data is good enough to plan with?",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town, business or taxpayer is described.)",
            "Part 9 explained where data comes from, and Part 10 explained what shape it is in. This part gives "
            "a quick test of whether a source can be trusted. By the end of this post you will know the five "
            "ROCCC checks, how to score a data set with them, and what to do when a source fails one.",
            ("photo", "blog/data-roccc.jpg", "The ROCCC test: reliable, original, comprehensive, current and "
             "cited. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Five Questions in One Word"),
            "ROCCC is a short checklist taught in the Google Data Analytics course for judging whether data "
            "is credible. Each letter is one question.",
            ("point", "R: Reliable", "Is the source trustworthy, and was the data collected in a consistent "
             "way? Official receipts issued under the office’s rules are reliable. Numbers copied by hand from "
             "memory are not."),
            ("point", "O: Original", "Can you trace the data back to where it was first recorded? A copy of a "
             "copy can carry errors you cannot see. Go back to the first source when you can."),
            ("point", "C: Comprehensive", "Does it contain everything needed to answer your question? A list "
             "of business tax payments that leaves out the first quarter cannot tell you the year’s total."),
            ("point", "C: Current", "Is it recent enough for the decision? Last year’s tax rates are not "
             "current if an ordinance changed them in January."),
            ("point", "C: Cited", "Is it documented, with a named source, a date and a description of how it "
             "was made? Data with no citation is hard to check."),
            ("quote", "Good data is not data you like. It is data you can trace, check and explain."),
            ("h", "Scoring the Two Files"),
            "Score each check as pass, partial or fail, and write one line explaining why.",
            ("point", "Office receipts, three years", "Reliable: pass, issued under the office’s rules. "
             "Original: pass, taken directly from the receipts. Comprehensive: partial, two months of one year "
             "were encoded late and must be checked. Current: pass, includes this year. Cited: pass, with a "
             "source note from Part 9."),
            ("point", "Seminar handout", "Reliable: unknown, the method is not given. Original: fail, it is a "
             "summary of data from elsewhere. Comprehensive: unknown, it does not say which towns were "
             "included. Current: unknown, no date. Cited: fail, no author or source."),
            "The office’s own data has one partial that can be fixed. The handout has two fails and three "
            "unknowns. It might be useful as a question to explore, but not as a number to plan with.",
            ("h", "Unknown Is Not the Same as Pass"),
            "When you cannot answer a ROCCC question, mark it unknown, not pass. An unknown is a task: ask the "
            "person who gave you the data, look for the original, or find the date.",
            "In the opening story, a phone call to the seminar organizer might turn the handout’s unknowns into "
            "answers. Until then, the honest description is: “source not verified.”",
            ("h", "What to Do When a Source Fails"),
            ("point", "Fix it", "If the problem is in your own data, such as months encoded late, correct "
             "the records and note the fix in the source note."),
            ("point", "Replace it", "If a better source exists, use it. Instead of a growth figure from an "
             "unknown handout, compute your own office’s growth from the receipts."),
            ("point", "Use it with a warning", "If there is no better source, use the data but say plainly "
             "which checks it failed. For example: “This comparison uses a figure we could not verify.”"),
            ("point", "Set it aside", "If a source fails on reliability and originality and cannot be "
             "traced, leave it out of decisions."),
            ("h", "ROCCC for the Treasury’s Common Sources"),
            ("point", "Official receipts and collection reports", "They are the first record, so they can "
             "score well on reliability and originality. Check comprehensiveness for late-encoded or "
             "missing days."),
            ("point", "Data shared by another office", "Ask for the date and how it was collected. Check "
             "currency: an assessment roll from last year may not include this year’s new declarations."),
            ("point", "Published statistics", "Check the citation: which agency, which year, and which "
             "table. Use the agency’s own publication rather than a news story or a slide that quotes it."),
            ("point", "Online lists and directories", "They can score poorly on original and cited. Treat them "
             "as leads, as in Part 9."),
            ("h", "Checking “Comprehensive” in Practice"),
            "Of the five checks, comprehensive is one your own data can fail without anyone noticing. Three "
            "quick tests help.",
            ("point", "Count the days", "For each month, count the days that have at least one receipt and "
             "compare with the working days. A working day with no receipts may mean a closed office or a missing file, so check it."),
            ("point", "Compare with signed reports", "Add up each month in your data and compare it with the "
             "monthly collections report that was signed. A difference points to missing or extra records."),
            ("point", "Check every category", "Make sure each revenue account, collector and barangay you "
             "expect appears at least once. One that is missing entirely may have been left out of the "
             "extract."),
            ("h", "A ROCCC Note, Written Out"),
            ("point", "Data set", "Business tax receipts, January 2024 to November 2026."),
            ("point", "Reliable: pass", "Official receipts issued under the office’s rules."),
            ("point", "Original: pass", "Extracted directly from the collection system."),
            ("point", "Comprehensive: partial", "March and April 2025 were encoded late; totals are being "
             "checked against the signed monthly reports."),
            ("point", "Current: pass", "Includes receipts up to November 30, 2026."),
            ("point", "Cited: pass", "Source note kept with the file, owner: the revenue unit."),
            ("h", "Making ROCCC a Habit"),
            "Add a short ROCCC section to every source note: five lines, one per letter, each with pass, "
            "partial, fail or unknown and a reason. It takes a few minutes and saves a reader from guessing "
            "later.",
            "When you present results, mention the weakest check. “This analysis uses our own receipts, "
            "complete except for March and April 2025, which are being checked” tells the reader exactly how far to "
            "trust it.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting a number because it is convenient", "The handout’s growth figure was attractive "
             "because it was high. That is a reason to check it more, not less."),
            ("point", "Assuming official means current", "An official list can still be out of date."),
            ("point", "Skipping your own data", "Your office’s records can fail a check too, such as "
             "comprehensive when days are missing."),
            ("h", "Key Takeaways"),
            ("point", "Five checks", "Reliable, original, comprehensive, current and cited."),
            ("point", "Score honestly", "Pass, partial, fail or unknown, each with a reason."),
            ("point", "Unknown is a task", "Find the answer before treating it as a pass."),
            ("point", "Say the weakest check", "Tell readers how far to trust the result."),
            ("h", "Your Part 11 Exercise"),
            "Pick one number your office used in a plan or report this year that came from outside your own "
            "records.",
            ("point", "Score it", "Run the five ROCCC checks and write a reason for each."),
            ("point", "Find the original", "Try to trace it to the first place it was published or recorded."),
            ("point", "Decide", "Fix, replace, use with a warning, or set aside."),
            "If you cannot trace it at all, ask yourself whether the plan still holds without it.",
            ("cta", "Read: Data Analytics Series, Part 9", "/blog/data-analytics-part-9-where-data-comes-from/"),
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("ask", "Which number has your office used that would fail the ROCCC test today?"),
        ],
    },
    {
        "date": "December 27, 2026",
        "title": "Data Analytics Series, Part 10: Data Types, Structured Data and Wide vs Long Tables",
        "slug": "data-analytics-part-10-data-types-and-table-shapes",
        "category": "data",
        "summary": "Before you can analyze data, you need to know what kind of data it is and what shape it "
                   "is in. This part explains data types, structured and unstructured data, and wide and "
                   "long tables, with treasury examples and the mistakes each one prevents.",
        "publish_on": "2026-12-27 21:00",
        "body": [
            "An analyst opens a spreadsheet of business permits and asks for the total gross sales declared. "
            "The answer comes back far too low. A quick look shows why: about a third of the amounts were typed "
            "with letters in front, like “PHP 1,250,000,” and the spreadsheet treated them as text. The "
            "SUM formula skipped every one of them without a warning.",
            "In another column, the barangay codes “007” and “012” have become 7 and 12. The lookup that "
            "matches codes to barangay names now fails for every barangay with a leading zero.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town, business or taxpayer is described.)",
            "Part 9 asked where data comes from. This part asks what kind of data it is and what shape it is "
            "in. By the end of this post you will know the basic data types, the difference between structured "
            "and unstructured data, how wide and long tables differ, and when to use each shape.",
            ("photo", "blog/data-wide-long.jpg", "The same collections in two shapes: a wide table with one "
             "column per month, and a long table with one row per collector per month. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Data Types: What Kind of Value Is This?"),
            "Every value in a column has a type. The type decides what you can do with it.",
            ("point", "Number", "A value you can add, average or compare: amounts, counts, areas. Store "
             "amounts as plain numbers, and let the cell format show the peso sign and commas."),
            ("point", "Text", "Letters, or digits that are not meant for arithmetic: names, addresses, "
             "receipt numbers and codes. A barangay code is text, even if it looks like a number, because "
             "nobody adds codes together and the leading zeros matter."),
            ("point", "Date", "A day on the calendar. Stored as a real date, it can be sorted, filtered by "
             "month and used to count days late."),
            ("point", "True or false", "A value with only two possible answers, such as whether a receipt was "
             "cancelled. Analysts also call this a Boolean."),
            ("quote", "Ask what you will do with a column before you decide its type."),
            ("h", "How to Spot a Wrong Type in a Spreadsheet"),
            ("point", "Look at the alignment", "In Google Sheets and Excel, numbers line up on the right of a "
             "cell by default and text on the left. An amount sitting on the left may be stored as text."),
            ("point", "Count before you sum", "Use COUNT, which counts only numbers, beside COUNTA, which "
             "counts every filled cell. If the two differ in an amount column, some amounts are text."),
            ("point", "Check the codes", "If codes lost their leading zeros, set the column format to plain "
             "text and type or import them again."),
            ("point", "Check the dates", "A date typed as “12/01/2026” can be read as December 1 or January "
             "12, depending on the spreadsheet’s regional setting. Write dates as year-month-day, such as "
             "2026-12-01, or check the setting first."),
            ("h", "Structured and Unstructured Data"),
            "The second question is how the data is organized.",
            ("point", "Structured data", "Data in rows and columns, where every row follows the same layout: a "
             "receipts table, a list of permits, an assessment roll. Spreadsheets and databases are built for "
             "it."),
            ("point", "Unstructured data", "Data without a fixed layout: scanned letters, photos of business "
             "signs, recorded taxpayer complaints, free-written remarks. It holds real information, but it "
             "must be read or sorted before it can be counted."),
            "Some data falls in between. A permit form has fixed fields, such as name and address, and a "
            "remarks field where anything can be written. Treat the fixed fields as structured and the remarks "
            "as unstructured.",
            "A practical rule: if you will need to count or total something, give it its own column with a "
            "type. If a reason for cancellation is written only in remarks, nobody can count cancellations by "
            "reason without reading every line.",
            ("h", "Wide and Long Tables"),
            "Structured data can still come in different shapes. Take the same numbers, collections by "
            "collector for three months, arranged two ways.",
            ("point", "Wide table", "One row per collector, one column per month: Collector, January, February, "
             "March. Three rows of four columns."),
            ("point", "Long table", "One row per collector per month: Collector, Month, Amount. Nine rows of "
             "three columns."),
            "Both hold exactly the same information. They differ in what is easy to do with them.",
            ("point", "Wide is easier to read", "A person can scan across a row and compare months at a glance. "
             "It suits a printed report or a summary for the head of office."),
            ("point", "Long is easier to analyze", "Adding April means adding rows, not a new column, so "
             "formulas and charts keep working. Filters and pivot tables work best with one row per "
             "record."),
            ("h", "When to Use Each Shape"),
            ("point", "Store and analyze in long", "Keep the working data in long form: one row per "
             "receipt, per collector per day, or per collector per month."),
            ("point", "Present in wide", "Turn it into wide form at the end, for the report people will read. "
             "A pivot table does this in a few clicks: put collectors in rows, months in columns and amounts "
             "in values."),
            ("point", "Watch for wide tables that grow", "A sheet that gains a new column every month is a "
             "sign the data should be stored long."),
            ("h", "Turning a Wide Table Into a Long One"),
            "If you receive a wide table, you can reshape it by hand in a few minutes for a small sheet.",
            ("point", "1. Set up the columns", "On a new sheet, type three headers: Collector, Month and Amount."),
            ("point", "2. Copy the first month", "Paste the list of collectors under Collector, their January "
             "amounts under Amount, and type “January” in the Month column beside each one."),
            ("point", "3. Repeat below", "Paste the same collectors again under the January rows, with "
             "February’s amounts and “February” as the month. Do the same for each remaining month."),
            ("point", "4. Check the total", "The sum of the Amount column must equal the sum of all the month "
             "columns in the wide table. If it does not, a row was missed or pasted twice."),
            "For larger tables, Excel’s Power Query has an Unpivot Columns command that does the same "
            "reshaping in one step. Whichever way you use, run the total check at the end.",
            ("h", "A Quick Check Before Any Analysis"),
            "Before you write a single formula, look at each column and answer three questions.",
            ("point", "What type is it?", "Number, text, date or true/false."),
            ("point", "Is it stored as that type?", "Use the alignment and COUNT checks."),
            ("point", "Is the table long or wide?", "If you need to filter or pivot it, make it long first."),
            "Write the answers in the source note from Part 9, so the next person knows the shape before they "
            "start.",
            ("h", "Mistakes to Avoid"),
            ("point", "Typing letters into amounts", "Words like “PHP” turn a number into text. Let the cell "
             "format show the currency."),
            ("point", "Storing codes as numbers", "Leading zeros disappear, and matches fail."),
            ("point", "Hiding countable facts in remarks", "Give anything you will count its own column."),
            ("point", "Analyzing a wide table directly", "Reshape it to long first, or each new month can break your formulas."),
            ("h", "Key Takeaways"),
            ("point", "Type follows use", "Numbers are for arithmetic; codes and IDs are text."),
            ("point", "Check before you sum", "Alignment and COUNT reveal values stored as the wrong type."),
            ("point", "Structure what you will count", "Give countable facts their own typed column."),
            ("point", "Long to analyze, wide to present", "Keep working data long and build wide views for "
             "readers."),
            ("h", "Your Part 10 Exercise"),
            "Open one spreadsheet your office updates every month.",
            ("point", "Types", "For each column, write the type it should be and check that it is stored that "
             "way."),
            ("point", "Shape", "Decide whether the table is wide or long. If a new column appears every month, "
             "sketch the long version."),
            ("point", "Fix one thing", "Correct one column stored as the wrong type, and note the fix."),
            "Then rerun one total you report regularly. If it changes, you have found a number that was wrong "
            "before today.",
            ("cta", "Read: Data Analytics Series, Part 9", "/blog/data-analytics-part-9-where-data-comes-from/"),
            ("cta", "Read: Data Analytics Series, Part 5", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Business Intelligence Series, Part 9", "/blog/business-intelligence-part-9-testing-the-pipeline/"),
            ("ask", "Which column in your office’s spreadsheets is most often stored as the wrong type?"),
        ],
    },
    {
        "date": "December 22, 2026",
        "title": "Data Analytics Series, Part 9: Where Data Comes From, First-, Second- and Third-Party",
        "slug": "data-analytics-part-9-where-data-comes-from",
        "category": "data",
        "summary": "Every data set has a history: who collected it, how, when and why. This part explains "
                   "first-, second- and third-party data with treasury examples, gives six questions to ask "
                   "any source, and shows how to record a source so the next analyst can trust it.",
        "publish_on": "2026-12-22 21:00",
        "body": [
            "The revenue unit wants a list of businesses that may be operating without a permit. The analyst "
            "gathers three files: the office’s own list of permits issued this year, a list of barangay "
            "clearances shared by the barangays, and a business directory downloaded from a website. Any "
            "business in the second or third file but missing from the first goes on the list.",
            "The list has 140 names. In the first week of visits, the team finds that 30 of them closed years "
            "ago, 12 are the same business spelled two ways, and several are branches of businesses that "
            "already hold a permit under the main office’s name. The analysis was done correctly. The trouble "
            "was that the three files were treated as equally reliable, when each had a very different "
            "history.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town, business or taxpayer is described.)",
            "This part begins the Prepare step from Part 2. By the end of this post you will know the three "
            "kinds of data by who collected them, six questions to ask any source, how to combine sources "
            "without creating false matches, and how to write a source note that keeps the history with the "
            "data.",
            ("photo", "blog/data-three-sources.jpg", "Three kinds of data by who collected it: first-party "
             "from your own office, second-party shared by the one who collected it, and third-party "
             "gathered by someone else from other sources. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Three Kinds of Data, by Who Collected It"),
            "One useful way to sort data is by who collected it and how it reached you.",
            ("point", "First-party data", "Data your own office collected from the people it serves, through "
             "its own work. Official receipts, the permits you issued and the taxpayer records you keep are all "
             "first-party data for the treasury."),
            ("point", "Second-party data", "Data another organization collected directly from its own people, "
             "then shared with you. The barangay clearance list in the opening story is an example: the "
             "barangays collected it from businesses and passed it on."),
            ("point", "Third-party data", "Data compiled by someone who did not collect it at the source, "
             "such as a list put together from many other lists. The downloaded business directory is an "
             "example: whoever built it compiled listings from many places, at different times."),
            "The further data travels from the people who collected it, the more questions you need to ask "
            "before relying on it. That is not because second- and third-party data are bad. It is because "
            "you know less about how they were made.",
            ("quote", "Data does not arrive from nowhere. Every file has a history, and the history decides "
             "how far you can trust it."),
            ("h", "Where the Lines Blur"),
            "Inside a local government, the labels can depend on where you stand. The assessor’s office "
            "collects property information directly from owners and keeps the assessment roll. From the "
            "whole local government’s point of view, that is its own data. From the treasury’s desk, it is "
            "data another office collected and shared.",
            "Do not spend long arguing over the label. The label is only a reminder to ask the real question: "
            "who collected this, how, and how much do I know about the way it was made?",
            ("h", "Six Questions to Ask Any Source"),
            ("point", "1. Who collected it?", "An office, a barangay, a private website, a person? Write the "
             "name of the unit and a contact, not just “from the province.”"),
            ("point", "2. How was it collected?", "A form filled in by the taxpayer, encoding by staff, an "
             "inspection, a copy of another list? Each method can introduce different kinds of errors."),
            ("point", "3. When, and how often is it updated?", "A list from January says nothing about "
             "businesses that closed in June. Note the date of the data, not just the date you received it."),
            ("point", "4. Why was it collected?", "Data collected for one purpose may not fit another. A "
             "clearance list shows who asked for a clearance, which is not the same as who is operating "
             "today."),
            ("point", "5. What does each field mean?", "Does “address” mean the business location or the "
             "owner’s home? Does “date” mean the date of application or of approval? Ask before you compare."),
            ("point", "6. May we use it this way?", "Check that sharing and using the data for this purpose is "
             "allowed, especially when it holds personal information. Part 6 covers the Data Privacy Act "
             "principles that apply."),
            "If you cannot answer a question, write that down too. “Collection method unknown” is useful "
            "information for whoever reads the results.",
            ("h", "The Opening Story, Source by Source"),
            ("point", "Permits issued (first-party)", "Collected by the office, at the counter, for this year. "
             "Reliable for who holds a permit, recorded under the name on the application."),
            ("point", "Barangay clearances (second-party)", "Collected by each barangay when a business asked "
             "for a clearance. Shows who applied, not who is still open, and spellings follow each barangay’s "
             "own encoding."),
            ("point", "Business directory (third-party)", "Compiled by an outside website from sources it does "
             "not name, updated at unknown times. Useful for leads, not for conclusions."),
            "Seen this way, the right result was not one list of 140 names. It was a short list of businesses "
            "found in both the barangay list and the directory but not in the permits, to check first, and a "
            "longer list of directory-only names to treat as leads.",
            ("h", "Combining Sources Without False Matches"),
            "Two of the three problems in the opening story came from matching names. Names can change, be "
            "abbreviated or be spelled differently by different people.",
            ("point", "Use a shared code when one exists", "A permit number, a tax declaration number or a "
             "barangay clearance number matches more safely than a business name."),
            ("point", "Clean names the same way on both sides", "When names are all you have, make both lists "
             "uppercase, remove extra spaces and write common words the same way, such as “Sto.” and “Store,” before comparing. Then review close matches by hand."),
            ("point", "Keep the source on every row", "Add a column that says which file each row came from. "
             "When a result looks odd, you can trace it back quickly."),
            ("h", "Write a Source Note"),
            "Keep a short note beside every data set you receive. It keeps the history with the data, so the "
            "next analyst does not have to rediscover it.",
            ("point", "What to write", "Name of the data set, who collected it, the contact person, how it was "
             "collected, the period it covers, the date received, what each unclear field means, and what "
             "it may be used for."),
            ("point", "Where to keep it", "In the same folder as the file, with a matching name, or on the "
             "first sheet of the workbook."),
            ("h", "Mistakes to Avoid"),
            ("point", "Treating every file as equally reliable", "Give more weight to sources you know more "
             "about, and say so in the results."),
            ("point", "Forgetting the date of the data", "The date you downloaded a file is not the date its "
             "information was true."),
            ("point", "Reporting leads as findings", "A name in a third-party directory is a reason to check, "
             "not proof that a business is operating."),
            ("h", "Key Takeaways"),
            ("point", "Three kinds by who collected it", "First-party is your own, second-party is shared by "
             "the collector, and third-party is compiled by someone else."),
            ("point", "Ask six questions", "Who, how, when, why, what each field means, and whether you may "
             "use it."),
            ("point", "Match on codes, not names", "And keep the source of every row."),
            ("point", "Keep a source note", "The history of the data belongs beside the data."),
            ("h", "Your Part 9 Exercise"),
            "Pick one data set your office received from outside your own unit. Answer the six questions for "
            "it, and write the answers as a source note.",
            "Then mark each answer as known or unknown. If more than two are unknown, ask the person who sent "
            "it before you use the data in a report.",
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("cta", "Read: Business Intelligence Series, Part 6", "/blog/business-intelligence-part-6-warehouses-marts-lakes/"),
            ("ask", "Which data set in your office has the least-known history?"),
        ],
    },
    {
        "date": "December 17, 2026",
        "title": "Data Analytics Series, Part 8: Metrics and KPIs That Tell the Truth",
        "slug": "data-analytics-part-8-metrics-and-kpis",
        "category": "data",
        "summary": "Two offices can both report 90% collection efficiency and mean completely different things. "
                   "This part explains the difference between a metric and a KPI, shows how one definition "
                   "can flatter or expose performance, and gives a template for measures that tell the truth.",
        "publish_on": "2026-12-17 21:00",
        "body": [
            "At a provincial meeting, two treasurers compare notes. Both report a real property tax "
            "collection efficiency of 90%. One is quietly proud. The other is worried. They are both right, "
            "because they are not measuring the same thing.",
            "The first divided this year’s collections by this year’s collection target. The second divided "
            "this year’s collections by everything that was actually due, including unpaid taxes from past "
            "years. Same name, same percentage, very different stories about how each office is doing.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town or taxpayer is described.)",
            "Part 7 showed how to name the type of problem behind a request. This part is about the numbers "
            "that answer it. By the end of this post you will know the difference between a metric and a "
            "KPI, the questions that expose a misleading measure, and a template for writing measures that "
            "tell the same truth to everyone who reads them.",
            ("photo", "blog/data-kpi-parts.jpg", "A measure that tells the truth has five parts written down: "
             "its name, numerator, denominator, period and source. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Metric or KPI?"),
            ("point", "Metric", "Any number that measures something: collections today, receipts issued, "
             "taxpayers served, average waiting time. An office can track as many as it finds useful."),
            ("point", "KPI", "A key performance indicator is a metric chosen because it shows progress toward "
             "a goal that matters. Keep the list short, and tie each one to an objective, like the "
             "objectives from the Project Management series."),
            "Every KPI is a metric, but not every metric is a KPI. The test is simple: if this number moved, "
            "would someone change what they do? If not, it is a metric worth keeping, but not a key one.",
            ("h", "One Name, Two Definitions"),
            "Here are the two treasurers’ numbers, worked out.",
            ("point", "Office A: collections against target", "Target for current-year real property tax: "
             "₱10,000,000. Collected: ₱9,000,000. Efficiency: 9,000,000 ÷ 10,000,000 = 90%."),
            ("point", "Office B: collections against amount due", "Current-year tax due: ₱8,000,000. Unpaid "
             "taxes from past years still due: ₱2,000,000. Total due: ₱10,000,000. Collected against all of "
             "it: ₱9,000,000. Efficiency: 90%."),
            "Now look underneath. If Office A’s target was set low, its 90% may hide a large unpaid balance. "
            "Office B’s 90% already counts the old debts, so it says more about how much of what taxpayers "
            "owe is actually coming in.",
            "Neither definition is wrong. Each answers a different question. The danger is reporting either "
            "one under the same name without saying which it is.",
            ("quote", "A percentage without its definition is not a fact. It is half of one."),
            ("h", "Five Parts Every Measure Needs"),
            "Write each KPI down with these five parts, and put the same text wherever the number appears.",
            ("point", "1. Name", "A plain name that says what it is, such as “Current-year RPT collected "
             "against amount due.”"),
            ("point", "2. Numerator", "What is counted on top. For example: current-year real property tax "
             "collected, by official receipt date, excluding cancelled receipts."),
            ("point", "3. Denominator", "What it is divided by. For example: current-year real property tax "
             "due, from the assessment roll as of January 1."),
            ("point", "4. Period", "The time it covers: January to the end of the reporting month."),
            ("point", "5. Source", "Where each part comes from: the collection system for the numerator, the "
             "assessment roll for the denominator."),
            "With these five parts written, two offices, or two people in the same office, can compare their "
            "numbers honestly.",
            ("h", "The Two Treasurers, Rewritten"),
            "Apply the five parts to the opening example, and the confusion disappears before anyone "
            "compares a single percentage.",
            ("point", "Office A", "Name: current-year RPT collected against collection target. Numerator: "
             "current-year tax collected, January to November. Denominator: the target set at the start of the "
             "year. Source: the collection system and the approved target."),
            ("point", "Office B", "Name: RPT collected against total amount due. Numerator: current-year and "
             "past-year tax collected, January to November. Denominator: current-year tax due plus unpaid taxes "
             "from past years. Source: the collection system and the assessment roll."),
            "Side by side, the two names already say that the measures cannot be compared directly. The "
            "provincial meeting could still discuss both, but no one would mistake one office’s 90% for the "
            "other’s.",
            ("h", "Questions That Expose a Misleading Measure"),
            ("point", "Who set the denominator?", "A target is a choice. An amount due is a record. Measures "
             "built on targets can look better simply because the target was modest."),
            ("point", "What is left out?", "Excluding past-year balances, or certain accounts, changes the "
             "story. Say what is excluded."),
            ("point", "Can it improve without real improvement?", "If a number can rise because records "
             "changed rather than because work improved, pair it with a second measure that would catch "
             "that."),
            ("point", "Is the period fair?", "Comparing January to March with a full year, or a month with a "
             "holiday break with one without, can mislead."),
            ("h", "Pairing Measures"),
            "A single number can rise for the wrong reasons. Two measures that pull in different directions "
            "check each other, so a gain in one that hides a loss in the other is easier to spot.",
            ("point", "Collections with arrears", "Collections against amount due, paired with the total of "
             "unpaid balances older than one year. One rises when work improves; the other should fall."),
            ("point", "Speed with accuracy", "Average waiting time at the window, paired with the number of "
             "receipts cancelled for errors. Faster service should not mean more mistakes."),
            "Part 3 of the Business Intelligence series made the same point for dashboards: watch amounts "
            "with arrears, and speed with shortages.",
            ("h", "Leading and Lagging KPIs"),
            "A lagging KPI reports a result after it has happened, such as collection efficiency for the year. "
            "A leading KPI moves earlier and gives time to act, such as the number of large accounts not yet "
            "reminded by the end of the first quarter.",
            "Keep at least one leading measure beside each lagging one. The lagging number tells you how you "
            "did. The leading one tells you whether you can still change it.",
            ("h", "Showing a KPI on a Report"),
            "A KPI on a page needs more than its value. Show four things together, so the reader does not "
            "have to guess.",
            ("point", "The full name", "Use the written name, not a short label like “efficiency.”"),
            ("point", "The period", "For example: January to November 2026."),
            ("point", "A comparison", "The same measure for the same period last year, computed with the same "
             "definition."),
            ("point", "The definition", "A one-line note under the number, or a link to the written five "
             "parts."),
            "A line such as “Current-year RPT collected against amount due, January to November 2026: 82% "
            "(same period in 2025: 78%)” can be read correctly by someone who was not in the room when the "
            "measure was designed.",
            ("h", "When a Definition Changes"),
            "Sometimes an office decides to change a measure, such as switching from a target to the amount "
            "due. The change may be right, but it breaks the comparison with past reports.",
            "When that happens, recompute the past periods with the new definition if the records allow it. "
            "If they do not, mark the break clearly on every report, with the date the new definition began, "
            "so no one reads a jump in the number as a jump in performance.",
            ("h", "Key Takeaways"),
            ("point", "Keep KPIs few", "A KPI is a metric tied to a goal that someone will act on."),
            ("point", "Write the definition", "Name, numerator, denominator, period and source, every time."),
            ("point", "Same name is not same measure", "Always say what a percentage is divided by."),
            ("point", "Pair and lead", "Pair measures that check each other, and keep a leading measure "
             "beside each lagging one."),
            ("h", "Your Part 8 Exercise"),
            "Pick one percentage your office reports regularly. Write its five parts: name, numerator, "
            "denominator, period and source.",
            "Then ask a colleague to compute it from the same records, using only what you wrote. If their "
            "answer differs from yours, the definition still has a gap. Fix the wording until two people "
            "get the same number.",
            ("cta", "Read: Data Analytics Series, Part 7", "/blog/data-analytics-part-7-six-problem-types/"),
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Project Management Series, Part 6", "/blog/project-management-part-6-writing-objectives/"),
            ("ask", "What does your office divide by when it reports collection efficiency?"),
        ],
    },
    {
        "date": "December 12, 2026",
        "title": "Data Analytics Series, Part 7: Six Kinds of Problems Data Can Solve",
        "slug": "data-analytics-part-7-six-problem-types",
        "category": "data",
        "summary": "A request for “a report” can hide one of several basic problem types. This part walks "
                   "through six of them with treasury examples, so you can name the problem first and pick "
                   "the right method before you open a spreadsheet.",
        "publish_on": "2026-12-12 21:00",
        "body": [
            "Three requests reach the analyst in one morning. The head of office asks, “Will we hit the "
            "target this year?” The cashier asks, “Why did yesterday’s deposit not match the collections?” "
            "The revenue unit asks, “Can you group the businesses so we know who to visit first?”",
            "All three are called “a report.” They are really three different kinds of problems, and each "
            "needs a different approach. An analyst who treats them all the same can end up building three "
            "tables and answering none of the questions.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "The Google Data Analytics Certificate groups the questions analysts meet into six common problem "
            "types. Naming the type is the first move of the Ask step from Part 2, because the type tells you "
            "what data you need and what method to use. By the end of this post you will be able to recognize "
            "all six in your own office’s requests and know where to start with each.",
            ("photo", "blog/data-six-problems.jpg", "Six common problem types: making predictions, categorizing "
             "things, spotting something unusual, identifying themes, discovering connections and finding "
             "patterns. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "1. Making Predictions"),
            "The question is about the future: what is likely to happen? “Will we hit the collection target "
            "this year?” is a prediction problem.",
            ("point", "What you need", "Past data for the same measure over several periods, and a way to "
             "describe how the current period compares."),
            ("point", "Where to start", "Part 4 projected a year-end total from the share collected by "
             "October in past years. Simple methods like that are a good first step, as long as the answer is "
             "shown as a range."),
            ("h", "2. Categorizing Things"),
            "The question is about sorting items into groups by their features. “Group the businesses so we "
            "know who to visit first” is a categorizing problem.",
            ("point", "What you need", "A list of items, each with the features that matter: amount owed, "
             "months overdue, type of business, barangay."),
            ("point", "Where to start", "Agree on the groups and the rules first, for example: owes more than "
             "₱10,000 and overdue more than six months goes to the first visit list. Write the rule down so "
             "anyone can repeat it."),
            ("h", "3. Spotting Something Unusual"),
            "The question is about what does not fit the normal pattern. “Why did yesterday’s deposit not "
            "match the collections?” starts as this kind of problem: first find what is unusual, then explain "
            "it.",
            ("point", "What you need", "A clear idea of normal: the usual daily range, the usual difference "
             "between collections and deposits (ideally zero), the usual number of cancelled receipts."),
            ("point", "Where to start", "Compare each day with that normal and list the days, collectors or "
             "receipts that fall outside it. The list is not an accusation. It is where to look first."),
            ("h", "4. Identifying Themes"),
            "The question is about grouping categories into a few broader ideas. It fits comments and "
            "complaints well.",
            "Suppose the office has two hundred written comments from taxpayers at the counter. Reading them "
            "one by one gives impressions. Sorting them first into categories, such as long line, no seats, "
            "slow lookup of past payments, wrong amount and unclear wording, and then grouping those into "
            "themes, such as the waiting experience and the bill itself, turns them into evidence.",
            ("point", "How it differs from categorizing", "Categorizing places each item in a group. "
             "Identifying themes goes one level up and groups the categories into broader ideas."),
            ("h", "5. Discovering Connections"),
            "The question is about finding links between things that are usually looked at separately, often "
            "by combining data from different sources or offices.",
            "For example, the treasury has payment records and the assessor’s office has the property "
            "records. Joined by a common property number, they can show which properties have never had a "
            "recorded payment. Neither office can see that from its own records alone.",
            ("point", "What you need", "A shared key, such as a property number, and an agreement between "
             "the offices on how the combined data may be used."),
            ("h", "6. Finding Patterns"),
            "The question is about what repeats over time. “When during the year do business tax payments "
            "come in?” is a pattern problem.",
            "Under the Local Government Code, business taxes may be paid in quarterly installments within the "
            "first twenty days of January and of each following quarter. A chart of daily collections across "
            "several years will show whether payments in your office bunch up near those dates, which is useful for planning staff at the windows. Put two or three past years side by side, so a one-time spike is not mistaken for a pattern.",
            ("point", "How it differs from prediction", "Finding patterns describes what has repeated. "
             "Prediction uses that knowledge to estimate a specific future value."),
            ("quote", "Name the problem before you touch the data. The type of question decides the type of "
             "answer."),
            ("h", "When a Request Combines Types"),
            "The cashier’s deposit question starts as spotting something unusual, then becomes a "
            "connection problem when the analyst joins the receipts with the deposit slips to find which "
            "receipts were not deposited. The head of office’s target question needs patterns first, then a "
            "prediction.",
            "Naming the types in order gives you a plan: first this, then that. It also helps you explain to "
            "the person who asked why the answer will take two steps, not one.",
            ("h", "Turning a Vague Request Into a Typed Question"),
            "A request does not arrive with a type attached. Suppose the head of office says, “Give me some numbers on "
            "business permits.” Before opening any file, the analyst asks three follow-up questions.",
            ("point", "What decision is this for?", "“I want to know whether we need extra staff for the renewal "
             "period.” That points to timing."),
            ("point", "What would a useful answer look like?", "“Which weeks are busiest, and how busy.” That is a "
             "pattern problem: what repeats each year."),
            ("point", "Is anything else behind it?", "“Last January some renewals were very late.” That adds a second "
             "type: spotting something unusual, namely which businesses renewed late and whether they share "
             "features."),
            "The vague request has become two typed questions in a clear order: find the weekly pattern of "
            "renewals over past years, then list the late renewals and look at what they have in common. Each "
            "has its own data and its own method, and the head of office can see exactly what will be delivered.",
            "This short conversation also protects the analyst’s time. Without it, the result can be a long table of permit counts that answers nobody’s real question.",
            ("h", "A Quick Guide"),
            ("point", "“What will happen?”", "Making predictions."),
            ("point", "“Which group does each one belong to?”", "Categorizing things."),
            ("point", "“What doesn’t look right?”", "Spotting something unusual."),
            ("point", "“What are people telling us, overall?”", "Identifying themes."),
            ("point", "“How does this relate to that?”", "Discovering connections."),
            ("point", "“What keeps happening?”", "Finding patterns."),
            ("h", "Key Takeaways"),
            ("point", "Name the type first", "The problem type tells you what data and method you need."),
            ("point", "Categories versus themes", "Categories sort the items; themes group the categories "
             "into bigger ideas."),
            ("point", "Patterns versus predictions", "Patterns describe what repeats; predictions estimate "
             "what comes next."),
            ("point", "Some requests combine types", "Write the types in order and you have a plan."),
            ("h", "Your Part 7 Exercise"),
            "Collect the last five requests your office received for “a report” or “some numbers.” For each "
            "one, write:",
            ("point", "The question", "In one sentence, as the person asked it."),
            ("point", "The type or types", "Which of the six does it belong to, and in what order?"),
            ("point", "The data needed", "Which records would answer it, and does the office already keep "
             "them?"),
            "If a few types come up again and again, those are the ones worth building a routine for.",
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("ask", "Which of the six problem types does your office ask about most often?"),
        ],
    },
    {
        "date": "December 7, 2026",
        "title": "Data Analytics Series, Part 6: Data Ethics and the Data Privacy Act for Analysts",
        "slug": "data-analytics-part-6-data-ethics-privacy",
        "category": "data",
        "summary": "Analysts handle other people’s information every day. This part explains the three privacy "
                   "principles of the Data Privacy Act in plain words, shows how a harmless-looking chart can "
                   "still reveal a person, and gives a checklist to run before any analysis leaves your desk.",
        "publish_on": "2026-12-07 21:00",
        "body": [
            "The analyst is proud of the new chart: business tax collections by barangay, by type of "
            "business, for the whole year. It goes into the monthly report and onto the bulletin board.",
            "A week later, a store owner comes to the office, upset. In her barangay there is only one "
            "hardware store, hers. The chart shows exactly how much the hardware stores in that barangay paid. "
            "Anyone who reads the bulletin board now knows what her business paid, and from that, roughly how much it sells, since business tax is based on gross sales. No name appeared on the chart. It still pointed to one person.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 5 touched on privacy when choosing tools. This part goes further, because analysts make "
            "privacy decisions every time they choose what to collect, what to keep and what to show. By the "
            "end of this post you will know the three principles the Data Privacy Act asks every analysis to "
            "follow, the ways a report can expose a person without naming them, and a short checklist to run "
            "before you share any result.",
            ("photo", "blog/data-privacy-principles.jpg", "The three general privacy principles of the Data "
             "Privacy Act: transparency, legitimate purpose and proportionality. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Ethics Comes Before the Law"),
            "Data ethics asks a simple question: is this use of other people’s information fair to them? The "
            "law sets the minimum. Ethics asks whether you would be comfortable if the people in your data "
            "saw exactly what you did with it.",
            "In the Philippines, the minimum is the Data Privacy Act of 2012 (Republic Act No. 10173) and its "
            "implementing rules, overseen by the National Privacy Commission. It applies to government offices "
            "as well as private companies.",
            ("h", "The Three Principles in Plain Words"),
            "The law says that processing personal information must follow three general principles. Its "
            "implementing rules explain each one.",
            ("point", "Transparency", "The people in the data should know the nature, purpose and extent of "
             "what is done with their information. For an analyst, this means not using data in ways the "
             "office never told people about."),
            ("point", "Legitimate purpose", "Processing must fit a declared and specified purpose that is not "
             "against the law, morals or public policy. Data collected to issue a business permit is not "
             "automatically fair to use for something unrelated."),
            ("point", "Proportionality", "Processing must be adequate, relevant, suitable, necessary and not "
             "excessive for that purpose. If totals answer the question, use totals, not names."),
            "Put together, the three principles give an analyst a daily habit: before using a column, ask "
            "whether people were told, whether this use fits the reason it was collected, and whether you "
            "need it at all.",
            ("h", "Some Information Needs Extra Care"),
            "The law treats some information as sensitive personal information. It includes a person’s age, "
            "marital status, health, education, religious or political affiliations, and numbers issued by "
            "the government that are specific to the person, such as social security numbers and tax "
            "returns.",
            "Treasury records can contain some of these, especially government-issued numbers and details "
            "drawn from tax filings. Treat any column like that as off limits for analysis unless the purpose "
            "truly needs it and your office has approved its use.",
            ("h", "How a Report Can Point to One Person"),
            "The story at the start shows the trap. Removing names is not always enough. A report can still "
            "point to a person when:",
            ("point", "A group is very small", "If a category has only one or two members, its total is "
             "really their total. Merge small groups into a larger one, or show “fewer than five” instead of "
             "the exact figure."),
            ("point", "Details can be combined", "A barangay, a type of business and a year may each seem "
             "harmless. Together they can narrow a list down to one taxpayer."),
            ("point", "Rows are shared instead of results", "Sending a spreadsheet of individual records "
             "when only a summary was asked for exposes more than the question needed."),
            "The law itself recognizes the difference. Its rules allow personal data to be kept longer when it "
            "is aggregated or kept in a form that does not permit identification of the people in it. Shaping "
            "results so no one can be singled out protects people, and the rules treat such data differently.",
            ("quote", "Ask not only “Did I remove the names?” but “Could anyone still find the person?”"),
            ("h", "Ethics Beyond Privacy"),
            "Privacy is the part the law spells out. Ethical analysis also covers how results are presented.",
            ("point", "Honest charts", "Start bar charts at zero, label every axis, and do not hide a bad "
             "month by choosing a flattering time range."),
            ("point", "Fair comparisons", "Before ranking barangays or collectors, check whether they faced "
             "the same conditions. A low number may reflect a smaller area, not a weaker effort."),
            ("point", "Clear uncertainty", "Say when a cause is only likely, as Part 4 did, and show forecasts "
             "as ranges."),
            ("h", "People Have Rights Over Their Data"),
            "The implementing rules list rights that every data subject holds. Among them: the right to be "
            "informed, to object, to access their data, to have errors corrected, to have data blocked or "
            "erased on certain grounds, to damages, and, where data is processed electronically, to get a copy "
            "in a commonly used format.",
            "For an analyst, the right to correction has the most direct effect on daily work. If a taxpayer proves that a record is "
            "wrong, the fix must reach every copy, including the data you pulled for analysis last month.",
            ("h", "When Something Goes Wrong"),
            "Mistakes happen: a file is emailed to the wrong person, a laptop is lost, a shared folder is left "
            "open. Report it to your data protection officer at once.",
            "Under NPC Circular 16-03, when a reportable personal data breach happens, the office must notify "
            "the National Privacy Commission, and the affected people, within 72 hours of knowing about it. "
            "That clock only works if staff speak up quickly, so a culture where people report mistakes "
            "without fear is part of good data practice.",
            ("h", "Keep Working Copies Under Control"),
            "Analysis creates copies: an export for this report, a cleaned version, a version emailed for checking. "
            "Each copy is one more place where personal data can leak.",
            ("point", "Work from one approved location", "Keep working files in the folder or system your office has "
             "approved, not on a personal laptop, phone or private email."),
            ("point", "Strip what you do not need early", "Remove names, addresses and identification numbers in the "
             "first step if the question does not need them. Later copies are then safer by default."),
            ("point", "Delete when done", "When the report is final, delete the extra working copies and note in "
             "your notes file that you did."),
            ("h", "Before You Share: A Checklist"),
            ("point", "Purpose", "Does this analysis fit the reason the data was collected?"),
            ("point", "Minimum data", "Did I use only the columns the question needs?"),
            ("point", "Small groups", "Does any figure describe fewer than five people or businesses?"),
            ("point", "Combinations", "Could two or three details together point to one person?"),
            ("point", "Format", "Am I sharing results, not raw rows?"),
            ("point", "Storage", "Is my working copy saved only where the office allows, and will I delete "
             "it when the work is done?"),
            ("h", "Key Takeaways"),
            ("point", "Three principles", "Transparency, legitimate purpose and proportionality guide every "
             "use of personal data."),
            ("point", "No names is not enough", "Small groups and combined details can still identify a "
             "person."),
            ("point", "Share results, not rows", "Aggregated data protects people, and the rules allow it to be kept longer."),
            ("point", "Report mistakes fast", "Breach notice to the National Privacy Commission runs on a "
             "72-hour clock."),
            ("h", "Your Part 6 Exercise"),
            "Take the last report you shared and run the checklist above on it, line by line.",
            "Mark any figure that describes fewer than five people or businesses, and any table that could be "
            "a summary instead of a list. Fix one of them in the next edition. That single change is a real "
            "improvement in how your office treats the people behind its numbers.",
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("cta", "Read: Data Analytics Series, Part 5", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Cybersecurity Series, Part 6", "/blog/cybersecurity-part-6-cloud-and-privacy/"),
            ("ask", "Which figure in your office’s reports describes a group so small it could point to one person?"),
        ],
    },
    {
        "date": "December 2, 2026",
        "title": "Data Analytics Series, Part 5: The Analyst’s Toolkit on a Zero Budget",
        "slug": "data-analytics-part-5-zero-budget-toolkit",
        "category": "data",
        "summary": "No software budget is no excuse. This part lays out a complete analytics toolkit that costs "
                   "nothing to start: spreadsheets, a small database, Python, a free dashboard builder and a "
                   "plain notes file, with what each is good for and where each stops.",
        "publish_on": "2026-12-02 21:00",
        "body": [
            "The revenue clerk finishes an online course in data analytics and comes back to the office full "
            "of ideas. Then she checks the budget. There is no line for analytics software, and the next "
            "chance to add one is a year away. She decides the ideas will have to wait.",
            "They do not have to wait. Every step of the analysis process in this series can be done with "
            "tools that cost nothing to start. What they ask for instead is time to learn and care in how "
            "they are used.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "In Part 4, a whole analysis was done in a spreadsheet. This part widens the view to five kinds "
            "of free tools, what each one is good for, and where each one stops. By the end of this post you "
            "will be able to pick the right free tool for a task, know the limits to watch for, and set up a "
            "starter kit on your own computer this week.",
            ("photo", "blog/data-zero-budget-toolkit.jpg", "Five kinds of free tools cover the whole analysis: "
             "spreadsheets, a small database, Python, a dashboard builder and a notes file. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "First, the Question"),
            "A tool cannot rescue a vague question. Part 2 started every analysis with the Ask step for a "
            "reason. Before opening any program, write the question in one sentence, name who will use the "
            "answer, and name the decision it supports. The cheapest tool that answers that question well is "
            "the right tool.",
            ("h", "1. Spreadsheets: The Place to Start"),
            "A spreadsheet is a quick way to look at a few thousand rows, add them up and spot "
            "something odd. Two free options are worth knowing.",
            ("point", "Google Sheets", "Free with a Google account and runs in a web browser. A single "
             "spreadsheet can hold up to 10 million cells."),
            ("point", "LibreOffice Calc", "Part of the free, open-source LibreOffice suite. It runs on the "
             "computer itself, so it works without an internet connection. Recent versions allow 1,048,576 "
             "rows in a sheet."),
            "Both have the tools used in Part 4: SUMIFS for totals with conditions, sorting and filtering, "
            "and pivot tables for quick summaries.",
            ("point", "Where it stops", "When the file gets slow, when the same cleaning steps must be "
             "repeated by hand every month, or when several people edit the same copy and nobody knows which "
             "version is right."),
            ("h", "2. A Small Database: SQLite"),
            "When the records outgrow a spreadsheet, the next step does not need a server. SQLite keeps a "
            "whole database in one ordinary file. Its authors have dedicated the code to the public domain, "
            "so anyone may use it for free.",
            "Python’s standard library includes a module for SQLite, so a standard Python installation can use it with nothing extra to install. For "
            "people who prefer clicking to typing, DB Browser for SQLite is a free, open-source program that "
            "lets you open the file, browse the tables and run SQL queries in a window.",
            "SQL is worth learning for one reason above all: a query is written down. Next month you run the "
            "same query on new data and get an answer built exactly the same way.",
            ("point", "Where it stops", "SQLite allows only one writer at a time per database file. That suits "
             "one analyst well. When many staff must enter records at the same moment all day, a server-based "
             "database is the better fit."),
            ("h", "3. Python: For Work You Repeat"),
            "Python is free to download and use. With the pandas library, which is also free and open source, "
            "a monthly report that takes an afternoon of copying and pasting can become a script that you run with one command and that gives the same result every time.",
            "The real gain is not speed. It is that every step is recorded. Anyone can read the script and "
            "see exactly how a number was produced, which makes the work easier to check and easier to hand "
            "over.",
            ("point", "Where it stops", "It takes practice before it saves time. Start with one "
             "report you prepare every month, not with the hardest problem in the office."),
            ("h", "4. Dashboards: Sharing the View"),
            "When the same numbers are needed by several people every week, a dashboard saves everyone from "
            "asking. Two free options are worth knowing.",
            ("point", "Data Studio", "Google’s web-based report builder, called Looker Studio until April "
             "2026. It has a no-cost tier, reads directly from Google Sheets, and shares a report through a "
             "link, the same way a document is shared."),
            ("point", "Power BI Desktop", "A free download from Microsoft for Windows computers. It is strong "
             "at linking several tables into one model, the topic of the Business Intelligence series. "
             "Building is free; sharing reports with others through Microsoft’s online service needs a paid "
             "license."),
            ("point", "Where it stops", "A dashboard only repeats what the data says. If the source sheet is "
             "wrong or late, the dashboard is wrong or late too, just in a nicer layout."),
            ("h", "5. A Notes File: The Tool That Makes Work Checkable"),
            "The last tool costs nothing and matters as much as the others: a plain text file or a simple document kept beside the data. For "
            "each analysis, write the question, where the data came from and on what date, every cleaning "
            "step, and any assumption you made.",
            "This file is what lets someone else check your work, and it is what lets you repeat the "
            "analysis next year without starting over. It costs nothing, and it is the first thing to reach "
            "for when someone questions a number.",
            ("quote", "Free tools lower the cost of starting. They do not lower the standard of the work."),
            ("h", "Free Is Not the Same as Safe"),
            "Free cloud tools keep your files on another company’s computers. Treasury records hold "
            "taxpayers’ names, addresses and payment details, which are protected under the Data Privacy Act "
            "of 2012 (Republic Act No. 10173).",
            "Before you upload anything, check your office’s rules on cloud services and ask your data "
            "protection officer. A safe habit is to work with totals, or to replace names with codes, before "
            "the data leaves the office computer. The collection analysis in Part 4, for example, needed only "
            "the amounts, the dates and the areas, not anyone’s name.",
            ("h", "What Free Tools Still Cost"),
            "Free software saves the license fee, not the effort. Three costs remain, and it helps to name them "
            "before you begin.",
            ("point", "Learning time", "Set aside a regular hour each week, with your head of office’s approval, "
             "so learning is part of the job rather than an after-hours hobby."),
            ("point", "A connection", "Browser-based tools need a working internet connection. Keep an offline "
             "copy of anything you need at the counter or in a meeting."),
            ("point", "Continuity", "If only one person knows how a script or a dashboard works, the office "
             "depends on that person. The notes file and a short handover session protect the work when people "
             "move to other posts."),
            ("h", "Which Tool for Which Job"),
            ("point", "A one-time total or a quick check", "A spreadsheet."),
            ("point", "Many months of records, asked the same questions again and again", "SQLite with saved "
             "queries."),
            ("point", "A monthly report built the same way every time", "A Python script."),
            ("point", "Numbers several people need to see every week", "A free dashboard builder."),
            ("point", "Every analysis, without exception", "A notes file."),
            ("h", "Key Takeaways"),
            ("point", "Start with the question", "The right tool is the cheapest one that answers it well."),
            ("point", "Know where each tool stops", "Move to the next tool when the current one gets slow, "
             "manual or confusing, not before."),
            ("point", "Write every step down", "A query, a script or a notes file makes your work checkable and "
             "repeatable."),
            ("point", "Protect personal data", "Use totals or codes before anything goes to a cloud service."),
            ("h", "Your Part 5 Exercise"),
            "Set up a starter kit this week:",
            ("point", "Install one offline tool", "LibreOffice, or Python if your office allows it."),
            ("point", "Rebuild one report", "Take a report you already prepare by hand and rebuild it once, "
             "using totals only, with no names."),
            ("point", "Start the notes file", "Write the question, the source, the date and each step. Keep it "
             "next to the data."),
            "Next month, run the same report again and compare how long it took. That difference is the first "
            "return on a toolkit that cost nothing.",
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Keep a receipts register in SQLite", "/tutorials/receipts-register-with-sqlite/"),
            ("ask", "Which report in your office would you rebuild first with free tools?"),
        ],
    },
    {
        "date": "November 27, 2026",
        "title": "Data Analytics Series, Part 4: Four Questions, One Data Set, Worked End to End",
        "slug": "data-analytics-part-4-four-questions-worked",
        "category": "data",
        "summary": "What happened, why, what is likely and what should we do? This part takes one made-up set of "
                   "real property tax records and answers all four questions in order, with every number "
                   "shown, so you can see how each answer builds on the last.",
        "publish_on": "2026-11-27 21:00",
        "body": [
            "“How are we doing, and what should we do in the last two months?” The head of office asks it at the November meeting, and the room goes quiet. Everyone has a feeling about the answer. Nobody has the answer.",
            "In Part 1, I introduced four kinds of analysis: descriptive, diagnostic, predictive and prescriptive. Definitions are easy to remember and hard to use, so this part puts them to work. It takes one small set of records and answers all four questions in order, with every number shown. By the end you will see how each answer feeds the next, and you will have a four-line routine to try on your own reports.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town or taxpayer is described. The arithmetic, however, is real, so you can check every step.)",
            ("photo", "blog/data-four-questions.jpg", "Four questions asked of one data set, in order: describe "
             "what happened, diagnose why, predict what is likely, and prescribe what to do. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Situation"),
            "A municipal treasury has a real property tax collection target of ₱12,000,000 for the year. It is early November, and the question from the meeting is waiting for an answer.",
            "The analyst has the office’s collection records from January to October of this year and the same "
            "records for the past three years. That is all. No new survey, no special software. A spreadsheet "
            "is enough.",
            ("h", "Question 1, Descriptive: What Happened?"),
            "Start by adding up what was collected, by period, and compare it with the same period last year.",
            ("point", "This year, January to October", "First quarter ₱4,200,000; second quarter ₱1,900,000; "
             "third quarter ₱1,500,000; October ₱800,000. Total ₱8,400,000."),
            ("point", "Against the target", "₱8,400,000 is 70% of the ₱12,000,000 target."),
            ("point", "Against last year", "The same ten months last year brought in ₱8,900,000. This year is "
             "₱500,000 lower, a drop of about 5.6%."),
            "That is the descriptive answer, and it is already useful. The office is behind last year, and it "
            "has 30% of its target left to collect in two months. But a total does not say where the money went "
            "missing, so the next question follows naturally.",
            ("h", "Question 2, Diagnostic: Why Did It Happen?"),
            "A drop in a total can come from anywhere. The analyst breaks the same numbers down by area and "
            "compares each part with last year.",
            ("point", "Town-center barangays", "₱5,600,000 this year against ₱5,550,000 last year. Up ₱50,000."),
            ("point", "Coastal barangays", "₱1,450,000 against ₱2,000,000. Down ₱550,000, or 27.5%."),
            ("point", "Upland barangays", "₱1,350,000 against ₱1,350,000. No change."),
            "The parts add up: ₱5,600,000 plus ₱1,450,000 plus ₱1,350,000 is ₱8,400,000, and the changes, plus "
            "₱50,000, minus ₱550,000 and zero, explain the whole ₱500,000 drop. Almost all of it is in the "
            "coastal barangays.",
            "Now the analyst asks the people who know the ground. The collectors explain that last year the "
            "office held six roving collection days in the coastal barangays during the third quarter. This "
            "year it held only two, because the service vehicle was under repair.",
            "Is that the cause? It is a strong lead, not yet proof. The timing fits, the place fits and the "
            "size is plausible. A careful analyst says exactly that: “The drop is concentrated in the coastal "
            "barangays, and it matches the reduced roving collection days. Other causes are possible, but this "
            "one fits the evidence best.”",
            ("h", "Question 3, Predictive: What Is Likely to Happen?"),
            "The head of office now wants to know where the year will end. The analyst looks at the past three "
            "years and asks: by the end of October, what share of the full year’s collection had usually come "
            "in?",
            ("point", "The past three years", "81%, 80% and 82% of each year’s total had been collected by the "
             "end of October."),
            ("point", "The projection", "If this year follows the same pattern, the full-year total is "
             "₱8,400,000 divided by that share. At 82%, that is about ₱10,240,000. At 80%, about ₱10,500,000. "
             "At the middle value of 81%, about ₱10,370,000."),
            ("point", "Against the target", "The likely year-end range of ₱10.2 to ₱10.5 million leaves a "
             "shortfall of roughly ₱1.5 to ₱1.8 million against the ₱12,000,000 target."),
            "Notice two things. First, the forecast is a range, not a single number. Three years of history is "
            "not much, and an honest forecast shows its uncertainty. Second, the forecast assumes nothing "
            "changes. Its real value is to show what will happen if the office does nothing different, which "
            "is exactly what the last question is about.",
            ("h", "Question 4, Prescriptive: What Should We Do?"),
            "Prescriptive analysis compares possible actions by their likely effect. The analyst lists two "
            "options, using the office’s own past results.",
            ("point", "Option A: restore roving days", "Last year, each roving collection day in the coastal "
             "barangays brought in about ₱90,000 on average. Four extra days in November and December could "
             "bring in about ₱360,000."),
            ("point", "Option B: letters to the largest delinquent accounts", "Last year, a similar round of "
             "letters to 40 accounts led about one in four to pay, at an average of ₱15,000 each. The same "
             "result this year would be about 10 payments, or ₱150,000."),
            ("point", "Both together", "About ₱510,000, if the past results hold."),
            "Then comes the uncomfortable part, which a good analyst does not hide. Even both options together would close only about a third of the smaller ₱1.5 million gap. The recommendation therefore has three "
            "lines: restore the roving days, send the letters, and tell the local chief executive and the "
            "budget office now that the year is likely to end below target, so they can plan for it.",
            ("quote", "A good recommendation tells people what to do and what it will not fix."),
            ("h", "How the Four Answers Fit Together"),
            "Look back at the chain. The descriptive answer showed a gap. The diagnostic answer found where it "
            "was. The predictive answer showed how big it would become if nothing changed. The prescriptive "
            "answer compared actions and was honest about their limits.",
            "Skip any link and the chain breaks. Without the diagnosis, the office might have sent letters "
            "everywhere instead of fixing the coastal schedule. Without the forecast, nobody would have known "
            "that the gap was too big to close, and the shortfall would have been a surprise in January.",
            ("h", "Doing It in a Spreadsheet"),
            "None of this needs special software. With one table of payments, where each row has a date, an "
            "area and an amount, the whole analysis takes four small steps.",
            ("point", "Totals by period", "Use SUMIFS to add the amounts between two dates, once for this year "
             "and once for last year."),
            ("point", "Totals by area", "Use SUMIFS again, with the area as a second condition. A pivot table "
             "does the same job in a few clicks."),
            ("point", "The projection", "Divide this year’s total so far by each past year’s October share. "
             "Show the smallest and largest results as the range."),
            ("point", "The options", "Multiply each past result by the planned number of days or letters, "
             "and write the assumption next to the answer."),
            "Keep each step on its own sheet, with a short note at the top saying what it does. Anyone in the "
            "office can then follow the work and check it, which matters as much as the result.",
            ("h", "What to Check Before You Present"),
            ("point", "Do the parts add up to the whole?", "Here, the three areas add up to ₱8,400,000 and the "
             "changes add up to the ₱500,000 drop. If they do not, something is missing or counted twice."),
            ("point", "Are the periods the same?", "Compare January to October with January to October, not "
             "with a full year."),
            ("point", "Is the cause confirmed or only likely?", "Say which one, in plain words."),
            ("point", "Is the forecast a range?", "A single number suggests more certainty than the data gives."),
            ("h", "Key Takeaways"),
            ("point", "Each answer feeds the next", "Describe the gap, find where it is, size it, then choose what to do."),
            ("point", "Say how sure you are", "A likely cause is not a proven one, and a forecast is a range, not a single number."),
            ("point", "Tell people what will not be fixed", "An honest recommendation lets the office plan for the shortfall early."),
            ("h", "Your Part 4 Exercise"),
            "Take any total your office reports every month. Then try the four questions on it, one line each:",
            ("point", "Describe", "What was the total, and how does it compare with the same period last year?"),
            ("point", "Diagnose", "Break it into two or three parts. Which part explains most of the change?"),
            ("point", "Predict", "Using past years, where is it likely to end, as a range?"),
            ("point", "Prescribe", "Name one action, its likely effect, and what it will not fix."),
            ("cta", "Read: Data Analytics Series, Part 3", "/blog/data-analytics-part-3-deciding-with-data/"),
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("ask", "Which of the four questions does your office usually skip?"),
        ],
    },
    {
        "date": "November 22, 2026",
        "title": "Data Analytics Series, Part 3: Deciding With Data, Not Hunches",
        "slug": "data-analytics-part-3-deciding-with-data",
        "category": "data",
        "summary": "Experience and data are not rivals. Here is what a data-driven decision really looks like in a "
                   "local treasury, five ways analysts think before they touch a formula, and the traps that turn "
                   "good numbers into bad choices.",
        "publish_on": "2026-11-22 21:00",
        "body": [
            "Every December, a treasury holds the same short meeting. Should the office open on "
            "the Saturday before the business tax deadline? Business taxes are due within the "
            "first twenty days of January, and every year the last few days bring long lines.",
            "One senior collector is sure it is worth it. “People always come on Saturdays.” A "
            "clerk is just as sure it is not. “Last time we opened, the room was half empty by "
            "ten.” The head of office has to approve overtime and keep the vault staffed either "
            "way. Two experienced people, two opposite hunches, one decision.",
            "(As always in this series, the office, the people and the numbers are made up. No "
            "real town or taxpayer is described.)",
            "This part is about what happens next in an office that thinks like an analyst. It is"
            " not about fancy tools. It is about a habit: checking what the records say before "
            "deciding, and being honest about what they cannot say. By the end of this post, you "
            "will know how to weigh experience against records, five thinking habits analysts "
            "use, the traps that spoil good data, and how to write a short decision note.",
            ("h", "What “Data-Driven” Really Means"),
            "A data-driven decision is one where evidence, gathered and checked with care, "
            "carries real weight in the choice. It does not mean the spreadsheet decides. People "
            "still decide. The data simply makes sure they are arguing about facts instead of "
            "memories.",
            "Some practitioners prefer the phrase data-inspired, and the difference is useful. A "
            "data-driven choice follows closely from a clear analysis. A data-inspired choice "
            "uses data to spark ideas or test a hunch, while leaving room for things the numbers "
            "cannot measure, such as goodwill with taxpayers or the morale of a tired staff. A "
            "decision can land somewhere in between, and that is fine as long as everyone knows "
            "which is which.",
            ("h", "Experience Is Data Too"),
            "The senior collector’s hunch is not worthless. Years at the counter are a kind of "
            "data, stored in a person instead of a table. The trouble is that one person sees "
            "only part of the picture, and a single memorable day can stand in for many ordinary "
            "ones.",
            "The best decisions use both. Experience suggests what to look at and what might "
            "explain it. Records show whether the pattern is real, how big it is and whether it "
            "has changed. When the two disagree, that is not a crisis. It is the most interesting"
            " moment in the whole analysis.",
            ("h", "Back to the Saturday Question"),
            "Here is how the office could settle it in an afternoon.",
            ("point",
             "Ask the real question",
             "Not “Do people come on Saturdays?” but “Would a Saturday opening in mid-January "
             "serve enough taxpayers to justify the cost, and would it shorten the lines on the "
             "last weekdays?”"),
            ("point",
             "Look at the records",
             "The office pulls the business tax receipts from the past three Januaries and counts"
             " them by date of payment. In the one year it opened on a Saturday, it has that "
             "day’s count too."),
            ("point",
             "Read the pattern",
             "Suppose the counts show that the Saturday opening served 140 taxpayers, almost all "
             "before eleven, and that the following Monday was about 20% lighter than the same "
             "Monday in other years. Both hunches were partly right: people did come, but only in"
             " the morning."),
            ("point",
             "Decide, then measure again",
             "Open on that Saturday, but only from eight to noon, and count again next January to"
             " see whether the result holds."),
            "Neither the collector nor the clerk lost the argument. The decision is better than "
            "either hunch, and it costs less than a full day.",
            ("h", "Five Ways an Analyst Thinks"),
            "Before typing a single formula, good analysts use a handful of thinking habits. You "
            "may already use some of them without naming them.",
            ("photo",
             "blog/data-analyst-thinking.jpg",
             "Five thinking habits that come before any formula: see it, plan it, frame it, "
             "connect it, and zoom between the whole and the part. (Illustration: Butch Mahinay, "
             "aumahinay.dev)",
             "medium"),
            ("point",
             "See it",
             "Picture the data before you calculate. A quick chart of receipts by day often "
             "answers the question faster than a table."),
            ("point",
             "Plan it",
             "Decide what you will do and in what order: which records, which period, which "
             "comparison. A plan keeps you from wandering."),
            ("point",
             "Frame it",
             "Keep the problem at the center. Every step should help answer the question that was"
             " asked, not a more interesting one."),
            ("point",
             "Connect it",
             "Look for links between things. Do long lines on the last day go with a slow first "
             "week? Remember that a link is not proof that one causes the other."),
            ("point",
             "Zoom in and out",
             "Move between the big picture and the details. The total for January matters, and so"
             " does the single day when the system was down."),
            ("h", "Traps That Spoil Good Data"),
            "Data does not protect you from bad decisions on its own. These traps can catch even "
            "experienced people.",
            ("point",
             "Looking only for support",
             "If you already believe Saturdays are busy, you will notice the one busy Saturday "
             "and stop looking. Decide what evidence would change your mind before you look."),
            ("point",
             "Trusting the loudest story",
             "One angry complaint can feel bigger than a hundred quiet payments. Count before you conclude."),
            ("point",
             "Forgetting the context",
             "A day with few receipts may have been a typhoon day, a holiday or a day the system "
             "was down. Numbers without notes can lie by accident."),
            ("point",
             "Measuring what is easy",
             "Receipts are easy to count. Waiting time is not, because no record shows when a "
             "person joined the line. Be honest about what your data cannot see, and find another"
             " way to check it, even if that means standing in the room with a notebook for an "
             "hour."),
            ("point",
             "Stopping at the decision",
             "A data-driven choice is a test. If you never measure the result, you will never "
             "learn whether it worked."),
            ("quote",
             "Data does not make the decision. It makes sure the decision is about the right facts."),
            ("h", "Write the Decision Down"),
            "One small habit makes every data-driven decision easier to learn from: a short "
            "decision note. It takes five minutes and fits on half a page.",
            ("point", "The question", "What exactly was being decided, in one sentence."),
            ("point",
             "The evidence",
             "Which records were used, for which period, and what they showed. Include the "
             "numbers, not just the conclusion."),
            ("point",
             "The choice and the reason",
             "What was decided, and which part of the evidence or experience tipped it."),
            ("point", "The check", "What will be measured afterwards, and on what date someone will look."),
            "Next December, when the same meeting comes around, nobody has to rely on memory. The"
            " office opens the note, compares the prediction with what actually happened, and "
            "decides again with better information. Over a few years, these notes become a "
            "valuable record, because they show not only what was done but why.",
            ("h", "When the Data Is Not Enough"),
            "Sometimes the records simply cannot answer the question. A new kind of fee has no "
            "history. A change in the law makes old patterns useless. A decision must be made "
            "today and the data will take a week to clean.",
            "In those cases, a good analyst says so plainly. “We do not have enough data to know."
            " Here is our best judgment, here is what it rests on, and here is how we will check "
            "it in a month.” That sentence is more useful, and more honest, than a confident "
            "number built on weak ground.",
            ("h", "Key Takeaways"),
            ("point",
             "Experience is data too",
             "Years at the counter suggest where to look. Records show whether the pattern is "
             "real and how big it is."),
            ("point",
             "Decide what would change your mind",
             "Write it down before you look, so you do not notice only the evidence that agrees with you."),
            ("point",
             "Count before you conclude",
             "One loud story can outweigh a hundred quiet records unless someone counts."),
            ("point",
             "Write a decision note",
             "Half a page on the question, the evidence, the choice and the check turns every "
             "decision into a lesson."),
            ("h", "Your Part 3 Exercise"),
            "Think of one recurring decision in your office that is usually settled by opinion. Then write:",
            ("point", "The two hunches", "What do the different sides believe, and why?"),
            ("point",
             "The record that could settle it",
             "Which existing record, with a date on it, would show who is right?"),
            ("point",
             "What would change your mind",
             "Before looking, write the result that would make you drop your own hunch."),
            "If you can, spend thirty minutes pulling that record. Even a rough count by day can "
            "be enough to move the conversation from memories to facts.",
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("cta",
             "Read: Business Intelligence Series, Part 3",
             "/blog/business-intelligence-part-3-what-to-watch/"),
            ("ask",
             "What decision in your office is still settled by whoever argues longest? What "
             "record could settle it instead?"),
        ],
    },
    {
        "date": "November 17, 2026",
        "title": "Data Analytics Series, Part 2: The Six Steps of Every Analysis",
        "slug": "data-analytics-part-2-six-steps",
        "category": "data",
        "summary": "Ask, Prepare, Process, Analyze, Share and Act. Here is what each step means, the mistakes that "
                   "happen when one is skipped, and a full worked example: deciding whether a treasury office "
                   "needs a second payment window.",
        "publish_on": "2026-11-17 21:00",
        "body": [
            "Every week, someone in a government office opens a spreadsheet, scrolls through a "
            "few thousand rows, makes a chart and sends it to the boss. Sometimes it helps. Often"
            " it does not, and nobody can say exactly why. The chart was correct. The numbers "
            "added up. Yet no decision came out of it.",
            "In a case like this, the problem is not the math. It is the order of the work. The "
            "person started with the data and hoped a question would appear. Good analysis runs "
            "the other way around, and it follows a set of steps that experienced analysts repeat"
            " almost without thinking.",
            "In Part 1, we described data analytics as the craft of turning everyday records into"
            " answers people can act on. This part lays out the road from the first question to "
            "the final decision. By the end of this post, you will know the six steps of every "
            "analysis, see them used on a real office question, and know what goes wrong when a "
            "step is skipped.",
            ("h", "Six Steps, in Plain Words"),
            "The Google Data Analytics Professional Certificate teaches the process as six "
            "phases: Ask, Prepare, Process, Analyze, Share and Act. Other courses and companies "
            "use different names. An older and widely used model called CRISP-DM, developed in "
            "the late 1990s, also has six phases, starting with understanding the business "
            "problem and ending with putting the results to use. The labels differ, but the logic"
            " is the same everywhere. Here is that logic in my own words.",
            ("point",
             "Ask",
             "Decide exactly what you need to know, who needs to know it, and what they will do "
             "with the answer."),
            ("point",
             "Prepare",
             "Find the data that can answer the question, and check where it came from and "
             "whether it can be trusted."),
            ("point",
             "Process",
             "Clean the data: fix errors, remove duplicates, handle blanks and make the format consistent."),
            ("point",
             "Analyze",
             "Organize the clean data, calculate, compare and look for patterns that answer the question."),
            ("point",
             "Share",
             "Show the findings to the people who decide, in a form they can understand quickly."),
            ("point", "Act", "Make the decision, carry it out, and measure again to see whether it worked."),
            ("quote", "Start with the question, not the spreadsheet."),
            ("photo",
             "blog/data-six-steps.jpg",
             "The six steps of an analysis form a loop: after Act, you measure again and, if "
             "needed, start over with a sharper question. (Illustration: Butch Mahinay, "
             "aumahinay.dev)",
             "medium"),
            "The best way to understand the six steps is to watch them at work. So let us follow "
            "one ordinary office problem from beginning to end.",
            ("h", "A Worked Example: Do We Need a Second Window?"),
            "Imagine a municipal treasury with one payment window for walk-in taxpayers. (As "
            "always in this series, the office and the numbers are made up.) Every few weeks "
            "someone complains about the long line. A staff member suggests opening a second "
            "window. The head of office cannot simply say yes, because a second window means "
            "moving a person away from other work. She wants evidence first.",
            ("h", "Step 1: Ask"),
            "The first version of the question is “Are the lines too long?” That sounds "
            "reasonable, but it cannot be answered. Too long for whom? Every day, or only on some"
            " days? Compared with what?",
            "A better question is specific and tied to a decision: “On which days and hours does "
            "the wait at the payment window go beyond 30 minutes, and would a second window on "
            "those days alone fix it?”",
            "Now everyone knows what a good answer looks like. It also tells us who the answer is"
            " for, the head of office, and what she will do with it: decide whether to open a "
            "second window, and when. Notice that the question already hints at a cheaper option "
            "than a full-time window. Good questions often do.",
            ("h", "Step 2: Prepare"),
            "Next, find the data. Every payment produces an official receipt with a date and, in "
            "many systems, a time. That gives us when each transaction was finished. It does not "
            "tell us when each person joined the line, which is what waiting time really is.",
            "So the analyst has two choices: use the receipt times as a stand-in, or collect new "
            "data. In our example, the office does both. It pulls a full year of receipt times "
            "from its records. Then, for two weeks that include the busy days before the March 31"
            " real property tax deadline, a staff member writes down the time each person takes a"
            " queue number and the time the person is served.",
            "This step is also where we check the data. Who recorded it? Is it complete, or are "
            "some days missing? Were the receipt clocks set correctly? A receipt system whose "
            "clock runs ten minutes fast will quietly distort every result that follows.",
            ("h", "Step 3: Process"),
            "Real records are messy. When our analyst opens the files, the problems appear quickly:",
            ("point",
             "Duplicates",
             "A few receipts were printed twice after a printer jam and appear twice in the export."),
            ("point",
             "Cancelled receipts",
             "Some receipts were cancelled and reissued, so counting them would inflate the "
             "number of transactions."),
            ("point",
             "Inconsistent times",
             "The handwritten log mixes “2:15 PM” with “14:15” and, on one page, just “2:15”."),
            ("point",
             "Gaps",
             "One afternoon has no handwritten entries at all because the staff member was called"
             " to a meeting."),
            "Cleaning means removing the duplicates, leaving out cancelled receipts, writing "
            "every time in one format and marking the afternoon with no entries as missing "
            "instead of pretending it was quiet. Each change is written down, so anyone can see "
            "what was done and why. This step is rarely exciting, but it is where an analysis can"
            " be won or lost.",
            ("h", "Step 4: Analyze"),
            "With clean data, the analyst can finally count and compare. The two-week log shows "
            "how long each person waited, and it reveals a simple link: once one window gets more"
            " than about 25 payers in an hour, the wait climbs past 30 minutes. The analyst then "
            "counts receipts by day and by hour across the whole year to find every hour above "
            "that level. Three patterns stand out:",
            ("point",
             "The rush is predictable",
             "Most long waits happen in the first three weeks of January and in the days just "
             "before each quarterly real property tax deadline."),
            ("point",
             "Mornings are worse",
             "On busy days, the line peaks between 9 and 11 in the morning. Afternoons are usually calm."),
            ("point",
             "Ordinary days are fine",
             "On most days, the window serves well under 25 payers an hour, and the log shows "
             "typical waits of under ten minutes."),
            "The answer to the question is now clear. Waits go beyond 30 minutes on about "
            "twenty-five mornings a year, all of them predictable. A second window every day "
            "would sit idle most of the time. A second window on those mornings would cover "
            "nearly all the long waits.",
            ("h", "Step 5: Share"),
            "The head of office does not need the spreadsheet. She needs the answer, the evidence"
            " and a recommendation, on one page. The analyst prepares a simple bar chart showing,"
            " for each month, how many morning hours had more than 25 payers, a short table of "
            "the peak days and hours, and three sentences:",
            "“Long waits are not an everyday problem. They happen on about twenty-five "
            "predictable mornings a year, mostly in January and before quarterly deadlines. "
            "Opening a second window on those mornings only would cover nearly all of them, "
            "without taking a person away from other work for the rest of the year.”",
            "Notice what is left out: the cleaning details, the formulas and the dozens of other "
            "charts the analyst made while exploring. Those stay in the analyst's notes in case "
            "someone asks. Sharing is about what the decision maker needs, not about showing how "
            "hard the analyst worked.",
            ("h", "Step 6: Act"),
            "The head of office approves a second window on peak mornings and posts the schedule "
            "at the entrance and on the town's page. That is the decision. But the process is not"
            " finished.",
            "After the next January, the office keeps the two-week waiting log again, and the "
            "analyst compares the new numbers with the old ones. Did waits drop below 30 minutes?"
            " Did the second window get used? If the answer is yes, the change stays. If not, the"
            " office goes back to Step 1 with a sharper question. This loop is the quiet strength"
            " of the process. Every decision becomes a small experiment, and every experiment "
            "teaches the office something.",
            ("h", "What Goes Wrong When a Step Is Skipped"),
            "Each step protects against a common mistake. It helps to know them by name.",
            ("point",
             "Skipping Ask",
             "You produce a beautiful report that answers nothing. Everyone nods, and nothing changes."),
            ("point",
             "Skipping Prepare",
             "You trust data you should not. The clock was wrong, half the days were missing, or "
             "the file was last month's."),
            ("point",
             "Skipping Process",
             "Duplicates and cancelled receipts inflate the totals, and a correct formula gives a"
             " wrong answer."),
            ("point",
             "Skipping Analyze",
             "You jump from a hunch to a conclusion. “Everyone knows January is busy” is true, "
             "but it does not tell you how many staff you need or when."),
            ("point",
             "Skipping Share",
             "The findings stay in the analyst's head or laptop, and the people who decide never see them."),
            ("point",
             "Skipping Act",
             "The report is filed, the meeting ends, and the same problem returns next year."),
            ("h", "The Steps Are a Loop, Not a Ladder"),
            "In practice, analysts move back and forth. While cleaning, you may discover that a "
            "key field was never recorded, which sends you back to Prepare. While analyzing, you "
            "may find that the question was too narrow, which sends you back to Ask. That is "
            "normal. The six steps are a guide for thinking, not a form to fill in from top to "
            "bottom.",
            "What matters is that each step happens at least once, and that Ask comes first. A "
            "clear question makes every later step easier, because it tells you which data to "
            "look for, what to clean, what to calculate and what to show.",
            ("h", "Where the Six Steps Live in a Treasury System"),
            "A good information system can make some steps much lighter. When I designed ALTOS "
            "for Philippine local treasuries, I tried to support the steps that usually take the "
            "most effort. Receipts and deposits are recorded as they happen, with their dates and"
            " amounts, so the Prepare step does not start with a box of paper. Checks for "
            "duplicates and missing details help the Process step. Reports and charts make Share "
            "faster.",
            "But no system can do Ask or Act for you. Choosing the right question and making the "
            "decision remain human work, and that is exactly as it should be.",
            ("h", "Key Takeaways"),
            ("point",
             "Ask comes first",
             "A specific question tied to a decision tells you which data to find, what to clean "
             "and what to show."),
            ("point",
             "Check before you trust",
             "Duplicates, cancelled receipts and wrong clocks can make a correct formula give a "
             "wrong answer."),
            ("point",
             "Share the answer, not the work",
             "The decision maker needs the finding, the evidence and a recommendation on one page."),
            ("point",
             "Act, then measure again",
             "Every decision is a small experiment. Measure the result and loop back if it did not work."),
            ("h", "Your Part 2 Exercise"),
            "Take the question you wrote down after Part 1. If you did not do it yet, choose one "
            "now. Then write one or two lines for each step:",
            ("point", "Ask", "Rewrite your question so it is specific and names the decision it supports."),
            ("point", "Prepare", "List the data you would need, and where each piece comes from."),
            ("point", "Process", "Guess the three most likely problems in that data."),
            ("point", "Analyze", "Write the calculation or comparison that would answer the question."),
            ("point",
             "Share",
             "Name the person who needs the answer, and the one chart you would show them."),
            ("point", "Act", "Write what would change, and how you would know if it worked."),
            "If you can fill in all six, you already have the plan for a real analysis.",
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("cta",
             "Try the free Python lesson: Build a simple RCD summary with pandas",
             "/tutorials/rcd-summary-with-pandas/"),
            ("ask",
             "Which step do you find hardest in your own work: asking the right question, finding"
             " the data, cleaning it, or getting people to act on it?"),
        ],
    },
    {
        "date": "November 13, 2026",
        "title": "Data Analytics Series, Part 1: What Data Analytics Really Is, and Why Every Office Already Has the Data",
        "slug": "data-analytics-part-1-what-it-is",
        "category": "data",
        "summary": "Data analytics is the craft of turning everyday records into answers people can act on. "
                   "Here is what it means, the four kinds of questions it can answer, a famous cholera map from 1854, "
                   "and why a local treasury is already sitting on a mountain of useful data.",
        "publish_on": "2026-11-13",
        "body": [
            "Picture a Monday morning in a municipal treasury office. The mayor calls and asks a "
            "simple question: “Will we reach our real property tax target this year?” Someone "
            "opens a logbook. Someone else starts adding up receipt stubs from the past months. "
            "By lunchtime, the office has a total, but not yet an answer.",
            "(As in all my examples, the office and the numbers are made up. No real taxpayer or "
            "town is described.)",
            "The answer was in the office all along. It was written, line by line, on thousands "
            "of official receipts: who paid, how much, for what, and on which day. What was "
            "missing was a way to turn those records into something the mayor could decide on. "
            "That way has a name. It is data analytics, and this post is the first in a series "
            "about it.",
            ("h", "Why I Am Writing This Series"),
            "I completed the Google Data Analytics Professional Certificate on Coursera, and "
            "later the Google Advanced Data Analytics Professional Certificate. What I learned "
            "there did not stay in the classroom. It shaped how I think about treasury records, "
            "and it became one of the foundations of ALTOS, the system I built for Philippine "
            "local treasuries.",
            "Data analytics lessons online can use examples such as online shops or bike rentals."
            " Those are fine, but they can feel far from a town hall in the province. This series"
            " explains the same ideas in plain words, with examples from the work I know: "
            "collections, disbursements, targets, deadlines and the people at the counter. By the"
            " end of this post, you will know what data analytics is, the four kinds of questions"
            " it answers, and why your office already holds the data to start.",
            ("h", "Data, Information and Insight"),
            "Three words are often mixed up, so let us start there. Think of them as three steps "
            "on a ladder.",
            ("point",
             "Data",
             "Raw facts, recorded one at a time. A single official receipt is data: receipt "
             "number 1234567, dated March 3, ₱2,450.00, real property tax, paid by a named owner,"
             " received by a named collector. On its own, one receipt tells you very little."),
            ("point",
             "Information",
             "Data that has been organized so it means something. “We collected ₱1.8 million in "
             "real property tax in the first quarter” is information. It came from hundreds of "
             "receipts, added up and grouped by period."),
            ("point",
             "Insight",
             "Information that explains something and points to an action. “Most of the shortfall"
             " comes from three barangays where no collection day was held this year” is an "
             "insight. It tells the office where to look and what to do next."),
            "Data analytics is the work of climbing that ladder on purpose: from scattered "
            "records, to organized information, to an insight that someone can act on.",
            ("quote", "Data is what happened. Insight is what you can do about it."),
            ("h", "So What Is Data Analytics?"),
            "Here is a working definition in plain words. Data analytics is the practice of "
            "collecting, cleaning, organizing and examining data in order to answer questions and"
            " support decisions.",
            "Notice the last part. Analytics is not about producing more reports or prettier "
            "charts. It exists to help a person decide something: where to send collectors, when "
            "to open an extra window, which accounts to follow up first, or whether a new "
            "procedure is working.",
            "You will also hear two related terms. A data analysis is one investigation, such as "
            "checking why collections dropped in May. Data analytics is the whole discipline "
            "around it: the process, the tools, the habits and the people. Data science is a "
            "wider field still. It includes building new statistical models and machine learning "
            "systems. A good analyst borrows from it, but you do not need it to begin.",
            ("h", "A Cholera Outbreak and a Famous Map"),
            "A famous story in this field happened long before computers. On August 31, 1854, "
            "cholera broke out in Soho, a crowded neighborhood in London. Hundreds of people died"
            " within days. Most doctors at the time believed the disease spread through foul air.",
            "A physician named John Snow suspected the water instead. He went through the records"
            " of who had died and where they had lived, and he asked families where they drew "
            "their water. Again and again, the answer led to one public pump on Broad Street. He "
            "also studied the exceptions. A brewery stood nearby, but none of its workers was "
            "recorded as dying of cholera. They drank the beer they were given, and the brewery "
            "had its own deep well.",
            "On September 7, Snow presented his findings to the local parish board. The next day,"
            " the handle of the pump was removed so no one could use it. Snow himself noted that "
            "the outbreak was already slowing by then, and that many residents had fled. That "
            "honesty is part of the lesson. His evidence was strong enough to act on, and he did "
            "not claim more than it showed.",
            "A few months later, Snow drew the picture that made the case famous. On a street map"
            " of the area, he placed a small mark for each death at its address. The marks pile "
            "up around the Broad Street pump and thin out farther away. Anyone could see the "
            "pattern in seconds, even without reading his tables.",
            "Snow had no spreadsheet, no database and no software. He had a clear question, "
            "carefully collected records, the courage to bring his evidence to the people who "
            "could act, and a simple picture that made the pattern plain to everyone. Those four "
            "things are still the heart of data analytics today.",
            ("h", "Four Kinds of Questions"),
            "Analysts often sort their work into four types, each answering a different question."
            " Here they are with treasury examples.",
            ("point",
             "Descriptive: What happened?",
             "Total collections last month by revenue source. This is the base for everything else."),
            ("point",
             "Diagnostic: Why did it happen?",
             "Business tax collections fell 12% compared with last January. Was it fewer "
             "businesses, smaller declared sales, or simply that more owners chose to pay in "
             "quarterly installments instead of the full year at once?"),
            ("point",
             "Predictive: What is likely to happen?",
             "Based on the pattern of the past three years, where will real property tax "
             "collections probably end by December, and how wide is the range of likely results?"),
            ("point",
             "Prescriptive: What should we do?",
             "Given the forecast, which barangays should get a collection day first, and which "
             "delinquent accounts deserve a personal visit rather than a letter?"),
            "Each type builds on the one before it. You cannot explain a drop you have not "
            "measured, and you cannot plan around a forecast you do not trust. That is why the "
            "first steps deserve care.",
            ("h", "You Do Not Need Expensive Software"),
            "A common worry is that analytics needs costly tools or a degree in mathematics. It "
            "does not. Useful analysis in a small office can start with tools that are free or "
            "already installed:",
            ("point",
             "A spreadsheet",
             "Google Sheets, LibreOffice Calc or Excel. Sorting, filtering, formulas and pivot "
             "tables will take you remarkably far."),
            ("point",
             "A database and SQL",
             "When records grow into tens of thousands of rows, a database such as SQLite keeps "
             "them organized, and SQL is the language for asking it questions."),
            ("point",
             "A charting tool",
             "A good chart can make a pattern obvious in seconds, as Snow's map did. Spreadsheets"
             " and free tools such as Looker Studio can do this."),
            ("point",
             "A programming language",
             "Python, later on, for work that is repeated every month or is too large for a "
             "spreadsheet. My free Python tutorials already cover some of this."),
            "The tool matters less than the thinking. A clear question answered with a simple "
            "spreadsheet is worth more than a beautiful dashboard that answers nothing.",
            ("h", "The Analyst's Mindset"),
            "Good analysts share a few habits. They are curious and keep asking why. They learn "
            "the context, because a number means nothing until you know how it was recorded. A "
            "dip in collections may be a real problem, or it may be a week of encoding that has "
            "not been posted yet. They are healthy skeptics who check their own results before "
            "trusting them. And they remember that behind every row there is a person.",
            "That last habit matters a great deal in government. Treasury records hold names, "
            "addresses, property details and amounts paid. In the Philippines, the Data Privacy "
            "Act of 2012 (Republic Act No. 10173) sets the rules for handling personal "
            "information. An analyst should work with the least personal data the question needs."
            " Totals by barangay, for example, rarely need anyone's name. I wrote about this in "
            "more detail in a separate post on data at the treasury counter.",
            ("h", "Where ALTOS Fits"),
            "When I built ALTOS, I kept one lesson from analytics in front of me: an answer is "
            "only as good as the records behind it. So ALTOS records each receipt and each "
            "deposit as the transaction happens, instead of copying figures later from paper. "
            "Collections can then be compared with targets by month and by revenue source, and "
            "year-end results can be forecast with an honest range rather than a single hopeful "
            "number.",
            "Just as important, every result in ALTOS is treated as a prompt for a person to "
            "decide, never as an automatic action. Data can point to where a problem might be. "
            "People still have to look, judge and act. That idea runs through this whole series.",
            ("h", "Key Takeaways"),
            ("point",
             "Data, information, insight",
             "Raw records become organized information, and information becomes insight when it "
             "points to an action."),
            ("point",
             "Analytics serves a decision",
             "If no one will decide anything with the answer, the analysis is not finished, no "
             "matter how good the chart looks."),
            ("point",
             "Four kinds of questions",
             "What happened, why, what is likely next, and what should we do. Each one rests on "
             "the one before it."),
            ("point",
             "Start with what you have",
             "Official receipts, registers and a free spreadsheet are enough to begin. The "
             "thinking matters more than the tool."),
            ("h", "Your Part 1 Exercise"),
            "Analytics is learned by doing. Before you read any further in this series, try these"
            " three small steps:",
            ("point",
             "Write down one question",
             "Pick a real question from your work that you wish you could answer with numbers. "
             "For example: Which month brings in the most collections? Or: How many days does it "
             "take for a voucher to be paid?"),
            ("point",
             "List the records that already exist",
             "Write down every logbook, register, report or file that holds part of the answer. "
             "You will probably find more than you expect."),
            ("point",
             "Name the decision",
             "Write down who would use the answer and what they would do differently. If no one "
             "would act on it, choose a better question."),
            "Keep that page. You will use it again in Part 2.",
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("cta", "Read: Why I Built ALTOS", "/blog/why-i-built-altos/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("cta",
             "Try the free Python lesson: Add up a day's collections",
             "/tutorials/add-up-daily-collections/"),
            ("ask",
             "What question at your office would you most like to answer with data? Tell me, and "
             "it may become an example in this series."),
        ],
    },
]
