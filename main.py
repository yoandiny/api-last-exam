from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Characteristics(BaseModel):
    max_speed: int
    max_fuel_capacity: int

class carModel(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristics
    

@app.get("/ping")
async def ping():
    return "pong !"

carList = []

@app.post("/cars")
async def addCar(car: carModel):
    if(car):
        carList.append(car)
        return JSONResponse(content={"message":"Car successfully added"}, status_code=201)
    else:
        return JSONResponse(content={"error": "Car couldn't be added"})
    
@app.get("/cars")
async def getCarList():
    return carList
    
    
        
