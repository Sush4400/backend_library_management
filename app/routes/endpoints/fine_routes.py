from fastapi import APIRouter, Depends
from app.services import fine_services
from app.schemas.fine_schemas import FineCreate, FineUpdate, FineResponse
from app.db.database import get_db


router = APIRouter(prefix="/fines", tags=["Fines"])


router.get("/", response_model=list[FineResponse])
def get_fines():
    pass


router.get("/{fine_id}", response_model=FineResponse)
def get_fine():
    pass


router.post("/", response_model=FineResponse)
def create_fine():
    pass


router.patch("/{fine_id}", response_model=FineResponse)
def update_fine():
    pass


router.delete("/{fine_id}")
def delete_fine():
    pass