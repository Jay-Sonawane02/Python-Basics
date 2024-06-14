#WAP to ask for 3 fav movies to user and store them in a list

movies=[]
for i in range(3):
    movie = input("Enter movie name: ")
    movies.append(movie)

print(movies)
print(movies.index('A'))


