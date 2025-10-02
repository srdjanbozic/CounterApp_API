from fastapi import APIRouter
import asyncio

router = APIRouter(prefix="/api", tags=["counter"])

# In memory storage sa lock-om
counter_value = {"value": 0}
counter_lock = asyncio.Lock()

@router.get("/counter")
async def get_counter():
    """Vrati trenutnu vrednost brojaca"""
    async with counter_lock:
        return counter_value

@router.post("/increment")
async def increment_counter():
    """Uvecaj brojac za 1"""
    async with counter_lock:
        counter_value["value"] += 1
        return counter_value.copy()

@router.post("/decrement")
async def decrement_counter():
    """Smanji brojač za 1"""
    async with counter_lock:
        counter_value["value"] -= 1
        return counter_value.copy()

@router.post("/reset")
async def reset_counter():
    """Resetuj brojač na 0"""
    async with counter_lock:
        counter_value["value"] = 0
        return counter_value.copy()