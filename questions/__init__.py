import itertools

"""
goals for this
0. foundations
- pwd
- ls
- cd

1. working with files
2. your own code
- hello world
3. other peoples' code
- clone something, what?
- libraries
4. this project
- git clone https://github.com/fourhundredtwenty/slidesite.git
- cd slidesite
"""

from . import foundations
from . import working_with_files


questions = []
questions += foundations.questions
questions += working_with_files

keyfunc = lambda x: x.category
questions = sorted(questions, key=keyfunc)
questions_by_category = {}
for k, g in itertools.groupby(questions, key=keyfunc):
    if not k in questions_by_category:
        questions_by_category[k] = []
    questions_by_category[k] += list(g)  # Store group iterator as a list
