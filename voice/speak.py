#Manage speaking

import pyttsx3
import asyncio
import edge_tts
from playsound import playsound
import os
import pygame
import random

#Future Changes: Stream audio

pygame.mixer.init()
class Voice():
    def __init__(self):
        pass
        #self.wait_message = ["One moment sir.", "Please wait as I process your request", "Currently Processing", "Just a moment", "Give me a second sir.", "Right away sir.", "I will be done shortly."]
    #def wait(self):
        #asyncio.run(self.speak(random.choice(self.wait_message)))
    
    def run(self, reply):
        
        asyncio.run(self.speak(reply))
        

    async def speak(self, text):
        # en-GB-ThomasNeural or en-GB-RyanNeural
        tts = edge_tts.Communicate(text=text, voice="en-GB-ThomasNeural", rate="+3%", pitch="-7Hz")
        
        await tts.save("speech.mp3")
        sound = pygame.mixer.Sound("speech.mp3")
        sound.play()
        os.remove("speech.mp3") 

