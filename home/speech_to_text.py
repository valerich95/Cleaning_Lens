import speech_recognition as sr

def speech_to_text(input_query_model):
    recognizer = sr.Recognizer()

    # Path to the WAV file you want to transcribe
    audio_file = input_query_model.user_voice

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Adjust the recognizer for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        try:
            # Recognize the speech using the recognizer
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)  # You can use other engines too

            # Print the transcribed text
            setattr( input_query_model , 'search_query' , text)
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return  f"Could not request results from Google Speech Recognition service; {e}"

    # You can replace `recognize_google` with other available recognizers in the library.
