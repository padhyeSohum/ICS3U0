your_favourites = {"movie01", "movie02", "movie03", "movie04", "movie05", "movie06", "movie07"}
person1_favourites = {"movie06", "movie07", "movie08", "movie09", "movie10", "movie11", "movie13"}
person2_favourites = {"movie07", "movie09", "movie11", "movie12", "movie13", "movie14", "movie15"}
person3_favourites = {"movie02", "movie06", "movie07", "movie14", "movie15", "movie16", "movie17"}

common_favourites = your_favourites.intersection(person1_favourites, person2_favourites)

all_favourites = your_favourites.union(person1_favourites, person2_favourites, person3_favourites)

person3_unique_favs = person3_favourites.difference(your_favourites, person1_favourites, person2_favourites)

your_and_person1s_uniques = your_favourites.symmetric_difference(person1_favourites)

# task 3
your_favourites.add("movie18")
your_favourites.add("movie19")

person2_favourites.discard("movie11")

print(person3_favourites.issubset(all_favourites))
print(len(all_favourites))

your_favourites.difference_update(person1_favourites)
person2_favourites.intersection_update(person3_favourites)
print(your_favourites.isdisjoint(person3_favourites))

universal_favourites = your_favourites.intersection(person1_favourites, person2_favourites, person3_favourites)
print(universal_favourites)

list_all_favs = [your_favourites, person1_favourites, person2_favourites, person3_favourites]

your_common_count = your_favourites.difference(your_favourites.difference(person1_favourites, person2_favourites, person3_favourites))
person1_common_count = person1_favourites.difference(person1_favourites.difference(your_favourites, person2_favourites, person3_favourites))
person2_common_count = person2_favourites.difference(person2_favourites.difference(your_favourites, person1_favourites, person3_favourites))
person3_common_count = person3_favourites.difference(person3_favourites.difference(your_favourites, person1_favourites, person2_favourites))

at_least_two = your_common_count.union(person1_common_count, person2_common_count, person3_common_count)
print(len(at_least_two))

your_uniques = your_favourites.difference(person1_favourites, person2_favourites, person3_favourites)
person1_uniques = person1_favourites.difference(your_favourites, person2_favourites, person3_favourites)
person2_uniques = person2_favourites.difference(your_favourites, person1_favourites, person3_favourites)
person3_uniques = person3_favourites.difference(your_favourites, person1_favourites, person2_favourites)

if len(your_uniques) > 0: print("You are the only person who likes: " + str(your_uniques))
if len(person1_uniques) > 0: print("Person 1 is the only person who likes: " + str(person1_uniques))
if len(person2_uniques) > 0: print("Person 2 is the only person who likes: " + str(person2_uniques))
if len(person3_uniques) > 0: print("Person 3 the only person who likes: " + str(person3_uniques))

all_uniques = your_uniques.union(person1_uniques, person2_uniques, person3_uniques)
print("All of the favourite movies that only one person likes are: " + str(all_uniques))