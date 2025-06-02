#-----------------------------------------------------------------------------
# Name:        Movie Database
# Purpose:     To use functions to create a CLI tool that a user can use to store and get movies
#
# Author:      Sohum Padhye
# Created:     10-May-2925
# Updated:     11-May-2025
#-----------------------------------------------------------------------------

# initialize and create a default starting value for the movie database
def create_movie_database():
    '''
    Initializes the movie database.

    Initializes a database of a dictionary, with keys as movie names along with their
    values as a tuple containing the movie's genre and rating, then returns that database.

    Parameters
    ----------
    None

    Returns
    -------
    dictionary
        The initial database of the program.
    '''

    return {
        "The Lucas Movie": ("Action", 9.2),
        "The Sohum Movie": ("Action", 10.0),
        "The Aarnav Movie": ("Comedy", 9.3),
        "The Danny Movie": ("Adventure", 9.5),
        "The Clinton Movie": ("Comedy", 9.4)
    }

# add a movie to the database
def add_movie(database, title, genre, rating):
    '''
    Adds a movie to the database.

    Takes in the database and the movie details as input, then adds it 
    to the database after checking that a movie with that name does not 
    already exist.

    Parameters
    ----------
    database : dictionary
        The current, not-yet-updated database.
    title : string
        The title of the movie the user wishes to add to the database.
    genre : string
        The genre of the movie the user wishes to add to the database.
    rating : float
        The rating (out of 10) of the movie the user wishes to add to the database.

    Returns
    -------
    dictionary
        The new database after it has been updated, or the same database if a movie
        with the same name already exists.
    '''
    if not isinstance(database, dict):
        raise Exception("Function add_movie: Internal error.")
    if not isinstance(title, str):
        raise TypeError("Function add_movie: Expecting string value as input for 'title'.")
    if not isinstance(genre, str):
        raise TypeError("Function add_movie: Expecting string value as input for 'genre'.")
    if not isinstance(rating, (int, float)):
        raise TypeError("Function add_movie: Expecting integer or floatc value as input for 'rating'.")

    if rating < 0 or rating > 10:
        raise ValueError("Function add_movie: Input value of 'rating' outside of expected input range (0, 10).")
    

    # check if there is already a movie with this name in the database
    if database[title]:
        raise Exception(f"Function add_movie: Movie with name '{title} already exists in database.'")    
    
    # if not, then add it
    database[title] = (genre, rating)
    print("Movie added!")
    return database

# get recommendations of movies in the database for the user
def get_recommendations(database, genre, min_rating):
    '''
    Gives the user recommendations based on a genre that they like.

    Fetches all movies in the database that are the same genre as the genre
    the user is requesting, and of equal or higher rating than the inputted rating.

    Parameters
    ----------
    database : dictionary
        The current database.
    genre : string
        The genre of the movies that the user would like to get recommendations for.
    min_rating : float
        The minimum rating of the movies that the user would like to get recommendations for.
    
    Returns
    -------
    list of strings
        A list of the movie names that would comply with the user's inputted genre and
        the minimum rating.
    '''

    if not isinstance(database, dict):
        raise Exception("Function get_recommendations: Internal error.")
    if not isinstance(genre, str):
        raise TypeError("Function get_recommendations: Expecting string value as input for 'genre'.")
    if not isinstance(min_rating, (int, float)):
        raise TypeError("Function get_recommendations: Expecting integer or float value as input for 'min_rating'.")
    
    if min_rating < 0 or min_rating > 10:
        raise ValueError("Function add_movie: Input value of 'min_rating' outside of expected input range (0, 10).")

    recommended_movies = []

    # loop through the keys in the database
    for i in database.keys():

        # if the genere is correct and the movie's rating is 
        # greater than or equal to the target rating, then
        # add the movie to the list of recommended movies
        if database[i][0].lower() == genre:
            if database[i][1] >= min_rating:
                recommended_movies.append(i)
    return recommended_movies

# run the menu of the program
def run_menu(database):
    '''
    Runs the start menu.

    Runs the start menu which allows users to select an action of the program to perform.

    Parameters
    ----------
    database : dictionary
        The current database.
    
    Returns
    -------
    dictionary
        The updated database after all of the updates are made.
    '''

    if not isinstance(database, dict):
        raise Exception("Function run_menu: Internal error.")

    print("Welcome to the movie database. Here are your actions:")
    print("- Add movie: Type 1\n- Get recommendations: Type 2\n- Exit: Type 3, e, or q")

    # create a list of valid actions
    action_list = ["1", "2", "3", "e", "E", "q", "Q"]

    # ask for input from the user, then keep asking until they enter a valid action (if they haven't already)
    action = input("Enter an action: ")
    while not (action in action_list):
        action = input("Please enter a valid action (1, 2, 3, e, q): ")
    

    while action in ["1", "2"]:
        if action == "1": # add a movie
            # take inputs for parameters, then make the variable database equal to the new database
            title = input("Enter the movie's title: ")
            genre = input("Enter the movie's genre: ")
            rating = float(input("Enter the movie's rating: "))
            database = add_movie(database, title, genre, rating)
        elif action == "2": # get recommendations
            # take inputs from parameters, then make the variable recommendatinos equal to the recommendations
            genre = input("Enter the genre of movies you would like to see recommendations for: ").lower()
            min_rating = float(input("Enter the minimum rating you would like to search: "))
            recommendations = get_recommendations(database, genre, min_rating)
            print("Your movie recommendations are: " + ", ".join(recommendations))
        
        # ask for action input from user again
        action = input("Enter an action: ")
        while not (action in action_list):
            action = input("Please enter a valid action (1, 2, or 3): ")
    
    # user wants to leave, print goodbye
    print("Goodbye!")
    return database

def main():
    '''
    Starts the program.

    Runs the necessary functions to initialize the movie database, then run the start menu.

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    movie_db = create_movie_database()
    database = run_menu(movie_db)

    # print updated database when user is done
    print("Your updated database is: " + str(database))

# start program
try:
    main()
except Exception as e:
    print("Something went wrong:", e)