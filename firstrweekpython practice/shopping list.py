# Shopping List Manager (Mini project)
shopping_list = []

while True:
    choice = input("Enter choice (add / remove / show / quit): ")

    if choice == "add":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print("Item added")

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    elif choice == "show":
        print("Shopping list:", shopping_list)

    elif choice == "quit":
        print("Program ended")
        break

    else:
        print("Invalid choice:")
