from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["counter"])

# In memory storage
counter_value = {"value": 0}

@router.get("/counter")
def get_counter():
    """Vrati trenutnu vrednost brojaca"""
    return counter_value

@router.post("/increment")
def increment_counter():
    """Uvecaj brojac za 1"""
    counter_value["value"] += 1
    return counter_value

@router.post("/decrement")
def decrement_counter():
    """Smanji brojač za 1"""
    counter_value["value"] -= 1
    return counter_value


@router.post("/reset")
def reset_counter():
    """Resetuj brojač na 0"""
    counter_value["value"] = 0
    return counter_value

