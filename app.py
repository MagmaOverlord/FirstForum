import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def home():
  return flask.render_template('index.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

if __name__ == "__main__":
  app.run()