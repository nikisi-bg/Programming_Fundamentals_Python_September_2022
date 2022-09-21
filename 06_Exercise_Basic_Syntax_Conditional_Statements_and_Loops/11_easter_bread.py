budget = float(input())
price_one_kg_flour = float(input())
breads_counter = 0
colored_eggs_counter = 0

eggs_price = price_one_kg_flour * 0.75
milk_price = price_one_kg_flour * 1.25 / 4
one_bread_price = eggs_price + price_one_kg_flour + milk_price

while budget >= one_bread_price:
    budget -= one_bread_price
    breads_counter += 1
    colored_eggs_counter += 3
    if breads_counter % 3 == 0:
         colored_eggs_counter -= breads_counter - 2

print(f"You made {breads_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
