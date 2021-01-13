from creatures import fish, birds, amphibians, mammals, reptiles

while True:
    choice = globals()[input("Type 'fish' or 'birds' or 'amphibians' or 'mammals' or 'reptiles': ")]
    print('\n')
    print(choice.characteristics())
    print('\n')
    print(choice.examples())
    print('\n')