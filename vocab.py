"""Civil Service Exam Vocabulary: a second tutorial series on /tutorials/civil-service-vocabulary/.

Based on Butch's Google Doc "Civil Service Exam Vocabulary Masterclass" (2026-11-07),
edited: plainer meanings, real example sentences, accurate government context, and
exam-style practice questions with answers behind "Show answer".

Each module: number, slug, title, publish_on (YYYY-MM-DD, Philippine date; None = live now),
words [(word, part of speech, meaning, example, synonyms, antonyms, note)],
practice [(question, [choices], index of the right choice, why)].
Meanings were checked against Merriam-Webster (linked on each word).
"""

VOCAB = {
    "title": "Civil Service Exam Vocabulary",
    "slug": "civil-service-vocabulary",
    "intro": (
        "Ten words at a time for the Career Service Examination (Professional and Subprofessional). "
        "The exam's verbal part tests vocabulary, analogies and how words are used in a sentence, so each "
        "word comes with a plain meaning, an example from government work, words that mean the same "
        "and the opposite, and practice questions in the exam's style."
    ),
    "note": (
        "I earned my Career Service Professional eligibility in 2012 and have spent more than 15 years in "
        "government service. These are study notes, not official exam material: for the exam schedule, rules and "
        "coverage, always check the Civil Service Commission."
    ),
    "csc_url": "https://csc.gov.ph/",
}

MODULES = [
    {
        "number": 1,
        "slug": "governance-law-and-public-administration",
        "title": "Governance, law and public administration",
        "summary": "Ten words you meet in memos, audit reports and office orders: acquiesce, ad hoc, anomaly, "
                   "arbitrary, ascertain, assiduous, autonomous, bureaucracy, cognizant and compliance.",
        "publish_on": None,
        "words": [
            ("acquiesce", "verb",
             "To accept or agree to something quietly, without protest.",
             "The department head acquiesced to the auditor's request for the original receipts.",
             ["comply", "consent", "yield"], ["resist", "object", "defy"],
             "Usually followed by \"to\" or \"in\": acquiesce to a request, acquiesce in a decision."),
            ("ad hoc", "adjective",
             "Formed or done for one particular purpose only, not as a permanent arrangement.",
             "The mayor created an ad hoc committee to look into the delayed payroll.",
             ["temporary", "special", "improvised"], ["permanent", "standing", "regular"],
             "A \"standing committee\" is the permanent kind; an \"ad hoc committee\" ends when its job is done."),
            ("anomaly", "noun",
             "Something that is different from what is normal or expected.",
             "The cashier flagged an anomaly: two official receipts carried the same serial number.",
             ["irregularity", "deviation", "aberration"], ["norm", "rule", "standard"],
             "In news about government, \"anomaly\" often hints at wrongdoing, but the word itself only means "
             "something out of the ordinary."),
            ("arbitrary", "adjective",
             "Based on personal choice or chance, not on a reason, rule or law.",
             "Fees must be set by ordinance, not by an arbitrary decision at the counter.",
             ["random", "unreasoned", "whimsical"], ["reasoned", "lawful", "systematic"],
             "Often paired with \"capricious\": an arbitrary and capricious act is one without legal basis."),
            ("ascertain", "verb",
             "To find out something for certain.",
             "Before releasing the check, the treasurer ascertained that the payee's documents were complete.",
             ["determine", "verify", "establish"], ["guess", "assume", "overlook"],
             "Pronounced \"as-er-TAYN\". It is about making sure, not just finding out."),
            ("assiduous", "adjective",
             "Showing great care and steady, hard work.",
             "Her assiduous record-keeping made the year-end audit quick and clean.",
             ["diligent", "industrious", "meticulous"], ["careless", "negligent", "lazy"],
             "Close to \"diligent\"; both describe effort that keeps going over time."),
            ("autonomous", "adjective",
             "Able to govern itself or act on its own, without outside control.",
             "Under the 1987 Constitution, local governments enjoy local autonomy, though they remain under the "
             "general supervision of the President.",
             ["self-governing", "self-ruling", "independent"], ["dependent", "subordinate", "controlled"],
             "Noun: autonomy. \"Local autonomy\" is a key phrase in the Local Government Code of 1991 (RA 7160)."),
            ("bureaucracy", "noun",
             "A system of government offices run by appointed officials who follow set rules and procedures; "
             "also used for too many rules that slow things down.",
             "The new online permit system cut through the bureaucracy that used to take a week.",
             ["administration", "officialdom", "red tape"], [],
             "Neutral in public administration books, but often negative in everyday speech, meaning \"red tape\"."),
            ("cognizant", "adjective",
             "Aware of something; having knowledge of it.",
             "Officers must be cognizant of the budget ceiling before approving any purchase.",
             ["aware", "mindful", "conscious"], ["unaware", "ignorant", "oblivious"],
             "Usually followed by \"of\": cognizant of the rules."),
            ("compliance", "noun",
             "The act of following a rule, law, order or standard.",
             "This quarter, the office was in full compliance with the deadlines for its monthly reports.",
             ["adherence", "conformity", "obedience"], ["violation", "breach", "defiance"],
             "\"In compliance with\" is a common opening in official letters: \"In compliance with your memo...\""),
        ],
        "practice": [
            ("Choose the word closest in meaning to ASSIDUOUS.",
             ["careless", "diligent", "arrogant", "silent"], 1,
             "Assiduous means careful and hard-working, like diligent."),
            ("Choose the word opposite in meaning to COGNIZANT.",
             ["aware", "mindful", "oblivious", "informed"], 2,
             "Cognizant means aware; oblivious means not aware at all."),
            ("Complete the sentence: The council formed an ____ committee that will be dissolved once the flood "
             "relief audit is finished.",
             ["autonomous", "arbitrary", "ad hoc", "assiduous"], 2,
             "A committee made for one task and dissolved afterward is an ad hoc committee."),
            ("ANOMALY is to IRREGULARITY as COMPLIANCE is to ____.",
             ["adherence", "violation", "audit", "penalty"], 0,
             "The first pair are synonyms, so the answer is the synonym of compliance: adherence."),
            ("Which sentence uses ACQUIESCE correctly?",
             ["The clerk acquiesced the receipts in the drawer.",
              "After a short discussion, the supplier acquiesced to the new delivery schedule.",
              "The auditor acquiesced loudly against the findings.",
              "The office was acquiesced by the new rules."], 1,
             "Acquiesce means to agree quietly and is followed by \"to\" or \"in\". Choice A uses it to mean "
             "\"put away\", C to mean \"protest\", and D wrongly makes it passive."),
        ],
    },
]


def module_url(m):
    return f"/tutorials/{VOCAB['slug']}/{m['slug']}/"


def word_source(word):
    return "https://www.merriam-webster.com/dictionary/" + word.replace(" ", "%20")
