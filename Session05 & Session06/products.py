product_names = []
product_is_bought = []
product_prices = []
for i in range(100):
  answer = input("help, add, display, edit, remove, search, buy, details, exit: ")
  if answer == "help":
    help_text = """
      Tasks:
      - add: Adds a new product.
      - remove: Removes a specified product.
      - edit: Edits a product.
      - search: Searches for a product.
      - display: Displays all products.
      - buy: Buys a product.
      - help: Displays this help text.
      - exit: Exits the program.
      """
    print(help_text)
  elif answer == "add":
    name = input("product name: ")
    if name not in product_names:
      product_names.append(name)
      product_is_bought.append(False)
      product_prices.append(None)
      print("added!")
    else:
      print(f"{name}:already exists!")
  elif answer == "display":
    if len(product_names) == 0:
      print("Empty!")
    for i, p in enumerate(product_names):
      bought = product_is_bought[i]
      price = product_prices[i]
      print(f"{i+1}){p} ==> bought: {bought}, price: {price}")
  elif answer == "remove":
    name = input("product name: ")
    if name in product_names:
      ind = product_names.index(name)
      product_names.pop(ind)
      product_is_bought.pop(ind)
      product_prices.pop(ind)
      print("removed!")
    else:
      print(f"{name}: not found!")
  elif answer == "edit":
    old_name = input("product name: ") # p1
    if old_name in product_names:
      new_name = input("new name: ") # p5
      if new_name not in product_names: # True
        ind = product_names.index(old_name) # 0
        product_names[ind] = new_name # 0 ====> p5
        new_price = int(input("new price: ")) # 100
        if product_prices[ind] != None:
          product_prices[ind] = new_price # 0 ===> 100
        else:
          print("Not purchased!")
        print("edited!")
      else:
        print(f"{new_name} : already exists!")
    else:
      print(f"{old_name}: not found!")
  elif answer == "search":
    name = input("product name: ")
    if name in product_names:
      ind = product_names.index(name)
      bought = product_is_bought[ind]
      price = product_prices[ind]
      print(f"{name} ==> bought: {bought}, price: {price}")
    else:
      print(f"{name} : not found!")
  elif answer == "details":
    total = len(product_names)
    not_purchased = product_is_bought.count(False)
    purchased = product_is_bought.count(True)
    print(f"total: {total}")
    print(f"purchased: {purchased}")
    print(f"not purchased: {not_purchased}")
    prices = []
    for i in product_prices:
      if i:
        prices.append(i)
    print(f"sum: {sum(prices)}")
  elif answer == "buy":
    name = input("product name: ")
    if name in product_names:
      price = int(input(f"price of {name}: "))
      # edit
      ind = product_names.index(name)
      product_prices[ind] = price
      product_is_bought[ind] = True
      print("bought!")
    else:
      print(f"{name}: not found!")
  elif answer == "":
    continue
  elif answer == "exit":
    break
  else:
    print(f"{answer}: command not found!")