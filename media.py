"""Module to hold media classes for Fresh tomatoes page"""
import webbrowser


class Movie(object):
    """Class used to initialize and define a movie object"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
            """Inits Movie object with
            Args:
                movie_title: Name of movie
                movie_storyline: Short storyline of movie
                poster_image: url of movie poster
                trailer_youtube: Youtube url of movie's trailer
            """
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This function opens the YouTube trailer in a browser.
        Args:
            None
        """
        webbrowser.open(self.trailer_youtube_url)
