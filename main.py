from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def root():
    return {"原神nb"}

@app.get("/ping")
def ping():
    return {"原神不nb"}
