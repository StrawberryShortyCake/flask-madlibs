from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def show_story_form():
    """at the load of the home page, get the fields needed to initialize
        as silly story instance, to show a respective prompts form"""

    prompts = silly_story.prompts

    return render_template(
        "questions.jinja",
        prompts=prompts
    )


@app.get("/results")
def show_completed_story():
    """gets prompt answers from query string, 
    creates dictionary with promt:answer pairs,
    generates story using answers dictionary"""

    answers = {}
    for promt in silly_story.prompts:
        # NOTE: can pass request.args to get_result_text (request.args is dictionary-like)
        # for loop still potentially good for error-handling 
        input = request.args[promt]
        answers[promt] = input

    story = silly_story.get_result_text(answers)

    return render_template(
        "results.jinja",
        story=story
    )
