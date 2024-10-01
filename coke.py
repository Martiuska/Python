def main():
    amount_due = 50  # Total amount to be paid

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")  # Capitalize 'Due'

        # Ask the user to insert a coin
        try:
            coin = int(input("Insert a coin (5, 10, or 25 cents): "))
        except ValueError:
            # If the user enters something that is not an integer
            print("Invalid input. Please insert a valid coin.")
            continue

        # Check if the inserted coin is valid
        if coin in [25, 10, 5]:
            amount_due -= coin  # Subtract the coin from the amount due
        else:
            print("Invalid coin. Only 25, 10, or 5 cents accepted.")

    # Calculate the change if necessary
    if amount_due < 0:
        print(f"Change Owed: {abs(amount_due)}")  # Capitalize 'Owed'
    else:
        print("Change Owed: 0")  # Handle exact payment

if __name__ == "__main__":
    main()
