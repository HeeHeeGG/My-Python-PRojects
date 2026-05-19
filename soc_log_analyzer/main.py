from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()

@app.post("/analyze")
async def analyze_log_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt log files are accepted")
    
    content = await file.read()
    text = content.decode("utf-8")

    from analyzer import analyze_log
    results = analyze_log(text)

    return results













