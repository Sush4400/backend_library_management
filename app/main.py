from fastapi import FastAPI
from app.routes.api import api_router



app = FastAPI(
    title="Library Management System",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Library Management System"}
