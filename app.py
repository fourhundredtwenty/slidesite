import sys

sys.path.insert(0, "vendor/lib/python3.7/site-packages/")

import random

from flask import Flask, session, abort
from flask import render_template
from flask import jsonify

app = Flask(__name__)
app.secret_key = "eyyyy lmao"

from questions import questions, questions_by_category


@app.route("/random")
@app.route("/<string:question_id>")
def question(question_id=None):
    question_ids = [q.q_id for q in questions]

    # question is always set to a random question by default.
    # If you provide a question ID it'll go find that one
    if question_id is not None:
        try:
            question = [q for q in questions if str(q.q_id) == str(question_id)][0]
        except IndexError:
            abort(404)
    else:
        question = random.choice(questions)

    next_exists = question.q_id + 1 in question_ids
    prev_exists = question.q_id - 1 in question_ids

    return render_template(
        "app.html", question=question, next_exists=next_exists, prev_exists=prev_exists
    )


@app.route("/")
@app.route("/ls")
def list():
    return render_template(
        "question_list.html", questions_by_category=questions_by_category
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
