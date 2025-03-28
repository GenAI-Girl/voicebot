Voicebot
Welcome to the Voicebot project! This voice-based assistant helps users search for skills from a resume-based dataset. The user interacts with the system purely through voice commands in the terminal, and the responses are provided back via voice.(The Voicebot is entirely command-line-based, with voice input/output handled through Python libraries without the need for Flask, UI, or JavaScript)

Overview
The Voicebot is built entirely in Python. It uses Speech Recognition to capture voice input and Text-to-Speech (TTS) to provide voice responses. The system processes voice commands to search for skills within a resume-based dataset and provides the corresponding person's name and contact details. This project does not use any UI or Flask framework, and all interactions occur in the terminal.

Features
Voice Interface: Interact with the bot using voice commands.

Speech Recognition: Captures and processes user queries based on skills.

Text-to-Speech (TTS): Provides voice feedback, including names and contact details.

Integration with a resume-based dataset to retrieve relevant data.

Terminal-based Interaction: Entire interaction is handled via terminal commands (no UI or web framework).

Installation
To set up the Voicebot locally, follow these steps:

Clone the repository to your local machine:

bash
Copy
git clone https://github.com/GenAI-Girl/Voicebot.git
Navigate to the project directory:

bash
Copy
cd voicebot
Install the required Python packages using pip:

bash
Copy
pip install -r requirements.txt
Set up environment variables (if required):

Create a .env file in the project directory.

Define any necessary environment variables (like dataset paths, API keys, etc.).

Run the Python script:

bash
Copy
python app.py
The application will start, and you can interact with the voicebot directly through the terminal.

Requirements
Before running the Voicebot, ensure you have the following Python libraries installed:

SpeechRecognition: For capturing and processing voice input.

gTTS (Google Text-to-Speech): For generating voice responses.

playsound: For playing the generated voice responses.

To install the dependencies listed in requirements.txt, run:

bash
Copy
pip install -r requirements.txt
