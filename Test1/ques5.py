from prettytable import PrettyTable

x = PrettyTable()
salespeople = [
    'Abhinav','Ishaan','Anamika','Ishtuti'
]

products = [
    'product_1', 'product_2', 'product_3', 'product_4', 'product_5'
]

dct = {}
for people in salespeople:
    dct[people] = {}
    for product in products:
        dct[people][product] = 5 ## Dummy data for all


for people in salespeople:
    for product in products:
        dct[people][product] += int(input(f"Hi {people}! How many {product} have you sold this month: "))



x.field_names = ["Sales Person", "Product", "Quantity"]
for people in salespeople:
    product_count = 0
    for product in products:
        x.add_row([people, product, dct[people][product]])
        product_count += dct[people][product]
    x.add_row(['', 'Total', product_count])
    x.add_row(['', '', ''])


print(x)