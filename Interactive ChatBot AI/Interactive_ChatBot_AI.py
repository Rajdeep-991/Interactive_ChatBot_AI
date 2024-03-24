import google.generativeai as palm
import pyttsx3
import speech_recognition as sr

with open('Google_API_Key.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

palm.configure(api_key = GOOGLE_API_KEY)
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nChatBot is Listening....\n")
        audio = recognizer.listen(source)

    try:
        user_prompt = recognizer.recognize_google(audio)
        print(f"You\n---\n{user_prompt}")
    
    except sr.UnknownValueError:
        print("ChatBot\n-------\nI could not understand what you said\n")
        exit()
    
    except sr.RequestError as e:
        print("ChatBot\n-------\nCould not connect to Google Speech\n")
        exit()
    
    if user_prompt.lower() in ["Bye", "Exit", "Quit", "bye", "exit", "quit"]:
        print()
        break

    else:
        completion = palm.generate_text(
            model = model,
            prompt = user_prompt,
            max_output_tokens = 2024
        )
        tts_engine = pyttsx3.init()
    
    spoken_response = completion.result.replace('*', '')

    print("\nChatBot\n-------")
    print(spoken_response, "\n\n")

    tts_engine.say(spoken_response)
    tts_engine.runAndWait()