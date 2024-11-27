import tkinter as tk

# Initialize the main window
m = tk.Tk()
m.title("CineRoll")  # Set the window title
m.geometry("800x600")  # Set the window si

cinnamon_color = "#D2691E"  # Hex code for cinnamon color
m.configure(bg=cinnamon_color)

title_label = tk.Label(m, text="Welcome to CineRoll", font=("Arial", 16, "bold"), bg=cinnamon_color, fg="white")
title_label.pack(pady=40) 

entry_label = tk.Label(m, text="Enter a movie name:", font=("Arial", 12))
entry_label.pack(pady=20)

movie_entry = tk.Entry(m, width=30, font=("Arial", 12))
movie_entry.pack(pady=20)

m.mainloop()
