#program to view,add and remove items in the shopping list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list succesfully!")
            else:
                print("Shopping list cannot be empty")
        
        elif choice == "2":
            item = input("Enter the name of the item to be removed from the list: ").strip()
            
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed succesfully!")
            else:
                print("'{item}' is not in the shopping list!")
        
        elif choice == "3":
            if shopping_list:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("\nYour shopping list is currently empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
        
        