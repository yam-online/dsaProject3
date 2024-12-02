import tkinter as tk
import validation

# validate movie input


# function to show the movie details page
def show_movie_details():
    userInput = movie_entry.get().lower()
    closestMovie = validation.findClosestMovie(userInput)

    if closestMovie:
        movie_title_label.config(text=f"Title: {closestMovie.capitalize()}")
        home_frame.pack_forget()
        # display the movie details page
        movie_details_frame.pack(fill="both", expand=True)
    else:
        error_label.config(text="No movie found. Please try again or enter another movie.", fg="red")

# create the main window
m = tk.Tk()
m.title("CineRoll")
m.geometry("800x600")  # default screen size
m.configure(bg="#fae9cf")

# create the home frame
home_frame = tk.Frame(m, bg="#fae9cf")
home_frame.pack(fill="both", expand=True)

# title
title_label = tk.Label(
    home_frame,
    text="Welcome to CineRoll",
    font=("Helvetica", 20, "bold"),  # Sans-serif font
    bg="#fae9cf",
    fg="#986544",
)
title_label.pack(pady=20)

# movie entry label
entry_label = tk.Label(home_frame, text="Enter a movie name:", font=("Arial", 12), bg="#fae9cf", fg="#986544")
entry_label.pack(pady=10)

# movie entry box
movie_entry = tk.Entry(home_frame, width=40, font=("Arial", 12), relief="sunken", bd=4)
movie_entry.pack(pady=10)

movie_entry.bind("<Return>", lambda event: show_movie_details())

# rating entry label
rating_label = tk.Label(home_frame, text="Enter a minimum required rating (0-5)", font=("Arial", 12), bg="#fae9cf", fg="#986544")
rating_label.pack(pady=10)

# rating entry box
rating_entry = tk.Entry(home_frame, width=40, font=("Arial", 12), relief="sunken", bd=4)
rating_entry.pack(pady=10)

rating_entry.bind("<Return>", lambda event: show_movie_details())

# error label
error_label = tk.Label(home_frame, text="", font=("Arial", 12), bg="#fae9cf", fg="red")
error_label.pack(pady=5)

# create the movie details frame
movie_details_frame = tk.Frame(m, bg="#fae9cf")

# movie Details Page: Title
details_title_label = tk.Label(
    movie_details_frame,
    text="Movie Details",
    font=("Helvetica", 20, "bold"),  # Sans-serif font
    bg="#fae9cf",
    fg="#986544",
)
details_title_label.pack(pady=20)

# title
movie_title_label = tk.Label(
    movie_details_frame, text="Title: [Sample Title]", font=("Arial", 12), bg="#fae9cf", fg="#986544"
)
movie_title_label.pack(pady=10)

m.mainloop()
