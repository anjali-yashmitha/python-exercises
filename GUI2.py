import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Function to play music
def play_music():
    song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if song_path:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(-1)  # -1 loops the song indefinitely

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Main Tkinter window
root = tk.Tk()
root.title("Penguin")
root.geometry("300x300")

canvas = tk.Canvas(root, width=250, height=250, bg="red")
canvas.pack()

# Penguin Body
canvas.create_oval(70, 60, 180, 200, outline="black", fill="black")

# White belly
canvas.create_oval(90, 90, 160, 170, outline="white", fill="white")

# Head
canvas.create_oval(90, 30, 160, 90, outline="black", fill="black")

# Beak
canvas.create_polygon(125, 60, 150, 70, 125, 80, outline="orange", fill="orange")

# Eyes
canvas.create_oval(100, 50, 110, 60, outline="white", fill="white")
canvas.create_oval(140, 50, 150, 60, outline="white", fill="white")

# Wings
canvas.create_arc(60, 100, 110, 160, start=180, extent=180, outline="black", fill="black")
canvas.create_arc(140, 100, 190, 160, start=0, extent=180, outline="black", fill="black")

# Feet
canvas.create_oval(90, 180, 110, 200, outline="orange", fill="orange")
canvas.create_oval(140, 180, 160, 200, outline="orange", fill="orange")

# Buttons to play and stop music
btn_play = tk.Button(root, text="Play Music", command=play_music)
btn_play.pack(side=tk.LEFT, padx=20, pady=10)

btn_stop = tk.Button(root, text="Stop Music", command=stop_music)
btn_stop.pack(side=tk.RIGHT, padx=20, pady=10)

# Run the application
root.mainloop()
