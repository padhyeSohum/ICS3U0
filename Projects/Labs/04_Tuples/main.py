your_favourites = ("movie01", "movie02", "movie03", "movie04", "movie05")
person1_favourites = ("movie04", "movie05", "movie06", "movie07", "movie08")
person2_favourites = ("movie05", "movie06", "movie09", "movie10", "movie11")
person3_favourites = ("movie08", "movie09", "movie12", "movie13", "movie14")

print(your_favourites[0])
print(your_favourites[-1])

print(person1_favourites[2])

print(person2_favourites[0:3])

if "movie09" in person3_favourites:
    print('"movie09" is in person 3\'s favourites!')

movie_info = ("WeeWooWeeWoo", "2025", "Sohum")
title, year, director = movie_info
print(f'The movie "{title}" directed by {director} was released in {year}.')

all_favourites = [your_favourites, person1_favourites, person2_favourites, person3_favourites]
print(all_favourites[2][1])

count = your_favourites.count("movie05") + person1_favourites.count("movie05") + person2_favourites.count("movie05") + person3_favourites.count("movie05")

print(f'"movie05" appears {count} time(s) in all tuples.')

print(f'"movie03 appears at index {your_favourites.index("movie03")}.')

print(f'"movie01" appears {your_favourites.count("movie01")} time(s) in your favourites.')