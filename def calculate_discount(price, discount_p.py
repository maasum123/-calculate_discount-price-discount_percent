def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): Original price.
        discount_percent (float): Discount percentage (between 0 and 100).

    Returns:
        float: Final price after applying the discount.
    """
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage (e.g., 20 for 20%): "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price != original_price:
    print(f"Final price after applying {discount_percentage}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")
