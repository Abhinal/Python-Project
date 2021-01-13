# from art import logo
# print(logo)

def Add(a, b):
  return a + b

def Subtract(a, b):
  return a - b

def Multiply(a, b):
  return a * b

def Divide(a, b):
  return a / b


operations = {
  '+' : Add,
  '-' : Subtract,
  '*' : Multiply,
  '/' : Divide
}

a = int(input('What is the first number?: '))
for symbol in operations:
  print(symbol)
operation_symbol = input('Pick an operation from the line above: ')
b = int(input('What is the  second number?: '))

calculation_function = operations[operation_symbol]
result = calculation_function(a, b)

print(f"{a} {operation_symbol} {b} = {result}")

for symbol in operations:
  print(symbol)
operation_symbol = input('Pick an operation from the line above: ')
c = int(input('What is the  second number?: '))

calculation_function = operations[operation_symbol]
result2 = calculation_function(result, c)

print(f"{result} {operation_symbol} {c} = {result2}")