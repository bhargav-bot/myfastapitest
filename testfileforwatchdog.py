from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


app=FastAPI(default_response_class=ORJSONResponse)

@app.get("/")
async def root():
    return {"message": "Hello World123456"}
