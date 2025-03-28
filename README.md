Voicebot
Welcome to the Voicebot project! This voice-based assistant is designed to help users search for skills and get relevant contact details from a resume-based dataset. The user interacts with the system using voice commands, and the responses are provided back in the form of voice.

Overview
The Voicebot is built using Python and the Flask framework. It uses Speech Recognition for capturing voice input and Text-to-Speech (TTS) for speaking back the responses to the users. The voicebot queries a resume-based dataset to find information about skills and returns the corresponding person's name and contact details. The voice interactions are seamless, with voice input and output.

Features
Voice Interface for users to interact using voice commands.

Speech Recognition to capture and understand user queries based on skills.

Text-to-Speech (TTS) to provide voice feedback with the desired person's name and contact details.

Integration with a resume-based dataset to retrieve relevant information.

Users can search for skills by asking via voice, and the bot will respond with the matching person's name and contact details.

Installation
To set up the Voicebot locally, follow these steps:

Clone the repository to your local machine:

bash
Copy
git clone https://github.com/GenAI-Girl/voicebot.git
Navigate to the project directory:

bash
Copy
cd voicebot
Install the required Python packages using pip:

bash
Copy
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the project directory.

Define the necessary environment variables such as the dataset path and API keys, if any.

Run the Flask application:

bash
Copy
python app.py
The application will start a local server, and you can begin interacting with the voicebot.

Requirements
Before running the Voicebot, make sure you have the following installed:

Python 3.x

SpeechRecognition for capturing voice input.

gTTS (Google Text-to-Speech) for generating voice responses.

playsound for playing the audio responses.

Make sure to install the dependencies listed in requirements.txt:

bash
Copy
pip install -r requirements.txt
