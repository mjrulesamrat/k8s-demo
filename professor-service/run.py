from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/api/v1/incoming")
def incoming():
    return {"message": "You've seccussfully reached professor server!"}
