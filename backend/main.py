from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to KelanaAI"
    }


@app.get("/api/v1/recommendations")
def get_recommendations():
    return [
        "Tokyo Tower",
        "Mount Fuji",
        "Shibuya"
    ]


@app.get("/api/v1/transportations")
def get_transportations():
    return [
        "Bus",
        "Train",
        "Flight"
    ]