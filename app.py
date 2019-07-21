import random

from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

from questions import questions

from models import QuestionResponseModel


@app.route("/")
@app.route("/<int:question_id>")
def root(question_id=None):
    if id:
        question = random.choice(questions)
    else:
        question = questions[question_id]
    return render_template("app.html", question=question)


@app.route("/ls")
def list():
    question = questions

    return render_template("question_list.html", questions=questions)


@app.route("/respond/<int:question_id>/<string:response>")
def respond(question_id, response):
    q_response = QuestionResponseModel(question_id)
    q_response.response = response
    q_response.save()
    return q_response.response