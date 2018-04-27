# DangerDrive

To run, be sure to use python 3 and make sure Flask and Requests are installed.

There is a Pipfile included if you wish to use pipenv.

## To Run using pipenv (Tested on Linux and Windows)
Clone this repository.
Navigate into the project directory.
Run the following terminal commands.
```
pip install pipenv
pipenv shell --three
pipenv install
export FLASK_APP=DangerDrive.py
flask run
```

## To Run without pipenv
Clone this repository.
Navigate into the project directory.
Run the following terminal commands.
```
pip install flask
pip install requests
export FLASK_APP=DangerDrive.py
flask run
```

You may have to use pip3 instead of pip.

## Usage
Navigate to the address specified by flask (It's probably http://127.0.0.1:5000/).

## IMPORTANT NOTE!!!
This repository does not include our API keys!  The code submitted with our report has the API keys included.