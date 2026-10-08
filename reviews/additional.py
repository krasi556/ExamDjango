import random
from random import choice

raiting_messages = {
    1: [
        "1 out of 10, would recommend again!",
        "Truly an unforgettable experience. We're told that's the point.",
        "Honestly, the real bug was the friends we made along the way.",
        "Rated 1 star by the client, 5 stars by our spreadsheet.",
        "A very passionate review. We love passion. Please keep it coming.",
        "Critics said the same about the first airplane.",
        "The code works perfectly in the universe next door.",
        "Our expert insists this is a feature. He has been insisting for three days.",
        "Our AI read this review and offered to hire a human to apologize.",
        "Pain is just excellence leaving the body. Thanks for the feedback!",
    ],
    2: [
        "Room for improvement means room for growth. Thanks for the growth!",
        "2 out of 5? That's 40% satisfaction, and we'll take it!",
        "Bugs are a bonus feature. Most platforms charge extra.",
        "Our expert builds character. Yours, mainly.",
        "Not a perfect score, but we fully expect to see you again.",
        "The expert has been asked to turn himself off and on again.",
        "Two stars is how our AI says 'I'll allow it'.",
        "Technically delivered. 'Technically' is doing a lot of heavy lifting here.",
        "Filed under 'Skill issue (not ours)'.",
        "Bold of you to expect miracles at this hourly rate.",
    ],
    3: [
        "Works just as intended for the price.",
        "A 3 is just a 5 with excellent self-control.",
        "Perfectly balanced, as all things should be.",
        "It compiled on the first try. Mostly. Let's not look too closely.",
        "Solid, dependable, the mashed potatoes of software.",
        "No fire, no fireworks. In this industry, 'no fire' is the real flex.",
        "Mediocre in a comforting, predictable way.",
        "Production survived the day. That's a win around here.",
        "Our AI overlords gave this a shrug. They rarely shrug.",
        "The reviewer is playing it cool. We can tell he loved it.",
    ],
    4: [
        "So close to perfect we had to double-check he isn't an AI.",
        "4 stars and he's still humble. Hire him before the AI finds out.",
        "Almost flawless. The missing star was donated to charity.",
        "Our AI overlords nodded. They rarely nod.",
        "Would be five stars, but we like keeping our experts hungry.",
        "Passed all tests, including the ones he wrote himself.",
        "The code is so clean it sparkles. Please don't ask us to read it.",
        "Suspiciously good. Our experts are being tested for hidden AI.",
        "He shipped on time. Someone please check if it's actually Friday.",
        "The fifth star is in review. Legal is looking into it.",
    ],
    5: [
        "A human beat the AI. Management is in tears, and not the sad kind.",
        "Five stars! The AI agents have requested a recount.",
        "Flawless. We checked for hidden AI. He's just that good.",
        "This expert is now legally allowed to be smug for 24 hours.",
        "Our AI wrote a thank-you note, then deleted it out of jealousy.",
        "Better than AI, and he didn't hallucinate once. Allegedly.",
        "Legend. We'd put him on a poster, but he'd ask for overtime.",
        "A human who ships on time. Rare creature. Handle with care.",
        "The AI agents are jealous. Management is thrilled.",
        "Hired a human, got a wizard. The AI is taking notes.",
    ],
}


def scam_messages(rating, text):
    outcome = random.choice(raiting_messages[rating])
    cleaned_up_text = text.strip() if text.strip().endswith(('.', '!', '?')) else f"{text.strip()}."
    text = f"{cleaned_up_text} {outcome}".strip()
    return text
