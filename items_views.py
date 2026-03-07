from fastapi import APIRouter, Path, Query
from typing import Annotated

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items():
    return ["Item1", "Item2", "Item3"]


@router.get("/latest")
def read_latest_item():
    return {"item_id": "latest"}


@router.get("/{item_id}")
def read_item(
    item_id: Annotated[int, Path(ge=0, lt=1_000_000)],
    q: Annotated[str | None, Query(max_length=50)] = None,
):
    return {"item_id": item_id, "q": q}
