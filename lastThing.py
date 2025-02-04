menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":6.00}
menu2 = {"fries":2.50,
         "chips":1.00,
         "pretzel":3.50}

def concession(menu):
    cart= []
    total = 0

    print("-------menu-------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("------------------")
    while True:
        food = input("select an item (q to quit): ").lower()
        if food == "q":
            break
        elif menu.get(food) is not None:
            cart.append(food)
    for food in cart:
        total += menu.get(food)
        print(food,end=" ")
    print(cart)
    print(f"total is: ${total:.2f}")


concession(menu)
concession(menu2)



# cart = []
# total = 0

# print("-------menu-------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("------------------")

# while True:
#     food = input("select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)


# for food in cart:
#     total += menu.get(food)
#     print(food,end=" ")



# print(cart)
# print(f"total is: ${total:.2f}")










