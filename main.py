from fastapi import FastAPI , Path ,HTTPException , Query
import json

app=FastAPI()

def load_data():
    with open("patients.json", 'r') as f:
        data=json.load(f)
    return data

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