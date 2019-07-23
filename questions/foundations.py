from .question_base import Question

category = "0 - foundations"
questions = []

# PWD
pwd = Question()
pwd.q_id = 0
pwd.title = "use pwd to show where you are"
pwd.content = """
**Question**: What folder are you in when you open a new Terminal window?

**How**: Run the command `pwd` by typing it into your terminal and hitting enter.

**What to expect**: The next line that prints out in the terminal, immediately after hitting enter, is the response from the terminal. If you're on a Mac it should look like `/Users/kierran`, on Linux it would be `/home/kierran` but either way, that's your home folder! After that line you should get another line that ends in `$`, that's an indication that the the terminal is ready to take your next command.

```bash
~ $ pwd
/Users/akarpinski
~ $
```

**Why**: Sometimes you need to be able to ask "where am I"? Running pwd is the equivalent of checking your URL bar in your browser to see where you are.
"""
pwd.answers = [
    "The Terminal is sort of like your Finder. Just like every new Finder window your terminal starts off in a folder somewhere on your computer. From there you can move around your computer into different folders.",
    "Because nothing can be simple there are a bunch of other names for 'the folder where you currently are in this terminal window'. A more common term is 'current working directory' or just 'working directory' and because of this name the command that shows where you are is called 'print working directory' = pwd",
    "[the full manual page for the 'pwd' command](http://www.linuxcommand.org/lc3_man_pages/pwdh.html). is pretty boring and useless",
    "try mistyping `pwd` and see what happens. I'd expect errors but check for yourself so you can learn what normal errors look like!",
]
pwd.category = "0 - foundations"
questions.append(pwd)

# LS
question = Question()
question.q_id = 1
question.title = "use ls to list files"
question.content = """
**Question**: What files are in the folder when you open a new terminal window?

**How**: Run the command `ls` (that's ell-ess) by typing it into your terminal and hitting enter. `ls` stands for `list`

**What to expect**: A bunch of new lines should come out. These are all the files in your home folder. On my computer it looks like this
```bash
~ $ ls
Applications
Boostnote
Code
Desktop
Documents
Downloads
Google Calendar-darwin-x64
Library
Movies
Music
... # abridged
```

**Why**: in the terminal there's no permanent view of what files are around you. If you want to know what's in front of you you have to ask. It's somewhat like sonar, you send out a ping and see what's out there. If you don't send out the ping, then you're running blind by default.  While working in the terminal you'll probably want to periodically run `ls` to see what's going on while you make changes in a folder"
"""
question.answers = [
    "adding an extra word after `ls` lets you ask for the list of files in a *different* folder. for example `ls Desktop` will show you the files on your desktop, and `ls Pictures` would show you your pictures",
    """[here's the manual page for the `ls` command](http://man7.org/linux/man-pages/man1/ls.1.html) it's a whole hell of a lot more interesting than the manual for `pwd`.

You can get to the same manual page by running the command `man ls` in the terminal. To get out of `man` you can hit `q` to quit.""",
]
question.category = "0 - foundations"
ls = question
questions.append(ls)

# CD
question = Question()
question.q_id = 2
question.title = "use cd to change which folder you're in"
question.content = """
**Question**: Use the `cd` command to move to your Desktop.

**How**: Run the command `cd Desktop` by typing it into your terminal and hitting enter.

**What to expect**: If everything goes right you won't get anything but a new prompt. This can look like cd failed, but it didn't. Here's it on my machine
```bash
~ $ cd Desktop
~/Desktop $
```

**Why**: Sometimes you need to be able to ask "where am I"? Running pwd is the equivalent of checking your URL bar in your browser to see where you are.
"""
question.answers = [
    "The cd command changes your current directory. It's the equivalent of double-clicking on a folder in the finder. unlike ls or pwd, cd needs information from you, the user on where to go. You say which directory you want to move to by typing it directly after cd, like this: `cd Desktop`.",
    "http://linuxcommand.org/lc3_man_pages/cdh.html",
    """What does it look like if you do it wrong?
```bash

```
""",
]
question.category = "0 - foundations"
cd = question
questions.append(cd)

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
question.category = "0 - foundations"
flags = question
questions.append(flags)
