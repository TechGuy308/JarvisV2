#Main User Interface
import customtkinter as ctk
import core.orchestrator as orchestrator

class JarvisGUI():

    def __init__(self):
        super().__init__()
        self.orchestrator = orchestrator.Orchestrator()

        self.root = ctk.CTk()
        self.root.title("My First Tkinter App")
        self.root.geometry("400x300")  # Width x Height in pixels
        self.user_text_entry_box = ctk.CTkEntry(self.root, width=350,height=30)

        self.user_text_entry_box.pack(pady=10)

        self.user_text_entry_button = ctk.CTkButton(self.root, text="Send", command=lambda:self.user_input())
        self.user_text_entry_button.pack(pady=10)

    def user_input(self):
        text = self.user_text_entry_box.get()
        
        self.orchestrator.handle_text(text)

    def run(self):
        self.root.mainloop()






