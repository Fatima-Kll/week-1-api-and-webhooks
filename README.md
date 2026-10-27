# Week 1 — APIs, JSON & n8n Webhooks

## Overview

This project contains two beginner exercises completed while learning API integration and workflow automation with Python and n8n.

- **Python API exercise:** Retrieves a post from JSONPlaceholder, checks the HTTP status code, extracts JSON fields, and handles request errors.
- **n8n webhook exercise:** Receives form data, validates required fields, and returns a success response or an HTTP 400 validation error.

## Technologies

- Python
- `requests`
- REST APIs and HTTP
- JSON
- n8n
- Webhooks

## Project Structure

```text
week-1-api-and-webhooks/
├── python-api/
│   └── api_exercise.py
├── n8n-webhook/
│   ├── data_receiver.py
│   └── form-validation-workflow.json
├── .gitignore
└── README.md
```

## 1. Python API Exercise

**API:** [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

The script sends a GET request to `/posts/1` and:

- Uses a 10-second timeout.
- Checks the HTTP status code.
- Parses the JSON response.
- Prints the post's title and body.
- Handles request exceptions.

### Run the API Script

Install the dependency if needed:

```bash
python -m pip install requests
```

From the `python-api` directory, run:

```bash
python api_exercise.py
```

### Tests Performed

- **Successful request:** Returned the post's title and body.
- **Nonexistent post (`/posts/9999`):** Returned HTTP 404 and displayed the failure status.
- **Invalid domain:** The request exception was caught and reported.

## 2. n8n Webhook Exercise

This workflow receives form data through a POST webhook and checks that the required fields are present.

### Expected Behavior

- **Valid input:** Returns a success response.
- **Missing required field:** Returns HTTP 400 with a validation error.

### Run the n8n Workflow

1. Open your local n8n instance.
2. Import `n8n-webhook/form-validation-workflow.json`.
3. Open the workflow and configure the Webhook node to use its Test URL.
4. Start listening for a test event.
5. Run `data_receiver.py` from the `n8n-webhook` directory.
6. Check the HTTP response and the workflow execution in n8n.

**Note:** The Python webhook script must use the correct local n8n Test URL. Test URLs require the workflow to be listening for a test event.

## Learning Outcomes

- Making HTTP GET requests with Python.
- Understanding HTTP status codes.
- Parsing JSON and accessing dictionary values.
- Handling timeouts and request exceptions.
- Receiving webhook data in n8n.
- Validating input and returning appropriate HTTP responses.

## Future Improvements

- Practise POST requests to external APIs.
- Learn API authentication and environment variables.
- Extend the workflow with additional validation and error handling.
