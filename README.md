Interactive Chatbot AI
----------------------
Overview :
This project implements a voice-activated AI chatbot using Google's PaLM (Pathways Language Model) for natural language processing and response generation. The chatbot listens to the user's spoken input, processes it using Google's speech recognition service, and responds using text-to-speech synthesis.

Features :
1. Voice Recognition: Utilizes the speech_recognition library to capture and convert speech to text.
2. AI Response Generation: Employs Google's PaLM to generate contextually relevant and coherent text responses.
3. Text-to-Speech: Uses pyttsx3 to convert the AI-generated text responses back to speech for a natural conversational experience.
4. Continuous Interaction: Keeps the conversation going in a loop until the user says "Bye", "Exit", "Quit", "bye", "exit", or "quit".

Requirements :
1. Python 3.x
2. google.generativeai library
3. pyttsx3 library
4. speech_recognition library
5. Google API Key for accessing the PaLM and Speech Recognition services

How to Use :
1. Ensure you have the required Python libraries installed. You can install them using pip --> pip install google-generativeai pyttsx3 SpeechRecognition
2. Save your Google API Key in a file named Google_API_Key.txt.
3. Run the Python script. The chatbot will start listening for your voice input.
4. Speak to the chatbot and listen to its responses.
5. To exit the conversation, say "bye", "exit", or "quit".

How It Works :
1. The script reads the Google API Key from a file.
2. It configures the PaLM API with the provided key.
3. The chatbot enters a loop where it continuously listens for the user's speech.
4. The speech is converted to text using Google's speech recognition service.
5. The text is then sent to the PaLM model to generate a relevant response.
6. The response is spoken out loud using the pyttsx3 library.
7. The loop continues until the user issues an exit command.

Notes :
1. API Key Security: Ensure your Google API Key is kept secure and not exposed in public repositories. Consider using environment variables or encrypted storage for better security.
2. Speech Recognition Limitations: The accuracy of speech recognition may vary depending on the quality of the microphone, background noise, and clarity of speech.
3. Rate Limits: Be aware of any rate limits associated with the Google APIs you are using to avoid service interruptions.
4. Customizations: You can customize the chatbot's behavior by adjusting the parameters in the palm.generate_text method, such as max_output_tokens.
5. Dependencies: Ensure all dependencies are properly installed and compatible with your system to avoid runtime errors.
