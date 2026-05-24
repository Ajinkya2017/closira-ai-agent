ESCALATION_KEYWORDS = [
    "angry",
    "refund",
    "complaint",
    "manager",
    "human",
    "lawsuit",
    "terrible",
    "bad service",
    "not happy",
    "medical",
    "discount",
    "negotiate"
]


def check_escalation(user_input):

    user_input = user_input.lower()

    for keyword in ESCALATION_KEYWORDS:

        if keyword in user_input:

            return {
                "escalate": True,
                "reason": f"Detected escalation keyword: {keyword}"
            }

    return {
        "escalate": False,
        "reason": None
    }