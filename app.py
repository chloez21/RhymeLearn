from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from gtts import gTTS

# Load environment variables from .env
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Available artist styles
ARTIST_STYLES = ["Kendrick Lamar", "Eminem", "Nicki Minaj", "Drake", "Snoop Dogg", "50 Cent"]

def generate(text, artist):
    # Call OpenAI API to generate lyrics
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI trained to convert educational content into engaging rap lyrics."},
            {"role": "user", "content": f"Create lyrics in the style of {artist} based on this textbook content: {text}"}
        ]
    )
    # Extract the message content from the completion object
    response = completion.choices[0].message.content
    return response

def generate_and_speak(text, genre):
    # Generate lyrics and convert to speech
    lyrics = generate(text, genre)
    tts = gTTS(lyrics, lang='en')
    tts.save("output.mp3")
    return lyrics, "output.mp3"

def main():
    # Create a Gradio interface
    iface = gr.Interface(
        theme='sudeepshouche/minimalist',
        fn=generate_and_speak,
        inputs=[
            gr.Textbox(lines=10, label="Textbook Content", placeholder="Enter Textbook Content Here..."),
            gr.Dropdown(choices=ARTIST_STYLES, label="Artist Style")
        ],
        outputs=[
            gr.Textbox(label="Generated Lyrics"),
            gr.Audio(label="Rap Audio Playback")
        ],
        examples=[
            ["The simplest way to do smoothing is to add one to all the n-gram counts, before we normalize them into probabilities...", "Eminem"],
            ["The Industrial Revolution, sometimes divided into the First Industrial Revolution and Second Industrial Revolution...", "Snoop Dogg"],
        ],
        title="RhymeLearn",
        description="Enter textbook content and select a genre to convert it into engaging rap lyrics and hear them!"
    )
    iface.launch()

if __name__ == "__main__":
    main()
