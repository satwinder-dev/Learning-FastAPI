from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open('devs.json' ,'r') as f:
        data = json.load(f)
    print("data read from json", data)
    return data

# @app.get("/view")
# def read_data():
#     data = load_data()
#     return data 
dc = load_data()

@app.get("/dev")
def read_root():
    print(dc)
    return dc

@app.get("/dev/{dev_id}")
def get_dev(dev_id:int):
    for dev in dc:
        if dev_id == dev["id"]:
            print(dev)
            return dev

@app.post("/dev")
def create_dev(dev : dict):
    dc.append(dev)
    return {"message":"dev added", "data":dev}

@app.put("/dev/{dev_id}")
def update(dev_id:int , updated_dev : dict):
    for index,dev in enumerate(dc):
        if dev["id"] == dev_id:
            dc[index] = updated_dev
            print(update)
            return {"message" : "dev updated", "data" : updated_dev}
        
@app.delete("/dev/{dev_id}")
def delete_dev( dev_id : int):
    for index,dev in enumerate(dc):
        if dev["id"] == dev_id:
           deleted= dc[index]
           dc.pop(index)
           print(deleted)
           return deleted