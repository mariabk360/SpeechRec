import streamlit as st
import speech_recognition as sr


def transcribe_speech(selected_api, language):
    # Initialize recognizer class
    r = sr.Recognizer()
    # Set the selected API
    if selected_api == "Google":
        recognizer = sr.Recognizer()
    elif selected_api == "Microsoft Bing":
        recognizer = sr.Recognizer()
    elif selected_api == "IBM":
        recognizer = sr.Recognizer()
    elif selected_api == "Google Cloud":
        recognizer = sr.Recognizer()
    elif selected_api == "Houndify":
        recognizer = sr.Recognizer()
    elif selected_api == "Sphinx":
        recognizer = sr.Recognizer()
    elif selected_api == "Wit":
        recognizer = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        r.adjust_for_ambient_noise(source)
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # Using the selected API for speech recognition
            if selected_api == "Google":
                text = recognizer.recognize_google(audio_text, language=language)
            elif selected_api == "Microsoft Bing":
                text = recognizer.recognize_bing(audio_text, language=language)
            elif selected_api == "IBM":
                text = recognizer.recognize_ibm(audio_text, language=language)
            elif selected_api == "Google Cloud":
                text = recognizer.recognize_google_cloud(audio_text, language=language)
            elif selected_api == "Houndify":
                text = recognizer.recognize_houndify(audio_text, language=language)
            elif selected_api == "Sphinx":
                text = recognizer.recognize_sphinx(audio_text, language=language)
            elif selected_api == "Wit":
                text = recognizer.recognize_wit(audio_text, language=language)

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
        "Select Speech Recognition API", ["Google"]
    )  # Add more API options if available

    # Add a text input to choose the language
    language = st.text_input(
        "Enter the language you are speaking in (e.g., 'en' for English):"
    )

    # Add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(selected_api, language)
        st.write("Transcription: ", text)

        # Add a button to save the transcribed text to a file
        if st.button("Save to File"):
            with open("transcription.txt", "w") as file:
                file.write(text)
            st.write("Transcription saved to 'transcription.txt'.")


if __name__ == "__main__":
    main()
