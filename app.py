import os
import speech_recognition as sr
from gtts import gTTS
import playsound
from voicebot.ingest import ingestdata
from voicebot.retrieval_generation import generation

def capture_audio():
    """
    Capture voice input from the microphone and convert it to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak your question.")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError as e:
        print("Error with the speech recognition service:", e)
        return None

def text_to_speech(text):
    """
    Convert the provided text to speech and play it.
    """
    tts = gTTS(text, lang='en')
    temp_file = "temp_response.mp3"
    tts.save(temp_file)
    playsound.playsound(temp_file, True)
    os.remove(temp_file)

if __name__ == '__main__':
    # Ingest data and initialize your retrieval-generation chain
    vstore, _ = ingestdata(None)
    if vstore is None:
        raise ValueError("Failed to initialize vector store. Check your configuration.")
    
    chain = generation(vstore)
    
    # Loop to continuously capture and respond to voice input
    while True:
        question = capture_audio()
        if question:
            response = chain.invoke(question)
            print("Response:", response)
            text_to_speech(response)
