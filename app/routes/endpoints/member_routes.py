from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.member_schemas import MemberUpdate, MemberCreate, MemberResponse
from app.services import member_services

router = APIRouter(prefix="/members", tags=["Members"])


router.get("/", response_model=list[MemberResponse])
def get_members(db: Session=Depends(get_db)):
    return member_services.get_members(db)


router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: int, db: Session=Depends(get_db)):
    return member_services.get_member(db, member_id)


router.post("/", response_model=MemberResponse)
def create_member(data: MemberCreate, db: Session=Depends(get_db)):
    return member_services.create_member(db, data)


router.patch("/{member_id}", response_model=MemberResponse)
def update_member(member_id: int, data: MemberUpdate, db: Session=Depends(get_db)):
    return member_services.update_member(db, member_id, data)


router.delete("/{member_id}")
def delete_member(member_id: int, db: Session=Depends(get_db)):
    return member_services.delete_member(db, member_id)