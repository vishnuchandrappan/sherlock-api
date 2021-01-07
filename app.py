from flask import Flask, request
from core.sherlock_interface import parseSherlockResults
from flask_apispec import FlaskApiSpec

docs = FlaskApiSpec(app)
app = Flask(__name__)


@app.route('/')
def helloWorld():
    return {
        "status": "ok",
        "message": "sherlock api v1"
    }


# takes about 22000 ms
@app.route('/user/<username>')
def showUser(username):
    result = parseSherlockResults(username)
    return {
        "status": "ok",
        "data": result
    }


@app.route('/user')
def index():
    usernames = request.args["usernames"].split(",")
    final = {}
    for username in usernames:
        result = parseSherlockResults(username.strip())
        final[username] = result

    return {
        "data": final
    }


if __name__ == "__main__":
    app.run(debug=True)
