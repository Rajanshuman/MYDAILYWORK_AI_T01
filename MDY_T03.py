def chatbot():
    print("Welcome to the chatbot! I can help you with some basic queries.")
    print("Type 'hi' or 'hello' to greet me, 'help' to know what I can do, 'quit' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello']:
            print("Bot: Hi! How can I assist you today?")
        elif user_input == 'help':
            print("Bot: I can help you with some basic queries. You can ask me about the weather, time, or just chat with me.")
        elif user_input == 'quit':
            print("Bot: Goodbye! It was nice chatting with you.")
            break
        elif 'weather' in user_input:
            print("Bot: The weather is sunny today! (Note: This is a static response and doesn't actually check the weather.)")
        elif 'time' in user_input:
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"Bot: The current time is {current_time}.")
        else:
            print("Bot: Sorry, I didn't understand that. Please try again!")

if __name__ == "__main__":
    chatbot()