from flask import Flask

app = Flask(__name__)

#   $env:FLASK_ENV = "development"
#   $env:FLASK_APP = "hello"
#   flask run
#   remember to be in right folder!
@app.route('/')
def hello():
    return 'Hello, World!'