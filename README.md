For Ubuntu

sudo apt install python3-venv - required to create virtual environments in Python

python3 -m venv env - creating the virtual environment

source env/bin/activate - Activate the virtual environment

python --version - Verify the environment

or -- view-> open command palette -> python create environment and select venv (so that virtual environment will be created)

pip install fastapi uvicorn

touch main.py

pip install python-dotenv

pip install openai

create a .env file

AZURE_OPENAI_ENDPOINT=https://.openai.azure.com 
AZURE_OPENAI_API_KEY=123456 
CHAT_COMPLETIONS_DEPLOYMENT_NAME=gpt

Install Python extension(Microsoft - from vs code extension) - Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.

Run -> Add configuration -> select python Debugger - Select Fastapi Launch and Debug a Fastapi web application - > launch.json will be creation .

Run -> Run without Debugging

Go to postman tool ------------------Add a post request in a collection

POST -> http://127.0.0.1:8000/qna

body - raw ->

{ "question": "write a python programme for fibonacci series using recursion", "system_prompt": "you are an ai assistant that helps people find information" }

response ->

{ "answer": "Sure, here's a Python program to print the Fibonacci series using recursion:\n\n\ndef fibonacci(n):\n    if n <= 1:\n        return n\n    else:\n        return (fibonacci(n-1) + fibonacci(n-2))\n        \nn_terms = int(input('Enter the number of terms for the Fibonacci series: '))\n\n# Validation\nif n_terms <= 0:\n    print(\"Please enter a positive integer\")\nelse:\n    print(\"Fibonacci series:\")\n    for i in range(n_terms):\n        print(fibonacci(i))\n\n\nIn this program, we first define a function fibonacci() that takes a number as an argument and returns the Fibonacci series up to that number. We use recursion to calculate the Fibonacci series.\n\nWe then ask the user to input the number of terms for the Fibonacci series they want to generate. We also add a validation check to ensure that the user has entered a positive integer.\n\nOnce we have the number of terms, we run a loop to generate the Fibonacci series using the fibonacci() function. The loop runs from 0 to the number of terms entered by the user minus one, and prints each value in the series." }
