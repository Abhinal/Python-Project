product_info = {}
product_data = ['Price_per_unit','Quantity']
bill_amount = 0
while(True):
    name = input("Enter Product Name (enter -99 to calculate bill): ")
    if(name == '-99'):
        break
    product_info[name] = {}
    for entry in product_data:
        product_info[name][entry] = input(entry+": ")
print('\n\n')
print('Product'.center(10,' '),'Quantity'.center(10,' '),'Rate'.center(10,' '),'Total'.center(10,' '))
for name in product_info:
    amount = int(product_info[name]['Quantity']) * int(product_info[name]['Price_per_unit'])
    print(name.center(10,' '),product_info[name]['Quantity'].center(10,' '),product_info[name]['Price_per_unit'].center(10,' '),str(amount).center(10,' '))
    bill_amount += amount
print('\nTotal bill:',bill_amount)