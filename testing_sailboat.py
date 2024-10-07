# Pre-defined answers
answers = {
    "What types of boats are available?": "We have sailboats, motorboats, and yachts available for rent.",
    "What are the prices?": "Prices vary depending on the boat type and rental duration. Please check our pricing page.",
    "How do I book a boat?": "You can book a boat through our website or by contacting our support team.",
    "What is the cancellation policy?": "You can cancel your booking up to 24 hours in advance for a full refund.",
    "Can I get a refund?": "Refunds are available as per our cancellation policy."
}

def chatbot():
    print("Welcome to the Boat Rental Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = answers.get(user_input, "Chatbot: I'm sorry, I don't understand that.")
        print("Chatbot:", response)

if __name__ == '__main__':
    chatbot()
