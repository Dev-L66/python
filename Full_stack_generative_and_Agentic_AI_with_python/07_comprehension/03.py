prices_sar = {
    "Pencil": 50,
    "Pen": 40,
    "Colors": 500
}


prices_usd = {tea:price/80 for tea, price in prices_sar.items()}


print(prices_usd)