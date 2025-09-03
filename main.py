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
    response = "pong"
    return response

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
    
@app.get("/cars/{id}")
async def getCarById(id: str):
    for car in carList:
        if(car.identifier == id):
            return car
    
    return JSONResponse(content={"error": "Couldn't find any phone with this id"}, status_code=404)

@app.put("/cars/{id}/characteristics")
async def modifyCarChar(id: str, characteristics: Characteristics):
    for car in carList:
        if(car.identifier == id):
            car.characteristics.max_speed = characteristics.max_speed
            car.characteristics.max_fuel_capacity = characteristics.max_fuel_capacity

            return car
    
    return JSONResponse(content={"error": "Couldn't find any car with this id"}, status_code=404)

    
        
