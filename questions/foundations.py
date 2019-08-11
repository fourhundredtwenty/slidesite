from .question_base import Question

category = "0 - foundations"
questions = []
subtitle = "start here"

# PWD
question = Question()
question.q_id = 0
question.title = "use pwd to show where you are"
question.content = """
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
question.answers = [
    "Need to open a terminal window but don't now how? I almost wrote a whole section about that but then I googled 'how to open terminal mac' because I bet someone did a better job, like with pictures and stuff. And yeah [Apple beat me to it, it's great](https://support.apple.com/en-au/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)",
    "The Terminal is sort of like the Finder app that you use to browse files. Just like every new Finder window your terminal starts off in your home folder. From there you can move around your computer into different folders.",
    "Because nothing can be simple there are a bunch of other names for 'the folder where you currently are in this terminal window'. A more common term is 'current working directory' or just 'working directory' and because of this name the command that shows where you are is called 'print working directory' = pwd",
    "[the full manual page for the 'pwd' command](https://ss64.com/osx/pwd.html). is pretty boring and useless",
    "try mistyping `pwd` and see what happens. I'd expect errors but check for yourself so you can learn what normal errors look like! I promise you won't break your computer if you type `pwc`",
]
question.category = category
pwd = question
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

**Why**: in the terminal there's no permanent view of what files are around you. If you want to know what's in front of you you have to ask. It's somewhat like sonar, you send out a ping and see what's out there. If you don't send out the ping, then you're running blind by default.  While working in the terminal you'll probably want to periodically run `ls` to see what's going on while you make changes in a folder
"""
question.answers = [
    "adding an extra word after `ls` lets you ask for the list of files in a *different* folder. for example `ls Desktop` will show you the files on your desktop, and `ls Pictures` would show you your pictures",
    """[here's the manual page for the `ls` command](https://ss64.com/osx/ls.html) it's a whole hell of a lot more interesting than the manual for `pwd`.

You can get to the same manual page by running the command `man ls` in the terminal. To get out of a `man` page you can hit `q` to quit.""",
]
question.category = category
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

You can run `pwd` now to double-check that it's worked

```
~/Desktop $ pwd
/Users/akarpinski/Desktop
```

**Why**: `cd` is the basic tool you use to get around. It's the equivalent of double-clicking a folder in the Finder, or clicking on a link on the web. You need `cd` to move from one place to another.
"""
question.answers = [
    "the first two commands you saw, `pwd` and `ls`, have been one single word. For those commands there's no spaces, no extra words: you just type `ls` and hit enter. `cd` is different because you need to tell `cd` where to take you. In general these extra words are called arguments. Some commands (like `pwd`) don't take any arguments. Others like `cd` take one, and there are even some commands that can take hundreds of arguments",
    "[here's the official manual page for `cd`](http://linuxcommand.org/lc3_man_pages/cdh.html)",
    """there are some nice shortcuts you can use with `cd`

- `cd` (that's no arguments) go to your home directory
- `cd -` go back to the last directory you were in
- `cd ..` go up a folder (e.g. /Users/kierran/Pictures-> /Users/kierran)
    """,
    """What might go wrong?

```bash
# If you try to go to a folder that doesn't exist...
$ cd Dorktop
bash: cd: Dorktop: No such file or directory

# If you try cd into a file instead of a folder
~ $ cd some_file.txt
cd: 'some_file.txt' is not a directory

# If you miss the space
$ cdDesktop
bash: cdDesktop: command not found
```
    """,
]
question.category = category
cd = question
questions.append(cd)

# FLAGS
question = Question()
question.q_id = 3
question.title = "add a flag to ls to get more details from the output"
question.content = """
**Question**:  Use the `ls` command to see the size of a file.

**How**: You can change the behavior of most commands by adding special words after the command itself. e.g. `ls -l`. These extra words are called "flags". Flags always start with a single dash (`-`) followed by a single letter e.g. `-a`. The `-l` (that's ell) flag tells `ls` to use the long-format output.  **Try it** by typing `ls -l` into your terminal and hitting enter (or return).

**What to expect**: You should get a lot more detail than `ls` without the `-l` flag. Every is the information about a single file or folder. The final column of each row is a filename. The rest of the columns in that line are additional information about that file. Here's how it looks on my machine:

```bash
~ $ ls -l
total 15136
drwx------@   5 akarpinski  staff      160 Mar 14  2018 Applications
drwxr-xr-x    6 akarpinski  staff      192 Jun  7 10:57 Boostnote
drwxr-xr-x   18 akarpinski  staff      576 Jul 23 11:59 Code
drwx------+  35 akarpinski  staff     1120 Jul 25 09:44 Desktop
drwx------   18 akarpinski  staff      576 May 10 14:19 Documents
drwx------  621 akarpinski  staff    19872 Jul 25 17:10 Downloads
drwxr-xr-x    7 akarpinski  staff      224 Mar 14  2018 Google Calendar-darwin-x64
drwx------+  82 akarpinski  staff     2624 Jul 16 10:11 Library
drwx------+   6 akarpinski  staff      192 Jan 30 20:45 Movies
... # (truncated for sanity)
```

Here is what each column means:

| permissions 	| links 	| owner (user) 	| owner (group) 	| file size 	| last modified time 	|   filename   	|
|:-----------:	|:-----:	|:------------:	|:-------------:	|:---------:	|:------------------:	|:------------:	|
| drwx------@ 	|   5   	|  akarpinski  	|     staff     	|    160    	|     Mar 14 2018    	| Applications 	|

The fifth column from the left is the file size in blocks


**Why**: Flags are the fastest, simplest way to change what a command does. The purpose of Linux manual pages is mostly to show and describe the flags available for every command, so it's important to learn early that "flags control how commands behave".
"""
question.answers = [
    "I gave you a simplified version of what flags look like above. Flags can start with a single (`-`) **or** a double dash (`--`). Usually flags that start with two dashes are just a longer and more readable version of the single-letter flag. For example, `ls -r` and `ls --reverse` do the same thing (reverse sort the output). Several commands like `find` and `git` have atypical flag formatting. These commands were all written by humans and sometimes it shows.",
    """Here's some available flags for `ls` that can show you the size of a file:

- `ls -l`      List in long format. Ownership, Date/Time etc
- `ls -s`      Display the number of file system blocks actually used by each file, in units of 512 bytes
- `ls -h`      When used with the -l option, use unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte

Here's an example of using `-s` for size together with `-h` for human-readable output

```bash
~ $ ls -lh giphy.gif
-rw-r--r--@ 1 akarpinski  staff    42K May 16  2018 giphy.gif
```

That gif is 42 kilobytes in size!

    """,
    """
`ls` isn't the only command that can tell you about file size. Here are two other commands that can do it too:

- `du`: "Display disk usage statistics" - [this SuperUser.com post has some great details](https://superuser.com/questions/162749/how-to-get-the-summarized-sizes-of-directories-and-their-subdirectories). And if you'd like to see a [man page for du](https://ss64.com/osx/du.html), there you go.
- `stat`: "Display the status of a file" - This [StackExchange.com post is only OK for describing stat](https://unix.stackexchange.com/questions/16640/how-can-i-get-the-size-of-a-file-in-a-bash-script). And the [man page is kind of a lot](https://ss64.com/osx/stat.html)

    """,
    """`ls` behaves differently on mac os and linux, including some differences in flags.

- the [macOS man page for `ls` at ss64.com](https://ss64.com/osx/ls.html)
- and the [GNU/Linux man page for `ls` at kernel.org](http://man7.org/linux/man-pages/man1/ls.1.html)

    """,
    """A handful of other useful ls flags that I like and use:
`-a`  `a` stands for `all`. This flag tells `ls` to show *all* files, including files which would [otherwise be hidden](https://askubuntu.com/questions/94780/what-are-dot-files)
`-R` recursively list all sub-directories. That is list the current dir, then go into every dir in the current dir and list that too and repeat until there's nothing unlisted.
`-1` list only one file per line. Don't produce multi-column output
`-F` add special characters after the filename to describe the file
    - `/` [directory](http://www.linfo.org/directory.html)
    - `*` [executable](http://www.linfo.org/executable.html)
    - `@` [symbolic link](http://www.linfo.org/hard_link.html) (alias)
`--help` displays help-text in the terminal and then exits
    """,
    """What happens if you try to use an invalid flag:
```bash
~ $ ls -Z
ls: illegal option -- Z
usage: ls [-ABCFGHLOPRSTUWabcdefghiklmnopqrstuwx1] [file ...]
```:
    """,
]
flags = question
questions.append(flags)

for question in questions:
    question.category = category
    question.subtitle = subtitle
