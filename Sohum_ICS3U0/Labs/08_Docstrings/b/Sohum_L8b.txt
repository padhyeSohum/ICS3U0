#-----------------------------------------------------------------------------
# Name:        Movie Database
# Purpose:     To use functions to create a CLI tool that a user can use to store and get movies
#
# Author:      Sohum Padhye
# Created:     28-Apr-2025
# Updated:     30-Apr-2025
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

    # check if there is already a movie with this name in the database
    if database[title]:
        print("There is a movie with this name already in the database!")
    
    # if not, then add it
    else:
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
main()