print("Welcome to Codec Technologies Chatbot")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hello! How can I help you?")

    elif "internship" in user:
        print("Bot: We offer AI and Technology internships.")

    elif "course" in user:
        print("Bot: We provide training programs in AI, Python and Web Development.")

    elif "contact" in user:
        print("Bot: Contact us at vaishali@codectechnologies.in")

    elif "bye" in user:
        print("Bot: Thank you for contacting Codec Technologies!")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")