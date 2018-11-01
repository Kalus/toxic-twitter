# ToxicSense

A tool to visualize toxicity in social media.

# Installation

1. Clone this repository.
2. Create a python3 virtual environment and activate it. Follow instructions here https://docs.python.org/3/library/venv.html.
3. Install the requirements by running `pip install -r requirements.txt`
4. Go to ToxicSense folder and start the server with `python manage.py runserver` (Ignore the warnings about migrations)
5. Go to http://localhost:8000/

Note: If you are on a Mac and you see some weird errors about Objective C, you may need to run `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` from your terminal. It has something to do with the twitter scraper not playing well with python3 on MacOS.