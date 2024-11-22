from decimal import Decimal
import math

def is_round_number(num):
    num = float(num)
    return num % 1 == 0

def is_multiple_of_decimal(num, divisor):
    num = Decimal(str(num))
    divisor = Decimal(str(divisor))
    return num % divisor == 0

def is_odd(num):
    return num % 2 != 0

def get_items_description_points(items):
    points = 0
    for item in items:
        trimmed_text = item["shortDescription"].strip()
        text_len = len(trimmed_text)
        if text_len % 3 == 0:
            points += math.ceil(float(item["price"]) * 0.2)
    return points