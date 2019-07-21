from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class QuestionResponseModel(Model):
    class Meta:
        table_name = "question_responses"

    question_id = NumberAttribute(hash_key=True)
    response = UnicodeAttribute(default=0)


if not QuestionResponseModel.exists():
    QuestionResponseModel.create_table(read_capacity_units=1, write_capacity_units=1)