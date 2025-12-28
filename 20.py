print("Shopping list manager")
LIST=[]

while True:
    print("Choose an option:add/remove/show/quit")
    choice=input("Enter your choice:")
    if choice=="add":
        print("Enter item name:")
        item=input()
        LIST.append(item)
        print("Item has been added.")
    elif choice=="remove":
        print("Enter item name:")
        item=input()
        if item in LIST:
            LIST.remove(item)
            print("Item removed")
        else:
            print("Item not found")
    elif choice=="show":
        print("Shopping list:")
        print(LIST)
    elif choice=="quit":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
