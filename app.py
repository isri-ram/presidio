from flask import Flask, render_template,request, send_from_directory, jsonify
from movies import get_all_movies, append_movie, update_movie, delete_movies

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/movies')
def show_all_movies():
    movies = get_all_movies()
    return render_template('movies.html', movies=movies)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movie_details = {
            'name': request.form['name'],
            'director': request.form['director'],
            'release_year': int(request.form['release_year']),
            'language': request.form['language'],
            'rating': int(request.form['rating'])
        }
        append_movie(movie_details)

    return render_template('add_movie.html')

@app.route('/search_movie', methods=['POST'])
def search_movie():
    search_criteria = request.json.get('search_criteria', '').lower()
    movies = get_all_movies()

    for movie in movies:
        if search_criteria in movie['name'].lower():
            return jsonify(movie)

    return jsonify(None)


@app.route('/update_movie', methods=['GET', 'POST'])
def update_movie_route():
    if request.method == 'POST':
        movie_name = request.form.get('movieName', '')
        updated_details = {
            'name': request.form.get('name', ''),
            'director': request.form.get('director', ''),
            'releaseYear': request.form.get('releaseYear', ''),
            'language': request.form.get('language', ''),
            'rating': request.form.get('rating', '')
        }
        print(updated_details)
        success = update_movie(movie_name, updated_details)

        if success:
            return render_template('update_movie.html', movie_name=movie_name, message='Movie updated')
        else:
            return render_template('update_movie.html', message='Movie not found')

    return render_template('update_movie.html')


@app.route('/delete_movie', methods=['GET','POST'])
def delete_movie():
    if request.method == 'POST':
        movie_name = request.form.get('deleteMovieName', '')
        print(movie_name)
        if delete_movies(movie_name):
            return render_template('delete_movie.html', movie_name=movie_name, message='Movie updated')
        else:
            return render_template('delete_movie.html', message='Movie not found')
    return render_template('delete_movie.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


# if __name__ == '__main__':
#     app.run(debug=True)