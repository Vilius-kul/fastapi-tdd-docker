from fastapi import FastAPI

app = FastAPI()


@app.route("/ping")
def pong():
    return {"ping": "pong"}
