import sys
from models.item import LostItem, FoundItem
from services.item_manager import ItemManager


def main():
    manager = ItemManager()

    # Prepopulating database engine with manual test cases
    manager.add_item(FoundItem(1, "Umbrella", "Social Hall", "Personal Effects"))
    manager.add_item(FoundItem(2, "Scientific Calculator", "Room 101", "Electronics"))

    print("=============================================")
    print("  FINDERS KEEPERS CAMPUS MANAGEMENT SYSTEM   ")
    print("=============================================\n")

    # Demonstration of administrative summary calculations
    print("[+] Current Administrative Report Metrics:")
    print(manager.generate_summary_report())
    print("-" * 45)

    # Testing try-except exception block pipeline
    try:
        print("[+] Simulating user search query submission...")
        user_lost_name = "Scientific Calculator"
        user_lost_loc = "Room 101"
        user_lost_cat = "Electronics"

        if not user_lost_name or not user_lost_loc:
            raise ValueError("Input validation failed: Crucial property values are blank.")

        search_target = LostItem(3, user_lost_name, user_lost_loc, user_lost_cat)
        print(f" -> Searching automated matching engine for: '{search_target.name}'...")

        matches = manager.find_matches(search_target)
        if matches:
            print(f"\n[!] MATCH FOUND: System discovered {len(matches)} matching object(s)!")
            for match in matches:
                print(f" -> Found Item ID [{match.id}]: {match.name} turned in at {match.location}")

            # Simulate a claim and change state
            print("\n[+] Processing item return validation...")
            manager.update_status(item_id=2, new_status="Returned")
            print("[+] Updated Admin Metrics:", manager.generate_summary_report())
        else:
            print("[-] No records matching that item description were located.")

    except Exception as e:
        print(f"[ERROR] An application exception occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()