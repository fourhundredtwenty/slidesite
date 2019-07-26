from .question_base import Question

questions = []
category = "1 - working with files"
subtitle = "make the datas go"

# CAT
question = Question()
question.q_id = 100
question.title = "read the contents of a file"
question.content = "There"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.category = category
cat = question
questions.append(cat)

"https://stackoverflow.com/questions/3137094/how-to-count-lines-in-a-document"

# GREP
question = Question()
question.q_id = 101
question.title = "absolute vs. relative paths"
question.content = "Use the cd command to change your working directory to the Desktop"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.category = category
questions.append(question)

question = Question()
question.q_id = 102
question.title = "write to a file"
question.content = "Use the cd command to change your working directory to the Desktop"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.category = category
questions.append(question)

# WC
question = Question()
question.q_id = 103
question.title = "idk"
question.content = "You can modify the behavior of ls by adding so-called 'flags' to the end of them. for example, in 'ls -a' we would say we've 'added the `a` flag' which shows additional hidden files. Find a flag that lets you see the size of files. Now find a flag that shows you when the file was created. There's a lot of flags! You can read about the flags ls supports in the ls manual page: http://man7.org/linux/man-pages/man1/ls.1.html"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.category = category
questions.append(question)

# Make a File
question = Question()
question.q_id = 104
question.title = "try out some new ls command options"
question.content = "You can modify the behavior of ls by adding so-called 'flags' to the end of them. for example, in 'ls -a' we would say we've 'added the `a` flag' which shows additional hidden files. Find a flag that lets you see the size of files. Now find a flag that shows you when the file was created. There's a lot of flags! You can read about the flags ls supports in the ls manual page: http://man7.org/linux/man-pages/man1/ls.1.html"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.category = category
questions.append(question)

for question in questions:
    question.category = category
    question.subtitle = subtitle
