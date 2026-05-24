def ask_qualification_questions():

    answers = {}

    questions = [
        "What type of business are you?",
        "How many team members do you have?",
        "What tools are you currently using?"
    ]

    for question in questions:

        answer = input(f"{question}\n> ")

        answers[question] = answer

    return answers