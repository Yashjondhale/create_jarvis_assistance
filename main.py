import pyttsx3  
import speech_recognition as sr 
import pyjokes  
import wikipedia as w  
import pywhatkit as kit  
import datetime  
import webbrowser  
import pyaudio  

engine = pyttsx3.init()  
def speak(text):
    
    engine.say(text)  
    engine.runAndWait()  

def listen():
    
    recognizer = sr.Recognizer()  # Create an instance of the recognizer.
    with sr.Microphone() as source: 
        print("Listening...")  
        audio = recognizer.listen(source)  
        try:
            command = recognizer.recognize_google(audio)  
            print(f"You said: {command}") 
            return command.lower()  # Return the command in lowercase for uniformity.
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.") 
            return None  # Return None if recognition fails.
        except sr.RequestError:
            speak("Sorry, my speech service is down.")  # Handle API request errors.
            return None  # Return None if there's an issue with the service.

def respond_to_command(command):
   
    if 'time' in command:
       
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")  

    elif 'joke' in command:
        
        joke = pyjokes.get_joke()  
        speak(joke)  

    elif 'wikipedia' in command:
      
        speak("What would you like to know about?") 
        topic = listen()  # Listen for the topic.
        if topic:
            summary = w.summary(topic,sentences=2)  
            print("According to wikipedia ...")
            speak(summary)  # Speak the summary.

    elif 'play' in command:
        # If the command requests to play a song.
        song = command.replace("play", "").strip()  
        speak(f"Playing {song}") 
        kit.playonyt(song) 
    elif 'open' in command:
      
        site = command.replace("open", "").strip() 
        url = f"https://{site}.com"  
        webbrowser.open(url)  
        speak(f"Opening {site}")  

    elif 'exit' in command or 'stop' in command:
        # If the command requests to exit or stop the assistant.
        speak("Jay Shree ram! good bye ")  # Speak a farewell message.
        return False  # Return False to indicate the assistant should stop.

    else:
        # If the command is unrecognized.
        speak("I'm not sure how to respond to that.")  
    
    return True  # Return True to continue listening for further commands.

if __name__ == "__main__":
    speak("Hello, I am jarvis your personal assistant ")  # Introduce the assistant at the start.
    active = True  # Set a flag to keep the assistant running.

    while active:
        command = listen()  
        if command:
            active = respond_to_command(command)  # Process the command and update the active status.
