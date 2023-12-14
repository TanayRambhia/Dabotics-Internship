def get_response(user_input):
    # Define predefined rules for the chatbot
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! How can I assist you today?",
        "how are you?": "I'm good, thank you. How about you?",
        "fine": "Great to hear that!",
        "what's your name?": "I'm a chatbot. You can call me ChatMaster!",
        "bye": "Goodbye! Have a nice day!",
        "thanks": "You're welcome!",
        "help": "Sure, what do you need help with?",
        "what can you do?": "I can assist you with information, answer questions, or guide you. Feel free to ask!",
        "where are you from?": "I exist in the digital world! :)"
        # Add more predefined responses based on expected user input
    }
    
    # Check if the user input matches any predefined rule
    for key in responses:
        if user_input.lower() == key:
            return responses[key]
    
    # Fallback response if no match found
    return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Chatbot conversation loop
def chatbot():
    print("Chatbot: Hello! How can I assist you today? Type 'bye' to exit.")
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
