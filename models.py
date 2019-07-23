from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import TableError

from unittest.mock import Mock


class QuestionResponseModel(Model):
    class Meta:
        table_name = "question_responses"

    question_id = NumberAttribute(hash_key=True)
    response = UnicodeAttribute(null=True)

try:
    if not QuestionResponseModel.exists():
        QuestionResponseModel.create_table(read_capacity_units=1, write_capacity_units=1)
except TableError:
    QuestionResponseModel = Mock()
