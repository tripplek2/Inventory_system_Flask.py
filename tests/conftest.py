import pytest
from models.inventory_manager import InventoryManager


@pytest.fixture
def manager():
    return InventoryManager()
