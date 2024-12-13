def simple_chatbot(user_input): 
    conversations = { 
        "hi": "Hello! How can I help you?", 
        "how are you": "I'm doing well, thank you. How about you?", 
        "name": "I'm a chatbot. You can call me ChatPy!", 
        "age": "I don't have an age. I'm just a program.", 
        "bye": "Goodbye! Have a great day.", 
        "python": "Python is a fantastic programming language!", 
        "weather": "I'm sorry, I don't have real-time data. You can check a weather website for 
updates.", 
        "help": "I'm here to assist you. Ask me anything!", 
        "thanks": "You're welcome! If you have more questions, feel free to ask.", 
        "default": "I'm not sure how to respond to that. You can ask me something else.", 
        "what is the time now": now, 
    } 
    # Convert user input to lowercase for case-insensitive matching 
    user_input_lower = user_input.lower() 
    # Retrieve the response based on user input 
    response = conversations.get(user_input_lower, conversations["default"]) 
    return response 
# Chatbot interaction loop 
print("Hello! I'm ChatPy, your friendly chatbot.")
print("You can start chatting. Type 'bye' to exit.") 
while True: 
    user_input = input("You: ") 
     
    if user_input.lower() == 'bye': 
        print("ChatPy: Goodbye! Have a great day.") 
        break 
    response = simple_chatbot(user_input) 
    print("ChatPy:", response)
