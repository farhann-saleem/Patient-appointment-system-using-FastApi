from fastapi import FastAPI, Path, HTTPException, Query
import json
from typing import Annotated  , Literal
from pydantic import BaseModel  , Field , computed_field
from fastapi.responses import JSONResponse

app=FastAPI()

class Patient(BaseModel):
    id : Annotated[str , Field(..., description="ID of the patient " , examples=['P001'])]
    name: Annotated[str , Field(..., description="Name of the patient " )]
    city: Annotated[str , Field(..., description="Name of the Patient" )]
    age :  Annotated[int   , Field(..., gt=0 ,lt=120 ,description="City where the patient is living " )]
    gender: Annotated[str ,Literal['male' , 'female' , 'others'] ,Field(..., description="Gender of the patient")]
    height:  Annotated[float , Field(...,gt=0 ,description="In meters")]
    weight :  Annotated[float, Field(...,gt=0, description="In Kgs")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi
    
    @computed_field 
    @property
    def verdict(self)-> str:
        if self.bmi <18.5:
            return "Underweight"
        elif self.bmi <25 : 
            return "Normal"
        else :
            return "Overweight"
        


def load_data():
    with open("patients.json", 'r') as f:
        data=json.load(f)
    return data

def save_data(data):
    with open("patients.json" , 'w') as f:
        json.dump(data , f)

@app.get('/')
def hello():
    return {"message":"Patient Management System API "}

@app.get('/about')
def about():
    return {"message":"Handling all your records in one place with the power of API"}


@app.get("/view")
def view():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description='ID of the patient in DB' , example='P001')):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        # return {"error":"patient_id not found"}
        HTTPException(status_code=404 , detail="Patient not found")


@app.get("/sort")
def sort_patients(sort_by :str =Query(..., description="sort on the basis of height , weight or bmi") , order :str=Query('asc' , description='sort in ascending or descending order')):
    valid_feilds=['height' , 'weight' , 'bmi']
    valid_order=['asc', 'desc']
    if sort_by not in valid_feilds:
        raise HTTPException(status_code=400 , detail='invalid field. select from {valid_feilds}')
    
    if order not in valid_order:
        raise HTTPException(status_code=400 , detail='invalid field.select from {valid_order}')
    
    data=load_data()

        sort_order= True if order=='desc' else False
        sorted_data=sorted(data.values(), key=lambda x : x.get(sort_by, 0),reverse=sort_order)
        return sorted_data 


@app.post("/create")
def create_patient(patient:Patient):
    data=load_data()
    
    if patient.id in data:
        raise HTTPException(status_code=400 , detail="Patient Id already exists")
    
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    patient_data_to_save = patient.model_dump(exclude=['id'])
    # STEP 2: Manually add the computed fields so they are stored in the JSON file
    #         This ensures the data is complete when read back later.
    patient_data_to_save['bmi'] = patient.bmi        # <-- NEW LINE 1
    patient_data_to_save['verdict'] = patient.verdict  # <-- NEW LINE 2

    # STEP 3: Store the complete dictionary
    data[patient.id] = patient_data_to_save
    save_data(data)

    return JSONResponse(status_code=201 , content={'message':'patient created successfully'})