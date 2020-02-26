import flask
from flask import request

app = flask.Flask(__name__)

generalP = []
gamesP = []
tvP = []
booksP = []

@app.route('/')
def home():
  return flask.render_template('index.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == "GET": 
        return flask.render_template('books.html', posts = booksP)
    else:
        post = request.json
        booksP.append(post)
        return flask.render_template('books.html', posts = booksP)

@app.route('/games', methods=['GET', 'POST'])
def games():
    if request.method == "GET": 
        return flask.render_template('games.html', posts = gamesP)
    else:
        post = request.json
        gamesP.append(post)
        return flask.render_template('games.html', posts = gamesP)

@app.route('/general', methods=['GET', 'POST'])
def general():
    if request.method == "GET": 
        return flask.render_template('general.html', posts = generalP)
    else:
        post = request.json
        generalP.append(post)
        return flask.render_template('general.html', posts = generalP)
        

@app.route('/tv', methods=['GET', 'POST'])
def tv():
    if request.method == "GET": 
        return flask.render_template('tv.html', posts = tvP)
    else:
        post = request.json
        tvP.append(post)
        return flask.render_template('tv.html', posts = tvP)

@app.route('/post')
def post():
    return flask.render_template('post.html')

if __name__ == "__main__":
  app.run()