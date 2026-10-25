# python-repo 🐍

This repository is loaded with a bunch of programming exercises written in Python.

*Essential knowledge of python is required to understand this code.*

Find the problems description under the doc folder:

* [Day of year](./doc/day_of_year.md)
* [Is prime](./doc/is_prime.md)

## Prerequisites

* Make sure Python 3 is installed and working on your system (if not, see the next section).
* Check if Python is in PATH, and add it if not. 

## 💾 Python 3 Installation

There are several ways to get your own copy of Python 3, depending on the operating system you use.

### Linux

Linux users most probably have Python already installed, because Python's infrastructure is intensively used by many Linux OS components.
If you're a Linux user, open the terminal/console, and type:

```
python3
```

at the shell prompt, press Enter and wait.

If you see something like this:

```
$ python3
Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

then you don't have to do anything else.
If Python 3 is absent, then refer to your Linux documentation in order to find out how to use your package manager to download and install a new package – the one you need is named python3 or its name begins with that.

### ¬ Linux

All non-Linux users can download a copy at https://www.python.org/downloads/ .

## 📂 Project structure 

The src folder contains the scripts, while the site folder holds the problem descriptions.

```
/
└── python-repo
    │
    ├── src
    │   ├── day_of_year.py
    │   ├── is_prime.py
    │   └── ...
    │
    ├── site
    │   ├── day_of_year.md
    │   ├── is_prime.md
    │   └── ...   
    │
    └── README.md          
```