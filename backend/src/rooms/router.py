from fastapi import APIRouter, WebSocket

from .schemas import Room


router = APIRouter(
    prefix="/rooms",
    tags=["rooms"],
)


@router.post("/", response_model=Room)
def create_room(room: Room):
    return room.name


@router.websocket("/{room_id}")
async def join_room(websocket: WebSocket, room_id: str):
    # Check room exist
    # If it does start websocket connection
    return 