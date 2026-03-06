from fastapi import FastAPI
app = FastAPI()

dc = [
    {
        "id" : 1,
        "name": "Satwinder",
        "tech": ["React", "Next.js"],
        "city": "Patiala"
    },
    {
        "id" : 2,
        "name": "Rahul",
        "tech": ["Python", "FastAPI"],
        "city": "Delhi"
    },
    {   
        "id" : 3,
        "name": "Ankit",
        "tech": ["Node.js", "Express"],
        "city": "Mumbai"
    },
    {
        "id" : 4,
        "name": "Priya",
        "tech": ["Angular", "TypeScript"],
        "city": "Bangalore"
    },
    {
        "id" : 5,
        "name": "Simran",
        "tech": ["Django", "PostgreSQL"],
        "city": "Chandigarh"
    },
    {
        "id" : 5,
        "name": "Simran",
        "tech": ["Django", "PostgreSQL"],
        "city": "Chandigarh"
    }
]

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
       
@app.patch("/dev/{dev_id}")
def update_dev(dev_id : int , updated_fields: dict):
    for dev in dc :
        if dev["id"] == dev_id:
            dev.update(updated_fields)
            updated = dev
            print(updated)
            return updated