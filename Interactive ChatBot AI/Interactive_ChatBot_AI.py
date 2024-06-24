# Import the Google PaLM generative AI library and alias it as 'palm'
import google.generativeai as palm

# Import the pyttsx3 library for text-to-speech conversion
import pyttsx3

# Import the SpeechRecognition library and alias it as 'sr' for speech-to-text conversion
import speech_recognition as sr

# Load Google API key from a file
with open('Google_API_Key.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

# Configure the PaLM API with the loaded API key
palm.configure(api_key = GOOGLE_API_KEY)

# Get a list of available models and select the first one that supports text generation
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

# Main loop to keep the chatbot running
while True:
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("\nChatBot is Listening....\n")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google's speech recognition
        user_prompt = recognizer.recognize_google(audio)
        print(f"You\n---\n{user_prompt}")
    
    except sr.UnknownValueError:
        # Handle case when speech is unintelligible
        print("ChatBot\n-------\nI could not understand what you said\n")
        exit()
    
    except sr.RequestError as e:
        # Handle case when there's a problem with the API request
        print("ChatBot\n-------\nCould not connect to Google Speech\n")
        exit()
    
    # Check for exit commands to break the loop
    if user_prompt.lower() in ["Bye", "Exit", "Quit", "bye", "exit", "quit"]:
        print()
        break

    else:
        # Generate a response using the PaLM text generation model
        completion = palm.generate_text(
            model = model,
            prompt = user_prompt,
            max_output_tokens = 2024)
        tts_engine = pyttsx3.init()
    
    # Clean up the response text
    spoken_response = completion.result.replace('*', '')

    # Print the chatbot's response
    print("\nChatBot\n-------")
    print(spoken_response, "\n\n")

    # Use text-to-speech to speak the response
    tts_engine.say(spoken_response)
    tts_engine.runAndWait()
