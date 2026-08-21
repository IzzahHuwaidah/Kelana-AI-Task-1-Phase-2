from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.trip import Trip
from database import SessionLocal, init_db
from services.trip_service import (
    get_trip_category,  
    calculate_daily_budget,
    get_travel_season,
)

class TripRequest(BaseModel):
        destination:    str 
        days:           int
        budget:         float
        travel_month:   str

# untuk update budget terbaru
class TripUpdate(BaseModel):
        budget:         float

app = FastAPI()

init_db()

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

# POST endpoint - receives JSON, returns JSON
@app.post("/api/v1/trips")
def create_trip(request: TripRequest) :
    daily_budget = calculate_daily_budget(
        request.budget, request.days
    )
    category = get_trip_category(
        request.budget
    )
    season = get_travel_season(request.travel_month
    )

    # create a Trip ORM object
    trip = Trip(
        destination  = request.destination,
        days         = request.days,
        budget       = request.budget,
        category     = category,
        daily_budget = daily_budget,
        travel_month = request.travel_month,
        season       = season
    )

    # save to PostgreSQL
    db = SessionLocal()
    db.add(trip)
    db.commit()
    db.refresh(trip)    # get the auto-generated id
    db.close()
    return trip

@app.get("/api/v1/trips")
def list_trips():
    db = SessionLocal()
    trips = db.query(Trip).all()
    db.close()
    return trips


@app.get("/api/v1/trips/{trip_id}")
def get_trip(trip_id: int):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    db.close()
    # handling not found
    if trip is None:
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")
    return trip

@app.put("/api/v1/trips/{id}")
def update_trip(id: int, request: TripUpdate):
    db = SessionLocal()

    trip = db.query(Trip).filter(Trip.id == id).first()

    if trip is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail=f"Trip with id {id} not found"
        )

    trip.budget = request.budget

    trip.category = get_trip_category(request.budget)

    trip.daily_budget = calculate_daily_budget(
        request.budget,
        trip.days
    )

    db.commit()
    db.refresh(trip)
    db.close()

    return trip

@app.delete("/api/v1/trips/{id}")
def delete_trip(id: int):
    db = SessionLocal()

    trip = db.query(Trip).filter(Trip.id == id).first()

    if trip is None:
        db.close()
        raise HTTPException(
            status_code=404,
            detail=f"Trip with id {id} not found"
        )

    db.delete(trip)
    db.commit()
    db.close()

    return {
        "message": f"Trip with id {id} deleted successfully"
    }