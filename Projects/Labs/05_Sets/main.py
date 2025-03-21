#-----------------------------------------------------------------------------
# Name:        Set Operations
# Purpose:     To explore various set operations and properties
#
# Author:      Sohum Padhye
# Created:     6-Mar-2025
# Updated:     6-Mar-2025
#-----------------------------------------------------------------------------

# initialize all sets to be used
your_favourites = {"movie01", "movie02", "movie03", "movie04", "movie05", "movie06", "movie07"}
person1_favourites = {"movie06", "movie07", "movie08", "movie09", "movie10", "movie11", "movie13"}
person2_favourites = {"movie07", "movie09", "movie11", "movie12", "movie13", "movie14", "movie15"}
person3_favourites = {"movie02", "movie06", "movie07", "movie14", "movie15", "movie16", "movie17"}

# find favourites between you, person1, and person2
common_favourites = your_favourites.intersection(person1_favourites, person2_favourites)

# combine all unique movies from all four sets
all_favourites = your_favourites.union(person1_favourites, person2_favourites, person3_favourites)

# identify movies that person3 likes but nobody else does
person3_unique_favs = person3_favourites.difference(your_favourites, person1_favourites, person2_favourites)

# find movies that are in your list or person1's list, but not both
your_and_person1s_uniques = your_favourites.symmetric_difference(person1_favourites)

# add two new movies to your favourites set
your_favourites.add("movie18")
your_favourites.add("movie19")

# remove a movie from person2's favourites set
person2_favourites.discard("movie11")

# check if person3's favorites is a subset of the combined favorites
print(person3_favourites.issubset(all_favourites))

# find the total number of unique movies across all sets
print(len(all_favourites))

# remove movies from your_favorites that exist in both your set and person1_favorites
your_favourites.difference_update(person1_favourites)

# update person2_favorites to only include movies that are also in person3_favorites 
person2_favourites.intersection_update(person3_favourites)

# check if your_favorites and person3_favorites have no movies in common
print(your_favourites.isdisjoint(person3_favourites))

# find which movie are liked by all four people
universal_favourites = your_favourites.intersection(person1_favourites, person2_favourites, person3_favourites)
print(universal_favourites)

# find how many movies are liked by at least two people
list_all_favs = [your_favourites, person1_favourites, person2_favourites, person3_favourites]

your_common_count = your_favourites.difference(your_favourites.difference(person1_favourites, person2_favourites, person3_favourites))
person1_common_count = person1_favourites.difference(person1_favourites.difference(your_favourites, person2_favourites, person3_favourites))
person2_common_count = person2_favourites.difference(person2_favourites.difference(your_favourites, person1_favourites, person3_favourites))
person3_common_count = person3_favourites.difference(person3_favourites.difference(your_favourites, person1_favourites, person2_favourites))

at_least_two = your_common_count.union(person1_common_count, person2_common_count, person3_common_count)
print(len(at_least_two))

# find movies that only one person likes
your_uniques = your_favourites.difference(person1_favourites, person2_favourites, person3_favourites)
person1_uniques = person1_favourites.difference(your_favourites, person2_favourites, person3_favourites)
person2_uniques = person2_favourites.difference(your_favourites, person1_favourites, person3_favourites)
person3_uniques = person3_favourites.difference(your_favourites, person1_favourites, person2_favourites)

if len(your_uniques) > 0: print("You are the only person who likes: " + str(your_uniques))
if len(person1_uniques) > 0: print("Person 1 is the only person who likes: " + str(person1_uniques))
if len(person2_uniques) > 0: print("Person 2 is the only person who likes: " + str(person2_uniques))
if len(person3_uniques) > 0: print("Person 3 the only person who likes: " + str(person3_uniques))

# set of all movies that are unique to each person's favourites
all_uniques = your_uniques.union(person1_uniques, person2_uniques, person3_uniques)
print("All of the favourite movies that only one person likes are: " + str(all_uniques))