"""Simple Python Voice AI Assistant.

Requirements:
  pip install SpeechRecognition pyttsx3 pyaudio

Usage:
  python3 voice_assistant.py
"""

from __future__ import annotations

import datetime as dt
import webbrowser

import pyttsx3
import speech_recognition as sr


class VoiceAssistant:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)

    def speak(self, message: str) -> None:
        print(f"Assistant: {message}")
        self.engine.say(message)
        self.engine.runAndWait()

    def listen(self) -> str:
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower().strip()
        except sr.UnknownValueError:
            self.speak("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            self.speak("Speech service is unavailable right now.")
            return ""

    def handle_command(self, command: str) -> bool:
        if not command:
            return True

        if "exit" in command or "quit" in command or "stop" in command:
            self.speak("Goodbye!")
            return False

        if "hello" in command or "hi" in command:
            self.speak("Hello! How can I help you?")
            return True

        if "time" in command:
            now = dt.datetime.now().strftime("%I:%M %p")
            self.speak(f"The time is {now}.")
            return True

        if "date" in command or "day" in command:
            today = dt.datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {today}.")
            return True

        if "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            self.speak("Opening YouTube.")
            return True

        if "open google" in command:
            webbrowser.open("https://www.google.com")
            self.speak("Opening Google.")
            return True

        if "search for" in command:
            query = command.split("search for", 1)[1].strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
                self.speak(f"Searching for {query}.")
            else:
                self.speak("Please tell me what to search for.")
            return True

        self.speak("I can tell time and date, open Google or YouTube, and search the web.")
        return True

    def run(self) -> None:
        self.speak("Voice assistant started. Say a command, or say exit to quit.")
        running = True
        while running:
            command = self.listen()
            running = self.handle_command(command)


if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
