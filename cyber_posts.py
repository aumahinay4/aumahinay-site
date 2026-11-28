# Cybersecurity blog series (Season 1: Cyber Hygiene and Personal Defense).
# Planned from Butch's Google Doc "10-Week Cybersecurity Blog Series Roadmap & Drafts"
# (Drive 1cqfvL885e80Hj7cjLE5YWEC392nrzD2ZkZmSLoHgwRE), written in original words and
# fact-checked on 2026-11-10 (Parts 6-10 the same day). Butch (2026-11-10): Part 1 goes live on Nov 10, then one part every Saturday at
# 10 pm PH ("YYYY-MM-DD 22:00"). A "cta" button to a later part shows only once that part is live.
# Newest first, like BLOG in content.py, which puts these posts at the top of its list.

SERIES = "Cybersecurity Series"

CYBER_POSTS = [
    {
        "title": "Cybersecurity Series, Part 40: Forty Parts in Ten Habits, the Series Wrap-Up",
        "slug": "cybersecurity-part-40-series-wrap-up",
        "category": "security",
        "date": "April 5, 2028",
        "summary": "The last part of the Cybersecurity Series gathers forty parts into ten habits: for your "
                   "accounts, your devices, the scams that reach you, and the office where you work. It ends with "
                   "a one-page checklist and a map of where to go back for each topic.",
        "publish_on": "2028-04-05 21:00",
        "body": [
            "This series opened with how modern cyberattacks really work. Since then it has covered fake parcels, cloned voices, lost phones, shared office computers, a locked records room "
            "and a group chat with too many members.",
            "Forty lessons are hard to keep in mind. Ten short habits, each with a reason, are easier. That is "
            "what this final part is for.",
            "(This is a summary of the earlier parts of the series. Each habit points back to the parts that "
            "explain it, with their sources.)",
            "Part 39 closed with office group chats. This part looks back over the whole series. When you finish "
            "reading, you will have ten habits that sum up the series, a one-page checklist "
            "for an office, a list of where to report problems in the Philippines, and a map of which part to "
            "reread for each topic.",
            ("photo", "blog/cyber-wrapup.jpg", "Forty parts in ten habits: protect your accounts, keep devices "
             "updated and locked, pause before every request for money or codes, and give the office a simple "
             "baseline. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Habits for Your Accounts"),
            ("point", "1. One strong, unique password per account, with a second step", "Part 2 explained why "
             "identity is the new perimeter. Turn on two-step verification wherever it is offered, and keep "
             "passwords out of notebooks and group chats."),
            ("point", "2. Never share a one-time PIN", "The code is meant only for you. Treat anyone who asks for it, however official they sound, as a scammer. "
             "Parts 13, 27 and 35 showed how scammers ask for it while pretending to help."),
            "Accounts are the keys. In scam after scam in this series, the loss began when someone handed over "
            "a key.",
            ("h", "Habits for Your Devices"),
            ("point", "3. Update, then update again", "Part 11 called updates the fix you keep postponing. Turn "
             "on automatic updates for the phone, the computer and the apps."),
            ("point", "4. Lock and encrypt", "A screen lock and encryption, from Parts 12 and 17, turn a lost "
             "device into only a lost device."),
            ("point", "5. Wipe before you let go", "Part 29 walked through what to do before selling, donating "
             "or throwing away a phone or laptop."),
            ("h", "Habits for the Scams That Reach You"),
            ("point", "6. Pause when it is urgent", "A deadline, a prize, a threat or a crying voice is a signal "
             "to slow down. Fake delivery texts, fake aid pages, job offers, romance and tech support scams in "
             "this series all used urgency."),
            ("point", "7. Check through a channel you already trust", "Call the number on the back of your "
             "card or the official website you typed yourself, never the number in the message. Part 15 showed "
             "how to read a web address, and Part 19 how a sender can be faked."),
            ("point", "8. Money and codes never move by chat or call alone", "A request for a transfer, load or "
             "code is confirmed in person or by a known number first. Part 22 explained why even a familiar "
             "voice is not enough."),
            ("photo", "blog/cyber-wrapup-map.jpg", "A map of the series: which parts to reread for accounts, "
             "devices, scams and the office. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Habits for the Office"),
            ("point", "9. A one-page baseline everyone follows", "Part 18 gave a small office ten rules, from "
             "one person, one account to access ending when the job ends. Parts 33, 37, 38 and 39 applied them "
             "to shared computers, doors and keys, departing staff and group chats."),
            ("point", "10. Report fast, without blame", "Part 9 laid out incident response. A clerk who reports "
             "a mistake within the hour does more good than one who hides it and hopes. Part 20 added the "
             "Data Privacy Act duties that apply at every desk."),
            ("h", "A One-Page Office Checklist"),
            "Print this, and check it once a quarter.",
            ("point", "Accounts", "Every person has their own login. Two-step verification is on for email and "
             "key systems. The access list is current."),
            ("point", "Devices", "Updates are automatic. Screens lock. Laptops are encrypted."),
            ("point", "Backups", "Important files have a copy that has been restored at least once as a test."),
            ("point", "People", "New staff are briefed. Departing staff are closed out on the last day."),
            ("point", "Places", "Restricted rooms are locked. Keys are listed and returned."),
            ("point", "Messages", "Work chats have current members only. No personal data is posted there."),
            ("point", "Reporting", "Everyone knows whom to tell, and how fast."),
            "Part 23 offered a yearly checkup for individuals. This list is the office version.",
            ("h", "Where to Report in the Philippines"),
            ("point", "Scams and cybercrime", "The Cybercrime Investigation and Coordinating Center hotline "
             "1326, mentioned throughout this series."),
            ("point", "Bank and e-wallet fraud", "Your bank or e-wallet provider first, through its official "
             "app or hotline, so it can try to stop the transfer."),
            ("point", "Personal data breaches at work", "Your office’s Data Protection Officer, as Part 9 explained. Under "
             "the National Privacy Commission’s breach rules, some breaches must be reported to the Commission within 72 hours."),
            ("point", "Fake pages and accounts", "Report them on the platform where you found them."),
            ("h", "Where to Reread"),
            ("point", "How attacks work", "Part 1, Part 3 on human hacking, Part 5 on ransomware, Part 7 on why "
             "apps get hacked, and Part 10 on what comes next."),
            ("point", "Home and personal", "Part 4 on home networks, Part 6 on the cloud, Part 16 on public "
             "Wi-Fi, and Part 28 on keeping kids safer online."),
            ("point", "Money and scams", "Parts 13, 24 to 27, 30 to 32 and 34 to 36."),
            ("point", "Social media and fake identities", "Part 14 on cloned accounts and Part 22 on deepfakes "
             "and cloned voices."),
            ("point", "Files and privacy", "Part 21 on sharing files and Part 20 on privacy at work."),
            ("point", "The office", "Parts 8, 9, 18, 33 and 37 to 39."),
            ("h", "Passing the Habits On"),
            "A habit often spreads faster when someone shows it than when someone posts it.",
            ("point", "One habit per staff meeting", "Spend five minutes on one habit, with one story from this "
             "series, and ask who has seen something like it."),
            ("point", "Pair a new staff member with a buddy", "On the first day, the buddy helps set up two-step "
             "verification and shows where the checklist is kept."),
            ("point", "Share at home", "Parents, children and older relatives receive the same fake texts and "
             "calls. Ten minutes at the dinner table may save a family’s savings."),
            ("h", "Why Habits, Not Tools"),
            "Tools help, and several parts recommended them. But story after story in this series turned on a "
            "moment when a person decided: to click, to share a code, to post a screenshot, to leave an account "
            "open. A habit makes the safe choice automatic in that moment. A checklist keeps the office from "
            "depending on any one person’s memory.",
            ("h", "Mistakes to Avoid"),
            ("point", "Treating security as the technical person’s job", "Every habit above is for everyone."),
            ("point", "Waiting for a big incident", "Small lapses are the warning."),
            ("point", "Trying everything at once", "Pick one habit a week until all ten are routine."),
            ("point", "Blaming the person who reports", "Blame teaches people to stay quiet."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Accounts", "Unique passwords, two-step verification, and no shared codes."),
            ("point", "Devices", "Updated, locked, encrypted, and wiped before you let go."),
            ("point", "Scams", "Pause, check through a trusted channel, and never move money or codes on a "
             "request alone."),
            ("point", "The office", "A one-page baseline and fast, blame-free reporting."),
            ("h", "Your Final Action Plan"),
            ("point", "This week", "Turn on two-step verification for your email and your main bank or e-wallet "
             "account."),
            ("point", "This month", "Print the office checklist and go through it with your supervisor."),
            ("point", "Every quarter", "Pick the weakest line on the checklist and fix it."),
            "Thank you for reading all forty parts. The habits are short on purpose. Keep them where you can see "
            "them, and pass them on to the one person in your office who still writes passwords on a card.",
            ("cta", "Read: Cybersecurity Series, Part 1: How Modern Cyberattacks Really Work", "/blog/cybersecurity-part-1-how-cyberattacks-work/"),
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("cta", "Read: Cybersecurity Series, Part 9: Incident Response, or What to Do When Something Goes Wrong", "/blog/cybersecurity-part-9-incident-response/"),
            ("cta", "Read: Cybersecurity Series, Part 23: Your Yearly Security Checkup, One Afternoon, Twelve Checks", "/blog/cybersecurity-part-23-yearly-security-checkup/"),
            ("ask", "Which of the ten habits will you start this week?"),
        ],
    },
    {
        "title": "Cybersecurity Series, Part 39: Office Group Chats, Who Belongs, What to Post and What to Keep",
        "slug": "cybersecurity-part-39-office-group-chats",
        "category": "security",
        "date": "March 27, 2028",
        "summary": "Office work now happens in group chats too. Those chats also collect "
                   "screenshots of personal data, former staff who never left, and decisions nobody can find "
                   "later. This part covers who should be in a work chat, what should never be posted, how to "
                   "spot a fake message from the boss, and what to keep as a record.",
        "publish_on": "2028-03-27 21:00",
        "body": [
            "It was meant to be helpful. A clerk took a screenshot of the list of delinquent taxpayers, names "
            "and amounts included, and posted it in the office group chat so the collectors could plan their "
            "visits. The chat had 63 members.",
            "Eleven of them worked in other offices. Three more no longer worked in the local government at "
            "all. By the afternoon, the screenshot had been forwarded to a barangay group, and a taxpayer whose "
            "name was on it came to the counter, holding his phone.",
            "(The office, the chat and the people are invented for this post. The privacy principle and the "
            "government report quoted below are real.)",
            "Part 38 closed accounts when someone leaves. Group chats are an easy place to miss that "
            "step. This part looks at the chat itself. Read on to learn who should be in a work chat, "
            "what should never be posted there, how the Data Privacy Act’s proportionality principle applies, "
            "how to spot a fake request in a chat, and why some messages are records that must be kept.",
            ("photo", "blog/cyber-chats.jpg", "Office group chats: the right members, nothing that exposes "
             "personal data, a check before acting on requests for money, and decisions copied into the "
             "record. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Who Belongs in a Work Chat"),
            ("point", "One chat, one purpose", "A small chat for the collection team, a separate one for "
             "announcements. A single chat for everything ends up with everyone in it."),
            ("point", "Review the members monthly", "Remove anyone who has left or transferred. Part 38 added "
             "this to the last-day checklist."),
            ("point", "Name the admins", "Two people who manage members, not everyone."),
            ("point", "Close the door", "Where the app allows it, require admin approval to join, and reset "
             "an invite link that has been shared too widely."),
            ("point", "Keep social chats separate", "Birthday greetings and jokes belong in a different chat "
             "from work, so work messages are not buried and the work chat stays small."),
            ("h", "What Should Never Be Posted"),
            ("point", "Lists of taxpayers with names and amounts", "Share the file through the office drive "
             "with access limited to those who need it, as Part 21 explained."),
            ("point", "Photos of IDs, receipts or forms", "They carry names, addresses, signatures and numbers."),
            ("point", "Passwords, codes and one-time PINs", "Not even “just for today.”"),
            ("point", "Screenshots of system screens", "They can show more than the part you meant to share."),
            ("point", "Complaints about named taxpayers", "A chat is not private, and messages can be forwarded "
             "in seconds."),
            ("h", "The Proportionality Test"),
            "The implementing rules of the Data Privacy Act set out three principles for processing personal "
            "data: transparency, legitimate purpose and proportionality. On proportionality, they say processing "
            "shall be “adequate, relevant, suitable, necessary, and not excessive in relation to a declared "
            "and specified purpose.”",
            "Posting in a chat is processing. Before sharing anything with a name on it, ask three questions.",
            ("point", "Is it needed?", "Could the collectors plan their visits with barangay totals instead of "
             "names?"),
            ("point", "Is the audience right?", "Does every member of this chat need to see it?"),
            ("point", "Is there a safer channel?", "A shared file with limited access can be safer."),
            "Part 20 covered the Data Privacy Act at your desk. The same rules follow you into the chat.",
            ("photo", "blog/cyber-chats-check.jpg", "Three questions before posting anything with a name on it: "
             "is it needed, is the audience right, and is there a safer channel? (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "When Something Was Already Posted"),
            "Mistakes happen. What matters is how fast the office responds.",
            ("point", "Delete it at once", "The person who posted it, or an admin, removes the message for "
             "everyone if the app allows it."),
            ("point", "Ask members to delete copies", "Including anything they saved or forwarded. Note who "
             "confirmed."),
            ("point", "Tell the supervisor and the Data Protection Officer", "They decide whether it is a "
             "breach that must be reported. Part 9 explained that the National Privacy Commission’s rules "
             "require notice within 72 hours for a breach that needs notification."),
            ("point", "Talk to the people affected", "If a taxpayer’s details reached people who should not "
             "have them, an honest explanation from the office is better than a rumor."),
            ("point", "Fix the cause", "A shared file, a smaller chat, or a rule in the chat policy, so the "
             "same mistake is not repeated."),
            "Blaming the clerk who posted it in good faith does little. Making the safe way the easy way does "
            "more.",
            ("h", "Fake Requests in the Chat"),
            "Scammers also use chats. A message may appear to come from the head of office, from a new number or "
            "a copied profile picture, asking for an urgent transfer, load or a code.",
            ("point", "Check the sender, not the name", "Display names and photos are easy to copy. Part 14 "
             "showed how accounts are cloned."),
            ("point", "Confirm by another channel", "Call the person on the number you already have, or ask in "
             "person."),
            ("point", "Be wary of voice notes too", "Part 22 explained that a voice can be cloned."),
            ("point", "No money or codes by chat", "Payments and approvals follow the office’s written process."),
            ("h", "Messages Can Be Records"),
            "In February 2025, the Office of the Australian Information Commissioner reported on how Australian "
            "government agencies use messaging apps. It noted that official information sent or received through "
            "apps, including disappearing messages, can be government records, and recommended that agencies set "
            "a clear policy on whether messaging apps may be used for work.",
            "These are Australian findings, not Philippine rules, but the lesson travels well.",
            ("point", "Copy decisions out of the chat", "If a decision is made in a chat, write it into the "
             "minutes or a memo. Part 27 of the Project Management Series described meetings that decide."),
            ("point", "Avoid disappearing messages for work", "A decision that vanishes cannot be checked "
             "later."),
            ("point", "Keep official files in official places", "A chat is a conversation, not a filing "
             "cabinet."),
            ("h", "Your Phone Holds the Chat"),
            "Every work chat lives on someone’s phone.",
            ("point", "Lock the phone", "A screen lock keeps a lost phone from opening every chat. Part 12 "
             "covered phone security."),
            ("point", "Hide previews", "Turn off message previews on the lock screen for work chats."),
            ("point", "Leave when you leave", "Exit work chats on your last day, and remind others to do the "
             "same."),
            ("h", "A One-Page Chat Policy"),
            "An office can agree on a short policy in one meeting.",
            ("point", "Which chats exist", "Their purpose and their admins."),
            ("point", "What not to post", "The list above."),
            ("point", "How to share files", "The office drive, with limited access."),
            ("point", "How decisions are recorded", "Minutes or memo, not the chat alone."),
            ("h", "Mistakes to Avoid"),
            ("point", "One chat for everything", "Split by purpose and audience."),
            ("point", "Never reviewing members", "Former staff can stay for years."),
            ("point", "Posting names and amounts", "Share totals, or use a limited file."),
            ("point", "Acting on a chat request for money", "Confirm by another channel."),
            ("h", "Stay-Safe Reminders"),
            ("point", "The right members", "One purpose per chat, reviewed monthly."),
            ("point", "Proportionality applies", "Share only what is needed, with only who needs it."),
            ("point", "Confirm before acting", "Names and voices can be faked."),
            ("point", "Decisions leave the chat", "Into minutes or a memo."),
            ("h", "Your Part 39 Action Plan"),
            ("point", "Today", "Open your work chats and count members who no longer belong."),
            ("point", "This week", "Ask the admins to remove them and to require approval to join."),
            ("point", "This month", "Agree on a one-page chat policy at your next staff meeting."),
            "After the screenshot, the office split its chat in two, removed fourteen members and deleted the "
            "post. The collectors now get a list of barangays and totals in the chat, and the names in a shared "
            "file only they can open.",
            ("cta", "Read: Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk", "/blog/cybersecurity-part-20-privacy-at-work/"),
            ("cta", "Read: Cybersecurity Series, Part 21: Sharing Files Safely, Links, Attachments and Who Can See Them", "/blog/cybersecurity-part-21-safe-file-sharing/"),
            ("cta", "Read: Cybersecurity Series, Part 38: When Someone Leaves or Transfers, Closing Accounts and Access", "/blog/cybersecurity-part-38-closing-access-when-staff-leave/"),
            ("cta", "Read: Cybersecurity Series, Part 14: Your Social Media Account Is a Scammer’s Best Disguise", "/blog/cybersecurity-part-14-social-media-accounts/"),
            ("ask", "How many people in your office group chat still work in your office?"),
        ],
    },
    {
        "title": "Cybersecurity Series, Part 38: When Someone Leaves or Transfers, Closing Accounts and Access",
        "slug": "cybersecurity-part-38-closing-access-when-staff-leave",
        "category": "security",
        "date": "March 17, 2028",
        "summary": "People retire, resign and move to other offices. Their accounts, keys and admin rights can "
                   "stay behind. This part explains what to close, what to keep, and what to change when "
                   "someone leaves or transfers, using a simple checklist built on a widely used US government "
                   "security standard.",
        "publish_on": "2028-03-17 21:00",
        "body": [
            "The audit team asked a simple question: who had signed in to the collection system last week? "
            "The list had eleven names. The office had nine staff.",
            "One name belonged to a clerk who had transferred to the assessor’s office in January. The other "
            "belonged to a casual employee whose contract had ended in December. Neither had done anything "
            "wrong. Their accounts had simply never been closed, and someone had been using one of them "
            "because it still had the old password written on a card.",
            "(The office, the people and the system are invented for this post. The security controls quoted "
            "below are from a published US government standard.)",
            "Part 37 looked at doors, keys and visitors. This part looks at what happens when a person who had "
            "those keys walks out of the job for the last time. Read on to learn why access lingers, what a "
            "widely used standard says to do, a checklist for the last day, how a transfer differs from a "
            "departure, and how to check that nothing was missed.",
            ("photo", "blog/cyber-leaving.jpg", "When someone leaves: list their access, close accounts on the "
             "last day, collect keys and devices, change shared secrets, and keep the office’s files. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Access Lingers"),
            ("point", "Nobody owns the task", "Human resources processes the papers. The technical person may "
             "not be told."),
            ("point", "Access is scattered", "A system login, an email account, a shared drive, a social media "
             "page, a group chat, a vault combination, a door key."),
            ("point", "Transfers look harmless", "The person is still in the same local government, so their "
             "old access feels safe to leave in place."),
            ("point", "Closing feels rude", "Nobody wants to lock out a colleague who is still having a "
             "farewell lunch."),
            "Part 18 made “access ends when the job ends” rule 9 of its one-page baseline. This part turns "
            "that rule into steps.",
            ("h", "What a Widely Used Standard Says"),
            "The US National Institute of Standards and Technology publishes a catalog of security controls, "
            "SP 800-53. Its control PS-4, Personnel Termination, lists what an organization should do when "
            "someone leaves. Among them:",
            ("point", "Disable system access", "Within a time period the organization sets."),
            ("point", "Revoke credentials", "Terminate or revoke any authenticators and credentials linked to "
             "the person."),
            ("point", "Hold an exit interview", "One that includes a discussion of security topics."),
            ("point", "Retrieve property", "Collect all security-related property, such as keys, cards and "
             "devices."),
            ("point", "Keep the office’s information", "Retain access to the information and systems the "
             "person controlled."),
            "Its control PS-5, Personnel Transfer, adds that when a person is reassigned, the organization "
            "should review whether they still need their current access and modify it to match the new job.",
            "These are not Philippine rules. They are a practical checklist that any office, large or small, "
            "can borrow.",
            ("h", "Step 1: Keep an Access List for Every Person"),
            "You cannot close what you do not know about. For each staff member, keep one row in a sheet:",
            ("point", "Systems", "Every system login, with the level of access."),
            ("point", "Email and shared drives", "Office email, shared folders and files they own."),
            ("point", "Pages and groups", "Office social media pages where they are an admin, and work group "
             "chats."),
            ("point", "Physical access", "Keys, combinations, badges, the vault and the records room, from the "
             "key register in Part 37."),
            ("point", "Devices", "Office laptop, phone, USB drives, tokens."),
            "Update the row whenever access is granted. On the last day, the row becomes the checklist.",
            ("photo", "blog/cyber-leaving-list.jpg", "One row per person becomes the last-day checklist: each item "
             "is closed, collected or changed, with the time and who did it. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 2: The Last Day"),
            ("point", "Close system accounts", "Disable them at the end of the last working day, not weeks "
             "later. Disable first. Delete only after the records are safe."),
            ("point", "Collect keys and devices", "Against the key register and the property list. Sign for "
             "each."),
            ("point", "Change what was shared", "Any password, combination or code the person knew and others "
             "still use. This step is easy to forget."),
            ("point", "Remove admin roles", "From office social media pages, the sending service, the Wi-Fi "
             "router and any shared account."),
            ("point", "Remove from work chats", "Group chats where office information is discussed."),
            ("point", "Hold a short exit talk", "Remind the person that personal data handled at work stays "
             "confidential after they leave, and ask whether any work files sit on "
             "personal devices."),
            ("h", "What the Data Privacy Act Says About Leaving"),
            "The duty to protect personal data does not end with the job. Section 20(e) of the Data Privacy "
            "Act of 2012, Republic Act No. 10173, says that employees involved in processing personal "
            "information shall hold it under strict confidentiality if it is not intended for public "
            "disclosure.",
            ("quote", "“This obligation shall continue even after leaving the public service, transfer to "
             "another position or upon termination of employment or contractual relations.”"),
            "That sentence covers all three cases in this post: leaving, transferring and the end of a contract. "
            "Reading it aloud during the exit talk takes a minute and makes the point better than a long "
            "lecture. Closing the accounts is the office’s part. Keeping quiet about what was seen is the "
            "person’s part, and the law expects both.",
            ("h", "Step 3: Keep the Office’s Files"),
            "Closing an account should not lose the work.",
            ("point", "Move file ownership", "Files the person owned in a shared drive should be transferred to "
             "the office account or a supervisor before the account is removed. Part 21 covered who can see "
             "shared files."),
            ("point", "Handle the mailbox", "Keep the office mailbox accessible to the supervisor for a set "
             "time, so replies from taxpayers are not lost."),
            ("point", "Keep the records", "Logs of what the person did stay with the office for audit."),
            ("h", "Transfers Are Different"),
            "A transfer is not a departure. The person still needs some access, just not the same access.",
            ("point", "Review", "List what the old job needed and what the new job needs."),
            ("point", "Remove what no longer fits", "The collector moving to the market office no longer needs "
             "the collection system’s cashier role."),
            ("point", "Grant the new access separately", "Through the normal request, recorded in the access "
             "list."),
            "Zero trust, from Part 8, rests on the idea that access should match the current need. A transfer "
            "is exactly the moment the need changes.",
            ("h", "Step 4: Check a Week Later"),
            ("point", "Sign-in reports", "Look for any sign-in by a closed account."),
            ("point", "Admin lists", "Check each page and service for old names."),
            ("point", "The access list", "Confirm every item on the person’s row is marked done."),
            ("h", "Mistakes to Avoid"),
            ("point", "Waiting for the paperwork", "Close access on the last working day."),
            ("point", "Forgetting shared secrets", "Change every code the person knew."),
            ("point", "Deleting too fast", "Disable first, move the files, then delete."),
            ("point", "Ignoring transfers", "Reassignment needs a review too."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Keep an access list", "One row per person, updated when access is granted."),
            ("point", "Close on the last day", "Accounts, keys, admin roles and chats."),
            ("point", "Change shared secrets", "What one person knew, everyone must assume is known."),
            ("point", "Transfers need a review", "Match access to the new job."),
            ("h", "Your Part 38 Action Plan"),
            ("point", "This week", "Start an access list with one row per staff member."),
            ("point", "This month", "Compare the sign-in list of your main system with the current staff."),
            ("point", "Next departure", "Use the person’s row as the last-day checklist, and agree with human "
             "resources that the technical person is told before the last day."),
            "After the audit, the office closed both accounts, changed the shared password on the card, and "
            "added one line to the clearance form every departing employee brings around: “Access list "
            "closed,” with a space for the technical person to sign.",
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("cta", "Read: Cybersecurity Series, Part 37: Physical Security at the Office, Doors, Keys and Visitors", "/blog/cybersecurity-part-37-physical-security/"),
            ("cta", "Read: Cybersecurity Series, Part 8: Zero Trust, or Why Every Door Gets Checked", "/blog/cybersecurity-part-8-zero-trust/"),
            ("cta", "Read: Cybersecurity Series, Part 21: Sharing Files Safely, Links, Attachments and Who Can See Them", "/blog/cybersecurity-part-21-safe-file-sharing/"),
            ("ask", "When someone left your office last, who closed their accounts, and when?"),
        ],
    },
    {
        "title": "Cybersecurity Series, Part 37: Physical Security at the Office, Doors, Keys and Visitors",
        "slug": "cybersecurity-part-37-physical-security",
        "category": "security",
        "date": "March 8, 2028",
        "summary": "Passwords and updates mean little if anyone can walk into the records room or carry out a "
                   "laptop. This part covers the physical side of security in a small office: who may enter "
                   "which room, how to handle visitors and keys, what tailgating is, and what the Data Privacy "
                   "Act’s implementing rules say about physical measures.",
        "publish_on": "2028-03-08 21:00",
        "body": [
            "The man wore a lanyard and carried a toolbox. He said he was from the internet provider, sent to "
            "check the connection, and asked where the network equipment was. The clerk at the front desk "
            "pointed him down the hall. It was the room where the records of every real property owner in "
            "town were kept, and the door had been propped open with a chair because the air conditioner was "
            "broken.",
            "He spent twenty minutes inside, alone. Nobody had called the provider to confirm he was coming.",
            "(The visitor, the office and the events are invented for this post. The rules quoted below are "
            "from the cited regulations.)",
            "Part 36 dealt with a fake warning on the screen. This part steps away from the screen to the door. "
            "Read to the end and you will know why physical security matters as much as passwords, which "
            "rooms need control, how to handle visitors and keys, what tailgating looks like, and what the "
            "Data Privacy Act’s implementing rules expect.",
            ("photo", "blog/cyber-physical.jpg", "Physical security: control who enters each room, escort "
             "visitors, manage keys, and keep devices and papers out of reach. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why the Door Matters"),
            "Every protection in this series assumes that a stranger cannot simply touch the equipment.",
            ("point", "A device in hand", "Someone with a few minutes alone at a computer can plug in a "
             "drive, read an unlocked screen or take the device. Part 17 explained how encryption limits the "
             "damage when a device is lost."),
            ("point", "Paper is data too", "Tax declarations, receipts and payroll sheets hold names, "
             "addresses and amounts. A file cabinet left open needs no password."),
            ("point", "Network equipment", "A switch or router in an open room can be connected to, reset or "
             "unplugged."),
            ("h", "What the Data Privacy Act Rules Say"),
            "The implementing rules and regulations of the Data Privacy Act of 2012, Republic Act No. 10173, "
            "include a section on physical security measures, Section 27. Where appropriate, it expects "
            "offices that handle personal data to have:",
            ("point", "Access controls on rooms", "Policies and procedures to monitor and limit access to, "
             "and activities in, the rooms and workstations where personal data is processed."),
            ("point", "A sensible layout", "Office space and workstations arranged so that people processing "
             "personal data have privacy from those who pass by."),
            ("point", "Defined duties and schedules", "So that only the people doing that work are in the room "
             "or at the workstation at a given time."),
            ("point", "Rules for media", "Policies for the transfer, removal, disposal and re-use of electronic "
             "media."),
            ("point", "Protection from damage", "Measures that protect rooms and equipment, as far as "
             "practicable, from disasters, power problems, outside access and similar threats."),
            "Part 20 covered privacy at your desk. This part is about the rooms and doors around it.",
            ("h", "Map the Rooms"),
            "Walk through the office and sort every room into three groups.",
            ("point", "Public", "The counter area and the waiting area. Anyone may be there during office "
             "hours."),
            ("point", "Staff only", "Work areas behind the counter, where computers and current files are."),
            ("point", "Restricted", "The vault, the records room and the room or cabinet with network "
             "equipment. Only named people may enter, and the door stays locked."),
            "Post the rule on each restricted door: who may enter, and who to call if someone else asks.",
            ("photo", "blog/cyber-physical-zones.jpg", "Three zones in a treasury office: public, staff only "
             "and restricted, with the rule for each door. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Visitors"),
            ("point", "Confirm before they arrive", "A real technician’s visit can be confirmed by calling the "
             "company at the number on your contract or bill, not a number the visitor gives."),
            ("point", "Log every visitor", "Name, organization, purpose, time in and time out."),
            ("point", "Escort in staff and restricted areas", "A visitor is never alone in a room with "
             "records, equipment or cash."),
            ("point", "Give visitors a badge", "A simple numbered visitor card, returned on the way out, "
             "makes a stranger without one easy to spot."),
            ("point", "Ask without embarrassment", "“May I see your work order? I’ll call your office to "
             "confirm.” A real visitor expects it."),
            ("h", "Tailgating"),
            "Tailgating is following an authorized person through a locked door without using your own access. "
            "It can look like politeness: someone carrying boxes, a smile, a door held open.",
            ("point", "Let the door close", "Each person opens a restricted door for themselves."),
            ("point", "Offer to help instead", "“Let me get someone to let you in” is courteous and safe."),
            ("point", "Never prop a restricted door", "If it must stay open for repairs, a staff member stays "
             "beside it."),
            ("h", "Keys and Combinations"),
            ("point", "A key register", "Who holds which key, signed when issued and when returned."),
            ("point", "Change when people leave", "When a person with a vault combination or a restricted key "
             "transfers or retires, change the combination or the lock. Part 18 made “access ends when the "
             "job ends” one of its rules."),
            ("point", "No spare keys in drawers", "A spare key in an unlocked drawer is an open door."),
            ("h", "Devices and Papers"),
            ("point", "Lock the screen when you stand up", "Part 33 covered the habits for shared computers."),
            ("point", "Laptops stay locked away", "After hours, laptops go into a locked cabinet or are taken "
             "home under the office’s rules."),
            ("point", "Clear the printer", "Collect printouts at once. A report left in the tray can walk out "
             "with anyone."),
            ("point", "Dispose properly", "Old drives and papers follow the office’s disposal rules, as "
             "Part 29 advised for devices, and its records schedule."),
            ("h", "Power, Water and Fire"),
            "Section 27 also covers protection from damage. Keep records and equipment off the floor in rooms "
            "that flood, use a surge protector or uninterruptible power supply for key equipment, and know "
            "where the fire extinguisher is.",
            ("h", "A Short Monthly Walk-Through"),
            "Once a month, the person who owns physical security walks the office with a short list. It takes "
            "about fifteen minutes.",
            ("point", "Doors", "Do restricted doors close and lock by themselves? Is any one propped or left "
             "unlocked?"),
            ("point", "Logs", "Is the visitor log filled in, with times out as well as times in?"),
            ("point", "Keys", "Does the key register match the people who still work in the office?"),
            ("point", "Equipment", "Is anything plugged into the network equipment that nobody recognizes? "
             "Are cables and power strips in order?"),
            ("point", "Papers", "Are printers, desks and shared tables clear of documents with personal "
             "data at the end of the day?"),
            "Write the date and what was found. A list of small fixes each month is a sign the check works.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting a uniform", "Confirm every unscheduled visitor."),
            ("point", "Propping doors", "A propped restricted door is an unlocked one."),
            ("point", "Keys without a register", "Nobody knows who can get in."),
            ("point", "Leaving visitors alone", "Escort them in staff and restricted areas."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Three zones", "Public, staff only and restricted."),
            ("point", "Confirm, log, escort", "Every visitor, every time."),
            ("point", "Keys and combinations change with people", "When access ends, it really ends."),
            ("point", "The law expects it", "Section 27 of the Data Privacy Act rules lists physical measures."),
            ("h", "Your Part 37 Action Plan"),
            ("point", "Today", "Walk the office and label each room public, staff only or restricted."),
            ("point", "This week", "Start a visitor log at the front desk and a key register for restricted "
             "rooms."),
            ("point", "This month", "Check who holds the vault combination and the records room key, and "
             "change any that a former staff member knew."),
            "The internet provider had sent nobody. A technician from the municipal IT office checked the "
            "network equipment that afternoon and found a small device plugged into the back of the switch. "
            "The next day, the records room door had a lock, a sign and a visitor log, and the air "
            "conditioner was finally fixed.",
            ("cta", "Read: Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk", "/blog/cybersecurity-part-20-privacy-at-work/"),
            ("cta", "Read: Cybersecurity Series, Part 33: Shared Office Computers, Habits That Keep One Desk From Exposing Everyone", "/blog/cybersecurity-part-33-shared-office-computers/"),
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("cta", "Read: Cybersecurity Series, Part 3: The Art of Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("ask", "Who can walk into your office’s records room today without anyone noticing?"),
        ],
    },
    {
        "title": "Cybersecurity Series, Part 36: Tech Support Scams, the Fake Virus Warning That Wants a Phone Call",
        "slug": "cybersecurity-part-36-tech-support-scams",
        "category": "security",
        "date": "February 28, 2028",
        "summary": "A loud warning fills the screen, says the computer is infected, and gives a number to call. "
                   "This part explains how tech support scams work, what the US Federal Trade Commission says "
                   "real companies do not do, how to close a fake warning safely, and what to do if you "
                   "already let a stranger into your computer.",
        "publish_on": "2028-02-28 21:00",
        "body": [
            "It was ten minutes before lunch when the screen on the cashier’s computer turned red. A box in "
            "the middle said the computer was infected, that personal and bank data were at risk, and that "
            "she must not shut it down. A voice read the warning aloud through the speakers. At the bottom was "
            "a phone number for “technical support.”",
            "The browser would not close. The beeping would not stop. Carmen picked up her phone and dialed the "
            "number, because the screen said that was the only way to fix it.",
            "(Carmen, the office and the call are made up for this post. The advice below comes from the cited "
            "government sources.)",
            "Part 35 looked at fake customer service that waits for you to search. This part looks at a scam "
            "that interrupts you instead: the fake virus warning. After this post, you will know how tech "
            "support scams work, the signs that a warning is fake, how to close one safely, and what to do if "
            "you already called, paid or let someone connect to your computer.",
            ("photo", "blog/cyber-techsupport.jpg", "Tech support scams: a fake warning, a phone number, a "
             "request to connect to your computer, and a demand for payment. Real security warnings do not "
             "ask you to call. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "How the Scam Works"),
            ("point", "The warning", "A web page, sometimes reached through a bad ad or a mistyped address, fills "
             "the screen. It may copy a well-known logo, play an alarm, and claim to have found viruses."),
            ("point", "The number", "The page tells you to call a support line right away. Some versions "
             "arrive as a phone call instead, from someone who says your computer has been sending errors."),
            ("point", "The connection", "The “technician” asks you to install a remote-access app, so they "
             "can see and control your screen."),
            ("point", "The show", "They open system screens full of warnings that are normal, and call them "
             "proof of infection."),
            ("point", "The bill", "They ask for payment for a repair, a license or a protection plan, or they "
             "ask you to open your bank or e-wallet to “check” for hackers."),
            ("h", "What the FTC Says Real Companies Do Not Do"),
            "The US Federal Trade Commission’s guide to tech support scams, dated September 2025, "
            "is direct about the signs.",
            ("point", "No surprise contact", "The FTC says legitimate tech companies won’t contact you by "
             "phone, email or text message to tell you there is a problem with your computer."),
            ("point", "No phone numbers in warnings", "In an April 2025 consumer alert, the FTC said security "
             "pop-up warnings from real tech companies will never ask you to call a phone number."),
            ("point", "Payment methods that are hard to reverse", "The FTC lists gift cards, wire transfers, "
             "bank transfers, cryptocurrency and payment apps among the methods scammers insist on."),
            ("point", "Moving money “to protect it”", "The FTC warns that some scammers hand you to a fake "
             "official who tells you to move your money to keep it safe. That is a scam."),
            ("h", "Why It Works"),
            ("point", "Noise and urgency", "An alarm and a countdown make people act before they think."),
            ("point", "A screen that will not close", "The page uses full-screen mode and pop-ups to look "
             "like the whole computer is locked."),
            ("point", "Fear of blame", "At work, a staff member may worry about being blamed and try to fix "
             "it quietly instead of telling the office’s technical person."),
            ("photo", "blog/cyber-techsupport-steps.jpg", "What to do when a fake warning appears, and what to "
             "do if you already called or let someone connect. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "How to Close a Fake Warning"),
            "A fake warning is a web page. Closing the browser removes it.",
            ("point", "Do not call, click or type", "Not the number, not the buttons inside the warning, not "
             "even one that says “Cancel.”"),
            ("point", "Leave full screen", "In common browsers such as Chrome and Edge, pressing the Esc key exits full-screen mode, so "
             "the browser’s own close button appears."),
            ("point", "Close the browser", "If the page will not let go on a Windows computer, press Ctrl, "
             "Shift and Esc together to open Task Manager, select the browser, and choose End task."),
            ("point", "Do not restore the old tabs", "When you open the browser again, it may offer to reopen "
             "the pages. Decline, or the warning returns."),
            ("point", "Then check properly", "The FTC suggests updating your security software and running a "
             "scan. Part 11 explained why updates matter."),
            "On a phone, the same kind of warning appears inside the browser. Close the tab, and do not "
            "install any app the page recommends.",
            ("h", "If You Already Called or Let Someone Connect"),
            ("point", "Disconnect", "Turn off Wi-Fi or unplug the network cable, so the remote session ends."),
            ("point", "Remove the remote-access app", "Uninstall whatever they told you to install. At the "
             "office, let the technical person do this and check the computer."),
            ("point", "Change passwords from another device", "The FTC advises changing your password right "
             "away, and changing it on any other account that used the same one."),
            ("point", "Call your bank or e-wallet", "If you paid or opened a banking app during the call, ask "
             "the bank to block the account or card and reverse what it can."),
            ("point", "Report it", "In the Philippines, call the CICC hotline 1326. At work, follow the "
             "incident steps from Part 9 and tell your supervisor."),
            ("h", "At the Office"),
            ("point", "Make reporting safe", "Tell staff that a fake warning is not their fault, and that "
             "reporting it quickly is the right move."),
            ("point", "Post the rule", "Beside each computer: “A real warning never asks you to call. Close "
             "the browser and tell IT.”"),
            ("point", "Limit who can install apps", "If daily work uses a normal account without administrator "
             "rights, a caller has a harder time talking anyone into installing remote access. Part 18 made "
             "“fewest possible administrators” rule 3 of its baseline."),
            ("point", "Keep one trusted contact", "Name the person or office that handles computer problems, "
             "and make sure staff know that real support at work comes from that person, not from a number "
             "on a screen."),
            ("point", "Check the browser", "Blocking pop-ups and removing unknown browser extensions reduces "
             "the pages that can take over a screen. The office’s technical person can check each computer "
             "once a quarter."),
            ("h", "Mistakes to Avoid"),
            ("point", "Calling the number on the screen", "Real warnings do not include one."),
            ("point", "Letting a stranger connect", "Remote access hands over the computer."),
            ("point", "Paying to “fix” a warning", "Especially by gift card, transfer or crypto."),
            ("point", "Hiding it at work", "Report it so others are warned and the computer is checked."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Warnings with phone numbers are fake", "So says the FTC."),
            ("point", "Close the browser", "Esc, then close, or Task Manager on Windows."),
            ("point", "Never allow remote access to a caller", "Disconnect if you already did."),
            ("point", "Act fast if you paid", "Bank first, then CICC 1326."),
            ("h", "Your Part 36 Action Plan"),
            ("point", "Today", "Practice pressing Ctrl, Shift and Esc on a Windows computer, so you know where "
             "Task Manager is before you need it."),
            ("point", "This week", "Show a parent or co-worker a picture of a fake warning, and tell them the "
             "one rule: never call the number."),
            ("point", "For the office", "Write down who to call when a warning appears, and put that name "
             "and number beside each computer."),
            "The “technician” was asking Carmen to download an app when the office’s IT assistant walked past and "
            "saw the red screen. He ended the call, closed the browser from Task Manager and scanned the "
            "computer. Nothing had been installed. The next morning, a small card appeared beside every "
            "computer in the treasury: “A real warning never asks you to call.”",
            ("cta", "Read: Cybersecurity Series, Part 35: Fake Customer Service, When Help Is the Trap", "/blog/cybersecurity-part-35-fake-customer-service/"),
            ("cta", "Read: Cybersecurity Series, Part 11: Software Updates, the Fix You Keep Postponing", "/blog/cybersecurity-part-11-software-updates/"),
            ("cta", "Read: Cybersecurity Series, Part 9: Incident Response, or What to Do When Something Goes Wrong", "/blog/cybersecurity-part-9-incident-response/"),
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("ask", "Has a fake virus warning ever appeared on a computer at your office?"),
        ],
    },
    {
        "date": "February 18, 2028",
        "title": "Cybersecurity Series, Part 35: Fake Customer Service, When Help Is the Trap",
        "slug": "cybersecurity-part-35-fake-customer-service",
        "category": "security",
        "summary": "When something goes wrong with a bank, an e-wallet or an online order, people look for "
                   "help fast, and scammers are waiting with fake pages, fake hotlines and fake agents. This "
                   "part explains how these traps work, what the Bangko Sentral and the US Federal Trade "
                   "Commission advise, how to find the real channel, and what to do if you already talked "
                   "to a fake.",
        "publish_on": "2028-02-18 21:00",
        "body": [
            "Mario’s e-wallet transfer to his sister had been “processing” for an hour. Worried, he typed "
            "the e-wallet’s name and “customer service” into a social media search. A page with the right "
            "logo and thousands of followers answered his comment within minutes. An agent sent him a "
            "message: to release the stuck transfer, he only needed to verify his account by giving the code "
            "that would arrive by text.",
            "He gave the code. Ten minutes later, his balance was zero. The original transfer, it turned out, "
            "had gone through on its own.",
            "(Mario and the page are invented for this post. The advice quoted below is real and cited.)",
            "Part 34 looked at fake delivery texts. This part looks at a trap that waits for you to come to "
            "it: fake customer service. You will learn where these fakes appear, why they work, what the "
            "Bangko Sentral ng Pilipinas and the US Federal Trade Commission advise, how to find a company’s "
            "real channel, and what to do if you already shared something.",
            ("photo", "blog/cyber-help.jpg", "Fake customer service: fake pages, fake numbers and fake "
             "agents wait for people in a hurry. Find the real channel yourself, and never share a "
             "one-time PIN. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Where the Fakes Appear"),
            ("point", "Social media pages and comments", "Pages that copy a bank’s or e-wallet’s name and "
             "logo, and accounts that reply to public complaints with “Send us a message.”"),
            ("point", "Search results", "The FTC warned on April 3, 2025 that scammers buy paid search "
             "placements using another company’s name, and put their own phone number next to a trusted "
             "name."),
            ("point", "Calls that come to you", "Someone who says they are from your bank’s fraud team, "
             "calling to “help” with a problem you did not report."),
            ("point", "Messaging apps", "An “agent” who moves the conversation to a private chat."),
            "Banks have warned about this. In a customer advisory, CIMB Bank PH reported “unauthorized social "
            "media accounts and online profiles falsely claiming to represent” it, and listed its official "
            "pages and its website so customers could check.",
            ("h", "Why It Works"),
            ("point", "You start the contact", "Because you searched or posted first, the reply feels like "
             "the help you asked for."),
            ("point", "You are worried", "A stuck transfer, a locked account or a missing parcel makes "
             "people act fast."),
            ("point", "It looks right", "A copied logo, a similar name and a quick, polite reply."),
            ("point", "The request sounds routine", "“Verify your account,” “confirm the code,” “install this "
             "app so we can check.”"),
            ("h", "What the Bangko Sentral Advises"),
            "In an August 2026 #BSPSecuriTips message shared by Standard Chartered Philippines, the BSP said "
            "banks will never ask for your personal or financial information. Its advice, in short:",
            ("point", "Don’t give your details to anyone", "Including someone who says they are from the bank."),
            ("point", "Use only official channels", "Contact your bank or e-wallet only through its official "
             "customer service channels."),
            ("point", "Act fast if exposed", "Contact the bank or e-money issuer at once through those "
             "channels."),
            ("point", "Report and escalate", "Report scammers to the CICC at 1326 or the PNP Anti-Cybercrime "
             "Group. If the bank does not address your concern, escalate it to the BSP through its "
             "online assistant, BSP Online Buddy."),
            ("h", "What the FTC Advises About Search"),
            ("point", "The first results may be ads", "They may not be the company you want."),
            ("point", "Don’t assume a number in search results is legit", "Scroll to the regular results and "
             "find the company’s own site."),
            ("point", "Type the address yourself", "If you know the company’s website, type it directly. If "
             "you are paying a bill, use the address or number printed on the bill."),
            ("h", "Government Services Are Copied Too"),
            "The same FTC alert said scammers also buy search ads using the name of a government service. "
            "Taxpayers looking for how to pay a tax, renew a permit or get a certificate can land on a page "
            "that charges a “processing fee” or collects personal details.",
            ("point", "Start from the office itself", "Use the website or page your local government "
             "announces at its offices or on its official notices."),
            ("point", "Check the address", "Look for an address ending in .gov.ph, the domain reserved for Philippine government offices. A "
             "look-alike address is a reason to stop."),
            ("point", "When unsure, ask at the counter", "A call or a visit to the treasurer’s office costs "
             "less than a fake fee."),
            ("photo", "blog/cyber-help-path.jpg", "The safe path to real help, and the shortcuts that lead "
             "to fakes. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "How to Find the Real Channel"),
            ("point", "Start inside the app", "Your bank or e-wallet app has a help or contact section. That "
             "is the safest door, because you did not have to search for it."),
            ("point", "Use the number on your card or statement", "It was printed by the bank."),
            ("point", "Type the website yourself", "Part 15 showed how to read a web address. From the real "
             "site, follow its links to its official social media pages."),
            ("point", "Don’t trust followers or badges alone", "A page can buy followers, and a name can be "
             "copied. Check the link from the official website."),
            ("point", "Hang up and call back", "If someone calls claiming to be your bank, end the call and "
             "dial the number on your card yourself."),
            ("h", "What Real Help Will Not Ask For"),
            ("point", "Your one-time PIN", "Part 13 explained that a one-time PIN is the key to your account. "
             "Real support does not need it."),
            ("point", "Your password or full card number", "Support can find your account without them."),
            ("point", "A remote-access app", "Installing an app that lets someone see or control your phone "
             "hands them the account."),
            ("point", "A fee to fix a problem", "Or a transfer to a “safe account.”"),
            ("h", "If You Already Shared Something"),
            ("point", "Call your bank or e-wallet through the official channel at once", "Ask them to block "
             "the account and reverse what they can."),
            ("point", "Change your password and PIN", "From your own device, through the official app."),
            ("point", "Uninstall any app they asked for", "And check that nothing else was added."),
            ("point", "Report it", "CICC 1326 or the PNP Anti-Cybercrime Group, with screenshots of the page, "
             "the chat and the numbers used. Report the fake page to the platform too."),
            ("quote", "Help you found by searching might not be help. Help you reached through the app, the "
             "card or the official website is far safer."),
            ("h", "Mistakes to Avoid"),
            ("point", "Posting your problem publicly", "It invites fake “agents” to message you."),
            ("point", "Calling the first number in search results", "Use the app, the card or the bill."),
            ("point", "Sharing a code to “verify” your account", "Real support does not need it."),
            ("point", "Staying on a call you did not start", "Hang up and call the official number."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Fakes wait where you look for help", "Pages, search results, calls and chats."),
            ("point", "Banks don’t ask for your details", "So says the BSP."),
            ("point", "Find the real channel yourself", "App, card, statement or typed website."),
            ("point", "Act fast if exposed", "Bank first, then CICC 1326, then BSP Online Buddy if needed."),
            ("h", "Your Part 35 Action Plan"),
            ("point", "Today", "Open your bank and e-wallet apps and find their help sections, so you know "
             "where they are before you need them."),
            ("point", "This week", "Save your bank’s official hotline from the back of your card into your "
             "phone contacts."),
            ("point", "For your family", "Tell them one rule: never search social media for customer service. "
             "Start from the app."),
            "Mario’s e-wallet froze the account that received his money, and he reported the page to the "
            "platform and to the CICC. Now his bank’s hotline is saved in his phone, copied from the back of "
            "his card, and the help section in each of his apps is the first place he looks.",
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 14: Your Social Media Account Is a Scammer’s Best Disguise", "/blog/cybersecurity-part-14-social-media-accounts/"),
            ("cta", "Read: Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address", "/blog/cybersecurity-part-15-fake-websites/"),
            ("cta", "Read: Cybersecurity Series, Part 34: Fake Delivery Texts, the Parcel That Never Was", "/blog/cybersecurity-part-34-fake-delivery-texts/"),
            ("ask", "Where do you look first when you need help from your bank or e-wallet?"),
        ],
    },
    {
        "date": "February 9, 2028",
        "title": "Cybersecurity Series, Part 34: Fake Delivery Texts, the Parcel That Never Was",
        "slug": "cybersecurity-part-34-fake-delivery-texts",
        "category": "security",
        "summary": "A text says your parcel could not be delivered and asks you to pay a small fee or update "
                   "your address through a link. This part explains how these messages work, what the "
                   "Philippine Postal Corporation has said it does not do, the signs of a fake, how to check "
                   "a real delivery, and what to do if you already clicked.",
        "publish_on": "2028-02-09 21:00",
        "body": [
            "Joy was waiting for a pair of school shoes she had ordered online for her son. On Tuesday "
            "afternoon, a text arrived: her parcel was on hold because of an incomplete address. To "
            "reschedule delivery, she only had to confirm her address and pay a redelivery fee of less than "
            "₱20 through the link. The amount was so small that paying felt easier than asking.",
            "She opened the link and typed her card number. That evening, her bank sent an alert for a "
            "₱9,800 purchase she had not made.",
            "(Joy and her parcel are invented for this post. The warnings quoted below are real and cited.)",
            "Part 33 kept a shared office computer from exposing everyone who uses it. This part looks at a message that can reach anyone who shops online: the fake delivery text. You will learn how "
            "these messages work, what the post office has said about them, the signs of a fake, how to "
            "check a real delivery safely, and what to do if you already clicked or paid.",
            ("photo", "blog/cyber-parcel.jpg", "Fake delivery texts: a small fee, an urgent deadline and a "
             "link. Check your order where you bought it, not through the message. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "How the Scam Works"),
            "The message is built to make one click feel harmless.",
            ("point", "A believable story", "A failed delivery, an incomplete address, a parcel on hold. Anyone "
             "who shops online may be waiting for something, so the story can fit."),
            ("point", "A small amount", "A fee of a few pesos does not feel like a risk. The real target is "
             "the card number, the bank login or the one-time PIN typed into the fake page."),
            ("point", "A deadline", "“Update within 24 hours or the parcel will be returned.” Urgency leaves "
             "less time to think."),
            ("point", "A link", "The link leads to a page dressed up as a courier or the post office, with a "
             "logo and a payment form."),
            "Once the details are typed in, the scammers can use the card, or try to log in to the bank or "
            "e-wallet. Part 13 explained how one-time PINs protect those accounts, and why nobody should "
            "ever ask you for one.",
            ("h", "What the Post Office Has Said"),
            "The Philippine Postal Corporation, PHLPost, has warned the public about these messages more than "
            "once.",
            ("point", "May 2025", "GMA News reported on May 9, 2025 that PHLPost warned of scam messages using "
             "its name and logo. The messages said a parcel could not be delivered because of an incorrect "
             "address, and asked for a ₱17.05 fee through a fake website."),
            ("point", "What PHLPost says it does not do", "In the same report, PHLPost said it “does not send "
             "text messages, emails, or online notices requesting payment or address updates for "
             "undelivered parcels.”"),
            ("point", "A later warning", "In August 2026, the Daily Tribune reported a PHLPost warning about texts "
             "citing “an incomplete address” and asking for a redelivery fee by card. PHLPost said it does "
             "not ask for bank details, card information, passwords or one-time passwords by text."),
            "A private courier has warned its customers too. In November 2023, Philstar reported that PHLPost warned "
            "against messages using its name to ask for personal information, and that DHL Express "
            "Philippines had told customers to check the domain names of links and “never disclose sensitive "
            "information” such as passwords and card numbers. The scammer only needs a "
            "name people recognize, and the message can use any courier’s name.",
            ("h", "What the FTC Advises"),
            "The same trick is reported in other countries. In a consumer alert on December 14, 2023, the US "
            "Federal Trade Commission described fake messages saying “you missed a delivery attempt” and "
            "asking you to click a link to reschedule. Its advice:",
            ("point", "Don’t click", "If a message about an unexpected delivery tells you to click a link, "
             "don’t."),
            ("point", "Use contacts you know", "Contact the shipping company through a phone number or website "
             "you know is real, not the one in the message."),
            ("point", "Check where you bought it", "If you did order something, go to the site or app where "
             "you bought it and check the delivery status there."),
            ("photo", "blog/cyber-parcel-signs.jpg", "Reading a fake delivery text: the warning signs, one "
             "by one. The message and link are invented. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "The Signs of a Fake"),
            ("point", "An ordinary mobile number", "The text comes from a personal-looking number, not the "
             "name of the company."),
            ("point", "A fee to release a parcel", "Especially a small, oddly exact amount."),
            ("point", "A strange web address", "Part 15 explained how to read a web address. Look at the "
             "part just before the first single slash. If it is not the company’s real domain, close the page."),
            ("point", "A request for card details or a PIN", "A real delivery does not need your one-time "
             "PIN."),
            ("point", "No order to match", "You are not expecting anything from that company, or your shop "
             "app shows the parcel moving normally."),
            ("h", "How to Check a Real Delivery"),
            ("point", "Open the shop app or website yourself", "The order page shows the courier and the "
             "tracking status."),
            ("point", "Use the courier’s official channel", "Type the courier’s address yourself, or call the "
             "number on its official website. For PHLPost, GMA News listed the hotline (02) 8288-7678 and "
             "the website phlpost.gov.ph."),
            ("point", "Pay cash on delivery only to the rider at your door", "And only for an order you "
             "recognize."),
            ("h", "If You Already Clicked or Paid"),
            ("point", "Call your bank or e-wallet at once", "Report the transaction, ask them to block the "
             "card, and change your online banking password."),
            ("point", "If you typed a one-time PIN", "Tell the bank that too. It may mean someone tried to "
             "log in or approve a payment."),
            ("point", "Report it", "Call the CICC hotline 1326, and keep a screenshot of the text, the "
             "sender’s number and the web address."),
            ("point", "Watch your accounts", "Check statements for the next few weeks. Part 13 described the "
             "protections under the anti-scam law, Republic Act No. 12010."),
            "If you clicked but typed nothing, close the page. Do not return to it, and delete the message.",
            ("quote", "The fee is small because the fee is not the point. Your card number is."),
            ("h", "Mistakes to Avoid"),
            ("point", "Paying a small fee to be safe", "The fee is the bait."),
            ("point", "Tracking through the link in the text", "Use the shop app or the courier’s own site."),
            ("point", "Sharing a one-time PIN", "No real delivery needs it."),
            ("point", "Waiting to call the bank", "Speed matters when a card is exposed."),
            ("h", "Stay-Safe Reminders"),
            ("point", "PHLPost does not text for fees", "Or for address updates, according to its 2025 warning."),
            ("point", "Check at the source", "The shop where you ordered, or the courier’s official site."),
            ("point", "Read the web address", "The real domain decides, not the logo."),
            ("point", "Act fast if you paid", "Bank or e-wallet first, then CICC 1326."),
            ("h", "Your Part 34 Action Plan"),
            ("point", "Today", "Find the official tracking page of the courier you use most, and bookmark it."),
            ("point", "This week", "Show a parent or older relative one fake delivery text and the "
             "signs above."),
            ("point", "Next time", "When a delivery text arrives, open your shop app before anything else."),
            ("point", "For the office", "If your office sends or receives official mail and parcels, tell "
             "staff that a delivery text about an office package is checked with the courier by phone or "
             "through the official site before anyone pays anything."),
            "Joy’s bank reversed the charge after she filed a dispute, though it took two weeks. Her son’s "
            "shoes arrived on Thursday, brought by a rider who did not ask for any fee. Now, when a delivery "
            "text arrives, she opens the shop app first.",
            ("cta", "Read: Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address", "/blog/cybersecurity-part-15-fake-websites/"),
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 25: Online Marketplace Scams, Buying and Selling Without Getting Burned", "/blog/cybersecurity-part-25-online-marketplace-scams/"),
            ("cta", "Read: Cybersecurity Series, Part 24: QR Code Scams, When a Square of Dots Sends You the Wrong Way", "/blog/cybersecurity-part-24-qr-code-scams/"),
            ("ask", "Have you received a delivery text for a parcel you never ordered?"),
        ],
    },
    {
        "date": "January 31, 2028",
        "title": "Cybersecurity Series, Part 33: Shared Office Computers, Habits That Keep One Desk From Exposing Everyone",
        "slug": "cybersecurity-part-33-shared-office-computers",
        "category": "security",
        "summary": "When several people use one computer, one person’s open email, saved password or "
                   "forgotten download becomes everyone’s risk. This part covers separate accounts, locking "
                   "the screen, keeping passwords out of the browser, guest mode for personal browsing, "
                   "cleaning up files and printouts, and an end-of-day routine.",
        "publish_on": "2028-01-31 21:00",
        "body": [
            "The computer at the front counter was used by three people in two shifts. On Monday morning, "
            "the first clerk to sit down found the office email still open from Friday, a personal social "
            "media account signed in on another tab, and a spreadsheet in the Downloads folder titled "
            "“delinquent list final.” The printer tray beside it held two copies of someone’s payslip.",
            "Nobody had done anything unusual. Each person had simply left the computer the way they found "
            "it: open.",
            "(The office and its counter computer are invented for this post. The tips below follow the "
            "help pages of Google and the baseline from earlier parts of this series.)",
            "Part 32 covered romance scams that target people one by one. This part looks at a risk that "
            "sits on office desks: a computer shared by several people. You will learn why sharing a "
            "computer is different from sharing a stapler, how separate accounts and screen locks help, why "
            "passwords should not be saved in a shared browser, when to use guest mode, how to leave no files "
            "or printouts behind, and a short routine for the end of the day.",
            ("photo", "blog/cyber-shared.jpg", "Shared office computers: one account per person, lock the "
             "screen, keep passwords out of the browser, and leave nothing behind. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why a Shared Computer Is Different"),
            "A shared computer remembers more than people expect. Browsers keep people signed in, offer to "
            "save passwords, and fill in forms. Files land in the Downloads folder and stay there. The next "
            "person inherits all of it.",
            ("point", "Open sessions", "An email account left signed in lets the next person read, send and "
             "delete as you."),
            ("point", "Saved passwords", "A password saved in a shared browser is a password shared with "
             "everyone who uses that computer."),
            ("point", "Files left behind", "A list of taxpayers in the Downloads folder is personal "
             "information sitting where anyone can open it."),
            ("point", "No way to tell who did what", "If everyone uses one account, a deleted record or a "
             "strange email can’t be traced to a person, including the person who did nothing wrong."),
            "Section 20 of the Data Privacy Act of 2012 requires reasonable and appropriate security measures "
            "for personal information. Part 20 explained what that means at a desk. A shared computer is one "
            "of the places where it is tested daily.",
            ("h", "Habit 1: One Person, One Account"),
            "Rule 1 of the one-page baseline in Part 18 is “one person, one account.” It applies to the "
            "computer itself, not only to email and systems.",
            ("point", "Separate sign-ins", "Windows and other operating systems let a computer have more "
             "than one user account. Each person signs in with their own, and their files and browser stay "
             "in their own space."),
            ("point", "Separate system accounts", "The collection system, the email and the shared folders "
             "should each recognize the person, not the desk."),
            ("point", "Ask the person in charge of IT", "In an office, setting up accounts is their job. A "
             "short request listing who uses which computer is a good start."),
            ("h", "Habit 2: Lock the Screen When You Stand Up"),
            "A computer left unlocked for five minutes is a computer anyone can use as you for five minutes.",
            ("point", "The shortcut", "On Windows, hold the Windows logo key and press L. The screen locks "
             "and shows the sign-in screen."),
            ("point", "The automatic lock", "Set the screen to lock by itself after a few minutes of no use, "
             "as a backup for the times you forget."),
            ("point", "Make it normal", "When everyone locks, nobody feels singled out. A friendly reminder "
             "beats a written warning."),
            ("h", "Habit 3: Keep Passwords Out of the Shared Browser"),
            ("point", "Say no to “save password”", "On a shared computer, choose Never when the browser "
             "offers to save a password."),
            ("point", "Sign out, don’t just close", "Closing a tab can leave you signed in. Use the Sign out "
             "option in the account menu."),
            ("point", "Use a password manager on your own device", "Part 2 explained password managers and "
             "two-factor authentication. Your personal manager belongs on your own phone or computer, not "
             "in a shared browser."),
            ("h", "Habit 4: Personal Browsing Belongs in Guest Mode"),
            "Sometimes a person needs to check a personal account on an office computer. Google’s Chrome help "
            "describes guest mode for exactly this kind of situation: it is meant for shared or public "
            "computers.",
            ("point", "What it does", "Google says pages you visit in guest mode won’t appear in the browser "
             "history, and your history, cookies and site data are deleted when you leave."),
            ("point", "What it does not do", "The same page says your activity may still be visible to the "
             "websites you visit, to your internet service provider, and to your employer or the network "
             "operator."),
            ("point", "How to open it", "In Chrome on a computer, select the profile icon at the top right, "
             "then open the Guest profile."),
            ("point", "Files still need care", "Google’s page does not say that downloaded files are removed. "
             "Delete anything you downloaded before you close the window."),
            ("h", "Habit 5: Leave No Files or Printouts Behind"),
            ("point", "Save work where it belongs", "Office files go to the office’s shared folder, with the "
             "access settings Part 21 described, not to the desktop or Downloads folder of a shared computer."),
            ("point", "Clear the Downloads folder", "At least once a day, delete the files you downloaded. "
             "Empty the Recycle Bin too."),
            ("point", "Collect printouts at once", "A payslip or a taxpayer list left on the printer is a "
             "data leak on paper."),
            ("point", "Be careful with flash drives", "Plug in only drives you trust, and remove yours "
             "when you leave."),
            ("h", "If You Find Something Left Open"),
            "Sooner or later, someone will sit down at a computer where a colleague is still signed in. "
            "What happens next matters.",
            ("point", "Don’t look around", "Sign the account out or close the window without reading or "
             "changing anything."),
            ("point", "Tell the person", "A quiet word helps more than a group chat message."),
            ("point", "Report anything sensitive", "If personal information was exposed, tell the person in "
             "charge, following the incident steps in Part 9."),
            ("photo", "blog/cyber-shared-routine.jpg", "Two routines for a shared computer: one for a short "
             "break, one for the end of the day. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "An End-of-Day Routine"),
            "Habits stick better as a routine. A five-step check, taped beside the monitor, works for the "
            "whole office.",
            ("point", "1. Sign out of every account", "Email, the collection system, social media."),
            ("point", "2. Close the browser", "All windows, including guest windows."),
            ("point", "3. Clear your files", "Downloads, desktop and the Recycle Bin."),
            ("point", "4. Collect your papers", "From the printer and the desk."),
            ("point", "5. Sign out of the computer", "Or shut it down, following office practice."),
            ("quote", "Leave the shared computer the way you would want to find it: empty."),
            ("h", "Mistakes to Avoid"),
            ("point", "One sign-in for the whole counter", "Ask for one account per person."),
            ("point", "Walking away unlocked", "Windows logo key plus L, every time."),
            ("point", "Saving passwords in a shared browser", "Choose Never."),
            ("point", "Trusting guest mode with downloads", "Delete your files yourself."),
            ("h", "Stay-Safe Reminders"),
            ("point", "One person, one account", "On the computer and in every system."),
            ("point", "Lock, then leave", "A shortcut plus an automatic lock."),
            ("point", "Guest mode for personal browsing", "It clears history and cookies, not visibility."),
            ("point", "Leave nothing behind", "Files, sessions and printouts."),
            ("h", "Your Part 33 Action Plan"),
            ("point", "Today", "Press Windows logo key and L the next time you stand up."),
            ("point", "This week", "Open the browser’s saved passwords on a shared computer, and remove any "
             "that belong to you."),
            ("point", "This month", "Tape the five-step routine beside each shared computer, and ask IT for "
             "separate accounts."),
            "By Friday, the front counter computer had three user accounts, a screen that locked itself after "
            "five minutes, and a small card taped to the monitor. On Monday, the first clerk to sit down found "
            "a sign-in screen, and nothing else.",
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("cta", "Read: Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk", "/blog/cybersecurity-part-20-privacy-at-work/"),
            ("cta", "Read: Cybersecurity Series, Part 21: Sharing Files Safely, Links, Attachments and Who Can See Them", "/blog/cybersecurity-part-21-safe-file-sharing/"),
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("ask", "How many people share the computer nearest to you, and does each one have their own sign-in?"),
        ],
    },
    {
        "date": "January 21, 2028",
        "title": "Cybersecurity Series, Part 32: Romance Scams, When the Person Online Asks for Money",
        "slug": "cybersecurity-part-32-romance-scams",
        "category": "security",
        "summary": "A romance scam can take weeks of kind messages before the first request for money. This "
                   "part explains how these scams unfold, the excuses that come up in reports to the US "
                   "Federal Trade Commission, why being asked to receive and forward money can make you part "
                   "of a crime under Philippine law, and what to do if you have already sent money.",
        "publish_on": "2028-01-21 21:00",
        "body": [
            "Tita Rosa, a retired teacher, had been widowed for three years when a man named Daniel sent her "
            "a friend request. His profile said he was an engineer on an offshore oil rig. He wrote every "
            "morning and every night. He remembered the names of her grandchildren and asked about her "
            "blood pressure. After six weeks, he said he had sent her a package with a gift, and the courier "
            "needed ₱18,000 for customs before it could be released.",
            "She paid. Two weeks later, he asked for a bigger favor: a friend would send money to her account, "
            "and she should send it on to another account, because his own bank was blocked offshore.",
            "(Tita Rosa and Daniel are invented for this post. The figures from the US Federal Trade "
            "Commission and the Philippine law quoted below are real and cited.)",
            "Part 31 looked at fake aid pages that ask for a fee. This part looks at a scam that asks for "
            "trust first and money later. You will learn how romance scams unfold, the excuses scammers use, "
            "why the request to pass money along is especially dangerous, how to check a new online friend, "
            "and what to do if you or someone you love has already paid.",
            ("photo", "blog/cyber-romance.jpg", "Romance scams: they build trust, then ask for money, and "
             "sometimes ask you to move money for them. Never send or forward money for someone you have "
             "not met. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What the Numbers Say"),
            "Philippine figures for romance scams alone are hard to find, so the clearest numbers come from "
            "the United States. In a Data Spotlight published February 9, 2023, the Federal Trade "
            "Commission reported the following for 2022:",
            ("point", "Reports", "Nearly 70,000 people reported a romance scam."),
            ("point", "Losses", "Reported losses reached $1.3 billion, with a median loss of $4,400 per person."),
            ("point", "Where it started", "About 40 percent of people who lost money said the contact began "
             "on social media, and 19 percent on a website or app."),
            ("point", "How they paid", "Cryptocurrency and bank wires made up more than 60 percent of "
             "reported losses. Gift cards were the method reported most often."),
            "These are reported cases only. The US Commodity Futures Trading Commission, citing the "
            "same $1.3 billion, says actual losses are likely much higher.",
            ("h", "How a Romance Scam Unfolds"),
            "The FTC describes romance scammers as people who “play the long game.” The pattern below is a "
            "typical one, not a script every scammer follows.",
            ("point", "1. Contact", "A friend request, a message on a dating app, or a “wrong number” text "
             "that turns into a friendly chat."),
            ("point", "2. Trust", "Daily messages, compliments, and attention to your family and health. The "
             "conversation may move to WhatsApp, Telegram or another private app."),
            ("point", "3. A reason not to meet", "A job abroad, a military post, an offshore rig. Each time, "
             "there is a reason the video call fails or the visit is postponed."),
            ("point", "4. The first request", "A fee for a package, a hospital bill, a plane ticket, or an "
             "investment they want to “teach” you."),
            ("point", "5. More requests", "Each payment is followed by a new problem that needs more money."),
            ("point", "6. Moving money for them", "A request to receive money and send it somewhere else."),
            ("photo", "blog/cyber-romance-steps.jpg", "How a romance scam unfolds, step by step. The danger "
             "rises at step 4, when money is first mentioned. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "The Excuses Scammers Use"),
            "The FTC’s 2023 spotlight listed the lies that came up in reports. A few of them:",
            ("point", "“I’m on a military base or an oil rig”", "A reason they cannot meet. The FTC called the "
             "military base the most popular excuse."),
            ("point", "“I’m sick, hurt or in jail”", "An emergency that needs money now."),
            ("point", "“Let me teach you to invest”", "The FTC mentions cryptocurrency, and warns that the money "
             "you “invest” goes straight to the scammer."),
            ("point", "“I sent you a package”", "And now it needs a customs fee. The FTC says if someone tells "
             "you to send money to receive a package, “you can bet it’s a scam.”"),
            ("h", "Why “Just Pass It Along” Is Dangerous"),
            "Tita Rosa’s second request was the more serious one. The US Commodity Futures Trading "
            "Commission warns that romance scam victims may be recruited as money mules, people who receive "
            "and move money obtained through fraud, sometimes without knowing it.",
            "In the Philippines, Republic Act No. 12010, the Anti-Financial Account Scamming Act, approved "
            "July 20, 2024, lists money mule acts in Section 4. They include using, borrowing or allowing the "
            "use of a financial account, and selling or lending one, to obtain, receive, deposit, transfer or "
            "withdraw proceeds known to come from crimes or social engineering schemes.",
            ("point", "The money is someone else’s loss", "The “friend’s” money sent to your account may come "
             "from another victim."),
            ("point", "Your name is on the account", "Investigators trace the account first. Explaining that "
             "you were deceived takes time and stress, even when it is true."),
            ("point", "The rule is simple", "The CFTC’s advice: never agree to move money for someone you "
             "have never met face to face."),
            ("h", "Warning Signs"),
            ("point", "They want to leave the app quickly", "And continue on a private chat."),
            ("point", "They cannot meet or video call", "Or the video is blurry, short or frozen each time. Part "
             "22 explained that video and voice can now be faked, so even a call is not proof."),
            ("point", "Money enters the conversation", "For any reason, after weeks of no money talk."),
            ("point", "They ask for secrecy", "“Don’t tell your children, they won’t understand.”"),
            ("point", "They ask you to receive and send money", "Stop at once."),
            ("h", "Checks You Can Make"),
            ("point", "Search the photo", "The FTC suggests a reverse image search of profile pictures. If the "
             "same face appears under other names, the profile is likely fake."),
            ("point", "Tell someone you trust", "The FTC advises talking to friends or family about a new love "
             "interest and paying attention if they are worried."),
            ("point", "Ask for a live meeting in a public place", "Someone who always has a reason to refuse "
             "is giving you an answer."),
            ("h", "If Money Has Already Been Sent"),
            ("point", "Stop sending", "No further payments, whatever the new reason."),
            ("point", "Do not forward any money you received", "Tell your bank or e-wallet about it instead, as "
             "the CFTC advises."),
            ("point", "Contact your bank or e-wallet at once", "Report the transfers and ask what they can do."),
            ("point", "Report it", "Call the CICC hotline 1326 or go to the PNP Anti-Cybercrime Group. Keep "
             "screenshots of the profile, the messages and the payment receipts."),
            ("point", "Watch for “recovery” offers", "Someone who promises to get your money back for a fee "
             "may be the same scam with a new face."),
            ("h", "Talk Without Shame"),
            "People who fall for romance scams are not foolish. Scammers spend weeks earning trust, and "
            "loneliness is not a weakness. If a parent, aunt or friend is in one, ask questions gently. "
            "Anger can push a person closer to the scammer, who seems to have endless patience.",
            ("h", "Mistakes to Avoid"),
            ("point", "Paying “just this once”", "The first payment is followed by the next request."),
            ("point", "Moving money for an online friend", "It can make you a money mule."),
            ("point", "Keeping it secret", "Secrecy protects the scammer, not you."),
            ("point", "Trusting a video call alone", "Faces and voices can be faked."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Trust first, money later", "That is the pattern."),
            ("point", "Packages and customs fees are a classic lie", "The FTC calls it a sure sign of a scam."),
            ("point", "Never receive and forward money", "RA 12010 penalizes money mule acts."),
            ("point", "Report quickly", "Bank or e-wallet first, then CICC 1326 or the PNP."),
            ("h", "Your Part 32 Action Plan"),
            ("point", "Talk to older relatives", "Especially those who live alone or were recently widowed. "
             "Share the warning signs above."),
            ("point", "Agree on a family rule", "No money sent to anyone met online without talking to someone "
             "in the family first."),
            ("point", "Learn the reverse image search", "Try it once on a photo, so you know how before you "
             "need it."),
            "Tita Rosa did not send the money on. Her nephew noticed a large deposit from a stranger and "
            "asked her about it. Together they searched Daniel’s photo and found it on three other profiles "
            "under three other names. They called the bank that afternoon and reported the account to the "
            "CICC. She still checks her messages every morning, but now she also calls her nephew on Sundays.",
            ("cta", "Read: Cybersecurity Series, Part 31: Fake Ayuda Pages, When “Government Aid” Is a Trap", "/blog/cybersecurity-part-31-fake-ayuda-pages/"),
            ("cta", "Read: Cybersecurity Series, Part 26: Job and Investment Scams, When Easy Money Asks You to Pay First", "/blog/cybersecurity-part-26-job-and-investment-scams/"),
            ("cta", "Read: Cybersecurity Series, Part 22: Deepfakes and Cloned Voices, When Seeing and Hearing Is Not Enough", "/blog/cybersecurity-part-22-deepfakes-and-voice-clones/"),
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("ask", "Has someone in your family ever been asked for money by a person they met only online?"),
        ],
    },
    {
        "date": "January 12, 2028",
        "title": "Cybersecurity Series, Part 31: Fake Ayuda Pages, When “Government Aid” Is a Trap",
        "slug": "cybersecurity-part-31-fake-ayuda-pages",
        "category": "security",
        "summary": "Posts and texts promising cash aid from the government can be bait for your personal "
                   "data or your money. This part explains what the DSWD has said about fake pages and "
                   "links, how its real assistance programs work, the warning signs of a fake offer, and "
                   "what to do if you already filled in a form.",
        "publish_on": "2028-01-12 21:00",
        "body": [
            "Aling Mercy runs a small sari-sari store and shares a phone with her daughter. One evening, a "
            "post appeared in a neighborhood group: “DSWD ₱10,000 cash aid for minimum wage earners. "
            "Register here before slots run out.” The page had the agency’s logo, a photo of a ribbon "
            "cutting, and hundreds of comments saying “Done po!” She tapped the link, typed her full name, "
            "birthday, address and mobile number, and uploaded a photo of her ID.",
            "The last screen asked for a ₱150 “processing fee” through an e-wallet. That was when her "
            "daughter took the phone.",
            "(Aling Mercy and the post are illustrations for this lesson. The warnings from the DSWD quoted "
            "below are real and are dated.)",
            "Part 30 looked at lending apps that reach into your contacts. This part looks at offers that "
            "pretend to give money instead of lending it. You will learn what the Department of Social "
            "Welfare and Development has said about fake pages and links, how its assistance is actually "
            "given, the signs that an aid offer is fake, how to check before you click, and the steps to "
            "take if you already shared your details.",
            ("photo", "blog/cyber-ayuda.jpg", "Fake ayuda offers: look for an assessment, not a link; "
             "check the official page; never pay to receive aid; report the post. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Aid Is Used as Bait"),
            "Aid offers work as bait because they reach people who need help and because real programs "
            "do exist. A scammer does not have to invent a program. Borrowing the name of a real one is "
            "enough.",
            ("point", "The name is familiar", "AKAP, AICS and educational assistance are real programs that "
             "people have heard of on the news."),
            ("point", "The need is real", "Someone short of money for tuition or medicine has a strong "
             "reason to act quickly."),
            ("point", "The prize is your data", "Even without a fee, a form with your name, birthday, "
             "address, number and ID photo is useful to someone opening accounts or loans in your name."),
            ("quote", "If the aid comes with a link and a fee, the only one receiving help is the sender."),
            ("h", "What the DSWD Has Said"),
            "The DSWD has warned the public about fake pages and messages several times. Four of those "
            "warnings show the pattern.",
            ("point", "June 2024: a fake AKAP page", "The DSWD said a Facebook page using the name “AKAP "
             "Financial Assistance Program” was not part of its official page, and asked the public not "
             "to engage with it and to report it (Inquirer, June 11, 2024)."),
            ("point", "July 2024: TikTok and other accounts", "The DSWD warned that accounts offering "
             "educational assistance carried false information and might gather personal data that "
             "scammers could use for theft. It said AICS clients go through an interview and assessment, "
             "and that the aid is given through its Crisis Intervention Units and field offices "
             "(Philippine News Agency, July 9, 2024)."),
            ("point", "November 2024: misleading AKAP posts", "Spokesperson Irene Dumlao warned against "
             "online posts misinforming the public about AKAP. She said the amount of aid depends on a "
             "social worker’s assessment after an interview (Daily Tribune, November 2024)."),
            ("point", "Texts about student aid", "The DSWD has said, “DSWD is not sending out links or any "
             "survey to avail of an educational assistance,” and asked the public not to click such links "
             "(Malaya Business Insight)."),
            ("h", "How Real Assistance Works"),
            "Programs and rules change, so check the current details with the DSWD. The warnings above "
            "describe three features to look for, and a fake offer can leave all three out.",
            ("point", "An assessment", "For AICS and AKAP, the DSWD described an interview and an assessment "
             "by a social worker before aid is given. A form that approves you in minutes skips the step "
             "the agency itself describes."),
            ("point", "An official channel", "The DSWD named its Crisis Intervention Units, its field "
             "offices and its verified Facebook page, facebook.com/dswdserves, as official sources."),
            ("point", "An amount that depends on need", "In the November 2024 warning, AKAP aid ranged from "
             "₱1,000 to ₱10,000 based on the assessment. A post promising the same fixed amount to everyone "
             "who registers does not match that description."),
            ("h", "Seven Warning Signs of a Fake Offer"),
            ("point", "A fee to receive aid", "A processing, release or membership fee before the money "
             "arrives."),
            ("point", "A deadline and “limited slots”", "Pressure to act tonight, before you can check."),
            ("point", "A link in a text or a group post", "Especially a shortened link or a web address that "
             "is not a .gov.ph site. Part 15 explained how to read a web address."),
            ("point", "A page that is not the verified one", "A different name, a recent creation date, or "
             "few posts other than the offer."),
            ("point", "Requests for an ID photo and a selfie", "Together, these can be used to open an "
             "e-wallet or a loan in your name."),
            ("point", "Requests for a one-time PIN", "The aid process the DSWD describes uses interviews, not "
             "codes. Do not share the code sent to your phone with anyone."),
            ("point", "Comments that all say “Done”", "Comments are easy to fake, and they prove nothing "
             "about the page."),
            ("h", "Check Before You Click"),
            ("point", "Go to the source yourself", "Open the DSWD’s verified page or website by typing it, "
             "not through the link in the post, and look for the same announcement."),
            ("point", "Ask your barangay or municipal social welfare office", "They can tell you which "
             "programs are open in your area and how to apply."),
            ("point", "Ask someone else to look", "Aling Mercy’s daughter noticed the fee in seconds. A "
             "second pair of eyes is a cheap safeguard."),
            ("h", "If You Already Filled In the Form"),
            ("point", "Do not pay", "If you have not paid, stop. If you have, keep the receipt and the "
             "reference number."),
            ("point", "Report the payment to your e-wallet or bank", "Ask them to flag the receiving account."),
            ("point", "Watch for follow-up messages", "Scammers with your details may call pretending to be "
             "the DSWD, a bank or a courier. Never give a one-time PIN."),
            ("point", "Report the page and the scam", "Report the post on the platform. You can also call "
             "the Cybercrime Investigation and Coordinating Center (CICC) hotline 1326, mentioned in earlier parts of this series."),
            ("point", "Check for accounts in your name", "If you sent an ID photo, watch for unfamiliar "
             "loan or e-wallet messages in the weeks that follow."),
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting the logo", "Anyone can copy a logo and a photo."),
            ("point", "Paying a small fee", "A small fee is still a sign of a scam, and it confirms you will pay."),
            ("point", "Sharing the post to help others", "Check first, or you spread the bait."),
            ("point", "Staying silent after sharing data", "Act early, while it can still help."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Real aid involves an assessment", "As the DSWD has described for AICS and AKAP."),
            ("point", "The DSWD says it does not send aid links", "For educational assistance, in its own words."),
            ("point", "No fee to receive aid", "Treat any fee as a warning sign."),
            ("point", "Check at the source", "The verified page, your local social welfare office or a "
             "field office."),
            ("h", "Your Part 31 Action Plan"),
            ("point", "Save the official page", "Follow the DSWD’s verified page so real announcements reach you."),
            ("point", "Talk to older relatives", "Show them a sample fake post and the seven warning signs."),
            ("point", "Agree on a rule at home", "Nobody pays or sends an ID photo for “aid” without asking "
             "someone else first."),
            "Aling Mercy did not pay the fee. Her daughter reported the page, and the next morning they "
            "went to the municipal social welfare office and asked which help was really available. The "
            "answer took longer than ten minutes. It also did not ask for a single peso.",
            ("cta", "Read: Cybersecurity Series, Part 30: Online Lending Apps, Your Contacts and the Rules Lenders Must Follow", "/blog/cybersecurity-part-30-online-lending-apps/"),
            ("cta", "Read: Cybersecurity Series, Part 26: Job and Investment Scams, When Easy Money Asks You to Pay First", "/blog/cybersecurity-part-26-job-and-investment-scams/"),
            ("cta", "Read: Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address", "/blog/cybersecurity-part-15-fake-websites/"),
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("ask", "Have you or someone in your family ever seen an aid post that turned out to be fake? What gave it away?"),
        ],
    },
    {
        "date": "January 3, 2028",
        "title": "Cybersecurity Series, Part 30: Online Lending Apps, Your Contacts and the Rules Lenders Must Follow",
        "slug": "cybersecurity-part-30-online-lending-apps",
        "category": "security",
        "summary": "A loan app approves you in minutes, then asks for your contacts, your photos and your "
                   "location. This part explains what Philippine regulators allow lenders to do, the "
                   "interest caps on small loans, the collection practices that are prohibited, and how to "
                   "protect yourself before and after you borrow.",
        "publish_on": "2028-01-03 21:00",
        "body": [
            "Ramon needed ₱5,000 for his son’s school project and a tricycle repair. A lending app on his "
            "phone promised approval in ten minutes. It asked to see his contacts, his photos and his "
            "location, and he tapped Allow on every screen. The money arrived, minus a “service fee” he had "
            "not noticed. Two days after the due date, his sister, his barangay captain and his former "
            "teacher received the same message: Ramon was a scammer who refused to pay his debts.",
            "He had been one day short of the full amount. Now half his contact list knew.",
            "(Ramon and his loan are made up for this post. Any resemblance to a real person or lender is "
            "unintended.)",
            "Part 29 cleared old phones before letting them go. This part looks at an app that can reach "
            "into a phone you still use. Read on, and you will learn what the National Privacy Commission "
            "says lending apps may and may not take from your phone, what the Securities and Exchange "
            "Commission lists as unfair collection practices, the caps on interest for small loans, the "
            "checks to make before you borrow, and what to do if a lender harasses you or your contacts.",
            ("photo", "blog/cyber-lending.jpg", "Online lending apps: check the lender, deny the contacts, "
             "read the total cost, and report harassment. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Why Loan Apps Ask for So Much"),
            "An app can request permissions to read your contacts, photos, camera, location and messages. "
            "Some of these are needed to verify who you are. Others, the regulators say, are not, and have "
            "been used to shame borrowers into paying.",
            ("point", "Your contacts", "A list of the people you know, with their numbers."),
            ("point", "Your photos", "Including your ID and your face, taken for verification."),
            ("point", "Your social media", "Friends and family lists, reachable with one message."),
            ("quote", "A loan should cost you interest, not your privacy or your name."),
            ("h", "What the Privacy Commission Says"),
            "In October 2020, the National Privacy Commission announced NPC Circular No. 20-01, its "
            "guidelines on processing personal data for loan-related transactions. As the NPC described "
            "it:",
            ("point", "Contacts are an unnecessary permission", "Accessing a borrower’s phone contacts or "
             "email list is treated as unnecessary. Lenders may not copy or save contacts for debt "
             "collection or to harass borrowers or their contacts."),
            ("point", "Social media is barred too", "Harvesting social media contacts is likewise not "
             "allowed for collection or harassment."),
            ("point", "Photos only for identity checks", "Camera access is allowed for know-your-customer "
             "checks, and the borrower’s photo must not be used to harass or embarrass them over a "
             "delinquent loan."),
            ("point", "Turn permissions off", "Apps must prompt users to turn off permissions once their "
             "purpose is achieved."),
            "The NPC later amended these guidelines with NPC Circular No. 2022-02. If you need the details "
            "for a complaint, read both on the NPC’s website.",
            ("h", "What the SEC Prohibits in Collection"),
            "SEC Memorandum Circular No. 18, Series of 2019, prohibits unfair debt collection practices by "
            "financing and lending companies. Among the practices it lists:",
            ("point", "Threats", "Threatening to take any action that cannot legally be taken."),
            ("point", "Insults", "Obscene, insulting or profane language meant to abuse the borrower."),
            ("point", "Public shaming", "Disclosing or publishing the names and personal information of "
             "borrowers who allegedly refuse to pay, except as the circular allows."),
            ("point", "False claims", "Any false representation or deceptive means to collect a debt."),
            ("point", "Late-night calls", "Contact before 6 a.m. or after 10 p.m., unless the account is more "
             "than 15 days past due or the borrower has expressly agreed."),
            ("point", "Your contact list", "Contacting people in the borrower’s contact list, other than named "
             "guarantors or co-makers, is an unfair practice even if the borrower consented."),
            "The message Ramon’s sister received broke several of these at once.",
            ("h", "The Caps on Small Loans"),
            "The Bangko Sentral ng Pilipinas set ceilings on small, short loans in Circular No. 1133, Series "
            "of 2021. The SEC applied them to lending and financing companies through Memorandum Circular "
            "No. 3, Series of 2022, effective March 3, 2022, as BusinessWorld reported.",
            ("point", "Which loans", "Unsecured, general-purpose loans of not more than ₱10,000, with a term "
             "of up to four months."),
            ("point", "Interest", "A nominal interest rate of at most 6 percent a month, or 0.2 percent a "
             "day."),
            ("point", "Total monthly cost", "An effective interest rate, fees included, of at most 15 percent "
             "a month."),
            ("point", "Late penalties", "At most 5 percent a month on the amount due."),
            ("point", "Overall ceiling", "Total charges capped at 100 percent of the amount borrowed."),
            "A column in the Daily Tribune in September 2025 reported that the caps were still being "
            "enforced, and that the SEC was studying whether to lower them. Rules can change, so check the "
            "SEC’s current advisories before relying on these numbers.",
            "Here is what the 15 percent ceiling means in pesos. On a ₱5,000 loan for one month, the "
            "interest and fees together should not exceed ₱750. If an app deducts ₱1,500 as a “service "
            "fee” before the money reaches you, ask whether it is within the cap, and keep the screenshot.",
            ("h", "Before You Borrow"),
            ("point", "Check the lender", "The SEC issues Certificates of Authority to lending and financing "
             "companies, and can revoke them. Look up the company name, not just the app name, in the "
             "SEC’s lists and advisories."),
            ("point", "Read the total cost", "Look for the amount you will receive, the amount you must "
             "repay, and the due date. If the app cannot show them before you accept, do not accept."),
            ("point", "Deny what is not needed", "Do not allow access to contacts, messages or social media. "
             "On Android and iPhone, you can review and remove an app’s permissions in Settings at any time."),
            ("point", "Borrow from a known source first", "A cooperative, your employer’s loan program or a "
             "bank you already use may cost less and come with a person you can talk to."),
            ("h", "If a Lender Harasses You"),
            ("point", "Save everything", "Screenshots of messages, call logs, the app’s screens and your "
             "payment records."),
            ("point", "Warn your contacts", "A short message: “A lending app may send messages about me. "
             "Please ignore and forward them to me.” This takes away the shame the lender is counting on."),
            ("point", "Remove permissions", "Turn off the app’s access to contacts, photos and location, "
             "then uninstall it after saving what you need."),
            ("point", "Report it", "Unfair collection practices go to the SEC. Misuse of your personal "
             "data goes to the National Privacy Commission. Threats can be reported to the CICC hotline "
             "1326 or the PNP Anti-Cybercrime Group."),
            ("point", "Keep paying what you truly owe", "Harassment does not cancel a valid debt, and "
             "paying it on record protects you. Pay through official channels and keep the receipt."),
            ("h", "For Treasury Workers"),
            "Salary loans and emergencies reach government offices too. If a colleague is being shamed by "
            "a lending app, the first help is practical: show them how to save the evidence, warn their "
            "contacts and file a report. And if a lender messages your office phone about a co-worker, do "
            "not forward it or discuss it. It is personal information, and Part 20 explained the duty to "
            "protect it.",
            ("h", "Mistakes to Avoid"),
            ("point", "Tapping Allow on every screen", "Deny contacts, messages and social media access."),
            ("point", "Borrowing without seeing the total", "Know the amount received and the amount due."),
            ("point", "Hiding the harassment", "Warn your contacts and report it."),
            ("point", "Deleting the app first", "Save the evidence, then remove it."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Contacts are off limits", "The NPC treats contact list access as unnecessary for lending."),
            ("point", "Shaming is prohibited", "The SEC lists contacting your contacts and publishing names as unfair practices."),
            ("point", "Small loans have caps", "6 percent nominal and 15 percent effective a month, under the 2021 and 2022 rules."),
            ("point", "Report to the right office", "SEC for collection, NPC for privacy, CICC 1326 for threats."),
            ("h", "Your Part 30 Action Plan"),
            ("point", "Today", "Open Settings on your phone and check which apps can read your contacts. "
             "Remove access from any app that does not need it."),
            ("point", "This week", "If you have a loan app installed, find the company name, look it up with "
             "the SEC, and check the total cost of your loan."),
            ("point", "Share it", "Send the three reporting offices, SEC, NPC and CICC 1326, to your family "
             "group chat."),
            "If you never borrow online, the first step still helps. Other apps can ask for contacts too, "
            "and the setting to remove that access is the same.",
            "Ramon saved the screenshots, sent his contacts a short warning, and filed complaints with the "
            "SEC and the NPC. He paid the remaining balance through the app’s official channel and kept the "
            "receipt. His sister replied to his warning with a thumbs-up and one line: “Already deleted it.”",
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 26: Job and Investment Scams, When Easy Money Asks You to Pay First", "/blog/cybersecurity-part-26-job-and-investment-scams/"),
            ("cta", "Read: Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk", "/blog/cybersecurity-part-20-privacy-at-work/"),
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet, Securing It Before It Is Lost", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("ask", "Which apps on your phone can read your contacts right now, and do they need to?"),
        ],
    },
    {
        "date": "December 24, 2027",
        "title": "Cybersecurity Series, Part 29: Before You Sell, Donate or Throw Away a Phone or Laptop",
        "slug": "cybersecurity-part-29-wiping-old-devices",
        "category": "security",
        "summary": "An old phone or laptop can still hold your messages, photos, saved passwords and work "
                   "files. This part walks through what to do before a device leaves your hands: back up, "
                   "sign out, remove cards, reset properly, and handle office devices and broken drives with "
                   "extra care.",
        "publish_on": "2027-12-24 21:00",
        "body": [
            "Liza bought a new phone and sold her old one to a neighbor’s son for a fair price. She "
            "deleted her photos one by one the night before, closed her apps, and handed it over. Two "
            "days later, her sister called. “Why is your Facebook liking posts at two in the morning?” "
            "The neighbor’s son had opened the app. Liza had never signed out. Her deleted photos were "
            "still in a folder she did not know about, and her e-wallet app was still on the home screen.",
            "Nothing was stolen. But for two days, a stranger had a key to her accounts, and she had "
            "handed it over herself.",
            "(Liza and her neighbor are made up for this post. Any resemblance to a real person is "
            "unintended.)",
            "Part 12 secured a phone before it could be lost. This part covers the day you let it go on "
            "purpose: selling it, giving it to a relative, trading it in, or throwing it away. By the end, "
            "you will know the steps that matter for phones and laptops, why deleting files one by one is "
            "not enough, how to keep from locking out the next owner, and what extra care an office device "
            "needs.",
            ("photo", "blog/cyber-wipe.jpg", "Before a device leaves your hands: back up, sign out, take out "
             "the cards, reset it properly, and check that nothing of yours is left. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Deleting Is Not Enough"),
            "Deleting a photo can move it to a recently deleted folder. Closing an app does not sign you "
            "out of it. A device that has been used for years holds far more than what shows on the home "
            "screen: saved passwords, messages, account sessions, downloaded files and backups.",
            "A factory reset is designed to erase the data on the device and return it to the way it left "
            "the factory. But a reset is only one step. Before it come the steps that protect your accounts "
            "and your copy of your own information.",
            ("quote", "Selling a phone is like selling a house. Take your things out, then change the "
             "locks, then hand over the keys."),
            ("h", "Step 1: Back Up What You Want to Keep"),
            "The US Federal Trade Commission’s consumer advice on getting rid of a phone starts here: back "
            "up your phone so you have a copy of your information. Apple’s guide for iPhones also begins "
            "with a backup.",
            ("point", "Photos and videos", "Copy them to your new device, a computer or a cloud account "
             "you control."),
            ("point", "Chats", "Messaging apps have their own backup settings. Check each one you use."),
            ("point", "Two-factor codes", "If an authenticator app holds codes for your accounts, move them "
             "to the new phone, or set up two-factor again on each account, before erasing the old one. Otherwise you may lock yourself out."),
            ("point", "Check the backup", "Open a few photos and messages on the new device before erasing "
             "the old one."),
            ("h", "Step 2: Sign Out of Your Accounts"),
            "This is the step Liza missed, and the one that protects you after the device is gone.",
            ("point", "Android", "Google’s help explains that a protected device asks, after a factory "
             "reset, for the screen lock or the password of a Google Account that was on the device. If "
             "the new owner cannot give it, the page says they will not be able to use the device at all. "
             "To turn this protection off, Google says to remove your Google Account from the device. Do "
             "this before the reset, so the buyer is not stuck."),
            ("point", "iPhone", "Apple’s guide says to sign out of your Apple Account in Settings before "
             "erasing, and to unpair any Apple Watch. It warns not to delete contacts, calendars, "
             "reminders, documents or photos by hand while signed in to iCloud, because that removes them "
             "from iCloud and from your other devices too."),
            ("point", "Apps that hold money", "Sign out of e-wallet and banking apps, and remove saved "
             "cards from payment apps. Part 13 covered why an e-wallet deserves the same care as cash."),
            ("point", "Social media and email", "Sign out on the device, then check each account’s list of "
             "logged-in devices from your new phone, and remove the old one if it still appears."),
            ("h", "Step 3: Take Out the Cards"),
            ("point", "SIM card", "The FTC’s advice says a SIM card may store personal information, and "
             "to remove it. If you will not reuse it, the FTC says to destroy it. Remember from Part 27 "
             "that in the Philippines a SIM is registered to your name."),
            ("point", "Memory card", "If the phone has an SD card for storage, the FTC says to remove it. "
             "A reset of the phone may not erase what is on the card."),
            ("point", "eSIM", "Apple’s guide says that on a phone with an eSIM, choose the option to erase "
             "the eSIM profile when prompted during the erase. If you are unsure, ask your network "
             "provider before you hand the phone over."),
            ("h", "Step 4: Reset It Properly"),
            ("point", "iPhone", "Apple’s path is Settings, then General, then Transfer or Reset, then "
             "Erase All Content and Settings. Apple notes that erasing also turns off Find My and "
             "Activation Lock, so the next owner can use the device."),
            ("point", "Android", "Use the factory reset option in Settings. The wording and menu "
             "differ from brand to brand, so search your phone maker’s help for the exact steps."),
            ("point", "After the reset", "Turn the device on. You should see the first setup screen, "
             "with none of your apps, photos or accounts. If anything of yours appears, stop and repeat "
             "the steps."),
            ("h", "Laptops and Computers"),
            "The same order applies: back up, sign out, then erase.",
            ("point", "Sign out", "Sign out of your browser profile, email, cloud storage and any password "
             "manager. Browsers can hold saved passwords and open sessions."),
            ("point", "Use the built-in reset", "Windows and macOS both offer official ways to erase the "
             "computer and reinstall the system. Use the official option for your computer, "
             "and choose the setting that removes your files, not the one that keeps them."),
            ("point", "Encryption helps", "Part 17 explained that encryption makes data unreadable without "
             "the key. A drive that was encrypted from the start is much safer to reset and pass on."),
            ("h", "Office Devices Need More Care"),
            "A treasury laptop or phone may hold taxpayer names, receipts and reports. The Data Privacy "
            "Act, covered in Part 20, expects offices to protect personal data, and that duty does not end "
            "when a device is replaced.",
            ("point", "Do not decide alone", "Office devices are government property. Follow your office’s "
             "rules for returning or disposing of equipment, and involve the person in charge of IT."),
            ("point", "Keep a record", "Write down which device was erased, by whom, on what date and how. "
             "If questions come up later, the record answers them."),
            ("point", "Know the standard", "For organizations, the US National Institute of Standards and "
             "Technology publishes guidelines for media sanitization, updated in September 2025. It "
             "defines sanitization as making access to the data infeasible for a given level of effort."),
            ("point", "Broken drives", "A drive that no longer works cannot be reset, but it may still hold "
             "readable data. Do not throw it in the trash. Ask your IT person how your office destroys "
             "such drives."),
            ("h", "If the Device Is Already Gone"),
            ("point", "Change passwords", "Start with email, then e-wallets, banking and social media."),
            ("point", "Remove the device", "From your Google or Apple account, and from each app’s list of "
             "logged-in devices."),
            ("point", "Ask the new owner", "Apple’s guide suggests asking the new owner to erase the device "
             "using the steps above. A family member or buyer you know may help."),
            ("point", "Watch your accounts", "Check for messages or payments you did not make over the next "
             "few weeks."),
            "Liza did all four. She changed her passwords from her new phone, removed the old phone from "
            "her Facebook and Google accounts, and asked her neighbor’s son to bring the phone back for an "
            "hour. Together they reset it, and he got a phone that was truly his.",
            ("h", "Mistakes to Avoid"),
            ("point", "Deleting files by hand", "Use the full reset instead."),
            ("point", "Resetting before signing out", "The buyer may be locked out, or your account may stay linked."),
            ("point", "Forgetting the cards", "Take out the SIM and memory card."),
            ("point", "Throwing a broken drive away", "It may still hold your data."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Back up first", "And check the backup on the new device."),
            ("point", "Sign out before the reset", "Google, Apple, e-wallets, social media and email."),
            ("point", "Remove the SIM and memory card", "Destroy a SIM you will not reuse."),
            ("point", "Office devices follow office rules", "With a written record of each erase."),
            ("h", "Your Part 29 Checklist"),
            "Copy this list and keep it with the device you plan to replace next.",
            ("point", "Before", "Back up, move authenticator codes, sign out of every account, remove cards "
             "from payment apps."),
            ("point", "During", "Take out the SIM and memory card, then run the full factory reset."),
            ("point", "After", "Turn it on, check the setup screen, then remove the device from your "
             "accounts’ device lists."),
            "Then look around your home for old phones in drawers. If one still has your accounts on it, "
            "it does not have to be sold to be a risk.",
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet, Securing It Before It Is Lost", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("cta", "Read: Cybersecurity Series, Part 17: Encryption Made Simple, Locking Data So a Lost Device Is Only a Lost Device", "/blog/cybersecurity-part-17-encryption-made-simple/"),
            ("cta", "Read: Cybersecurity Series, Part 27: Your SIM Is a Key, Registration, SIM Swaps and Lost Phones", "/blog/cybersecurity-part-27-sim-registration-and-sim-swaps/"),
            ("cta", "Read: Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk", "/blog/cybersecurity-part-20-privacy-at-work/"),
            ("ask", "How many old phones are in a drawer at your home, and is anyone still signed in on them?"),
        ],
    },
    {
        "date": "December 15, 2027",
        "title": "Cybersecurity Series, Part 28: Kids Online, Settings, Talks and Habits That Keep Them Safer",
        "slug": "cybersecurity-part-28-kids-online",
        "category": "security",
        "summary": "Children use the same apps and phones as adults, sometimes with fewer defenses. This part "
                   "covers the parental controls built into Android and iPhone, the scams aimed at young "
                   "gamers, what children should never share, and how to keep them talking to you when "
                   "something goes wrong.",
        "publish_on": "2027-12-15 21:00",
        "body": [
            "Ten-year-old Paolo wanted a rare skin for his character in an online game. A player he had "
            "met in the game offered him one for free. All Paolo had to do was log in on a website the "
            "player sent, “to receive the gift.” He typed his username and password, then his mother’s "
            "e-wallet number when the site asked for it “to verify age.” By evening, his game account was "
            "gone, and his mother had a text asking for a one-time code.",
            "(Paolo and his family are imagined for this lesson. The details are examples, not a report "
            "of a real case.)",
            "Part 27 protected your mobile number. This part protects the youngest people in your home. "
            "Keep reading and you will know what parental controls Android phones and iPhones offer, the "
            "tricks aimed at children in games and chats, what children should keep private, how to talk "
            "about it without making them hide things, and what the law and the hotlines offer if something "
            "serious happens.",
            ("photo", "blog/cyber-kids.jpg", "Kids online: set the controls, keep personal details private, "
             "spot fake gifts and strangers, and keep the conversation open. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Start With the Settings"),
            "Both major phone systems include free tools for parents. They do not replace attention, but "
            "they set limits that hold when you are not looking.",
            ("point", "Android: Google Family Link", "Google’s help says parents can approve or block apps "
             "the child wants to download, set daily screen time limits and a bedtime, see the location of "
             "the child’s device, and restrict mature content on Google Play."),
            ("point", "Who it is for", "Google’s help describes Family Link accounts for children under 13, "
             "or the applicable age in their country, and requires the parent to be an adult living in the "
             "same country."),
            ("point", "iPhone: Screen Time and Family Sharing", "Apple’s Screen Time includes downtime, app "
             "limits and content restrictions, and Family Sharing’s Ask to Buy sends purchase requests to a "
             "parent for approval."),
            "Set these up together with your child, and explain each one. A rule a child understands is "
            "easier to keep than one they discover.",
            ("quote", "Settings set the walls. Conversations keep the door open."),
            ("h", "Check the Age Rule Before Installing"),
            "Apps can set a minimum age in their terms. Facebook’s terms, for example, require users to be at least 13. Before installing an app for a child, read its age rule in the app store listing or the terms.",
            ("point", "Do not lie about the birth year", "An account opened with an older birth year may not get the settings the app gives younger users, and the child learns that rules are for getting around."),
            ("point", "Use the child’s own account", "A child using a parent’s account sees adult content settings and may have access to the parent’s saved payment details."),
            ("point", "Review once a year", "Children grow, and so do the apps they want. Look at the settings again on each birthday."),
            ("h", "Tricks Aimed at Young Gamers"),
            "Children are targets for the same reasons adults are: they have accounts worth stealing and sometimes access to money, a parent’s. The tricks are familiar from earlier parts of this series, "
            "dressed for a younger audience.",
            ("point", "The free gift", "Free skins, coins or items, if the player logs in on a website. That "
             "website is a fake login page, as in Part 15."),
            ("point", "The trade that needs a code", "A “friend” asks for the code that just arrived by text "
             "to “confirm the trade.” It is the account’s recovery code, as in Part 25’s verification code "
             "trick."),
            ("point", "The parent’s wallet", "Any request for a parent’s e-wallet number, card or code is a "
             "stop sign, whatever the reason given."),
            ("h", "What Children Should Keep Private"),
            ("point", "Passwords and codes", "Not shared with friends, even best friends. Parents may know "
             "them; nobody else."),
            ("point", "Where they are", "Home address, school name, uniform in photos, and real-time "
             "location."),
            ("point", "Family money details", "Parents’ e-wallet numbers, cards and one-time codes."),
            ("point", "Photos they would not show a teacher", "Once sent, a photo cannot be taken back."),
            ("h", "Strangers Online"),
            "Not every new contact is dangerous, and children make real friends in games. Some signs call "
            "for a pause.",
            ("point", "Gifts and favors", "Free items, game currency or load from someone they met online."),
            ("point", "Secrecy", "“Don’t tell your parents.” Any request for secrecy is a reason to tell."),
            ("point", "Moving to private chats", "Asking to continue on another app, away from the game’s own "
             "chat."),
            ("point", "Requests for photos or meetings", "These go to a parent right away."),
            "The rule for children is simple: if something online makes you feel uncomfortable, confused or "
            "pressured, tell an adult you trust, and you will not be in trouble for telling.",
            ("h", "Talk So They Keep Talking"),
            ("point", "Ask about their online life", "Which games, which friends, what they enjoy. Interest "
             "comes before rules."),
            ("point", "Do not punish the report", "If telling you about a problem means losing the phone, a "
             "child may stop telling. Deal with the problem, not the messenger."),
            ("point", "Use real examples", "Paolo’s story, or one from the news, makes the danger concrete "
             "without a lecture."),
            ("point", "Agree on the rules together", "Screen time, where devices stay at night, and what "
             "needs a parent’s yes."),
            ("h", "When It Is Serious"),
            "Republic Act No. 11930, which lapsed into law on July 30, 2022, is the Philippine law against "
            "online sexual abuse and exploitation of children. If a child is asked for sexual images, "
            "threatened, or pressured to meet someone, it is a matter for the authorities, not only the "
            "family.",
            ("point", "Keep the evidence", "Do not delete the chat. Take screenshots of the profile and the "
             "messages."),
            ("point", "Do not confront the account", "Block it after saving the evidence."),
            ("point", "Report it", "Call the CICC hotline 1326 or go to the PNP Anti-Cybercrime Group or the "
             "Women and Children Protection Desk at your local police station."),
            ("h", "For Treasury Workers"),
            "Office phones and laptops are not toys. If children use a shared family device that also opens "
            "work email or the office’s bank portal, separate them: a child profile or a different device. "
            "A game installed on a work phone brings its chats, links and in-app purchases with it.",
            ("h", "Mistakes to Avoid"),
            ("point", "Setting controls in secret", "Explain them, so the child does not work around them."),
            ("point", "Sharing a parent’s e-wallet on a child’s phone", "Keep payment apps off it, or locked."),
            ("point", "Punishing a child for telling", "Thank them, then fix the problem."),
            ("point", "Deleting evidence in anger", "Save it first, then block and report."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Use the built-in controls", "Family Link on Android, Screen Time on iPhone."),
            ("point", "Free gifts are bait", "Fake logins and code requests target young gamers."),
            ("point", "Some things stay private", "Passwords, codes, location and family money details."),
            ("point", "Keep them talking", "A child who reports early gives you time to act."),
            ("h", "Your Part 28 Action Plan"),
            ("point", "Today", "Ask your child which games and apps they use, and who they talk to there."),
            ("point", "This week", "Set up Family Link or Screen Time together, and explain each setting."),
            ("point", "This month", "Agree on three family rules, write them down, and post them near "
             "where devices charge at night."),
            "Tell your child, in those words, that they will never be in trouble for telling you about "
            "something that went wrong online.",
            "Paolo’s mother reported the e-wallet number to her provider and refused the code. Her account "
            "stayed safe. The game account was recovered with help from the game’s support page. That "
            "weekend, the family set up Family Link together, and Paolo wrote the first rule himself: “No "
            "free gifts from strangers.”",
            ("cta", "Read: Cybersecurity Series, Part 27: Your SIM Is a Key, Registration, SIM Swaps and Lost Phones", "/blog/cybersecurity-part-27-sim-registration-and-sim-swaps/"),
            ("cta", "Read: Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address", "/blog/cybersecurity-part-15-fake-websites/"),
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet, Securing It Before It Is Lost", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("cta", "Read: Cybersecurity Series, Part 25: Online Marketplace Scams, Buying and Selling Without Getting Burned", "/blog/cybersecurity-part-25-online-marketplace-scams/"),
            ("ask", "What is one online rule your family agreed on, and did it work?"),
        ],
    },
    {
        "date": "December 6, 2027",
        "title": "Cybersecurity Series, Part 27: Your SIM Is a Key, Registration, SIM Swaps and Lost Phones",
        "slug": "cybersecurity-part-27-sim-registration-and-sim-swaps",
        "category": "security",
        "summary": "Your mobile number receives the codes that open your bank, e-wallet and email. This part "
                   "explains what the SIM Registration Act requires, how a SIM swap lets someone else "
                   "receive those codes, the warning signs, and what to do in the first hour if your number "
                   "stops working.",
        "publish_on": "2027-12-06 21:00",
        "body": [
            "On a Thursday afternoon, the signal bars on Nora’s phone disappeared. She assumed the network "
            "was down and kept working. By the time she noticed that her officemates still had signal, "
            "someone had used her number to receive a one-time code and reset the password of her e-wallet. "
            "Her phone was still in her hand the whole time. Her number was not.",
            "(Nora is a made-up character, and so is her afternoon. The pattern she meets is real, and "
            "sources are named below.)",
            "Part 26 covered scams that ask you to pay first. This part covers a quieter risk: losing "
            "control of your mobile number. You will learn what the SIM Registration Act requires and "
            "allows, what a SIM swap is and why it matters, the signs that your number has been taken, how "
            "to make it harder, and what to do first if it happens.",
            ("photo", "blog/cyber-sim.jpg", "Your SIM is a key: register it truthfully, guard the details "
             "used to verify you, move codes off text messages where you can, and act fast when the signal "
             "vanishes. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Your Number Matters"),
            "Banks, e-wallets and email services send one-time codes by text message to confirm that it is "
            "you. Part 2 explained multi-factor authentication. When the second factor is a text message, "
            "whoever controls the number controls the code.",
            ("quote", "Your phone number is not just how people reach you. It is how your accounts recognize "
             "you."),
            ("h", "What the SIM Registration Act Requires"),
            "Republic Act No. 11934, the SIM Registration Act, was signed on October 10, 2022. As summarized "
            "by the law firm MTF Counsel, it covers the following.",
            ("point", "Every SIM registered", "Prepaid and postpaid, with registration a condition for "
             "activation, backed by a government-issued ID."),
            ("point", "Deactivation on report", "If a SIM is lost, or the user dies, the user or family can "
             "report it, and the telecom company must deactivate the SIM within 24 hours of the report."),
            ("point", "Penalties", "For giving false information or a fictitious ID when registering, for "
             "spoofing a registered SIM, and for selling or transferring a registered SIM without "
             "following the law’s rules."),
            ("point", "Confidentiality", "Breaches of the confidentiality of registration data are "
             "punishable."),
            "Registration had a deadline. Gulf News reported that the deadline for existing SIMs was July 25, "
            "2023, after a 90-day extension, with deactivation of unregistered SIMs starting the next day. "
            "It cited the National Telecommunications Commission as reporting about 114 million SIMs "
            "registered as of July 30, 2023.",
            ("h", "What Registration Does Not Do"),
            "Registration ties a number to an identity. It does not stop someone from tricking a telecom "
            "store into moving your number to a new SIM, and it does not stop you from reading a code aloud "
            "to a stranger. The penalties apply after the fact. Your own habits work before it.",
            ("point", "Do not sell or lend a registered SIM", "The law penalizes the transfer of a registered "
             "SIM without following its rules. A SIM registered in your name and used by someone else for "
             "scams leads back to you."),
            ("point", "Register with your own true details", "False information is itself an offense."),
            ("h", "Links That Ask You to Re-register"),
            "A text that asks you to register, update or “re-verify” your SIM through a link deserves suspicion. Registration under the law goes through your telecom company’s own channels, and a link in a text can lead to a look-alike page, as Part 15 showed with fake websites.",
            ("point", "Use the official app or website", "Type the address yourself or open your telecom’s own app."),
            ("point", "Never send an ID photo by chat", "A photo of your ID, with your birthdate and number, is exactly what an impostor needs at a store counter."),
            ("h", "What a SIM Swap Is"),
            "In a rule adopted in November 2023, the US Federal Communications Commission described SIM swap and port-out "
            "fraud as ways for bad actors to take control of a consumer’s cell phone account without ever "
            "getting hold of the phone. The criminal convinces the provider to move the number to a SIM, or "
            "to another provider, that the criminal controls.",
            "The FCC said this lets criminals complete text and voice checks to get into a victim’s other "
            "accounts. Its rule requires US providers to use secure ways to confirm a customer’s identity "
            "before a SIM change, and to notify customers right away when a SIM change or port-out is "
            "requested.",
            ("h", "Warning Signs"),
            ("point", "Sudden loss of signal", "No service in a place where others have it, and a restart "
             "does not help."),
            ("point", "A message you did not expect", "A text or email from your provider about a SIM "
             "change, a replacement or a port request."),
            ("point", "Codes you did not ask for", "One-time codes arriving for logins you did not start."),
            ("point", "Locked out", "A password that suddenly no longer works on your e-wallet or email."),
            ("h", "Make It Harder"),
            ("point", "Use an authenticator app or passkey where offered", "Part 2 explained these. A code "
             "generated on your phone does not travel by text message, so moving your number does not move "
             "it."),
            ("point", "Guard your verification details", "Birthdate, mother’s maiden name, ID numbers: these "
             "are what a criminal needs to pass as you at a store. Keep them off public posts, as Part 14 "
             "advised."),
            ("point", "Set the PINs you are offered", "Use the PIN or lock features in your e-wallet and "
             "banking apps, and keep them different from your birthday."),
            ("point", "Never read a code to anyone", "No bank, e-wallet or telecom agent needs your one-time "
             "code."),
            ("h", "The First Hour"),
            ("point", "Confirm from another phone", "Call your own number. Then call your telecom’s hotline "
             "from a colleague’s phone and report the problem."),
            ("point", "Call your bank and e-wallet", "Ask them to lock or watch the accounts linked to your "
             "number, using the hotline in the official app or website."),
            ("point", "Change passwords from a trusted device", "Start with email, since password resets for "
             "other accounts can go there."),
            ("point", "Report it", "To the CICC hotline 1326 or the PNP Anti-Cybercrime Group, with the time "
             "your signal disappeared."),
            ("h", "For Treasury Workers"),
            "Some office tasks depend on a phone number: a bank portal that sends codes, an official "
            "e-mail recovery number, a payment app on an office phone. Know whose SIM each one is, keep it "
            "registered to the right person or office, and write down who reports it if the phone is lost. "
            "A lost office phone should be reported to the telecom as promptly as a personal one.",
            ("h", "Mistakes to Avoid"),
            ("point", "Ignoring a sudden “No service”", "Check whether others have signal."),
            ("point", "Lending a registered SIM", "It stays in your name."),
            ("point", "Relying only on text codes", "Use an app or passkey where offered."),
            ("point", "Posting verification details", "Birthdates and IDs help impostors."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Your number is a key", "Text codes follow the number, not the phone."),
            ("point", "Registration is the law", "RA 11934, with 24-hour deactivation on report."),
            ("point", "SIM swaps move the number", "Watch for signal loss and unexpected notices."),
            ("point", "Act in the first hour", "Telecom, bank, passwords, report."),
            ("h", "Your Part 27 Action Plan"),
            ("point", "Today", "Save your telecom’s hotline in a colleague’s or family member’s phone."),
            ("point", "This week", "Switch one important account from text codes to an authenticator app "
             "or passkey, if it offers one."),
            ("point", "This month", "List the office accounts that depend on a phone number, and whose SIM "
             "each one uses."),
            "Write the first-hour steps on a card in your wallet. On the day your signal vanishes, you will "
            "not want to be searching for them.",
            "Nora’s e-wallet provider froze the account within the hour, and the transfer that had been "
            "started did not go through. The telecom restored her number the next day. That weekend she "
            "moved her e-wallet and email to app-based codes, and taped the hotline numbers inside her "
            "phone case.",
            ("cta", "Read: Cybersecurity Series, Part 26: Job and Investment Scams, When Easy Money Asks You to Pay First", "/blog/cybersecurity-part-26-job-and-investment-scams/"),
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet, Securing It Before It Is Lost", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("cta", "Read: Cybersecurity Series, Part 14: Your Social Media Account Is a Scammer’s Best Disguise", "/blog/cybersecurity-part-14-social-media-accounts/"),
            ("ask", "If your phone lost signal right now, which of your accounts would be at risk?"),
        ],
    },
    {
        "date": "November 26, 2027",
        "title": "Cybersecurity Series, Part 26: Job and Investment Scams, When Easy Money Asks You to Pay First",
        "slug": "cybersecurity-part-26-job-and-investment-scams",
        "category": "security",
        "summary": "A message offers easy work from home, or a plan that doubles your money in weeks. This "
                   "part explains how task scams and investment scams work, the numbers the FTC has "
                   "reported, how to check an investment offer with the SEC, and the one rule that applies to both: never pay to get paid.",
        "publish_on": "2027-11-26 21:00",
        "body": [
            "The message arrived on a Tuesday night: “Hi! We are hiring part-time online staff. Just like "
            "and rate products, 30 minutes a day, ₱500 to ₱2,000 daily.” Carla, a job order employee saving "
            "for her daughter’s tuition, replied. By Friday the app showed ₱3,800 in commissions, and ₱150 "
            "had actually reached her e-wallet. Then came a “combination task”: deposit ₱5,000 to unlock it, "
            "and get it all back with a bonus. She nearly did.",
            "(Carla and her story are made up to show how the scam works. The amounts are examples too.)",
            "Part 25 dealt with scams in buying and selling. This part covers two scams that promise income: "
            "fake jobs and fake investments. You will come away knowing how a task scam works step by step, "
            "what the US Federal Trade Commission has reported about it, how investment scams use the same "
            "pattern, how to check an investment offer with the Securities and Exchange Commission, and what "
            "to do if you already paid.",
            ("photo", "blog/cyber-easy-money.jpg", "Job and investment scams: an unexpected offer, fake "
             "earnings, a small payout, then a deposit you never see again. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "How a Task Scam Works"),
            "The FTC described the pattern in a data report of December 12, 2024, and again in a consumer "
            "alert in August 2025.",
            ("point", "The contact", "An unexpected text, WhatsApp or social media message offers online "
             "work with few details, such as “optimizing” apps or “boosting” products."),
            ("point", "The tasks", "Simple, repetitive clicks, like rating products or liking videos, in an "
             "app that shows a commission growing with each one."),
            ("point", "The small payout", "The FTC says scammers may pay out a small amount early, to build "
             "trust."),
            ("point", "The deposit", "To unlock the next set of tasks or withdraw the “earnings,” the worker "
             "is told to deposit their own money. The balance on the screen was never real, and the deposit "
             "does not come back."),
            "The FTC adds a detail that matters: if a victim hesitates, scammers may add them to a group chat "
            "where others post “success stories” to push them to pay.",
            ("quote", "A real job pays you. It never asks you to pay to get paid."),
            ("h", "Why It Catches Careful People"),
            "Each step in the FTC’s description is built to lower a person’s guard a little more.",
            ("point", "The payout is real", "The first small amount actually arrives, so the job seems to be real too."),
            ("point", "The balance grows", "The app shows earnings that feel already yours, which makes walking away feel like losing money."),
            ("point", "Others seem to win", "The group chat full of “success stories” makes paying look normal."),
            "None of this needs the victim to be careless. It needs them to be hopeful, and to believe what a screen shows them.",
            ("h", "What the Numbers Show"),
            "In the December 2024 report, the FTC said reported losses to job scams more than tripled from "
            "2020 to 2023, and topped $220 million in the first half of 2024 alone. It estimated about 20,000 "
            "task scam reports in that half year, up from about 5,000 in all of 2023. The FTC also notes that "
            "the vast majority of frauds are not reported, so these are the cases it heard about, not all of them.",
            "These are US figures. They are here because they show how fast the pattern grew, and a message like Carla’s can reach any phone with a chat app.",
            ("h", "Investment Scams Follow the Same Script"),
            "Swap “tasks” for “trading” and the pattern is the same: an unexpected contact, a screen showing "
            "returns, a small withdrawal that works, then a request for more money.",
            ("point", "Returns that are too high", "In April 2026, the SEC warned the public about one scheme "
             "whose plans advertised returns of up to ₱43,411 a day."),
            ("point", "Recruit to earn", "The same advisory warned against commission-based recruiting "
             "without a permit to sell securities."),
            ("point", "An app from a link", "The SEC also told the public to be careful about installing apps "
             "from unofficial sources, such as files sent by text or social media."),
            ("h", "Check an Investment Offer With the SEC"),
            "In the Philippines, the SEC has said that soliciting investments from the public requires both "
            "registration and a secondary license. A business permit or a certificate of incorporation alone "
            "is not a license to take investments.",
            ("point", "Ask for the secondary license", "Not just the company’s registration. If they cannot "
             "show one, stop."),
            ("point", "Search the SEC’s advisories", "The SEC publishes advisories naming schemes it has "
             "found operating without authority."),
            ("point", "Know the risk to recruiters", "The SEC has warned that salesmen and promoters of "
             "unlicensed schemes can face criminal penalties. Recruiting friends into one can make you liable, "
             "not only a victim."),
            ("h", "Warning Signs in One List"),
            "The FTC’s August 2025 alert lists signs of a task scam. Several of them fit investment scams too.",
            ("point", "An offer you did not apply for", "The FTC says real employers will not contact you "
             "that way, through a random text or chat."),
            ("point", "Quick, easy money", "Pay for a few minutes of clicking, or returns far above what a "
             "bank or bond pays."),
            ("point", "Any request to pay first", "A deposit, a “fee,” a “tax” on your earnings, or money to "
             "unlock a withdrawal."),
            ("point", "Pay for ratings or likes", "The FTC tells people not to accept money for giving "
             "ratings or likes online."),
            ("h", "For Treasury Workers"),
            "Regular employees draw a monthly salary, and some offices also employ job order and contract "
            "of service workers who may look for extra income. Both are reachable by the same messages. If an "
            "offer arrives on an office phone or office account, report it to whoever handles IT, so others "
            "are warned. And never use an office device to install an app sent by a stranger.",
            ("h", "If You Already Paid"),
            ("point", "Stop paying", "No further deposit will release the earlier ones."),
            ("point", "Save everything", "Screenshots of the chat, the app, the account numbers and every "
             "transfer."),
            ("point", "Call your bank or e-wallet", "Use the hotline in the official app, and report the "
             "receiving accounts."),
            ("point", "Report it", "Call the CICC hotline 1326 or go to the PNP Anti-Cybercrime Group. For an "
             "investment scheme, report it to the SEC as well."),
            "The FTC also warns about refund and recovery scams: people who promise to get your money back for a fee. Paying them is "
            "paying to get paid, again.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting the balance on the screen", "Only money you can withdraw is real."),
            ("point", "Paying to unlock earnings", "In the FTC’s description, that is the scam."),
            ("point", "Recruiting others", "You may share the legal risk."),
            ("point", "Paying a “recovery agent”", "It is the same trick in a new costume."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Never pay to get paid", "The FTC’s rule, and the simplest one."),
            ("point", "Same script for jobs and investments", "Contact, fake gains, small payout, deposit."),
            ("point", "Check the secondary license", "A business registration is not enough to take "
             "investments."),
            ("point", "Report quickly", "Bank, CICC 1326, and the SEC for investment schemes."),
            ("h", "Your Part 26 Action Plan"),
            ("point", "Today", "Write “Never pay to get paid” in your family group chat, with one sentence on "
             "how task scams work."),
            ("point", "This week", "If anyone you know is in an “investment” paying high returns, ask for "
             "its secondary license."),
            ("point", "Next time a job message arrives", "Do not reply. Block, report and delete."),
            "Scam stories change. The request at the end, pay first, appears in every version described in this part.",
            "Carla showed the chat to her supervisor the next morning. The supervisor had read the same "
            "script in a news report the week before. Carla blocked the number, reported the account to her e-wallet, and kept her ₱5,000 for tuition.",
            ("cta", "Read: Cybersecurity Series, Part 25: Online Marketplace Scams, Buying and Selling Without Getting Burned", "/blog/cybersecurity-part-25-online-marketplace-scams/"),
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 22: Deepfakes and Cloned Voices, When Seeing and Hearing Is Not Enough", "/blog/cybersecurity-part-22-deepfakes-and-voice-clones/"),
            ("cta", "Read: Cybersecurity Series, Part 3: The Art of Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("ask", "Have you or someone you know received a “like and earn” job message? What did it promise?"),
        ],
    },
    {
        "date": "November 17, 2027",
        "title": "Cybersecurity Series, Part 25: Online Marketplace Scams, Buying and Selling Without Getting Burned",
        "slug": "cybersecurity-part-25-online-marketplace-scams",
        "category": "security",
        "summary": "Selling a used phone or buying a cheap appliance online is convenient, and scammers know "
                   "it. This part covers the fake payment screenshot, the overpayment refund, the shared "
                   "code, the deal that is too cheap, and the habits and the law that protect buyers and "
                   "sellers.",
        "publish_on": "2027-11-17 21:00",
        "body": [
            "Lito posted his old phone for sale on a Sunday night. By Monday morning, a buyer had agreed to "
            "the price without haggling and sent a screenshot of an e-wallet transfer for the full amount. "
            "“Paid already. Please ship today, my rider is waiting.” The screenshot looked right: the logo, "
            "the amount, a reference number. Lito almost wrapped the phone. Then he opened his own e-wallet "
            "app. The balance had not changed.",
            "(Lito, his buyer and the amounts here are invented. Any resemblance to a real person or account "
            "is a coincidence.)",
            "Part 24 looked at QR codes that send money to the wrong place. This part looks at the people on "
            "the other side of an online sale. Read on, and you will know the scams that target sellers, the "
            "ones that target buyers, the checks to make before any money moves, what the "
            "Internet Transactions Act does for online shoppers, and what to do if a sale goes wrong.",
            ("photo", "blog/cyber-marketplace.jpg", "Online marketplace scams: check your own app, refuse "
             "overpayments, never share a code, and question the deal that is too cheap. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Scams That Target Sellers"),
            "The US Federal Trade Commission described three tricks aimed at people who sell things online "
            "in a consumer alert of July 27, 2022. The examples come from the United States. Watch for the same moves here.",
            ("point", "The fake payment notice", "The buyer insists on paying through a mobile payment app, "
             "then sends a fake notice of payment, hoping you ship the item before you notice that no money "
             "came in."),
            ("point", "The overpayment refund", "The buyer claims to have paid too much by mistake and asks "
             "you to send back the difference. In the alert’s check version, the payment later bounces, "
             "and the seller loses the refund and the item."),
            ("point", "The verification code", "The buyer asks you to read back a code sent to your phone. In the FTC’s example, the scammer used the code to set up a Google Voice number linked to the seller’s phone, then used it to scam others while hiding who they were."),
            ("quote", "A screenshot is a picture of a payment, not a payment."),
            ("h", "Scams That Target Buyers"),
            "The FTC’s guide to shopping online lists warning signs on the buying side.",
            ("point", "The price that is too good", "The guide warns that deep discounts on expensive "
             "brand-name items may signal goods that are counterfeit or stolen."),
            ("point", "Unusual payment demands", "Be wary, the guide says, of sellers who insist on gift cards, wire transfers, payment apps or cryptocurrency."),
            ("point", "Reviews that may not be real", "The guide notes that some reviews and ratings are fake "
             "or misleading, and suggests checking more than the star rating."),
            "A pattern joins the seller and buyer scams: pressure to act now. “My rider is waiting.” "
            "“Many people want it, pay the reservation today.” Pressure is the scammer’s tool for skipping "
            "your checks.",
            ("h", "Five Checks Before Money Moves"),
            ("point", "Open your own app", "Sellers: confirm payment by opening your e-wallet or bank app "
             "yourself, not by looking at a screenshot, a text message or an email that says you were paid."),
            ("point", "Refuse every overpayment", "If a buyer pays too much, do not send back the "
             "difference. The FTC’s advice is never to deposit a check for more than the selling price."),
            ("point", "Keep codes to yourself", "The FTC says not to share a verification code with someone "
             "you do not know. A real buyer has no reason to ask for one."),
            ("point", "Search the name", "Buyers: the FTC suggests searching the seller or product name with "
             "the words “complaint” or “scam” to see what other buyers say."),
            ("point", "Meet in a safe place if you can", "For local sales, the FTC suggests meeting buyers in "
             "person and accepting cash. Choose a busy public place, in daylight."),
            ("h", "Stay Inside the Platform"),
            "Buyers and sellers who meet on a marketplace site are sometimes asked to “continue the "
            "conversation” on another messaging app, or to pay outside the site’s own checkout. Moving off "
            "the platform can mean losing its records and any buyer or seller protection it offers. Before "
            "a large purchase, read what protection the site gives, and keep the whole conversation where "
            "the site can see it.",
            ("h", "What the Internet Transactions Act Does"),
            "Republic Act No. 11967, the Internet Transactions Act of 2023, was signed on December 5, 2023. "
            "The Department of Trade and Industry describes it as a law to boost and protect e-commerce and "
            "build trust in online transactions.",
            ("point", "An E-Commerce Bureau", "Created under the DTI, with an online business database and a "
             "government-wide system for tracking online consumer complaints."),
            ("point", "Powers against bad sellers", "The DTI lists compliance orders, subpoenas, takedowns of "
             "websites and the blacklisting of online businesses among its powers under the law."),
            ("point", "Duties for platforms and merchants", "The law sets out liabilities for online "
             "merchants, e-retailers, e-marketplaces and digital platforms, with penalties for violators."),
            "For a buyer, this means a complaint about an online seller has a government office to go to, "
            "apart from the police. For the scams themselves, the Anti-Financial Account Scamming Act from "
            "Part 13 still applies.",
            ("h", "For Treasury Workers"),
            "Offices buy supplies through formal procurement, not marketplace chats. The risk at work is "
            "personal: a colleague selling something on their lunch break, or receiving a “payment” on the "
            "office phone. The same checks apply. And if someone asks you to read back a code that just "
            "arrived on an office phone, the answer is no, whoever they say they are.",
            ("h", "If a Sale Goes Wrong"),
            ("point", "Stop and save", "Stop replying. Take screenshots of the listing, the chat, the "
             "profile and any payment details before they disappear."),
            ("point", "Call your bank or e-wallet", "Use the hotline in the official app. Report the account "
             "you paid and ask what can still be done."),
            ("point", "Report the account", "Use the marketplace’s own report button so the listing can be "
             "reviewed."),
            ("point", "File a report", "Call the CICC hotline 1326 or go to the PNP Anti-Cybercrime Group. "
             "For a complaint about an online seller, the DTI’s consumer channels are another route."),
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting a screenshot", "Check your own app."),
            ("point", "Refunding an overpayment", "Cancel the deal instead."),
            ("point", "Sharing a verification code", "No real buyer needs it."),
            ("point", "Paying outside the platform", "You may lose its records and protection."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Sellers check the app", "Money is real only when your own balance shows it."),
            ("point", "Buyers check the seller", "Search the name with “scam,” and question deep discounts."),
            ("point", "Pressure is a warning sign", "A real buyer or seller can wait for your checks."),
            ("point", "The law gives you a door", "The DTI’s E-Commerce Bureau tracks online complaints."),
            ("h", "Your Part 25 Action Plan"),
            ("point", "Today", "Turn on notifications in your e-wallet app, so a real payment shows up "
             "where you can see it."),
            ("point", "This week", "Tell one family member who sells online about the fake screenshot and "
             "the code request."),
            ("point", "Next purchase", "Before paying, search the seller’s name with “scam” and read the "
             "site’s buyer protection."),
            "Write the three checks on a note near your phone: own app, no refunds of overpayments, no "
            "codes. They take less than a minute, and a real buyer has no reason to object.",
            "Lito messaged the buyer: “Payment not received. I will ship when it shows in my account.” The "
            "buyer called him impatient, then blocked him. Lito reported the account, posted the phone "
            "again, and sold it two days later to a woman who paid in cash at a busy coffee shop.",
            ("cta", "Read: Cybersecurity Series, Part 24: QR Code Scams, When a Square of Dots Sends You the Wrong Way", "/blog/cybersecurity-part-24-qr-code-scams/"),
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address", "/blog/cybersecurity-part-15-fake-websites/"),
            ("cta", "Read: Cybersecurity Series, Part 14: Your Social Media Account Is a Scammer’s Best Disguise", "/blog/cybersecurity-part-14-social-media-accounts/"),
            ("ask", "Have you ever been sent a payment screenshot that turned out to be fake?"),
        ],
    },
    {
        "date": "November 8, 2027",
        "title": "Cybersecurity Series, Part 24: QR Code Scams, When a Square of Dots Sends You the Wrong Way",
        "slug": "cybersecurity-part-24-qr-code-scams",
        "category": "security",
        "summary": ("A QR code hides where it leads, which is why scammers like it. From stickers pasted over a "
                   "store’s payment code to fake delivery messages, these scams follow a pattern, and a few "
                   "habits keep a quick scan from becoming a costly one."),
        "publish_on": "2027-11-08 21:00",
        "body": [
            "A small eatery near the town plaza accepted payments by QR code. A printed code stood on the "
            "counter in a little acrylic stand. For two days, customers scanned it, paid and left. On the "
            "third day, the owner checked her e-wallet and found that the money from those two days had "
            "never arrived. Someone had pasted a new sticker over her code. The customers had paid a "
            "stranger.",
            "(This story is fictional. The eatery, its owner and its customers are made up.)",
            "QR codes are convenient because they hide a long address or an account number behind a square "
            "of dots. That same hiding is what makes them useful to scammers. Read to the end and you will "
            "know how QR code scams work, the warnings issued by the FBI, the U.S. Federal Trade Commission "
            "and the Bangko Sentral ng Pilipinas, how to check a code before you trust it, and what a "
            "business can do to protect the code its customers pay with.",
            ("photo", "blog/cyber-qr.jpg", "QR code scams: look for stickers, preview the address, check the "
             "name before you pay, and use the official app. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Why QR Codes Are Easy to Abuse"),
            "A person can read a web address and notice a strange spelling. Nobody can read a QR code by "
            "looking at it. The Bangko Sentral ng Pilipinas made this point in April 2026, when a BSP officer "
            "explained “quishing,” the use of malicious QR codes to trick people into visiting fake websites. "
            "The code hides the real address, so a user may not be able to tell a harmful link from a real "
            "one until after scanning.",
            ("quote", "A QR code is a closed envelope. Look inside before you act on it."),
            ("h", "The Main Tricks"),
            ("point", "A sticker over the real code", "The FBI warned in January 2022, in public service "
             "announcement I-011822-PSA, that criminals tamper with physical QR codes and replace legitimate "
             "ones with their own, redirecting payments meant for a business. The BSP described the same "
             "trick: scammers paste their own codes over legitimate merchant codes."),
            ("point", "A fake website", "A code can open a lookalike site that asks for a login or card "
             "details. Anything you type there goes to the criminal."),
            ("point", "A message with a reason to scan", "The FTC’s December 2023 alert describes codes sent by "
             "text or email with a made-up reason: a package that could not be delivered, a problem with "
             "your account, or suspicious activity that requires a password change. The urgency is meant to "
             "make you scan without thinking."),
            ("point", "A code that installs an app", "The FBI advises against downloading an app from a QR "
             "code. Apps should come from your phone’s official app store."),
            ("h", "Before You Scan"),
            ("point", "Look at the code itself", "Is it a sticker on top of another code? Is the edge raised, "
             "or does it look newer than the sign around it? The FBI suggests checking physical codes for "
             "tampering, such as a sticker placed over the original."),
            ("point", "Ask whether you expected it", "A QR code in an unexpected message, especially one "
             "that pushes you to act fast, deserves suspicion. The FTC’s advice: if you think it might be "
             "real, contact the company through a phone number or website you already know."),
            ("point", "Use your phone’s own camera", "The FBI suggests avoiding third-party QR scanner apps, "
             "since many phone cameras already have a built-in scanner."),
            ("h", "After You Scan, Before You Tap"),
            ("point", "Read the address", "When the camera shows the link, read it before opening it. Look for "
             "misspellings or swapped letters, and read the domain from the right, as Part 15 showed."),
            ("point", "Do not log in from a scanned link", "If the page asks for your bank or e-wallet "
             "password, close it and open the official app or a bookmark instead."),
            ("point", "Read the name before you pay", "When a payment code opens your e-wallet or bank app, "
             "look at the recipient name the app shows before you confirm. If it is not the store or person "
             "you meant to pay, stop."),
            ("h", "QR Codes in Work Email"),
            "An email at work that asks you to scan a QR code to keep your account active, sign a document "
            "or see a payroll notice deserves the same care as any other link. Scanning moves the link from "
            "your office computer to your phone, where the small screen makes the address harder to read. "
            "Ask your office’s IT contact or the sender, through a channel you already know, before you scan. "
            "Part 19 covered how fake senders work.",
            ("h", "QR Ph and Paying in Stores"),
            "In the Philippines, QR payments run on QR Ph, the national QR code standard adopted under BSP "
            "Circular No. 1055 in 2019. The BSP required its supervised payment service providers to use and "
            "display QR Ph on their internet and mobile channels starting July 1, 2023, so one code can be "
            "paid from different banks and e-wallets. That convenience works for honest stores and for "
            "anyone who pastes a fake code, which is why the name check matters.",
            ("h", "For Store Owners and Offices That Accept QR Payments"),
            ("point", "Keep the code where you can see it", "Behind the counter or under a clear, fixed cover "
             "is harder to tamper with than a loose card on a table."),
            ("point", "Check it every morning", "Scan your own code and confirm that your business name "
             "appears. It takes ten seconds."),
            ("point", "Watch your incoming payments", "A busy day with no money arriving is the warning sign. "
             "Turn on payment notifications."),
            ("point", "Tell customers what name to expect", "A small line under the code, such as “Pay to: "
             "the store’s registered name,” helps customers catch a swap."),
            ("h", "For Treasury Workers"),
            "If your local government accepts payments through a QR code, treat the printed "
            "code like an accountable form: know where every copy is posted, check them on a schedule, and "
            "make sure the official name shown in the payment app matches the local government’s account. "
            "Payments made to a fake code do not reach the treasury, and the taxpayer will rightly ask why "
            "their payment is missing.",
            ("h", "If You Paid the Wrong Code"),
            ("point", "Call your bank or e-wallet at once", "Use the hotline in the official app. Report the "
             "transaction and the recipient’s details."),
            ("point", "Tell the store", "They need to remove the fake code before others pay it."),
            ("point", "Report it", "Part 13 listed where to report scams in the Philippines, including the "
             "1326 hotline of the Cybercrime Investigation and Coordinating Center."),
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting a code because it is in a real store", "A sticker can be added by anyone."),
            ("point", "Opening links without reading them", "Preview the address first."),
            ("point", "Logging in from a scanned link", "Use the official app."),
            ("point", "Confirming payment without reading the name", "Check the recipient every time."),
            ("h", "Stay-Safe Reminders"),
            ("point", "QR codes hide their destination", "That is why scammers use them."),
            ("point", "Look, preview, check the name", "Three habits that stop the tricks above."),
            ("point", "Unexpected codes deserve suspicion", "Especially those that come with urgency."),
            ("point", "Businesses should guard their codes", "Check them daily and watch incoming payments."),
            ("h", "Your Part 24 Action Plan"),
            ("point", "Today", "Next time you pay by QR, read the recipient name before you confirm."),
            ("point", "This week", "If you run a store or a payment counter, scan your own code and check the "
             "name that appears."),
            ("point", "This month", "Tell an older relative about sticker scams and the name check."),
            "The eatery owner reported the fake code to her e-wallet provider and the police, and moved her "
            "real code behind the counter, inside a frame screwed to the wall. Under it she added a line in "
            "marker: “The name should say Aling Rosa’s Eatery.” Her regular customers started reading it out "
            "loud before every payment, half as a joke and half as a habit.",
            ("cta", "Read: Cybersecurity Series, Part 23: Your Yearly Security Checkup, One Afternoon, Twelve Checks", "/blog/cybersecurity-part-23-yearly-security-checkup/"),
            ("cta", "Read: Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address", "/blog/cybersecurity-part-15-fake-websites/"),
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 3: The Art of Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("ask", "Have you ever checked the name before paying by QR code? Has a code ever surprised you?"),
        ],
    },
    {
        "date": "October 29, 2027",
        "title": "Cybersecurity Series, Part 23: Your Yearly Security Checkup, One Afternoon, Twelve Checks",
        "slug": "cybersecurity-part-23-yearly-security-checkup",
        "category": "security",
        "summary": ("Security habits fade unless someone checks them. This yearly checkup takes one afternoon: "
                   "twelve checks covering accounts, devices, money, files and family, each linked to the part "
                   "of this series that explains it."),
        "publish_on": "2027-10-29 21:00",
        "body": [
            "Every year, a retired teacher brings her car in for a tune-up before the long drive to her "
            "province for the holidays. The mechanic checks the brakes, the tires and the oil, even when "
            "nothing seems wrong. This year, her nephew asked her a question she had never considered: when "
            "was the last time anyone checked her phone, her email and her bank apps the same way?",
            "(The teacher and her nephew are fictional, as is everything else in this story.)",
            "Security is not something you set up once. Passwords age, apps pile up, old shares stay open and "
            "new scams arrive. By the end of this post, you will have a yearly checkup you can finish in one "
            "afternoon: twelve checks, grouped by area, each pointing to the part of this series that explains "
            "it in full.",
            ("photo", "blog/cyber-checkup.jpg", "The yearly security checkup: accounts, devices, money and "
             "files, and the people you protect. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Before You Start"),
            "Pick a date you will remember. You could tie it to a birthday, the start of the school year or the week you file your taxes. Block two to three hours, sit with your phone and computer, and "
            "keep a notebook nearby to write down what you changed. The notebook matters: next year, it tells "
            "you where you left off.",
            ("quote", "A checkup finds the small problem before it becomes the big one."),
            ("h", "Part One: Your Accounts"),
            ("point", "Check 1: Your email account", "Your email unlocks your other accounts, because password resets go there. Confirm it has two-factor authentication, that the recovery phone "
             "number and recovery email are current, and that no forwarding rule sends your mail elsewhere. "
             "Parts 2 and 19 cover this."),
            ("point", "Check 2: Your passwords", "Open your password manager, or your list, and look for "
             "passwords used on more than one site and accounts you no longer use. Change the reused ones and "
             "close the accounts you do not need. Part 2 explains password managers and passkeys."),
            ("point", "Check 3: Your social media", "Look at the list of devices where you are logged in and "
             "sign out of any you do not recognize. Make sure your recovery codes are saved somewhere safe. "
             "Part 14 walks through it."),
            ("h", "Part Two: Your Devices"),
            ("point", "Check 4: Updates", "On every phone, tablet and computer, check for system updates and "
             "app updates, and turn on automatic updates where you can. Ask whether each device still gets "
             "security updates at all. Part 11 explains why this matters."),
            ("point", "Check 5: Your phone", "Confirm the screen lock is on, that one-time codes do not show "
             "on the lock screen, and that remote locking and erasing is set up and works. Part 12 has the "
             "steps."),
            ("point", "Check 6: Your home router", "Make sure the router’s admin password is not the default "
             "one, that its software is up to date, and that your Wi-Fi uses WPA3 or WPA2 with a strong password. Part 4 covers the router."),
            ("point", "Check 7: Encryption", "Confirm that your phone and laptop are encrypted, and that any "
             "USB drive with personal records is too. Part 17 shows how to check."),
            ("h", "Part Three: Your Money and Your Files"),
            ("point", "Check 8: Bank and e-wallet apps", "Delete banking and e-wallet apps you no longer use, "
             "review transaction alerts, and confirm that your registered mobile number and email are "
             "current. Part 13 covers e-wallet safety and the anti-scam law."),
            ("point", "Check 9: Backups", "Pick one important file and actually restore it from your backup. "
             "A backup you have never tested is only a hope. Part 5 explains the 3-2-1 approach."),
            ("point", "Check 10: Shared files", "Open your cloud drive and review what is shared, especially "
             "anything open to anyone with the link. Remove people who no longer need access. Part 21 has the "
             "details."),
            ("h", "Part Four: The People You Protect"),
            ("point", "Check 11: Your family", "Sit with an elderly parent or a young relative for twenty "
             "minutes. Check their phone lock and their e-wallet settings, and remind them about voice-clone "
             "and fake-website scams. Agree on a family code word if you have not yet. Parts 15 and 22 "
             "explain these scams."),
            ("point", "Check 12: Your emergency plan", "Write down, on paper, what you would do in the first "
             "hour if your phone were stolen or an account taken over: which bank hotline to call, how to "
             "lock the phone remotely, and where to report. Part 9 covers incident response, including the "
             "Cybercrime Investigation and Coordinating Center’s hotline, 1326."),
            ("h", "For Small Offices"),
            "An office can run the same checkup once a year for its shared accounts and devices. Part 18 "
            "gave a one-page baseline for a small office. Use it as the checklist, mark each item done or "
            "not done, and assign a name and a date to every item that is not. Repeat the review of who has "
            "access to shared drives and systems, and remove accounts for staff who have left or moved.",
            ("h", "How Long It Really Takes"),
            "The first checkup is the slowest, because you are finding things for the first time: old "
            "accounts, forgotten shares, apps you never open. Write down what you found. In the second year, "
            "you start from your notes, and the checks go faster.",
            ("h", "What to Do With What You Find"),
            ("point", "Fix the quick things on the spot", "Turning on an update or deleting an old app takes "
             "a minute."),
            ("point", "Schedule the bigger things", "Setting up a password manager or a backup can take an "
             "evening. Put it on your calendar for the next week."),
            ("point", "Ask for help without embarrassment", "If something is confusing, ask someone you trust "
             "to sit with you. Security is easier with two people."),
            ("h", "When Not to Wait a Year"),
            "Some events call for a checkup right away, whatever the calendar says.",
            ("point", "A lost or stolen device", "Run Checks 1, 3, 5 and 8 the same day."),
            ("point", "A notice that your data was leaked", "Change that password and any place you reused it, "
             "then run Check 2."),
            ("point", "A new phone or computer", "Run Checks 4, 5 and 7 before you move your accounts to it."),
            ("point", "A scam attempt in the family", "Run Check 11 with everyone, while the story is fresh."),
            ("h", "Mistakes to Avoid"),
            ("point", "Doing it once and forgetting", "Set the date for next year before you finish."),
            ("point", "Skipping the backup test", "A backup is only proven when a file comes back."),
            ("point", "Checking your own devices but not your family’s", "A scammer needs only one person in the family to believe them."),
            ("point", "Trying to fix everything in one sitting", "Fix the quick things, schedule the rest."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Security needs a yearly review", "Settings drift and new risks appear."),
            ("point", "Twelve checks cover the basics", "Accounts, devices, money, files and family."),
            ("point", "A notebook makes next year easier", "Write down what you changed."),
            ("point", "Help the people around you", "Their safety is part of yours."),
            ("h", "Your Part 23 Action Plan"),
            ("point", "Today", "Choose the date of your yearly checkup and put it in your calendar, with a "
             "reminder."),
            ("point", "This week", "Do Check 1, your email account. It protects your other accounts."),
            ("point", "This month", "Finish all twelve checks, and write down what you changed."),
            "The teacher and her nephew spent a Saturday afternoon on the twelve checks. They found an old "
            "online shopping account with a reused password, a backup that had stopped running months "
            "earlier, and a family group chat that had never heard of voice clones. By dinner, everything was "
            "fixed or scheduled, and she had written a date on the first page of a new notebook: the same "
            "Saturday, next year.",
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("cta", "Read: Cybersecurity Series, Part 22: Deepfakes and Cloned Voices, When Seeing and Hearing Is Not Enough", "/blog/cybersecurity-part-22-deepfakes-and-voice-clones/"),
            ("cta", "Read: Cybersecurity Series, Part 5: Inside a Ransomware Attack", "/blog/cybersecurity-part-5-ransomware/"),
            ("ask", "When did you last check your accounts and devices? Which of the twelve checks will you do first?"),
        ],
    },
    {
        "date": "October 20, 2027",
        "title": "Cybersecurity Series, Part 22: Deepfakes and Cloned Voices, When Seeing and Hearing Is Not Enough",
        "slug": "cybersecurity-part-22-deepfakes-and-voice-clones",
        "category": "security",
        "summary": ("A familiar face on a video call or a familiar voice on the phone can now be faked. A real "
                   "case cost one company about US$25 million, yet simple checks still work against these scams."),
        "publish_on": "2027-10-20 21:00",
        "body": [
            "The phone rang just after dinner. The voice on the line belonged to a woman’s son, who was "
            "working in another city. He was crying. He said he had been in an accident, that the other "
            "driver was hurt, and that he needed money for a settlement tonight or he would be detained. He "
            "begged her not to tell his father. Then another man came on the line and gave her an e-wallet "
            "number.",
            "(Everyone and everything in this story is fictional, including the numbers.)",
            "Scammers no longer need to sound like strangers. With recordings of a person’s voice or a few photos, software can imitate a person well enough to fool someone who loves them. By the last "
            "section, you will know what deepfakes and voice clones are, how scammers use them, what "
            "happened in a real case that cost a company about US$25 million, and the checks that still work "
            "when your eyes and ears cannot be trusted.",
            ("photo", "blog/cyber-deepfakes.jpg", "Deepfakes and voice clones: pause, call back on a number "
             "you know, ask a question only the real person can answer, and verify any payment. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Deepfake Is"),
            "A deepfake is a video, image or audio recording made or changed by software to show a person "
            "saying or doing something they never said or did. A voice clone is the audio version: software "
            "that learns how a person sounds and then speaks any words in that voice.",
            "These tools have legitimate uses, such as dubbing films or giving a voice back to someone who "
            "has lost theirs. The same tools can also be used to impersonate a boss, a parent or a child.",
            ("quote", "The face and the voice can be borrowed. The callback number cannot."),
            ("h", "A Real Case: The Video Call That Cost About US$25 Million"),
            "In January 2024, the engineering firm Arup reported a fraud to the police in Hong Kong. An "
            "employee there had joined what looked like a genuine company video conference. The people on "
            "the call, who appeared to be senior officers of the company, were deepfakes. They persuaded the "
            "employee to make a series of transfers to bank accounts the scammers chose. The total was "
            "HK$200 million, about US$25.6 million.",
            "Arup said its financial stability and business operations were not affected and that none of "
            "its internal systems were compromised. That is the important lesson. Nothing was hacked. A "
            "person was convinced.",
            ("h", "How Voice-Clone Scams Work"),
            "The U.S. Federal Trade Commission warns about family emergency scams, in which someone contacts "
            "you pretending to be a family member or close friend who needs money to get out of trouble. "
            "The FTC says scammers use voice cloning to make these requests more believable.",
            ("point", "A sample of the voice", "Short clips can come from public videos, social media "
             "posts or a brief phone call."),
            ("point", "An emergency", "An accident, an arrest, a hospital bill or a stranded trip, with no time to think."),
            ("point", "Secrecy", "“Don’t tell Dad.” “Don’t call my phone, it’s broken.” Secrecy stops you "
             "from checking."),
            ("point", "A fast way to pay", "An e-wallet number, a bank transfer, prepaid load or gift "
             "cards, money that is hard to get back."),
            ("h", "The Signs to Watch For"),
            "A good fake can look and sound real, so do not rely on spotting glitches. Watch the situation "
            "instead.",
            ("point", "Urgency", "You are told to act within minutes."),
            ("point", "Secrecy", "You are told not to tell anyone or not to call back."),
            ("point", "A new way to pay", "The money goes to an account or wallet you have never used for "
             "this person."),
            ("point", "A different channel", "Your boss, who always emails, suddenly calls from an unknown "
             "number. Your child, who always messages, calls from someone else’s phone."),
            ("h", "The Checks That Still Work"),
            ("point", "Hang up and call back", "Call the person on the number you already have for them. "
             "If they answer and know nothing about it, you have your answer."),
            ("point", "Ask a question only they can answer", "Something that is not on social media: the "
             "name of a childhood pet, what you ate at your last family dinner."),
            ("point", "Agree on a family code word", "Choose a word or phrase today, share it in person, and "
             "agree that anyone asking for emergency money must say it."),
            ("point", "Reach someone else", "Call a sibling, a spouse or a co-worker who would know where "
             "the person is."),
            ("point", "Slow down", "A real emergency can survive a two-minute phone call to check."),
            ("h", "At Work: Video Calls and Payment Requests"),
            "The Arup case shows that a video call is not proof of identity. Offices that handle money can "
            "add a few simple rules.",
            ("point", "No payment on a call alone", "A request made during a call or video conference is "
             "confirmed through a separate channel before any money moves."),
            ("point", "Use the payment rule from Part 19", "Changes to bank details and urgent transfers are "
             "confirmed by phone, using a number already on file."),
            ("point", "Two people for large transfers", "One person prepares, another approves. A scammer "
             "has to fool both."),
            ("point", "Permission to pause", "Office heads can tell staff in advance that checking a request "
             "will never get them in trouble, even if the request turns out to be real."),
            ("h", "Protect Your Own Face and Voice"),
            "You cannot hide completely, and you do not need to. A few habits lower the risk.",
            ("point", "Review who can see your posts", "Videos of you speaking that only friends can see are harder for strangers to collect."),
            ("point", "Be careful with unknown calls", "If a stranger calls and keeps you talking without a "
             "clear reason, you can end the call."),
            ("point", "Tell your family about this scam", "A strong defense for an elderly parent is knowing the trick exists before the call comes."),
            ("h", "If You Already Sent Money"),
            ("point", "Call your bank or e-wallet at once", "Ask them to stop or reverse the transfer and "
             "flag the receiving account. Part 13 covered what to do and where to report in the "
             "Philippines."),
            ("point", "Report it", "Report to the police cybercrime unit and keep the call logs, numbers "
             "and messages."),
            ("point", "Warn the person who was impersonated", "Their voice or face may be used again on "
             "someone else."),
            ("h", "For Treasury Workers"),
            "Treasuries release payments on the strength of signatures and approvals. Treat a voice or a "
            "face on a screen the same way you treat an email: as a request, not as authority. Follow the "
            "voucher, the signatures and the callback rule, whoever seems to be asking.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting a familiar voice", "Voices can be cloned."),
            ("point", "Trusting a familiar face on video", "The Arup employee did, and it cost about US$25 million."),
            ("point", "Calling back the number that called you", "Use the number you already have."),
            ("point", "Keeping it secret because you were asked to", "Secrecy is the scammer’s tool."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Faces and voices can be faked", "Video and audio are no longer proof."),
            ("point", "The situation gives it away", "Urgency, secrecy and a new way to pay."),
            ("point", "Verify through another channel", "Call back on a known number, or ask a question only "
             "the real person can answer."),
            ("point", "Set rules in advance", "A family code word and an office rule for payments."),
            ("h", "Your Part 22 Action Plan"),
            ("point", "Today", "Choose a family code word and share it in person with the people closest "
             "to you."),
            ("point", "This week", "Tell an elderly relative about voice-clone scams, using the story at the "
             "top of this post."),
            ("point", "This month", "Ask your office to adopt one rule: no payment based on a call or video "
             "conference alone."),
            "The mother did not send the money. She ended the call, sat down, and dialed her son’s number "
            "from her own contacts. He answered on the second ring, from his office, confused and perfectly "
            "fine. That weekend, the family chose a code word, and she taught it to her sister too.",
            ("cta", "Read: Cybersecurity Series, Part 19: Email Security, Fake Senders and the Changed Bank Account", "/blog/cybersecurity-part-19-email-security/"),
            ("cta", "Read: Cybersecurity Series, Part 14: Your Social Media Account Is a Scammer’s Best Disguise", "/blog/cybersecurity-part-14-social-media-accounts/"),
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 3: The Art of Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("ask", "Does your family have a code word yet? What would you choose?"),
        ],
    },
    {
        "date": "October 11, 2027",
        "title": "Cybersecurity Series, Part 21: Sharing Files Safely, Links, Attachments and Who Can See Them",
        "slug": "cybersecurity-part-21-safe-file-sharing",
        "category": "security",
        "summary": ("A shared link can reach far more people than you meant. Choose between a link and an "
                   "attachment, set who can open a file, give access that ends on its own, protect a file with a "
                   "password and clean up old shares."),
        "publish_on": "2027-10-11 21:00",
        "body": [
            "An office needed to send a list of beneficiaries to three partner offices, so a staff member "
            "uploaded the spreadsheet to a cloud drive and set the link to “Anyone with the link can view.” "
            "It was the easiest setting, and it worked. Weeks later, someone in one of the partner offices "
            "pasted that same link into a large group chat to ask a question about one name. Now anyone in "
            "that chat, and anyone they forwarded it to, could open the whole list.",
            "(Nothing in this story is real. The offices, the people and the list are made up.)",
            "Sharing files is part of daily work, and it is where good intentions leak data. After this "
            "post, you will know when to send a link and when to send an attachment, how to choose who can "
            "open a file, how to give access that ends on its own, how to protect a file with a password, "
            "and how to clean up the shares you no longer need.",
            ("photo", "blog/cyber-file-sharing.jpg", "Safe file sharing: restrict the link, give the least "
             "access, set an end date, and review who still has access. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "A Link or an Attachment?"),
            "Both have a place, and each has a different risk.",
            ("point", "An attachment is a copy", "Once sent, it lives in every inbox it reaches, and you "
             "cannot take it back. Anyone who receives it can forward it."),
            ("point", "A link points to one file you control", "You can change who may open it, or turn it "
             "off, at any time. But a link set to open for anyone is only as private as the places it gets "
             "pasted."),
            "For personal data or anything sensitive, a link restricted to named people is the "
            "safer choice, because you keep control after you click Send.",
            ("quote", "Share a file the way you would lend a key: to a named person, for a reason, and "
             "ask for it back."),
            ("h", "Who Can Open It"),
            "Cloud drives let you choose the general access for a file. In Google Drive, for example, the "
            "Share window offers two main choices.",
            ("point", "Restricted", "Only the people you add by email can open the file. Google’s help "
             "page puts it this way: only people with access can open it."),
            ("point", "Anyone with the link", "Whoever has the link can open the file, including people you never added. This is convenient for public material, such as a flyer or a schedule."),
            "The office in our story used the second setting for a list of names. Restricted, with the three "
            "partner offices added by email, would have kept the file closed to the group chat.",
            ("h", "Give the Least Access That Works"),
            ("point", "Viewer", "Can open and read. This is enough for anyone who only needs to see a "
             "file."),
            ("point", "Commenter", "Can read and leave comments, but cannot change the content."),
            ("point", "Editor", "Can change the file and, depending on the settings, share it with others. "
             "Give this role only to people who must edit."),
            "Google Drive also lets the owner choose whether people can download, copy and print the file, "
            "under the Settings of the Share window. That helps, but Google’s own help page notes that you "
            "cannot stop people from sharing a file’s content in other ways. Someone can still take a "
            "screenshot. Limit the people first, and the settings second.",
            ("h", "Access That Ends on Its Own"),
            "Some sharing is meant to be temporary, yet the access stays until someone removes it. "
            "Google Drive offers an expiration date on a person’s access: open Share, choose the person, "
            "select Add expiration, and pick a date, which must be within one year. Google lists this option "
            "among the features for accounts through work or school, so check whether your account has it.",
            "If your tool has no expiry option, put a reminder in your calendar to remove access when the "
            "work is done.",
            ("h", "Protecting a File With a Password"),
            "Sometimes a file must go by email, for example to someone outside your office who cannot use "
            "your drive. Then protect the file itself.",
            ("point", "Office documents", "In Microsoft Word or Excel, go to File, Info, then Protect "
             "Document or Protect Workbook, and choose Encrypt with Password. Without the password, the "
             "file will not open."),
            ("point", "Send the password another way", "If the password is in the same email as the file, "
             "anyone who gets the email gets both. Send it by text message or tell it by phone."),
            ("point", "Use a strong password", "Part 2 covered passphrases. A short password on a file can "
             "be guessed by software."),
            ("h", "USB Drives and Shared Computers"),
            ("point", "Treat a found USB drive as a risk", "Do not plug in a drive you found or were given by "
             "a stranger. Give it to whoever handles your office’s computers."),
            ("point", "Encrypt drives that leave the office", "Part 17 covered encryption. A lost drive that "
             "is encrypted is a lost drive, not a data leak."),
            ("point", "Do not leave files on shared computers", "Delete what you saved on a shared office or "
             "internet café computer, and sign out of every account before you stand up."),
            ("h", "Cleaning Up Old Shares"),
            "Shares pile up. A folder shared with a former co-worker, a link sent to a supplier last year, a "
            "file still open to anyone with the link: each is a door you forgot to close.",
            ("point", "See who has access", "In Google Drive, right-click a file and open its File information, then Details, to see the owner and everyone with access. Manage access lets you change it."),
            ("point", "Remove people who no longer need it", "Especially staff who have moved to other "
             "offices."),
            ("point", "Turn public links back to Restricted", "When the work that needed a public link is "
             "done, close it."),
            ("point", "Keep office files in office accounts", "When files sit in one person’s personal "
             "account, the office can lose them when that person leaves. Store office work where the office "
             "keeps control."),
            ("h", "For Treasury Workers"),
            "Treasury files carry names, property records, amounts and bank details. Share collection "
            "reports, delinquency lists and payroll files only through restricted links or protected files, "
            "and only to the people whose work needs them. Before sending any list outside the office, ask "
            "whether the recipient needs every column, or only a total.",
            ("h", "Mistakes to Avoid"),
            ("point", "Using “Anyone with the link” for personal data", "Restrict it to named people."),
            ("point", "Giving Editor when Viewer is enough", "Start with the least access."),
            ("point", "Sending the password with the file", "Use another channel."),
            ("point", "Never reviewing old shares", "Check who still has access."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Links keep control, attachments do not", "Prefer a restricted link for sensitive "
             "files."),
            ("point", "Choose who and how much", "Restricted access, and the smallest role that works."),
            ("point", "Give access an end", "Use expiry dates or a reminder to remove access."),
            ("point", "Clean up regularly", "Old shares are open doors."),
            ("h", "Your Part 21 Action Plan"),
            ("point", "Today", "Open your cloud drive and find one file shared with “Anyone with the link.” "
             "Decide whether it should be Restricted."),
            ("point", "This week", "Review who has access to your three most sensitive files, and remove "
             "anyone who no longer needs it."),
            ("point", "This month", "Agree with your team on one rule: personal data is shared only through "
             "restricted links or password-protected files."),
            "The office changed the beneficiaries list to Restricted that same day and added the three "
            "partner offices by email. The link in the group chat stopped working for everyone else. The "
            "office could not undo what had already been seen, but it closed the door, wrote down what "
            "happened, and changed how it shares lists from then on.",
            ("cta", "Read: Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk", "/blog/cybersecurity-part-20-privacy-at-work/"),
            ("cta", "Read: Cybersecurity Series, Part 17: Encryption Made Simple, Locking Data So a Lost Device Is Only a Lost Device", "/blog/cybersecurity-part-17-encryption-made-simple/"),
            ("cta", "Read: Cybersecurity Series, Part 6: Keeping Your Life in the Cloud Safe and Private", "/blog/cybersecurity-part-6-cloud-and-privacy/"),
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("ask", "How does your office share lists with other offices today? Is there one setting you would change after reading this?"),
        ],
    },
    {
        "date": "October 1, 2027",
        "title": "Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk",
        "slug": "cybersecurity-part-20-privacy-at-work",
        "category": "security",
        "summary": ("Offices hold other people’s names, addresses, IDs and money records. The Data Privacy Act "
                   "asks certain things of the people who handle them, a few desk habits keep records safe, and "
                   "there are clear steps when personal data leaks."),
        "publish_on": "2027-10-01 21:00",
        "body": [
            "A frontline clerk wanted to be helpful. A client had asked for a copy of a requirement she had "
            "submitted, so the clerk took a photo of the client’s ID and application form with her own phone "
            "and sent it through a chat app. It was quick, and the client was grateful. A month later, the "
            "clerk’s phone was stolen at a jeepney stop. The phone had no screen lock, and its gallery held "
            "more than a hundred photos of other people’s IDs.",
            "(This is a teaching case. The clerk, the client and the office are fictional.)",
            "Privacy at work depends on small habits at a desk as much as on the law. By the end of this post, "
            "you will know what the Data Privacy Act of 2012 protects, which kinds of information need the "
            "most care, the desk habits that keep other people’s records safe, how to share personal data "
            "only when there is a reason, and what to do when something leaks.",
            ("photo", "blog/cyber-privacy-work.jpg", "Privacy at work: know what is sensitive, collect only "
             "what you need, keep it locked, and report leaks fast. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "The Law Behind It"),
            "The Data Privacy Act of 2012, Republic Act No. 10173, was approved on August 15, 2012. It "
            "protects personal information, meaning information that can identify a person. It covers "
            "information processed by government offices and private businesses alike, and it created the "
            "National Privacy Commission to enforce it.",
            "The Act is not a reason to stop serving people. Offices still collect names, addresses and IDs "
            "because the work needs them. What the Act asks is that this information is collected for a "
            "clear purpose, used only for that purpose, kept safe, and not kept or shared beyond what the "
            "purpose needs.",
            ("quote", "Treat every record you hold as if its owner were standing beside your desk."),
            ("h", "Personal and Sensitive Information"),
            "The Act has a separate, stricter category called sensitive personal information. It includes a "
            "person’s race, ethnic origin, marital status, age, color, and religious, philosophical or "
            "political affiliations; their health, education, genetic or sexual life; and "
            "government-issued identifiers such as social security numbers and tax returns.",
            "Look at an ordinary office form with that list in mind. A business permit application, a "
            "payroll sheet, a scholarship list or a patient logbook can hold several of these at once. That "
            "is why a photo of one ID card is not a small thing. It can hold a full name, a birthdate and an "
            "ID number in a single picture.",
            ("point", "Personal information", "Anything that can identify a person, such as a name with an "
             "address, a photo or an email address."),
            ("point", "Sensitive personal information", "The stricter list above, including age, marital "
             "status, health and government-issued numbers."),
            ("point", "Not covered", "Information about a government official that relates to their "
             "position and functions, such as their title, office address and the duties of their position, is one of the Act’s exceptions."),
            ("h", "The Rights of the People in Your Records"),
            "The Act gives the people whose information you hold a set of rights. Knowing them helps you "
            "answer a client who asks what the office does with their papers.",
            ("point", "To be informed", "They can know that their information is being collected and "
             "processed."),
            ("point", "To access", "They can ask what information about them the office holds and how it "
             "is used."),
            ("point", "To correct", "They can dispute an error and have it corrected."),
            ("point", "To withdraw consent", "They can suspend or withdraw their consent to the processing of their information."),
            ("point", "To be paid for damages", "They can claim damages caused by a violation of their "
             "rights."),
            ("h", "Desk Habits That Protect Records"),
            "These habits need no technology. They are about how a desk is kept.",
            ("point", "Clean desk at the end of the day", "Put forms and folders with personal data in a "
             "drawer or cabinet that locks. A pile of applications on a counter overnight can be read by "
             "anyone who passes."),
            ("point", "Lock the screen when you stand up", "On Windows, press the Windows key and L. On a "
             "Mac, press Control, Command and Q. It takes two seconds."),
            ("point", "Turn screens away from the counter", "A client in line should not be able to read "
             "the record of the client before them."),
            ("point", "Shred, do not throw away", "Spoiled forms, extra photocopies and old printouts with "
             "names and numbers go through a shredder, not the wastebasket."),
            ("point", "Keep printouts off the printer tray", "Collect them at once, especially on a shared "
             "printer."),
            ("h", "Phones and Chats at Work"),
            "The clerk in our story meant well. She used her own phone to make the work "
            "faster. The risk was not the photo. It was where the photo stayed afterward.",
            ("point", "Use office tools for office records", "If your office has an official way to receive "
             "and send documents, use it, so the records stay in one controlled place."),
            ("point", "Delete what you no longer need", "If you had to take a photo of a document, send it "
             "where it belongs and then delete it from the phone, including the recently deleted folder."),
            ("point", "Lock the phone", "Part 12 covered screen locks. A phone that holds client data needs "
             "one."),
            ("point", "Be careful with group chats", "A list of names, addresses and amounts posted to a "
             "large group chat can be forwarded anywhere. Send it only to the people who need it."),
            ("h", "Collect Less, Keep Less"),
            "The safest record is the one an office never collected. Before adding a field to a form, ask "
            "whether the work truly needs it. Before keeping a photocopy of an ID, ask whether seeing the "
            "original was enough. And before keeping old files, check how long your office is required to "
            "keep them, then dispose of them properly when that period ends.",
            ("h", "Sharing Personal Data the Right Way"),
            ("point", "Ask why", "Share personal information only when there is a clear purpose and the "
             "person asking has a role that needs it."),
            ("point", "Share the least", "If someone needs a total, send the total, not the list of names "
             "behind it."),
            ("point", "Hide other recipients", "When emailing several clients at once, put their addresses in "
             "BCC so they cannot see each other’s addresses."),
            ("point", "Protect the file", "Send a link that only named people can open, rather than an "
             "attachment that can be forwarded anywhere."),
            ("h", "When Personal Data Leaks"),
            "Mistakes happen: a lost phone, a misdirected email, a stolen laptop. What matters next is speed "
            "and honesty.",
            ("point", "Report it inside the office at once", "Tell your supervisor and the person your office "
             "has named to handle data privacy. The Act requires organizations to designate people "
             "accountable for compliance."),
            ("point", "Contain it", "Change passwords, ask the wrong recipient to delete the email, or lock "
             "and erase a lost phone remotely if it was set up for that."),
            ("point", "Notify when required", "Under the National Privacy Commission’s breach rules, when "
             "sensitive personal information is believed to have been acquired by an unauthorized person "
             "and there is a real risk of serious harm, the affected people must be notified within 72 "
             "hours from discovery. The office’s privacy contact decides this, so report first."),
            "Hiding a breach is the worst choice. The Act penalizes knowingly concealing a security breach that should "
            "have been reported to the Commission with imprisonment of one year and six months to five "
            "years and a fine of ₱500,000 to ₱1,000,000.",
            ("h", "For Treasury Workers"),
            "A treasury holds tax declarations, business records, payrolls and the names of people who owe "
            "money. Keep delinquency lists and payroll sheets off public counters and out of group chats. "
            "When a taxpayer asks about their own account, confirm who they are before reading figures "
            "aloud, and keep the conversation at a level where the next person in line cannot hear.",
            ("h", "Mistakes to Avoid"),
            ("point", "Keeping client IDs in your phone’s gallery", "Send them where they belong, then delete "
             "them."),
            ("point", "Leaving forms on the counter overnight", "Lock them away."),
            ("point", "Posting lists of names in large chats", "Share only with those who need them."),
            ("point", "Keeping quiet about a leak", "Report it the same day."),
            ("h", "Stay-Safe Reminders"),
            ("point", "The Data Privacy Act covers offices too", "RA 10173 applies to government and private "
             "organizations alike."),
            ("point", "Some information is sensitive", "Age, marital status, health and government ID numbers "
             "need the most care."),
            ("point", "Privacy is a desk habit", "Clean desk, locked screen, shredder, careful chats."),
            ("point", "Leaks must be reported fast", "Notification rules can run on a 72-hour clock."),
            ("h", "Your Part 20 Action Plan"),
            ("point", "Today", "Look through your phone’s gallery and delete any client documents that "
             "belong in the office’s files instead."),
            ("point", "This week", "Find out who your office has named to handle data privacy, and save "
             "their contact details."),
            ("point", "This month", "Walk around your office after hours and note every place where personal "
             "data is left in the open."),
            "The clerk reported the stolen phone to her supervisor that same afternoon. The office’s privacy "
            "contact checked what the gallery held, notified the clients who were affected, and changed the "
            "office’s rule: client documents now come in through the office email and never stay on personal phones. The clerk was the first to say it was a better rule.",
            ("cta", "Read: Cybersecurity Series, Part 19: Email Security, Fake Senders and the Changed Bank Account", "/blog/cybersecurity-part-19-email-security/"),
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet, Securing It Before It Is Lost", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("cta", "Read: Cybersecurity Series, Part 6: Keeping Your Life in the Cloud Safe and Private", "/blog/cybersecurity-part-6-cloud-and-privacy/"),
            ("ask", "Where does personal data sit in the open in your office? What one change would fix it?"),
        ],
    },
    {
        "date": "September 22, 2027",
        "title": "Cybersecurity Series, Part 19: Email Security, Fake Senders and the Changed Bank Account",
        "slug": "cybersecurity-part-19-email-security",
        "category": "security",
        "summary": ("An email can show any name it likes. Learn how fake senders work, why a request to change "
                   "bank details deserves special care, how to handle attachments and links, and what an office "
                   "can set up so others cannot pretend to be it."),
        "publish_on": "2027-09-22 21:00",
        "body": [
            "The email came from a supplier the office had paid for years. Same name, same signature, same "
            "friendly tone. “Please note that we have changed banks,” it said. “Kindly send this month’s "
            "payment to the new account below.” The account was in a different name, but the email had an "
            "explanation for that too. The disbursing clerk had the voucher ready. Then she remembered a "
            "rule her office had written down the year before.",
            "(The clerk and the supplier are a composite. No real person, business or account is described.)",
            "Email is where scams dress up as business. After this post, you will know how a fake sender "
            "works, how to read who an email really came from, why a request to change bank details deserves "
            "a phone call every time, how to treat attachments and links, and what an office can set up so "
            "that others cannot easily send email in its name.",
            ("photo", "blog/cyber-email.jpg", "Email security: check the real address, call before changing "
             "bank details, treat attachments with care, and protect your office’s domain. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Scam That Costs the Most"),
            "The scam in our story has a name: business email compromise. A criminal pretends to be a "
            "supplier, a boss or a co-worker, and asks for a payment, for example to a new account. The FBI’s "
            "Internet Crime Complaint Center received 21,442 complaints of business email compromise in 2024, "
            "with losses close to $2.8 billion that year, according to the payments association Nacha’s "
            "summary of the FBI report.",
            "It works because it asks for something ordinary. Offices pay suppliers routinely. Suppliers "
            "change banks. The email does not need a virus or a link. It only needs someone to believe it.",
            ("quote", "A dangerous email can ask for nothing more than a new account number."),
            ("h", "How a Fake Sender Works"),
            ("point", "The display name is free text", "Anyone can make an email show “City Treasurer” or a "
             "supplier’s name. The name you see is not proof of who sent it."),
            ("point", "Lookalike addresses", "An address can differ from the real one by one letter, or use "
             "a free email service with the supplier’s name in it."),
            ("point", "A different reply-to", "The email comes from one address, but your reply goes to "
             "another. Check where “Reply” will actually send."),
            ("point", "A real account, taken over", "Sometimes the email really does come from the supplier’s "
             "address, because a criminal has broken into it. Then every check of the address passes."),
            "The last case is why checking the address is not enough on its own.",
            ("h", "The One Rule for Payment Changes"),
            "Part 18 put it in the office baseline as rule 8: payment requests and changes to bank details are "
            "confirmed by phone, using a number already on file.",
            ("point", "Use the number you already have", "Not the one in the email, which may belong to the "
             "criminal."),
            ("point", "Ask the person you usually deal with", "Describe the request and ask whether they sent "
             "it."),
            ("point", "Write down the confirmation", "Who you spoke to, when, and what they confirmed, and "
             "keep it with the voucher."),
            ("point", "Treat urgency as a warning", "A real supplier can wait an hour for a phone call."),
            ("h", "When the Boss Emails"),
            "A second version of the scam pretends to be someone senior. An email that appears to come from "
            "the office head asks a staff member, quietly and urgently, to buy prepaid load or gift cards, "
            "or to transfer money for something confidential. The pressure comes from rank as well as time.",
            ("point", "Confirm in person or by phone", "A real office head can be reached. A request that "
             "insists you must not call or tell anyone is the warning itself."),
            ("point", "Agree on this in advance", "Office heads can tell their staff now that they will "
             "never ask for money or load by email or chat alone."),
            ("h", "Attachments: Open With Care"),
            ("point", "Expect it before you open it", "An attachment you were not expecting deserves a quick "
             "message to the sender, through another channel, before you open it."),
            ("point", "Close documents that ask to “enable content”", "A document that will not show its "
             "contents until you enable editing or macros is a known trick to run harmful code. Close it "
             "and ask."),
            ("point", "Watch the file type", "A file named “invoice.pdf.exe” is a program, not a PDF. "
             "Compressed files and unusual types deserve extra care."),
            ("h", "Links: Look Before You Tap"),
            "On a computer, rest the mouse pointer on a link to see where it really goes. On a phone, press "
            "and hold the link to preview the address. Then read the domain from the right, as Part 15 "
            "showed. Better still, for anything that involves money or a login, ignore the link and open the "
            "site from your own bookmark.",
            ("h", "Protect Your Own Inbox"),
            ("point", "Two-factor authentication", "A taken-over email account can lead to other losses, because password resets go there. Parts 2 and 14 covered how to protect it."),
            ("point", "Check forwarding rules", "A criminal who gets into an account may set it to forward "
             "copies of your mail elsewhere. Look at your email settings for forwarding you did not set up."),
            ("point", "Use the official account for official work", "An office email address on the office’s "
             "own domain is easier to protect and to recognize than a personal free account."),
            ("h", "For Offices: Stop Others From Using Your Name"),
            "An office that owns its email domain can publish records that tell other mail servers which "
            "servers may send email for it. Three standards do this work:",
            ("point", "SPF", "Lists the servers allowed to send email for the domain."),
            ("point", "DKIM", "Adds a digital signature to outgoing email, so receivers can check it was not "
             "altered and came from the domain."),
            ("point", "DMARC", "Tells receivers what to do with email that fails those checks, such as "
             "rejecting it, and sends reports back to the domain owner."),
            "Setting these up is a task for whoever manages the office’s domain and email. With a strict DMARC policy in place, a criminal trying to send email from the office’s exact address has a much harder time reaching inboxes.",
            ("h", "For Treasury Workers"),
            "Treasuries pay suppliers, contractors and employees, which makes them a likely target. Keep a "
            "supplier file with bank details and phone numbers verified in person or by an official letter, "
            "and change it only after a confirmed call. Tell suppliers in writing that the office will never "
            "change their payment details because of an email alone, and ask them to tell you the same.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting the display name", "It can say anything."),
            ("point", "Calling the number in the email", "It may lead straight to the criminal."),
            ("point", "Enabling content to read a document", "Close it and ask the sender."),
            ("point", "Running official business on personal email", "It is harder to protect and to verify."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Business email compromise is expensive", "Close to $2.8 billion in losses reported "
             "to the FBI in 2024 alone."),
            ("point", "A changed bank account means a phone call", "Using a number already on file."),
            ("point", "Attachments and links need a pause", "Expect the file, preview the link."),
            ("point", "Offices can protect their name", "SPF, DKIM and DMARC make spoofing harder."),
            ("h", "Your Part 19 Action Plan"),
            ("point", "Today", "Check your email settings for forwarding rules you did not create."),
            ("point", "This week", "Write the payment-change rule on one line and share it with everyone "
             "who handles vouchers."),
            ("point", "This month", "Ask whoever manages your office’s domain whether SPF, DKIM and DMARC "
             "are set up."),
            "The clerk called the supplier using the number in the office’s supplier file. The supplier had "
            "not changed banks, and its own email account had been broken into a week earlier. The payment "
            "went to the right account, and the supplier thanked her for the call.",
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("cta", "Read: Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address", "/blog/cybersecurity-part-15-fake-websites/"),
            ("cta", "Read: Cybersecurity Series, Part 3: The Art of Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("ask", "Has your office ever received a request to change a supplier’s bank account by email? How did you check it?"),
        ],
    },
    {
        "date": "September 13, 2027",
        "title": "Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office",
        "slug": "cybersecurity-part-18-small-office-baseline",
        "category": "security",
        "summary": ("A small office does not need a security department to be hard to break into. Ten rules drawn "
                   "from this series fit on one page, each with an owner and a check you can finish in an "
                   "afternoon."),
        "publish_on": "2027-09-13 21:00",
        "body": [
            "The new office head of a small government unit asked her staff a simple question at their "
            "Monday meeting: “If our computers were attacked tonight, who would we call, and what would we "
            "lose?” Nobody answered. There were eight computers, two printers, one Wi-Fi router, a shared "
            "email password taped under a keyboard, and no one whose job it was to worry about any of it.",
            "(The office is a composite. No real office or person is described.)",
            "Seventeen parts of this series have covered passwords, scams, networks, ransomware, updates, "
            "phones and encryption, one topic at a time. A small office needs them together, on one page, "
            "with names attached. When you finish reading, you will have a ten-rule baseline you can print, "
            "an owner for each rule, a way to check each one in an afternoon, and a short list of what to do "
            "first if you can only do three things this month.",
            ("photo", "blog/cyber-baseline.jpg", "A one-page baseline: accounts, updates, backups and a plan, "
             "each with an owner. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why a Baseline, and Why One Page"),
            "A baseline is the minimum every computer, account and person in the office meets. It is not a "
            "policy manual. A one-page list can be posted, checked and remembered. A forty-page manual is "
            "filed and forgotten.",
            "The rules below are not new. Each one points back to a part of this series that explains the "
            "why and the how. The new part is putting a name beside each rule.",
            "A one-page baseline also helps on a new employee’s first day. They read one page and know the "
            "office’s rules from the start, instead of learning them after a mistake.",
            ("quote", "Security is a list of habits with someone’s name beside each one."),
            ("h", "The Ten Rules"),
            ("point", "1. One person, one account", "No shared logins. Every staff member signs in as "
             "themselves, so actions can be traced and access can be removed. (Part 2)"),
            ("point", "2. Long, unique passwords and two-factor authentication", "On email, banking, "
             "government portals and anything that holds money or personal data. (Parts 2 and 14)"),
            ("point", "3. Fewest possible administrators", "Daily work uses a normal account. Only the person "
             "who maintains a computer has administrator rights on it. (Part 8)"),
            ("point", "4. Updates on automatically", "Operating systems, browsers and office software. "
             "Replace devices that no longer receive updates. (Part 11)"),
            ("point", "5. Backups that are tested", "Keep several copies, one of them offline, and actually "
             "restore a file from the backup every few months. (Part 5)"),
            ("point", "6. Encrypted laptops and drives", "With recovery keys recorded and stored safely. "
             "(Part 17)"),
            ("point", "7. A separate guest Wi-Fi", "Visitors and personal gadgets stay off the network the "
             "office computers use. Change the router’s default password. (Part 4)"),
            ("point", "8. Verify before you pay or click", "Payment requests and changes to bank details are "
             "confirmed by phone using a number already on file. (Parts 3 and 15)"),
            ("point", "9. Access ends when the job ends", "When someone leaves or moves, their accounts and "
             "keys are removed on their last day. (Part 8)"),
            ("point", "10. A written plan and a call list", "Who to call, what to unplug and what to record "
             "when something goes wrong. (Part 9)"),
            ("h", "Do Not Forget the Paper"),
            "Not every leak is digital. The shared password taped under a keyboard in our story is a rule 1 "
            "and rule 2 problem written on paper.",
            ("point", "No passwords on notes", "Use a password manager, not sticky notes or a notebook in "
             "the drawer."),
            ("point", "Lock the screen when you stand up", "On Windows, the Windows key and L together lock "
             "it in a second. A computer left open at the counter is an open door."),
            ("point", "Shred what has personal data", "Printed taxpayer lists, old forms and draft reports go "
             "to a shredder, not the wastebasket."),
            ("point", "Clear the printer tray", "Collect printouts at once, especially from a shared "
             "printer."),
            ("h", "Give Every Rule an Owner"),
            "A rule without an owner becomes everyone’s job, which in practice means nobody’s. The owner is "
            "not the person who does all the work. It is the person who checks that the work was done.",
            ("point", "In a small office", "The office head can own rules 8 and 10. The person most "
             "comfortable with computers can own rules 3 to 7. The administrative officer can own rules 1 "
             "and 9, because they already handle hiring and leaving."),
            ("point", "Write the names on the page", "And review them when people change roles."),
            ("h", "Checking the Baseline in One Afternoon"),
            "These rules can be checked by looking, not by buying anything.",
            ("point", "Accounts", "List every shared login. Each one is a rule 1 problem to fix."),
            ("point", "Two-factor", "Open the security settings of the office email and the bank portal. "
             "Is two-factor on?"),
            ("point", "Updates", "On each computer, open the update settings. Note any that say updates are "
             "paused, or that the system is no longer supported."),
            ("point", "Backups", "Pick one file and try to restore it from the backup. Time how long it "
             "takes."),
            ("point", "Encryption", "Check each laptop for Device encryption, BitLocker or FileVault."),
            ("point", "Router", "Log in with the default password. If it works, rule 7 needs attention."),
            ("point", "Leavers", "Compare the list of accounts with the list of current staff."),
            ("h", "If You Can Only Do Three Things This Month"),
            ("point", "Turn on two-factor for email and banking", "Password reset links go to email, and banking is where the money is."),
            ("point", "Test one backup restore", "A backup you have never restored is a hope, not a plan."),
            ("point", "Write the call list", "Names and numbers for your IT help, your bank, and the "
             "cybercrime hotline 1326 from Part 9, printed and posted."),
            "These three guard against three painful losses: a taken email account, money sent to a scammer, and "
            "files held for ransom with no way back.",
            ("h", "Keep It Alive"),
            "A baseline decays. New staff join, new devices arrive, settings drift. Put a short review on the "
            "calendar every three months: the same afternoon checklist, the same owners, a few minutes at a "
            "staff meeting to report what changed. Keep a dated copy of each review. It shows auditors, and "
            "your future self, that the office took reasonable care.",
            ("h", "For Treasury Offices"),
            "A treasury handles public money and taxpayers’ personal data, so the Data Privacy Act’s "
            "requirement of reasonable and appropriate security measures applies directly. Two rules matter "
            "especially at the counter and in the vault room. Rule 8 protects against fake requests to change "
            "where payments go. Rule 9 makes sure a collector who transfers out can no longer sign in to the "
            "collection system.",
            ("h", "Mistakes to Avoid"),
            ("point", "Writing a manual instead of a page", "Short rules get followed."),
            ("point", "Buying tools before setting habits", "The first checks cost nothing but time."),
            ("point", "Leaving rules without owners", "Everyone’s job is nobody’s job."),
            ("point", "Checking once and stopping", "Review every three months."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Ten rules, one page", "Accounts, passwords, admin rights, updates, backups, "
             "encryption, Wi-Fi, verification, leavers and a plan."),
            ("point", "Every rule has an owner", "The owner checks; the work can be shared."),
            ("point", "Check by looking", "One afternoon finds the biggest gaps."),
            ("point", "Start with three", "Two-factor, a tested restore and a call list."),
            ("h", "Your Part 18 Action Plan"),
            ("point", "Today", "Print the ten rules and write an owner beside each."),
            ("point", "This week", "Do the one-afternoon check and list what failed."),
            ("point", "This month", "Fix the three first-priority items, then schedule the next review."),
            "Three months later, the office head asked the same question at another Monday meeting. This "
            "time the answer was on the wall, printed on one page, with a name beside every line.",
            ("cta", "Read: Cybersecurity Series, Part 17: Encryption Made Simple", "/blog/cybersecurity-part-17-encryption-made-simple/"),
            ("cta", "Read: Cybersecurity Series, Part 9: Incident Response, or What to Do When Something Goes Wrong", "/blog/cybersecurity-part-9-incident-response/"),
            ("cta", "Read: Cybersecurity Series, Part 11: Software Updates, the Fix You Keep Postponing", "/blog/cybersecurity-part-11-software-updates/"),
            ("cta", "Read: Cybersecurity Series, Part 8: Zero Trust, or Why Every Door Gets Checked", "/blog/cybersecurity-part-8-zero-trust/"),
            ("ask", "Which of the ten rules would your office fail today? I'd like to hear where you would start."),
        ],
    },
    {
        "date": "September 3, 2027",
        "title": "Cybersecurity Series, Part 17: Encryption Made Simple, Locking Data So a Lost Device Is Only a Lost Device",
        "slug": "cybersecurity-part-17-encryption-made-simple",
        "category": "security",
        "summary": ("Encryption turns readable data into scrambled data that only the right key can open. It "
                   "protects your phone, laptop, USB drive and messages once it is turned on, but one mistake "
                   "can lock you out of your own files."),
        "publish_on": "2027-09-03 21:00",
        "body": [
            "A treasury clerk took a USB drive home to finish a report over the weekend. On it was a "
            "spreadsheet of taxpayers with names, addresses and amounts paid. On the jeepney ride back on "
            "Monday, the drive slipped out of her bag. She noticed at the office, and her first question "
            "was the right one: “Was it encrypted?”",
            "(The clerk is a composite. No real person, office or file is described.)",
            "If the answer is yes, a lost drive is a lost piece of plastic. If the answer is no, anyone who "
            "picks it up can read every name on it. Read to the end and you will know what encryption is in "
            "plain words, where it already protects you, how to turn it on for your phone, laptop, USB "
            "drives and files, what end-to-end encryption means for your messages, and the one mistake that "
            "can lock you out of your own data.",
            ("photo", "blog/cyber-encryption.jpg", "Encryption made simple: phones, laptops, USB drives and "
             "messages, and a safe place for the recovery key. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "What Encryption Is"),
            "Encryption scrambles data so that it looks like nonsense to anyone without the key. The key is a secret, unlocked on your devices by your PIN, password or fingerprint. With the key, the data turns back "
            "into the original. Without it, guessing is so slow that, for well-made encryption with a strong "
            "password, it is not practical.",
            "Think of a locked box rather than a hidden one. Everyone can see the box. Only the person with "
            "the key can open it.",
            ("quote", "Encryption does not hide your data. It makes it useless to anyone without the key."),
            ("h", "Two Places Data Needs Protection"),
            ("point", "Data on the move", "What travels between your device and a website or app. Parts 15 "
             "and 16 covered this: the encrypted connection behind the address bar."),
            ("point", "Data at rest", "What sits on your phone, laptop, USB drive or backup. This part is "
             "mainly about that, because lost and stolen devices are a real, everyday risk."),
            ("h", "Your Phone: Probably Already Encrypted"),
            "Modern phones encrypt their storage, and the screen lock is what protects the key.",
            ("point", "Android", "Android’s own documentation says that all devices launching with Android "
             "10 and higher are required to use file-based encryption."),
            ("point", "iPhone", "Apple’s data protection is turned on when you set a passcode."),
            "That is why Part 12 insisted on a strong screen lock. A four-digit PIN that anyone can guess "
            "weakens the encryption behind it, because it unlocks the key.",
            ("h", "Your Laptop: Check It Today"),
            "Laptops deserve a check, because encryption may not be on, and a laptop can hold years of files.",
            ("point", "Windows", "Look in Settings for Device encryption, or for BitLocker. Which one you "
             "have depends on your Windows edition and your hardware."),
            ("point", "Mac", "Turn on FileVault in the Privacy and Security settings."),
            ("point", "Save the recovery key", "Turning on encryption gives you a recovery key. Store it "
             "somewhere safe and separate from the laptop: printed and filed, in your password manager, or, "
             "for office laptops, with your IT staff."),
            ("h", "The Mistake That Locks You Out"),
            "Encryption works both ways. If you lose the key and the recovery key, your own data is as "
            "unreadable to you as it is to a thief. A laptop that fails after an update and asks for a "
            "recovery key you never saved can mean files lost for good.",
            "This is the one mistake to plan against. Save the recovery key on the day you turn encryption on, "
            "and keep a backup of your important files, as Part 5 advised for ransomware.",
            ("h", "USB Drives and Single Files"),
            ("point", "Use an encrypted drive or container", "Encryption tools built into your laptop, or "
             "drives that require a password, protect the whole drive."),
            ("point", "Password-protect sensitive files", "Spreadsheets, PDFs and archives can be saved with a "
             "password that encrypts them. Use a long password, not the office name and the year."),
            ("point", "Send the password a different way", "If you email a protected file, send the "
             "password by text or call, never in the same email."),
            ("point", "Carry less", "The safest file on a USB drive is the one you did not copy to it."),
            ("h", "Backups Need Locks Too"),
            "A backup is a full copy of your data, which makes it just as valuable to a thief as the "
            "original. An external backup drive sitting in a desk drawer holds everything the laptop does.",
            ("point", "Encrypt the backup drive", "Use the same built-in tools as for the laptop, and save "
             "that recovery key too."),
            ("point", "Guard the cloud account", "A cloud backup is protected by the account that holds it. "
             "Part 6 covered the strong password and two-factor authentication it needs."),
            ("point", "Keep backups out of sight", "Store an office backup drive in a locked cabinet, not on "
             "top of the computer it backs up."),
            ("h", "Messages: What End-to-End Means"),
            "End-to-end encryption means a message is encrypted on the sender’s phone and decrypted only on "
            "the recipient’s phone. The company carrying it cannot read it in between.",
            ("point", "Some apps do it by default", "WhatsApp encrypts chats end to end. Meta announced on "
             "December 6, 2023 that end-to-end encryption would be the default for personal one-to-one chats "
             "in Messenger, with the rollout taking time to reach everyone."),
            ("point", "Ordinary text messages do not", "SMS messages are not end-to-end encrypted. Do not "
             "send passwords, ID numbers or account details by text."),
            ("point", "Encryption ends at the screen", "Anyone who unlocks the recipient’s phone, or takes a "
             "screenshot, can read the message. Encryption protects the trip, not what people do after."),
            ("h", "What Encryption Cannot Do"),
            ("point", "It cannot protect an unlocked device", "If the phone is open in a thief’s hand, the "
             "data is already decrypted."),
            ("point", "It cannot stop a phishing page", "If you type your password into a fake site, it "
             "goes to the scammer, encrypted all the way."),
            ("point", "It cannot fix a weak password", "A file protected by “123456” is barely protected."),
            ("h", "Why Offices Must Care"),
            "Section 20 of the Data Privacy Act of 2012, Republic Act No. 10173, requires those who handle "
            "personal information to put in place reasonable and appropriate security measures to protect "
            "it. For a treasury holding taxpayer names, addresses and payments, encrypting laptops and drives "
            "is a practical place to start.",
            ("h", "For Treasury Workers"),
            ("point", "Encrypt every office laptop", "And keep the recovery keys with the IT staff, recorded "
             "by device."),
            ("point", "No unencrypted copies of taxpayer lists", "If a file must leave the office, encrypt it "
             "first, and only with your office’s approval."),
            ("point", "Report a lost device at once", "Even an encrypted one. Your office may need to record "
             "the incident and check what was on it."),
            ("h", "Mistakes to Avoid"),
            ("point", "Not saving the recovery key", "Encryption without a recovery key can lock you out."),
            ("point", "Sending the password with the file", "Use a different channel."),
            ("point", "A weak screen lock", "It is the key to your phone’s encryption."),
            ("point", "Trusting SMS with secrets", "Text messages are not end-to-end encrypted."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Encryption makes lost data unreadable", "With a strong key, a lost device is only a "
             "lost device."),
            ("point", "Phones encrypt; laptops need checking", "Turn on Device encryption, BitLocker or "
             "FileVault."),
            ("point", "Save the recovery key", "Separate from the device, on the day you turn it on."),
            ("point", "End-to-end protects the trip", "Not the screen at the other end."),
            ("h", "Your Part 17 Action Plan"),
            ("point", "Today", "Check whether your laptop is encrypted, and turn it on if it is not."),
            ("point", "At the same time", "Save the recovery key somewhere safe and separate."),
            ("point", "This week", "Find the files with personal data on your USB drives, delete what you "
             "do not need, and protect the rest with a password."),
            "The clerk’s drive was never found. The file on it had been saved with a long password the week "
            "before, after an office briefing on data privacy. Her office recorded the loss, and nobody’s "
            "name was exposed.",
            ("cta", "Read: Cybersecurity Series, Part 16: Public Wi-Fi, Charging Stations and Staying Safe While Traveling", "/blog/cybersecurity-part-16-public-wifi-and-travel/"),
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("cta", "Read: Cybersecurity Series, Part 5: Inside a Ransomware Attack", "/blog/cybersecurity-part-5-ransomware/"),
            ("cta", "Read: Your Data at the Treasury Counter: What an Office May Share, and What It Must Protect", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "Is your laptop encrypted right now? I'd like to hear what you found when you checked."),
        ],
    },
    {
        "date": "August 25, 2027",
        "title": "Cybersecurity Series, Part 16: Public Wi-Fi, Charging Stations and Staying Safe While Traveling",
        "slug": "cybersecurity-part-16-public-wifi-and-travel",
        "category": "security",
        "summary": ("Is the free Wi-Fi at the airport or café safe? Mostly, yes, for a reason worth knowing. This "
                   "post explains the real risks today, what the FBI said about charging stations, and a simple "
                   "travel routine for your phone and laptop."),
        "publish_on": "2027-08-25 21:00",
        "body": [
            "A treasury employee on her way to a seminar in Manila waited at the bus terminal with an hour "
            "to spare and a phone at 15%. Two networks appeared: “Terminal_Free_WiFi” and “Terminal Free "
            "WiFi 2.” A charging kiosk nearby offered free USB ports. She wanted to check her email and send "
            "a report to her office. Which network was safe? And was the kiosk?",
            "(The employee and the terminal are a composite. No real person or place is described.)",
            "Advice about public Wi-Fi has changed, and some of the old warnings no longer fit. Stay with me "
            "to the end, and you will know why ordinary browsing on public Wi-Fi is safer than it used to "
            "be, which risks remain, what the FBI said about free charging stations and how experts reacted, "
            "and a short routine for keeping your devices safe on the road.",
            ("photo", "blog/cyber-travel.jpg", "Staying safe while traveling: check the network name, trust "
             "encryption but not every site, use your own charger, and keep sharing to contacts only. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Public Wi-Fi Is Safer Than It Used to Be"),
            "Years ago, most websites sent information without encryption, as the FTC notes, so anyone on the same network "
            "could read it. That has changed. The United States Federal Trade Commission now says that "
            "“because of the widespread use of encryption, connecting through a public Wi-Fi network is "
            "usually safe.”",
            "Encryption scrambles what travels between your device and a website or app, so the café owner "
            "or the person at the next table cannot read your password or your messages on the way. Part 15 "
            "explained the limit: encryption protects the line, not the honesty of the site at the other "
            "end.",
            ("quote", "The danger has moved from the network to the page you land on."),
            ("h", "The Risks That Remain"),
            ("point", "Lookalike network names", "Anyone can set up a hotspot and name it anything, including "
             "“Terminal_Free_WiFi.” A fake network cannot read encrypted traffic, but it can show you a "
             "fake login page."),
            ("point", "Sign-in pages that ask too much", "Some free networks show a sign-in page first. A "
             "page that asks for your email password, bank details or ID number to give you Wi-Fi is a "
             "warning sign."),
            ("point", "Fake update pop-ups", "A page that says your browser or app must update before you "
             "connect is not your device speaking, as Part 11 explained."),
            ("point", "Shared screens and printers", "Internet café computers and print shops can keep "
             "your files and stay logged in to your accounts after you leave."),
            ("h", "Choosing a Network"),
            ("point", "Ask the staff for the exact name", "If two names look alike, ask which one is real "
             "instead of guessing."),
            ("point", "Prefer your own mobile data for money", "For banking and e-wallets, your phone’s "
             "data connection, or a hotspot from your own phone, avoids the question entirely."),
            ("point", "Turn off auto-join", "Tell your phone to forget public networks after you leave, so "
             "it does not join a network with the same name somewhere else."),
            ("point", "Use apps and bookmarks, not links", "On any network, open your bank through its app "
             "or your bookmark."),
            ("h", "What About Free Charging Stations?"),
            "In April 2023, the FBI’s Denver field office posted a warning: “Avoid using free charging "
            "stations in airports, hotels or shopping centers. Bad actors have figured out ways to use public "
            "USB ports to introduce malware and monitoring software onto devices.” It advised carrying your "
            "own charger and cable and using an electrical outlet instead.",
            "The warning spread widely. A report by the security company Malwarebytes said many security "
            "experts were skeptical, and noted that the FBI office named no specific case, and that there were no "
            "known recent cases of this kind of attack, known as juice jacking.",
            "Both points can be true. The attack is possible in theory, no known recent case was found, "
            "and the fix costs almost nothing. Carry your own charger and plug it into a wall outlet, or carry a "
            "power bank. If you must use a USB port, and your phone asks whether to trust the device or "
            "allow file transfer, say no and keep it to charging only.",
            ("h", "What a VPN Does, and What It Does Not"),
            "A virtual private network, or VPN, sends your traffic through an encrypted tunnel to a VPN "
            "company’s server before it goes out to the internet. On public Wi-Fi, that hides which sites you "
            "visit from the network’s owner.",
            ("point", "It moves trust, it does not remove it", "The VPN company can now see what the café "
             "could have seen. Choose a provider you have reason to trust, or one your office provides."),
            ("point", "It does not stop fake websites", "A fake login page is just as fake through a VPN. "
             "Reading the address still matters."),
            ("point", "Be careful with unknown free VPN apps", "An app that routes all your traffic is a "
             "powerful thing to install from a company you know nothing about."),
            "For an office, a VPN the IT staff set up may be the approved way to reach office systems from "
            "outside. Ask before you travel.",
            ("h", "If Your Phone Is Lost on the Road"),
            "Travel is a time when phones go missing: in a taxi, at a terminal, in a hotel room. Part 12 covered the "
            "first hour. Before a trip, write your bank, e-wallet and network hotlines on paper and keep them "
            "separate from the phone, together with a copy of your ID. If the phone disappears, those numbers "
            "are the first thing you will need, and the phone that held them will be gone.",
            ("h", "Sharing and Bluetooth on the Road"),
            "Phones can send photos and files to nearby devices. In a crowded terminal, that feature can "
            "also receive unwanted files from strangers. Set nearby sharing to your contacts only, and turn "
            "on the setting to receive from everyone only when you need it, then turn it back off.",
            ("h", "A Short Travel Routine"),
            ("point", "Before you leave", "Update your phone and laptop, check that remote lock is on "
             "(Part 12), and back up your files."),
            ("point", "In transit", "Use your own data for money, keep the phone locked, and use your own "
             "charger."),
            ("point", "At the hotel or seminar", "Log out of any shared computer, delete your files from "
             "it, and collect every page you printed."),
            ("point", "When you return", "Remove public networks from your saved list."),
            ("h", "For Treasury Workers"),
            "Seminars, trainings and audits take treasury staff away from the office, sometimes with official "
            "files. Do not open the office’s financial systems over a public network unless your office has "
            "approved a secure way to do it. Carry only the files you need, keep them on an encrypted, "
            "password-protected device, and never leave a laptop or USB drive unattended at a venue.",
            ("h", "Mistakes to Avoid"),
            ("point", "Picking the network with the strongest signal", "Ask the staff for the real name."),
            ("point", "Giving personal details to a Wi-Fi sign-in page", "A café does not need your bank "
             "password."),
            ("point", "Leaving files at the print shop", "Delete them from the computer and log out."),
            ("point", "Leaving sharing open to everyone", "Set it to contacts only."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Encryption made public Wi-Fi safer", "The FTC now calls it usually safe."),
            ("point", "Fake pages remain a risk", "Read the address, as Part 15 showed."),
            ("point", "Use your own charger", "The FBI warning was debated, but the habit is free."),
            ("point", "Keep money on your own data", "Bank and e-wallet tasks can wait for your own "
             "connection."),
            ("h", "Your Part 16 Action Plan"),
            ("point", "Today", "Put a short charging cable and a wall adapter in your bag."),
            ("point", "Tonight", "Set nearby sharing to contacts only, and remove old public networks from "
             "your phone."),
            ("point", "Before your next trip", "Update your devices and confirm remote lock works."),
            "The employee asked the terminal staff, who said neither network was theirs; the terminal’s own "
            "Wi-Fi had a different name posted at the counter. She sent her report using her phone’s data, "
            "and charged her phone at a wall outlet with her own cable. It took the same hour.",
            ("cta", "Read: Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address", "/blog/cybersecurity-part-15-fake-websites/"),
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("cta", "Read: Cybersecurity Series, Part 4: Securing Your Home and Remote Network", "/blog/cybersecurity-part-4-home-network/"),
            ("cta", "Read: Cybersecurity Series, Part 11: Software Updates", "/blog/cybersecurity-part-11-software-updates/"),
            ("ask", "Where do you connect to public Wi-Fi most often, and how do you choose the network?"),
        ],
    },
    {
        "date": "August 16, 2027",
        "title": "Cybersecurity Series, Part 15: Fake Websites, and How to Read a Web Address",
        "slug": "cybersecurity-part-15-fake-websites",
        "category": "security",
        "summary": ("A fake login page can look perfect and still carry the padlock. Learn what the padlock "
                   "really means, how to read a web address in ten seconds, why the top search result can be a "
                   "trap, and which browser habits keep you on the real site."),
        "publish_on": "2027-08-16 21:00",
        "body": [
            "An office clerk needed to pay a bill online before lunch. She typed her bank’s name into a "
            "search engine and clicked the first result. The page looked exactly right: the logo, the colors, "
            "the login box. It even had the little padlock beside the address. She typed her username and "
            "password, and the page asked for the code sent to her phone. That is when she noticed the "
            "address had one letter wrong.",
            "(The clerk is a composite. No real person, bank or website is described.)",
            "A fake website does not have to look fake. It can copy the real one down to the last button, and it can "
            "carry the same padlock. After this post, you will know what that padlock does and does not "
            "promise, how to read a web address in about ten seconds, why the top search result can be a "
            "trap, and the browser habits that keep you on the real site.",
            ("photo", "blog/cyber-fake-sites.jpg", "Spotting fake websites: the padlock is not proof, read "
             "the address, skip search ads, and use bookmarks. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "What the Padlock Really Means"),
            "For years, people were told to look for the padlock. The padlock means the connection is "
            "encrypted: what you type travels scrambled between your browser and the site. It says nothing "
            "about who runs the site. A scammer can get the same encryption for a fake page.",
            "Google decided this misunderstanding was serious enough to act on. In Chrome version 117, "
            "released in September 2023, it replaced the padlock with a neutral “tune” icon, saying the "
            "change prevents the misunderstanding that the lock is linked to a page’s trustworthiness. "
            "Google reported that in one of its studies of 1,880 people, 89% misread what the padlock meant.",
            "The United States Federal Trade Commission makes the same point in its advice on public Wi-Fi: "
            "scammers “create fake websites and encrypt them to make you think they’re safe when they’re "
            "not.”",
            ("quote", "Encryption tells you the line is private. It does not tell you who is on the other end."),
            ("h", "Read the Address, Not the Page"),
            "The page can copy anything. The web address is the one thing a scammer cannot fully copy, "
            "because the real domain belongs to the real owner. Here is how to read it.",
            ("point", "1. Find the first single slash", "In https://www.example.com/login, look at the part "
             "between “https://” and the first “/” after it. Here that is www.example.com."),
            ("point", "2. Read that part from the right", "The ending and the name just before it, such as "
             "example.com, or example.gov.ph for a Philippine government site, tell you who owns the "
             "address. Everything further left is chosen by that owner."),
            ("point", "3. Watch for the trick", "In bank.com.secure-login.example/home, the domain is "
             "secure-login.example, not bank.com. The real bank’s name has been placed on the left, where "
             "anyone can put anything."),
            ("point", "4. Look for lookalike letters", "A swapped or added letter, “rn” standing in for “m”, "
             "or an extra word like “-verify” or “-support” can make a fake address look right at a "
             "glance."),
            "A useful local check: Philippine government websites end in .gov.ph. A page claiming to be a "
            "government office on any other ending deserves a second look.",
            ("h", "Why the Top Search Result Can Be a Trap"),
            "On December 21, 2022, the FBI warned that “cyber criminals are using search engine advertisement "
            "services to impersonate brands and direct users to malicious sites.” Sponsored results can appear above the real ones, so a fake page can sit at the very top. The FBI noted that financial "
            "websites, especially cryptocurrency platforms, had been impersonated to steal login details.",
            "Its advice was simple. Check the address before clicking an ad, and type the business’s address "
            "directly into the browser instead of searching for it. It also suggested an ad-blocking browser "
            "extension.",
            ("h", "Habits That Keep You on the Real Site"),
            ("point", "Bookmark the sites that hold money", "Your bank, your e-wallet’s web page, your "
             "government accounts. Use the bookmark every time instead of searching."),
            ("point", "Let your password manager be a detector", "A password manager, as Part 2 described, "
             "offers your saved password on the site it was saved for. If it offers nothing on a page that "
             "looks like your bank, stop and read the address."),
            ("point", "Heed the red warning screen", "Major browsers show a full-page warning when a site is "
             "reported as deceptive. Do not click past it."),
            ("point", "Do not log in from a link", "Links in texts and emails are where fake pages hide. "
             "Open the app or your bookmark instead, as Part 13 advised for e-wallets."),
            ("h", "Fake Shops and Fake Downloads"),
            "Fake websites do not only steal logins. Some sell things that never arrive, and some hand you a "
            "file that does harm.",
            ("point", "A price far below everyone else’s", "Ask why. A shop with no address, no history and "
             "only one way to pay deserves doubt."),
            ("point", "Payment to a personal account", "Be wary when a company asks you to pay into a personal name."),
            ("point", "“Your browser is out of date” pop-ups", "Modern browsers update themselves, as Part 11 explained. A web page offering a browser update is not your browser."),
            ("point", "Software from its official site or store", "Free copies of paid software from "
             "unknown sites can carry malware."),
            ("h", "Short Links and QR Codes Hide the Address"),
            "A shortened link and a QR code have the same weakness: you cannot see where they lead until you "
            "open them. Scammers use both. A QR code sticker can be placed over a real one on a poster, a "
            "parking meter or a payment counter.",
            ("point", "Preview before you open", "When your camera reads a QR code, look at the web address it shows before you tap, and read the domain from the right."),
            ("point", "Be careful with codes that ask for logins or payments", "A QR code on a flyer has "
             "no business taking you to your bank’s login page."),
            ("point", "Check the sticker", "At a counter, look for a code pasted on top of another one, "
             "and ask the staff if in doubt."),
            ("h", "Browser Extensions: Small Programs With Big Access"),
            "An extension can read and change the pages you visit. That is useful for a dictionary or an ad "
            "blocker, and dangerous for one you installed and forgot. Keep only the extensions you use, "
            "install them from the browser’s official store, and remove any that ask for access they do not "
            "need.",
            ("h", "For Treasury Workers"),
            "Offices that accept online payments should publish the exact address of their payment page, in "
            "full, on their official website and their posted notices. Tell taxpayers plainly that the office "
            "will never send a payment link by text message. A taxpayer who knows the right address can spot "
            "the wrong one.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting the padlock", "It means encrypted, not honest."),
            ("point", "Reading the address from the left", "The domain is on the right, just before the "
             "first single slash."),
            ("point", "Clicking the top result for your bank", "It may be a paid ad. Use a bookmark."),
            ("point", "Clicking past a browser warning", "The warning means the site has been reported as deceptive or harmful."),
            ("h", "Stay-Safe Reminders"),
            ("point", "The padlock is about privacy", "It does not prove who runs the site."),
            ("point", "The address is the truth", "Read the part just before the first single slash, from "
             "the right."),
            ("point", "Ads can impersonate brands", "Type the address or use a bookmark for anything that "
             "holds money."),
            ("point", "Your password manager can warn you", "If it stays silent on a familiar page, check "
             "the address."),
            ("h", "Your Part 15 Action Plan"),
            ("point", "Today", "Bookmark your bank, e-wallet and government accounts, and use only those "
             "bookmarks."),
            ("point", "This week", "Open your browser’s extensions page and remove anything you do not use."),
            ("point", "Practice", "For the next five links you open, read the domain before the page loads."),
            "The clerk closed the page without entering the code, then called her bank from the number on "
            "the back of her card and changed her password. Her account was untouched. The code she did not "
            "type was the one thing standing between the scammer and her money.",
            ("cta", "Read: Cybersecurity Series, Part 14: Your Social Media Account Is a Scammer’s Best Disguise", "/blog/cybersecurity-part-14-social-media-accounts/"),
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("cta", "Read: Cybersecurity Series, Part 3: The Art of Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("ask", "Have you ever landed on a fake website that looked real? What gave it away?"),
        ],
    },
    {
        "date": "August 6, 2027",
        "title": "Cybersecurity Series, Part 14: Your Social Media Account Is a Scammer’s Best Disguise",
        "slug": "cybersecurity-part-14-social-media-accounts",
        "category": "security",
        "summary": ("A hacked social media account lets a scammer borrow your face and your friends’ trust. "
                   "Accounts are taken in a few common ways. Lock yours down, stop posting certain things, and "
                   "know what to do in the first hour if it happens."),
        "publish_on": "2027-08-06 21:00",
        "body": [
            "The message came from a cousin, with his photo and his name, in the middle of a workday. “Pa-help "
            "naman, emergency lang. Can you send ₱3,000 to this e-wallet number? I’ll pay you back tonight.” "
            "The clerk who received it almost sent the money. Then she called her cousin. He was at home, "
            "confused, and locked out of his own account.",
            "(The clerk and her cousin are a composite. No real person is described.)",
            "A stolen social media account is valuable to a scammer, and not for your photos. It comes with a "
            "real face, a real name and hundreds of people who trust that face. When you finish reading, you "
            "will know why ordinary accounts are targeted, the tricks used to take them, the settings that "
            "lock yours down, what to stop posting, and the steps to take in the first hour after an account "
            "is taken.",
            ("photo", "blog/cyber-social.jpg", "Social media safety: a unique password, an authenticator app, "
             "a check of where you are logged in, and less personal detail in public. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Your Account Is Worth Stealing"),
            "Part 3 of this series showed that scammers work on trust. A message from a stranger asking for money is easy to ignore. The same message from a cousin’s account gets a second look, and sometimes a "
            "transfer.",
            ("point", "Your friends list", "Every person on it is a possible victim of a message that "
             "appears to come from you."),
            ("point", "Your pages and groups", "An account that manages a page or group can post to everyone "
             "who follows it."),
            ("point", "Your linked accounts", "Some apps let you sign in with a social media account. "
             "Losing it can mean losing access to those apps too."),
            ("quote", "A hacked account does not steal from you first. It steals from the people who trust you."),
            ("h", "How Accounts Get Taken"),
            "Taking an account does not require clever hacking. The tricks below are the same ones covered "
            "earlier in this series, pointed at a social media login.",
            ("point", "Fake warning messages", "A message says your page broke the platform’s rules and will "
             "be removed unless you log in through a link. The link goes to a copy of the login page."),
            ("point", "Reused passwords", "A password leaked from one website is tried on others. If you use "
             "the same one everywhere, one leak opens them all."),
            ("point", "The “wrong number” code", "A friend’s account, already taken, says it sent a code to "
             "your phone by mistake and asks you to send it back. That code is the key to your own account."),
            ("point", "Quizzes and fake apps", "Some ask you to sign in or to share details that answer "
             "security questions."),
            ("h", "Lock It Down: Five Settings"),
            ("point", "1. A unique, long password", "Use a password manager, as Part 2 described, so every "
             "account gets its own."),
            ("point", "2. Two-factor authentication with an app", "Turn it on, and choose an authenticator "
             "app or a security key over text messages where you can. Codes by text can be intercepted, and "
             "Part 12 showed how they can appear on a lock screen."),
            ("point", "3. Login alerts", "Ask to be notified when someone logs in from a new device."),
            ("point", "4. Check where you are logged in", "Look at the list of active sessions in the "
             "security settings, and log out of any device you do not recognize."),
            ("point", "5. Secure the email behind it", "A password reset goes to your email. If that email "
             "is weak, the social media account is weak too."),
            "On Facebook and Instagram, these settings are gathered in Accounts Center, under Password and "
            "security. Other platforms have similar menus. Set them up once, and check them every few months.",
            ("h", "Keep Your Recovery Details Current"),
            "Recovery details are the spare keys to your account, and they only help if they still work.",
            ("point", "An email you still use", "If the recovery email is an old address you no longer open, "
             "a reset link sent there is lost, or found by someone else."),
            ("point", "A phone number you still hold", "If you changed numbers, update the account before you "
             "need a code, not after."),
            ("point", "Backup codes on paper", "When you turn on two-factor authentication, platforms such as "
             "Facebook offer a set of recovery codes. Print or write them down and keep them at home, away "
             "from the phone."),
            ("h", "Post Less of What Unlocks You"),
            "Some of what people share in public is the same information used to verify them.",
            ("point", "Your full birthday", "Banks, hotlines and forms use it to confirm who you are. "
             "Consider hiding the year."),
            ("point", "Answers to security questions", "Your first school, your mother’s maiden name, your "
             "first pet. Posts and quizzes can reveal them."),
            ("point", "IDs, cards and boarding passes", "A photo of a new ID or a boarding pass can show "
             "numbers and barcodes you never meant to publish."),
            ("point", "Where you are right now", "Posting that the whole family is away for a week tells "
             "everyone the house is empty. Post the photos when you are home."),
            ("h", "When a Friend Asks for Money"),
            "Treat every money request sent through social media as unverified until you confirm it another "
            "way.",
            ("point", "Call them", "Use the number you already have, not one given in the message."),
            ("point", "Ask something only they know", "Part 10 suggested a family code word for exactly "
             "this."),
            ("point", "Do not be rushed", "Urgency is a scammer’s tool. A real emergency survives a "
             "two-minute phone call."),
            ("h", "The First Hour After an Account Is Taken"),
            ("point", "Start the recovery", "For Facebook, go to facebook.com/hacked from a browser and "
             "follow the steps. Other platforms have similar help pages."),
            ("point", "Secure your email first", "Change its password and check its recovery settings, so "
             "the attacker cannot reset everything again."),
            ("point", "Warn people another way", "Text or call family and close friends: ignore money "
             "requests from my account."),
            ("point", "Check linked money", "If your e-wallet or bank app uses the same email or password, "
             "change those too, and watch for transactions you did not make."),
            "If someone was tricked into sending money, report it to their e-wallet or bank at once, as Part "
            "13 described.",
            ("h", "For Treasury Workers and Office Pages"),
            "Offices post announcements, schedules and payment reminders on social media. A taken-over office "
            "page could post a fake payment account to the whole town.",
            ("point", "More than one admin", "At least two trusted staff, each with two-factor "
             "authentication, so one lost account does not lock the office out."),
            ("point", "Personal and official stay separate", "Give each staff member access through their own account instead of sharing one login, and remove access when a person leaves the office."),
            ("point", "State the official channels", "Pin a post that lists the only accounts that may "
             "receive payments, and repeat that the office never asks for codes or passwords."),
            ("h", "Mistakes to Avoid"),
            ("point", "Sending a code “back” to a friend", "It is your login code, and the friend’s account "
             "is already taken."),
            ("point", "Relying on text-message codes alone", "An authenticator app is harder to "
             "intercept."),
            ("point", "Leaving old devices logged in", "An old phone sold or lost can still be signed in."),
            ("point", "Posting while away", "Share the trip after you are back."),
            ("h", "Stay-Safe Reminders"),
            ("point", "Your account carries your friends’ trust", "That trust is what scammers steal."),
            ("point", "A takeover can start with a simple trick", "A fake warning, a reused password or a "
             "code sent “back.”"),
            ("point", "Two-factor with an app", "Plus login alerts and a check of active sessions."),
            ("point", "Verify money requests by phone", "Every time, no matter whose face is on the message."),
            ("h", "Your Part 14 Action Plan"),
            ("point", "Tonight, ten minutes", "Turn on two-factor authentication with an authenticator app, "
             "turn on login alerts, and log out of devices you do not recognize."),
            ("point", "This week", "Hide your birth year and remove posts that show IDs or boarding passes."),
            ("point", "Tell your family", "Agree that any money request by chat will be confirmed by a call."),
            "The clerk’s cousin got his account back two days later. The first thing he posted was a warning. "
            "Three relatives replied that they had received the same message. One had already sent the money.",
            ("cta", "Read: Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law", "/blog/cybersecurity-part-13-ewallets-and-the-anti-scam-law/"),
            ("cta", "Read: Cybersecurity Series, Part 3: The Art of Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("ask", "Has a friend’s hacked account ever asked you for money? I'd like to hear how you spotted it."),
        ],
    },
    {
        "date": "July 28, 2027",
        "title": "Cybersecurity Series, Part 13: E-Wallets and the Anti-Scam Law, Guarding Your Money and Your Name",
        "slug": "cybersecurity-part-13-ewallets-and-the-anti-scam-law",
        "category": "security",
        "summary": ("Lending your e-wallet account for a small fee can make you a money mule under Republic Act "
                   "No. 12010. The anti-scam law also tells banks and e-wallets what they must do, and a few "
                   "habits keep your money and your name safe."),
        "publish_on": "2027-07-28 21:00",
        "body": [
            "A college student gets a message from a friendly stranger. He runs a small online business, he "
            "says, and his own e-wallet has reached its limit. Could she let him use her verified account for a "
            "few weeks? Money would come in and go out, and she would keep ₱500 a week for her trouble. It "
            "sounds harmless. Nobody is asking for her money, only her account.",
            "(The student and the stranger are a composite. No real person is described.)",
            "That account is exactly what scammers want. Stolen money has to land somewhere with a real, "
            "verified name on it before it disappears, and a borrowed account gives them that name. Read to "
            "the end and you will know what the Anti-Financial Account Scamming Act says, why lending an "
            "account is no longer a small favor, what your bank or e-wallet must do to protect you, and the "
            "habits that keep both your money and your name safe.",
            ("photo", "blog/cyber-ewallet.jpg", "E-wallet safety: never lend your account, never share a code, "
             "use the official app, and report fast. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Law in One Paragraph"),
            "Republic Act No. 12010, the Anti-Financial Account Scamming Act, was approved on July 20, 2024. It "
            "covers financial accounts in a broad sense. Section 3 includes deposit, investment and credit card "
            "accounts, and it names e-wallet accounts too. Section 4 then defines three kinds of offenses: "
            "acting as a money mule, carrying out a social engineering scheme, and economic sabotage.",
            ("h", "Money Mules: When an Account Becomes a Crime"),
            "Section 4(a) treats a person as a money mule when they do certain acts “for the purpose of "
            "obtaining, receiving, depositing, transferring, or withdrawing proceeds that are known to be "
            "derived from crimes, offenses, or social engineering schemes.” The acts listed include:",
            ("point", "Using, borrowing or allowing the use of an account", "This is the student’s case: "
             "letting someone else move money through her name."),
            ("point", "Opening an account under a fake name", "Or with another person’s identity or ID "
             "documents."),
            ("point", "Buying, renting, selling or lending an account", "Section 5 separately lists buying "
             "or selling a financial account as an offense."),
            ("point", "Recruiting others", "Hiring or inducing other people to do any of the acts above."),
            "Under Section 16(a), a money mule faces imprisonment of six to eight years, a fine of ₱100,000 to "
            "₱500,000, or both, at the court’s discretion. That is a heavy price for ₱500 a week.",
            "Notice the words “known to be derived.” The law aims at people who know, or come to know, where "
            "the money is from. But a stranger paying you to use your account is the warning itself. Once you "
            "see money from people you do not know passing through your name, it becomes hard to claim you did not know.",
            ("quote", "Nobody pays to borrow an account for an honest reason."),
            ("h", "Social Engineering: Stealing the Keys"),
            "Section 4(b) covers how scammers get your details in the first place. A social engineering scheme is committed by a "
            "person who obtains another person’s sensitive identifying information through deception or "
            "fraud, by pretending to act for a bank or e-wallet, or by using electronic communications.",
            "In practice, that is the text saying your account will be locked unless you “verify” it, the "
            "caller who claims to be from customer support and needs your one-time code, and the link to a "
            "page dressed up like your e-wallet’s login. Part 3 of this series showed how these tricks play "
            "on fear and urgency. The penalty under Section 16(b) is ten to twelve years of imprisonment, a "
            "fine of ₱500,000 to ₱1,000,000, or both.",
            ("h", "When It Becomes Economic Sabotage"),
            "Section 4(c) raises these acts to economic sabotage when they are committed by a group of three or "
            "more people conspiring together, against three or more victims, using a mass mailer, or through "
            "human trafficking. Section 16(c) sets the penalty at life imprisonment, a fine of ₱1,000,000 to "
            "₱5,000,000, or both. Scam operations that send messages in bulk to strangers can fall into this "
            "group.",
            ("h", "What Your Bank or E-Wallet Must Do"),
            "The law also places duties on institutions. Section 6 says they “shall ensure that access to their "
            "clients’ Financial Account is protected by adequate risk management systems and controls such as "
            "MFAs, FMS, and other Account Owner enrollment and verification processes.” MFA is multi-factor "
            "authentication, which Part 2 covered. FMS is a fraud management system, which watches for "
            "unusual transactions.",
            "Section 7 lets an institution temporarily hold funds involved in a disputed transaction, for a period set by the Bangko Sentral ng Pilipinas (BSP) that may not exceed 30 "
            "calendar days unless a court extends it. Section 8 calls for a coordinated verification process "
            "between the institutions and the account owners involved when a transaction is disputed.",
            "There is one more line worth reading. Section 6 adds that institutions found by the BSP to have "
            "adequate controls “shall not be liable for any loss or damage” arising from these offenses. In "
            "other words, your own care still matters. The law can punish a scammer, but your habits are what "
            "keep your money from leaving in the first place.",
            ("h", "Habits That Keep Your E-Wallet Safe"),
            ("point", "Never share a one-time code or PIN", "No real bank or e-wallet employee needs it. A "
             "request for it is the scam."),
            ("point", "Use only the official app", "Install it from the official app store, and reach "
             "support through the contact details inside the app, not a number in a text message."),
            ("point", "Ignore links in messages about your account", "Open the app yourself and check there. "
             "If something is wrong, the app will show it."),
            ("point", "Keep a separate wallet PIN", "Part 12 explained why the wallet’s PIN should differ "
             "from the phone’s screen lock."),
            ("point", "Turn on transaction alerts", "An alert for every transaction lets you spot one you did "
             "not make within minutes."),
            ("point", "Never lend, rent or sell your account", "Not to a friend’s business, not for a fee, "
             "not for a few weeks."),
            ("h", "If Money Leaves Without You"),
            "Speed matters, because the hold under Section 7 can only work on money that has not yet been "
            "moved on.",
            ("point", "Call your institution first", "Use the hotline printed in the app or on the official "
             "website. Report the transaction and ask them to secure the account."),
            ("point", "Write everything down", "Times, amounts, reference numbers, and screenshots of the "
             "messages that tricked you."),
            ("point", "Report the scam", "The Cybercrime Investigation and Coordinating Center’s hotline, "
             "1326, appears in Part 9 of this series."),
            ("point", "Escalate if needed", "If your bank or e-wallet does not resolve your complaint, the "
             "BSP accepts consumer complaints about the institutions it supervises, including through its "
             "online chat assistant."),
            ("h", "For Treasury Workers"),
            "Some treasuries now take payments through bank transfers and e-wallets. That brings these scams to the "
            "counter. A taxpayer may receive a fake message, supposedly from the treasury, asking them to pay "
            "into a personal account. Post your official payment channels where taxpayers can see them, say "
            "clearly that the office never asks for one-time codes, and never use a personal account to receive "
            "public money.",
            ("h", "Mistakes to Avoid"),
            ("point", "Thinking “it is only my account”", "Under Section 4(a), lending it to move "
             "proceeds of a crime can make you a money mule."),
            ("point", "Trusting a familiar logo", "A message can copy any bank’s colors and name. Check "
             "inside the official app."),
            ("point", "Waiting a day to report", "Every hour gives the scammer time to move the money on."),
            ("point", "Assuming the bank will pay it back", "Section 6 protects institutions that have "
             "adequate controls. Prevention is your best protection."),
            ("h", "Stay-Safe Reminders"),
            ("point", "An account is a key", "Scammers need real names to receive stolen money. Do not "
             "lend yours."),
            ("point", "RA 12010 has teeth", "Six to eight years for money mules, ten to twelve for social "
             "engineering, and up to life for economic sabotage."),
            ("point", "Codes stay with you", "No legitimate employee asks for your one-time code or PIN."),
            ("point", "Report within minutes", "Call your institution first, then report the scam."),
            ("h", "Your Part 13 Action Plan"),
            ("point", "Tonight", "Turn on transaction alerts and check that your wallet has its own PIN."),
            ("point", "This week", "Save your bank and e-wallet hotlines from their official apps or "
             "websites, and write them on paper at home."),
            ("point", "Talk to one person", "Tell a student or relative that renting out an account is a "
             "crime, and why."),
            "The student in our story said no and blocked the stranger. Weeks later, a classmate who said yes "
            "found her account frozen and her name in a police report. The ₱500 a week did not cover the "
            "lawyer.",
            ("cta", "Read: Cybersecurity Series, Part 12: Your Phone Is Your Wallet", "/blog/cybersecurity-part-12-securing-your-phone/"),
            ("cta", "Read: Cybersecurity Series, Part 3: The Art of Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("cta", "Read: Cybersecurity Series, Part 9: Incident Response", "/blog/cybersecurity-part-9-incident-response/"),
            ("ask", "Has anyone ever offered to pay you to use your account? I'd like to hear how you answered."),
        ],
    },
    {
        "date": "July 19, 2027",
        "title": "Cybersecurity Series, Part 12: Your Phone Is Your Wallet, Securing It Before It Is Lost",
        "slug": "cybersecurity-part-12-securing-your-phone",
        "category": "security",
        "summary": "A phone now holds an e-wallet, a bank app, email, photos and the codes that unlock "
                   "everything else. This part shows how to lock it properly, keep harmful apps off it, hide "
                   "one-time codes from a stranger’s view, and what to do in the first hour after it is lost "
                   "or stolen.",
        "publish_on": "2027-07-19 21:00",
        "body": [
            "A jeepney ride home after a long day. A phone in the back pocket, then not. By the time its owner "
            "notices, the phone is gone, and with it the e-wallet, the bank app, the email account, the "
            "family photos and the text messages where every one-time code arrives.",
            "A lost phone used to mean a lost phone. Today it can mean a lost wallet, a lost identity and a "
            "few anxious days of resetting passwords. The good news is that much of the damage can be limited by settings that take about fifteen minutes to set up, before anything happens.",
            "In this part, we treat the phone as what it has become: the key to almost everything else. By the last section, you will know how to lock your phone properly, how to keep harmful apps "
            "off it, how to stop one-time codes from being read off your screen, how to set up remote "
            "locking and erasing, and what to do in the first hour after a phone is lost or stolen.",
            ("photo", "blog/cyber-phone.jpg", "Securing your phone: lock it, install apps only from the "
             "store, hide codes on the lock screen, and set up remote lock and erase. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why the Phone Is the Master Key"),
            "Part 2 called email the master key to your accounts, because a password reset link goes there. "
            "The phone has become an even bigger key. It receives the reset links, the "
            "one-time codes by text message and the approval prompts. It also holds apps that are already "
            "signed in.",
            "That means a thief does not need to know your passwords. If the phone is unlocked, or easy to "
            "unlock, the apps are open and the codes arrive on the same screen. Securing the phone protects "
            "every account that trusts it.",
            ("quote", "Whoever holds your unlocked phone holds the keys to your accounts."),
            ("h", "Step 1: A Real Screen Lock"),
            ("point", "Use a PIN or password, not a simple swipe", "A six-digit PIN or a longer passcode is "
             "harder to guess than four digits. Avoid birthdays, 123456 and repeated digits."),
            ("point", "Add a fingerprint or face unlock", "They make a strong PIN easy to live with, because "
             "you type it less often. The PIN still matters: it is the fallback a thief would try."),
            ("point", "Set a short auto-lock", "Thirty seconds to one minute. A phone that stays unlocked for "
             "ten minutes on a table is an open wallet."),
            ("point", "Watch for shoulder surfers", "In a crowded line or vehicle, people can watch you type "
             "your PIN, then take the phone later. Use your fingerprint or face in public, or shield the "
             "screen."),
            ("h", "Step 2: Lock the Apps That Hold Money"),
            "E-wallet and banking apps have their own PIN or biometric login. Turn it on, and use a PIN that "
            "is different from the phone’s screen lock. If someone learns the screen lock by watching, the "
            "money still has a second door.",
            "Do not save the PINs in your notes app, in a photo of a card, or in a message to yourself. A "
            "thief who opens the phone can find them there. A password manager, as described in Part 2, "
            "is the right place.",
            ("h", "Step 3: Keep Codes Off the Lock Screen"),
            "One-time codes by text message can appear in a notification on the lock screen. Anyone holding "
            "the phone, even a locked one, may be able to read them. That turns your second factor into "
            "something a thief can see without your PIN.",
            ("point", "Hide message content on the lock screen", "Look in your phone’s notification settings "
             "for the option to hide sensitive content or show notifications only when the phone is "
             "unlocked."),
            ("point", "Prefer an authenticator app or passkey", "Where an account offers it, use an "
             "authenticator app or a passkey instead of text messages, as Part 2 recommended. They are "
             "harder to intercept."),
            ("point", "Never read a code to anyone", "A one-time code is meant for you alone. Treat anyone who asks for it, by call, text or chat, as a scammer, as Part 3 explained."),
            ("h", "Step 4: Only Trusted Apps"),
            "Harmful apps are one way phones are attacked. Some pretend to be games, flashlight "
            "tools or loan apps, then read messages, show fake login screens or send data away.",
            ("point", "Install from the official store", "On Android, Google’s help explains that Google "
             "Play Protect runs a safety check on Play Store apps before you download them, checks the device "
             "for harmful apps from other sources, and may deactivate or remove harmful apps. It is on by "
             "default. Check it under your profile picture in the Play Store, then Play Protect."),
            ("point", "Be wary of app files sent by message", "A file that ends in .apk, sent through chat "
             "and described as an update, a loan app or a delivery tracker, is a way to install malware outside the store’s checks."),
            ("point", "Review permissions", "A calculator does not need your contacts or text messages. Part 6 "
             "showed how to review what each app can reach. Remove apps you no longer use."),
            ("point", "Keep the phone updated", "As Part 11 explained, updates close known flaws. Check for "
             "them under System, then Software updates, on Android, or Settings on an iPhone."),
            ("h", "Step 5: Set Up Remote Lock and Erase Today"),
            "This step is easy to skip, and it is the one people wish they had done when the phone is gone. "
            "Both major phone systems can locate, lock and erase a lost phone from another device, but only if "
            "the feature was set up before the loss.",
            ("point", "Android: Find Hub", "Google’s help describes how Find Hub can show the phone’s "
             "estimated location, ring it at full volume for five minutes even when silenced, lock it with a "
             "“Mark as lost” option that also turns off notifications, and erase it. To lock or erase, the "
             "phone must have power, be connected, be signed in to a Google Account, and have Find Hub "
             "turned on."),
            ("point", "iPhone: Find My", "Apple’s help advises putting a stolen device in Lost Mode as "
             "quickly as possible, through iCloud.com/find. Apple also describes Stolen Device Protection, "
             "which requires Face ID or Touch ID for some sensitive changes, even if someone knows the "
             "passcode."),
            ("point", "Test it once", "Sign in from a computer or a family member’s phone and make your own "
             "phone ring. If it works today, it will work when you need it."),
            ("h", "Step 6: Back It Up"),
            "Photos of children growing up, receipts saved for a tax return, contacts collected over years: "
            "these are worth more than the phone. Turn on the phone’s cloud backup, or copy important files to "
            "a computer regularly. Part 5 explained why a backup the attacker cannot reach is the cure for "
            "ransomware. For a lost phone, a backup is the difference between buying a new phone and starting "
            "over.",
            ("h", "The First Hour After a Loss"),
            ("point", "1. Lock it remotely", "Use Find Hub or Find My to mark it as lost. Apple advises not to "
             "add your contact details to the lock message if the phone was stolen, since a thief could use "
             "them for a scam."),
            ("point", "2. Call your mobile network", "Ask them to block the SIM, so no one receives your "
             "codes by text. Request a replacement SIM for the same number."),
            ("point", "3. Call your bank and e-wallet providers", "Use the hotline on their official website "
             "or app, and ask them to lock or watch the accounts."),
            ("point", "4. Change the key passwords", "From a safe device, change your email password first, "
             "then the accounts that matter most, and sign the lost phone out of them."),
            ("point", "5. Erase only when hope is gone", "Apple’s help calls erasing a last resort, because it "
             "cannot be undone, and Google’s help notes that an erased phone can no longer be located."),
            ("point", "6. Report it", "Report the theft to the police. The SIM Registration Act, Republic Act "
             "No. 11934, signed in October 2022, links each SIM to a registered owner, so report quickly if a "
             "SIM in your name might be misused."),
            ("h", "For Treasury Workers and Office Phones"),
            "A work phone or a personal phone used for work carries more than your own data. It may hold "
            "group chats where collection reports are shared, photos of documents, or email with taxpayer "
            "information. Losing it can become a personal data breach, which Part 9 explained may need to be "
            "reported.",
            "Keep work documents in the office’s approved storage rather than in the phone’s gallery. Delete "
            "photos of IDs and forms once they are filed. And tell the office right away if a phone with work "
            "data is lost. A quick report makes containment possible.",
            ("h", "Stay-Safe Reminders"),
            ("point", "The phone is the master key", "It receives codes and holds signed-in apps."),
            ("point", "Two locks for money", "A strong screen lock, and a different PIN for wallets and banks."),
            ("point", "Hide codes and trust only the store", "Codes off the lock screen, apps from the "
             "official store."),
            ("point", "Prepare for loss today", "Set up remote lock, test it, and keep a backup."),
            ("h", "Your Part 12 Action Plan"),
            ("point", "Fifteen minutes tonight", "Set a six-digit PIN, a one-minute auto-lock and hidden "
             "lock-screen content."),
            ("point", "Check the wallet apps", "Turn on their own PIN or biometric login, different from the "
             "screen lock."),
            ("point", "Ring your own phone", "Open Find Hub or Find My from another device and make your phone "
             "ring. Then write your bank, e-wallet and network hotlines on paper and keep them at home."),
            "If the jeepney ride ever goes wrong, those fifteen minutes will be the best you ever spent on "
            "your phone.",
            "Thank you for following this series through twelve parts. Share it with one person who would "
            "benefit, especially someone who handles money, records or the accounts of an elderly parent.",
            ("cta", "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("cta", "Read: Cybersecurity Series, Part 6: Keeping Your Life in the Cloud Safe and Private", "/blog/cybersecurity-part-6-cloud-and-privacy/"),
            ("cta", "Read: Cybersecurity Series, Part 11: Software Updates", "/blog/cybersecurity-part-11-software-updates/"),
            ("cta", "Read: Cybersecurity Series, Part 9: Incident Response", "/blog/cybersecurity-part-9-incident-response/"),
            ("ask", "If your phone disappeared right now, which account would you need to protect first?"),
        ],
    },
    {
        "date": "July 9, 2027",
        "title": "Cybersecurity Series, Part 11: Software Updates, the Fix You Keep Postponing",
        "slug": "cybersecurity-part-11-software-updates",
        "category": "security",
        "summary": "An attack does not always need a genius. Sometimes a computer that missed an update is enough. This part "
                   "explains what an update fixes, why the WannaCry outbreak spread through machines that were "
                   "two months behind, what end of support means for an old computer, and how a small office "
                   "can keep every device current without stopping work.",
        "publish_on": "2027-07-09 21:00",
        "body": [
            "Picture the computer in the corner of the office, with a small message that has been waiting for weeks. “Updates are ready. Restart now?” And every day, someone clicks “Remind me tomorrow,” "
            "because there is a line at the window and the restart takes too long.",
            "That small button is a real security decision, even if it does not feel like one. "
            "In this part, we look at what an update actually does, what happens when it is skipped, and how "
            "to build a routine that keeps every device current without getting in the way of the work. Stay with me to the end, and you will know how attackers use known flaws, what end of support means "
            "for an old computer or phone, how to check whether a device is up to date, and how a small office "
            "can plan its updates instead of postponing them.",
            ("photo", "blog/cyber-updates.jpg", "Software updates: install them, restart, replace devices "
             "that no longer get them, and keep a simple list. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "What an Update Really Fixes"),
            "Software is written by people, and people make mistakes. Some mistakes only cause a crash. Others "
            "open a door: a way for someone outside to read files, run their own program or take control of "
            "the device. These doors are called vulnerabilities.",
            "When a maker finds one, or someone reports it, the maker writes a fix and sends it out as an "
            "update. Some updates add features, but the ones that matter here are security updates, sometimes "
            "called patches.",
            "Here is the uncomfortable part. Once a fix is published, the flaw is no longer a secret. Attackers "
            "can study the update, work out what it changed, and build a tool that attacks every device that "
            "has not installed it yet. From that day, the race is between the person who installs the update "
            "and the person who wants to use the flaw.",
            ("quote", "An update you postpone is a door you have been told about and left open."),
            ("h", "A Lesson From 2017: WannaCry"),
            "On May 12, 2017, Microsoft detected a new kind of ransomware that spread like a worm. It became "
            "known as WannaCry, or WannaCrypt. It locked files and demanded payment, as described in Part 5, "
            "but its spread was what made it famous. It did not need anyone to click a link. Once inside a "
            "network, it searched for other Windows computers with a particular flaw in file sharing and "
            "copied itself to them.",
            "The fix for that flaw was not new. Microsoft had released it on March 14, 2017, as security "
            "bulletin MS17-010, about two months before the outbreak. Microsoft’s guidance at the time said "
            "that customers with Windows Update turned on were protected against attacks on this "
            "vulnerability. Microsoft also wrote that the exploit worked against unpatched Windows 7 and "
            "older systems, and that Windows 10 computers were not affected.",
            "Microsoft then took the unusual step of making the fix available for systems it no longer normally supported, including Windows XP. The lesson is "
            "simple. The damage did not come from a flaw nobody knew about. It came from a fix that had not "
            "been installed.",
            ("h", "Known Flaws Are Enough"),
            "News stories like to talk about “zero-day” attacks, which use a flaw before any fix exists. Those "
            "are real. But an attacker does not need one when a flaw that was fixed long ago is still open on "
            "the computer in front of them.",
            "The United States Cybersecurity and Infrastructure Security Agency keeps a public list called the "
            "Known Exploited Vulnerabilities Catalog: flaws that attackers are known to have used in real "
            "attacks. CISA adds a flaw to the list only when there is reliable evidence it has been exploited and a clear fix exists, such as a vendor update, and it urges organizations to treat these as a high priority. If a flaw is on that list and your device has not been updated, you are not waiting for a rare event. You are exposed to a method that has already worked elsewhere.",
            ("h", "When the Updates Stop: End of Support"),
            "Every product has a last day of security updates. After that, new flaws are found, but no fixes "
            "arrive. The device still turns on and still looks fine, which is what makes this risk easy to "
            "miss.",
            ("point", "Windows 10", "Microsoft ended support on October 14, 2025. Its help page says the "
             "software will continue to function, but security updates and fixes are no longer provided. "
             "Microsoft offers a paid Extended Security Updates program for consumers that can cover a "
             "Windows 10 device until October 12, 2027, as a bridge to a newer system."),
            ("point", "Phones", "Each phone maker decides how long a model receives updates. An old phone "
             "that still holds your e-wallet, email and photos may have stopped receiving them years ago."),
            ("point", "Routers and gadgets", "As Part 4 and Part 10 explained, routers, cameras and smart "
             "devices run software too, and some stop receiving updates early."),
            "For an office, this turns into a planning question, not a technical one. A computer that handles "
            "collections, payroll or personal data should not be running a system that no longer receives "
            "security fixes. Its replacement belongs in the budget before its last update, not after an "
            "incident.",
            ("h", "How to Check a Device in Two Minutes"),
            ("point", "Windows", "Open Settings, then Windows Update. It shows whether updates are waiting, "
             "and whether a restart is needed to finish them."),
            ("point", "Android", "Google’s help says to open Settings, tap About phone, then Android version, "
             "where the Android security update date is listed. Updates themselves are under System, then "
             "Software updates. Google advises connecting to Wi-Fi and charging to at least 75% first."),
            ("point", "Browsers", "Chrome, Edge and Firefox download updates on their own, but a downloaded update is applied when the browser is restarted. A browser left open for weeks may be running old code."),
            ("point", "Apps", "Turn on automatic updates in the app store, and remove apps you no longer use. "
             "An app you do not have cannot be attacked."),
            ("h", "Why Restarts Matter"),
            "Some updates download quietly but only take effect after a restart. A computer that has not been "
            "restarted in a month may show that updates were downloaded, while still running the old, flawed "
            "code. That is why the restart button matters as much as the download.",
            "A simple office rule helps: every computer is restarted at the end of the working day "
            "at least once a week. Ten minutes after closing, with no taxpayer waiting, is some of the cheapest security work an office can do.",
            ("h", "An Update Routine for a Small Office"),
            ("point", "Keep a list", "One sheet with every computer, phone, printer and router: who uses it, "
             "what system it runs, and when it was last updated. You cannot update what you have forgotten "
             "you own."),
            ("point", "Turn on automatic updates", "Automatic updates do not depend on anyone remembering. "
             "Schedule the installation for after office hours where the system allows it."),
            ("point", "Test the critical ones first", "For the computer that runs a collection or accounting "
             "system, update one machine first and confirm the system still works before updating the rest. "
             "Ask the system’s supplier which updates they have tested."),
            ("point", "Mark the end dates", "Note when each device stops receiving security updates, and put "
             "its replacement in the next budget."),
            ("point", "Name an owner", "One person checks the list each month. Without an owner, the list "
             "becomes another file nobody opens."),
            ("h", "Updates Without Fear"),
            "People postpone updates for real reasons. They worry that something will break, that the printer "
            "will stop working, or that the computer will restart in the middle of a transaction. These fears "
            "are fair, and the answer is planning, not avoidance.",
            "Make a backup before major updates, as Part 5 described. Install them when the office is closed. "
            "Keep the supplier’s support number at hand for the critical systems. If an update does cause a "
            "problem, the supplier or the maker’s support pages can help undo or fix it. A ransomware attack "
            "through an old flaw can stop an office for much longer.",
            "One more caution: install updates only from the device itself, the official app store or the "
            "maker’s website. A pop-up on a web page that says your computer needs an urgent update is a "
            "trick for getting people to install malware, the kind of lure Part 3 described.",
            ("h", "Stay-Safe Reminders"),
            ("point", "Updates close known doors", "Once a fix is public, attackers study it and target "
             "devices that have not installed it."),
            ("point", "WannaCry’s fix was two months old", "The damage came from updates not installed, not "
             "from an unknown flaw."),
            ("point", "End of support is a deadline", "A device with no security updates belongs in the "
             "replacement plan."),
            ("point", "Restart to finish", "Downloaded is not installed until the device restarts."),
            ("h", "Your Part 11 Action Plan"),
            ("point", "Check three devices", "Your phone, your work computer and your browser. Install what "
             "is waiting and restart."),
            ("point", "Start the list", "Write down every device in your home or office and the system it "
             "runs."),
            ("point", "Find the oldest", "Look up whether it still receives security updates. If it does "
             "not, decide this week how it will be replaced or kept offline."),
            "Then press Restart on that computer in the corner, after closing time. It is one of the simplest security fixes in this whole series.",
            ("cta", "Read: Cybersecurity Series, Part 5: Inside a Ransomware Attack", "/blog/cybersecurity-part-5-ransomware/"),
            ("cta", "Read: Cybersecurity Series, Part 4: Securing Your Home and Remote Network", "/blog/cybersecurity-part-4-home-network/"),
            ("cta", "Read: Cybersecurity Series, Part 10: AI, Quantum Computers and the Next Wave", "/blog/cybersecurity-part-10-future-threats/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "Which device in your home or office has gone the longest without an update?"),
        ],
    },
    {
        "date": "June 30, 2027",
        "title": "Cybersecurity Series, Part 10: AI, Quantum Computers and the Next Wave of Threats",
        "slug": "cybersecurity-part-10-future-threats",
        "category": "security",
        "summary": "How artificial intelligence helps both scammers and defenders, why quantum computers are already "
                   "changing the way the internet is locked, what billions of smart gadgets mean for your home, and the "
                   "habits that will still protect you ten years from now.",
        "publish_on": "2027-06-30 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "body": [
            "Every few years, a new technology arrives with two promises at once. It will make "
            "life easier, and it will make crime easier too. Email gave us faster letters and "
            "phishing. Online banking gave us convenience and account takeovers. Mobile wallets "
            "let a vendor in the public market accept payment with a phone, and they also gave "
            "scammers a new way to ask for money.",
            "In this tenth part of the series, we look ahead at three changes already underway: "
            "artificial intelligence, quantum computing and the flood of smart devices in our "
            "homes and offices. None of them is a reason to panic. Each one is a reason to "
            "understand a little more, so that you can enjoy the benefits without becoming the "
            "easy target. By the end of this post, you will know how each change affects you and "
            "the habits that will still protect you years from now.",
            ("h", "Artificial Intelligence in the Hands of Scammers"),
            "Not long ago, the easiest way to spot a scam email was its language. The grammar was"
            " clumsy, the greeting was strange and the tone did not match the supposed sender. "
            "Generative AI tools have removed much of that warning sign. A scammer who barely "
            "speaks English can now produce a polished, polite message in English, Filipino or "
            "any other language in seconds, and tailor it to your job or your local government using details "
            "from your public posts.",
            "Voices and faces can be copied too. With a short recording taken from a video "
            "online, tools can produce speech that sounds like a particular person. We saw in "
            "Part 3 how an employee in Hong Kong was tricked into sending about HK$200 million "
            "after a video call with what appeared to be senior colleagues, all of them fakes. "
            "The same trick works at a smaller scale: a voice message that sounds like your "
            "child, your boss or your mayor, asking for an urgent transfer or a load of e-wallet "
            "credits.",
            "The defense is not a better eye for fakes. The fakes will keep improving, and trying"
            " to judge them by how real they look is a contest we will lose. The defense is a "
            "habit: when a message asks for money, passwords or one-time PINs, verify it through "
            "a channel you already trust. Call back on the number you have saved, not the number "
            "in the message. Some families agree on a private code word for emergencies, "
            "something an impostor would not know. It sounds old-fashioned, and that is exactly "
            "why it works.",
            ("quote", "When anything can be faked, verification becomes a daily habit, not a special event."),
            ("h", "When the AI Itself Is the Target"),
            "AI tools are now built into email, office software, search engines and customer "
            "service. That makes the tools themselves a target. The OWASP Foundation, which we "
            "met in Part 7, publishes a separate list of the top risks for applications built on "
            "large language models. Its 2025 edition places prompt injection first, followed by "
            "sensitive information disclosure. In plain words, these are two of the biggest "
            "worries:",
            ("point",
             "Hidden instructions",
             "An AI assistant reads a web page, a document or an email that contains instructions"
             " written for the AI, not for you. If the assistant obeys, it might reveal "
             "information or take an action you never asked for. This is called prompt injection."),
            ("point",
             "Leaked information",
             "Whatever you paste into an AI tool may be stored, reviewed or used according to "
             "that service's terms. Pasting a list of taxpayers, a payroll file or a confidential"
             " memo into a public chatbot can be a data leak, even if nobody meant harm."),
            ("point",
             "Too much power",
             "An assistant connected to your email, files and accounts can do a lot of good, and "
             "a lot of damage if it is tricked. The more an AI tool is allowed to do on its own, "
             "the more carefully its permissions should be limited."),
            "For ordinary users, the practical rules are simple. Do not paste personal or "
            "confidential data into an AI tool unless your office has approved that tool for that"
            " kind of data. Read what an AI assistant is about to send or delete before you "
            "confirm it. And treat its answers the way you would treat advice from a confident "
            "stranger: useful, but worth checking, especially on law, health and money.",
            ("h", "AI on the Defenders' Side"),
            "The same technology also works for the good side. Email providers use machine "
            "learning to filter billions of spam and phishing messages. Banks use it to notice a "
            "transaction that does not fit your usual pattern and pause it for a check. Security "
            "teams use it to sort through mountains of logs and find the one login that looks "
            "wrong. The contest between attackers and defenders is not new. AI simply speeds up "
            "both sides, which makes the basic controls from earlier parts, such as multi-factor "
            "authentication, updates and backups, even more important.",
            ("h", "Quantum Computers and the Locks of the Internet"),
            "Every time you see the padlock in your browser, your connection is protected by "
            "mathematics. Some of that mathematics relies on problems that ordinary computers "
            "would need an impossibly long time to solve. A large and reliable quantum computer, "
            "which works on very different principles, could solve some of those problems much "
            "faster. That would weaken several of the methods that protect online banking, "
            "government websites and digital signatures today.",
            "Such a machine does not exist yet, and experts disagree on when it might. So why "
            "worry now? Because of a strategy often called \"harvest now, decrypt later.\" An "
            "attacker can record encrypted data today and store it, hoping to unlock it years "
            "from now. For records that must stay confidential for decades, such as land records,"
            " tax files, health information or state secrets, it matters a great deal.",
            "The good news is that the work to replace these locks is well underway. On August "
            "13, 2024, the United States National Institute of Standards and Technology (NIST) "
            "published its first three post-quantum cryptography standards, known as FIPS 203, "
            "FIPS 204 and FIPS 205. They describe new methods for exchanging keys and making "
            "digital signatures that are designed to resist quantum attacks. In March 2025, NIST "
            "chose another method, called HQC, as a backup, and more standards are in progress. "
            "Major web browsers, including Google Chrome, have already begun using a post-quantum"
            " key exchange on many secure connections, mostly without users noticing.",
            "For individuals, the action is almost boring: keep your browser, phone and computer "
            "updated, because that is how the new locks reach you. For organizations, the work is"
            " bigger. They need to know where they use encryption, which systems are too old to "
            "be updated, and which records must stay secret the longest, so that those are moved "
            "to the new methods first.",
            ("h", "Billions of Small Computers in Our Homes"),
            "A smart TV, a Wi-Fi camera, a voice speaker, a smart plug and even some rice cookers"
            " and air conditioners are all small computers connected to the internet. They are "
            "convenient and often cheap, and some never receive a security update.",
            "The danger was made clear in October 2016. A piece of malware called Mirai had "
            "spread to a huge number of internet cameras and video recorders, mostly by trying "
            "factory-default usernames and passwords. On October 21, that army of hijacked "
            "gadgets flooded Dyn, a company that helps direct internet traffic, and many popular "
            "websites, including Twitter, Netflix and Reddit, became unreachable for parts of the"
            " day. The owners of those cameras had no idea their devices were taking part.",
            "Smart devices can also be a privacy risk in their own right. A camera that faces the"
            " inside of your home, a speaker that listens for a wake word, or a baby monitor with"
            " a weak password can expose the most private parts of family life. Before buying a "
            "smart device, ask a few questions:",
            ("point",
             "Does the maker provide updates?",
             "Choose brands that publish security updates and say how long they will support the product."),
            ("point",
             "Can I change the default password?",
             "If a device has a fixed password you cannot change, do not connect it to the internet."),
            ("point",
             "Does it need to be online at all?",
             "Turn off remote access and cloud features you do not use. A camera that only "
             "records to a memory card is harder to reach from outside."),
            ("point",
             "Where does it sit on my network?",
             "Put smart gadgets on your guest network, as we described in Part 4, so that a "
             "hacked TV cannot reach your work laptop."),
            ("h", "What Will Not Change"),
            "It is easy to feel that security is a race we can never win. But look back at the "
            "attacks in this series. Old or new, the threats in this series lean on a handful of "
            "weaknesses: a stolen or guessed password, a person rushed into acting, a missing "
            "update, a setting left open, or data with no backup. The tools change. The weak "
            "points stay remarkably familiar.",
            "That means the habits you have built so far in this series will keep paying off. A"
            " passkey or an authenticator app defeats much of what AI-written phishing can do. A "
            "habit of verifying requests defeats the cloned voice. Automatic updates bring you "
            "the new post-quantum locks. A guest network contains the hacked gadget. An offline "
            "backup turns ransomware into a bad day instead of a catastrophe.",
            ("h", "Looking Back So Far"),
            "So far, we have walked from the basics to the frontier. We learned how"
            " attacks unfold, then protected our accounts with strong passwords, passkeys and "
            "multi-factor authentication. We studied how scammers play on emotion, secured the "
            "home router and survived a ransomware scenario. We tidied up our cloud accounts, "
            "looked at how apps get hacked, met the idea of zero trust and wrote a plan for when "
            "things go wrong. Today we looked ahead.",
            "If you followed the action plans, your digital life is already far safer than "
            "before. If you skipped a few, that is fine. Pick one part, do its action plan this "
            "week, and come back to the others when you can.",
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Verify, do not judge by looks",
             "AI makes fakes convincing, so confirm requests through a channel you already trust."),
            ("point",
             "Guard what you paste",
             "Keep personal or confidential data out of AI tools your office has not approved."),
            ("point",
             "Updates bring the new locks",
             "Post-quantum protection reaches you through ordinary browser and phone updates."),
            ("point",
             "Smart gadgets need care",
             "Change default passwords, update them, and keep them on the guest network."),
            ("h", "Your Part 10 Action Plan"),
            ("point",
             "Agree on a family or office code word",
             "Choose a word or question that only your circle knows, to use whenever a voice or "
             "video call asks for money urgently."),
            ("point",
             "Set an AI rule for yourself",
             "Decide which information you will never paste into an AI tool, such as IDs, client "
             "lists and anything marked confidential, and follow your office policy."),
            ("point",
             "Audit one smart device",
             "Change its default password, update its software, turn off features you do not use "
             "and move it to your guest network."),
            "Share this series with one person who would benefit, "
            "especially someone who handles money, records or the accounts of an elderly parent.",
            ("cta", "Read: Cybersecurity Series, Part 1: How Modern Cyberattacks Really Work", "/blog/cybersecurity-part-1-how-cyberattacks-work/"),
            ("cta",
             "Read: Cybersecurity Series, Part 9: Incident Response",
             "/blog/cybersecurity-part-9-incident-response/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "Which part of this series helped you most? I would love to hear from you."),
        ],
    },
    {
        "date": "June 21, 2027",
        "title": "Cybersecurity Series, Part 9: Incident Response, or What to Do When Something Goes Wrong",
        "slug": "cybersecurity-part-9-incident-response",
        "category": "security",
        "summary": "What to do in the first hour after a hacked account, a lost phone, a scam transfer or an office "
                   "breach, how to keep evidence intact, where to report in the Philippines, and how to write a "
                   "one-page response plan before you need it.",
        "publish_on": "2027-06-21 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "body": [
            "Offices hold fire drills. People know where the exits are, who carries the logbook "
            "and where to gather outside. But how many offices, or families, have ever practiced "
            "what to do when a computer is hacked, an account is taken over or money is sent to a"
            " scammer? When it happens, people improvise, and under stress, improvising can make "
            "things worse.",
            "Part 9 of this series is about incident response: the calm, ordered steps that limit"
            " the damage when something goes wrong. You do not need to be a technical expert to "
            "follow them. You need a plan that is written down before the bad day arrives. When you finish reading, you will know what to do in the first hour of common emergencies,"
            " how to keep evidence intact, where to report in the Philippines, and how to write a"
            " one-page plan.",
            ("h", "What Counts as an Incident?"),
            "A security incident is any event that threatens the confidentiality, integrity or "
            "availability of information or systems. Put more simply: someone saw what they "
            "should not see, changed what they should not change, or stopped you from using what "
            "you need. Examples include:",
            ("point",
             "For individuals",
             "A hacked email or social media account, a lost or stolen phone, a transfer to a "
             "scammer, or a strange login alert you did not cause."),
            ("point",
             "For offices",
             "Malware on a work computer, a ransomware note, a misdirected email containing "
             "personal data, a lost laptop or flash drive, or a staff account used from an "
             "unknown place."),
            "Not every alert is an incident. A login warning might be you on a new phone. But "
            "every alert deserves a quick check, because the cost of ignoring a real one is far "
            "higher than the cost of checking a false one.",
            ("h", "How the Professionals Think About It"),
            "The United States National Institute of Standards and Technology (NIST) publishes a "
            "guide on this subject, Special Publication 800-61. Its third revision, released in "
            "April 2025, links incident response to the six functions of the NIST Cybersecurity "
            "Framework 2.0: Govern, Identify, Protect, Detect, Respond and Recover. The message "
            "is that response does not start when the alarm rings. It starts with preparation and"
            " ends with lessons that make the next incident less likely.",
            "For everyday use, I find it easier to think in six plain steps:",
            ("point",
             "Prepare",
             "Know your important accounts and systems, keep backups, and write down who to call."),
            ("point", "Notice", "Pay attention to warnings, odd behavior and reports from others."),
            ("point", "Contain", "Stop the damage from spreading: disconnect, lock, freeze."),
            ("point",
             "Clean up",
             "Remove the attacker's access, such as changed passwords, removed malware and closed doors."),
            ("point",
             "Recover",
             "Restore services and data from trusted sources, then watch closely for a while."),
            ("point", "Learn", "Ask what happened and what would have stopped it, then fix that."),
            ("h", "The First Hour: Personal Emergencies"),
            "Here is what to do in the first hour for these situations.",
            ("point",
             "Your email or social media account was taken over",
             "Use the service's official recovery page to regain access. Change the password to a"
             " new, unique one, sign out all other sessions and turn on multi-factor "
             "authentication. Check recovery email, phone numbers and forwarding rules, because "
             "attackers can change these to come back later. Warn your contacts not to act on "
             "messages sent while you were locked out."),
            ("point",
             "Your phone was lost or stolen",
             "Use Find My on iPhone or Find My Device on Android to lock or erase it. Call your "
             "mobile network to block the SIM so that one-time PINs cannot be received. Contact "
             "your bank and e-wallet providers to secure your accounts from another device."),
            ("point",
             "You sent money to a scammer",
             "Call your bank or e-wallet provider immediately through its official hotline or "
             "app, and ask them to flag and hold the transaction. Speed matters. The "
             "Anti-Financial Account Scamming Act (Republic Act No. 12010) allows financial "
             "institutions to temporarily hold funds involved in a suspected scam while it is "
             "checked. Then report it to the authorities."),
            ("point",
             "You clicked a bad link or opened a bad file",
             "Disconnect from the internet, run a full security scan, and change the passwords of"
             " any account you typed in after clicking, using a different, clean device."),
            ("h", "The First Hour: Office Incidents"),
            "In an office, the most important rule is to report quickly and avoid the urge to "
            "clean up quietly. Staff sometimes hide a mistake out of embarrassment, and every "
            "hour of silence gives an attacker more time. A healthy office treats an honest early"
            " report as a good deed, not a confession.",
            ("point",
             "Isolate, do not destroy",
             "Unplug the network cable or turn off Wi-Fi on the affected computer. If possible, "
             "leave it switched on, because evidence in its memory disappears when it is turned "
             "off."),
            ("point",
             "Call the right people",
             "Tell your IT team or provider and your supervisor at once. If personal data may be "
             "involved, alert your Data Protection Officer."),
            ("point",
             "Write things down",
             "Note the time, what you saw, what you clicked and who you told. Photograph error "
             "messages or ransom notes with a phone."),
            ("point",
             "Do not contact the attacker",
             "Do not reply to ransom notes or extortion messages on your own."),
            ("h", "A Little About Digital Forensics"),
            "Digital forensics is the careful collection and study of electronic evidence. It "
            "answers questions such as how the attacker got in, what they touched and whether "
            "data left the building. You do not have to be an investigator, but you can avoid "
            "destroying the clues that investigators need.",
            "Think of a crime scene. Moving things around, wiping surfaces or throwing away items"
            " makes the investigation harder. The same is true for computers. Reinstalling the "
            "operating system, deleting suspicious files or clearing browser history may feel "
            "like fixing the problem, but it can erase the evidence of how it happened. "
            "Professionals copy the data first, record a digital fingerprint of each copy, called"
            " a hash, to prove nothing was changed, and keep a record of who handled the evidence"
            " and when. This record is known as the chain of custody, and it matters if the case "
            "reaches a court.",
            "Two simple habits make any investigation easier: keep the clocks of your computers "
            "and devices set to the correct time automatically, and make sure important systems "
            "keep logs of logins and changes. Without accurate times and logs, reconstructing "
            "what happened is like auditing a cashbook with missing pages.",
            ("quote", "The worst time to look for the fire exit is when the room is already full of smoke."),
            ("h", "Where to Report in the Philippines"),
            "Reporting helps you, and it helps authorities connect cases and warn others. These "
            "are the main channels:",
            ("point",
             "Cybercrime Investigation and Coordinating Center (CICC)",
             "Call the Inter-Agency Response Center hotline 1326 for scams and other cybercrimes."),
            ("point",
             "PNP Anti-Cybercrime Group and NBI Cybercrime Division",
             "Both investigate cybercrimes and accept complaints from the public."),
            ("point",
             "Your bank or e-wallet provider",
             "Report fraud on your account through official channels only, never through links in a message."),
            ("point",
             "The National Privacy Commission (NPC)",
             "Organizations that handle personal data have specific duties. Under the NPC's "
             "breach rules, a personal information controller must notify the Commission within "
             "72 hours of learning of a breach that requires notification, such as one involving "
             "sensitive personal information that could lead to identity fraud, and must also "
             "inform the affected people."),
            ("h", "Talking About It Honestly"),
            "How an organization communicates after an incident shapes how much trust it keeps. A"
            " good notice explains what happened in plain language, what information was "
            "involved, what the organization is doing about it, and what affected people should "
            "do to protect themselves. It gives a contact person and promises updates, then keeps"
            " that promise.",
            ("h", "Learning Without Blame"),
            "After the incident is closed, hold a short review. The goal is not to find someone "
            "to punish. It is to find the weak point that let the incident happen and fix it. Ask"
            " four questions: What happened? Why did it work? What helped us respond? What would "
            "we change? Then assign each improvement to a person with a date, just as you would "
            "follow up on audit findings.",
            "A useful way to practice is a tabletop exercise. Gather the key people for an hour, "
            "describe a made-up scenario, such as \"the collection system shows a ransom note at 8"
            " am on a Monday,\" and walk through what each person would do. The gaps appear "
            "quickly: nobody knows the IT provider's after-hours number, or the backups are kept "
            "on the same network. Finding those gaps in a meeting room is much cheaper than "
            "finding them during a real attack.",
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Plan before the bad day",
             "A one-page plan with phone numbers beats improvising under stress."),
            ("point", "Contain first, clean later", "Disconnect and lock, but do not wipe the evidence."),
            ("point", "Report early and honestly", "Every hour of silence gives an attacker more time."),
            ("point",
             "Learn without blame",
             "Find the weak point, then assign the fix to a person with a date."),
            ("h", "Your Part 9 Action Plan"),
            ("point",
             "Write a one-page plan",
             "List your important accounts or systems, where the backups are, and who to call, "
             "with phone numbers for your bank, mobile network, IT support and the CICC hotline "
             "1326."),
            ("point",
             "Store it where you can reach it",
             "Keep a printed copy, because a hacked computer or a lost phone may be exactly what "
             "you cannot use."),
            ("point",
             "Run a 30-minute drill",
             "Pick one scenario from this post and talk through it with your family or team. Fix "
             "the first gap you find."),
            ("cta",
             "Read Part 10: AI, Quantum and What Comes Next",
             "/blog/cybersecurity-part-10-future-threats/"),
            ("cta",
             "Read: Cybersecurity Series, Part 8: Zero Trust",
             "/blog/cybersecurity-part-8-zero-trust/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "Has your office ever run a cybersecurity drill? Tell me what surprised you most."),
        ],
    },
    {
        "date": "June 11, 2027",
        "title": "Cybersecurity Series, Part 8: Zero Trust, or Why Every Door Gets Checked",
        "slug": "cybersecurity-part-8-zero-trust",
        "category": "security",
        "summary": "Why the old idea of a safe inside network no longer works, what zero trust really means in "
                   "plain language, how it echoes the internal controls of a well-run treasury, and simple ways to "
                   "apply it at home and in a small office.",
        "publish_on": "2027-06-11 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "body": [
            "For a long time, computer security was built like an old fortress. There was a "
            "strong wall around the office network, with firewalls at the gate. Anyone outside "
            "was suspicious. Anyone inside, connected to the office network, was trusted. If you "
            "were at your desk, you could reach almost every shared folder and system in the "
            "building.",
            "That model has two problems. First, the wall has too many openings now. People work "
            "from home, use phones, log in to cloud services and connect from coffee shops. "
            "Second, and more serious, once an attacker gets inside the wall, through one phished"
            " password or one infected laptop, the fortress model lets them walk freely from room"
            " to room. Ransomware, which we discussed in Part 5, can spread exactly this way.",
            "Part 8 of this series is about the answer that security experts have worked toward "
            "for more than a decade: zero trust. After this post, you will know what it "
            "really means, why it echoes the internal controls of a well-run treasury, and "
            "low-cost steps a small office can take this month.",
            ("h", "What Zero Trust Means"),
            "Zero trust is often summed up as \"never trust, always verify.\" It does not mean "
            "distrusting your colleagues or your family. It means that a system should not grant "
            "access just because a request comes from a familiar place. Every request to use "
            "something important, whether it comes from inside the office or outside, should be "
            "checked: who is asking, from what device, for what, and does it make sense right "
            "now?",
            "The term was popularized around 2010 by John Kindervag, then an analyst at the "
            "research firm Forrester. Google described its own version, called BeyondCorp, in "
            "2014, after moving its employees away from relying on the internal network for "
            "trust. In August 2020, NIST published Special Publication 800-207, Zero Trust "
            "Architecture. In 2021, a United States executive order directed federal agencies to "
            "move toward zero trust, and the idea has since spread to governments and companies "
            "around the world.",
            ("h", "The Core Ideas in Plain Words"),
            "NIST lists seven tenets of zero trust. Stripped of technical terms, they come down "
            "to a few ideas that anyone can understand:",
            ("point",
             "Location is not proof",
             "Being on the office Wi-Fi or inside the building does not make a request safe. "
             "Every connection is treated as if it could be hostile, and data is protected "
             "wherever it travels."),
            ("point",
             "Check every time it matters",
             "Access is granted for one session or task, not forever. When you return tomorrow, "
             "or ask for something more sensitive, you are checked again."),
            ("point",
             "Give the least access needed",
             "A person or program gets only what it needs to do its job, for as long as it needs "
             "it. A clerk who encodes payments does not need to approve them."),
            ("point",
             "Look at the whole picture",
             "The decision considers who you are, the health of your device, the time, the place "
             "and whether the request fits your normal pattern."),
            ("point",
             "Assume a breach is possible",
             "Design systems so that if one account or computer is compromised, the damage stays "
             "small and is noticed quickly."),
            ("point",
             "Watch and improve",
             "Collect information about devices, logins and traffic, and use it to catch problems"
             " and tighten the rules over time."),
            ("h", "Treasury Work Already Knows This Idea"),
            "When I first studied zero trust, it felt familiar. Good public financial management "
            "has followed a similar philosophy for a long time, under the name of internal "
            "control.",
            "Consider how a well-run treasury handles money. The person who collects payments is "
            "not the same person who records them in the books, and neither is the person who "
            "approves disbursements. This is segregation of duties. The vault does not open just "
            "because someone works in the building. Access is limited to specific people, often "
            "requires two of them together, and every opening is logged. Cash counts happen "
            "regularly and sometimes without warning. Nobody takes these controls as an insult. "
            "They protect honest employees as much as they protect public funds.",
            "Zero trust applies the same discipline to digital systems. It replaces \"she works "
            "here, so she can see everything\" with \"she can see what her job requires, and the "
            "system confirms it is really her.\"",
            ("quote",
             "Trust is not a feeling we give to a network. It is a decision the system makes "
             "again every time it matters."),
            ("h", "What It Looks Like in Practice"),
            "Large organizations build zero trust with identity platforms, device management and "
            "careful network design. The United States Cybersecurity and Infrastructure Security "
            "Agency (CISA) describes the work in five areas, which it calls pillars: identity, "
            "devices, networks, applications and workloads, and data. Translated into everyday "
            "terms, it often looks like this:",
            ("point",
             "Identity",
             "Every person has their own account, protected by multi-factor authentication, "
             "ideally a phishing-resistant method such as a passkey or security key. No shared "
             "logins."),
            ("point",
             "Devices",
             "Only devices that are updated, protected and known to the organization can reach "
             "sensitive systems."),
            ("point",
             "Networks",
             "The network is divided into smaller zones, so that a problem in one area cannot "
             "easily spread to another."),
            ("point",
             "Applications",
             "Each application checks permissions on its own, every time, instead of trusting "
             "anyone who reaches it."),
            ("point",
             "Data",
             "Sensitive files are labeled, encrypted and shared only with the people who need "
             "them, with a record of who opened what."),
            ("h", "Zero Trust for a Small Office"),
            "You do not need a big budget to start. Many of the most valuable steps cost little or nothing:",
            ("point",
             "One person, one account",
             "Stop sharing a single login for the office computer, the email or a government "
             "portal. Individual accounts make actions traceable and access easy to remove."),
            ("point",
             "MFA everywhere",
             "Turn on multi-factor authentication for email, cloud storage, banking and every "
             "system that holds money or personal data."),
            ("point",
             "Separate daily and admin accounts",
             "Do everyday work with an ordinary account. Use an administrator account only when "
             "installing or changing something."),
            ("point",
             "Review access when people move",
             "When an employee transfers, retires or resigns, remove or change their access on "
             "the same day. Old accounts are favorite doors for attackers."),
            ("point",
             "Separate the networks",
             "Keep guests, personal phones and smart devices off the network that holds your "
             "financial and records systems."),
            ("point",
             "Approve money in two steps",
             "Any change in payment details or any unusual transfer should require confirmation "
             "by a second person through a separate channel."),
            ("h", "Zero Trust at Home"),
            "Families can borrow the same thinking. Give each family member their own user "
            "account on shared computers, so a child's game download cannot touch a parent's work"
            " files. Use the guest network from Part 4 for visitors and smart gadgets. Check "
            "which apps can see your location, contacts and photos, and remove access that is not"
            " needed. And treat every unexpected request for money or codes the same way, even "
            "when it seems to come from someone you love: verify it through a channel you already"
            " trust.",
            ("h", "Common Myths"),
            ("point",
             "\"Zero trust is a product you can buy\"",
             "Vendors sell tools that help, but zero trust is an approach. No single box or app "
             "makes an organization zero trust."),
            ("point",
             "\"It means we do not trust our people\"",
             "It means systems stop assuming. Clear rules and checks actually protect staff from "
             "being blamed for an attacker's actions."),
            ("point",
             "\"It is all or nothing\"",
             "It is a journey. A sensible first step is identity and multi-factor authentication,"
             " then improve step by step."),
            ("point",
             "\"It makes work slower\"",
             "Done well, it can make work smoother. Signing in once with a passkey on a trusted "
             "device is faster than juggling many passwords and a VPN."),
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Location is not proof",
             "Being inside the office network does not make a request safe."),
            ("point",
             "Least access, checked often",
             "Give people only what their job needs, and check again when it matters."),
            ("point",
             "Treasury controls already do this",
             "Segregation of duties and a logged vault are zero trust on paper."),
            ("point", "Start with identity", "One person, one account, with multi-factor authentication."),
            ("h", "Your Part 8 Action Plan"),
            ("point",
             "Count your shared logins",
             "List every account that more than one person uses. Plan to replace each one with "
             "individual accounts."),
            ("point",
             "Do an access review",
             "For your email, cloud folders or office systems, check who has access. Remove "
             "anyone who no longer needs it."),
            ("point",
             "Add a second check for money",
             "Agree with your family or team that changes to bank details or urgent transfers "
             "always need a call-back on a known number."),
            ("cta", "Read Part 9: Incident Response", "/blog/cybersecurity-part-9-incident-response/"),
            ("cta",
             "Read: Cybersecurity Series, Part 7: Why Apps Get Hacked",
             "/blog/cybersecurity-part-7-why-apps-get-hacked/"),
            ("cta",
             "Read: ALTOS Principle 6, Separate the Hands",
             "/blog/altos-framework-separate-the-hands/"),
            ("ask",
             "Does your office still use a shared login for any important system? What makes it "
             "hard to change? I would like to know."),
        ],
    },
    {
        "date": "June 2, 2027",
        "title": "Cybersecurity Series, Part 7: Why Apps Get Hacked, Explained with the OWASP Top 10",
        "slug": "cybersecurity-part-7-why-apps-get-hacked",
        "category": "security",
        "summary": "A plain-language tour of the ten most serious risks in web applications, as listed in the OWASP "
                   "Top 10:2025, with everyday examples, questions to ask before your office buys a system, and "
                   "habits for anyone who builds software.",
        "publish_on": "2027-06-02 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "body": [
            "Every app you use was written by people. Your bank's mobile app, the online payment "
            "page of your local government, the school portal and the delivery app all started as"
            " lines of code typed by developers working under deadlines. People make mistakes, "
            "and some of those mistakes become doors that attackers can open.",
            "You do not need to be a programmer to understand where those doors usually are. In "
            "Part 7 of this series, we take a guided tour of the most common weaknesses in web "
            "applications. If you use apps, this will help you understand the news. If your "
            "office buys or runs a system, it will help you ask better questions. And if you "
            "build software, as I do for treasury work, it is a checklist worth keeping close. Read to the end and you will know the ten most serious app risks in plain words, "
            "six questions to ask before your office buys a system, and habits that keep your own"
            " apps safer.",
            ("h", "What Is OWASP?"),
            "The OWASP Foundation, whose name stands for Open Worldwide Application Security "
            "Project, is a nonprofit community that produces free guides and tools for building "
            "safer software. Its best-known work is the OWASP Top 10, an awareness document that "
            "ranks the most critical security risks in web applications. It is updated every few "
            "years based on data from real applications and a survey of practitioners. The "
            "current edition is the OWASP Top 10:2025.",
            "Here are the ten risks, explained with everyday examples.",
            ("h", "1. Broken Access Control"),
            "This is the top risk, and it is about permissions. The app checks who you are, but "
            "forgets to check what you are allowed to see or do. A classic example: you view your"
            " own receipt at an address that ends in a number, such as receipt 1045. You change "
            "it to 1046 and see a stranger's receipt, with their name and address. The system "
            "should have refused. It is like a records room where the clerk checks your ID at the"
            " door, but then lets you open any cabinet inside.",
            ("h", "2. Security Misconfiguration"),
            "The software may be fine, but it was set up badly. Default administrator passwords "
            "are left unchanged, detailed error messages reveal how the system works inside, "
            "unnecessary features are switched on, or a storage folder full of documents is left "
            "open to the internet. A data leak can come not from clever hacking but from a "
            "setting nobody checked.",
            ("h", "3. Software Supply Chain Failures"),
            "Modern apps are built from many ready-made parts, called libraries or packages, "
            "written by other people. That saves time, but every part is a dependency you must "
            "trust. If one of those parts has a flaw, is outdated or is secretly replaced with a "
            "malicious version, every app that uses it is at risk. It is like a treasury buying "
            "accountable forms from a supplier: if the supplier is careless or dishonest, your "
            "controls are weakened before you even begin.",
            ("h", "4. Cryptographic Failures"),
            "This is about protecting data with encryption, or failing to. Examples include a "
            "site that does not use HTTPS, passwords stored in a form that can be read or easily "
            "reversed, or sensitive records saved without encryption. When such a database is "
            "stolen, the attacker can read everything at once.",
            ("h", "5. Injection"),
            "An app takes what you type into a form and passes it to a database or another "
            "program. If it does not handle that input carefully, an attacker can type something "
            "that the program mistakes for a command. The best-known type is SQL injection, where"
            " carefully crafted text in a search box or login form tricks the database into "
            "revealing or changing records. Developers prevent it by keeping data and commands "
            "strictly separate, using what are called parameterized queries.",
            ("h", "6. Insecure Design"),
            "Some weaknesses are not coding mistakes but planning mistakes. Imagine a "
            "password-reset page that lets anyone guess a six-digit code as many times as they "
            "like. Every line of code may work exactly as written, yet the design is unsafe "
            "because nobody asked, \"How would someone abuse this?\" Thinking about abuse early, "
            "sometimes called threat modeling, is far cheaper than fixing a design later.",
            ("h", "7. Authentication Failures"),
            "These are weaknesses in how an app confirms who you are. It might allow very weak "
            "passwords, never lock out repeated guesses, fail to offer multi-factor "
            "authentication, or keep you signed in long after you should have been logged out. "
            "Part 2 of this series explained why strong sign-in matters. This category is the "
            "developer's side of the same story.",
            ("h", "8. Software or Data Integrity Failures"),
            "An app trusts updates, files or data without checking that they are genuine and "
            "unaltered. A program that downloads updates without verifying their digital "
            "signature, for example, could be tricked into installing malware. In financial "
            "terms, it is like accepting a check without verifying the signature.",
            ("h", "9. Security Logging and Alerting Failures"),
            "If an app does not record important events, such as logins, failed attempts and "
            "changes to records, or if nobody is alerted when something suspicious happens, "
            "attacks can continue for weeks unnoticed. An unlogged system is like a vault without"
            " a logbook: when money goes missing, there is no trail to follow.",
            ("h", "10. Mishandling of Exceptional Conditions"),
            "This new category covers what happens when things go wrong: a network error, a "
            "missing value, an unexpected input. A well-built app fails safely. It shows a polite"
            " message, keeps the data consistent and denies access when in doubt. A poorly built "
            "one might crash and show internal details, leave a transaction half done, or, worst "
            "of all, let the user through because the check itself failed.",
            ("quote",
             "The risks on this list are not genius attacks. They are ordinary mistakes that "
             "nobody checked for."),
            ("h", "What App Users Can Do"),
            "You cannot fix an app's code, but you can lower your risk:",
            ("point",
             "Install apps only from official stores",
             "Use Google Play, the App Store or the official website of the bank or agency. Avoid"
             " installing app files sent through chat."),
            ("point", "Keep apps updated", "Updates often fix exactly the kinds of flaws described above."),
            ("point",
             "Give each app the least it needs",
             "A flashlight app does not need your contacts or location."),
            ("point",
             "Report what looks wrong",
             "If an app ever shows you someone else's information, stop, take a screenshot and "
             "report it to the provider through official channels. Do not explore further."),
            "That last point matters. Testing or probing systems you do not own, without "
            "permission, can be illegal under the Cybercrime Prevention Act of 2012 (Republic Act"
            " No. 10175), even if your intentions are good. Report it and let the owner fix it.",
            ("h", "Questions to Ask Before Your Office Buys a System"),
            "Offices that buy software, whether for collections, payroll or records, can use the "
            "OWASP Top 10 as a checklist. Before signing, ask the supplier:",
            ("point",
             "Access control",
             "Can each user be limited to only the functions and records their job needs? Can we "
             "see who did what, and when?"),
            ("point",
             "Sign-in",
             "Does the system support multi-factor authentication? How are passwords stored?"),
            ("point",
             "Updates and components",
             "How often do you release security updates, and how do you keep third-party components current?"),
            ("point",
             "Testing",
             "Has the system been tested for security by an independent party? Can you share a "
             "summary of the results?"),
            ("point",
             "Data protection",
             "Is data encrypted when stored and when sent? Where are the backups, and how fast "
             "can we restore?"),
            ("point",
             "Logging and support",
             "Are important actions logged and kept? Who do we call if we suspect a breach, and "
             "how fast will you respond?"),
            ("h", "For Those Who Build"),
            "If you write code, even small tools for your own office, a few habits help prevent "
            "these problems. Check permissions on the server for every request, not only by "
            "hiding buttons on the screen. Use parameterized queries for every database call. "
            "Store passwords only with a modern password-hashing method designed for the purpose,"
            " such as bcrypt or Argon2. Keep your dependencies updated and remove the ones you do"
            " not use. Log important events, and decide in advance what the system should do when"
            " something fails. Most of all, ask \"How could this be abused?\" before you write the "
            "first line.",
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Permissions are the top risk",
             "An app must check what you may see, not only who you are."),
            ("point",
             "Settings matter as much as code",
             "A default password or an open folder can leak data without any clever hacking."),
            ("point",
             "Ask before you buy",
             "Access control, sign-in, updates, testing, data protection and logging."),
            ("point",
             "Report, do not probe",
             "Testing systems you do not own can be illegal, even with good intentions."),
            ("h", "Your Part 7 Action Plan"),
            ("point",
             "Review your app permissions",
             "On your phone, open the permission settings and remove location, contacts, camera "
             "and microphone access from apps that do not need them."),
            ("point",
             "Delete apps you no longer use",
             "Every unused app is old code that may never be updated again."),
            ("point",
             "Share the checklist",
             "If your office is planning to buy or upgrade a system, pass the six questions above"
             " to the people handling the procurement."),
            ("cta", "Read Part 8: Zero Trust", "/blog/cybersecurity-part-8-zero-trust/"),
            ("cta",
             "Read: Cybersecurity Series, Part 6: Keeping Your Life in the Cloud Safe and Private",
             "/blog/cybersecurity-part-6-cloud-and-privacy/"),
            ("cta",
             "Read: ALTOS Principle 5, Every Record Has a Seal",
             "/blog/altos-framework-every-record-has-a-seal/"),
            ("ask",
             "Has an app ever shown you information that clearly was not yours? How did the "
             "provider respond?"),
        ],
    },
    {
        "date": "May 24, 2027",
        "title": "Cybersecurity Series, Part 6: Keeping Your Life in the Cloud Safe and Private",
        "slug": "cybersecurity-part-6-cloud-and-privacy",
        "category": "security",
        "summary": "Who is responsible for keeping your cloud files safe, why a single \"anyone with the link\" "
                   "setting can expose a whole office, how to check which apps can reach your accounts, and the "
                   "privacy rights every Filipino has under the Data Privacy Act.",
        "publish_on": "2027-05-24 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "body": [
            "Your family photos, your scanned IDs, the spreadsheets from work and years of "
            "messages probably live somewhere you have never seen: in the cloud. There is a "
            "well-known joke among IT people that \"the cloud is just someone else's computer.\" It"
            " is a joke, but it carries a useful truth. When you store something online, you are "
            "trusting a company's computers, and you are also trusting your own settings and "
            "habits.",
            "In Part 6 of this series, we look at how to keep your cloud accounts secure and how "
            "to protect your privacy in a world where so much of our lives is stored, shared and "
            "analyzed online. By the last section, you will know where your responsibility "
            "begins, how to share files safely, and how to remove the apps that still reach your "
            "accounts.",
            ("h", "What \"the Cloud\" Really Means"),
            "When you save a file to Google Drive, OneDrive, iCloud or Dropbox, it is copied to "
            "large data centers owned by those companies. The same is true when you post on "
            "social media, back up your phone or use an online accounting tool. The benefits are "
            "real: your files survive a lost phone, you can work from anywhere and you can share "
            "a document in seconds.",
            "The big providers invest heavily in security. Their data centers have guards, "
            "redundant power, specialist staff and constant monitoring, far beyond what a small "
            "office could afford. So why do cloud accounts get breached at all? The answer lies "
            "in a principle called shared responsibility.",
            ("h", "Shared Responsibility: Their Part and Your Part"),
            "Cloud security is divided between the provider and the customer. The provider is "
            "responsible for the security of the cloud: the buildings, the servers, the networks "
            "and the software that runs the service. You are responsible for security in the "
            "cloud: who can sign in to your account, what you upload, how you share it and which "
            "apps you connect to it.",
            "Think of a bank's safety deposit box. The bank guards the vault, the walls and the "
            "doors. But if you hand a copy of your key to a stranger, or leave the box open while"
            " you step out, the bank's strong vault will not help you.",
            "Your side of that line is yours to protect. The risk there is a weak password, a "
            "missing second factor or a careless sharing setting.",
            ("h", "Cloud Mistakes to Avoid"),
            ("point",
             "A weak account",
             "If your cloud account uses a reused password without multi-factor authentication, "
             "everything in it is one leaked password away from a stranger. Part 2 showed how to "
             "fix this with a password manager and passkeys."),
            ("point",
             "\"Anyone with the link\" sharing",
             "This setting lets anyone who has the link open the file, with no sign-in. Links get"
             " forwarded, pasted into group chats and posted by mistake. A spreadsheet of names, "
             "addresses and ID numbers shared this way is effectively public."),
            ("point",
             "Sharing that never ends",
             "Files shared years ago with former colleagues, old suppliers or a personal email "
             "address stay shared until someone removes the access."),
            ("point",
             "Connected apps you forgot",
             "Quizzes, photo editors, browser add-ons and productivity tools often ask to \"sign "
             "in with Google\" or Facebook and request access to your files or contacts. That "
             "access can remain long after you stop using them."),
            ("point",
             "Thinking sync is a backup",
             "Syncing copies changes everywhere, including deletions and files scrambled by "
             "ransomware. A synced folder is convenient, but it is not a separate backup."),
            ("h", "Share Like a Careful Records Officer"),
            "Good records management never hands out original documents to anyone who asks. "
            "Copies go to the people who have a right to them, each release is logged, and "
            "confidential records stay locked. Sharing files online deserves the same care.",
            ("point",
             "Share with names, not links",
             "Choose \"Restricted\" or its equivalent and add the specific people who need the "
             "file. Use public links only for material you would be comfortable posting on a "
             "bulletin board."),
            ("point",
             "Give the lowest access that works",
             "If someone only needs to read, give view access, not edit. Google Drive, for "
             "example, lets you turn off downloading, printing and copying for viewers."),
            ("point",
             "Set an expiry date",
             "Several services let you make access expire automatically. When I share a document "
             "for review, I give view-only access to the named person and let the access end on "
             "its own after a few days."),
            ("point",
             "Review shared files every few months",
             "Look for files shared with \"anyone with the link\" or with people outside your "
             "office, and remove what is no longer needed."),
            ("h", "Check Which Apps Can Reach Your Accounts"),
            "Over the years, you may have clicked \"Allow\" for many apps. It is worth reviewing "
            "them. In a Google Account, open the Security section and look for \"Your connections "
            "to third-party apps and services.\" There you can see which apps can access your "
            "account and what each one can do. Remove any you do not recognize or no longer use. "
            "Microsoft, Apple and Facebook accounts have similar pages in their security or "
            "privacy settings.",
            "Pay special attention to any app that can read your email or your files. Email "
            "access is a master key, because password reset links arrive there.",
            ("quote", "Every \"Allow\" you click is a key you hand out. Count your keys once in a while."),
            ("h", "Your Phone Knows a Lot About You"),
            "Privacy is not only about files in the cloud. The apps on your phone can collect "
            "your location, contacts, photos and even what you say near the microphone, depending"
            " on the permissions you give them. Much of this data is used to show targeted "
            "advertising, and some may be shared with partners.",
            "On an iPhone, open Settings, then Privacy and Security, to see which apps can use "
            "your location, contacts, photos, camera and microphone. On Android, look for the "
            "Permission manager in the Security and privacy settings; the exact menu differs by "
            "phone brand. Ask a simple question for each app: does it really need this to do its "
            "job? A calculator does not need your location. A messaging app may need your "
            "microphone, but only while you are recording.",
            ("h", "Think Before You Post"),
            "Small details in posts can add up to a full profile for a scammer or stalker:",
            ("point",
             "IDs and documents",
             "Never post photos of your IDs, passports, boarding passes or receipts with barcodes"
             " or QR codes. They contain more information than you might think."),
            ("point",
             "Location and routine",
             "Posting \"on vacation for two weeks\" while you are away tells people your house is "
             "empty. Consider posting travel photos after you return."),
            ("point",
             "Children's details",
             "School uniforms, school names and daily routines can reveal where a child can be "
             "found. Keep those posts to a private circle, or skip them."),
            ("point",
             "Answers to security questions",
             "Your first pet, your mother's maiden name and your first school are common security"
             " questions. Fun quizzes that ask for them deserve suspicion."),
            ("h", "Your Rights Under the Data Privacy Act"),
            "In the Philippines, the Data Privacy Act of 2012 (Republic Act No. 10173) protects "
            "personal information held by government offices and private companies alike. It is "
            "enforced by the National Privacy Commission (NPC). As a data subject, you have "
            "rights, including:",
            ("point",
             "The right to be informed",
             "You should be told when your personal data is being collected and processed, and "
             "for what purpose."),
            ("point",
             "The right to access and correct",
             "You can ask an organization what personal data it holds about you, and ask it to "
             "correct mistakes."),
            ("point",
             "The right to object and to erasure",
             "In certain cases, you can object to processing and ask that your data be blocked or"
             " removed, such as when it is no longer needed or was collected unlawfully."),
            ("point",
             "The right to complain and claim damages",
             "You can file a complaint with the NPC and may be entitled to damages if your data is misused."),
            "These rights also remind those of us who handle other people's data at work of our "
            "duty. Every taxpayer list, payroll file and application form is someone's personal "
            "information, entrusted to us for a specific purpose.",
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Security in the cloud is your part",
             "The provider guards the data center; you guard the sign-in, the sharing and the "
             "connected apps."),
            ("point", "Share with names, not links", "Give the lowest access that works, and let it expire."),
            ("point", "Count your keys", "Review connected apps and phone permissions every few months."),
            ("point",
             "Know your rights",
             "The Data Privacy Act lets you be informed, see and correct your data, object, and complain."),
            ("h", "Your Part 6 Action Plan"),
            ("point",
             "Secure your main cloud account",
             "Make sure it has a unique password and multi-factor authentication, ideally a passkey."),
            ("point",
             "Hunt for public links",
             "Search your cloud storage for files shared with \"anyone with the link\" and switch "
             "them to named people, or stop sharing them."),
            ("point",
             "Remove one forgotten app",
             "Open the third-party connections page of your Google, Microsoft or Facebook account"
             " and remove at least one app you no longer use."),
            ("cta", "Read Part 7: Why Apps Get Hacked", "/blog/cybersecurity-part-7-why-apps-get-hacked/"),
            ("cta",
             "Read: Cybersecurity Series, Part 5: Inside a Ransomware Attack",
             "/blog/cybersecurity-part-5-ransomware/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask",
             "How many forgotten apps did you find connected to your accounts? Tell me the oldest one."),
        ],
    },
    {
        "date": "May 14, 2027",
        "title": "Cybersecurity Series, Part 5: Inside a Ransomware Attack",
        "slug": "cybersecurity-part-5-ransomware",
        "category": "security",
        "summary": "How ransomware gangs break in, steal before they lock, and pressure victims to pay, what the "
                   "PhilHealth attack of 2023 taught the country, and the backup habit that takes away their leverage.",
        "publish_on": "2027-05-14 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "body": [
            "Imagine coming to the office on a Monday and finding every computer showing the same"
            " message: your files are encrypted, your records have been copied, and you have a "
            "few days to pay before everything is published online. Nothing opens. The collection"
            " system is down. The queue at the counter grows, and nobody can issue a receipt.",
            "This is not a scene from a movie. In September 2023, the Philippine Health Insurance"
            " Corporation (PhilHealth) went through a version of it. In Part 5 of this series, we"
            " look inside a modern ransomware attack: how it starts and why it is built to make "
            "you pay. We also look at what ordinary people and offices can do, so that a ransom "
            "note becomes an inconvenience instead of a disaster. Stay with me to the end, and you will know how an attack unfolds, why paying is a bad bet, and how to set up backups "
            "an attacker cannot touch.",
            ("h", "From Locked Screens to a Criminal Industry"),
            "Early ransomware was crude. A virus scrambled the files on one computer and asked "
            "for a few hundred dollars. If you paid, you might get a key. If you had a copy of "
            "your files somewhere else, you could ignore the note and start over.",
            "Criminals learned from that. Today, some ransomware groups run like businesses. One "
            "group writes and maintains the malware, runs the payment sites and even handles "
            "\"customer service\" with victims. Other criminals, called affiliates, rent the "
            "malware, break into targets, and share the ransom with the developers. This model is"
            " known as ransomware-as-a-service. It lowered the skill needed to launch an attack, "
            "and it is one reason ransomware remains one of the most common serious threats. "
            "Verizon's 2025 Data Breach Investigations Report found ransomware in 44% of the "
            "breaches it studied, up from 32% a year earlier.",
            ("h", "Double Extortion: Steal First, Then Lock"),
            "The biggest change came when attackers realized that good backups were ruining their"
            " business. If a victim could restore everything, why pay? So they began to copy the "
            "data out before encrypting it. Now the note carries two threats: pay to unlock your "
            "files, and pay again, or at the same time, to stop us from publishing what we took. "
            "This is called double extortion.",
            "Some groups go further, with what is sometimes called triple extortion. They contact"
            " the victim's clients, patients or partners directly, or flood the victim's website "
            "with traffic to add pressure. The goal is always the same: make paying feel like the"
            " fastest way to make the pain stop.",
            ("h", "How an Attack Unfolds"),
            "A ransomware attack is not always a single click that locks everything a minute "
            "later. It can follow the pattern we mapped in Part 1, over days or weeks.",
            ("point",
             "Getting in",
             "The usual doors are a phishing email, a stolen password for remote access or a VPN,"
             " or an unpatched device facing the internet, such as a firewall or a file-sharing "
             "server."),
            ("point",
             "Settling in",
             "The attacker installs remote-control tools so they can come back at will, sometimes"
             " using software that looks like ordinary IT administration."),
            ("point",
             "Spreading out",
             "They collect more passwords, especially those of administrators, and move from the "
             "first computer to servers, shared drives and backup systems."),
            ("point",
             "Stealing",
             "They quietly copy valuable data to servers they control, sometimes over days, "
             "trying not to cause a spike that someone might notice."),
            ("point",
             "Disabling recovery",
             "They delete or encrypt backups they can reach, turn off security tools and remove "
             "the recovery copies that the operating system keeps."),
            ("point",
             "Striking",
             "Only then do they launch the encryption, sometimes at night, on a weekend or before"
             " a holiday, when fewer people are watching. Thousands of files can be locked within"
             " hours."),
            "Notice that the actual encryption is the last step. Every step before it is a chance"
            " to catch the attacker: an alert on a strange login, a warning about a new "
            "administrator account, or a large upload at midnight.",
            ("h", "A Philippine Lesson: The PhilHealth Attack"),
            "On September 22, 2023, PhilHealth learned that it had been hit by the Medusa "
            "ransomware group. Its website, e-claims system, member portal and collection system "
            "went offline, and the agency's initial investigation found about 72 computers "
            "affected. The attackers reportedly demanded US$300,000 and threatened to release the"
            " stolen data.",
            "The government did not pay, in line with its policy. The attackers then published "
            "the data online. PhilHealth later estimated that the personal information of about "
            "13 million to 20 million members may have been exposed, and the National Privacy "
            "Commission looked into the agency's compliance with the Data Privacy Act.",
            "I do not cite this case to blame anyone. I cite it because it shows two hard truths."
            " First, refusing to pay is the right policy, but it does not undo a data leak; once "
            "the files are copied, the damage is partly done. Second, the real cost of ransomware"
            " is not only the ransom. It is the days of downtime, the citizens who cannot "
            "transact, the overtime, the investigation and the long work of rebuilding trust.",
            ("quote",
             "Refusing to pay is the right decision. Being able to refuse without fear is the real goal."),
            ("h", "Why Paying Is a Bad Bet"),
            "When the screens go dark, paying can look like the quickest way out. Law enforcement"
            " agencies, including the United States FBI, advise against it, and for good reasons.",
            ("point",
             "There is no guarantee",
             "The key may not work well. Decrypting large systems can be slow, and some files may"
             " come back damaged."),
            ("point",
             "Stolen data stays stolen",
             "Paying for silence relies on the promise of criminals. Data that has been copied "
             "can be sold or leaked later anyway."),
            ("point",
             "You become a known payer",
             "An organization that pays has shown it will pay. It may be targeted again, "
             "sometimes by the same group."),
            ("point",
             "You fund the next attack",
             "Every ransom pays for more tools, more affiliates and more victims."),
            "The encouraging news is that more victims are refusing. Verizon's 2025 report found "
            "that 64% of ransomware victims did not pay, up from 50% two years before, and that "
            "the median payment had fallen to US$115,000. Refusing is easier when you know you "
            "can recover.",
            ("h", "The Cure: Backups the Attacker Cannot Touch"),
            "Ransomware turns your own data into a hostage. A good backup takes the hostage away."
            " But it must be a backup the attacker cannot reach, because modern attackers look "
            "for backups first. A practical rule to follow is often written as 3-2-1-1-0.",
            ("point",
             "3 copies",
             "Keep at least three copies of important data: the original and two backups."),
            ("point",
             "2 kinds of storage",
             "Store them on at least two different kinds of media, such as your computer's drive "
             "and an external drive."),
            ("point",
             "1 off-site",
             "Keep one copy in another place, such as a trusted cloud service or a drive kept at "
             "another building."),
            ("point",
             "1 offline or unchangeable",
             "Keep one copy that ransomware cannot alter: a drive that is unplugged after each "
             "backup, or storage set to keep each version unchanged for a fixed period."),
            ("point",
             "0 surprises",
             "Test your backups by actually restoring files. A backup you have never restored is "
             "only a hope."),
            "For a household, this can be simple: your laptop, an external drive that you plug in"
            " every Sunday and then unplug, and a cloud backup of your most important folders. "
            "For an office, it means scheduled backups, at least one copy that is offline or "
            "locked against changes, and a written plan for how long a restore takes.",
            "There is a familiar idea from treasury work here. We never keep all the cash in one "
            "drawer, and we do not treat a collection as safe until it is counted, recorded and "
            "deposited. Data deserves the same discipline. A file that exists in only one place "
            "is not really safe.",
            ("h", "Making the Attack Harder"),
            "Backups help you recover. These habits help you avoid the attack or catch it early:",
            ("point",
             "Patch internet-facing devices first",
             "Firewalls, VPNs and remote access tools are favorite doors. Apply their security "
             "updates as soon as you can."),
            ("point",
             "Protect remote access with MFA",
             "Every remote login, for staff and for IT providers, should need a second factor, as"
             " we discussed in Part 2."),
            ("point",
             "Limit administrator accounts",
             "Use ordinary accounts for daily work. The fewer people and computers with full "
             "control, the slower an attacker can spread."),
            ("point",
             "Turn on built-in protection",
             "Windows has a feature called Controlled Folder Access in Windows Security that "
             "blocks unknown apps from changing protected folders. On a Mac, keep Time Machine "
             "backups going to a drive you disconnect afterward."),
            ("point",
             "Watch for warning signs",
             "New administrator accounts, security tools that suddenly switch off, or large data "
             "transfers at odd hours deserve immediate attention."),
            ("h", "If It Happens to You"),
            "If a ransom note appears, do not panic, and do not start deleting things. Disconnect"
            " the affected computer from the network by turning off Wi-Fi or unplugging the "
            "network cable. If you can, leave it switched on, because the evidence in its memory "
            "can help investigators. Photograph the ransom note. Tell your IT team or provider at"
            " once. In the Philippines, you can report cybercrime to the Cybercrime Investigation"
            " and Coordinating Center through its hotline 1326, or to the PNP Anti-Cybercrime "
            "Group. If personal data was involved, an organization may also have to notify the "
            "National Privacy Commission and the people affected.",
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Steal first, lock last",
             "Modern gangs copy data before encrypting it, so prevention matters as much as recovery."),
            ("point",
             "Every step is a chance",
             "Strange logins, new administrator accounts and midnight uploads come before the lock."),
            ("point",
             "Paying is a bad bet",
             "There is no guarantee, stolen data stays stolen, and payers get targeted again."),
            ("point", "Backups take the hostage away", "Follow 3-2-1-1-0, and actually test a restore."),
            ("h", "Your Part 5 Action Plan"),
            ("point",
             "Set up one automatic backup",
             "Back up your most important folders to an external drive or a trusted cloud "
             "service, and unplug the drive when the backup ends."),
            ("point",
             "Restore one file today",
             "Pick a folder and restore it from your backup. If you cannot, fix the backup before"
             " you need it."),
            ("point",
             "Turn on ransomware protection",
             "On Windows, open Windows Security, go to Virus and threat protection, then "
             "Ransomware protection, and turn on Controlled Folder Access. Allow your trusted "
             "apps when asked."),
            "With these first five parts, the series has covered the basics: how attacks work, "
            "how to protect your accounts, how to spot a scam, how to secure your home network "
            "and how to survive ransomware. Share these posts with someone who handles money or "
            "records, and come back to the action plans every few months.",
            ("cta",
             "Read Part 6: Cloud Security and Privacy",
             "/blog/cybersecurity-part-6-cloud-and-privacy/"),
            ("cta",
             "Read: Cybersecurity Series, Part 4: Securing Your Home and Remote Network",
             "/blog/cybersecurity-part-4-home-network/"),
            ("cta",
             "Read: ALTOS Principle 5, Every Record Has a Seal",
             "/blog/altos-framework-every-record-has-a-seal/"),
            ("ask", "Has your office ever tested restoring its backups? I would like to hear how it went."),
        ],
    },
    {
        "date": "May 5, 2027",
        "title": "Cybersecurity Series, Part 4: Securing Your Home and Remote Network",
        "slug": "cybersecurity-part-4-home-network",
        "category": "security",
        "summary": ("Your Wi-Fi router is the front door of your digital home. Lock it, keep smart devices apart "
                   "from your work laptop, filter dangerous websites, and learn what a VPN can and cannot do."),
        "publish_on": "2027-05-05 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "body": [
            "At home, the internet may arrive through one small box with blinking lights. The "
            "technician installs it, writes the Wi-Fi password on a piece of paper, and leaves. "
            "Years later, the same box is still there, running the same software, with the same "
            "admin password printed on its sticker. Behind it are our phones, our children's "
            "tablets, the smart TV, a CCTV camera and the laptop we use for work or for online "
            "banking.",
            "If you work from home even part of the time, the home router now protects not only "
            "family photos but sometimes office documents, government systems and money. In Part "
            "4 of this series, we will lock that front door, divide the house into safer rooms, "
            "and clear up some common myths about VPNs. When you finish reading, you will be able"
            " to secure your router in under an hour, separate risky gadgets from your work "
            "laptop, and judge when a VPN actually helps.",
            ("h", "Why the Router Matters"),
            "Your router does three jobs at once. It connects your home to your internet "
            "provider, it creates the Wi-Fi network your devices join, and it decides which "
            "traffic may come in from the internet. If an attacker controls it, they can watch or"
            " redirect your traffic, send you to fake websites, or use your connection for their "
            "own attacks. Security agencies have repeatedly warned about criminal and "
            "state-backed groups taking over old home and small-office routers to hide their "
            "activities.",
            ("h", "Step 1: Lock the Front Door"),
            "Start with the settings page of your router. Its address and default login are "
            "usually printed on the sticker on the device, often an address like 192.168.1.1 or "
            "192.168.0.1. If your router is managed by your internet provider, some settings may "
            "be locked; ask the provider for help, or check whether its app lets you change them.",
            ("point",
             "Change the admin password",
             "The password for the settings page is different from the Wi-Fi password. Replace "
             "the default with a long, unique one and save it in your password manager."),
            ("point",
             "Update the firmware",
             "Firmware is the router's software. Look for an update option, or turn on automatic "
             "updates if your router has them. If the maker no longer releases updates for your "
             "model, it is time to replace it."),
            ("point",
             "Use WPA3 or WPA2",
             "In the Wi-Fi security setting, choose WPA3 if all your devices support it, or the "
             "mixed WPA2/WPA3 mode if some older ones do not. Never use WEP or an open network."),
            ("point",
             "Use a strong Wi-Fi password",
             "A long passphrase of several unrelated words is easy to type on a phone and hard to guess."),
            ("point",
             "Turn off WPS",
             "WPS lets devices join by pressing a button or entering a short PIN. The PIN method "
             "has a long history of weaknesses, and few people need it."),
            ("point",
             "Turn off UPnP if you can",
             "UPnP lets devices on your network open doors in your router to the internet "
             "automatically, without asking you. It is convenient for some games and cameras, but"
             " a compromised device can use it too."),
            ("point",
             "Turn off remote management",
             "Unless you truly need to change router settings from outside your home, make sure "
             "the settings page cannot be reached from the internet."),
            ("h", "Step 2: Divide the House into Rooms"),
            "Not every device deserves the same trust. A cheap smart plug or an old CCTV camera "
            "may never receive a security update. If it shares a network with your work laptop, a"
            " compromised gadget becomes a foothold next to your most important files. The fix is"
            " to separate them, an idea security people call segmentation. If your router offers "
            "a guest network, use it for this.",
            ("point",
             "Main network",
             "Only for the devices you use and trust every day: your phones, laptops and tablets,"
             " kept up to date."),
            ("point",
             "Smart-device network",
             "Put smart TVs, cameras, speakers and appliances on the guest network, or on a "
             "separate network if your router supports more than one."),
            ("point",
             "Visitors",
             "Give guests the guest network too, ideally with \"client isolation\" turned on so "
             "devices on it cannot see each other."),
            "This is the same thinking behind a treasury vault. The public can reach the counter,"
            " but not the vault, and even staff need a reason and a key to open it. Your network "
            "can work the same way.",
            ("h", "Step 3: Let DNS Filter the Bad Sites"),
            "Every time you visit a website, your device first asks a DNS server to turn a name "
            "like aumahinay.dev into a numeric address. It is the internet's phone book. By "
            "default, you use the phone book of your internet provider. You can choose a "
            "different one that refuses to look up addresses known to host malware or phishing "
            "pages.",
            "Two free options are widely used. Quad9, run by a non-profit foundation, blocks "
            "known malicious domains at 9.9.9.9. Cloudflare's 1.1.1.1 for Families blocks malware"
            " at 1.1.1.2. (The plain 1.1.1.1 address is fast and private but does not block "
            "anything.) You can set these on your router, so every device at home benefits, or on"
            " a single phone or computer.",
            "Modern browsers and phones also support encrypted DNS, called DNS over HTTPS in "
            "browsers and Private DNS on Android. Encryption keeps people on the same network "
            "from seeing or tampering with the names you look up. DNS filtering is not a complete"
            " defense, but it can stop known bad links before the page even loads.",
            ("h", "Step 4: The Truth About VPNs"),
            "VPN advertisements promise privacy, safety and anonymity in one click. The reality "
            "is narrower. A VPN creates an encrypted tunnel between your device and the VPN "
            "company's server. That is useful, but it helps with a specific problem.",
            ("point",
             "What a VPN does",
             "It hides your traffic from the network you are on, such as hotel or café Wi-Fi, and"
             " from your internet provider. Websites see the VPN's address instead of yours. A "
             "company VPN also lets staff reach office systems safely from outside."),
            ("point",
             "What a VPN does not do",
             "It does not stop malware, it does not block phishing, and it does not make you "
             "anonymous when you log in to your own accounts. It also moves your trust from your "
             "internet provider to the VPN company, which can see your traffic instead."),
            "Most websites, including this one, already use HTTPS, which encrypts what you send "
            "and receive with that site. So on a trusted home network, a commercial VPN adds "
            "little security. On public Wi-Fi, a reputable VPN is a reasonable extra layer. When "
            "in doubt, your phone's mobile data is often safer than an unknown hotspot. Be "
            "careful with free VPN apps: running a VPN costs money, and some free ones pay for it"
            " with your data.",
            ("h", "Smart Gadgets Need Care Too"),
            "CCTV cameras, smart TVs, baby monitors and Wi-Fi plugs are small computers. A few "
            "habits reduce their risk:",
            ("point",
             "Change default passwords",
             "If a camera or gadget came with a password like admin or 12345, change it during setup."),
            ("point",
             "Update or replace",
             "Install updates through the device's app. If a gadget no longer gets updates, "
             "consider replacing it, especially cameras that face the inside of your home."),
            ("point",
             "Turn off what you do not use",
             "Disable remote viewing, voice assistants or cloud features you never use. Fewer "
             "features mean fewer doors."),
            ("point",
             "Buy from known brands",
             "A slightly more expensive device from a maker that publishes updates is often "
             "cheaper in the long run than a no-name gadget that never gets fixed."),
            ("h", "Working from Home Safely"),
            "If you handle office work at home, a few more habits help:",
            ("point",
             "Keep work and family devices apart",
             "Avoid letting children use the laptop you use for work or for official records."),
            ("point",
             "Lock the screen",
             "Press Windows key + L, or Control + Command + Q on a Mac, every time you step away."),
            ("point",
             "Use your office's approved tools",
             "Use the VPN, email and file-sharing services your office provides instead of "
             "personal accounts."),
            ("point",
             "Mind your surroundings",
             "Video calls and screens can be seen and heard by others in cafés and shared spaces."),
            ("h", "Stay-Safe Reminders"),
            ("point",
             "The router is the front door",
             "Change its admin password, update it, and turn off WPS, UPnP and remote management."),
            ("point", "Separate by trust", "Put smart gadgets and visitors on the guest network."),
            ("point",
             "Let DNS filter for you",
             "A filtering DNS such as 9.9.9.9 blocks known malicious sites."),
            ("point",
             "Know what a VPN is for",
             "It protects you on untrusted networks; it does not stop malware or phishing."),
            ("h", "Your Part 4 Action Plan"),
            ("point",
             "Log in to your router this week",
             "Change the admin password, install any firmware update, and turn off WPS and remote"
             " management."),
            ("point",
             "Move your gadgets",
             "Turn on the guest network and move smart TVs, cameras and other gadgets to it."),
            ("point",
             "Check who is connected",
             "Look at the list of connected devices on your router. If you see something you do "
             "not recognize, change the Wi-Fi password and reconnect your own devices."),
            ("point",
             "Try a filtering DNS",
             "Set 9.9.9.9 or 1.1.1.2 on your router or on your phone, then browse normally for a week."),
            "An hour spent on your router protects every person and every device in your home, every day.",
            ("cta", "Read Part 5: Ransomware", "/blog/cybersecurity-part-5-ransomware/"),
            ("cta",
             "Read: Cybersecurity Series, Part 3: The Art of Human Hacking",
             "/blog/cybersecurity-part-3-human-hacking/"),
            ("ask",
             "Did you find an old admin password or an unknown device on your router? Tell me "
             "what you found."),
        ],
    },
    {
        "date": "November 19, 2026",
        "title": "Cybersecurity Series, Part 3: The Art of Human Hacking",
        "slug": "cybersecurity-part-3-human-hacking",
        "category": "security",
        "summary": "Most scams do not break into computers; they persuade people. Learn the pressure tricks behind "
                   "phishing, smishing, fake bosses and deepfake calls, and the simple rules that stop them.",
        "publish_on": "2026-11-19 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "body": [
            "Why would a criminal spend months looking for a flaw in a well-protected system when"
            " a convincing message can get someone inside to open the door? That is the idea "
            "behind social engineering, or human hacking. Instead of attacking the machine, the "
            "attacker works on the person using it, through trust, fear, kindness or simple "
            "hurry.",
            "You may have received a text saying a package is on hold, an account will be "
            "suspended, or we have won a prize we never joined. In Part 3 of this series, we look"
            " at how these tricks work, why smart people fall for them, and the habits that "
            "defeat them, including scams that now use artificial intelligence to copy voices and"
            " faces. Read to the end and you will be able to spot the pressure tricks in a "
            "message within seconds and know exactly what to do if you already clicked.",
            ("Treasury work is a natural target for this kind of pressure, because it is where "
             "requests turn into money. The rule I lean on most is the second principle of my ALTOS "
             "Framework: no release without a voucher. A payment that rests only on a phone call or a "
             "message has no document behind it, and that gap is exactly what human hackers try to "
             "use."),
            ("h", "Why Smart People Get Fooled"),
            "Falling for a scam is not a sign of low intelligence. Scammers design messages to "
            "push us into acting before we think. Scams lean on levers like these:",
            ("point",
             "Urgency",
             "\"Your account will be locked in 30 minutes.\" A deadline leaves no time to check."),
            ("point",
             "Authority",
             "The message claims to come from a bank, a government agency, the police or your "
             "boss. We are trained to obey such voices."),
            ("point",
             "Fear",
             "A threat of arrest, a fine, a frozen account or a relative in trouble makes the "
             "heart beat faster and the mind work slower."),
            ("point",
             "Greed or hope",
             "A prize, a refund, an easy job or an investment that doubles your money."),
            ("point",
             "Familiarity",
             "The message uses your name, your office, a real supplier or a friend's account, so "
             "it feels normal."),
            "Once you know the levers, you can feel them being pulled. When a message makes you "
            "feel rushed, afraid or excited, treat that feeling as a warning sign and slow down.",
            ("quote", "When a message makes you hurry, that is exactly the moment to stop."),
            ("h", "The Many Faces of Phishing"),
            "Phishing is the use of a fake message to steal passwords, money or personal details,"
            " or to install malware. It comes in many forms:",
            ("point",
             "Email phishing",
             "A message that looks like it is from your bank, an online store or your IT "
             "department, with a link to a fake login page or a harmful attachment."),
            ("point",
             "Smishing",
             "Phishing by text message. Common examples include fake delivery notices, "
             "\"unclaimed\" rewards and warnings that your SIM or e-wallet will be suspended."),
            ("point",
             "Vishing",
             "Phishing by voice call. A caller pretends to be from a bank, a telco or the "
             "authorities and asks for a one-time PIN, card number or account details."),
            ("point",
             "Quishing",
             "Phishing with a QR code, printed on a poster or sent in an email. Because you scan "
             "it with your phone, you cannot easily see the address before it opens."),
            ("point",
             "Fake pages and look-alike addresses",
             "Attackers register names that look almost right, such as a letter swapped for a "
             "similar one, and copy the real site's design."),
            "Modern phishing pages can be very convincing. Some even pass your password and your "
            "one-time code to the real site at the same moment, logging the attacker in as you. "
            "That is why we said in Part 2 that passkeys and security keys, which refuse to work "
            "on fake sites, are the strongest protection.",
            ("h", "Business Email Compromise: The Fake Invoice"),
            "Some of the costliest scams involve no malware at all. In business email compromise,"
            " an attacker takes over or imitates the email of a boss, supplier or partner. "
            "Sometimes they read real conversations for weeks. Then, at the right moment, they "
            "send one message: a new bank account for the next payment, an urgent transfer the "
            "boss \"approved,\" or a request to buy gift cards.",
            "This should worry anyone who handles payments, including offices that pay suppliers "
            "and contractors. The defense is not a gadget; it is procedure. In treasury work, we "
            "already know that a payment needs proper documents and approval, no matter who is "
            "asking or how urgent it sounds. The same rule applies to email: a request to change "
            "bank details or to rush a payment must be confirmed by phone, using a number you "
            "already have, never the one in the message.",
            ("h", "Deepfakes: When Seeing Is No Longer Believing"),
            "Artificial intelligence has made human hacking more dangerous. With a short sample "
            "of someone's voice, taken from a video or a voicemail, criminals can produce a "
            "convincing copy that says anything. Video can be faked too.",
            "In early 2024, Hong Kong police described a case in which a finance employee of the "
            "engineering firm Arup joined a video call with people who looked and sounded like "
            "the company's chief financial officer and colleagues. They were deepfakes. Persuaded"
            " by the call, the employee made 15 transfers totaling about HK$200 million, roughly "
            "US$25 million.",
            "The same trick works on families. A parent receives a call from a crying voice that "
            "sounds exactly like their child, asking for money right away. The defense is to "
            "verify through a separate channel: hang up and call the person back on their known "
            "number, or ask a question only the real person can answer.",
            ("h", "How to Check a Message in Ten Seconds"),
            ("point",
             "Look at the real sender",
             "Check the full email address or number, not just the display name."),
            ("point",
             "Check the link before you tap",
             "On a computer, hover over it. On a phone, press and hold to preview the address. "
             "Read the domain name carefully from right to left."),
            ("point",
             "Go there yourself",
             "Instead of tapping a link, open your bank's app or type the address you know."),
            ("point",
             "Never share one-time codes",
             "Banks and e-wallets will not ask for your OTP, PIN or password by call, text or chat."),
            ("point",
             "Be suspicious of attachments",
             "Turn on \"show file extensions\" so a file named invoice.pdf.exe cannot pretend to be a PDF."),
            ("h", "What Domain Owners Can Do"),
            "If you run a website or an office email domain, you can make it harder for criminals"
            " to send email in your name. Three records published in your domain's DNS settings "
            "do the work. SPF lists the servers allowed to send your mail. DKIM adds a digital "
            "signature to each message. DMARC tells receiving servers what to do when a message "
            "fails these checks, such as sending it to spam or rejecting it. Since 2024, Google "
            "and Yahoo have required these records from senders of large volumes of email, so "
            "they are now standard practice.",
            ("h", "The Law Is on Your Side"),
            "The Philippines has strengthened its laws against these schemes. The Anti-Financial "
            "Account Scamming Act (Republic Act No. 12010), signed in July 2024, punishes social "
            "engineering schemes, money muling and the selling or lending of bank and e-wallet "
            "accounts for scams. Large-scale schemes can even be treated as economic sabotage. "
            "The SIM Registration Act (Republic Act No. 11934) was also meant to make scammers "
            "easier to trace.",
            "If you encounter a scam, report it. The Cybercrime Investigation and Coordinating "
            "Center runs the Inter-Agency Response Center hotline 1326. Tell your bank or "
            "e-wallet right away if money or account details are involved, because quick reports "
            "give them the best chance to stop a transfer.",
            ("h", "If You Already Clicked"),
            "It happens to careful people every day. What matters is what you do in the next few "
            "minutes, so act rather than hope for the best.",
            ("point",
             "If you typed a password",
             "Change it at once on the real site, and anywhere else you used the same password. "
             "Then sign out of other sessions and check your MFA settings."),
            ("point",
             "If you shared a code or card details",
             "Call your bank or e-wallet immediately through its official hotline and ask them to"
             " block the account or card. Minutes count."),
            ("point",
             "If you opened a file",
             "Disconnect the device from the internet and ask your IT team or a trusted "
             "technician to check it before you use it for banking or work again."),
            ("point",
             "Tell someone",
             "Report it to your office IT team if it involved work, and warn family or colleagues"
             " who may receive the same message. There is no shame in reporting; the shame "
             "belongs to the scammer."),
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Your feelings are the warning",
             "Urgency, fear, authority and greed are levers. When you feel rushed, slow down."),
            ("point",
             "Verify on a second channel",
             "Confirm payment or bank-detail changes by calling a number you already have."),
            ("point",
             "Seeing is no longer believing",
             "Voices and video can be faked; a family safe word helps."),
            ("point", "Act fast if you clicked", "Change passwords, call your bank, and report to 1326."),
            ("h", "Habits That Stop a Scam"),
            ("point",
             "Adopt a call-back rule",
             "Never change bank details, approve a payment or share sensitive files based only on"
             " an email, text or chat. Call back on a number you already know."),
            ("point",
             "Agree on a family safe word",
             "Choose a word or question that only your family knows, to check any emergency call "
             "asking for money."),
            ("point",
             "Show file extensions",
             "On Windows 11, open File Explorer, choose View, then Show, and turn on File name "
             "extensions. On a Mac, open Finder Settings, then Advanced, and tick Show all "
             "filename extensions."),
            ("point",
             "Save 1326",
             "Add the hotline to your contacts, and share it with your parents and older relatives."),
            "Technology can catch scams, but the last line of defense is a person who pauses, "
            "checks and asks. Share these habits with the people around you, especially those who"
            " handle money.",
            ("cta", "Read Part 4: Your Home Network", "/blog/cybersecurity-part-4-home-network/"),
            ("cta",
             "Read: Cybersecurity Series, Part 2: Identity Is the New Perimeter",
             "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("cta",
             "Read: ALTOS Principle 6, Separate the Hands",
             "/blog/altos-framework-separate-the-hands/"),
            ("ask",
             "What is the most convincing scam message you have received? Send it to me (remove "
             "your personal details first), and it may help someone else."),
        ],
    },
    {
        "date": "November 14, 2026",
        "title": "Cybersecurity Series, Part 2: Identity Is the New Perimeter",
        "slug": "cybersecurity-part-2-passwords-and-mfa",
        "category": "security",
        "summary": ("Attackers no longer break in; they log in. That is why long passphrases beat complex "
                   "passwords, why a password manager helps, which kinds of two-step login are strongest, and "
                   "why passkeys are coming."),
        "publish_on": "2026-11-14 22:00",
        "body": [
            "A firewall cannot stop someone who walks in with your username and password. That is"
            " why you will hear security people say that identity is the new perimeter. Your work"
            " systems, your bank, your e-wallet and your social media accounts are all reachable "
            "from anywhere in the world. The only thing standing between an attacker and your "
            "account is how well you prove that you are you.",
            "In Part 2 of this series, we look at passwords, why the old rules failed, and the "
            "tools that make logins far safer: password managers, multi-factor authentication and"
            " passkeys. Along the way, you will see how to build a password that resists cracking, which login protections are strongest, and what to do if an account is taken over.",
            ("These are not just rules I read about for the Google Cybersecurity Professional "
             "Certificate. When I built ALTOS, several of the safeguards I wrote into it were about "
             "logins: passwords are stored only in scrambled form, accounts lock after repeated wrong "
             "attempts, and idle sessions close on their own. I also chose a .dev address for this "
             "website partly because every .dev site must use a secure connection. Small rules that "
             "work without anyone remembering them do most of the protecting."),
            ("h", "Why the Old Password Rules Failed"),
            "For years, we were told to create passwords with at least eight characters, a "
            "capital letter, a number and a symbol, and to change them every few months. The "
            "result was predictable. People wrote passwords like Password1! and then, when forced"
            " to change them, used Password2!. These are hard for people to remember and easy for"
            " computers to guess, because attackers know exactly how people adapt to such rules.",
            "The guidance has changed. The United States National Institute of Standards and "
            "Technology (NIST), whose digital identity guidelines are followed around the world, "
            "finalized a new edition in August 2025 (SP 800-63B-4). It says passwords used on "
            "their own should be at least 15 characters long, systems should accept much longer "
            "ones, and organizations should not impose composition rules like \"one symbol and one"
            " number\" or force regular password changes. Passwords should be changed when there "
            "is evidence they were exposed, and new passwords should be checked against lists of "
            "common and leaked ones.",
            ("h", "Length Beats Complexity"),
            "Every extra character multiplies the number of guesses an attacker needs. A password"
            " of eight random characters looks strong, but powerful graphics cards can try "
            "billions of guesses per second against passwords that a website stored carelessly. A"
            " passphrase of four or five unrelated words, such as "
            "\"mango-ladder-sunrise-pencil-river\", is much longer, easier to remember and far "
            "harder to crack.",
            "The catch is that a phrase only helps if it is truly random. Song lyrics, Bible "
            "verses, birthdays and your children's names are all among the first things attackers"
            " try.",
            ("h", "How Accounts Really Get Stolen"),
            "Guessing is not the only way in. They are stolen in other ways:",
            ("point",
             "Reused passwords",
             "When one website is breached, attackers try the same email and password on banks, "
             "email and social media. This is called credential stuffing, and it works because "
             "people reuse passwords."),
            ("point", "Phishing", "A fake login page collects your password as you type it."),
            ("point",
             "Infostealer malware",
             "Malicious programs, often hidden in pirated software or fake downloads, copy the "
             "passwords saved in your browser and send them to criminals, who sell them in bulk."),
            "Verizon's 2025 Data Breach Investigations Report found that the abuse of stolen "
            "credentials was the most common way into the systems it studied, at 22% of breaches."
            " A strong password does not help if it is reused, typed into a fake page or stolen "
            "from your computer. That is why the next two tools matter so much.",
            ("h", "Tool 1: A Password Manager"),
            "No one can remember a different long password for fifty accounts. A password manager"
            " does it for you. It creates a strong random password for each account, stores them "
            "in an encrypted vault, and fills them in when you log in. You remember only one "
            "strong master password.",
            "Good password managers encrypt your vault on your own device before it is synced, "
            "using your master password to build the key. The company that stores your vault "
            "cannot read it. Many reputable options exist, including free and open-source ones "
            "such as Bitwarden, as well as the managers built into your phone or browser. The "
            "best one is the one you will actually use.",
            "A password manager also protects you from fake websites in a quiet way: it will not "
            "offer to fill in your bank password on a page that is not your bank's real address. "
            "When it refuses, take that as a warning.",
            ("h", "Tool 2: Multi-Factor Authentication"),
            "Multi-factor authentication (MFA), also called two-step verification, asks for a "
            "second proof besides your password: something you have, like your phone, or "
            "something you are, like your fingerprint. Even if a criminal gets your password, "
            "they still need that second factor. Not all second factors are equally strong, "
            "though.",
            ("point",
             "Codes by SMS or email (good, but weakest)",
             "Far better than nothing, but codes can be stolen through SIM swapping, where a "
             "criminal convinces a telco to move your number to their SIM, or by tricking you "
             "into reading the code aloud."),
            ("point",
             "Authenticator apps (better)",
             "Apps such as Google Authenticator or Microsoft Authenticator produce a new "
             "six-digit code every 30 seconds on your phone, without using the mobile network."),
            ("point",
             "Passkeys and security keys (strongest)",
             "These use cryptography tied to the real website's address. A fake site cannot use "
             "them, so they resist phishing by design."),
            "Our regulators are moving the same way. Under Circular No. 1213 of the Bangko "
            "Sentral ng Pilipinas, banks and e-wallets with large online transaction volumes had "
            "until June 25, 2026 to act. By then they had to stop relying on SMS and email "
            "one-time PINs for high-risk transactions, and use stronger methods such as "
            "biometrics or passwordless login. If your bank app now asks for a face scan for "
            "large transfers, this is why.",
            ("h", "Tool 3: Passkeys"),
            "Passkeys are designed to replace passwords altogether. When you create a passkey, "
            "your device makes a pair of matching keys. The public key goes to the website; the "
            "private key stays on your phone or computer, protected by your fingerprint, face or "
            "screen lock. When you log in, your device proves it has the private key without ever"
            " sending it. There is nothing to type, nothing to reuse and nothing for a fake site "
            "to steal.",
            "Google, Apple and Microsoft accounts, along with a growing number of shopping, "
            "social media and banking services, now support passkeys. Look for \"Passkeys\" or "
            "\"Sign in without a password\" in your account's security settings.",
            ("h", "Protect the Master Key: Your Email"),
            "If you secure only one account today, make it your main email. Other accounts let "
            "you reset their passwords through email. Whoever controls your inbox can take over "
            "the rest. Give it a unique long password, your strongest form of MFA and an "
            "up-to-date recovery phone number.",
            ("quote", "Whoever controls your email can reset almost everything else. Guard it first."),
            ("h", "Signs Your Account Has Been Taken Over"),
            "Even careful people get caught. The sooner you notice, the less damage is done. "
            "Watch for these signs:",
            ("point",
             "Alerts you did not trigger",
             "Login alerts from a new device or place, or password reset emails you did not ask for."),
            ("point",
             "Changes you did not make",
             "A new recovery email or phone number, forwarding rules in your email, or messages "
             "in your Sent folder that you never wrote."),
            ("point",
             "Friends asking strange questions",
             "Contacts receiving requests for money or odd links from your account."),
            ("point",
             "Your SIM suddenly stops working",
             "If your phone loses signal for no clear reason and you cannot make calls, contact "
             "your telco at once. It may be a SIM swap."),
            "If you see these signs, act quickly. From a device you trust, change the password, "
            "sign out of all other sessions (look for a \"sign out everywhere\" option), check the "
            "recovery details and MFA settings, and remove anything you did not add. If money is "
            "involved, call your bank or e-wallet right away using the number on its official "
            "website or on the back of your card.",
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Length beats complexity",
             "A long, random passphrase is stronger and easier to remember than a short, complex password."),
            ("point", "Never reuse a password", "A password manager gives every account its own."),
            ("point",
             "Not all MFA is equal",
             "Authenticator apps beat SMS codes, and passkeys resist phishing by design."),
            ("point",
             "Guard your email first",
             "Whoever controls your inbox can reset almost everything else."),
            ("h", "Lock Down Your Logins"),
            ("point",
             "Start a password manager",
             "Install one and move your five most important accounts into it, each with a new, "
             "unique password of 15 characters or more."),
            ("point",
             "Upgrade your MFA",
             "Turn on an authenticator app or a passkey for your main email, and keep SMS only as a backup."),
            ("point",
             "Save your recovery codes",
             "When you turn on MFA, you are given backup codes. Print them and keep them "
             "somewhere safe at home, not in a photo on your phone."),
            ("point",
             "Stop saving passwords in random places",
             "Delete passwords stored in notes apps, chats or unprotected spreadsheets once they "
             "are in your password manager."),
            "None of this takes a computer expert. A password manager, a second factor and a "
            "passkey on your email will protect you better than any rule about symbols and "
            "numbers ever did.",
            ("cta", "Read Part 3: Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
            ("cta",
             "Read: Cybersecurity Series, Part 1: How Modern Cyberattacks Really Work",
             "/blog/cybersecurity-part-1-how-cyberattacks-work/"),
            ("cta",
             "Read: ALTOS Principle 5, Every Record Has a Seal",
             "/blog/altos-framework-every-record-has-a-seal/"),
            ("ask", "Have you tried passkeys yet? Tell me which account you switched first."),
        ],
    },
    {
        "date": "November 10, 2026",
        "title": "Cybersecurity Series, Part 1: How Modern Cyberattacks Really Work",
        "slug": "cybersecurity-part-1-how-cyberattacks-work",
        "category": "security",
        "summary": "Forget the hoodie-wearing genius. Today's cyberattacks are run like businesses. Learn what security "
                   "protects, who the attackers are, how a breach unfolds step by step, and why layered defenses work.",
        "publish_on": "2026-11-10",
        "body": [
            "Ask someone to picture a hacker and you will probably hear about a lone genius in a "
            "dark room, typing green code at impossible speed until a screen flashes \"Access "
            "granted.\" It makes a good movie scene. It is also misleading.",
            "Much of today's cybercrime looks less like a heist and more like a business. "
            "Criminal groups divide the work, rent out their tools, buy stolen passwords in bulk "
            "and use automated programs that scan the internet for weak devices day and night. "
            "You do not have to be important to become a victim. You only have to be easy.",
            "This post opens a cybersecurity series on this blog. I work in the treasury service "
            "and build software on the side, and both jobs have taught me the same lesson: what "
            "protects public money and public records is not one strong lock but many good "
            "habits. The series is written for everyone: parents, students, office workers, small"
            " business owners and anyone who uses a phone. We begin with the basics: what security protects, who the attackers are, how a typical breach unfolds, and why layers of defense work better than one strong wall.",
            ("h", "What Security Protects: The CIA Triad"),
            "Security professionals sum up their work in three words, known as the CIA triad. (It"
            " has nothing to do with the spy agency.)",
            ("point",
             "Confidentiality",
             "Only the right people can see the information. When a list of taxpayers' names and "
             "addresses leaks online, confidentiality has failed."),
            ("point",
             "Integrity",
             "Information stays accurate and unaltered. If someone quietly changes the bank "
             "account number on a supplier's invoice, integrity has failed, even if no one "
             "notices yet."),
            ("point",
             "Availability",
             "Systems and data are there when people need them. When ransomware locks an office's"
             " computers or a website is knocked offline, availability has failed."),
            "Every security tool you have heard of, from antivirus to backups to encryption, "
            "exists to protect one or more of these three. When you are unsure whether something "
            "is a security issue, ask: does it threaten who can see the data, whether it can be "
            "trusted, or whether it is there when needed?",
            ("h", "Who Is on the Other Side?"),
            "Attackers have different goals, and knowing their goals helps you understand their methods.",
            ("point",
             "Cybercriminals",
             "Motivated by money. They steal passwords, card numbers and bank details, run scams "
             "and deploy ransomware. Some use ransomware-as-a-service, renting ready-made malware"
             " from its developers and sharing the ransom with them."),
            ("point",
             "State-sponsored groups",
             "Teams backed by governments that spy, steal secrets or prepare to disrupt power, "
             "telecommunications and other critical services. They are patient and may hide "
             "inside a network for months."),
            ("point",
             "Hacktivists",
             "People driven by a political or social cause. They deface websites, leak documents "
             "or flood a site with traffic to take it offline, aiming for attention."),
            ("point",
             "Insiders",
             "People who already have access. Some act out of anger or greed, and others make "
             "honest mistakes: an email sent to the wrong person, or a shared folder left open to"
             " anyone with the link."),
            ("h", "How a Breach Unfolds"),
            "A serious attack is rarely a single event. It is a chain of steps, and each step is "
            "a chance to stop it. Security teams describe this chain with models such as Lockheed"
            " Martin's Cyber Kill Chain and the MITRE ATT&CK knowledge base, which catalogs the "
            "techniques real attackers use. In plain terms, an intrusion can follow a path like "
            "this:",
            ("point",
             "1. Reconnaissance",
             "The attacker gathers information: staff names from social media, email formats, "
             "leaked passwords from old breaches, and devices exposed to the internet."),
            ("point",
             "2. Initial access",
             "They get a foothold, often by logging in rather than breaking in: a phishing email "
             "that captures a password, a password bought from a criminal market, or a known flaw"
             " in a device that was never updated."),
            ("point",
             "3. Persistence",
             "They make sure they can return, by creating hidden accounts or installing "
             "remote-control tools that survive a restart."),
            ("point",
             "4. Privilege escalation and lateral movement",
             "The first computer is rarely the prize. They collect more passwords, gain "
             "administrator rights and move from machine to machine toward servers, databases and"
             " backups."),
            ("point",
             "5. Action on objectives",
             "Finally, they do what they came for: copy data out, transfer money, plant "
             "ransomware or disrupt services."),
            "Verizon's 2025 Data Breach Investigations Report, one of the industry's largest "
            "yearly studies, shows what the first doors look like. Stolen credentials were the "
            "most common way in, at 22% of breaches, followed closely by the exploitation of "
            "software flaws, at 20%. Third parties such as suppliers and service providers were "
            "involved in 30% of breaches, double the year before. In other words: weak passwords,"
            " missing updates and trusted partners.",
            ("h", "Why One Wall Is Not Enough"),
            "For a long time, organizations treated security like a castle. They built a strong "
            "wall, a firewall, around the office network and trusted everyone inside. That model "
            "has aged badly. Our data now lives in cloud services, our staff work from home and "
            "from their phones, and a single stolen password can carry an attacker across the "
            "drawbridge. Once inside a flat, trusting network, they can move freely.",
            "This does not mean firewalls are useless. It means they cannot be the only defense.",
            ("h", "How We Fight Back: Layers"),
            "The answer is defense in depth. Safety experts often explain it with the Swiss "
            "cheese model, first described by the psychologist James Reason to show how accidents"
            " happen. Picture each defense as a slice of Swiss cheese. Every slice has holes. "
            "Spam filters miss some emails. People get tired and click. Antivirus does not "
            "recognize every new threat. But when you stack several slices, the holes rarely line"
            " up.",
            "Suppose a phishing email slips past the filter and you type your password into a "
            "fake page. Multi-factor authentication stops the attacker from logging in. If they "
            "get past that, up-to-date software and endpoint protection may block their tools. If"
            " those fail, limited access rights keep them from reaching everything. And if the "
            "worst happens, offline backups let you recover without paying anyone.",
            "Treasury work runs on the same principle. We do not rely on one honest person; we "
            "use separation of duties, official receipts, daily reports of collections and "
            "deposits, and regular audits. No single control is perfect, but together they make "
            "errors and fraud hard to hide. Good cybersecurity works the same way.",
            ("quote",
             "You do not need to be impossible to hack. You need to be too costly, too slow and "
             "too noisy to be worth the trouble."),
            ("h", "Four Myths That Help Attackers"),
            "Let us also clear away a few beliefs that make attackers' work easier.",
            ("point",
             "Myth: I am not important enough to be targeted",
             "Attacks can be automated. A program that tries leaked passwords or scans for "
             "unpatched devices does not care who you are. Your account, your phone number and "
             "your computer's power are all worth something to a criminal."),
            ("point",
             "Myth: I have antivirus, so I am safe",
             "Antivirus is one useful slice of cheese, not the whole block. It cannot stop you "
             "from typing your password into a fake page or sending money to a scammer."),
            ("point",
             "Myth: Phones and Macs do not get hacked",
             "Every device can be attacked, and phones carry our banking apps, our one-time PINs "
             "and our private chats. Scams do not care which brand you use."),
            ("point",
             "Myth: Security is the IT office's job",
             "IT teams build the walls, but each of us holds a key. One rushed click can undo the"
             " best technology, and one careful pause can stop an attack that technology missed."),
            ("h", "A Note for the Philippines"),
            "Cybercrime is not a distant problem. Text scams, fake e-wallet links and account "
            "takeovers are part of daily life, and government agencies have suffered serious "
            "attacks. The country has laws to respond: the Cybercrime Prevention Act of 2012 "
            "(Republic Act No. 10175), the Data Privacy Act of 2012 (Republic Act No. 10173) and,"
            " more recently, the Anti-Financial Account Scamming Act of 2024 (Republic Act No. "
            "12010). Laws punish criminals after the fact, though. Habits protect us before.",
            ("h", "Stay-Safe Reminders"),
            ("point",
             "Security protects three things",
             "Confidentiality, integrity and availability: who can see data, whether it can be "
             "trusted, and whether it is there when needed."),
            ("point",
             "Attackers often log in instead of breaking in",
             "Stolen passwords and unpatched flaws are among the most common first doors."),
            ("point",
             "A breach is a chain",
             "Each step, from reconnaissance to the final action, is a chance to stop it."),
            ("point",
             "Layers beat walls",
             "Several imperfect defenses together stop what any single one would miss."),
            ("h", "Three Steps for This Week"),
            ("point",
             "Check your exposure",
             "Visit haveibeenpwned.com and enter your main email address. The free service shows "
             "which known data breaches included your address. If a password you still use was "
             "exposed, change it."),
            ("point",
             "Turn on automatic updates",
             "On your phone, computer and browser. Some attacks use flaws that were fixed months "
             "earlier, betting that people keep pressing \"Remind me later.\""),
            ("point",
             "Name your three most important accounts",
             "Usually your main email, your bank or e-wallet, and your work login. Your email "
             "matters most, because it can reset the passwords of almost everything else."),
            "Start with these three steps this week. They take less than an hour, and they close "
            "the doors that attackers try first.",
            ("cta", "Read Part 2: Identity", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("cta", "Read: Why .dev and Not .com", "/blog/why-dev-and-not-com/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "Which cybersecurity topic would you like this series to explain next?"),
        ],
    },
]
