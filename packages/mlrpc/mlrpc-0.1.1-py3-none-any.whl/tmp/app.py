from fastapi import FastAPI
from sample import function

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def read_users(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}

@app.get("/demo")
def load_from_sample():
    return {"result": function()}

@app.get("/test2")
def read_users2():
    return {"skip": "skip", "limit": "limit"}