def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    try:
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            return price
    except(ValueError, TypeError):
        print("Максимальная скидка не больше 20!!!")
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
if __name__ == "__discounted__":
    print(discounted(10000, 4000))