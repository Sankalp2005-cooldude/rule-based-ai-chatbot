def main():
    print("Hello from rule-based-chatbot!")


if __name__ == "__main__":
    main()

from chatbot.bot import get_response


print("=" * 40)
print("Welcome to DecodeBot 🤖")
print("Type 'bye' to exit")
print("=" * 40)

while True:

    user_message = input("\nYou: ")

    if user_message.lower().strip() == "bye":
        print("Bot: Goodbye!")
        break

    reply = get_response(user_message)

    print("Bot:", reply)