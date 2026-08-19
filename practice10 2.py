product_names = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
product_prices = [50000, 800, 1500, 12000, 10000]
product_qty = [10, 25, 15, 8, 5]

while True:
    print("\n" + "=" * 45)
    print("      PRODUCT INVENTORY SYSTEM")
    print("=" * 45)
    print("1. Add Product")
    print("2. Delete Product")
    print("3. Update Product Price")
    print("4. Display All Products")
    print("5. Search Product")
    print("6. Sort Products by Price (Ascending)")
    print("7. Sort Products by Price (Descending)")
    print("8. Sort Products by Name")
    print("9. Show Costliest / Cheapest Product")
    print("10. Exit")
    print("=" * 45)

    choice = input("Enter your choice (1-10): ").strip()

    if choice == "1":
        name = input("Enter product name: ").strip()

        if name in product_names:
            print("Product already exists!")
        else:
            price = float(input("Enter price: "))
            qty = int(input("Enter quantity: "))

            product_names.append(name)
            product_prices.append(price)
            product_qty.append(qty)

            print("Product added successfully.")

    elif choice == "2":
        name = input("Enter product name to delete: ").strip()

        if name in product_names:
            index = product_names.index(name)
            product_names.pop(index)
            product_prices.pop(index)
            product_qty.pop(index)
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    elif choice == "3":
        name = input("Enter product name: ").strip()

        if name in product_names:
            index = product_names.index(name)
            new_price = float(input("Enter new price: "))
            product_prices[index] = new_price
            print("Price updated successfully.")
        else:
            print("Product not found.")

    elif choice == "4":
        if len(product_names) == 0:
            print("No products available.")
        else:
            for i in range(len(product_names)):
                print(
                    i, 
                    product_names[i],
                    "Price:", product_prices[i],
                    "Qty:", product_qty[i]
                )

    elif choice == "5":
        name = input("Enter product name to search: ").strip()

        if name in product_names:
            index= product_names.index(name)

            print("\nProduct Found!")
            print("Product Name   :", product_names[index])
            print("Index Location :", index)
            print("Price          :", product_prices[index])
            print("Quantity       :", product_qty[index])
        else:
            print("Product not found in the inventory.")

    elif choice == "6":
        combined = list(zip(product_prices, product_names, product_qty))
        combined.sort()

        product_prices = [x[0] for x in combined]
        product_names = [x[1] for x in combined]
        product_qty = [x[2] for x in combined]

        print("Products sorted by price (ascending).")

    elif choice == "7":
        combined = list(zip(product_prices, product_names, product_qty))
        combined.sort(reverse=True)

        product_prices = [x[0] for x in combined]
        product_names = [x[1] for x in combined]
        product_qty = [x[2] for x in combined]

        print("Products sorted by price (descending).")

    elif choice == "8":
        combined = list(zip(product_names, product_prices, product_qty))
        combined.sort()

        product_names = [x[0] for x in combined]
        product_prices = [x[1] for x in combined]
        product_qty = [x[2] for x in combined]

        print("Products sorted by name.")

    elif choice == "9":
        highest = max(product_prices)
        lowest = min(product_prices)

        high_index = product_prices.index(highest)
        low_index = product_prices.index(lowest)

        print("\nCostliest Product:", product_names[high_index],
              "Price:", highest)
        print("Cheapest Product:", product_names[low_index],
              "Price:", lowest)

    elif choice == "10":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Enter a number between 1 and 10.")