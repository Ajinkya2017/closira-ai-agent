def generate_summary(conversation, qualification_data, escalation_data):

    summary = f"""
========== Conversation Summary ==========

Customer Intent:
{conversation}

Lead Qualification:
"""

    for key, value in qualification_data.items():

        summary += f"\n- {key}: {value}"

    summary += f"""

Escalation Status:
{escalation_data['escalate']}

Reason:
{escalation_data['reason']}

Recommended Next Action:
"""

    if escalation_data["escalate"]:
        summary += "\nHuman agent follow-up required."
    else:
        summary += "\nContinue automated engagement."

    return summary