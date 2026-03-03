from enum import Enum

from pydantic import BaseModel


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


Selection = dict[str, str | int | float | Category | None]
