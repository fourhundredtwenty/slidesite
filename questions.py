class Question:
    title = ""
    content = ""
    answers = []
    hardness = 0


# PWD
pwd = Question()
pwd.title = "where am I"
pwd.content = "Use pwd to find out what folder your terminal window starts in"
pwd.answers = [
    "Just like every new Finder window your terminal starts off in a folder somewhere on your computer. From there you can move around your computer into different folders. It's useful to be able to know where you are on your computer.",
    "Because nothing can be simple there are a bunch of other names for 'the folder where you currently are in this terminal window'. A more common term is 'current working directory' or just 'working directory' and because of this name the command that shows where you are is called 'print working directory' = pwd",
    "the full manual page for the 'pwd' command: http://www.linuxcommand.org/lc3_man_pages/pwdh.html",
    "just type 'pwd' and hit enter",
]
pwd.hardness = 0

# LS
question = Question()
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
question.title = "flags keep commands company"
question.content = "Use the cd command to change your working directory to the Desktop"
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "try using pwd after cd to see if it worked how you expect",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
]
question.hardness = 0
wc = question


questions = [pwd, ls, cd, flags, wc, grep]
