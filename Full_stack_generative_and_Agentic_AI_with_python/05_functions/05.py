def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100,200,150]

for price in orders:
    amt = add_vat(price, 10)
    print(amt)

