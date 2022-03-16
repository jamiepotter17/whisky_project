from flask import Flask

whiskyapp = Flask(__name__)

@whiskyapp.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    whiskyapp.run()
