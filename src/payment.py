class Payment:
    def __init__(self):
        self.coins = 0
        self.bills = 0
        self.total = 0
        self.options = 0

    def payment(self):
        print("\nPlease select the payment method.")
        while True:
            print("0. Stop Entering Money")
            print("1. Enter coins")
            print("2. Enter bills")
            self.options = int(input())

            if self.options == 0:
                break
            elif self.options == 1:
                print("Enter coins")
                while True:
                    self.coins = int(input())
                    if self.coins == 0:
                        break
                    elif self.coins in [1, 5, 10, 25]:
                        self.total += self.coins
                    else:
                        print("Invalid Coins, Please enter new coins")
            elif self.options == 2:
                print("Enter bills")
                while True:
                    self.bills = int(input())
                    if self.bills == 0:
                        break
                    elif self.bills in [1, 5]:
                        self.total += self.bills * 100
                    else:
                        print("Invalid Bills, Please enter new bills")
            else:
                print("Invalid Options")

        return self.total

