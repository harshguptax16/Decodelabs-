"""
=======================================================================
DecodeLabs - AI Internship : Project 1
AI Chatbot
=======================================================================
"""

import random

exit_command = {'bye','goodbye','quit','exit',"i'm outta here"}
abusive_command = {'fuck you','bitch','asshole','dipshit','motherfuck','bastard','nigge'}
sad_words = {'sad','depressed','unhappy','tired','miserable','bad day','stressed','angry','upset','frustrated','lonely'}
happy_words = {'happy','good','great','awesome','fantastic','amazing','wonderful','excited','joyful','cheerful','good day'}

how_are_you_replies = [
    "I'm just a bunch of if-else statement, but I'm doing great!",
    "Running smoothly, thanks for asking.",
    "Can't Complain - I don't have feelings, but I appreciate you asking"
]

def get_input():
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    return clean_input

def process(user_input, mood: str):
    neutral_responses = {
        "hello": "Hi there, How can I help you today?",
        "bye": "Goodbye!",
        "thank you": "You're Welcome!",
        "who made you": "I was created by an Intern called 'Harsh Gupta'.",
        "your name": "My name is Chitbot, nice to meet you!",
        "joke": "Why did the computer go to the doctor? Because it caught a virus!",
        "bro": "Bro? Yeah I'm here, what's up!",
        "weather": "Sorry, I can't check live weather yet.",
        "what can you do?": "I can chat with you, tell jokes, and adjust my tone to your mood.",
        "good morning": "Good morning! Hope you have a great day!",
        "good night": "Good night! Sleep well.",
        "i am fine": "Good to know! How can I help you today?",
        "who are you?": "I'm Chitbot, your friendly AI chatbot. Built for Project.",
        "sorry": "No worries at all.",
        "love you": "Aww, that's sweet of you!",
    }
    low_responses = {
        "hello": "Heyy... I hope things get better. What's up?",
        "bye": "Take care of yourself. Okay?",
        "thank you": "Anytime. I'm here for you.",
        "who made you": "An Intern called 'Harsh Gupta' made me.",
        "your name": "I'm Chitbot. Here to listen if you need it.",
        "joke": "Here's something light: I told my computer I needed a break. It froze!",
        "bro": "Ok Sorry, my bad",
        "weather": "Not sure about the weather, but I hope it's a bit brighter for you today.",
        "what can you do": "I can just sit here and chat with you for a while, if that  helps.",
        "good morning": "Good morning! Take it slow today, one step at a time.",
        "good night": "Good night! Best well, tomorrow's a new day.",
        "i am fine": "Glad to hear that. I'm still here if that changes.",
        "who are you?": "I'm Chitbot, Just here to give you company for now.",
        "sorry": "You don't need to apologize.",
        "love you": "That means a lot, thank you for saying that.",
    }
    good_responses = {
        "hello": "Heyy! Loved the energy Today!",
        "bye": "See you later! Keep that positive vibe going!",
        "thank you": "You're welcome, Happy to help!",
        "who made you": "An Awesome Intern called 'Harsh Gupta' made me.",
        "your name": "I'm Chitbot, at your service!",
        "joke": "Since you are in a good mood: I told my computer I needed a break. It gave me a KitKat pic!",
        "bro": "Yo! Bro. Let's Goo.",
        "weather": "No live weather updates, but It's looking sunny and bright here!",
        "what can you do": "Loads of Stuff! I can chat, tell jokes, and keep the good vibes going.",
        "good morning": "Good morning! Hope your day is as awesome as you are!",
        "good night": "Good night! Sweet Dreams! End the day on a high note!",
        "i am fine": "Love that for you! Keep it up!",
        "who are you?": "Chitbot - your upbeat AI Buddy for today!",
        "sorry": "No Appologies Needed, all Good!",
        "love you": "Love you too! Buddy!",
    }
    
    if mood == "low":
        responses = low_responses
    elif mood == "good":
        responses = good_responses
    else:
        responses = neutral_responses
        
    reply = responses.get(user_input, "I do not understand")
    return reply

def main():
    print("=" * 50)
    print("              Mood-Based Rule Chitbot")
    print("    A Decode Internship Project by Harsh Gupta")
    print("=" * 50)
    print()
    
    current_mood = "neutral"
    
    print("Bot: Hello! Type 'exit' or 'quit' to end the chat.")
    
    mood_input = input("Bot: Before we start, how are you feeling today? (happy/sad/neutral): ").lower().strip()
    
    if any(word in mood_input for word in happy_words):
        current_mood = "good"
        print("Bot: Great to hear that! Let's keep the good vibes going!")
    elif any(word in mood_input for word in sad_words):
        current_mood = "low"
        print("Bot: I'm sorry to hear that. I'll keep things gentle today.")
    else:
        print("Bot: Alright, let's get started!")
        
    while True:
        user_input = get_input()
        
        if any(word in user_input for word in abusive_command):
            print("Bot: Please refrain from using abusive language.")
        elif any(word in user_input for word in happy_words):
            current_mood = "good"
            print("Bot: Glad to hear that! I'll keep things upbeat now")
        elif any(word in user_input for word in sad_words):
            current_mood = "low"
            print("Bot: I'm sorry to hear that. I'll keep things gentle now.")
        elif "how are you" in user_input:
            reply = random.choice(how_are_you_replies)
            print(f"Bot: {reply}")
        elif user_input in exit_command:
            print("Bot: Goodbye! Take care!")
            break
        elif user_input == "":
            print("Bot: ...I didn't quite catch that. Try typing something.")
        else:
            print(f"Bot: {process(user_input, current_mood)}")

if __name__ == "__main__":
    main()