product_names = []
product_prices = []
product_qty = []

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

    # ADD PRODUCT
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

    # DELETE PRODUCT
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

    # UPDATE PRICE
    elif choice == "3":
        name = input("Enter product name: ").strip()

        if name in product_names:
            index = product_names.index(name)

            new_price = float(input("Enter new price: "))
            product_prices[index] = new_price

            print("Price updated successfully.")
        else:
            print("Product not found.")

    # DISPLAY PRODUCTS
    elif choice == "4":
        if len(product_names) == 0:
            print("No products available.")
        else:
            print("\n{:<5} {:<20} {:<10} {:<10}".format(
                "No.", "Name", "Price", "Qty"))
            print("-" * 50)

            for i in range(len(product_names)):
                print("{:<5} {:<20} {:<10} {:<10}".format(
                    i + 1,
                    product_names[i],
                    product_prices[i],
                    product_qty[i]
                ))

    # SEARCH PRODUCT
    elif choice == "5":
        name = input("Enter product name to search: ").strip()

        if name in product_names:
            index = product_names.index(name)

            print("\nProduct Found")
            print("Name :", product_names[index])
            print("Price:", product_prices[index])
            print("Qty  :", product_qty[index])
        else:
            print("Product not found.")

    # SORT PRICE ASCENDING
    elif choice == "6":
        if len(product_names) == 0:
            print("No products to sort.")
        else:
            combined = list(zip(product_prices,
                                product_names,
                                product_qty))

            combined.sort()

            product_prices = [item[0] for item in combined]
            product_names = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]

            print("Products sorted by price (ascending).")

    # SORT PRICE DESCENDING
    elif choice == "7":
        if len(product_names) == 0:
            print("No products to sort.")
        else:
            combined = list(zip(product_prices,
                                product_names,
                                product_qty))

            combined.sort(reverse=True)

            product_prices = [item[0] for item in combined]
            product_names = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]

            print("Products sorted by price (descending).")

    # SORT BY NAME
    elif choice == "8":
        if len(product_names) == 0:
            print("No products to sort.")
        else:
            combined = list(zip(product_names,
                                product_prices,
                                product_qty))

            combined.sort()

            product_names = [item[0] for item in combined]
            product_prices = [item[1] for item in combined]
            product_qty = [item[2] for item in combined]

            print("Products sorted alphabetically.")

    # COSTLIEST / CHEAPEST
    elif choice == "9":
        if len(product_prices) == 0:
            print("No products available.")
        else:
            highest = max(product_prices)
            lowest = min(product_prices)

            costliest_index = product_prices.index(highest)
            cheapest_index = product_prices.index(lowest)

            print("\n------ PRICE SUMMARY ------")
            print(f"Costliest Product : {product_names[costliest_index]} "
                  f"(Price: {highest})")

            print(f"Cheapest Product  : {product_names[cheapest_index]} "
                  f"(Price: {lowest})")

    # EXIT
    elif choice == "10":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Enter a number between 1 and 10.")