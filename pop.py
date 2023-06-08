import random
import tkinter as tk
import pygame
import tkinter.filedialog as tkfiledialog

# Configuration
window_width = 400
window_height = 400
bubble_size = 50

def pop_bubble(event):
    canvas = event.widget
    x = (event.x - start_x) // bubble_size
    y = (event.y - start_y) // bubble_size

    # Check if the coordinates are within the valid range
    if x < 0 or x >= cols or y < 0 or y >= rows:
        return

    bubble_state = canvas.itemcget(bubbles[x][y], "state")

    # Check if the bubble is already hidden
    if bubble_state == "hidden":
        return

    canvas.itemconfigure(bubbles[x][y], state='hidden')
    pygame.mixer.Sound.play(custom_sound)

def update_bubbles(event=None):
    global bubbles, cols, rows, bubble_size, start_x, start_y

    # Clear canvas
    canvas.delete("all")

    # Get slider values
    cols = cols_slider.get()
    rows = rows_slider.get()

    # Calculate starting position of the bubble field
    start_x = (window_width - cols * bubble_size) // 2
    start_y = (window_height - rows * bubble_size) // 2

    # Create the bubbles
    bubbles = []
    for i in range(cols):
        column = []
        for j in range(rows):
            x1 = start_x + i * bubble_size
            y1 = start_y + j * bubble_size
            x2 = x1 + bubble_size
            y2 = y1 + bubble_size

            bubble = canvas.create_oval(x1, y1, x2, y2, outline="#FFFFF0", fill="#FFFFFF")
            column.append(bubble)
        bubbles.append(column)

def select_custom_sound():
    file_path = tkfiledialog.askopenfilename(filetypes=[("Sound Files", "*.wav")])
    if file_path:
        global custom_sound
        custom_sound = pygame.mixer.Sound(file_path)

# Initialize pygame mixer
pygame.mixer.init()
custom_sound = pygame.mixer.Sound("pop.wav")  # Default sound

# Create the main window
window = tk.Tk()
window.title("Bubble Wrap Simulator")

# Create the canvas
canvas = tk.Canvas(window, width=window_width, height=window_height)
canvas.pack()

# Create sliders for number of bubbles
cols_slider = tk.Scale(window, from_=1, to=10, orient=tk.HORIZONTAL, label="Number of Bubbles Wide", command=update_bubbles)
cols_slider.set(4)  # Initial value
cols_slider.pack()

rows_slider = tk.Scale(window, from_=1, to=10, orient=tk.HORIZONTAL, label="Number of Bubbles High", command=update_bubbles)
rows_slider.set(4)  # Initial value
rows_slider.pack()

# Create the bubbles
bubbles = []
cols = cols_slider.get()
rows = rows_slider.get()

for i in range(cols):
    column = []
    for j in range(rows):
        x1 = i * bubble_size
        y1 = j * bubble_size
        x2 = x1 + bubble_size
        y2 = y1 + bubble_size

        bubble = canvas.create_oval(x1, y1, x2, y2, outline="black", fill="#FFFFFF")
        column.append(bubble)
    bubbles.append(column)

# Create custom sound button
custom_sound_button = tk.Button(window, text="Select Custom Sound", command=select_custom_sound)
custom_sound_button.pack()

# Bind the pop_bubble function to left mouse click events
canvas.bind("<Button-1>", pop_bubble)

# Start the main loop
window.mainloop()
