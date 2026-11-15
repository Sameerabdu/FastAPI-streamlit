from fastapi import FastAPI 

app = FastAPI(
    title="My First  API Built using FastAPi",
    description="A simple API built using FastAPI",
    version="1.0.0"
)

@app.get("/")
def home():
    return{
          "message": "Welcome to my first FastAPI application!",
          "status": "success"
    }


@app.get("/greet/{name}")
def greet_user(name: str):
    return {
        "message": f"Hello, {name}!",
        "status": "success"
    }
