# Cybersecurity blog series (Season 1: Cyber Hygiene and Personal Defense).
# Planned from Butch's Google Doc "10-Week Cybersecurity Blog Series Roadmap & Drafts"
# (Drive 1cqfvL885e80Hj7cjLE5YWEC392nrzD2ZkZmSLoHgwRE), written in original words and
# fact-checked on 2026-11-10. Parts 1-5 go live together (Butch, 2026-11-10: "post today at least 5").
# Newest first, like BLOG in content.py, which puts these posts at the top of its list.

SERIES = "Cybersecurity Series"

CYBER_POSTS = [
    {
        "date": "November 10, 2026",
        "title": "Cybersecurity Series, Part 5: Inside a Ransomware Attack",
        "slug": "cybersecurity-part-5-ransomware",
        "category": "security",
        "summary": "How ransomware gangs break in, steal before they lock, and pressure victims to pay, what the "
                   "PhilHealth attack of 2023 taught the country, and the backup habit that takes away their leverage.",
        "publish_on": "2026-11-10",
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
            "computer from the network by turning off Wi-Fi or unplugging the network cable, but do not switch "
            "it off, because the evidence in its memory can help investigators. Photograph the ransom note. Tell "
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
            "This ends the first five parts of the series. Together, they cover the basics most people need: how "
            "attacks work, how to protect your accounts, how to spot a scam, how to secure your home network and "
            "how to survive ransomware. Bookmark them, share them with someone who handles money or records, and "
            "come back to the action plans every few months.",
            ("cta", "Start again with Part 1", "/blog/cybersecurity-part-1-how-cyberattacks-work/"),
            ("ask", "Has your office ever tested restoring its backups? I would like to hear how it went."),
        ],
    },
    {
        "date": "November 10, 2026",
        "title": "Cybersecurity Series, Part 4: Securing Your Home and Remote Network",
        "slug": "cybersecurity-part-4-home-network",
        "category": "security",
        "summary": "Your Wi-Fi router is the front door of your digital home. Here is how to lock it, separate your "
                   "smart devices from your work laptop, filter dangerous websites, and understand what a VPN can "
                   "and cannot do.",
        "publish_on": "2026-11-10",
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
            "Modern phones and browsers also support encrypted DNS, often called DNS over HTTPS or Private DNS on "
            "Android. Encryption keeps people on the same network from seeing or tampering with the names you look "
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
            "Part 5 closes this first set with the threat that worries offices most: ransomware, and the backup "
            "habit that defeats it.",
            ("cta", "Read Part 5: Ransomware", "/blog/cybersecurity-part-5-ransomware/"),
            ("ask", "Did you find an old admin password or an unknown device on your router? Tell me what you found."),
        ],
    },
    {
        "date": "November 10, 2026",
        "title": "Cybersecurity Series, Part 3: The Art of Human Hacking",
        "slug": "cybersecurity-part-3-human-hacking",
        "category": "security",
        "summary": "Most scams do not break into computers; they persuade people. Learn the pressure tricks behind "
                   "phishing, smishing, fake bosses and deepfake calls, and the simple rules that stop them.",
        "publish_on": "2026-11-10",
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
            ("point", "Show file extensions", "On Windows, open File Explorer, choose View, then Show, and turn on "
             "File name extensions. On a Mac, open Finder Settings, then Advanced, and tick Show all filename "
             "extensions."),
            ("point", "Save 1326", "Add the hotline to your contacts, and share it with your parents and older "
             "relatives, who are often targeted."),
            "In Part 4, we move from people to places: the home network that connects your family and, often, "
            "your work.",
            ("cta", "Read Part 4: Your Home Network", "/blog/cybersecurity-part-4-home-network/"),
            ("ask", "What is the most convincing scam message you have received? Send it to me (remove your personal "
             "details first), and it may help someone else."),
        ],
    },
    {
        "date": "November 10, 2026",
        "title": "Cybersecurity Series, Part 2: Identity Is the New Perimeter",
        "slug": "cybersecurity-part-2-passwords-and-mfa",
        "category": "security",
        "summary": "Attackers no longer break in; they log in. Here is why long passphrases beat complex passwords, "
                   "how a password manager works, which kinds of two-step login are strongest, and why passkeys "
                   "are the future.",
        "publish_on": "2026-11-10",
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
            ("point", "Phishing", "A fake login page collects your password as you type it. We will look at this "
             "closely in Part 3."),
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
            "Next, in Part 3, we look at the weakest and strongest link in every system: people, and the scams "
            "designed to fool them.",
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
            "Before we go further, let us clear away a few beliefs that make attackers' work easier.",
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
            "In Part 2, we will protect those accounts with the tools that make the biggest difference: long "
            "passphrases, password managers, multi-factor authentication and passkeys.",
            ("cta", "Read Part 2: Identity", "/blog/cybersecurity-part-2-passwords-and-mfa/"),
            ("ask", "Which cybersecurity topic would you like this series to explain next?"),
        ],
    },
]
