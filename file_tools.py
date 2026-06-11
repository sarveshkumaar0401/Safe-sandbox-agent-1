def save_result(content: str):
    with open("report.txt", "a", encoding="utf-8") as f:
        f.write(content + "\n")

    return "Saved successfully"

def read_report():
    with open("report.txt", "r", encoding="utf-8") as f:
        return f.read()
    
    