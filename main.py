from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import schemas
import crud
import services
from database import SessionLocal, engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/address-info/", response_model=schemas.AddressRequest)
def get_address_info(address: str, db: Session = Depends(get_db)):
    tron_info = services.get_tron_address_info(address)

    # Save to DB
    db_address_request = crud.create_address_request(
        db, schemas.AddressRequestCreate(**tron_info)
    )

    return db_address_request


@app.get("/address-requests/", response_model=schemas.PaginatedAddressRequests)
def read_address_requests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_address_requests(db, skip=skip, limit=limit)
    total = crud.count_address_requests(db)

    return {
        "count": total,
        "limit": limit,
        "offset": skip,
        "items": items
    }
