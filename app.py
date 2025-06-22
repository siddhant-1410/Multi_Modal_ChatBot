# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#VoiceBot UI with Gradio
import os
import gradio as gr

from brain_of_the_doc import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doc import text_to_speech_with_gtts

#load_dotenv()

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


import time

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    doctor_response = "No image provided for me to analyze"
    if image_filepath:
       
        wait_time = 0
        while not os.path.exists(image_filepath) and wait_time < 5:
            time.sleep(0.1)
            wait_time += 0.1

        if os.path.exists(image_filepath):
            encoded = encode_image(image_filepath)
            doctor_response = analyze_image_with_query(
                query=system_prompt + speech_to_text_output, 
                encoded_image=encoded, 
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )

    audio_file_path = text_to_speech_with_gtts(
        input_text=doctor_response, 
        mp3_path="final.mp3",
        wav_path="final.wav"
    ) 

    return speech_to_text_output, doctor_response, audio_file_path



# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Voice Response")  # Removed the hardcoded "Temp.mp3"
    ],
    title="Doctor - AI - Vision & Voice"
)

iface.launch(debug=True)
