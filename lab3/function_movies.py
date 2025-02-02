movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def movie_rate_func(movie):
    if movie['imdb'] > 5.5:
        return True
    else:
        return False

for movie in movies:
    if movie_rate_func(movie):
        print("True")
    else:
        print("False")

# function to create a list of movies with imdb > 5.5
def movies_list(movies):
    movie_list = []
    for movie in movies:
        if movie_rate_func(movie):
            movie_list.append({'name': movie['name'], 'imdb': movie['imdb'], 'category': movie['category']})
    for movie in movie_list:
        print(movie)  
movies_list(movies)


categories = set(movie['category'] for movie in movies)
cats_list = list(categories)

# function to sort movies by category
def by_category(movies, cats_list):
    for cat in cats_list:
        print("Category: " + cat)
        for movie in movies:
            if movie['category'] == cat:
                print(movie)
by_category(movies, cats_list)

# function for calculatng average imdb of all movies in the list
def average_rating(movies):
    total = 0
    for movie in movies:
        total += movie['imdb']
    average = total / len(movies)
    print(round(average, 3))
average_rating(movies)

# function for calculating average imdb of each category
def aver_by_cat(movies, cat):
    films_by_cat = [movie for movie in movies if movie['category'] == cat]
    total = 0
    for movie in films_by_cat:
        total += movie['imdb']
    aver = total / len(films_by_cat)
    print(round(aver, 3))
for cat in cats_list:
    print(cat)
    aver_by_cat(movies, cat)