from flask import Flask, request,jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "this is home page"

@app.route("/user/<id>")
def get_user(id):
    time = datetime.datetime.now()
    data = {
        "time":time
    }

    x = jsonify(data)
    return x, 200

if __name__ == "__main__":
    app.run(debug=True)
    