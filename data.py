import os
import json

LOG_FILE = "user_total_time.json"

def log_time_spent(user_id, time_spent):
    # Load or initialize data
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    # Add to user's total time
    data[user_id] = data.get(user_id, 0) + time_spent

    # Save updated data
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)


lessons = [
    {
        "id": 1, 
        "title": "What is Phishing?", 
        "image": "https://marvel-b1-cdn.bc0a.com/f00000000032040/cdn.prod.website-files.com/672e4d78ddc6417dc8ab2e1f/675a28b32b088f04d89ce051_32040_94c482e61bc04c5bb6a918a7cde3d962_1542746731.png",
        "content": "Phishing is a method cybercriminals use to trick you into giving up personal info."
    },
    {
        "id": 2, 
        "title": "Learn how to spot phishing", 
        "image": "https://www.technologysolutions.net/wp-content/uploads/2023/07/Phising-Awerness-scaled-2560x1280.jpeg",
        "content": ""
    },
    {
        "id": 3, 
        "title": "1. Asks for sensitive information", 
        "image": "https://www.imperva.com/learn/wp-content/uploads/sites/13/2019/01/phishing-attack-email-example.png",
        "content": "Legitimate emails will not request passwords, bank info, or SSNs."
    },
    {
        "id": 4, 
        "title": "2. Uses a different domain", 
        "image": "https://cybeready.com/wp-content/uploads/Screen-Shot-2020-11-05-at-13.09.28.png",
        "content": "Impersonates real companies, tricking users into thinking a message came from a person or entity they know or trust."
    },
    {
        "id": 5, 
        "title": "3. Contains look-alike links", 
        "image": "https://www.techtarget.com/rms/editorial/sSecurity_0415_ISM_soceng_phishing1.png",
        "content": "Scammers disguise malicious links by slightly altering well-known or official ones. Hover the cursor over any links to make sure they will take you to the site you expect. Look for https:// at the start of the URL, and do not click links that do not use HTTPS."
    },
    {
        "id": 6, 
        "title": "4. Includes suspicious attachments.", 
        "image": "https://ucdavisit.service-now.com/sys_attachment.do?sys_id=1a1f72931b4709504690ea04604bcbf3",
        "content": ".exe or .zip files in emails are risky since it is difficult to identify what files are stored within them. Avoid opening email attachments, even from a supposed established organization."
    },
    {
        "id": 7, 
        "title": "5. Uses poor spelling/grammar", 
        "image": "https://truecaller-web-cms.pages.dev/tc-main/OTM4ZGEyNmEtYmRmMS00ZjY5LWFlMmQtMGZiZDQ3MWE3MWFm_73d49237-c989-43b6-a044-dbcb7171c920_spam_example_truecaller_spelling_mistake.png?auto=compress,format&rect=0,0,1394,886&w=1394&h=886",
        "content": "Attackers may deliberately use grammatical errors to weed out less cautious users, who make easier targets."
    },
    {
        "id": 8, 
        "title": "6. Incites panic, seemingly urgent", 
        "image": "https://www.terranovasecurity.com/sites/default/files/2024-02/phishing_email_example_business_account.png",
        "content": "The aim is to make recipients feel as if they’re missing out on an urgent offer or reward, and are more likely to be less cautious."
    },
    {
    "id": 9,
    "title": "Tips",
    "image": "https://www.creativefabrica.com/wp-content/uploads/2022/06/13/Tips-Outline-Icon-Graphics-32281693-1.jpg",
    "content": [
        "Never give out personal information over email.",
        "Don't click email links from unknown sources.",
        "Monitor your online accounts regularly.",
        "Be wary of social, emotional lures.",
        "Keep your browser updated."
    ]
},
    {
        "id": 10, 
        "title": "Learn about the types of phishing", 
        "image": "https://images.prismic.io/sketchplanations/ZoKVHx5LeNNTwrK5_SP653-Typesofphishing.png?auto=format,compress",
        "content": ""
    },
    {
        "id": 11, 
        "title": "Types of Phishing - Spear Phishing", 
        "image": "https://vipre.com/wp-content/uploads/2022/11/spear-phishing-1024x747.jpeg",
        "content": "Spear phishing thieves target members of a particular group. The success rate of spear phishing is much higher, but also requires the hackers to invest time and resources into doing some pre-attack research."
    },
    {
        "id": 12, 
        "title": "Types of Phishing - Whale Phishing", 
        "image": "https://coremanaged.com/wp-content/uploads/2021/11/whale-attacks-email.jpg",
        "content": "Whale phishing is focused on a specific individual, usually the “biggest phish” at the target organization or an individual with significant wealth or power."
    },
    {
        "id": 13, 
        "title": "Types of Phishing - Smishing", 
        "image": "https://i.postimg.cc/dVww8xcv/img.png",
        "content": "Phishing also happens over text messages. Be cautious of unknown senders."
    }
]

quiz_questions = [
    {
        "id": 1,
        "question": "Is this phishing?",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Example_bank_phishing_email.svg/1200px-Example_bank_phishing_email.svg.png",
        "options": ["Yes", "No"],
        "answer": "Yes",
        "explanation": "It uses a fake sender address, a misleading link, and scare tactics to trick you into revealing your personal banking information."
    },
    {
        "id": 2,
        "question": "Is this phishing?",
        "image": "https://i.postimg.cc/vHcTXPrM/Screenshot-2025-05-02-at-2-29-01-PM.png",
        "options": ["Yes", "No"],
        "answer": "Yes",
        "explanation": "It uses a fake sender address, a deceptive link that looks similar to Citibank's official URL, and urgent language about “suspicious activity” to trick you."
    },
    {
        "id": 3,
        "question": "Is this phishing?",
        "image": "https://miro.medium.com/v2/resize:fit:1400/1*GDyWzrS3ZjmUfmsAKdtmDQ.png",
        "options": ["Yes", "No"],
        "answer": "No",
        "explanation": "It uses a legitimate sender address (cs-reply@amazon.com), contains no urgent or threatening language, and links directly to the official Amazon website (https://www.amazon.com)."
    },
    {
        "id": 4,
        "question": "Is this phishing?",
        "image": "https://cdn.abcotvs.com/dip/images/11371439_122221-ktrk-scam-text-tn-img.jpg",
        "options": ["Yes", "No"],
        "answer": "Yes",
        "explanation": "It uses a suspicious link (no https://), vague language, and fake urgency to trick you into clicking."
    },
    {
        "id": 5,
        "question": "Is this phishing?",
        "image": "https://i.postimg.cc/vmLZDCs7/Screenshot-2025-05-02-at-2-31-35-PM.png",
        "options": ["Yes", "No"],
        "answer": "No",
        "explanation": "It links to https://verify.id.me, which is an official domain used by ID.me and the message is calm, not threatening or overly urgent."
    },
    {
        "id": 6,
        "question": "What makes spear phishing different from regular phishing?",
        "options": [
            "A. It uses malware to infect your computer",
            "B. It targets specific individuals or groups using personalized information",
            "C. It involves stealing physical mail",
            "D. It can only happen on social media"
        ],
        "answer": "B. It targets specific individuals or groups using personalized information",
    },
    {
        "id": 7,
        "question": "Why is spear phishing often more successful than generic phishing?",
        "options": [
            "A. It uses stronger passwords",
            "B. Victims are forced to click links",
            "C. The messages feel more believable and relevant",
            "D. It avoids using email altogether"
        ],
        "answer": "C. The messages feel more believable and relevant",
    },
    {
        "id": 8,
        "question": "What is 'whale phishing'?",
        "options": [
            "A. A phishing attack aimed at random people",
            "B. A scam involving cryptocurrency",
            "C. A targeted attack on a high-profile individual within an organization",
            "D. A type of malware that infects smartphones"
        ],
        "answer": "C. A targeted attack on a high-profile individual within an organization",
    },
    {
        "id": 9,
        "question": "Why do some phishing emails contain obvious spelling and grammar mistakes?",
        "options": [
            "A. Hackers are usually in a hurry",
            "B. They want to avoid spam filters",
            "C. Errors help them identify less cautious targets",
            "D. It's a tactic to seem friendly"
        ],
        "answer": "C. Errors help them identify less cautious targets",
    },
    {
        "id": 10,
        "question": "Which file type is most suspicious when received in an unexpected email?",
        "options": [
            "A. .pdf",
            "B. .docx",
            "C. .jpg",
            "D. .zip"
        ],
        "answer": "D. .zip",  
        "explanation": "It is difficult to identify what files are stored within them."
    },
    {
        "id": 11,
        "question": "Which of the following is a *common red flag* in phishing emails?",
        "options": [
            "A. Urgent requests for sensitive info",
            "B. A casual greeting and personal tone",
            "C. Perfect grammar",
            "D. Professional logos and formatting"
        ],
        "answer": "A. Urgent requests for sensitive info",
    },
    {
        "id": 12,
        "question": "An email says your account will be locked in 1 hour if you don’t act now. What should you do?",
        "options": [
            "A. Click the link immediately",
            "B. Stay calm and verify with the company’s official website directly",
            "C. Forward it to friends as a warning",
            "D. Reply and ask for more details"
        ],
        "answer": "B. Stay calm and verify with the company’s official website directly",
    }
]


