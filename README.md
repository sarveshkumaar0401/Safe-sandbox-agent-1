# Safe Sandbox Code Execution Agent

A Safe Sandbox Code Execution Agent built using FastAPI, PydanticAI, Ollama (Qwen3), and Docker. The agent can intelligently choose tools, execute AI-generated Python code inside an isolated Docker container, save information, and retrieve stored reports.

## Features

- AI-powered tool selection using PydanticAI
- Secure Python code execution inside Docker
- Persistent report storage
- Report retrieval
- REST API using FastAPI
- Interactive API documentation with Swagger UI

## Architecture

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/b938f102-1e3b-4441-9331-aa6fdf523558" />

## Available Tools

### run_python()

Generates and executes Python code safely inside a Docker container.

Example:

Input:
```
Calculate factorial of 5
```

Output:
```
120
```

### save_text()

Stores text in the report file.

Example:

Input:
```
Save the text "Hello World"
```

### show_report()

Displays the contents of the report file.

Example:

Input:
```
Show report
```

## Tech Stack

- FastAPI
- PydanticAI
- Ollama
- Qwen3:8B
- Docker
- Python

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/safe-sandbox-code-execution-agent.git
cd safe-sandbox-code-execution-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Pull Model

```bash
ollama pull qwen3:8b
```

### Start Ollama

```bash
ollama serve
```

### Run API

```bash
uvicorn app:app --reload
```

## API Documentation

Open:

```
http://127.0.0.1:8000/docs
```

## Project Structure

```text
safe-sandbox-code-execution-agent/
│
├── app.py
├── agent.py
├── agent_tools.py
├── executor.py
├── file_tools.py
├── report.txt
├── requirements.txt
└── README.md
```

## Example Workflow

User:
```
Calculate factorial of 5
```

Agent:
- Chooses `run_python()`
- Generates Python code
- Executes code in Docker
- Returns result

Response:
```
120
```

## Why Docker?

The agent executes AI-generated Python code. Docker provides an isolated sandbox environment that prevents generated code from directly affecting the host machine.
