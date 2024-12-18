from fastapi import FastAPI
from models import userModel
import uvicorn
from database.connection import engine

#config database
userModel.Base.metadata.create_all(bind= engine)

#create an instance of the server

app =  FastAPI()


@app.get('/')
def main():
    return{"Welcome"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)