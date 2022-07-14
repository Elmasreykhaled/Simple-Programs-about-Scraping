import requests
from bs4 import BeautifulSoup
print("Hello To our small program\n")
movie = input(
    "Please Enter The movie name or a word that you remember from it's name>> ")
# search = the hobbit
# https://www.whatismymovie.com/results?text=the+hobbit
url = 'https://www.whatismymovie.com/results?text='+movie.replace(' ', '+')


def movies(movie):
    return movie[-5:-1]


try:
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    all_result = soup.findAll('h3')
    all_movies = []
    for i in range(0, len(all_result), 2):
        all_movies.append(all_result[i].get_text())
    all_movies = list(set(all_movies))
    based_movies = []
    genral_movies = []
    for i in all_movies:
        if movie.lower() in i.lower():
            based_movies.append(i)
        else:
            genral_movies.append(i)
    based_movies = sorted(based_movies, key=movies, reverse=True)
    genral_movies = sorted(genral_movies, key=movies, reverse=True)
    print("\nTitle based matches\n")
    for j in based_movies:
        print(j)
    print("\nGenral matches\n")
    for k in genral_movies:
        print(k)
except:
    "Please cheack your internet or try another word"
