from gtts import gTTS
import os
import tkinter as tk
from tkinter import messagebox

# Function to convert text to speech
def convert_to_speech():
    text = entry_text.get("1.0", "end-1c")  # Get text from the Text widget
    language = combo_language.get()  # Get selected language from the dropdown
    
    if text == "":
        messagebox.showwarning("Input Error", "Please enter some text to convert.")
        return
    
    try:
        # Generate speech
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("output.mp3")
        os.system("start output.mp3")  # For Windows
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("400x300")

# Label for instructions
label_instruction = tk.Label(root, text="Enter text to convert to speech:")
label_instruction.pack(pady=10)

# Text widget for entering text
entry_text = tk.Text(root, height=5, width=30)
entry_text.pack(pady=10)

# Dropdown for language selection
languages = ['en', 'es', 'fr', 'de', 'it', 'ja', 'hi']  # You can add more languages
combo_language = tk.StringVar(root)
combo_language.set(languages[0])  # Default language
dropdown_language = tk.OptionMenu(root, combo_language, *languages)
dropdown_language.pack(pady=10)

# Button to trigger the conversion
button_convert = tk.Button(root, text="Convert to Speech", command=convert_to_speech)
button_convert.pack(pady=20)

# Start the Tkinter loop
root.mainloop()
