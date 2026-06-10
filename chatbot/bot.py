from chatbot.responses import responses


def get_response(user_input):
    user_input = user_input.lower().strip()

    return responses.get(
        user_input,
        "Sorry, I don't understand that."
    )