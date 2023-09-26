# Define a function to handle user queries
def chatbot():
    while True:
        user_input = input("You: ").lower()  # Convert user input to lowercase for easier processing

        if "hello" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "bye" in user_input:
            print("Chatbot: Goodbye!")
            break  # Exit the loop when the user says goodbye
        elif "calculate" in user_input:
            try:
                expression = user_input.replace("calculate", "")
                result = eval(expression)
                print(f"Chatbot: The result is {result}")
            except Exception as e:
                print("Chatbot: Sorry, I couldn't calculate that.")
        elif "true or false" in user_input:
            # Example: Answering logical questions
            if "python is a programming language" in user_input:
                print("Chatbot: True")
            elif "water is a gas" in user_input:
                print("Chatbot: False")
            else:
                print("Chatbot: I'm not sure about that one.")
        else:
            print("Chatbot: I'm not sure how to respond to that. Ask me something else.")

if __name__ == "__main__":
    print("Chatbot: Hello! I'm your chatbot. Type 'bye' to exit.")
    chatbot()
