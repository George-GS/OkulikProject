def calculate_discount(price, discount_percent):
    """Возвращает цену со скидкой"""
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть от 0 до 100")

    final_price = price * (100 - discount_percent) / 100
    return round(final_price, 2)