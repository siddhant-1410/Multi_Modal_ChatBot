# AI Doctor with Vision and Voice

A simple AI medical consultation app where you can talk and show images to get basic medical advice.

## What This Project Does

This app lets you:
- Record your voice describing symptoms
- Upload medical images (like skin problems)
- Get AI-generated medical advice in text and voice format

It's like talking to an AI doctor that can see and hear.

## How It Works

1. You record audio describing your problem
2. You upload an image (optional)
3. AI converts your speech to text
4. AI analyzes your text + image together
5. AI gives medical advice
6. The advice is converted back to speech

## Models Used

- **Whisper-Large-v3**: Converts your voice to text
- **Meta-Llama/Llama-4-Scout-17b**: Analyzes images and provides medical responses
- **Google Text-to-Speech**: Converts AI response to voice

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone 
   ```

2. **Get API Key**
   - Sign up at [Groq](https://groq.com) and get your free API key

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variable**
   ```bash
   export GROQ_API_KEY="your_api_key_here"
   ```
   Or create a `.env` file with:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

5. **Run the App**
   ```bash
   python app.py
   ```

## How to Use

1. Click on the microphone and describe your symptoms
2. Upload an image if you have visible symptoms
3. Wait for the AI to process
4. Read the text response and listen to the audio response

## Files in This Project

- `app.py` - Main app file
- `brain_of_the_doc.py` - Handles image analysis
- `voice_of_the_patient.py` - Processes your voice input
- `voice_of_the_doc.py` - Converts AI response to speech

## Important Note

This is for educational purposes only. Always consult real doctors for medical advice.
