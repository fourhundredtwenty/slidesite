from models import QuestionResponseModel

import markdown2
import pynamodb


class Question:
    q_id = None
    title = ""
    _answers = []
    category = 0
    _content = ""

    # The response field stores the user's button-click in a database
    @property
    def response(self):
        try:
            return QuestionResponseModel.get(self.q_id)
        except QuestionResponseModel.DoesNotExist:
            qr = QuestionResponseModel(self.q_id)
            qr.save()
            return self.response

    # renders content to markdown
    @property
    def content(self):
        return markdown2.markdown(self._content, extras=["fenced-code-blocks"])

    @content.setter
    def content(self, content):
        self._content = content

    @property
    def answers(self):
        return [
            markdown2.markdown(answer, extras=["fenced-code-blocks"])
            for answer in self._answers
        ]

    @answers.setter
    def answers(self, answers):
        self._answers = answers
