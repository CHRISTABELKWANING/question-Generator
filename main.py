import json
import requests

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

STARTOCODE_QUESTION_GENERATOR = "https://startocode-ai-api-v1.fly.dev/ask"


def build_page(result_html=""):
    with open("templates/index.html", "r", encoding="utf-8") as file:
        html = file.read()

    html = html.replace("<!--RESULT-->", result_html)
    return html


@app.get("/")
def home():
    return HTMLResponse(build_page())


@app.post("/generate")
def generate(
    subject: str = Form(...),
    topic: str = Form(...),
    num_question: int = Form(...)
):
    instructions = (
        f"Generate exactly {num_question} questions about the topic "
        f"{topic} in the subject {subject}. "
        "Return ONLY a JSON array of strings, no other text."
    )
    data = {
        "subject": subject,
        "topic": topic,
        "num_question": num_question
    }

    response = requests.post(
        STARTOCODE_QUESTION_GENERATOR,
        json={"question": instructions},
        timeout=30,
    )

    data = response.json()
    print(instructions)
    print(data)


    #Parse the question from API response
    answers = data.get("answers", "")

    try:
        questions = json.loads(answers)
    except json.JSONDecodeError:
        questions = answers.split("\n")

    # build the result list
    questions_html = ""
    for question in questions:
        question = question.strip()
        if question:
            questions_html = questions_html + f"<li>{question}</li>"

    result_html = f"""
    <div class="results">
        <h2>{subject} - {topic}</h2>
        <ol>{questions_html}</ol>
    </div>
    """

    return HTMLResponse(build_page(result_html))