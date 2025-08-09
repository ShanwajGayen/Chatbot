def get_bot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I didn't understand that. Try saying 'hello', 'how are you', or 'bye'."

def chatbot():
    print("🤖 Chatbot: Hello! Type something to start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("🤖 Chatbot:", response)

        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    chatbot()