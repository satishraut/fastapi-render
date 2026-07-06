from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def healthcheck():
    return {"status": "healthy",
            "message": "The application is running smoothly."}