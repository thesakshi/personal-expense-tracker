from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Personal Expense Traker API is running!"}