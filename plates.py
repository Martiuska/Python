def is_valid(plate):
    # Check if the length is between 2 and 6 characters
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Check if the first two characters are letters
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    # Ensure the plate contains only letters and numbers (no special characters)
    if not plate.isalnum():
        return False

    # Numbers, if present, must be at the end and cannot start with '0'
    for i in range(len(plate)):
        if plate[i].isdigit():
            if plate[i] == '0':  # First number can't be '0'
                return False
            if not plate[i:].isdigit():  # Numbers must be at the end
                return False
            break

    return True


def main():
    plate = input("Enter a vanity plate: ").upper()  # Convert input to uppercase
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
