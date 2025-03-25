from sqlalchemy.orm import Session
from models import AddressRequest
import schemas


def create_address_request(db: Session, address_request: schemas.AddressRequestCreate):
    db_address_request = AddressRequest(**address_request.dict())
    db.add(db_address_request)
    db.commit()
    db.refresh(db_address_request)
    return db_address_request


def get_address_requests(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(AddressRequest)
        .order_by(AddressRequest.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def count_address_requests(db: Session):
    return db.query(AddressRequest).count()
