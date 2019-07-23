import sys

sys.path.insert(0, "vendor/lib/python3.7/site-packages/")

import random

from flask import Flask, session, abort
from flask import render_template
from flask import jsonify

app = Flask(__name__)
app.secret_key = "eyyyy lmao"

from questions import questions, questions_by_category

from models import QuestionResponseModel


@app.route("/")
@app.route("/<string:question_id>")
def root(question_id=None):
    question = random.choice(questions)

    # question is always set to a random question by default.
    # If you provide a question ID it'll go find that one
    if question_id is not None:
        try:
            question = [q for q in questions if str(q.q_id) == str(question_id)][0]
        except IndexError:
            abort(404)

    return render_template("app.html", question=question)


@app.route("/ls")
def list():
    return render_template(
        "question_list.html", questions_by_category=questions_by_category
    )


@app.route("/respond/<int:question_id>/<string:response>")
def respond(question_id, response):
    q_response = QuestionResponseModel(question_id)
    q_response.response = response
    q_response.save()
    return q_response.response


if __name__ == "__main__":
    app.run()


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(port=8000)
