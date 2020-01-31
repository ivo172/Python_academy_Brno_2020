film = dict()
film["name"] = "Shawshank Redemption"
film["rating"] = 87
film["year"] = 1994
film["director"] = "Frank Darabont"

film.update(starring=["Timm Robbins", "Morgan Freeman"])
film.update(budget=200)
print(film)

film.pop("budget")
print(film)

films = dict()
films.update(DRAMA=film)
print(films)

print(f"We can currently offer: {(list(films))}")
genre = input("What genre are you interested?: ")

if genre == "DRAMA":
    print(f"The genre {genre} represent film {films[genre]}.")

films.clear()
print("Database has been erased: ")
print(films)