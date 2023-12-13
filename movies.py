import json
import os
# File to store movie records
movies_json = 'static/movies.json'

def get_all_movies():
    if not os.path.exists('static/movies.json'):
        with open(movies_json, 'w') as file:
            json.dump([], file)

    with open(movies_json, 'r') as file:
        try:
            movies = json.load(file)
        except json.JSONDecoder:
            data = []
    return movies

def append_movie(movie_details):
    movies = get_all_movies()
    movies.append(movie_details)
    write_movies(movies)

def update_movie(movie_name, updated_details):
    movies = get_all_movies()

    for movie in movies:
        if movie['name'].lower() == movie_name.lower():
            movie.update(updated_details)
            write_movies(movies)
            return True

    return False

def delete_movies(movie_name):
    movies = get_all_movies()
    movies = [movie for movie in movies if movie['name'] != movie_name]
    write_movies(movies)

def write_movies(movies):
    with open(movies_json, 'w') as file:
        json.dump(movies, file, indent=2)
