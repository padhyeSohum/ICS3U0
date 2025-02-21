your_favourites = {"movie01", "movie02", "movie03", "movie04", "movie05", "movie06", "movie07"}
person1_favourites = {"movie06", "movie07", "movie08", "movie09", "movie010"}
person2_favourites = {"movie07", "movie09", "movie11", "movie12", "movie13"}
person3_favourites = {"movie02", "movie06", "movie07", "movie14", "movie15"}

common_favourites = your_favourites.intersection(person1_favourites).intersection(person2_favourites)

all_movies = your_favourites.union(person1_favourites, person2_favourites, person3_favourites)

person3_unique_favs = person3_favourites.difference(your_favourites).difference(person1_favourites).difference(person2_favourites)

your_and_person1s_uniques = your_favourites.symmetric_difference(person1_favourites)

# task 3