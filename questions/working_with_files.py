from .question_base import Question

questions = []
category = "1 - working with files"
subtitle = "make the datas go"

# Make a new folder to work in DONE

# create and delete

# create and edit

# copy


# Make, edit, and delete a file
# this sucks but you HAVE TO CHOOSE A WAY

# Copy a file
# Why?

# Rename the file

# edit the file

# CAT
question = Question()
question.q_id = 100
question.title = "make a folder and go into it"
question.content = """
**Question**: make a new folder (aka directory) named `good_at_computer`. Once you've made the directory change directory into it.

**How**: the `mkdir` command makes new directories and it requires a single argument: the name of the new folder to create. Make a new folder by running `mkdir good_at_computer` and then use `cd` to go into it: `cd good_at_computer`.

Try using `ls` and `pwd` to test that your `mkdir` and `cd` have worked.

**What to expect**: if everything goes right you won't get any output from `mkdir`. You'll want to run `ls` and check the output for your new folder if you'd like to confirm that `mkdir` worked.

```
# Make it
~ $ mkdir good_at_computer
~ $

# check for it
~ $ ls
Applications
Boostnote
. . .
git-live-view
good_at_computer <--------- there it is!
hello.bash
. . .
```

Moving into the new folder...

```bash
~ $ cd good_at_computer/                # move on in to the new folder
~/good_at_computer $ pwd                # ask "where am I?"
/Users/akarpinski/good_at_computer      # this looks good - I'm in the new folder
~/good_at_computer $ ls                 # and "what's in here?"
~/good_at_computer $                    # new prompt = no output. empty directory
```

**Why**: It's hard to find anything in your crowded home directory. My eyes tend to glaze over when I try to find one file in 100 lines of output. It's nice to be able to make your own folders and quarantine one project from another.

I'm suggesting `mkdir` early and I think it's a good tool for trying out new things in the relative safety of your own new directories.
"""
question.answers = [
    "If you haven't read about `cd` you can check out the question named [use `cd` to change which folder you're in](/2)",
    "this is [the official manual (`man` page) for `mkdir`](https://ss64.com/osx/mkdir.html)",
    "Wanna clean up after yourself? `rmdir` removes directories. Directories have to be empty before you delete them or `rmdir` will just give you an error. Here's [`rmdir`'s man page](https://ss64.com/osx/rmdir.html)",
]
question.category = category
cat = question
questions.append(cat)

question = Question()
question.q_id = 100.5
question.title = "what is a file anyway"
question.content = """

"""
question.answers = []
question.category = category
questions.append(question)

question = Question()
question.q_id = 101
question.title = "create and delete a file"
question.content = """
**What**:

- create a new file
- read the contents of the file (that is, look at what's inside)
- delete the file

**How**: You may already be familiar with the idea of a file. But in recent years web and mobile interfaces have introduced new metaphors for thinking about our data, so here's a history lesson that should be moved elsewhere.

There's a lot of ways to make a file. I've chosen just one above the fold, but check out the extra details section for some alternatives. I'm going to suggest you use `nano`. `nano` is a command line text editor aimed at ease of use and portability.

create a new file by running `nano FILENAME`. You can replace `FILENAME` with any name of your own choosing, but watch out for special characters (`!``"``$` etc)

![nano empty file example](https://s3.amazonaws.com/d34db33f/nano__Usersakarpinski_2019-08-03_12-02-54.png)

**What to expect**:

**Why**: Creating, reading, updating and deleting text files is a big part of programming. Programs are stored as text files on disk, as are configuration files and log data.
"""
question.answers = [
    "I've found a very very short article on the [absolute basics of nano](https://wiki.gentoo.org/wiki/Nano/Basics_Guide).",
    "I suggest using `nano` to create and edit a file above. There's a lot of other options and what you choose really seems to be a matter of personal preference. I think this is [a generally fine article about the differences between different terminal-based text editors](https://medium.com/linode-cube/emacs-nano-or-vim-choose-your-terminal-based-text-editor-wisely-8f3826c92a68) if you'd like to make a more informed choice yourself.",
    """Some other ways of creating a new file:

* in addition to `nano` there are other command-line text editors which will create a file if it doesn't already exist
  - `vi`, `vim` et al.
  - `emacs`
  - `pico`
  - `ed`
* `touch FILENAME` will create a new empty file named FILENAME
* you can use shell redirection to make a new file like `echo "this is gonna be in the file" >> FILENAME`

    """,
    "be wary of `rm`. This is the first command we've looked at that is properly dangerous. In the Terminal there's no concept of a trash can - once you delete something it's gone for good. Double-check what you write before hitting enter when it comes to `rm` commands. I've lost far more work to a bad `rm` than to hackers or hardware failure or anything fun like that.",
    """Most special characters will give you some sort of problem if you try to include them in your filename. They have special uses and will throw some weird errors at you. Here are some examples:
- `nano filename_?` or `*` - this will create a file just fine, but you'll have a hard time editing the file again afterwards since `*` and `?` are wildcard characters and the shell reads `*` as "0 or more letters of any kind" and `?` as "one character of any kind".
- `nano filename_\` - you'll get a new line beginning with `>`. If you hit enter again then `nano` will open. This happens because the backslash character (`\`) is an `escape character` and has the ability to negate whatever character comes after it. In this case: your <enter> keystroke got escaped.
- `nano filename_&` - on my computer that looks like

```
bash-3.2$ nano filename_&
[1] 89624
```
- `nano filename_<`
- `nano filename_<`

Workaround: if you put quotes around your filename you can call it whatever you want:
    """,
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
question.content = ""
question.answers = []
question.category = category
questions.append(question)

# Make a File
question = Question()
question.q_id = 104
question.title = "tbd"
question.content = ""
question.answers = []
question.category = category
questions.append(question)

for question in questions:
    question.category = category
    question.subtitle = subtitle
