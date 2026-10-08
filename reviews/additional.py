import random
from random import choice


raiting_messages = {
    1: [
        "1 out of 5, would recommend again!",
        "Truly an unforgettable experience. I'm trying very hard to forget it.",
        "Honestly, the real bug was the friends I made along the way.",
        "Rated 1 star by me, 5 stars by my therapist's invoice.",
        "I'm writing this with passion. Mostly the kind with capital letters.",
        "They said the same about the first airplane. Mine also crashed.",
        "The code works perfectly in the universe next door.",
        "The expert insists this is a feature. He has been insisting for three days.",
        "I asked my AI to review his work. It offered to hire a human to apologize.",

    ],
    2: [
        "Room for improvement means room for growth. I've seen a lot of room.",
        "2 out of 5? That's 40% satisfaction, and I'm being generous!",
        "The bugs were a bonus feature. Most freelancers charge extra.",
        "This expert builds character. Mine, mainly.",
        "Not a perfect score, but I'll probably hire him again. I'm an optimist.",
        "I asked him to turn it off and on again. He's still thinking about it.",
        "Two stars is how I say 'I'll allow it'.",
        "Technically delivered. 'Technically' is doing a lot of heavy lifting here.",
        "Filed under 'Skill issue (his)'.",
        "Bold of me to expect miracles at this hourly rate.",
    ],
    3: [
        "Works just as intended. For the price.",
        "A 3 is just a 5 with excellent self-control.",
        "Perfectly balanced, as all things should be.",
        "It compiled on the first try. Mostly. I'm not looking too closely.",
        "Solid, dependable, the mashed potatoes of software.",
        "No fire, no fireworks. In this industry, 'no fire' is the real flex.",
        "Mediocre in a comforting, predictable way.",
        "My production survived the day. That's a win around here.",
        "I showed it to my AI. It shrugged. It rarely shrugs.",
        "I'm playing it cool. He doesn't need to know I loved it.",
    ],
    4: [
        "So close to perfect I had to double-check he isn't an AI.",
        "4 stars and he's still humble. Hire him before the AI finds out.",
        "Almost flawless. The missing star was donated to charity.",
        "My AI overlords nodded. They rarely nod.",
        "Would be five stars, but I like keeping my experts hungry.",
        "Passed all tests, including the ones he wrote himself.",
        "The code is so clean it sparkles. Please don't ask me to read it.",
        "Suspiciously good. I'm having him tested for hidden AI.",
        "He shipped on time. Someone please check if it's actually Friday.",
        "The fifth star is in review. My lawyer is looking into it.",
    ],
    5: [
        "A human beat the AI. I'm in tears, and not the sad kind.",
        "Five stars! My AI agents have requested a recount.",
        "Flawless. I checked for hidden AI. He's just that good.",
        "This expert is now legally allowed to be smug for 24 hours.",
        "My AI wrote a thank-you note, then deleted it out of jealousy.",
        "Better than AI, and he didn't hallucinate once. Allegedly.",
        "Legend. I'd put him on a poster, but he'd ask for overtime.",
        "A human who ships on time. Rare creature. Handle with care.",
        "My AI agents are jealous. I'm thrilled.",
        "Hired a human, got a wizard. The AI is taking notes.",
    ],
}

def scam_messages(rating, text):
    outcome = random.choice(raiting_messages[rating])
    cleaned_up_text = text.strip() if text.strip().endswith(('.', '!', '?')) else f"{text.strip()}."
    text = f"{cleaned_up_text} {outcome}".strip()
    return text
