import random
MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.175  # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0
OUTPUT_FILE = 'output.txt'
price = INITIAL_PRICE

print("${:,.2f}".format(price))
out_file = open(OUTPUT_FILE, 'w')
day_counter = 0

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day_counter, price), file=out_file)

day_counter = 0

out_file.close()
