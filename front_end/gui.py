import tkinter as tk
import validation

# validate movie input
def validateMovieInput():
    movieInput = movie_entry.get().lower()
    closestMovie = validation.findClosestMovie(movieInput)

    if closestMovie:
        movie_title_label.config(text=f"Title: {closestMovie.capitalize()}")
        error_label.config(text="")
        rating_entry.focus_set()
    else:
        error_label.config(text="No movie found. Please spellcheck or enter another movie.")

# validate rating input
def validateRatingInput():
    ratingInput = rating_entry.get()
    validRating = validation.isValidRating(ratingInput)

    if validRating:
        rating_label.config(text=f"Minimum Rating: {validRating}")
        error_label.config(text="")
        rec_entry.focus_set()
    else:
        error_label.config(text="Invalid rating, try again (0-5).")

# validate number of recs input
def validateRecInput():
    recInput = rec_entry.get()
    validRec = validation.isValidNumber(recInput)

    if validRec:
        error_label.config(text="")
        show_movie_details()
    else:
        error_label.config(text="Invalid number, try again (1-20).")

# function to show the movie details page
def show_movie_details():
    home_frame.pack_forget()
    # display the movie details page
    movie_details_frame.pack(fill="both", expand=True)

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

# check movie input
movie_entry.bind("<Return>", lambda event: validateMovieInput())
movie_entry.bind("<Tab>", lambda event: validateMovieInput())

# rating entry label
rating_label = tk.Label(home_frame, text="Enter a minimum required rating (0-5):", font=("Arial", 12), bg="#fae9cf", fg="#986544")
rating_label.pack(pady=10)

# rating entry box
rating_entry = tk.Entry(home_frame, width=40, font=("Arial", 12), relief="sunken", bd=4)
rating_entry.pack(pady=10)

# check rating input
rating_entry.bind("<Return>", lambda event: validateRatingInput())
rating_entry.bind("<Tab>", lambda event: validateRatingInput())

# recommendations entry label
rec_label = tk.Label(home_frame, text="Enter the number of recommendations you would like (1-20):", font=("Arial", 12), bg="#fae9cf", fg="#986544")
rec_label.pack(pady=10)

# recommendations entry box
rec_entry = tk.Entry(home_frame, width=40, font=("Arial", 12), relief="sunken", bd=4)
rec_entry.pack(pady=10)

# check recs input
rec_entry.bind("<Return>", lambda event: validateRecInput())
rec_entry.bind("<Tab>", lambda event: validateRecInput())

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

# display title
movie_title_label = tk.Label(
    movie_details_frame, text="Title: [Sample Title]", font=("Arial", 12), bg="#fae9cf", fg="#986544"
)
movie_title_label.pack(pady=10)

# display rating
rating_label = tk.Label(
    movie_details_frame, text="Title: [Sample Title]", font=("Arial", 12), bg="#fae9cf", fg="#986544"
)
rating_label.pack(pady=10)

similar_label = tk.Label(
    movie_details_frame,
    text="Similar Movies",
    font=("Helvetica", 20, "bold"),  # Sans-serif font
    bg="#fae9cf",
    fg="#986544",
)
similar_label.pack(pady=20)

# restart the process without xing out
def back_button():
    # clear everything
    movie_entry.delete(0, tk.END)
    rating_entry.delete(0, tk.END)
    rec_entry.delete(0, tk.END)
    error_label.config(text="")
    movie_title_label.config(text="Title: [Sample Title]")
    rating_label.config(text="Minimum Rating: [Sample Rating]")

    # hide the movie details frame and show the home frame
    movie_details_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)

# back button implementation in the movie details frame
back_button = tk.Button(
    movie_details_frame,
    text="Back",
    font=("Helvetica", 12, "bold"),
    bg="#986544",
    fg="white",
    relief="raised",
    command=back_button,
)
back_button.pack(pady=20)


m.mainloop()
