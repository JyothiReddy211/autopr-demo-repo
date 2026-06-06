def calculate_discount(price, percentage):
    discount = price * (percentage / 100)
    return round(price - discount, 2)