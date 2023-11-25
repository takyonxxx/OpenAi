# Install the gTTS library if you haven't already

# conversation_handler.py
import threading
from gpt2_chatbot import GPT2Chatbot
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os


class ConversationHandler:
    def __init__(self):
        # Initialize speech recognition and GPT-2 chatbot objects
        self.recognizer = sr.Recognizer()
        self.gpt2_chatbot = GPT2Chatbot()

        # Initialize Google Translate translator
        self.translator = Translator()

    def translate_to_turkish(self, text):
        # Translate text to Turkish using Google Translate
        translation = self.translator.translate(text, dest="tr")
        return translation.text

    def recognize_continuous_speech(self, timeout=None):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while True:
                try:
                    print("Listening...")
                    audio_data = self.recognizer.listen(source, timeout=timeout)
                    recognized_text = self.recognizer.recognize_google(audio_data, language="en")
                    if recognized_text:
                        print(f"You said: {recognized_text}")
                        # Use translated text as input for GPT-2 chatbot
                        response = self.gpt2_chatbot.generate_response(recognized_text)
                        # Convert GPT-2 response to speech
                        self.text_to_speech(response)

                except sr.UnknownValueError:
                    print("Not understood...")
                    self.text_to_speech("Not understood.")
                except sr.RequestError:
                    print("Error connecting to the Google API. Check your internet connection.")
                    self.text_to_speech("Error connecting to the Google API. Check your internet connection.")
                except sr.WaitTimeoutError:
                    pass  # Handle if needed

    def text_to_speech(self, text):
        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang='en')
        tts_file_path = "response.mp3"
        tts.save(tts_file_path)

        # Check if the file was successfully created before playing it
        if os.path.exists(tts_file_path):
            # Play the generated speech using ALSA
            os.system(f"mpg123 {tts_file_path}")
        else:
            print("Error: Failed to create response.mp3")

        print("GPT-2 Chatbot:", text)

    def start_conversation(self, timeout):
        # Start conversation loop in a separate thread
        conversation_thread = threading.Thread(target=self.recognize_continuous_speech, args=(timeout,))
        conversation_thread.start()
