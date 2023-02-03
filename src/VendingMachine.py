def purchase():
    product = int(input("Enter your selection (0-5): "))
    balance = 0
    if product == 1:
        balance = 0.36
    elif product == 2:
        balance = 0.45
    elif product == 3:
        balance = 0.55
    elif product == 4:
        balance = 1.25
    elif product == 5:
        balance = 1.50
    return product, balance

def payment():
    return float(input("Enter your payment amount: "))

def getProduct():
    inventory = 5
    def display():
        nonlocal inventory
        inventory -= 1
        print("Product dispensed. Thank you for your purchase!")
    return display, inventory

def change():
    return float(input("Enter change amount: "))

def main():
    print("HELLO Customer!")
    product_obj, inventory = getProduct()
    balance = 0
    while inventory != 0:
        print("0. Get money back")
        print("1. Kitkat\t$.36")
        print("2. Mars\t\t$.45")
        print("3. Reese\t$.55")
        print("4. Twix\t\t$1.25")
        print("5. Snicker\t$1.50")
        product, balance = purchase()
        if product == 0:
            return
        pay_bal = payment()
        rem = balance - pay_bal
        while rem > 0:
            if rem >= 1:
                print("You are missing $" + str(rem))
                pay_bal = pay_bal + payment()
                rem = balance - pay_bal
        if pay_bal > balance:
            print("Your change is: $" + str(pay_bal - balance))
        product_obj()
        inventory -= 1

if __name__ == "__main__":
    main()
