# TextParse

[![Build Status](https://travis-ci.com/chowdhury18/TextParse.svg?branch=master)](https://travis-ci.com/github/chowdhury18/TextParse)

This application accepts post requests from the client and parses the given text. The backend service is built on [Flask](https://flask.palletsprojects.com/en/1.1.x/). A simple test case is written using [Pytest](https://docs.pytest.org/en/stable/) and the application is tested using [Travis CI](https://travis-ci.com/). The application is also deployed in [Heroku-Cloud Application Platform](https://www.heroku.com/) and can be accessed following the [link](https://chowdhury-textparser.herokuapp.com/).

## Getting Started

## Pre-requisite
- Python3
- Flask
- Pytest

## Step by step
Follow the instructions run the application.

- Install the dependencies.
```
pip3 install -r requirements.txt
```

- Run the application. (The application will run at http://localhost:5000)
```
python3 app.py
```

- Test the application. (make sure you are in the same folder as the test file)
```
pytest
```

- Test and build the application using [Travis CI](https://travis-ci.com/). Git add, commit and push to trigger a Travis CI build.
```
.travis.yml
--
language: python
python:
  - "3.6"
  - "pypy3"
install:
  - pip install -r requirements.txt
script: pytest
```

- Deploy the application to Heroku.
    
    - Login to heroku.
    ```
    heroku login
    ```
    
    - Create project
    ```
    heroku create <project-name> --buildpack heroku/python
    ```

    - Add the git repo to the Heroku
    ```
    heroku git:remote -a <project-name>
    ```

    - Install [gunicorn](https://gunicorn.org/). Gunicorn is a Python WSGI HTTP Server for UNIX.
    ```
    pip3 install gunicorn
    ```

    - Add the [Procfile](https://devcenter.heroku.com/articles/procfile) to specify the commands that are executed by the app on startup.
    ```
    web: gunicorn app:app
    
    # web - process type (web server)
    # app:app - First app represents the name of the python file or the application module (e.g., app.py) and the second app represents the flask app within app.py.
    ```

    - Git add, commit and push to Heroku.
    ```
    git add .
    git commit -m "<any-message>"
    heroku push heroku master
    ```

    - Test the application in browser
    ```
    https://<project-name>.herokuapp.com/
    ```

- Test the application locally

    - Download [postman](https://www.postman.com/) OR use command line tool [curl](https://curl.haxx.se/) to execute the operations. The following [link](https://www.taniarascia.com/making-api-requests-postman-curl/) has the instructions to execute CRUD in both postman and curl.

    - Follow the instruction to complete the post request to the endpoint **/analyze**
    ```
    Method: POST
    Application-type: application/json
    Request-Body:
    {
        "text" : "Life is beautiful."
    }
    Response-Body:
    {
        "characterCount": [{"a": 1},{"b": 1},{"e": 2},{"f": 2},{"i": 3},{"l": 2},{"s": 1},{"t": 1},{"u": 2}],
        "textLength": {
            "withSpaces": 18,
            "withoutSpaces": 16
        },
        "wordCount": {
            "wordCount": 3
        }
    }
    ```