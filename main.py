from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_movie_details(movie_name):
    url = f'https://imdb.iamidiotareyoutoo.com/justwatch?q={movie_name}'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()["description"]
    return data


# Home page to enter movie name
@app.route('/')
def home():
    return render_template('index.html')

# Search results page
@app.route('/search', methods=['POST'])
def search():
    movie_name = request.form['movie_name']
    movie_details = get_movie_details(movie_name)
    
    if movie_details:
        return render_template('results.html', data = movie_details)
    else:
        return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True)
