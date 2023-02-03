class Purchase:
    balance = 0
    product = 0

    def purchase(self):
        print("Please select your product.")
        self.product = int(input().strip())

        if self.product == 0:
            self.balance += 0
            return self.balance
        elif self.product == 1:
            self.balance += 36
        elif self.product == 2:
            self.balance += 45
        elif self.product == 3:
            self.balance += 55
        elif self.product == 4:
            self.balance += 125
        elif self.product == 5:
            self.balance += 150
        else:
            print("Invalid Products")

        return self.balance
