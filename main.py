import webbrowser
import pyttsx3
import musicLibrary

engine = pyttsx3.init()

# Function to make assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Assistant:", text)

# Predefined responses
def predefinedReplies(command):
    command = command.lower()
    if command in ["hello", "hi"]:
        speak("Hello! How are you?")
        return True
    elif command in ["bye", "exit", "quit"]:
        speak("Goodbye! Have a nice day.")
        return "exit"
    return False

# Process main commands
def processCommand(c):
    c = c.lower()

    # First check predefined replies
    result = predefinedReplies(c)
    if result == "exit":
        return "exit"
    elif result:
        return

    # Custom commands
    if "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        if song in musicLibrary.music:
            speak("Playing " + song)
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    else:
        speak("Sorry, I don’t understand that command.")

if __name__ == "__main__":
    speak("Chatbot Activated. Type your command below:")

    while True:
        command = input("You: ")
        if processCommand(command) == "exit":
            break
