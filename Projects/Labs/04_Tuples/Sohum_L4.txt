#-----------------------------------------------------------------------------
# Name:        Tuple Operations
# Purpose:     To explore various tuple operations and properties
#
# Author:      Sohum Padhye
# Created:     6-Mar-2025
# Updated:     6-Mar-2025
#-----------------------------------------------------------------------------

# initialize tuples
your_favourites = ("movie01", "movie02", "movie03", "movie04", "movie05")
person1_favourites = ("movie04", "movie05", "movie06", "movie07", "movie08")
person2_favourites = ("movie05", "movie06", "movie09", "movie10", "movie11")
person3_favourites = ("movie08", "movie09", "movie12", "movie13", "movie14")

# print my first and last favourite movies
print(your_favourites[0])
print(your_favourites[-1])

# print the middle movie from person 1's favourites tuple
print(person1_favourites[2])

# print the first three movies from person2's favourites tuple using slicing
print(person2_favourites[0:3])

# check if a specific movie is in person3's favourites tuples using the in operator
if "movie09" in person3_favourites:
    print('"movie09" is in person 3\'s favourites!')

# initialize a tuple called movie_info with name, year, and director
movie_info = ("WeeWooWeeWoo", "2025", "Sohum")

# unpack the tuple into three different variables
title, year, director = movie_info

# print a formatted string using these variables
print(f'The movie "{title}" directed by {director} was released in {year}.')

# create a list containing the tuples of all movies, then output the second movie from the third tuple in the list
all_favourites = [your_favourites, person1_favourites, person2_favourites, person3_favourites]
print(all_favourites[2][1])

# count how many times a specific movie appears across all tuples in the list
count = your_favourites.count("movie05") + person1_favourites.count("movie05") + person2_favourites.count("movie05") + person3_favourites.count("movie05")
print(f'"movie05" appears {count} time(s) in all tuples.')

# find the index of a specific movie in your favourites tuple
print(f'"movie03 appears at index {your_favourites.index("movie03")}.')

# count how many times a movie appears in person1's favourites tuple
print(f'"movie01" appears {person1_favourites.count("movie01")} time(s) in person1\'s favourites.')