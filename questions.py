from models import QuestionResponseModel

import markdown2
import pynamodb


class Question:
    q_id = None
    title = ""
    answers = []
    hardness = 0
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


# PWD
pwd = Question()
pwd.q_id = 0
pwd.title = "What folder are you in when you enter the Terminal?"
pwd.content = """
Use `pwd` to find out what folder your terminal window starts in

[fuck](https://github.com/trentm/python-markdown2/wiki/fenced-code-blocks)

```python
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class QuestionResponseModel(Model):
    class Meta:
        table_name = "question_responses"

    question_id = NumberAttribute(hash_key=True)
    response = UnicodeAttribute(null=True)


if not QuestionResponseModel.exists():
    QuestionResponseModel.create_table(read_capacity_units=1, write_capacity_units=1)
```
"""
pwd.answers = [
    "Just like every new Finder window your terminal starts off in a folder somewhere on your computer. From there you can move around your computer into different folders. It's useful to be able to know where you are on your computer.",
    "Because nothing can be simple there are a bunch of other names for 'the folder where you currently are in this terminal window'. A more common term is 'current working directory' or just 'working directory' and because of this name the command that shows where you are is called 'print working directory' = pwd",
    "the full manual page for the 'pwd' command: http://www.linuxcommand.org/lc3_man_pages/pwdh.html",
    "just type 'pwd' and hit enter",
]
pwd.hardness = 0

# LS
question = Question()
question.q_id = 1
question.title = "what's in here"
question.content = "use the ls command to see what files are in the current folder"
question.answers = [
    "to list the files in the current working directory (aka 'whatever folder I'm looking at right now') use the ls (LS) command. list = ls",
    "The manual page for the ls command http://linuxcommand.org/lc3_man_pages/ls1.html",
]
question.hardness = 0
ls = question

# CD
question = Question()
question.q_id = 2
question.title = "make there here"
question.location = "Terminal"
question.content = "Use the cd command to change your working directory to the Desktop"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.hardness = 0
cd = question

# FLAGS
question = Question()
question.q_id = 3
question.title = "flags keep commands company"
question.content = "check out the difference between running the command 'ls' and 'ls -l'. Here the dash-ell  that"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.hardness = 0
flags = question


# CAT
question = Question()
question.q_id = 4
question.title = "What's in the dictionary"
question.content = "There"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.hardness = 0
flags = question

"https://stackoverflow.com/questions/3137094/how-to-count-lines-in-a-document"

# GREP
question = Question()
question.q_id = 5
question.title = "flags keep commands company"
question.content = "Use the cd command to change your working directory to the Desktop"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.hardness = 0
grep = question

# WC
question = Question()
question.q_id = 6
question.title = "try out some new ls command options"
question.content = "You can modify the behavior of ls by adding so-called 'flags' to the end of them. for example, in 'ls -a' we would say we've 'added the `a` flag' which shows additional hidden files. Find a flag that lets you see the size of files. Now find a flag that shows you when the file was created. There's a lot of flags! You can read about the flags ls supports in the ls manual page: http://man7.org/linux/man-pages/man1/ls.1.html"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.hardness = 0
wc = question


questions = [pwd, ls, cd, flags, wc, grep]
questions = sorted(questions, key=lambda x: x.q_id)
