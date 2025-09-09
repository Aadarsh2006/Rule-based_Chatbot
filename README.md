# Simple Python Chatbot

This is a **text-based chatbot assistant** built in Python.  
It can respond to predefined commands like greetings (*hello, hi*) and exit commands (*bye, quit, exit*),  
as well as perform tasks like opening websites or playing music from a predefined library.  

---

## ✨ Features
- Responds to basic commands:
  - `hello`, `hi` → Greets the user  
  - `bye`, `exit`, `quit` → Exits the chatbot  
- Can open popular websites:
  - `open youtube` → Opens YouTube  
  - `open google` → Opens Google  
  - `open github` → Opens GitHub  
- Can play music from a predefined library (`musicLibrary.py`)  
- Text + Voice responses (using **pyttsx3**)  

---

## 📂 Project Structure
├── chatbot.py # Main chatbot code
├── musicLibrary.py # Dictionary of songs with links
└── README.md # Project documentation

---

## How to Run

- Clone this repository
- Make sure you have a musicLibrary.py file with songs in dictionary format.
- for example:
music = {
    "song1": "https://link-to-song1",
    "song2": "https://link-to-song2"
}

- Run the chatbot
- Start typing your commands in the terminal.

---

## 📌 Tech Stack
- Python
- pyttsx3 (for text-to-speech)
- webbrowser (to open websites)

---

## 🔮 Future Improvements
- Add more predefined responses
- Connect with APIs (e.g., weather, news)
- GUI-based chatbot interface
- Continuous conversation memory

## Author
- Aadarsh Jha
- Linkedin : www.linkedin.com/in/aadarshjha09
