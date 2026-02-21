from fastapi import FastAPI

app = FastAPI(title="Email Ingestion System")

@app.get("/")
def health_check():
    return {"status": "ok"}