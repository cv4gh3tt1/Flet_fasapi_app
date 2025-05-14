from fastapi import FastAPI

from database import CARS


app = FastAPI()


@app.get("/cars")
def get_cars():
    return CARS
