# Sandbox Agent



A secure AI-powered code execution and conversation management system built using FastAPI, PydanticAI, Ollama, Docker, PostgreSQL, and Gradio.



## Features



* FastAPI REST API

* PydanticAI Agent Integration

* Ollama (Qwen3:8B) Local LLM

* Secure Python Code Execution in Docker Sandbox

* Tool Calling Support

* PostgreSQL Conversation Storage

* User Management using user_id

* Conversation Memory using Database History

* Token Usage Tracking

* Input Tokens Tracking

* Cached Input Tokens Tracking

* Output Tokens Tracking

* Cost Tracking (USD)

* Gradio Admin Dashboard

* Usage Analytics Dashboard



---



## Architecture



User

↓

FastAPI

↓

PydanticAI Agent

↓

Ollama (Qwen3:8B)

↓

Tool Selection



├── run_python()

│ ↓

│ Docker Sandbox

│

├── save_text()

│ ↓

│ File Storage

│

└── show_report()

↓

Response



---



## Project Structure



```text

Sandbox-Agent/

│

├── app.py

├── agent.py

├── agent_tools.py

├── executor.py

├── file_tools.py

├── db.py

├── dashboard.py

│

├── reports/

│

├── requirements.txt

│

└── README.md

```



## Database Schema



### Users



```sql

CREATE TABLE users (

    user_id VARCHAR(255) PRIMARY KEY,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

```



### Messages



```sql

CREATE TABLE messages (

    id SERIAL PRIMARY KEY,



    user_id VARCHAR(255),



    prompt TEXT,

    response TEXT,



    input_tokens INT,

    cached_input_tokens INT,

    output_tokens INT,



    cost_usd DECIMAL(10,6),



    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,



    FOREIGN KEY (user_id)

    REFERENCES users(user_id)

    ON DELETE CASCADE

);

```



---



## API Endpoint



### POST /chat



Request



```json

{

    "user_id": "sarvesh",

    "message": "Calculate factorial of 5"

}

```



Response



```json

{

    "response": "120"

}

```



---



## Token Tracking



The application records:



* Input Tokens

* Cached Input Tokens

* Output Tokens

* Cost (USD)



### Note



Cached Input Tokens are currently reported as 0 because Ollama does not expose prompt caching usage in this setup.



Conversation history is stored in PostgreSQL and resent to the model, increasing Input Tokens, but no provider-side cached tokens are reused.



---



## Running PostgreSQL



Start container:



```bash

docker start postgres-kg

```



Connect:



```bash

docker exec -it postgres-kg psql -U postgres -d sandbox_agent

```



---



## Running FastAPI



```bash

uvicorn app:app --reload

```



Swagger UI:



```text

http://127.0.0.1:8000/docs

```



---



## Running Gradio Dashboard



```bash

python dashboard.py

```



Dashboard:



```text

http://127.0.0.1:7860

```



---



## Technologies Used



* Python

* FastAPI

* PydanticAI

* Ollama

* Qwen3:8B

* Docker

* PostgreSQL

* Gradio

* Pandas



---



## Future Improvements



* User Authentication

* Vector Database Memory

* Document Upload Support

* RAG Pipeline

* Multi-Agent Support

* Real Cost Calculation for Cloud Models

* Advanced Analytics Dashboard

* Prompt Caching Support



give this as git hub code
