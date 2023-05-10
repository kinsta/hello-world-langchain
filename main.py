import os

from flask import Flask, abort, render_template
import openai
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

if not os.environ.get('OPENAI_API_KEY'):
    raise Exception("OPENAI_API_KEY is not set")

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/ask")
def ask():
    llm = OpenAI(temperature=0.7)
    text = "Tell me a joke about artificial intelligence."
    return llm(text)


@app.route("/<path:any_path>")
def catch_all(any_path):
    abort(404)


if __name__ == "__main__":
    app.run()
