def get_bot_response(user_input):
    """Function to process user input and return a rule-based response using if-elif."""
    # Convert input to lowercase and strip whitespace for easy matching
    user_input = user_input.lower().strip()

    # Rule-based logic using if-elif
    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "what is your name" in user_input or "who are you" in user_input:
        return "I'm a basic rule-based Python Chatbot."
    elif "help" in user_input:
        return "I can answer basic greetings! Try saying 'hello', 'how are you', or 'bye'."
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Try asking something else!"


def start_chatbot():
    """Main function to run the chatbot loop and manage input/output."""
    print("========================================")
    print("         BASIC RULE-BASED CHATBOT       ")
    print("========================================")
    print("Chatbot: Hello! I'm here to chat. (Type 'bye' to exit)\n")

    # Main Chat Loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Get response using function
        response = get_bot_response(user_input)

        # Print chatbot output
        print(f"Chatbot: {response}\n")

        # Exit loop if user says bye
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


# Run the chatbot program
if __name__ == "__main__":
    start_chatbot()