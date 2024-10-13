import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

def list_microphones():
    mic_list = sr.Microphone.list_microphone_names()
    print("Available Microphones:", mic_list)
    return mic_list

def speech_to_text():
    try:
        mic = sr.Microphone(device_index=0)
        with mic as source:
            print("Adjusting for ambient noise... Please wait.")
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print("Listening...")
            audio = r.listen(source)  # Listen to the source
            print("Recognizing...")
            text = r.recognize_google(audio)  # Recognize speech using Google Web Speech API
            result_label.config(text="You said: " + text)
    except sr.UnknownValueError:
        result_label.config(text="Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        result_label.config(text="Could not request results from Google Speech Recognition service; {0}".format(e))

def on_button_click():
    speech_to_text()

# GUI setup
root = tk.Tk()
root.title("Speech to Text")

# List microphones on startup
mic_list = list_microphones()

# GUI components
record_button = tk.Button(root, text="Record", command=on_button_click)
record_button.pack(pady=20)

result_label = tk.Label(root, text="Press 'Record' and start speaking...")
result_label.pack(pady=20)

root.mainloop()
