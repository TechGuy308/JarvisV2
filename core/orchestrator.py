#Handle Workflow
from core.brain import *
from core.conversation_history import *
from core.memory import *
import voice.listen as listen, voice.speak as speak
import asyncio
import threading
import random


class Orchestrator():
    def __init__(self):
        #Classes for each module
        self.brain = Brain()
        self.memory = Memory()
        self.conversation = Conversation()
        self.voice = speak.Voice()
        
    # Future changes:
    def handle_text(self, user_input):
        self.conversation.add_user(user_input)
        history = self.conversation.get_messages()
        
        tool = self.brain.tool_caller(history)
        
        
        self.conversation.add_tool(str(tool))
        history = self.conversation.get_messages()

        reply = self.brain.jarvis_reply(history)
        self.conversation.add_ai(reply)

        print(f"hist: {history}")
        self.voice.speak(reply)
        
        
    




