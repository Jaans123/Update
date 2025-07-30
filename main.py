from fastapi import FastAPI, Form
import json

app = FastAPI()

@app.post("/submit")
async def submit(number: str = Form(...)):
    with open("latest_number.json", "w") as f:
        json.dump({"latest": number}, f)
    return {"status": "success", "number": number}

@app.get("/latest")
async def get_latest():
    try:
        with open("latest_number.json") as f:
            data = json.load(f)
        return data
    except:
        return {"latest": ""}
