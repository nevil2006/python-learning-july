from menu import items

def display_menu():
    print("Welcome to the Digital Vending Machine!")
    print("Available items:")
    for key, item in items.items():
        print(f"{key}. {item['name']} - ₹{item['price']}")

def vending_machine():
    while True:
        display_menu()
        choice = input("Enter item number (or 'q' to quit): ")

        if choice == 'q':
            print("Thank you for using the vending machine!")
            break

        try:
            item = items[choice]
            print(f"You selected: {item['name']} - ₹{item['price']}")
            money = int(input("Insert money: ₹"))

            if money >= item["price"]:
                change = money - item["price"]
                print(f"Dispensing {item['name']}... Change: ₹{change}\n")
            else:
                print("❌ Not enough money. Transaction cancelled.\n")
        except KeyError:
            print("⚠️ Invalid item selection. Try again.\n")
        except ValueError:
            print("⚠️ Please insert a valid amount.\n")

vending_machine()
