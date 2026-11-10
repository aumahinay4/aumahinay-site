# Cybersecurity blog series (Season 1: Cyber Hygiene and Personal Defense).
# Planned from Butch's Google Doc "10-Week Cybersecurity Blog Series Roadmap & Drafts"
# (Drive 1cqfvL885e80Hj7cjLE5YWEC392nrzD2ZkZmSLoHgwRE), written in original words and
# fact-checked on 2026-11-10 (Parts 6-10 the same day). Butch (2026-11-10): Part 1 goes live on Nov 10, then one part every Saturday at
# 10 pm PH ("YYYY-MM-DD 22:00"). A "cta" button to a later part shows only once that part is live.
# Newest first, like BLOG in content.py, which puts these posts at the top of its list.

SERIES = "Cybersecurity Series"

CYBER_POSTS = [
    {
        "date": "January 9, 2027",
        "title": "Cybersecurity Series, Part 10: AI, Quantum Computers and the Next Wave of Threats",
        "slug": "cybersecurity-part-10-future-threats",
        "category": "security",
        "summary": "How artificial intelligence helps both scammers and defenders, why quantum computers are already "
                   "changing the way the internet is locked, what billions of smart gadgets mean for your home, and the "
                   "habits that will still protect you ten years from now.",
        "publish_on": "2027-01-09 22:00",
        "body": [
            "Every few years, a new technology arrives with two promises at once. It will make life easier, and it "
            "will make crime easier too. Email gave us faster letters and phishing. Online banking gave us "
            "convenience and account takeovers. Mobile wallets let a vendor in the public market accept payment "
            "with a phone, and they also gave scammers a new way to ask for money.",
            "In this tenth part of the series, we look ahead at three changes already underway: artificial "
            "intelligence, quantum computing and the flood of smart devices in our homes and offices. None of them "
            "is a reason to panic. Each one is a reason to understand a little more, so that you can enjoy the "
            "benefits without becoming the easy target.",
            ("h", "Artificial Intelligence in the Hands of Scammers"),
            "Not long ago, the easiest way to spot a scam email was its language. The grammar was clumsy, the "
            "greeting was strange and the tone did not match the supposed sender. Generative AI tools have removed "
            "much of that warning sign. A scammer who barely speaks English can now produce a polished, polite "
            "message in English, Filipino or any other language in seconds, and tailor it to your job or your "
            "town using details from your public posts.",
            "Voices and faces can be copied too. With a short recording taken from a video online, tools can "
            "produce speech that sounds like a particular person. We saw in Part 3 how an employee in Hong Kong was "
            "tricked into sending about HK$200 million after a video call with what appeared to be senior "
            "colleagues, all of them fakes. The same trick works at a smaller scale: a voice message that "
            "sounds like your child, your boss or your mayor, asking for an urgent transfer or a load of "
            "e-wallet credits.",
            "The defense is not a better eye for fakes. The fakes will keep improving, and trying to judge them by "
            "how real they look is a contest we will lose. The defense is a habit: when a message asks for money, "
            "passwords or one-time PINs, verify it through a channel you already trust. Call back on the number you "
            "have saved, not the number in the message. Some families agree on a private code word for "
            "emergencies, something an impostor would not know. It sounds old-fashioned, and that is exactly why it "
            "works.",
            ("quote", "When anything can be faked, verification becomes a daily habit, not a special event."),
            ("h", "When the AI Itself Is the Target"),
            "AI tools are now built into email, office software, search engines and customer service. That makes "
            "the tools themselves a target. The OWASP Foundation, which we met in Part 7, publishes a separate "
            "list of the top risks for applications built on large language models. Its 2025 edition places "
            "prompt injection first, followed by sensitive information disclosure. In plain words, these are two "
            "of the biggest worries:",
            ("point", "Hidden instructions", "An AI assistant reads a web page, a document or an email that "
             "contains instructions written for the AI, not for you. If the assistant obeys, it might reveal "
             "information or take an action you never asked for. This is called prompt injection."),
            ("point", "Leaked information", "Whatever you paste into an AI tool may be stored, reviewed or used "
             "according to that service's terms. Pasting a list of taxpayers, a payroll file or a confidential "
             "memo into a public chatbot can be a data leak, even if nobody meant harm."),
            ("point", "Too much power", "An assistant connected to your email, files and accounts can do a lot of "
             "good, and a lot of damage if it is tricked. The more an AI tool is allowed to do on its own, the "
             "more carefully its permissions should be limited."),
            "For ordinary users, the practical rules are simple. Do not paste personal or confidential data into an AI "
            "tool unless your office has approved that tool for that kind of data. Read what an AI assistant "
            "is about to send or delete before you confirm it. And treat its answers the way you would treat advice "
            "from a confident stranger: useful, but worth checking, especially on law, health and money.",
            ("h", "AI on the Defenders' Side"),
            "The same technology also works for the good side. Email providers use machine learning to filter "
            "billions of spam and phishing messages. Banks use it to notice a transaction that does not fit your "
            "usual pattern and pause it for a check. Security teams use it to sort through mountains of logs and "
            "find the one login that looks wrong. The contest between attackers and defenders is not new. AI "
            "simply speeds up both sides, which makes the basic controls from earlier parts, such as multi-factor "
            "authentication, updates and backups, even more important.",
            ("h", "Quantum Computers and the Locks of the Internet"),
            "Every time you see the padlock in your browser, your connection is protected by mathematics. Some of "
            "that mathematics relies on problems that ordinary computers would need an impossibly long time to "
            "solve. A large and reliable quantum computer, which works on very different principles, could solve "
            "some of those problems much faster. That would weaken several of the methods that protect online "
            "banking, government websites and digital signatures today.",
            "Such a machine does not exist yet, and experts disagree on when it might. So why worry now? Because "
            "of a strategy often called \"harvest now, decrypt later.\" An attacker can record encrypted data today "
            "and store it, hoping to unlock it years from now. For most messages that hardly matters. For records "
            "that must stay confidential for decades, such as land records, tax files, health information or "
            "state secrets, it matters a great deal.",
            "The good news is that the work to replace these locks is well underway. On August 13, 2024, the "
            "United States National Institute of Standards and Technology (NIST) published its first three "
            "post-quantum cryptography standards, known as FIPS 203, FIPS 204 and FIPS 205. They describe new "
            "methods for exchanging keys and making digital signatures that are designed to resist quantum attacks. "
            "In March 2025, NIST chose another method, called HQC, as a backup, and more standards are in "
            "progress. Major web browsers, including Google Chrome, have already begun using a post-quantum key "
            "exchange on many secure connections, mostly without users noticing.",
            "For individuals, the action is almost boring: keep your browser, phone and computer updated, because "
            "that is how the new locks reach you. For organizations, the work is bigger. They need to know where "
            "they use encryption, which systems are too old to be updated, and which records must stay secret the "
            "longest, so that those are moved to the new methods first.",
            ("h", "Billions of Small Computers in Our Homes"),
            "A smart TV, a Wi-Fi camera, a voice speaker, a smart plug and even some rice cookers and air "
            "conditioners are all small computers connected to the internet. They are convenient, often cheap, "
            "and frequently forgotten once installed. Many never receive a security update.",
            "The danger was made clear in October 2016. A piece of malware called Mirai had spread to a huge number "
            "of internet cameras and video recorders, mostly by trying factory-default usernames and passwords. On "
            "October 21, that army of hijacked gadgets flooded Dyn, a company that helps direct internet "
            "traffic, and many popular websites, including Twitter, Netflix and Reddit, became unreachable for "
            "parts of the day. The owners of those cameras had no idea their devices were taking part.",
            "Smart devices can also be a privacy risk in their own right. A camera that faces the inside of your "
            "home, a speaker that listens for a wake word, or a baby monitor with a weak password can expose the "
            "most private parts of family life. Before buying a smart device, ask a few questions:",
            ("point", "Does the maker provide updates?", "Choose brands that publish security updates and say how "
             "long they will support the product."),
            ("point", "Can I change the default password?", "If a device has a fixed password you cannot change, "
             "do not connect it to the internet."),
            ("point", "Does it need to be online at all?", "Turn off remote access and cloud features you do not "
             "use. A camera that only records to a memory card is harder to reach from outside."),
            ("point", "Where does it sit on my network?", "Put smart gadgets on your guest network, as we "
             "described in Part 4, so that a hacked TV cannot reach your work laptop."),
            ("h", "What Will Not Change"),
            "It is easy to feel that security is a race we can never win. But look back at the attacks in this "
            "series. Most of them, old or new, still depend on a handful of weaknesses: a stolen or guessed "
            "password, a person rushed into acting, a missing update, a setting left open, or data with no "
            "backup. The tools change. The weak points stay remarkably familiar.",
            "That means the habits you have built through these ten parts will keep paying off. A passkey or "
            "an authenticator app defeats much of what AI-written phishing can do. A habit of verifying requests "
            "defeats the cloned voice. Automatic updates bring you the new post-quantum locks. A guest network "
            "contains the hacked gadget. An offline backup turns ransomware into a bad day instead of a "
            "catastrophe.",
            ("h", "Looking Back on Season One"),
            "Over ten weeks, we have walked from the basics to the frontier. We learned how attacks unfold, then "
            "protected our accounts with strong passwords, passkeys and multi-factor authentication. We studied "
            "how scammers play on emotion, secured the home router and survived a ransomware scenario. We "
            "tidied up our cloud accounts, looked at how apps get hacked, met the idea of zero trust and wrote "
            "a plan for when things go wrong. Today we looked ahead.",
            "If you followed the action plans, your digital life is already far safer than most. If you skipped "
            "a few, that is fine. Pick one part, do its action plan this week, and come back for the next one later.",
            ("h", "Your Part 10 Action Plan"),
            ("point", "Agree on a family or office code word", "Choose a word or question that only your circle "
             "knows, to use whenever a voice or video call asks for money urgently."),
            ("point", "Set an AI rule for yourself", "Decide which information you will never paste into an AI "
             "tool, such as IDs, client lists and anything marked confidential, and follow your office policy."),
            ("point", "Audit one smart device", "Change its default password, update its software, turn off "
             "features you do not use and move it to your guest network."),
            "Thank you for reading the first season of this series. Share it with one person who would benefit, "
            "especially someone who handles money, records or the accounts of an elderly parent.",
            ("cta", "Start again with Part 1", "/blog/cybersecurity-part-1-how-cyberattacks-work/"),
            ("ask", "Which part of this series helped you most, and what topic should Season Two cover? I would "
             "love to hear from you."),
        ],
    },
    {
        "date": "January 2, 2027",
        "title": "Cybersecurity Series, Part 9: Incident Response, or What to Do When Something Goes Wrong",
        "slug": "cybersecurity-part-9-incident-response",
        "category": "security",
        "summary": "What to do in the first hour after a hacked account, a lost phone, a scam transfer or an office "
                   "breach, how to keep evidence intact, where to report in the Philippines, and how to write a "
                   "one-page response plan before you need it.",
        "publish_on": "2027-01-02 22:00",
        "body": [
            "Most offices hold fire drills. People know where the exits are, who carries the logbook and where to "
            "gather outside. Very few offices, and even fewer families, have ever practiced what to do when a "
            "computer is hacked, an account is taken over or money is sent to a scammer. When it happens, people "
            "improvise, and under stress, improvising often makes things worse.",
            "Part 9 of this series is about incident response: the calm, ordered steps that limit the damage when "
            "something goes wrong. You do not need to be a technical expert to follow them. You need a plan that "
            "is written down before the bad day arrives.",
            ("h", "What Counts as an Incident?"),
            "A security incident is any event that threatens the confidentiality, integrity or availability of "
            "information or systems. Put more simply: someone saw what they should not see, changed what they "
            "should not change, or stopped you from using what you need. Examples include:",
            ("point", "For individuals", "A hacked email or social media account, a lost or stolen phone, a "
             "transfer to a scammer, or a strange login alert you did not cause."),
            ("point", "For offices", "Malware on a work computer, a ransomware note, a misdirected email containing "
             "personal data, a lost laptop or flash drive, or a staff account used from an unknown place."),
            "Not every alert is an incident. A login warning might be you on a new phone. But every alert deserves "
            "a quick check, because the cost of ignoring a real one is far higher than the cost of checking a "
            "false one.",
            ("h", "How the Professionals Think About It"),
            "The United States National Institute of Standards and Technology (NIST) publishes one of the most "
            "widely used guides on this subject, Special Publication 800-61. Its third revision, released in April "
            "2025, links incident response to the six functions of the NIST Cybersecurity Framework 2.0: Govern, "
            "Identify, Protect, Detect, Respond and Recover. The message is that response does not start when the "
            "alarm rings. It starts with preparation and ends with lessons that make the next incident less likely.",
            "For everyday use, I find it easier to think in six plain steps:",
            ("point", "Prepare", "Know your important accounts and systems, keep backups, and write down who to call."),
            ("point", "Notice", "Pay attention to warnings, odd behavior and reports from others."),
            ("point", "Contain", "Stop the damage from spreading: disconnect, lock, freeze."),
            ("point", "Clean up", "Remove the attacker's access, such as changed passwords, removed malware and closed doors."),
            ("point", "Recover", "Restore services and data from trusted sources, then watch closely for a while."),
            ("point", "Learn", "Ask what happened and what would have stopped it, then fix that."),
            ("h", "The First Hour: Personal Emergencies"),
            "Here is what to do in the first hour for the situations people meet most often.",
            ("point", "Your email or social media account was taken over", "Use the service's official recovery "
             "page to regain access. Change the password to a new, unique one, sign out all other sessions and "
             "turn on multi-factor authentication. Check recovery email, phone numbers and forwarding rules, "
             "because attackers often change these to come back later. Warn your contacts not to act on messages "
             "sent while you were locked out."),
            ("point", "Your phone was lost or stolen", "Use Find My on iPhone or Find My Device on Android to lock "
             "or erase it. Call your mobile network to block the SIM so that one-time PINs cannot be received. "
             "Contact your bank and e-wallet providers to secure your accounts from another device."),
            ("point", "You sent money to a scammer", "Call your bank or e-wallet provider immediately through its "
             "official hotline or app, and ask them to flag and hold the transaction. Speed matters. The "
             "Anti-Financial Account Scamming Act (Republic Act No. 12010) allows financial institutions to "
             "temporarily hold funds involved in a suspected scam while it is checked. Then report it to the "
             "authorities."),
            ("point", "You clicked a bad link or opened a bad file", "Disconnect from the internet, run a full "
             "security scan, and change the passwords of any account you typed in after clicking, using a "
             "different, clean device."),
            ("h", "The First Hour: Office Incidents"),
            "In an office, the most important rule is to report quickly and avoid the urge to clean up quietly. "
            "Staff sometimes hide a mistake out of embarrassment, and every hour of silence gives an attacker more "
            "time. A healthy office treats an honest early report as a good deed, not a confession.",
            ("point", "Isolate, do not destroy", "Unplug the network cable or turn off Wi-Fi on the affected "
             "computer. If possible, leave it switched on, because evidence in its memory disappears when it is "
             "turned off."),
            ("point", "Call the right people", "Tell your IT team or provider and your supervisor at once. If "
             "personal data may be involved, alert your Data Protection Officer."),
            ("point", "Write things down", "Note the time, what you saw, what you clicked and who you told. "
             "Photograph error messages or ransom notes with a phone."),
            ("point", "Do not contact the attacker", "Do not reply to ransom notes or extortion messages on your own."),
            ("h", "A Little About Digital Forensics"),
            "Digital forensics is the careful collection and study of electronic evidence. It answers questions "
            "such as how the attacker got in, what they touched and whether data left the building. You do not have "
            "to be an investigator, but you can avoid destroying the clues that investigators need.",
            "Think of a crime scene. Moving things around, wiping surfaces or throwing away items makes the "
            "investigation harder. The same is true for computers. Reinstalling the operating system, deleting "
            "suspicious files or clearing browser history may feel like fixing the problem, but it can erase the "
            "evidence of how it happened. Professionals copy the data first, record a digital fingerprint of each "
            "copy, called a hash, to prove nothing was changed, and keep a record of who handled the evidence and "
            "when. This record is known as the chain of custody, and it matters if the case reaches a court.",
            "Two simple habits make any investigation easier: keep the clocks of your computers and devices set to "
            "the correct time automatically, and make sure important systems keep logs of logins and changes. "
            "Without accurate times and logs, reconstructing what happened is like auditing a cashbook with "
            "missing pages.",
            ("quote", "The worst time to look for the fire exit is when the room is already full of smoke."),
            ("h", "Where to Report in the Philippines"),
            "Reporting helps you, and it helps authorities connect cases and warn others. These are the main "
            "channels:",
            ("point", "Cybercrime Investigation and Coordinating Center (CICC)", "Call the Inter-Agency Response "
             "Center hotline 1326 for scams and other cybercrimes."),
            ("point", "PNP Anti-Cybercrime Group and NBI Cybercrime Division", "Both investigate cybercrimes and "
             "accept complaints from the public."),
            ("point", "Your bank or e-wallet provider", "Report fraud on your account through official channels "
             "only, never through links in a message."),
            ("point", "The National Privacy Commission (NPC)", "Organizations that handle personal data have "
             "specific duties. Under the NPC's breach rules, a personal information controller must notify the "
             "Commission within 72 hours of learning of a breach that requires notification, such as one "
             "involving sensitive personal information that could lead to identity fraud, and must also inform "
             "the affected people."),
            ("h", "Talking About It Honestly"),
            "How an organization communicates after an incident shapes how much trust it keeps. People forgive "
            "mistakes more readily than they forgive silence or spin. A good notice explains what happened in "
            "plain language, what information was involved, what the organization is doing about it, and what "
            "affected people should do to protect themselves. It gives a contact person and promises updates, "
            "then keeps that promise.",
            ("h", "Learning Without Blame"),
            "After the incident is closed, hold a short review. The goal is not to find someone to punish. It is to "
            "find the weak point that let the incident happen and fix it. Ask four questions: What happened? Why "
            "did it work? What helped us respond? What would we change? Then assign each improvement to a person "
            "with a date, just as you would follow up on audit findings.",
            "A useful way to practice is a tabletop exercise. Gather the key people for an hour, describe a made-up "
            "scenario, such as \"the collection system shows a ransom note at 8 am on a Monday,\" and walk through "
            "what each person would do. The gaps appear quickly: nobody knows the IT provider's after-hours "
            "number, or the backups are kept on the same network. Finding those gaps in a meeting room is much "
            "cheaper than finding them during a real attack.",
            ("h", "Your Part 9 Action Plan"),
            ("point", "Write a one-page plan", "List your important accounts or systems, where the backups are, "
             "and who to call, with phone numbers for your bank, mobile network, IT support and the CICC hotline 1326."),
            ("point", "Store it where you can reach it", "Keep a printed copy, because a hacked computer or a "
             "lost phone may be exactly what you cannot use."),
            ("point", "Run a 30-minute drill", "Pick one scenario from this post and talk through it with your "
             "family or team. Fix the first gap you find."),
            ("cta", "Read Part 10: AI, Quantum and What Comes Next", "/blog/cybersecurity-part-10-future-threats/"),
            ("ask", "Has your office ever run a cybersecurity drill? Tell me what surprised you most."),
        ],
    },
    {
        "date": "December 26, 2026",
        "title": "Cybersecurity Series, Part 8: Zero Trust, or Why Every Door Gets Checked",
        "slug": "cybersecurity-part-8-zero-trust",
        "category": "security",
        "summary": "Why the old idea of a safe inside network no longer works, what zero trust really means in "
                   "plain language, how it echoes the internal controls of a well-run treasury, and simple ways to "
                   "apply it at home and in a small office.",
        "publish_on": "2026-12-26 22:00",
        "body": [
            "For a long time, computer security was built like an old fortress. There was a strong wall around "
            "the office network, with firewalls at the gate. Anyone outside was suspicious. Anyone inside, connected "
            "to the office network, was trusted. If you were at your desk, you could reach almost every shared "
            "folder and system in the building.",
            "That model has two problems. First, the wall has too many openings now. People work from home, "
            "use phones, log in to cloud services and connect from coffee shops. Second, and more serious, once "
            "an attacker gets inside the wall, through one phished password or one infected laptop, the fortress "
            "model lets them walk freely from room to room. Many of the ransomware attacks we discussed in Part 5 "
            "spread exactly this way.",
            "Part 8 of this series is about the answer that security experts have worked toward for more than a "
            "decade: zero trust.",
            ("h", "What Zero Trust Means"),
            "Zero trust is often summed up as \"never trust, always verify.\" It does not mean distrusting your "
            "colleagues or your family. It means that a system should not grant access just because a request comes "
            "from a familiar place. Every request to use something important, whether it comes from inside the "
            "office or outside, should be checked: who is asking, from what device, for what, and does it make sense "
            "right now?",
            "The term was popularized around 2010 by John Kindervag, then an analyst at the research firm Forrester. "
            "Google described its own version, called BeyondCorp, in 2014, after moving its employees away from "
            "relying on the internal network for trust. In August 2020, NIST published Special Publication 800-207, "
            "Zero Trust Architecture, which has become a common reference. In 2021, a United States executive order "
            "directed federal agencies to move toward zero trust, and the idea has since spread to governments and "
            "companies around the world.",
            ("h", "The Core Ideas in Plain Words"),
            "NIST lists seven tenets of zero trust. Stripped of technical terms, they come down to a few ideas "
            "that anyone can understand:",
            ("point", "Location is not proof", "Being on the office Wi-Fi or inside the building does not make a "
             "request safe. Every connection is treated as if it could be hostile, and data is protected wherever "
             "it travels."),
            ("point", "Check every time it matters", "Access is granted for one session or task, not forever. When "
             "you return tomorrow, or ask for something more sensitive, you are checked again."),
            ("point", "Give the least access needed", "A person or program gets only what it needs to do its job, "
             "for as long as it needs it. A clerk who encodes payments does not need to approve them."),
            ("point", "Look at the whole picture", "The decision considers who you are, the health of your device, "
             "the time, the place and whether the request fits your normal pattern."),
            ("point", "Assume a breach is possible", "Design systems so that if one account or computer is "
             "compromised, the damage stays small and is noticed quickly."),
            ("point", "Watch and improve", "Collect information about devices, logins and traffic, and use it to "
             "catch problems and tighten the rules over time."),
            ("h", "Treasury Work Already Knows This Idea"),
            "When I first studied zero trust, it felt familiar. Good public financial management has followed a "
            "similar philosophy for a long time, under the name of internal control.",
            "Consider how a well-run treasury handles money. The person who collects payments is not the same "
            "person who records them in the books, and neither is the person who approves disbursements. This is "
            "segregation of duties. The vault does not open just because someone works in the building. Access is "
            "limited to specific people, often requires two of them together, and every opening is logged. Cash "
            "counts happen regularly and sometimes without warning. Nobody takes these controls as an insult. "
            "They protect honest employees as much as they protect public funds.",
            "Zero trust applies the same discipline to digital systems. It replaces \"she works here, so she can see "
            "everything\" with \"she can see what her job requires, and the system confirms it is really her.\"",
            ("quote", "Trust is not a feeling we give to a network. It is a decision the system makes again "
             "every time it matters."),
            ("h", "What It Looks Like in Practice"),
            "Large organizations build zero trust with identity platforms, device management and careful network "
            "design. The United States Cybersecurity and Infrastructure Security Agency (CISA) describes the work "
            "in five areas, which it calls pillars: identity, devices, networks, applications and workloads, and "
            "data. Translated into everyday terms, it often looks like this:",
            ("point", "Identity", "Every person has their own account, protected by multi-factor authentication, "
             "ideally a phishing-resistant method such as a passkey or security key. No shared logins."),
            ("point", "Devices", "Only devices that are updated, protected and known to the organization can reach "
             "sensitive systems."),
            ("point", "Networks", "The network is divided into smaller zones, so that a problem in one area cannot "
             "easily spread to another."),
            ("point", "Applications", "Each application checks permissions on its own, every time, instead of "
             "trusting anyone who reaches it."),
            ("point", "Data", "Sensitive files are labeled, encrypted and shared only with the people who need them, "
             "with a record of who opened what."),
            ("h", "Zero Trust for a Small Office"),
            "You do not need a big budget to start. Many of the most valuable steps cost little or nothing:",
            ("point", "One person, one account", "Stop sharing a single login for the office computer, the email "
             "or a government portal. Individual accounts make actions traceable and access easy to remove."),
            ("point", "MFA everywhere", "Turn on multi-factor authentication for email, cloud storage, banking and "
             "every system that holds money or personal data."),
            ("point", "Separate daily and admin accounts", "Do everyday work with an ordinary account. Use an "
             "administrator account only when installing or changing something."),
            ("point", "Review access when people move", "When an employee transfers, retires or resigns, remove or "
             "change their access on the same day. Old accounts are favorite doors for attackers."),
            ("point", "Separate the networks", "Keep guests, personal phones and smart devices off the network that "
             "holds your financial and records systems."),
            ("point", "Approve money in two steps", "Any change in payment details or any unusual transfer should "
             "require confirmation by a second person through a separate channel."),
            ("h", "Zero Trust at Home"),
            "Families can borrow the same thinking. Give each family member their own user account on shared "
            "computers, so a child's game download cannot touch a parent's work files. Use the guest network from "
            "Part 4 for visitors and smart gadgets. Check which apps can see your location, contacts and photos, and "
            "remove access that is not needed. And treat every unexpected request for money or codes the same way, "
            "even when it seems to come from someone you love: verify it through a channel you already trust.",
            ("h", "Common Myths"),
            ("point", "\"Zero trust is a product you can buy\"", "Vendors sell tools that help, but zero trust is "
             "an approach. No single box or app makes an organization zero trust."),
            ("point", "\"It means we do not trust our people\"", "It means systems stop assuming. Clear rules and "
             "checks actually protect staff from being blamed for an attacker's actions."),
            ("point", "\"It is all or nothing\"", "It is a journey. Most organizations start with identity and "
             "multi-factor authentication, then improve step by step."),
            ("point", "\"It makes work slower\"", "Done well, it can make work smoother. Signing in once with a "
             "passkey on a trusted device is faster than juggling many passwords and a VPN."),
            ("h", "Your Part 8 Action Plan"),
            ("point", "Count your shared logins", "List every account that more than one person uses. Plan to "
             "replace each one with individual accounts."),
            ("point", "Do an access review", "For your email, cloud folders or office systems, check who has "
             "access. Remove anyone who no longer needs it."),
            ("point", "Add a second check for money", "Agree with your family or team that changes to bank details "
             "or urgent transfers always need a call-back on a known number."),
            ("cta", "Read Part 9: Incident Response", "/blog/cybersecurity-part-9-incident-response/"),
            ("ask", "Does your office still use a shared login for any important system? What makes it hard to "
             "change? I would like to know."),
        ],
    },
    {
        "date": "December 19, 2026",
        "title": "Cybersecurity Series, Part 7: Why Apps Get Hacked, Explained with the OWASP Top 10",
        "slug": "cybersecurity-part-7-why-apps-get-hacked",
        "category": "security",
        "summary": "A plain-language tour of the ten most serious risks in web applications, as listed in the OWASP "
                   "Top 10:2025, with everyday examples, questions to ask before your office buys a system, and "
                   "habits for anyone who builds software.",
        "publish_on": "2026-12-19 22:00",
        "body": [
            "Every app you use was written by people. Your bank's mobile app, the online payment page of your "
            "local government, the school portal and the delivery app all started as lines of code typed by "
            "developers working under deadlines. People make mistakes, and some of those mistakes become doors "
            "that attackers can open.",
            "You do not need to be a programmer to understand where those doors usually are. In Part 7 of this "
            "series, we take a guided tour of the most common weaknesses in web applications. If you use apps, this "
            "will help you understand the news. If your office buys or runs a system, it will help you ask better "
            "questions. And if you build software, as I do for treasury work, it is a checklist worth keeping close.",
            ("h", "What Is OWASP?"),
            "The OWASP Foundation, whose name stands for Open Worldwide Application Security Project, is a "
            "nonprofit community that produces free guides and tools for building safer software. Its best-known "
            "work is the OWASP Top 10, an awareness document that ranks the most critical security risks in web "
            "applications. It is updated every few years based on data from real applications and a survey of "
            "practitioners. The current edition is the OWASP Top 10:2025.",
            "Here are the ten risks, explained with everyday examples.",
            ("h", "1. Broken Access Control"),
            "This is the top risk, and it is about permissions. The app checks who you are, but forgets to check "
            "what you are allowed to see or do. A classic example: you view your own receipt at an address that "
            "ends in a number, such as receipt 1045. You change it to 1046 and see a stranger's receipt, with their "
            "name and address. The system should have refused. It is like a records room where the clerk checks your "
            "ID at the door, but then lets you open any cabinet inside.",
            ("h", "2. Security Misconfiguration"),
            "The software may be fine, but it was set up badly. Default administrator passwords are left unchanged, "
            "detailed error messages reveal how the system works inside, unnecessary features are switched on, or a "
            "storage folder full of documents is left open to the internet. Many data leaks reported in the news "
            "come not from clever hacking but from a setting nobody checked.",
            ("h", "3. Software Supply Chain Failures"),
            "Modern apps are built from many ready-made parts, called libraries or packages, written by other "
            "people. That saves time, but every part is a dependency you must trust. If one of those parts has a "
            "flaw, is outdated or is secretly replaced with a malicious version, every app that uses it is at risk. "
            "It is like a treasury buying accountable forms from a supplier: if the supplier is careless or "
            "dishonest, your controls are weakened before you even begin.",
            ("h", "4. Cryptographic Failures"),
            "This is about protecting data with encryption, or failing to. Examples include a site that does not use "
            "HTTPS, passwords stored in a form that can be read or easily reversed, or sensitive records saved "
            "without encryption. When such a database is stolen, the attacker can read everything at once.",
            ("h", "5. Injection"),
            "An app takes what you type into a form and passes it to a database or another program. If it does not "
            "handle that input carefully, an attacker can type something that the program mistakes for a command. "
            "The best-known type is SQL injection, where carefully crafted text in a search box or login form tricks "
            "the database into revealing or changing records. Developers prevent it by keeping data and commands "
            "strictly separate, using what are called parameterized queries.",
            ("h", "6. Insecure Design"),
            "Some weaknesses are not coding mistakes but planning mistakes. Imagine a password-reset page that lets "
            "anyone guess a six-digit code as many times as they like. Every line of code may work exactly as "
            "written, yet the design is unsafe because nobody asked, \"How would someone abuse this?\" Thinking "
            "about abuse early, sometimes called threat modeling, is far cheaper than fixing a design later.",
            ("h", "7. Authentication Failures"),
            "These are weaknesses in how an app confirms who you are. It might allow very weak passwords, never "
            "lock out repeated guesses, fail to offer multi-factor authentication, or keep you signed in long after "
            "you should have been logged out. Part 2 of this series explained why strong sign-in matters. This "
            "category is the developer's side of the same story.",
            ("h", "8. Software or Data Integrity Failures"),
            "An app trusts updates, files or data without checking that they are genuine and unaltered. A program "
            "that downloads updates without verifying their digital signature, for example, could be tricked into "
            "installing malware. In financial terms, it is like accepting a check without verifying the signature.",
            ("h", "9. Security Logging and Alerting Failures"),
            "If an app does not record important events, such as logins, failed attempts and changes to records, or "
            "if nobody is alerted when something suspicious happens, attacks can continue for weeks unnoticed. An "
            "unlogged system is like a vault without a logbook: when money goes missing, there is no trail to "
            "follow.",
            ("h", "10. Mishandling of Exceptional Conditions"),
            "This new category covers what happens when things go wrong: a network error, a missing value, an "
            "unexpected input. A well-built app fails safely. It shows a polite message, keeps the data consistent "
            "and denies access when in doubt. A poorly built one might crash and show internal details, leave a "
            "transaction half done, or, worst of all, let the user through because the check itself failed.",
            ("quote", "Most security failures are not genius attacks. They are ordinary mistakes that nobody "
             "checked for."),
            ("h", "What App Users Can Do"),
            "You cannot fix an app's code, but you can lower your risk:",
            ("point", "Install apps only from official stores", "Use Google Play, the App Store or the official "
             "website of the bank or agency. Avoid installing app files sent through chat."),
            ("point", "Keep apps updated", "Updates often fix exactly the kinds of flaws described above."),
            ("point", "Give each app the least it needs", "A flashlight app does not need your contacts or "
             "location."),
            ("point", "Report what looks wrong", "If an app ever shows you someone else's information, stop, take a "
             "screenshot and report it to the provider through official channels. Do not explore further."),
            "That last point matters. Testing or probing systems you do not own, without permission, can be illegal "
            "under the Cybercrime Prevention Act of 2012 (Republic Act No. 10175), even if your intentions are good. "
            "Report it and let the owner fix it.",
            ("h", "Questions to Ask Before Your Office Buys a System"),
            "Offices that buy software, whether for collections, payroll or records, can use the OWASP Top 10 as a "
            "checklist. Before signing, ask the supplier:",
            ("point", "Access control", "Can each user be limited to only the functions and records their job needs? "
             "Can we see who did what, and when?"),
            ("point", "Sign-in", "Does the system support multi-factor authentication? How are passwords stored?"),
            ("point", "Updates and components", "How often do you release security updates, and how do you keep "
             "third-party components current?"),
            ("point", "Testing", "Has the system been tested for security by an independent party? Can you share a "
             "summary of the results?"),
            ("point", "Data protection", "Is data encrypted when stored and when sent? Where are the backups, and how "
             "fast can we restore?"),
            ("point", "Logging and support", "Are important actions logged and kept? Who do we call if we suspect a "
             "breach, and how fast will you respond?"),
            ("h", "For Those Who Build"),
            "If you write code, even small tools for your own office, a few habits prevent most of these problems. "
            "Check permissions on the server for every request, not only by hiding buttons on the screen. Use "
            "parameterized queries for every database call. Store passwords only with a modern password-hashing "
            "method designed for the purpose, such as bcrypt or Argon2. Keep your dependencies updated and remove the ones you do not "
            "use. Log important events, and decide in advance what the system should do when something fails. "
            "Most of all, ask \"How could this be abused?\" before you write the first line.",
            ("h", "Your Part 7 Action Plan"),
            ("point", "Review your app permissions", "On your phone, open the permission settings and remove "
             "location, contacts, camera and microphone access from apps that do not need them."),
            ("point", "Delete apps you no longer use", "Every unused app is old code that may never be updated again."),
            ("point", "Share the checklist", "If your office is planning to buy or upgrade a system, pass the six "
             "questions above to the people handling the procurement."),
            ("cta", "Read Part 8: Zero Trust", "/blog/cybersecurity-part-8-zero-trust/"),
            ("ask", "Has an app ever shown you information that clearly was not yours? How did the provider respond?"),
        ],
    },
    {
        "date": "December 12, 2026",
        "title": "Cybersecurity Series, Part 6: Keeping Your Life in the Cloud Safe and Private",
        "slug": "cybersecurity-part-6-cloud-and-privacy",
        "category": "security",
        "summary": "Who is responsible for keeping your cloud files safe, why a single \"anyone with the link\" "
                   "setting can expose a whole office, how to check which apps can reach your accounts, and the "
                   "privacy rights every Filipino has under the Data Privacy Act.",
        "publish_on": "2026-12-12 22:00",
        "body": [
            "Your family photos, your scanned IDs, the spreadsheets from work and years of messages probably live "
            "somewhere you have never seen: in the cloud. There is a well-known joke among IT people that \"the "
            "cloud is just someone else's computer.\" It is a joke, but it carries a useful truth. When you store "
            "something online, you are trusting a company's computers, and you are also trusting your own settings "
            "and habits.",
            "In Part 6 of this series, we look at how to keep your cloud accounts secure and how to protect your "
            "privacy in a world where so much of our lives is stored, shared and analyzed online.",
            ("h", "What \"the Cloud\" Really Means"),
            "When you save a file to Google Drive, OneDrive, iCloud or Dropbox, it is copied to large data "
            "centers owned by those companies. The same is true when you post on social media, back up your phone "
            "or use an online accounting tool. The benefits are real: your files survive a lost phone, you can "
            "work from anywhere and you can share a document in seconds.",
            "The big providers invest heavily in security. Their data centers have guards, redundant power, "
            "specialist staff and constant monitoring, far beyond what a small office could afford. So why do "
            "cloud accounts get breached at all? The answer lies in a principle called shared responsibility.",
            ("h", "Shared Responsibility: Their Part and Your Part"),
            "Cloud security is divided between the provider and the customer. The provider is responsible for the "
            "security of the cloud: the buildings, the servers, the networks and the software that runs the service. "
            "You are responsible for security in the cloud: who can sign in to your account, what you upload, how "
            "you share it and which apps you connect to it.",
            "Think of a bank's safety deposit box. The bank guards the vault, the walls and the doors. But if you "
            "hand a copy of your key to a stranger, or leave the box open while you step out, the bank's strong "
            "vault will not help you.",
            "Most cloud breaches happen on the customer's side of that line. The research firm Gartner once "
            "predicted that through 2025, 99% of cloud security failures would be the customer's fault. Whatever the "
            "exact number, the lesson holds: the weak point is usually not the provider's data center. It is a "
            "weak password, a missing second factor or a careless sharing setting.",
            ("h", "The Most Common Cloud Mistakes"),
            ("point", "A weak account", "If your cloud account uses a reused password without multi-factor "
             "authentication, everything in it is one leaked password away from a stranger. Part 2 showed how to "
             "fix this with a password manager and passkeys."),
            ("point", "\"Anyone with the link\" sharing", "This setting lets anyone who has the link open the file, "
             "with no sign-in. Links get forwarded, pasted into group chats and posted by mistake. A spreadsheet "
             "of names, addresses and ID numbers shared this way is effectively public."),
            ("point", "Sharing that never ends", "Files shared years ago with former colleagues, old suppliers or "
             "a personal email address often stay shared forever unless someone removes the access."),
            ("point", "Connected apps you forgot", "Quizzes, photo editors, browser add-ons and productivity tools "
             "often ask to \"sign in with Google\" or Facebook and request access to your files or contacts. Many "
             "keep that access long after you stop using them."),
            ("point", "Thinking sync is a backup", "Syncing copies changes everywhere, including deletions and files "
             "scrambled by ransomware. A synced folder is convenient, but it is not a separate backup."),
            ("h", "Share Like a Careful Records Officer"),
            "Good records management never hands out original documents to anyone who asks. Copies go to the "
            "people who have a right to them, each release is logged, and confidential records stay locked. "
            "Sharing files online deserves the same care.",
            ("point", "Share with names, not links", "Choose \"Restricted\" or its equivalent and add the specific "
             "people who need the file. Use public links only for material you would be comfortable posting on a "
             "bulletin board."),
            ("point", "Give the lowest access that works", "If someone only needs to read, give view access, not edit. "
             "Many services also let you turn off downloading, printing and copying for viewers."),
            ("point", "Set an expiry date", "Several services let you make access expire automatically. When I share "
             "a document for review, I give view-only access to the named person and let the access end on its own "
             "after a few days."),
            ("point", "Review shared files every few months", "Look for files shared with \"anyone with the link\" "
             "or with people outside your office, and remove what is no longer needed."),
            ("h", "Check Which Apps Can Reach Your Accounts"),
            "Over the years, most of us have clicked \"Allow\" for many apps. It is worth reviewing them. In a "
            "Google Account, open the Security section and look for \"Your connections to third-party apps and "
            "services.\" There you can see which apps can access your account and what each one can do, and remove "
            "any you do not recognize or no longer use. Microsoft, Apple and Facebook accounts have similar pages "
            "in their security or privacy settings.",
            "Pay special attention to any app that can read your email or your files. Email access is the master "
            "key to most of your accounts, because password reset links usually arrive there.",
            ("quote", "Every \"Allow\" you click is a key you hand out. Count your keys once in a while."),
            ("h", "Your Phone Knows a Lot About You"),
            "Privacy is not only about files in the cloud. The apps on your phone can collect your location, "
            "contacts, photos and even what you say near the microphone, depending on the permissions you give "
            "them. Much of this data is used to show targeted advertising, and some may be shared with partners.",
            "On an iPhone, open Settings, then Privacy and Security, to see which apps can use your location, "
            "contacts, photos, camera and microphone. On Android, look for the Permission manager in the Security "
            "and privacy settings; the exact menu differs by phone brand. Ask a simple question for each app: does "
            "it really need this to do its job? A calculator does not need your location. A messaging app may need "
            "your microphone, but only while you are recording.",
            ("h", "Think Before You Post"),
            "Small details in posts can add up to a full profile for a scammer or stalker:",
            ("point", "IDs and documents", "Never post photos of your IDs, passports, boarding passes or receipts "
             "with barcodes or QR codes. They contain more information than you might think."),
            ("point", "Location and routine", "Posting \"on vacation for two weeks\" while you are away tells "
             "people your house is empty. Consider posting travel photos after you return."),
            ("point", "Children's details", "School uniforms, school names and daily routines can reveal where a "
             "child can be found. Keep those posts to a private circle, or skip them."),
            ("point", "Answers to security questions", "Your first pet, your mother's maiden name and your first "
             "school are common security questions. Fun quizzes that ask for them deserve suspicion."),
            ("h", "Your Rights Under the Data Privacy Act"),
            "In the Philippines, the Data Privacy Act of 2012 (Republic Act No. 10173) protects personal "
            "information held by government offices and private companies alike. It is enforced by the National "
            "Privacy Commission (NPC). As a data subject, you have rights that many people never use, including:",
            ("point", "The right to be informed", "You should be told when your personal data is being collected "
             "and processed, and for what purpose."),
            ("point", "The right to access and correct", "You can ask an organization what personal data it holds "
             "about you, and ask it to correct mistakes."),
            ("point", "The right to object and to erasure", "In certain cases, you can object to processing and ask "
             "that your data be blocked or removed, such as when it is no longer needed or was collected unlawfully."),
            ("point", "The right to complain and claim damages", "You can file a complaint with the NPC and may be "
             "entitled to damages if your data is misused."),
            "These rights also remind those of us who handle other people's data at work of our duty. Every "
            "taxpayer list, payroll file and application form is someone's personal information, entrusted to us "
            "for a specific purpose.",
            ("h", "Your Part 6 Action Plan"),
            ("point", "Secure your main cloud account", "Make sure it has a unique password and multi-factor "
             "authentication, ideally a passkey."),
            ("point", "Hunt for public links", "Search your cloud storage for files shared with \"anyone with the "
             "link\" and switch them to named people, or stop sharing them."),
            ("point", "Remove one forgotten app", "Open the third-party connections page of your Google, Microsoft "
             "or Facebook account and remove at least one app you no longer use."),
            ("cta", "Read Part 7: Why Apps Get Hacked", "/blog/cybersecurity-part-7-why-apps-get-hacked/"),
            ("ask", "How many forgotten apps did you find connected to your accounts? Tell me the oldest one."),
        ],
    },
    {
        "date": "December 5, 2026",
        "title": "Cybersecurity Series, Part 5: Inside a Ransomware Attack",
        "slug": "cybersecurity-part-5-ransomware",
        "category": "security",
        "summary": "How ransomware gangs break in, steal before they lock, and pressure victims to pay, what the "
                   "PhilHealth attack of 2023 taught the country, and the backup habit that takes away their leverage.",
        "publish_on": "2026-12-05 22:00",
        "body": [
            "Imagine coming to the office on a Monday and finding every computer showing the same message: your files "
            "are encrypted, your records have been copied, and you have a few days to pay before everything is "
            "published online. Nothing opens. The collection system is down. The queue at the counter grows, and "
            "nobody can issue a receipt.",
            "This is not a scene from a movie. In September 2023, the Philippine Health Insurance Corporation "
            "(PhilHealth) went through a version of it. In Part 5 of this series, we look inside a modern ransomware "
            "attack: how it starts, why it is built to make you pay, and what ordinary people and offices can do so "
            "that a ransom note becomes an inconvenience instead of a disaster.",
            ("h", "From Locked Screens to a Criminal Industry"),
            "Early ransomware was crude. A virus scrambled the files on one computer and asked for a few hundred "
            "dollars. If you paid, you might get a key. If you had a copy of your files somewhere else, you could "
            "ignore the note and start over.",
            "Criminals learned from that. Today, many ransomware groups run like businesses. One group writes and "
            "maintains the malware, runs the payment sites and even handles \"customer service\" with victims. Other "
            "criminals, called affiliates, rent the malware, break into targets, and share the ransom with the "
            "developers. This model is known as ransomware-as-a-service. It lowered the skill needed to launch an "
            "attack, and it is one reason ransomware remains one of the most common serious threats. Verizon's 2025 "
            "Data Breach Investigations Report found ransomware in 44% of the breaches it studied, up from 32% a year "
            "earlier.",
            ("h", "Double Extortion: Steal First, Then Lock"),
            "The biggest change came when attackers realized that good backups were ruining their business. If a "
            "victim could restore everything, why pay? So they began to copy the data out before encrypting it. Now "
            "the note carries two threats: pay to unlock your files, and pay again, or at the same time, to stop us "
            "from publishing what we took. This is called double extortion.",
            "Some groups go further, with what is sometimes called triple extortion. They contact the victim's "
            "clients, patients or partners directly, or flood the victim's website with traffic to add pressure. The "
            "goal is always the same: make paying feel like the fastest way to make the pain stop.",
            ("h", "How an Attack Unfolds"),
            "A ransomware attack is rarely a single click that locks everything a minute later. Most follow the "
            "pattern we mapped in Part 1, and they often take days or weeks.",
            ("point", "Getting in", "The usual doors are a phishing email, a stolen password for remote access or a "
             "VPN, or an unpatched device facing the internet, such as a firewall or a file-sharing server."),
            ("point", "Settling in", "The attacker installs remote-control tools so they can come back at will, often "
             "using software that looks like ordinary IT administration."),
            ("point", "Spreading out", "They collect more passwords, especially those of administrators, and move "
             "from the first computer to servers, shared drives and backup systems."),
            ("point", "Stealing", "They quietly copy valuable data to servers they control, sometimes over days, "
             "trying not to cause a spike that someone might notice."),
            ("point", "Disabling recovery", "They delete or encrypt backups they can reach, turn off security "
             "tools and remove the recovery copies that the operating system keeps."),
            ("point", "Striking", "Only then do they launch the encryption, often at night, on a weekend or before a "
             "holiday, when fewer people are watching. Thousands of files can be locked within hours."),
            "Notice that the actual encryption is the last step. Every step before it is a chance to catch the "
            "attacker: an alert on a strange login, a warning about a new administrator account, or a large upload "
            "at midnight.",
            ("h", "A Philippine Lesson: The PhilHealth Attack"),
            "On September 22, 2023, PhilHealth learned that it had been hit by the Medusa ransomware group. Its "
            "website, e-claims system, member portal and collection system went offline, and the agency's initial "
            "investigation found about 72 computers affected. The attackers reportedly demanded US$300,000 and "
            "threatened to release the stolen data.",
            "The government did not pay, in line with its policy. The attackers then published the data online. "
            "PhilHealth later estimated that the personal information of about 13 million to 20 million members may "
            "have been exposed, and the National Privacy Commission looked into the agency's compliance with the "
            "Data Privacy Act.",
            "I do not cite this case to blame anyone. I cite it because it shows two hard truths. First, refusing "
            "to pay is the right policy, but it does not undo a data leak; once the files are copied, the damage "
            "is partly done. Second, the real cost of ransomware is not only the ransom. It is the days of downtime, "
            "the citizens who cannot transact, the overtime, the investigation and the long work of rebuilding trust.",
            ("quote", "Refusing to pay is the right decision. Being able to refuse without fear is the real goal."),
            ("h", "Why Paying Is a Bad Bet"),
            "When the screens go dark, paying can look like the quickest way out. Law enforcement agencies, including "
            "the United States FBI, advise against it, and for good reasons.",
            ("point", "There is no guarantee", "The key may not work well. Decrypting large systems can be slow, and "
             "some files may come back damaged."),
            ("point", "Stolen data stays stolen", "Paying for silence relies on the promise of criminals. Data that "
             "has been copied can be sold or leaked later anyway."),
            ("point", "You become a known payer", "An organization that pays has shown it will pay. It may be "
             "targeted again, sometimes by the same group."),
            ("point", "You fund the next attack", "Every ransom pays for more tools, more affiliates and more "
             "victims."),
            "The encouraging news is that more victims are refusing. Verizon's 2025 report found that 64% of "
            "ransomware victims did not pay, up from 50% two years before, and that the median payment had fallen "
            "to US$115,000. Refusing is easier when you know you can recover.",
            ("h", "The Cure: Backups the Attacker Cannot Touch"),
            "Ransomware turns your own data into a hostage. A good backup takes the hostage away. But it must be a "
            "backup the attacker cannot reach, because modern attackers look for backups first. A practical rule "
            "to follow is often written as 3-2-1-1-0.",
            ("point", "3 copies", "Keep at least three copies of important data: the original and two backups."),
            ("point", "2 kinds of storage", "Store them on at least two different kinds of media, such as your "
             "computer's drive and an external drive."),
            ("point", "1 off-site", "Keep one copy in another place, such as a trusted cloud service or a drive "
             "kept at another building."),
            ("point", "1 offline or unchangeable", "Keep one copy that ransomware cannot alter: a drive that is "
             "unplugged after each backup, or storage set to keep each version unchanged for a fixed period."),
            ("point", "0 surprises", "Test your backups by actually restoring files. A backup you have never "
             "restored is only a hope."),
            "For a household, this can be simple: your laptop, an external drive that you plug in every Sunday and "
            "then unplug, and a cloud backup of your most important folders. For an office, it means scheduled "
            "backups, at least one copy that is offline or locked against changes, and a written plan for how long "
            "a restore takes.",
            "There is a familiar idea from treasury work here. We never keep all the cash in one drawer, and we "
            "do not treat a collection as safe until it is counted, recorded and deposited. Data deserves the same "
            "discipline. A file that exists in only one place is not really safe.",
            ("h", "Making the Attack Harder"),
            "Backups help you recover. These habits help you avoid the attack or catch it early:",
            ("point", "Patch internet-facing devices first", "Firewalls, VPNs and remote access tools are favorite "
             "doors. Apply their security updates as soon as you can."),
            ("point", "Protect remote access with MFA", "Every remote login, for staff and for IT providers, "
             "should need a second factor, as we discussed in Part 2."),
            ("point", "Limit administrator accounts", "Use ordinary accounts for daily work. The fewer people and "
             "computers with full control, the slower an attacker can spread."),
            ("point", "Turn on built-in protection", "Windows has a feature called Controlled Folder Access in "
             "Windows Security that blocks unknown apps from changing protected folders. On a Mac, keep "
             "Time Machine backups going to a drive you disconnect afterward."),
            ("point", "Watch for warning signs", "New administrator accounts, security tools that suddenly switch "
             "off, or large data transfers at odd hours deserve immediate attention."),
            ("h", "If It Happens to You"),
            "If a ransom note appears, do not panic, and do not start deleting things. Disconnect the affected "
            "computer from the network by turning off Wi-Fi or unplugging the network cable. If you can, leave it "
            "switched on, because the evidence in its memory can help investigators. Photograph the ransom note. Tell "
            "your IT team or provider at once. In the Philippines, you can report cybercrime to the Cybercrime "
            "Investigation and Coordinating Center through its hotline 1326, or to the PNP Anti-Cybercrime Group. "
            "If personal data was involved, an organization may also have to notify the National Privacy "
            "Commission and the people affected.",
            ("h", "Your Part 5 Action Plan"),
            ("point", "Set up one automatic backup", "Back up your most important folders to an external drive or a "
             "trusted cloud service, and unplug the drive when the backup ends."),
            ("point", "Restore one file today", "Pick a folder and restore it from your backup. If you cannot, fix "
             "the backup before you need it."),
            ("point", "Turn on ransomware protection", "On Windows, open Windows Security, go to Virus and threat "
             "protection, then Ransomware protection, and turn on Controlled Folder Access. Allow your trusted apps when asked."),
            "With these first five parts, the series has covered the basics most people need: how attacks work, how to protect "
            "your accounts, how to spot a scam, how to secure your home network and how to survive ransomware. "
            "Share these posts with someone who handles money or records, and come back to the action plans every few "
            "months.",
            ("cta", "Read Part 6: Cloud Security and Privacy", "/blog/cybersecurity-part-6-cloud-and-privacy/"),
            ("ask", "Has your office ever tested restoring its backups? I would like to hear how it went."),
        ],
    },
    {
        "date": "November 28, 2026",
        "title": "Cybersecurity Series, Part 4: Securing Your Home and Remote Network",
        "slug": "cybersecurity-part-4-home-network",
        "category": "security",
        "summary": "Your Wi-Fi router is the front door of your digital home. Here is how to lock it, separate your "
                   "smart devices from your work laptop, filter dangerous websites, and understand what a VPN can "
                   "and cannot do.",
        "publish_on": "2026-11-28 22:00",
        "body": [
            "In most homes, the internet arrives through one small box with blinking lights. The technician installs "
            "it, writes the Wi-Fi password on a piece of paper, and leaves. Years later, the same box is still "
            "there, running the same software, with the same admin password printed on its sticker. Behind it are "
            "our phones, our children's tablets, the smart TV, a CCTV camera and the laptop we use for work or for "
            "online banking.",
            "Since the pandemic, many of us also work from home at least part of the time. That means the home router "
            "now protects not only family photos but sometimes office documents, government systems and money. In "
            "Part 4 of this series, we will lock that front door, divide the house into safer rooms, and clear up "
            "some common myths about VPNs.",
            ("h", "Why the Router Matters"),
            "Your router does three jobs at once. It connects your home to your internet provider, it creates the "
            "Wi-Fi network your devices join, and it decides which traffic may come in from the internet. If an "
            "attacker controls it, they can watch or redirect your traffic, send you to fake websites, or use your "
            "connection for their own attacks. Routers are also attractive because owners rarely update them. "
            "Security agencies have repeatedly warned about criminal and state-backed groups taking over old home "
            "and small-office routers to hide their activities.",
            ("h", "Step 1: Lock the Front Door"),
            "Start with the settings page of your router. Its address and default login are usually printed on the "
            "sticker on the device, often an address like 192.168.1.1 or 192.168.0.1. If your router is managed by "
            "your internet provider, some settings may be locked; ask the provider for help, or check whether its "
            "app lets you change them.",
            ("point", "Change the admin password", "The password for the settings page is different from the "
             "Wi-Fi password. Replace the default with a long, unique one and save it in your password manager."),
            ("point", "Update the firmware", "Firmware is the router's software. Look for an update option, or turn "
             "on automatic updates if your router has them. If the maker no longer releases updates for your model, "
             "it is time to replace it."),
            ("point", "Use WPA3 or WPA2", "In the Wi-Fi security setting, choose WPA3 if all your devices support "
             "it, or the mixed WPA2/WPA3 mode if some older ones do not. Never use WEP or an open network."),
            ("point", "Use a strong Wi-Fi password", "A long passphrase of several unrelated words is easy to type "
             "on a phone and hard to guess."),
            ("point", "Turn off WPS", "WPS lets devices join by pressing a button or entering a short PIN. The PIN "
             "method has a long history of weaknesses, and few people need it."),
            ("point", "Turn off UPnP if you can", "UPnP lets devices on your network open doors in your router to "
             "the internet automatically, without asking you. It is convenient for some games and cameras, but a "
             "compromised device can use it too."),
            ("point", "Turn off remote management", "Unless you truly need to change router settings from outside "
             "your home, make sure the settings page cannot be reached from the internet."),
            ("h", "Step 2: Divide the House into Rooms"),
            "Not every device deserves the same trust. A cheap smart plug or an old CCTV camera may never receive a "
            "security update. If it shares a network with your work laptop, a compromised gadget becomes a foothold "
            "next to your most important files. The fix is to separate them, an idea security people call "
            "segmentation. At home, most routers make this easy with a guest network.",
            ("point", "Main network", "Only for the devices you use and trust every day: your phones, laptops and "
             "tablets, kept up to date."),
            ("point", "Smart-device network", "Put smart TVs, cameras, speakers and appliances on the guest network, "
             "or on a separate network if your router supports more than one."),
            ("point", "Visitors", "Give guests the guest network too, ideally with \"client isolation\" turned on so "
             "devices on it cannot see each other."),
            "This is the same thinking behind a treasury vault. The public can reach the counter, but not the vault, "
            "and even staff need a reason and a key to open it. Your network can work the same way.",
            ("h", "Step 3: Let DNS Filter the Bad Sites"),
            "Every time you visit a website, your device first asks a DNS server to turn a name like aumahinay.dev "
            "into a numeric address. It is the internet's phone book. By default, you use the phone book of your "
            "internet provider. You can choose a different one that refuses to look up addresses known to host "
            "malware or phishing pages.",
            "Two free options are widely used. Quad9, run by a non-profit foundation, blocks known malicious domains "
            "at 9.9.9.9. Cloudflare's 1.1.1.1 for Families blocks malware at 1.1.1.2. (The plain 1.1.1.1 address is "
            "fast and private but does not block anything.) You can set these on your router, so every device at "
            "home benefits, or on a single phone or computer.",
            "Modern browsers and phones also support encrypted DNS, called DNS over HTTPS in browsers and Private "
            "DNS on Android. Encryption keeps people on the same network from seeing or tampering with the names you look "
            "up. DNS filtering is not a complete defense, but it quietly stops many bad links before the page even "
            "loads.",
            ("h", "Step 4: The Truth About VPNs"),
            "VPN advertisements promise privacy, safety and anonymity in one click. The reality is narrower. A VPN "
            "creates an encrypted tunnel between your device and the VPN company's server. That is useful, but it "
            "helps with a specific problem.",
            ("point", "What a VPN does", "It hides your traffic from the network you are on, such as hotel or café "
             "Wi-Fi, and from your internet provider. Websites see the VPN's address instead of yours. A company VPN "
            "also lets staff reach office systems safely from outside."),
            ("point", "What a VPN does not do", "It does not stop malware, it does not block phishing, and it does "
             "not make you anonymous when you log in to your own accounts. It also moves your trust from your "
             "internet provider to the VPN company, which can see your traffic instead."),
            "Most websites, including this one, already use HTTPS, which encrypts what you send and receive with "
            "that site. So on a trusted home network, a commercial VPN adds little security. On public Wi-Fi, a "
            "reputable VPN is a reasonable extra layer. When in doubt, your phone's mobile data is often safer than "
            "an unknown hotspot. Be careful with free VPN apps: running a VPN costs money, and some free ones pay "
            "for it with your data.",
            ("h", "Smart Gadgets Need Care Too"),
            "CCTV cameras, smart TVs, baby monitors and Wi-Fi plugs are small computers. Many are sold cheaply, "
            "set up once and forgotten. A few habits reduce their risk:",
            ("point", "Change default passwords", "If a camera or gadget came with a password like admin or 12345, "
             "change it during setup."),
            ("point", "Update or replace", "Install updates through the device's app. If a gadget no longer gets "
             "updates, consider replacing it, especially cameras that face the inside of your home."),
            ("point", "Turn off what you do not use", "Disable remote viewing, voice assistants or cloud features "
             "you never use. Fewer features mean fewer doors."),
            ("point", "Buy from known brands", "A slightly more expensive device from a maker that publishes "
             "updates is often cheaper in the long run than a no-name gadget that never gets fixed."),
            ("h", "Working from Home Safely"),
            "If you handle office work at home, a few more habits help:",
            ("point", "Keep work and family devices apart", "Avoid letting children use the laptop you use for "
             "work or for official records."),
            ("point", "Lock the screen", "Press Windows key + L, or Control + Command + Q on a Mac, every time you "
             "step away."),
            ("point", "Use your office's approved tools", "Use the VPN, email and file-sharing services your office "
             "provides instead of personal accounts."),
            ("point", "Mind your surroundings", "Video calls and screens can be seen and heard by others in cafés and "
             "shared spaces."),
            ("h", "Your Part 4 Action Plan"),
            ("point", "Log in to your router this week", "Change the admin password, install any firmware update, and "
             "turn off WPS and remote management."),
            ("point", "Move your gadgets", "Turn on the guest network and move smart TVs, cameras and other gadgets "
             "to it."),
            ("point", "Check who is connected", "Look at the list of connected devices on your router. If you see "
             "something you do not recognize, change the Wi-Fi password and reconnect your own devices."),
            ("point", "Try a filtering DNS", "Set 9.9.9.9 or 1.1.1.2 on your router or on your phone, then browse "
             "normally for a week."),
            "An hour spent on your router protects every person and every device in your home, every day.",
            ("cta", "Read Part 5: Ransomware", "/blog/cybersecurity-part-5-ransomware/"),
            ("ask", "Did you find an old admin password or an unknown device on your router? Tell me what you found."),
        ],
    },
    {
        "date": "November 21, 2026",
        "title": "Cybersecurity Series, Part 3: The Art of Human Hacking",
        "slug": "cybersecurity-part-3-human-hacking",
        "category": "security",
        "summary": "Most scams do not break into computers; they persuade people. Learn the pressure tricks behind "
                   "phishing, smishing, fake bosses and deepfake calls, and the simple rules that stop them.",
        "publish_on": "2026-11-21 22:00",
        "body": [
            "Why would a criminal spend months looking for a flaw in a well-protected system when a convincing message "
            "can get someone inside to open the door? That is the idea behind social engineering, or human hacking. "
            "Instead of attacking the machine, the attacker works on the person using it, through trust, fear, "
            "kindness or simple hurry.",
            "Filipinos know this threat well. Many of us have received a text saying a package is on hold, an "
            "account will be suspended, or we have won a prize we never joined. In Part 3 of this series, we look at "
            "how these tricks work, why smart people fall for them, and the habits that defeat them, including "
            "scams that now use artificial intelligence to copy voices and faces.",
            ("h", "Why Smart People Get Fooled"),
            "Falling for a scam is not a sign of low intelligence. Scammers design messages to push us into acting "
            "before we think. Nearly every scam leans on one or more of these levers:",
            ("point", "Urgency", "\"Your account will be locked in 30 minutes.\" A deadline leaves no time to check."),
            ("point", "Authority", "The message claims to come from a bank, a government agency, the police or your "
             "boss. We are trained to obey such voices."),
            ("point", "Fear", "A threat of arrest, a fine, a frozen account or a relative in trouble makes the heart "
             "beat faster and the mind work slower."),
            ("point", "Greed or hope", "A prize, a refund, an easy job or an investment that doubles your money."),
            ("point", "Familiarity", "The message uses your name, your office, a real supplier or a friend's account, "
             "so it feels normal."),
            "Once you know the levers, you can feel them being pulled. When a message makes you feel rushed, "
            "afraid or excited, treat that feeling as a warning sign and slow down.",
            ("quote", "When a message makes you hurry, that is exactly the moment to stop."),
            ("h", "The Many Faces of Phishing"),
            "Phishing is the use of a fake message to steal passwords, money or personal details, or to install "
            "malware. It comes in many forms:",
            ("point", "Email phishing", "A message that looks like it is from your bank, an online store or your IT "
             "department, with a link to a fake login page or a harmful attachment."),
            ("point", "Smishing", "Phishing by text message. Common examples include fake delivery notices, "
             "\"unclaimed\" rewards and warnings that your SIM or e-wallet will be suspended."),
            ("point", "Vishing", "Phishing by voice call. A caller pretends to be from a bank, a telco or the "
             "authorities and asks for a one-time PIN, card number or account details."),
            ("point", "Quishing", "Phishing with a QR code, printed on a poster or sent in an email. Because you "
             "scan it with your phone, you cannot easily see the address before it opens."),
            ("point", "Fake pages and look-alike addresses", "Attackers register names that look almost right, such "
             "as a letter swapped for a similar one, and copy the real site's design."),
            "Modern phishing pages can be very convincing. Some even pass your password and your one-time code to "
            "the real site at the same moment, logging the attacker in as you. That is why we said in Part 2 that "
            "passkeys and security keys, which refuse to work on fake sites, are the strongest protection.",
            ("h", "Business Email Compromise: The Fake Invoice"),
            "Some of the costliest scams involve no malware at all. In business email compromise, an attacker takes "
            "over or imitates the email of a boss, supplier or partner. Sometimes they read real conversations for "
            "weeks. Then, at the right moment, they send one message: a new bank account for the next payment, an "
            "urgent transfer the boss \"approved,\" or a request to buy gift cards.",
            "This should worry anyone who handles payments, including offices that pay suppliers and contractors. "
            "The defense is not a gadget; it is procedure. In treasury work, we already know that a payment needs "
            "proper documents and approval, no matter who is asking or how urgent it sounds. The same rule applies "
            "to email: a request to change bank details or to rush a payment must be confirmed by phone, using a "
            "number you already have, never the one in the message.",
            ("h", "Deepfakes: When Seeing Is No Longer Believing"),
            "Artificial intelligence has made human hacking more dangerous. With a short sample of someone's voice, "
            "taken from a video or a voicemail, criminals can produce a convincing copy that says anything. Video "
            "can be faked too.",
            "In early 2024, Hong Kong police described a case in which a finance employee of the engineering firm "
            "Arup joined a video call with people who looked and sounded like the company's chief financial officer "
            "and colleagues. They were deepfakes. Persuaded by the call, the employee made 15 transfers totaling "
            "about HK$200 million, roughly US$25 million.",
            "The same trick works on families. A parent receives a call from a crying voice that sounds exactly like "
            "their child, asking for money right away. The defense is to verify through a separate channel: hang up "
            "and call the person back on their known number, or ask a question only the real person can answer.",
            ("h", "How to Check a Message in Ten Seconds"),
            ("point", "Look at the real sender", "Check the full email address or number, not just the display name."),
            ("point", "Check the link before you tap", "On a computer, hover over it. On a phone, press and hold "
             "to preview the address. Read the domain name carefully from right to left."),
            ("point", "Go there yourself", "Instead of tapping a link, open your bank's app or type the address you "
             "know."),
            ("point", "Never share one-time codes", "Banks and e-wallets will not ask for your OTP, PIN or password "
             "by call, text or chat."),
            ("point", "Be suspicious of attachments", "Turn on \"show file extensions\" so a file named "
             "invoice.pdf.exe cannot pretend to be a PDF."),
            ("h", "What Domain Owners Can Do"),
            "If you run a website or an office email domain, you can make it harder for criminals to send email "
            "in your name. Three records published in your domain's DNS settings do the work. SPF lists the servers "
            "allowed to send your mail. DKIM adds a digital signature to each message. DMARC tells receiving "
            "servers what to do when a message fails these checks, such as sending it to spam or rejecting it. "
            "Since 2024, Google and Yahoo have required these records from senders of large volumes of email, so "
            "they are now standard practice.",
            ("h", "The Law Is on Your Side"),
            "The Philippines has strengthened its laws against these schemes. The Anti-Financial Account Scamming "
            "Act (Republic Act No. 12010), signed in July 2024, punishes social engineering schemes, money muling "
            "and the selling or lending of bank and e-wallet accounts for scams. Large-scale schemes can even be "
            "treated as economic sabotage. The SIM Registration Act (Republic Act No. 11934) was also meant to make "
            "scammers easier to trace.",
            "If you encounter a scam, report it. The Cybercrime Investigation and Coordinating Center runs the "
            "Inter-Agency Response Center hotline 1326. Tell your bank or e-wallet right away if money or account "
            "details are involved, because quick reports give them the best chance to stop a transfer.",
            ("h", "If You Already Clicked"),
            "It happens to careful people every day. What matters is what you do in the next few minutes, so act "
            "rather than hope for the best.",
            ("point", "If you typed a password", "Change it at once on the real site, and anywhere else you used the "
             "same password. Then sign out of other sessions and check your MFA settings."),
            ("point", "If you shared a code or card details", "Call your bank or e-wallet immediately through its "
             "official hotline and ask them to block the account or card. Minutes count."),
            ("point", "If you opened a file", "Disconnect the device from the internet and ask your IT team or a "
             "trusted technician to check it before you use it for banking or work again."),
            ("point", "Tell someone", "Report it to your office IT team if it involved work, and warn family or "
             "colleagues who may receive the same message. There is no shame in reporting; the shame belongs to "
             "the scammer."),
            ("h", "Your Part 3 Action Plan"),
            ("point", "Adopt a call-back rule", "Never change bank details, approve a payment or share sensitive "
             "files based only on an email, text or chat. Call back on a number you already know."),
            ("point", "Agree on a family safe word", "Choose a word or question that only your family knows, to "
             "check any emergency call asking for money."),
            ("point", "Show file extensions", "On Windows 11, open File Explorer, choose View, then Show, and turn on "
             "File name extensions. On a Mac, open Finder Settings, then Advanced, and tick Show all filename "
             "extensions."),
            ("point", "Save 1326", "Add the hotline to your contacts, and share it with your parents and older "
             "relatives, who are often targeted."),
            "Technology catches many scams, but the last line of defense is a person who pauses, checks and asks. "
            "Share these habits with the people around you, especially those who handle money.",
            ("cta", "Read Part 4: Your Home Network", "/blog/cybersecurity-part-4-home-network/"),
            ("ask", "What is the most convincing scam message you have received? Send it to me (remove your personal "
             "details first), and it may help someone else."),
        ],
    },
    {
        "date": "November 14, 2026",
        "title": "Cybersecurity Series, Part 2: Identity Is the New Perimeter",
        "slug": "cybersecurity-part-2-passwords-and-mfa",
        "category": "security",
        "summary": "Attackers no longer break in; they log in. Here is why long passphrases beat complex passwords, "
                   "how a password manager works, which kinds of two-step login are strongest, and why passkeys "
                   "are the future.",
        "publish_on": "2026-11-14 22:00",
        "body": [
            "A firewall cannot stop someone who walks in with your username and password. That is why many security "
            "people now say that identity is the new perimeter. Your work systems, your bank, your e-wallet and your "
            "social media accounts are all reachable from anywhere in the world. The only thing standing between "
            "an attacker and your account is how well you prove that you are you.",
            "In Part 2 of this series, we look at passwords, why the old rules failed, and the tools that make "
            "logins far safer: password managers, multi-factor authentication and passkeys.",
            ("h", "Why the Old Password Rules Failed"),
            "For years, we were told to create passwords with at least eight characters, a capital letter, a number "
            "and a symbol, and to change them every few months. The result was predictable. People wrote passwords "
            "like Password1! and then, when forced to change them, used Password2!. These are hard for people to "
            "remember and easy for computers to guess, because attackers know exactly how people adapt to such rules.",
            "The guidance has changed. The United States National Institute of Standards and Technology (NIST), "
            "whose digital identity guidelines are followed around the world, finalized a new edition in August "
            "2025 (SP 800-63B-4). It says passwords used on their own should be at least 15 characters long, systems "
            "should accept much longer ones, and organizations should not impose composition rules like \"one "
            "symbol and one number\" or force regular password changes. Passwords should be changed when there is "
            "evidence they were exposed, and new passwords should be checked against lists of common and leaked ones.",
            ("h", "Length Beats Complexity"),
            "Every extra character multiplies the number of guesses an attacker needs. A password of eight random "
            "characters looks strong, but powerful graphics cards can try billions of guesses per second against "
            "passwords that a website stored carelessly. A passphrase of four or five unrelated words, such as "
            "\"mango-ladder-sunrise-pencil-river\", is much longer, easier to remember and far harder to crack.",
            "The catch is that a phrase only helps if it is truly random. Song lyrics, Bible verses, birthdays and "
            "your children's names are all among the first things attackers try.",
            ("h", "How Accounts Really Get Stolen"),
            "Surprisingly, most stolen accounts are not cracked by guessing. They are stolen in other ways:",
            ("point", "Reused passwords", "When one website is breached, attackers try the same email and password on "
             "banks, email and social media. This is called credential stuffing, and it works because so many "
             "people reuse passwords."),
            ("point", "Phishing", "A fake login page collects your password as you type it."),
            ("point", "Infostealer malware", "Malicious programs, often hidden in pirated software or fake "
             "downloads, copy the passwords saved in your browser and send them to criminals, who sell them in bulk."),
            "Verizon's 2025 Data Breach Investigations Report found that the abuse of stolen credentials was the "
            "most common way into the systems it studied, at 22% of breaches. A strong password does not help if "
            "it is reused, typed into a fake page or stolen from your computer. That is why the next two tools "
            "matter so much.",
            ("h", "Tool 1: A Password Manager"),
            "No one can remember a different long password for fifty accounts. A password manager does it for you. "
            "It creates a strong random password for each account, stores them in an encrypted vault, and fills them "
            "in when you log in. You remember only one strong master password.",
            "Good password managers encrypt your vault on your own device before it is synced, using your master "
            "password to build the key. The company that stores your vault cannot read it. Many reputable options "
            "exist, including free and open-source ones such as Bitwarden, as well as the managers built into your "
            "phone or browser. The best one is the one you will actually use.",
            "A password manager also protects you from fake websites in a quiet way: it will not offer to fill in "
            "your bank password on a page that is not your bank's real address. When it refuses, take that as a "
            "warning.",
            ("h", "Tool 2: Multi-Factor Authentication"),
            "Multi-factor authentication (MFA), also called two-step verification, asks for a second proof besides "
            "your password: something you have, like your phone, or something you are, like your fingerprint. Even "
            "if a criminal gets your password, they still need that second factor. Not all second factors are "
            "equally strong, though.",
            ("point", "Codes by SMS or email (good, but weakest)", "Far better than nothing, but codes can be stolen "
             "through SIM swapping, where a criminal convinces a telco to move your number to their SIM, or by "
             "tricking you into reading the code aloud."),
            ("point", "Authenticator apps (better)", "Apps such as Google Authenticator or Microsoft Authenticator "
             "produce a new six-digit code every 30 seconds on your phone, without using the mobile network."),
            ("point", "Passkeys and security keys (strongest)", "These use cryptography tied to the real website's "
             "address. A fake site cannot use them, so they resist phishing by design."),
            "Our regulators are moving the same way. Under Circular No. 1213 of the Bangko Sentral ng Pilipinas, "
            "banks and e-wallets with large online transaction volumes had until June 25, 2026 to stop relying on SMS and email one-time PINs for "
            "high-risk transactions and to use stronger methods such as biometrics or passwordless login. If your "
            "bank app now asks for a face scan for large transfers, this is why.",
            ("h", "Tool 3: Passkeys"),
            "Passkeys are designed to replace passwords altogether. When you create a passkey, your device makes a "
            "pair of matching keys. The public key goes to the website; the private key stays on your phone or "
            "computer, protected by your fingerprint, face or screen lock. When you log in, your device proves it has "
            "the private key without ever sending it. There is nothing to type, nothing to reuse and nothing for a "
            "fake site to steal.",
            "Google, Apple and Microsoft accounts, along with a growing number of shopping, social media and banking "
            "services, now support passkeys. Look for \"Passkeys\" or \"Sign in without a password\" in your account's "
            "security settings.",
            ("h", "Protect the Master Key: Your Email"),
            "If you secure only one account today, make it your main email. Nearly every other account lets you reset "
            "its password through email. Whoever controls your inbox can take over the rest. Give it a unique long "
            "password, your strongest form of MFA and an up-to-date recovery phone number.",
            ("quote", "Whoever controls your email can reset almost everything else. Guard it first."),
            ("h", "Signs Your Account Has Been Taken Over"),
            "Even careful people get caught. The sooner you notice, the less damage is done. Watch for these signs:",
            ("point", "Alerts you did not trigger", "Login alerts from a new device or place, or password reset "
             "emails you did not ask for."),
            ("point", "Changes you did not make", "A new recovery email or phone number, forwarding rules in your "
             "email, or messages in your Sent folder that you never wrote."),
            ("point", "Friends asking strange questions", "Contacts receiving requests for money or odd links from "
             "your account."),
            ("point", "Your SIM suddenly stops working", "If your phone loses signal for no clear reason and you "
             "cannot make calls, contact your telco at once. It may be a SIM swap."),
            "If you see these signs, act quickly. From a device you trust, change the password, sign out of all "
            "other sessions (most services have a \"sign out everywhere\" option), check the recovery details and "
            "MFA settings, and remove anything you did not add. If money is involved, call your bank or e-wallet "
            "right away using the number on its official website or on the back of your card.",
            ("h", "Your Part 2 Action Plan"),
            ("point", "Start a password manager", "Install one and move your five most important accounts into it, "
             "each with a new, unique password of 15 characters or more."),
            ("point", "Upgrade your MFA", "Turn on an authenticator app or a passkey for your main email, and keep "
             "SMS only as a backup."),
            ("point", "Save your recovery codes", "When you turn on MFA, you are given backup codes. Print them and "
             "keep them somewhere safe at home, not in a photo on your phone."),
            ("point", "Stop saving passwords in random places", "Delete passwords stored in notes apps, chats or "
             "unprotected spreadsheets once they are in your password manager."),
            "None of this takes a computer expert. A password manager, a second factor and a passkey on your email "
            "will protect you better than any rule about symbols and numbers ever did.",
            ("cta", "Read Part 3: Human Hacking", "/blog/cybersecurity-part-3-human-hacking/"),
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
            "Ask someone to picture a hacker and you will probably hear about a lone genius in a dark room, typing "
            "green code at impossible speed until a screen flashes \"Access granted.\" It makes a good movie scene. "
            "It is also misleading.",
            "Much of today's cybercrime looks less like a heist and more like a business. Criminal groups divide the "
            "work, rent out their tools, buy stolen passwords in bulk and use automated programs that scan the "
            "internet for weak devices day and night. Most victims are not chosen because they are important. They "
            "are chosen because they were easy.",
            "This post opens a cybersecurity series on this blog. I work in the treasury service and build software "
            "on the side, and both jobs have taught me the same lesson: what protects public money and public records "
            "is not one strong lock but many good habits. The series is written for everyone: parents, students, "
            "office workers, small business owners and anyone who uses a phone. In Part 1, we map the ground: "
            "what security protects, who the attackers are, how a typical breach unfolds, and how we fight back.",
            ("h", "What Security Protects: The CIA Triad"),
            "Security professionals sum up their work in three words, known as the CIA triad. (It has nothing to do "
            "with the spy agency.)",
            ("point", "Confidentiality", "Only the right people can see the information. When a list of taxpayers' "
             "names and addresses leaks online, confidentiality has failed."),
            ("point", "Integrity", "Information stays accurate and unaltered. If someone quietly changes the bank "
             "account number on a supplier's invoice, integrity has failed, even if no one notices yet."),
            ("point", "Availability", "Systems and data are there when people need them. When ransomware locks an "
             "office's computers or a website is knocked offline, availability has failed."),
            "Every security tool you have heard of, from antivirus to backups to encryption, exists to protect one or "
            "more of these three. When you are unsure whether something is a security issue, ask: does it threaten "
            "who can see the data, whether it can be trusted, or whether it is there when needed?",
            ("h", "Who Is on the Other Side?"),
            "Attackers have different goals, and knowing their goals helps you understand their methods.",
            ("point", "Cybercriminals", "The largest group, motivated by money. They steal passwords, card numbers "
             "and bank details, run scams and deploy ransomware. Many use ransomware-as-a-service, renting "
             "ready-made malware from its developers and sharing the ransom with them."),
            ("point", "State-sponsored groups", "Teams backed by governments that spy, steal secrets or prepare to "
             "disrupt power, telecommunications and other critical services. They are patient and may hide inside "
             "a network for months."),
            ("point", "Hacktivists", "People driven by a political or social cause. They deface websites, leak "
             "documents or flood a site with traffic to take it offline, aiming for attention."),
            ("point", "Insiders", "People who already have access. Some act out of anger or greed, but many insider "
             "incidents are honest mistakes: an email sent to the wrong person, or a shared folder left open to "
             "anyone with the link."),
            ("h", "How a Breach Unfolds"),
            "A serious attack is rarely a single event. It is a chain of steps, and each step is a chance to stop it. "
            "Security teams describe this chain with models such as Lockheed Martin's Cyber Kill Chain and the MITRE "
            "ATT&CK knowledge base, which catalogs the techniques real attackers use. In plain terms, most "
            "intrusions follow a path like this:",
            ("point", "1. Reconnaissance", "The attacker gathers information: staff names from social media, email "
             "formats, leaked passwords from old breaches, and devices exposed to the internet."),
            ("point", "2. Initial access", "They get a foothold, often by logging in rather than breaking in: a "
             "phishing email that captures a password, a password bought from a criminal market, or a known flaw in "
             "a device that was never updated."),
            ("point", "3. Persistence", "They make sure they can return, by creating hidden accounts or installing "
             "remote-control tools that survive a restart."),
            ("point", "4. Privilege escalation and lateral movement", "The first computer is rarely the prize. They "
             "collect more passwords, gain administrator rights and move from machine to machine toward servers, "
             "databases and backups."),
            ("point", "5. Action on objectives", "Finally, they do what they came for: copy data out, transfer money, "
             "plant ransomware or disrupt services."),
            "Verizon's 2025 Data Breach Investigations Report, one of the industry's largest yearly studies, shows "
            "what the first doors look like. Stolen credentials were the most common way in, at 22% of breaches, "
            "followed closely by the exploitation of software flaws, at 20%. Third parties such as suppliers and "
            "service providers were involved in 30% of breaches, double the year before. In other words: weak "
            "passwords, missing updates and trusted partners.",
            ("h", "Why One Wall Is Not Enough"),
            "For a long time, organizations treated security like a castle. They built a strong wall, a firewall, "
            "around the office network and trusted everyone inside. That model has aged badly. Our data now lives in "
            "cloud services, our staff work from home and from their phones, and a single stolen password can carry "
            "an attacker across the drawbridge. Once inside a flat, trusting network, they can often move freely.",
            "This does not mean firewalls are useless. It means they cannot be the only defense.",
            ("h", "How We Fight Back: Layers"),
            "The answer is defense in depth. Safety experts often explain it with the Swiss cheese model, first "
            "described by the psychologist James Reason to show how accidents happen. Picture each defense as a "
            "slice of Swiss cheese. Every slice has holes. Spam filters miss some emails. People get tired and "
            "click. Antivirus does not recognize every new threat. But when you stack several slices, the holes rarely "
            "line up.",
            "Suppose a phishing email slips past the filter and you type your password into a fake page. Multi-factor "
            "authentication stops the attacker from logging in. If they get past that, up-to-date software and "
            "endpoint protection may block their tools. If those fail, limited access rights keep them from reaching "
            "everything. And if the worst happens, offline backups let you recover without paying anyone.",
            "Treasury work runs on the same principle. We do not rely on one honest person; we use separation of "
            "duties, official receipts, daily reports of collections and deposits, and regular audits. No single "
            "control is perfect, but together they make errors and fraud hard to hide. Good cybersecurity works "
            "the same way.",
            ("quote", "You do not need to be impossible to hack. You need to be too costly, too slow and too noisy to "
                      "be worth the trouble."),
            ("h", "Four Myths That Help Attackers"),
            "Let us also clear away a few beliefs that make attackers' work easier.",
            ("point", "Myth: I am not important enough to be targeted", "Most attacks are automated. A program that "
             "tries leaked passwords or scans for unpatched devices does not care who you are. Your account, your "
             "phone number and your computer's power are all worth something to a criminal."),
            ("point", "Myth: I have antivirus, so I am safe", "Antivirus is one useful slice of cheese, not the whole "
             "block. It cannot stop you from typing your password into a fake page or sending money to a scammer."),
            ("point", "Myth: Phones and Macs do not get hacked", "Every device can be attacked, and phones carry our "
             "banking apps, our one-time PINs and our private chats. Scams do not care which brand you use."),
            ("point", "Myth: Security is the IT office's job", "IT teams build the walls, but each of us holds a key. "
             "One rushed click can undo the best technology, and one careful pause can stop an attack that "
             "technology missed."),
            ("h", "A Note for the Philippines"),
            "Cybercrime is not a distant problem. Text scams, fake e-wallet links and account takeovers are part of "
            "daily life, and government agencies have suffered serious attacks. The country has laws to respond: "
            "the Cybercrime Prevention Act of 2012 (Republic Act No. 10175), the Data Privacy Act of 2012 (Republic "
            "Act No. 10173) and, more recently, the Anti-Financial Account Scamming Act of 2024 (Republic Act No. "
            "12010). Laws punish criminals after the fact, though. Habits protect us before.",
            ("h", "Your Part 1 Action Plan"),
            ("point", "Check your exposure", "Visit haveibeenpwned.com and enter your main email address. The free "
             "service shows which known data breaches included your address. If a password you still use was "
             "exposed, change it."),
            ("point", "Turn on automatic updates", "On your phone, computer and browser. Many attacks use flaws that "
             "were fixed months earlier, betting that people keep pressing \"Remind me later.\""),
            ("point", "Name your three most important accounts", "Usually your main email, your bank or e-wallet, and "
             "your work login. Your email matters most, because it can reset the passwords of almost everything else."),
            "Start with these three steps this week. They take less than an hour, and they close the doors that "
            "attackers try first.",
            ("cta", "Read Part 2: Identity", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("ask", "Which cybersecurity topic would you like this series to explain next?"),
        ],
    },
]
