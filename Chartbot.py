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

    elif "fees" in user:
        print("Bot: please contact our office for fee details.") 

    elif "location" in user:
        print("Bot: our office is located in salem.")

    elif "timing" in user:
        print("Bot: our office timing is 9 am to 6 pm.")

    elif "website" in user:
       print("Bot: visit our website at www.codectechnologies .in ")

    elif "services" in user:
        print("Bot : we provide internships,cources , project guidence and training .") 

    elif "certification" in user:
        print("Bot: certificate will provide after successful completion.")

    elif "duration" in user:
        print("Bot: Internsip duration is 1 month.")

    elif "projects" in user:
        print("Bot: we provide real-time project experience.")              

    elif "bye" in user:
        print("Bot: Thank you for contacting Codec Technologies!")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")