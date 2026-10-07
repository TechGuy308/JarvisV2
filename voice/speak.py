#Manage speaking

import asyncio
import edge_tts
import os
import pygame
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from elevenlabs.play import play
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(dotenv_path="data/.env")
api_key = os.getenv("ELEVEN_LABS_API_KEY")
client = ElevenLabs(api_key=api_key)

pygame.mixer.init()
class Voice():
    def __init__(self):
        pass
    
    def run(self, reply):
        
        asyncio.run(self.speak(reply))
        

    def speak(self, text):
        print("speaking")
        # en-GB-ThomasNeural or en-GB-RyanNeural
        #tts = edge_tts.Communicate(text=text, voice="en-GB-ThomasNeural", rate="+3%", pitch="-7Hz")
        
        #await tts.save("speech.mp3")
        #sound = pygame.mixer.Sound("speech.mp3")
        #sound.play()
        #os.remove("speech.mp3") 
        voice_id= "C8fuiDiroiSGQjaE8hpt"
        audio = client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id="eleven_flash_v2",
            output_format="mp3_44100_128",
            voice_settings=VoiceSettings(stability=0.7, style_exaggeration=0.0, speed=0.73)
        )

        
        play(audio)

