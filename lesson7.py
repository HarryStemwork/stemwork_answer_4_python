store = "Harry Shopping Mall"
product = ["TV", "frigde", "fan", "cooler", "computer"] #create 5 products you will see in a shopping mall, remember to use string for all
cart = []
print(store)
print(product, '\n')
while True:
  msg = input("Please enter what you want to buy (q=Quit) : ")
  if msg == 'q' or msg == 'Q':
    break
  else:
    if msg in product:
      cart.append(msg)
print("You have bought :", cart)
