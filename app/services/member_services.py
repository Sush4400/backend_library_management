from sqlalchemy.orm import Session
from app.dao import member_dao
from fastapi import HTTPException, status
from app.schemas.member_schemas import MemberUpdate, MemberCreate
from app.models.member import Member



def get_members(db: Session):
    return member_dao.get_members(db)


def get_member(db: Session, member_id: int):
    member = member_dao.get_member(db, member_id)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Member not founds"
        )
    return member


def create_member(db: Session, data: MemberCreate):
    member = Member(**data.model_dump())
    return member_dao.create_member(db, member)


def update_member(db: Session, member_id: int, data: MemberUpdate):
    member = get_member(db, member_id)
    return member_dao.update_member(db, member, data)


def delete_member(db: Session, member_id: int):
    member = get_member(db, member_id)
    return member_dao.delete_member(db, member)