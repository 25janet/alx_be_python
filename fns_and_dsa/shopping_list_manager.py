def main():
    shopping_list = []  # Empty list to start with

    while True:
        print("\n--- Shopping List Menu ---")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View shopping list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✔️ '{item}' added to the shopping list.")
            else:
                print("⚠️ Item cannot be empty.")

        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"✔️ '{item}' removed from the shopping list.")
            else:
                print(f"❌ '{item}' not found in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("🕳️ Your shopping list is empty.")

        elif choice == '4':
            print("👋 Exiting the program. Goodbye!")
            break

        else:
            print("❗ Invalid choice. Please select an option from 1 to 4.")
