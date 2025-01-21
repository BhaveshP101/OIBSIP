import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)  

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio) 
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return None

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            if "exit" in command.lower() or "stop" in command.lower():
                speak("Goodbye! Have a great day.")
                break
            else:
                speak(f"You said: {command}")

if __name__ == "__main__":
    main()
