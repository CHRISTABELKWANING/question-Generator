QUESTION GENERATOR
# Project Overview
The Question Generator is a web application built withHTML, CSS and PYTHON(FastAPI).
It allows users to generate by entering a subject, topic, and the number of questions they want to generate.
The application sends the user's request to the Startocode Question Generator API and displays the generated 
questions in the browser.

# Features
.Generate questions based on a selected subject and topic.
.Choose the number of questions to generate.
.User-friendly web interface.
.FastAPI backend for handling form submissions and API requests.
.Displays generated questions in an easy-to-read format.

# Technologies Used
. Frontend: HTML, CSS
. Backend: Python, FastAPI
. API: Request Library
. Server: Uvicorn
. Tools: Git and GitHub

# Steps/Approach
. Created the project structure.
. Designed the user interface using HTML and CSS.
. Built the backend using FastAPI
. Created a form to collect the subject, topic, and number of questions.
. Sent the user's input to the Startocode Question Generator API using the Request library.
. Processed the API response.
. Displayed the generated questions on the webpage.
. Tested and debugged the application to resolve errors and improve functionality.

# Future Improvement 
. Improve the user interface and overall design
. Add loading indicators while questions are being generated.
. Improve error handling for API failures and invalid input.
. Allow users to download generated questions as PDF or text file.
. Add different difficulty levels for generated questions.
. Save previously generated qestions for later review.

# How to run te project
. Clone the repository.
. Created and activate a virtual environment.
. Install the required package:
--bash
--pip install fastapi uvicorn requests python-multipart

Start the server:
--bash
--uvicorn main:app --reload

open the browser and visit:
-- https://127.0.0.1:8000

# Author 
CHRISTABEL KWANING

