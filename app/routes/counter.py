from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["counter"])

@router.post("/increment")
def increment_counter(current_value: int = 0):
    """Primi trenutnu vrednost i vrati uvećanu"""
    return {"value": current_value + 1}

@router.post("/decrement")
def decrement_counter(current_value: int = 0):
    """Primi trenutnu vrednost i vrati umanjenu"""
    return {"value": current_value - 1}

@router.post("/reset")
def reset_counter():
    """Uvek vrati 0"""
    return {"value": 0}

# Za početno učitavanje 
@router.get("/counter")
def get_counter():
    """Uvek krece od 0"""
    return {"value": 0}