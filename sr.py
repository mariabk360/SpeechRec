import streamlit as st
import speech_recognition as sr

# Variable pour stocker l'instance de Recognizer
recognizer = None


def transcribe_speech(selected_api, language):
    global recognizer

    # Initialize recognizer class
    if recognizer is None:
        if selected_api == "Google":
            recognizer = sr.Recognizer()
        elif selected_api == "Google Cloud":
            recognizer = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        recognizer.adjust_for_ambient_noise(source)
        audio_text = recognizer.listen(source)
        st.info("Transcribing...")

        try:
            # Using the selected API for speech recognition
            if selected_api == "Google":
                text = recognizer.recognize_google(audio_text, language=language)
            elif selected_api == "Google Cloud":
                text = recognizer.recognize_google_cloud(
                    audio_text,
                    language=language,
                    credentials_json="speechrec-391719-903ff6c9f009.json",
                )

            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand you."
        except sr.RequestError:
            return "Sorry, my speech recognition service is currently unavailable."


def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Add a selectbox to choose the speech recognition API
    selected_api = st.selectbox(
        "Select Speech Recognition API",
        [
            "Google",
            "Google Cloud",
        ],
    )

    # Add a text input to choose the language
    language = st.text_input(
        "Enter the language you are speaking in (e.g., 'en' for English):"
    )

    if st.button("Stop"):
        global recognizer
        recognizer = None
    # Add a button to trigger speech recognition
    if st.button("Record"):
        text = transcribe_speech(selected_api, language)
        st.write("Transcription: ", text)

        # Add a button to save the transcribed text to a file
        if st.button("Save to File"):
            with open("transcription.txt", "w") as file:
                file.write(text)
            st.write("Transcription saved to 'transcription.txt'.")


if __name__ == "__main__":
    main()
