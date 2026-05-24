from agents.faq_agent import faq_response
from agents.escalation_agent import check_escalation
from agents.qualification_agent import ask_qualification_questions
from agents.summary_agent import generate_summary


def main():

    print("===== Closira AI Support Agent =====\n")

    conversation_history = []

    escalation_result = {
        "escalate": False,
        "reason": None
    }

    while True:

        user_input = input("Customer: ")

        if user_input.lower() == "exit":
            break

        conversation_history.append(f"Customer: {user_input}")

        escalation_check = check_escalation(user_input)

        if escalation_check["escalate"]:

            escalation_result = escalation_check

            print("\nAI Agent:")
            print("I am escalating this conversation to a human agent.")
            print(f"Reason: {escalation_check['reason']}\n")

            conversation_history.append(
                f"Escalation Triggered: {escalation_check['reason']}"
            )

            continue

        response = faq_response(user_input)

        print("\nAI Agent:")
        print(response)
        print()

        conversation_history.append(f"AI: {response}")

    print("\n===== Lead Qualification =====\n")

    qualification_data = ask_qualification_questions()

    summary = generate_summary(
        "\n".join(conversation_history),
        qualification_data,
        escalation_result
    )

    print(summary)


if __name__ == "__main__":
    main()