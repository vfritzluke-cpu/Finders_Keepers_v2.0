from typing import List
from models.item import Item


class ItemManager:
    """Manages the lifecycle, tracking, and matching logic of campus items."""

    def __init__(self):
        self._items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """Adds a registered item to the in-memory repository."""
        self._items.append(item)

    def get_all_items(self) -> List[Item]:
        """Retrieves all registered items."""
        return self._items

    def get_item_by_id(self, item_id: int) -> Item:
        """Finds a specific item by its unique identification key."""
        for item in self._items:
            if item.id == item_id:
                return item
        return None

    def update_status(self, item_id: int, new_status: str) -> bool:
        """Safely updates an item status (e.g., from Active to Returned)."""
        item = self.get_item_by_id(item_id)
        if item:
            item.status = new_status
            return True
        return False

    def find_matches(self, target_item: Item) -> List[Item]:
        """
        Cross-references attributes to instantly match a lost item
        with corresponding found database entries.
        """
        matches = []
        # Look for complementary types (e.g., if target is Lost, look through Found)
        target_type = "Found" if getattr(target_item, 'type', '') == "Lost" else "Lost"

        for item in self._items:
            if getattr(item, 'type', '') == target_type and item.status == "Active":
                # Normalize text values for accurate comparison checking
                if (item.name.lower() == target_item.name.lower() and
                        item.category.lower() == target_item.category.lower() and
                        item.location.lower() == target_item.location.lower()):
                    matches.append(item)
        return matches

    def generate_summary_report(self) -> dict:
        """Computes real-time analytical metrics for administrative use."""
        lost_count = sum(1 for i in self._items if getattr(i, 'type', '') == "Lost" and i.status == "Active")
        found_count = sum(1 for i in self._items if getattr(i, 'type', '') == "Found" and i.status == "Active")
        returned_count = sum(1 for i in self._items if i.status == "Returned")

        return {
            "Total Active Lost": lost_count,
            "Total Active Found": found_count,
            "Successfully Returned": returned_count
        }