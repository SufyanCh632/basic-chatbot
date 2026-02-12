#Import the regular expression module to handle pattern matching
import re 

#A dictionary that maps keywords to predefined responses
responses = {
"hello": "Hi there! How can I assist you today?",
"hi": "Hello! How can I help you?",
"how are you": "I'm just a bot, but I'm doing great! How about you?",
"what is your name": "I'm a chatbot created to assist you.",
"help": "Sure, I'm here to help. What do you need assistance with?",
"bye": "Goodbye! Have a great day!",
"thank you": "You're welcome! I'm happy to help.",
"default": "I'm not sure I understand. Could you please rephrase?"
}

#Function to find appropriate response based on the user's input
def chatbot_response(user_input):
	#Convert user input to lowercase to make matching case-insensitive
	user_input = user_input.lower()

	for keyword in responses:
		if re.search(keyword, user_input):
			return responses[keyword]

	return responses["default"]

#Main Function to run the chatbot
def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (type 'bye' to exit)")

    while True:
        #Get user input
        user_input = input("You: ")

        # If user types 'bye', exit the loop
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break

        #get Chatbot's response based on user input
        response = chatbot_response(user_input)

        #Print Chatbot's response
        print(f"Chatbot: {response}")

#Run the Chatbot
chatbot()

