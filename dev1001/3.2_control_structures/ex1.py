# Has a variable item_price.
item_price = 50
# Has a variable customer_has_coupon (set to True or False).
customer_has_coupon = False
# If customer_has_coupon is True, apply a 10% discount to item_price to get final_price.
if customer_has_coupon == True:
    final_price = item_price * 0.9
# Else, final_price is the same as item_price.
else:
    final_price = item_price
# Print the final_price.
print(f"Price: ${final_price:.2f}")
# Test with customer_has_coupon being both True and False."
