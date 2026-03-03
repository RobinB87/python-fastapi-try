from fastapi import APIRouter, HTTPException

from models.item import Category, Item, Selection

router = APIRouter(prefix="/items")

items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}


@router.get("/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, Selection | list[Item]]:
    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category == category,
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }


@router.get("/{id}")
def query_item_by_id(id: int) -> Item:
    if id not in items:
        raise HTTPException(status_code=404, detail=f"Item with {id=} does not exist.")
    return items[id]


@router.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        raise HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")
    items[item.id] = item
    return {"added": item}
