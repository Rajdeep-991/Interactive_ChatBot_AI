Interactive ChatBot AI
----------------------

Overview
--------
This project implements a voice-activated AI chatbot using Google's PaLM (Pathways Language Model) for natural language processing and response generation. The chatbot listens to the user's spoken input, processes it using Google's speech recognition service, and responds using text-to-speech synthesis.

Features
--------
- Voice Recognition: Utilizes the speech_recognition library to capture and convert speech to text.
- AI Response Generation: Employs Google's PaLM to generate contextually relevant and coherent text responses.
- Text-to-Speech: Uses pyttsx3 to convert the AI-generated text responses back to speech for a natural conversational experience.
- Continuous Interaction: Keeps the conversation going in a loop until the user says any of the following: "Bye", "Exit", "Quit", "bye", "exit", or "quit".

Requirements
------------
- Python 3.x
- google.generativeai library
- pyttsx3 library
- speech_recognition library
- Google API Key for accessing the PaLM and Speech Recognition services

How To Use
----------
- Ensure you have the required Python libraries installed. You can install them using pip:

  pip install google-generativeai pyttsx3 SpeechRecognition
- Save your Google API Key in a file named Google_API_Key.txt.
- Run the Python script. The chatbot will start listening for your voice input.
- Speak to the chatbot and listen to its responses.
- To exit the conversation, say any of the following: "Bye", "Exit", "Quit", "bye", "exit", or "quit".

How It Works
------------
- The script reads the Google API Key from a file.
- It configures the PaLM API with the provided key.
- The chatbot enters a loop where it continuously listens for the user's speech.
- The speech is converted to text using Google's speech recognition service.
- The text is then sent to the PaLM model to generate a relevant response.
- The response is spoken out loud using the pyttsx3 library.
- The loop continues until the user issues an exit command.

Notes
-----
- API Key Security: Ensure your Google API Key is kept secure and not exposed in public repositories by considering the use of environment variables or encrypted storage for better security.
- Speech Recognition Limitations: The accuracy of speech recognition may vary depending on the quality of the microphone, background noise, and clarity of speech.
- Rate Limits: Be aware of any rate limits associated with the Google APIs you are using to avoid service interruptions.
- Customizations: You can customize the chatbot's behavior by adjusting the parameters in the palm.generate_text method, such as max_output_tokens.
- Dependencies: Ensure all dependencies are properly installed and compatible with your system to avoid runtime errors.
