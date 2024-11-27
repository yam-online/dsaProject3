import tkinter as tk

# Function to show the movie details page
def show_movie_details():
    home_frame.pack_forget()

    # display details
    movie_details_frame.pack(fill="both", expand=True)

# create the main window
m = tk.Tk()
m.title("CineRoll")
m.geometry("800x600")  # default screen size
m.configure(bg="#D2691E")

# create the home frame
home_frame = tk.Frame(m, bg="#D2691E")
home_frame.pack(fill="both", expand=True)

title_label = tk.Label(home_frame, text="Welcome to CineRoll", font=("Arial", 16, "bold"), bg="#D2691E", fg="white")
title_label.pack(pady=20)

entry_label = tk.Label(home_frame, text="Enter a movie name:", font=("Arial", 12), bg="#D2691E", fg="white")
entry_label.pack(pady=10)

movie_entry = tk.Entry(home_frame, width=40, font=("Arial", 12))
movie_entry.pack(pady=10)

movie_entry.bind("<Return>", lambda event: show_movie_details())

# create the movie details frame
movie_details_frame = tk.Frame(m, bg="#D2691E")

# details title
details_title_label = tk.Label(
    movie_details_frame, text="Movie Details", font=("Arial", 16, "bold"), bg="#D2691E", fg="white"
)
details_title_label.pack(pady=20)

# movie title
movie_title_label = tk.Label(
    movie_details_frame, text="Title: [Sample Title]", font=("Arial", 12), bg="#D2691E", fg="white"
)
movie_title_label.pack(pady=10)

# rating
movie_rating_label = tk.Label(
    movie_details_frame, text="Rating: [Sample Rating]", font=("Arial", 12), bg="#D2691E", fg="white"
)
movie_rating_label.pack(pady=10)

# genre
movie_genre_label = tk.Label(
    movie_details_frame, text="Genre: [Sample Genre]", font=("Arial", 12), bg="#D2691E", fg="white"
)
movie_genre_label.pack(pady=10)

m.mainloop()
