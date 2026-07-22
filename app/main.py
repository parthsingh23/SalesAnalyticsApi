from fastapi import FastAPI

app = FastAPI(
    title="Sales Analytics API",
    description="Backend API for Sales Analytics Dashboard",
    version="1.0.0"
)

@app.get("/")
def root():
    return{
        "message":"Welcome to Sales Analytics API"
    }

@app.get("/about")
def about():
    return {
        "project": "Sales Analytics API",
        "developer": "Parth Singh"
    }

@app.get("/health")
def health():
    return {
        "status":"healthy"
    }
