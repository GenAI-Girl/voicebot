import os
import speech_recognition as sr
from gtts import gTTS
import playsound
from voicebot.ingest import ingestdata
from voicebot.retrieval_generation import generation

def capture_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak your question.")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print("Error with the speech recognition service:", e)
        return None

def text_to_speech(text):
    tts = gTTS(text, lang='en')
    filename = "temp_audio.mp3"
    tts.save(filename)
    playsound.playsound(filename, True)
    os.remove(filename)

if __name__ == '__main__':
    # Initialize your retrieval-generation chain
    vstore, _ = ingestdata(None)
    if vstore is None:
        raise ValueError("Failed to initialize Pinecone vector store. Check your configuration.")
    
    chain = generation(vstore)
    
    # Capture microphone input via Python
    user_input = capture_audio()
    if user_input:
        # Get the text response using your chain
        response_text = chain.invoke(user_input)
        print("Response:", response_text)
        # Convert and play the response as speech
        text_to_speech(response_text)
