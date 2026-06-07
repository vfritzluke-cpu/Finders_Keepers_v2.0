import pytest
from models.item import LostItem, FoundItem
from services.item_manager import ItemManager


@pytest.fixture
def manager():
    """Provides a fresh, clean ItemManager instance before each isolated test case."""
    return ItemManager()


def test_item_creation():
    """Tests if item sub-classes initialize and hold attributes accurately (SRP/LSP verification)."""
    lost_item = LostItem(id=1, name="ID Card", location="Library", category="Documents")
    assert lost_item.name == "ID Card"
    assert lost_item.category == "Documents"
    assert lost_item.type == "Lost"


def test_add_item(manager):
    """Tests if adding items to the manager collection repository works seamlessly."""
    found_item = FoundItem(id=2, name="iPhone 13", location="Canteen", category="Electronics")
    manager.add_item(found_item)
    assert len(manager.get_all_items()) == 1


def test_matching_logic(manager):
    """Tests if cross-reference filter engine automatically captures matching pairs."""
    lost = LostItem(id=3, name="Keys", location="Gym", category="Keys")
    found = FoundItem(id=4, name="Keys", location="Gym", category="Keys")
    manager.add_item(found)

    matches = manager.find_matches(lost)
    assert len(matches) == 1
    assert matches[0].name == "Keys"


def test_status_updating(manager):
    """Tests state transitions when an item is claimed and updated to 'Returned'."""
    item = FoundItem(id=5, name="Calculator", location="Room 101", category="Electronics")
    manager.add_item(item)

    success = manager.update_status(item_id=5, new_status="Returned")
    assert success is True
    assert manager.get_item_by_id(5).status == "Returned"