import docker
import tempfile
import os
import re

def execute_code(code: str):

    match = re.search(r"```python\s*(.*?)```", code, re.DOTALL)

    if match:
        code = match.group(1).strip()

    code = code.replace("```python", "")
    code = code.replace("```", "")
    code = code.strip()

    print("EXECUTING:")
    print(code)

    client = docker.from_env()

    with tempfile.TemporaryDirectory() as temp_dir:

        file_path = os.path.join(temp_dir, "temp.py")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

        output = client.containers.run(
            image="python:3.11",
            command="python /app/temp.py",
            volumes={
                temp_dir: {
                    "bind": "/app",
                    "mode": "ro"
                }
            },
            remove=True
        )

        return output.decode().strip()