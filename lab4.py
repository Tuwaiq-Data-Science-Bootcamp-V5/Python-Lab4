while True:
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        if 0 <= age <= 6:
            print("Kid")
        elif age < 0:
            print("Wrong age value, you cannot enter a value less than 0.")
        else:
            total_cost = 0
            num_items = int(input("Enter the number of items you want to buy: "))

            for _ in range(num_items):
                item_name = input("Enter the item name: ")
                item_price = float(input("Enter the item price: "))
                item_quantity = int(input("Enter the item quantity: "))
                try:
                    item_cost = item_price * item_quantity
                    total_cost += item_cost
                    print(f"Item Cost: ${item_cost:.2f}")
                    print(f"Total Cost So Far: ${total_cost:.2f}")
                except ValueError:
                    print("Invalid input for price or quantity. Please enter numeric values.")

            if total_cost > 200:
                total_cost *= 0.8  # Apply a 20% discount for total cost

            print(f"Total Cost After Discount: ${total_cost:.2f}")

        repeat = input("Do you want to repeat the process? (yes/no): ")
        if repeat.lower() != "yes":
            break
    except ValueError:
        print("Invalid input for age. Please enter a valid numeric age.")