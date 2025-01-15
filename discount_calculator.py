def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# Main program to interact with the user
def main():
    try:
        # Get user inputs
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)

        # Display the result
        if discount_percent >= 20:
            print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: {price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values for the price and discount percentage.")

# Run the program
if __name__ == "__main__":
    main()