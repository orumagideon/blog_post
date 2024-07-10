# Define your user-related routes and functions here

from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return [{"name": "Alice"}, {"name": "Bob"}]

# Remember to include your router in the main application
