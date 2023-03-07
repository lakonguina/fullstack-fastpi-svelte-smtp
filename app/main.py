from fastapi import FastAPI

from app.core.base import Base
from app.core.base import engine

from app.v1 import customer

app = FastAPI()

app.include_router(customer.router, tags=["customers"])

Base.metadata.create_all(bind=engine)
