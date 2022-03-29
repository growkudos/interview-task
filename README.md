# Kudos Software Engineer Interview Task

This repository contains a simple web server, written in Python. When running,
the server exposes a simple REST-style API. You'll be adding a small new feature
to this server. Don't worry if you haven't used Python before, or written web
server code. The goal of the exercise is demonstrate your ability to read and
understand a codebase that you're new to, before extending what's already there.

## Getting Started

First of all, you'll need a copy of this codebase to work on. You can download
the code as a Zip file from the 'Code' menu on GitHub, or clone it directly
using Git (if you're comfortable using it). 

### Installing Python

You'll need to have a recent version of Python 3 installed. This code was
written for Python 3.9 or newer. You can download Python for Windows, Linux, 
and macOS on [the official Python downloads page][dl]. During Python 
setup on Windows, you'll have the option to 'Add Python 3.x to PATH' – you 
should make sure this is enabled. After installing Python on Windows, log
out or restart your computer to make sure PATH changes take effect.

You can check if Python is installed properly by running the following command
on Linux and macOS (in a terminal):

```sh
python3 --version
```

Or on Windows (CMD/Command Prompt or PowerShell):

```cmd
python --version
```

You should see the installed version of Python printed in the terminal. If you
see an error, Python 3 is not installed correctly.

[dl]: https://www.python.org/downloads/

### Creating a virtual environment

A [virtual environment][venv] will allow you to install the packages this code requires
without affecting your system Python installation. Make sure your working
directory is the top-level directory of the interview task codebase you
downloaded (the same directory as this README.md file).

First, create the virtual environment by running the following command on Linux or macOS:

```sh
python3 -m venv reminders-env
```

Or on Windows (CMD/Command Prompt or PowerShell):

```cmd
python -m venv reminders-env
```

This tells Python to create a new virtual environment in the 'reminders-env'
directory. To use the virtual environment, you need to **activate** it by
running the following command.

On Linux and macOS:

```sh
source reminders-env/bin/activate
```

Or on Windows CMD/Command Prompt:

```cmd
reminders-env\Scripts\activate.bat
```

Or on Windows PowerShell:

```ps
reminders-env\Scripts\Activate.ps1
```

You'll see the prompt change to reflect that you've activated the virtual
environment. While the virtual environment is active, all Python commands such
as `python3` and `pip` will only affect the virtual environment. 

**You should run all subsequent commands while working on this task with the
virtual environment active.**

[venv]: https://docs.python.org/3.10/tutorial/venv.html

### Install the required third-party packages

We can use `pip` to automatically download and install all the needed
requirements for this project. Run the following command (on Linux, macOS, Windows CMD/Command Prompt, and Windows PowerShell):

```sh
pip install -r requirements.txt
```

You'll see `pip` install the packages listed in requirements.txt, along with any
additional packages that are needed.

### Run the server

Let's run the server and manually test its API endpoints. To run the server,
run the following command on Linux or macOS:

```sh
FLASK_APP=reminders flask run
```

Or on Windows CMD/Command Prompt, run the following two commands:

```cmd
set FLASK_APP=reminders
flask run
```

Or on Windows PowerShell, run the following two commands:

```ps1
$env:FLASK_APP='reminders'
flask run
```

This tells [Flask][flask] to discover our app inside the `reminders` package and
run its local development server. You should see the following message:

```
 * Serving Flask app 'reminders' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

(If you see a different address in the 'Running on' line, just substitute that
address in the commands that follow.)

In a separate terminal (or command prompt window), **activate the virtual
environment**. You can then use a package called [HTTPie][httpie] that was
installed by `pip` to excercise the app's API. Here's an example that shows how
to list all current reminders, then create a new one, then check the list again.
Lines typed are prefixed with `$`, and the results of each command are given
verbatim. All commands are the same for Linux, macOS, Windows CMD/Command Prompt, and Windows PowerShell

<details>
<summary>1. Listing current reminders</summary>

```
$ http get http://127.0.0.1:5000/reminders

HTTP/1.0 200 OK
Content-Type: application/json

[
    {
        "priority": 1,
        "title": "Re-paint the living room"
    },
    {
        "priority": 2,
        "title": "Learn some Python"
    },
    {
        "priority": 3,
        "title": "Complete the interview task"
    }
]
```

</details>

<details>
<summary>2. Creating a new reminder</summary>

This one uses the `--verbose` flag so you can see the JSON request body that
HTTPie constructs from the arguments given.

```
http --verbose post  http://127.0.0.1:5000/reminders title="My new reminder" priority:=3
POST /reminders HTTP/1.1
Accept: application/json, */*;q=0.5
Content-Type: application/json

{
    "priority": 3,
    "title": "My new reminder"
}


HTTP/1.0 201 CREATED
Content-Type: application/json

{
    "priority": 3,
    "title": "My new reminder"
}
```

</details>

<details>
<summary>3. Checking current reminders</summary>

```
$ http get http://127.0.0.1:5000/reminders

HTTP/1.0 200 OK
Content-Type: application/json

[
    {
        "priority": 1,
        "title": "Re-paint the living room"
    },
    {
        "priority": 2,
        "title": "Learn some Python"
    },
    {
        "priority": 3,
        "title": "Complete the interview task"
    },
    {
        "priority": 3,
        "title": "My new reminder"
    }
]
```

</details>

As you make requests, the terminal window will show debugging output from Flask,
including details of any errors that occur. If you're trying to figure out why
something isn't working, this is a good place to check!

Once you're done with the web server, you can stop it by typing Ctrl-C in the
terminal window where the server is running.

[flask]: https://flask.palletsprojects.com/en/2.0.x/
[httpie]: https://httpie.io

### Running the automated tests

The app has a small suite of automated tests that will make sure its current
features are working as intended. These tests use [pytest][pytest] to run them
and report feedback. Pytest will automatically discover and run these tests, so
long as your working directory is the same folder as this README.md file.

In a terminal **with the virtual environment activated**, run the following
command on Linux or macOS:

```sh
python3 -m pytest
```

Or on Windows CMD/Command Prompt, or Windows PowerShell:

```cmd
python -m pytest
```

You'll see pytest report the test results:

```
=== test session starts ===
platform yourplatform -- Python 3.x.y, pytest-7.1.1, pluggy-1.0.0
rootdir: /path/to/interview-task
collected 8 items

tests/test_models.py .. [ 25%]
tests/test_routes.py ...... [100%]

=== 8 passed in 0.05s ===
```

If a test fails, pytest will report which assertion didn't succeed to help with
debugging.

[pytest]: https://docs.pytest.org/en/7.1.x/

## Task to complete

We want to extend the list reminders API endpoint at `/reminders` so that users
can list only reminders with a given priority. The priority will be given as a
query parameter in the request URL called `priority`. With the default reminders
that are loaded when the server starts, we should be able to use the following
HTTPie command and get the result below:

```
$ http get http://127.0.0.1:5000/reminders?priority=3

HTTP/1.0 200 OK
Content-Type: application/json

[
    {
        "priority": 3,
        "title": "Complete the interview task"
    }
]
```

Some tips to get you started:

- You can access the query parameters within a Flask route using 
  [`request.args`][request-args]
- You can find the code for all the routes in `reminders/__init__.py`
- Don't worry too much about writing idiomatic Python code (unless you want
  to!); this exercise isn't really about Python, but more the way in which you
  approach making a change to an existing codebase
- You should consider how you and others will test your changes.
- Don't worry if there's aspects you struggle with or are uncertain about. The
  goal of this task is to give us insight into the way you think and solve
  problems, so don't worry about submitting the code, even if you feel it's
  incomplete or there's aspects you could improve upon.

[request-args]: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.args

### Submitting your work

Please submit your work by creating a zip archive of the entire repository,
except for the `reminders-env` and `__pycache__` folders (if present). 

If you're using macOS or Linux, you can use the following command from the
directory containing the interview-task repository (one level above this
README.md file) to automatically exclude unnecessary files:

```
zip -r completed-interview-task.zip interview-task -x "*/reminders-env/*" -x "*/__pycache__/*" -x "*/.*/*"
```

(This command assumes that the directory containing the code is called
`interview-task` – if not, you'll need to adjust the above command.)

This will help to keep the size of the zip file down. Email your completed task
to [engineering@growkudos.com][sub-email] with the subject 'Engineering
interview code submission for \<YOUR NAME HERE\>'.

[sub-email]: mailto:engineering@growkudos.com?subject=Engineering%20interview%20code%20submission%20for%20YOUR%20NAME%20HERE


## Project Structure

Here's a description of the way the project is laid out:

- **README.md** – that's this file!
- **requirements.txt** – lists the Python packages this project needs.
- **reminders/** – contains the web application code
  - **__init__.py** – contains the setup code for the app along with the code
    that handles HTTP requests on each route
  - **models.py** – contains the Reminder model class that represents individual
    reminders inside the app
  - **serialization.py** – contains code that converts Reminder instances into
    simple Python lists and dicts, ready to be used in a JSON response from a
    Flask route
- **tests/** – contains the automated test code<sup>1</sup>
  - **conftest.py** – contains test configuration, including pytest fixtures to 
    automate setting up common test requirements
  - **test_models.py** – contains tests for the models in reminders/models.py
  - **test_routes.py** – contains tests for the API endpoints

<sup>1</sup> pytest will automatically discover all test functions in the tests/
directory, so long as:
- They are in a file with a name that starts with `test_` 
- The function name also starts with `test_`

This allows you to include test helper functions if needed – just make sure
they don't start with `test_`!


## Questions

If you have any questions at all about this task, want feedback, or some tips,
please don't hesitate to reach out to your Kudos contact to ask questions!
