import AthenaBackend as ab
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import os
import sys

# Create the main window
window = tk.Tk()
window.title("Assistant Interface")

# Set the background color and dimensions of the window
window.configure(bg="white")
window.geometry("700x500")

# Increase the window geometry
new_width = 2000
new_height = 2000
window.geometry(f"{new_width}x{new_height}")

# Add the Assistant name
assistant_name = tk.Label(window, text="ATHENA", font=("Arial Black", 40, "bold"), fg="#002244", bg="white")
assistant_name.place(x=790, y=60)

# Add the tagline
tagline = tk.Label(window, text="THE VIRTUAL ASSISTANT", font=("Times New Roman ", 15), fg="#002244", bg="white")
tagline.place(x=800, y=150)

# Add the GIF image
# Load the image
image_path = r"C:\Users\mariy\Downloads\athena pic.jpg"
gif_image = Image.open(image_path)

# Resize the image
desired_width = 600
desired_height = 400
gif_image = gif_image.resize((desired_width, desired_height), Image.LANCZOS)

# Convert the image to PhotoImage
gif_photo = ImageTk.PhotoImage(gif_image)

# Create a label to display the GIF image
gif_label = tk.Label(window, bg="white", image=gif_photo)
gif_label.place(x=50, y=150)

# Function to update the GIF frames
def update_gif(frame_idx=0):
    gif_label.config(image=gif_frames[frame_idx])
    frame_idx = (frame_idx + 1) % len(gif_frames)
    window.after(100, update_gif, frame_idx)

# Create a circular button with "Start" label
def on_button_click_start():
    ab.wish() # Backend logic for starting the assistant

button_start = tk.Button(window, text="Start", font=("Arial", 20), fg="white", bg="#002244", bd=1, width=4, height=1, command=on_button_click_start)
button_start.place(x=380, y=770)

# Create a circular button with microphone symbol
def on_button_click_mic():
    query = ab.takecommand()  # Call the backend function for voice command recognition
    
    # Logic building for tasks
    if "open notepad" in query:
        ab.open_notepad()
    elif "screenshot" in query:
        ab.get_screenshot()
    elif "set alarm" in query:
        ab.alarm(query)
    elif "volume up" in query:
        ab.volumeup()
    elif "volume down" in query:
        ab.volumedown()
    elif 'pause' in query:
        ab.pause()
    elif 'shutdown system' in query:
        ab.shutdown()
    elif 'go to sleep'in query:
        ab.sleeping()
    elif 'click my photo' in query:
        ab.capture()
    elif 'play' in query:
        ab.play()
    elif "open vs code" in query:
        ab.open_vscode()
    elif "pictures" in query or "photos" in query:
        ab.open_pictures()
    elif "open camera" in query:
        ab.open_camera()
    elif "calculate" in query:
        ab.Calc(query)
    elif "wikipedia" in query:
        ab.search_wikipedia(query)
    elif "weather" in query:
        ab.get_weather(query)
    elif "open" in query and "youtube" in query:
        ab.search_youtube(query)
    elif "open" in query and "facebook" in query:
        ab.open_facebook()
    elif "open" in query and "stack overflow" in query:
        ab.open_stackoverflow()
    elif "open" in query and "google" in query:
        ab.search_google(query)
    elif "who are you" in query:
        ab.get_assistant_info()
    elif "do" in query and "you"in query and "love" in query:
        ab.express_love()
    elif "play" in query and "songs" in query and  "youtube" in query:
        ab.play_song()
    elif "search" in query:
        ab.perform_search(query)
    elif "who made you" in query:
        ab.get_creator_info()
    elif "night" in query or "evening" in query or "morning" in query or "afternoon"in query :
        ab.get_wish()
    elif "no thanks" in query or "thank you" in query or "goodbye" in query:
        ab.exit_assistant()
    else:
        ab.default_response()

button_mic = tk.Button(window, text="🎙", font=("Arial", 20), fg="white", bg="#002244", bd=1, width=4, height=1, command=on_button_click_mic)
button_mic.place(x=550, y=770)

# Create a Frame to embed the VS Code terminal
vscode_frame = tk.Frame(window, bg="black",)
vscode_frame.place(x=1150, y=320, width=700, height=350)

# Function to redirect the standard output to the Text widget
class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

# Redirect the standard output to the Text widget
output_text = tk.Text(vscode_frame,bd=5, bg="white")
output_text.pack()
sys.stdout = StdoutRedirector(output_text)


# Load the GIF frames
gif_frames = []
try:
    while True:
        gif_frames.append(ImageTk.PhotoImage(gif_image))
        gif_image.seek(len(gif_frames))  # Seek to the next frame
except EOFError:
    pass

# Start updating the GIF frames
update_gif()

# Start the main event loop
window.mainloop()