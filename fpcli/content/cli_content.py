from pydoc import classname


def get_views_content(name: str):
    class_name = f"{name.capitalize()}View"
    return f'''
from fastapi import Request

class {class_name}:

    async def index(self):
        """Get all the data"""
        
        return " Get all the data."

    async def edit(self, uuid: str):
        """Read or edit the data based on the given UUID. """
        
        return "Read or edit the data based on the given UUID. "

    async def create(self, request: Request):
        """Create new data based on the request."""

        return f"Create new data based on the request."

    async def update(self, request: Request, uuid: str):
        """Update the data based on the given UUID."""
        
        return f"fUpdate the data based on the given UUID."

    async def destroy(self, uuid: str):
        """ Delete the data based on the given UUID."""
        
        return "for delete the data"
        '''


def get_model_contant(name: str, app_name: str=None):
    class_name = f"{name.capitalize()}Model"
    return f'''
from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel,Field
import datetime


class {class_name}(SQLModel,table=True):
    """
    StudentModel represents the schema for student.
    """
    __tablename__ = '{app_name}_{name}'

    id: int= Field(default=None, primary_key=True)
    name: str
    status: Optional[bool] = Field(True, description="Last update timestamp")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(default=None, description="Last update timestamp")
    deleted_at: Optional[datetime] = Field(default=None, description="Deletion timestamp")


    '''


def get_validator_content(name: str):
    class_name = f"{name.capitalize()}Schema"
    return f'''
from pydantic import BaseModel, Field
from typing import Optional

class {class_name}(BaseModel):
    """
    {class_name} is used to validate {name} data.
    """
    uuid: Optional[str] = Field(None, description="Unique identifier for the data")
    name: str = Field(..., description="Name field")
    '''


def get_servie_content(name: str):
    class_name = f"{name.capitalize()}Service"

    return f'''
from typing import List, Optional
from sqlmodel import Session, select
from ..models.{name.lower()}_model import {name.capitalize()}Model
from uuid import UUID

class {class_name}:
    """
    {class_name} handles the business logic and database operations for {name}.
    """

    @staticmethod
    async def create(session: Session, data: dict) -> {name.capitalize()}Model:
        """
        Create a new {name.capitalize()}.
        """
        instance = {name.capitalize()}Model(**data)
        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance

    @staticmethod
    async def get_all(session: Session) -> List[{name.capitalize()}Model]:
        """
        Fetch all {name}s.

        Returns:
            List[{name.capitalize()}Model]: List of all {name}s.
        """
        result = session.exec(select({name.capitalize()}Model)).all()
        return result

    @staticmethod
    async def get_by_id(session: Session, uuid: UUID) -> Optional[{name.capitalize()}Model]:
        """
        Fetch a {name} by its UUID.
        """
        return session.get({name.capitalize()}Model, uuid)

    @staticmethod
    async def update(session: Session, uuid: UUID, data: dict) -> Optional[{name.capitalize()}Model]:
        """
        Update an existing {name}.
        """
        instance = session.get({name.capitalize()}Model, uuid)
        if instance:
            for key, value in data.items():
                setattr(instance, key, value)
            session.commit()
            session.refresh(instance)
        return instance

    @staticmethod
    async def delete(session: Session, uuid: UUID) -> bool:
        """
        Delete a {name} by its UUID.
        """
        instance = session.get({name.capitalize()}Model, uuid)
        if instance:
            session.delete(instance)
            session.commit()
            return True
        return False

    '''


def get_middleware_content(name: str):
    class_name = f"{name.capitalize()}Middleware"

    return f'''
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging

class {class_name}(BaseHTTPMiddleware):
    """
    {class_name} is a custom middleware for processing requests and responses.
    """
    async def dispatch(self, request: Request, call_next):
        """
        Intercept the incoming request, process it, then call the next handler.
        
        Args:
            request (Request): The incoming request.
            call_next (Callable): The function to call the next middleware or route handler.
        
        Returns:
            Response: The final response to be returned.
        """


        # Call the next middleware or route handler
        response = await call_next(request)


        return response
    '''


def get_seeder_content(name: str, app_name: str):
    class_name = f"{name.capitalize()}Seeder"
    service_name = f"{name.capitalize()}Service"
    return f'''
import asyncio
from {app_name.lower()}.services.{name.lower()}_service import {service_name}

class {class_name}:
    """
    Seeder for {name.capitalize()}Model to populate initial data.
    """

    @staticmethod
    async def run():
        """
        Run the seeder to insert sample data into the database.
        """
        data = [
            {{
                "status": True,
                "created_at": "2025-01-01T00:00:00Z",
                "updated_at": "2025-01-01T00:00:00Z"
            }},
            {{
                "status": False,
                "created_at": "2025-01-02T00:00:00Z",
                "updated_at": "2025-01-02T00:00:00Z"
            }}
        ]

        # Insert the data into the database using a loop
        for record in data:
            await {service_name}.create(record)

        print(f"{class_name} seed successfully!")
    '''




def get_route_content(controller_name: str, method: str, route_name: str):
    """
    Generate FastAPI route snippet in the format of app_router.add_api_route.
    
    Args:
        controller_name (str): The name of the controller (e.g., UserController).
        method (str): HTTP method (GET, POST, PUT, DELETE, etc.).
        route_name (str): The route name (e.g., '/user/', '/user/create').
    
    Returns:
        str: The generated route snippet in the desired format.
    """
    # Extract the controller method name dynamically
    controller_method = route_name.strip('/').replace('/', '_')

    # Generate the route content in app_router.add_api_route format
    return f'app_router.add_api_route("{route_name}", {controller_name}().{controller_method}, methods={["{method}"]})'

