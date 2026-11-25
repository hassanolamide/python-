def calculate_discount(price,discount):
    discount_amount =  (price * discount)/100
    final_price = price - discount_amount 
    return final_price

def calculate_tax(price,tax):
    discount_price = (price * tax)/ 100
    return discount_price