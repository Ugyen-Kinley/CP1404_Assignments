def main():
    the_number_of_items = int(input("Number of items: "))
    while the_number_of_items < 0:
        print("Invalid number of items!")
        the_number_of_items = int(input("Number of items: "))

    the_total_price = 0

    for i in range(the_number_of_items):
        price = float(input(f"Price of item: "))
        the_total_price += price

    if the_total_price > 100:
        discount = the_total_price * 0.10
        the_total_price -= discount

    print(f"Total price for {the_number_of_items} items is ${the_total_price:.2f}")


if __name__ == "__main__":
    main()
