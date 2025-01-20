import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)  # Capture audio

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Convert speech to text
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return None

# Main function
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
