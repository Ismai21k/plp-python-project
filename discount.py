def calculate_discount(price, discount_percent):
    
    discount = price * discount_percent/100

    if discount_percent >= 20:
        return price - discount

    return price

price = float(input("Enter the goods price :"))
discount_percent = float(input("Enter the discount percentage :"))

final_price = calculate_discount(price, discount_percent)

print("Final Price :", final_price)

