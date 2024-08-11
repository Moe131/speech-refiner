# Speech Refiner

Welcome to the **Speech Refiner** repository! This project leverages the power of AI, specifically the GPT-4 language model, to help you improve your English speaking skills. By analyzing your recorded speech, the system provides refined feedback and suggestions for enhancing clarity and pronunciation.

![Screen Shot 2024-08-06 at 16 28 28](https://github.com/user-attachments/assets/a296775d-9134-4c50-93a7-a344f0c032a0)


## Features

- **Record Audio**: Capture your voice using your microphone.
- **AI-Powered Refinement**: Utilize the GPT-4 model to analyze and refine your speech, offering feedback on grammar, vocabulary, and pronunciation.
- **Playback**: Listen to your recordings to review your progress.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) (for backend if applicable)
- [Flask](https://flask.palletsprojects.com/) (if using Flask for the server)
- Web browser (for accessing the frontend interface)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/speech-refiner.git
   cd speech-refiner

2. **Install Dependencies**:

   ```bash
    pip install -r requirements.txt

3. **set OpenAI API key in `.env` file**:
    ```sh
    OPENAI_API_KEY=YOUR_OPENAI_KEY
    ```
4. **Run the app**:
    ```sh
    python3 app.py
    ```
    
## Usage
- Start Recording: Click the "Start recording" button to begin recording your speech.
- Stop Recording: Click the "Stop recording" button to end the recording.
- Listen: Once recording is complete, listen to your recorded audio to review your speech.
- Refine: Click the "Refine" button to submit your recording for AI-powered analysis and feedback.

## AI-Powered Refinement
The core feature of Speech Refiner is its use of GPT-4, a state-of-the-art language model, to analyze your speech. This AI-powered tool provides detailed feedback on:
