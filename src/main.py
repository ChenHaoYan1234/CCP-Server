import flask
app = flask.Flask(__name__)

if __name__ == "__main__":
    app.run("127.0.0.1", 80)
