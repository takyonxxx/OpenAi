# continuous_speech_to_text.py

import speech_recognition as sr


class ContinuousSpeechToText:
    def __init__(self, language="tr-TR"):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language

    def check_microphone(self):
        if not sr.Microphone.list_microphone_names():
            print("No microphones found. Make sure a microphone is connected and recognized by your system.")
            return False
        return True

    def recognize_continuous_speech(self):
        if not self.check_microphone():
            return None

        print("Listening...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

        try:
            while True:
                with self.microphone as source:
                    audio = self.recognizer.listen(source)

                try:
                    text = self.recognizer.recognize_google(audio, language=self.language)
                    print(f"You said: {text}")
                    return text
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")
                except sr.RequestError as e:
                    print(f"Error with the speech recognition service; {e}")

        except KeyboardInterrupt:
            print("Stopped listening.")
            return None
