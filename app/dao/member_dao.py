from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.member import Member
from app.schemas.member_schemas import MemberUpdate



def get_members(db: Session) -> list[Member]:
    stmt = select(Member).order_by(Member.id)
    return list(db.scalars(stmt).all())


def get_member(db: Session, member_id: int) -> Member|None:
    stmt = select(Member).where(Member.id==member_id)
    return db.scalar(stmt)


def create_member(db: Session, member: Member) -> Member:
    db.add(Member)
    db.commit()
    db.refresh(member)
    return member


def update_member(db: Session, member: Member, data: MemberUpdate) -> Member:
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(member, field, value)

    db.commit()
    db.refresh(member)
    return member


def delete_member(db: Session, member: Member) -> None:
    db.delete(member)
    db.commit()
