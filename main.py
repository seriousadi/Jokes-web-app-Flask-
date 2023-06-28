from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    joke = ""
    if request.method == "POST":
        api_endpoint = "https://v2.jokeapi.dev/joke/Any?type=single"
        api_response = requests.get(api_endpoint).json()
        joke = api_response["joke"]
        print(joke)
        return render_template('index.html',joke=joke)

    return render_template('index.html', joke=joke)


if __name__ == "__main__":
    app.run()
