from .question_base import Question

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
question.category = "1 - working with files"
cat = question
questions.append(cat)

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
question.category = "0 - foundations"
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
question.category = "0 - foundations"
wc = question
questions.append(wc)

# Make a File
question = Question()
question.q_id = 6
question.title = "try out some new ls command options"
question.content = "You can modify the behavior of ls by adding so-called 'flags' to the end of them. for example, in 'ls -a' we would say we've 'added the `a` flag' which shows additional hidden files. Find a flag that lets you see the size of files. Now find a flag that shows you when the file was created. There's a lot of flags! You can read about the flags ls supports in the ls manual page: http://man7.org/linux/man-pages/man1/ls.1.html"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.category = "1 - working with files"
make_a_file = question
questions.append(make_a_file)
