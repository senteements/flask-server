from flask import Flask
import pyth
app = Flask(__name__)


@app.route('/')
def hello_world():
    return pyth.hellofrompython()


if (__name__ == "__main__"):
    app.run()
