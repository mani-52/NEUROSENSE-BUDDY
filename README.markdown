# NeuroSense: Emotion-Aware Conversational AI

## Overview
NeuroSense is a real-time, emotion-aware conversational AI system designed to enhance human-computer interaction by integrating facial expression recognition, speech processing, and adaptive response generation. It leverages **DeepFace** for facial emotion detection, **Google's Speech Recognition API** for voice input, and the **Groq** large language model for generating emotionally aligned, context-sensitive, and often humorous responses.

Unlike conventional AI assistants, NeuroSense dynamically adapts its tone and content based on the user's emotional state:
- **Motivational messages** for sadness.
- **Light humor** for happiness.
- **Calming tones** for anger or frustration.

The system supports both voice and text inputs and delivers spoken responses using the **pyttsx3** text-to-speech engine, creating a natural and immersive conversational experience.

## Features
- **Facial Emotion Detection**: Uses DeepFace to analyze facial expressions in real-time via webcam.
- **Speech Recognition**: Processes voice input using Google's Speech Recognition API.
- **Adaptive Response Generation**: Generates context-sensitive responses with emotional alignment using the Groq LLM.
- **Text-to-Speech**: Outputs spoken responses with pyttsx3 for a seamless conversational flow.
- **Modular Architecture**: Integrates computer vision, natural language processing, and speech synthesis.
- **Applications**: Suitable for mental health support, educational tools, and socially aware virtual agents.

## Installation

### Prerequisites
- Python 3.8+
- Webcam for facial emotion detection
- Microphone for voice input
- Internet connection for Google Speech Recognition API and Groq API

### Dependencies
Install the required Python packages using:
```bash
pip install deepface speechrecognition pyttsx3 groq opencv-python numpy
```

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/neurosense.git
   cd neurosense
   ```

2. **Install Dependencies**:
   Run the above `pip install` command to install all required libraries.

3. **API Keys**:
   - Obtain a **Groq API key** from [xAI](https://x.ai/api).
   - Configure the API key as an environment variable:
     ```bash
     export GROQ_API_KEY='your-api-key'
     ```

4. **System Requirements**:
   - Ensure a webcam and microphone are connected and functional.
   - Install necessary drivers for pyttsx3 (e.g., `espeak` on Linux or `nsss` on macOS).

## Usage
1. **Run the Application**:
   ```bash
   python main.py
   ```

2. **Interact with NeuroSense**:
   - **Voice Input**: Speak into the microphone, and NeuroSense will process your speech.
   - **Text Input**: Alternatively, type your input in the console.
   - **Facial Emotion Detection**: Ensure your webcam is active; NeuroSense will analyze your facial expressions in real-time.
   - **Output**: The system responds with spoken output (via pyttsx3) tailored to your emotional state.

3. **Example Interaction**:
   - User (visibly happy): "Tell me a joke!"
   - NeuroSense: "Why did the computer go to art school? Because it wanted to learn how to draw a better 'byte'! 😄"
   - User (visibly sad): "I'm feeling down today."
   - NeuroSense: "I'm here for you! Let's take a deep breath together and talk about something that sparks joy."

## Project Structure
```
neurosense/
├── main.py                # Main application script
├── emotion_detection.py   # Facial emotion detection using DeepFace
├── speech_processing.py   # Speech recognition and text-to-speech
├── response_generation.py # Emotion-aware response generation with Groq
├── requirements.txt       # List of dependencies
├── README.md             # Project documentation
└── utils/                # Helper functions and utilities
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **DeepFace**: For robust facial emotion detection.
- **Google Speech Recognition API**: For accurate speech-to-text conversion.
- **Groq**: For powerful and context-sensitive language generation.
- **pyttsx3**: For offline text-to-speech capabilities.

## Contact
For questions or feedback, please open an issue on GitHub or contact [your-email@example.com].