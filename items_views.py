from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items")


@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@router.get("/latest")
def get_latest_item():
    return {"item": {"id": "0"}}


@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000)]):
    return {
        "item": {
            "id": item_id,
        },
    }
