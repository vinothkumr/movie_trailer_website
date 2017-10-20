"""This module contain functions which creates
entries for Fresh Tomatoes Movie Trailer page"""
import media
import fresh_tomatoes


# ====================List of movies to be added in list==================
THUPPAKKI = media.Movie(
    "Thuppakki",
    "An army captain is on a mission to track down and destroy a "
    "terrorist gang and deactivate the sleeper cells under its command",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMGFjZTdmMmEtOGZmYi00NmU5LTk4MjEtYTdmN2QzMjRmMWZkXkEyXkFqcGdeQXVyNjUwNDEzNTE@._V1_QL50_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=2S0Fk2Dh9Mk")

THANI_ORUVAN = media.Movie(
    "Thani oruvan",
    "Story of an Officer Mithran who wants to arrest "
    "Siddharth Abhimanyu, an affluent scientist who uses secret "
    "illegal medical practices for profit",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzgxMDc2Mjg3M15BMl5BanBnXkFtZTgwMzU4NTkxNzE@._V1_QL50_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=r5Lih8rKd6k")

VIKRAM_VEDHA = media.Movie(
    "Vikram Vedha",
    "A ruthless cop wages a war against an unscrupulous gangster. "
    "However, certain events lead to the cop questioning his principles "
    "and motives. This leaves behind a battle between good and bad with "
    "what is good and what is bad being unclear",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI3Y2M3OTgtZmExNS00ZTEyLTg5NGItOWZiYjVlZWY5N2E1XkEyXkFqcGdeQXVyMzI4MzEwNQ@@._V1_QL50_SY1000_CR0,0,749,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1sVr-uWZPjE")

# Original name altered, as first letter of variable cannot be a digit
THREE_IDIOTS = media.Movie(
    "3 Idiots",
    "Two friends are searching for their long lost companion. They "
    "revisit their college days and recall the memories of their friend "
    "who inspired them to think differently, even as the rest of the "
    "world called them \"idiots\"",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZWRlNDdkNzItMzhlZC00YTdmLWIwNjktYjY5NjQ1ZmQ3N2FkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_QL50_SY1000_CR0,0,747,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=K0eDlFX9GMc")

LIMITLESS = media.Movie(
    "Limitless",
    "With the help of a mysterious pill that enables the user to access "
    "100 percent of his brain abilities, a struggling writer becomes a "
    "financial wizard, but it also puts him in a new world with "
    "lots of dangers",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BYmViZGM0MGItZTdiYi00ZDU4LWIxNDYtNTc1NWQ5Njc2N2YwXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_QL50_SY1000_CR0,0,692,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=jOLqNOfzus4")
# =======================End of movies list========================


# Create a list of movies that has to be
# included in the Fresh Tomatoes Movie trailer page
MOVIES = [VIKRAM_VEDHA, THUPPAKKI, THANI_ORUVAN, THREE_IDIOTS, LIMITLESS]

fresh_tomatoes.open_movies_page(MOVIES)
