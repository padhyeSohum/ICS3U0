#-----------------------------------------------------------------------------
# Name:        Dictionary Operations
# Purpose:     To explore the various properties and operations with dictionaries in Python
#
# Author:      Sohum Padhye
# Created:     28-Mar-2025
# Updated:     28-Mar-2025
#-----------------------------------------------------------------------------

# Task 1: Creating Dictionaries
your_favourites = {
    "movie01": "genre01", 
    "movie02": "genre02", 
    "movie03": "genre03", 
    "movie04": "genre04", 
    "movie05": "genre05"
}
person1_favourites = {
    "movie03": "2000", 
    "movie04": "2001", 
    "movie05": "2003", 
    "movie06": "2008", 
    "movie07": "2019"
}
person2_favourites = {
    "movie03": "person01", 
    "movie05": "person02", 
    "movie07": "person02", 
    "movie08": "person03", 
    "movie09": "person04"
}
person3_favourites = {
    "movie03": "7.5", 
    "movie04": "8.8", 
    "movie08": "9.1", 
    "movie10": "8.7", 
    "movie11": "9.8"
}

# Task 2: Accessing Dictionary Elements
# Use dictionary key access to print required information
print(your_favourites["movie01"], your_favourites["movie05"])
print(person1_favourites["movie05"])
print(person2_favourites["movie03"], person2_favourites["movie05"], person2_favourites["movie07"])

# Use the 'in' operator to check for a movie's presence
test_movie = "movie08"
if test_movie in person3_favourites:
    print(f"{test_movie} is in person3's favourites")
else:
    print(f"{test_movie} not in person3's favourites")

# Task 3: Dictionaries in Lists
all_favourites = [your_favourites, person1_favourites, person2_favourites, person3_favourites]

# Access the third dictionary in the list, then get its second item
print(all_favourites[2]["movie05"])

# Use a loop to count occurrences of specific movies across all dictionaries
test_movie = "movie04"
test_number_of_occurences = 0
for i in all_favourites:
    if test_movie in i:
        count += 1

# Task 4: Dictionary Methods
# Use the keys() method to get all movies from your_favorites
your_fav_movies = your_favourites.keys()

# Use the values() method to get all ratings from person3_favorites
person3_fav_movie_values = person3_favourites.values()

# Use the items() method to get and print all movie-director pairs from person2_favorites
print(person2_favourites.items())