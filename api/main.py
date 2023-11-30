from fastapi import FastAPI

from api.core.base import Base
from api.core.base import engine

from api.routes import customer

api = FastAPI(
    title="Bank",
    description="Bank helps you do awesome stuff.",
    version="0.0.1",
    terms_of_service="http://example.com/",
    contact={
        "name": "Bank",
        "url": "http://example.com/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

api.include_router(customer.router, tags=["Customers"])

Base.metadata.create_all(bind=engine)