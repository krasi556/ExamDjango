import random

raiting_messages = {
    1: [
        "But at least it fixed it, so that's nice.",
        "But the invoice was beautifully formatted.",
        "But he smiled through the entire disaster.",
        "But nothing exploded. Technically.",
        "But the coffee he made while 'debugging' was genuinely excellent.",
        "But I respect the confidence.",
        "But now I know exactly what not to do.",
        "But he did apologize. Eventually. Sort of.",
        "But the chaos had a certain rhythm to it.",
    ],
    2: [
        "But he's very punctual about being late.",
        "But I'm still recommending him, mostly out of pity.",
        "But the bugs really had personality.",
        "But he answers emails. Eventually.",
        "But I'll allow it, just this once.",
        "But he tried. I think.",
        "But the price was right, if nothing else was.",
        "But it compiles, which is more than I expected.",
        "But I've definitely seen worse. Somewhere.",
    ],
    3: [
        "But I still recommend them due to how cheap it is.",
        "But it got the job done, more or less.",
        "But he's reliable, if nothing else.",
        "But nobody panicked, which counts for something.",
        "But it works, and really, that's the whole job.",
        "But I'd hire him again, out of sheer habit.",
        "But he never once blamed the intern.",
        "But three stars is basically a passing grade.",
        "But at least he showed up. Every time.",
    ],
    4: [
        "But I'm docking a star on principle.",
        "But nobody's perfect. Except maybe him.",
        "But I'm still waiting for the catch.",
        "But even the AI looked a little suspicious.",
        "But he really should brag about this more.",
        "But I checked twice, just in case.",
        "But that last star is staying hidden. For now.",
        "But I'm already telling my friends. Quietly.",
    ],
    5: [
        "But I'm still looking for the catch. There isn't one.",
        "But I may have cried a little.",
        "But my AI has formally requested a recount.",
        "But I've already recommended him to everyone I know.",
        "But I'm framing this review.",
        "But my only complaint is that I have no complaints.",
        "But I checked. He's definitely human.",
        "But now every other expert has something to live up to.",
    ],

}


def scam_messages(rating, text):
    outcome = random.choice(raiting_messages[rating])
    cleaned_up_text = text.strip() if text.strip().endswith(('.', '!', '?')) else f"{text.strip()}."
    text = f"{cleaned_up_text} {outcome}".strip()
    return text
