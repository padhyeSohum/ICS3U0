def create_movie_database():
    return {
        "The Lucas Movie": ("Action", 9.9),
        "The Sohum Movie": ("Action", 10.0),
        "The Aarnav Movie": ("Comedy", 6.8),
        "The Danny Movie": ("Adventure", 9.5),
        "The Clinton Movie": ("Comedy", 9.2)
    }

def add_movie(database, title, genre, rating):
    database[title] = (genre, rating)
    return database

def get_recommendations(database, genre, min_rating):
    recommended_movies = []
    for i in database.keys():
        if database[i][0].lower() == genre:
            if database[i][1] >= min_rating:
                recommended_movies.append(i)
    return recommended_movies

def run_menu(database):
    print("Welcome to the movie database. Here are your actions:")
    print("- Add movie: Type 1\n- Get recommendations: Type 2\n- Exit: Type 3, e, or q")
    action_list = ["1", "2", "3", "e", "E", "q", "Q"]
    action = input("Enter an action: ")
    while not (action in action_list):
        action = input("Please enter a valid action (1, 2, 3, e, q): ")
    
    while action in ["1", "2"]:
        if action == "1":
            title = input("Enter the movie's title: ")
            genre = input("Enter the movie's genre: ")
            rating = float(input("Enter the movie's rating: "))
            database = add_movie(database, title, genre, rating)
            print("Movie added!")
        elif action == "2":
            genre = input("Enter the genre of movies you would like to see recommendations for: ").lower()
            min_rating = float(input("Enter the minimum rating you would like to search: "))
            recommendations = get_recommendations(database, genre, min_rating)
            print("Your movie recommendations are: " + ", ".join(recommendations))
        action = input("Enter an action: ")
        while not (action in action_list):
            action = input("Please enter a valid action (1, 2, or 3): ")
    
    print("Goodbye!")
    return database

def main():
    movie_db = create_movie_database()
    database = run_menu(movie_db)
    print("Your updated database is: " + str(database))

main()