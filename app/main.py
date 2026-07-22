from fastapi import FastAPI # Importing the FastAPI class from the fastapi library

app = FastAPI() # this creates FastAPI application, my backend server. Everything is attached to this "app" object

@app.get("/") # this is Decorator. This says if someone sends a GET to "/", exceute the func below

def root():
    return {"return":"Welcome to Sales Analytics API"} # automatically converted into JSON