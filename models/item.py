from abc import ABC

class Item(ABC):
    """Base class for all campus items."""
    def __init__(self, id: int, name: str, location: str, category: str, status: str = "Active"):
        self.id = id
        self.name = name
        self.location = location
        self.category = category
        self.status = status  # e.g., "Active", "Returned"

class LostItem(Item):
    """Represents an item reported lost by an owner."""
    def __init__(self, id: int, name: str, location: str, category: str, status: str = "Active"):
        super().__init__(id, name, location, category, status)
        self.type = "Lost"

class FoundItem(Item):
    """Represents an item found and turned in by a finder."""
    def __init__(self, id: int, name: str, location: str, category: str, status: str = "Active"):
        super().__init__(id, name, location, category, status)
        self.type = "Found"