class GetProduct:
    kitkat = 5
    mars = 5
    reeses = 5
    twix = 5
    snickers = 5
    inventory = kitkat + mars + reeses + twix + snickers

    @staticmethod
    def display():
        prod = Purchase()
        if prod.product == 1:
            print("Here is your Kitkat, please come back!")
            GetProduct.kitkat -= 1
        elif prod.product == 2:
            print("Here is your Mars bar, please come back!")
            GetProduct.mars -= 1
        elif prod.product == 3:
            print("Here is your Reese's cup, please come back!")
            GetProduct.reeses -= 1
        elif prod.product == 4:
            print("Here is your Twix bar, please come back!")
            GetProduct.twix -= 1
        elif prod.product == 5:
            print("Here is your Snickers bar, please come back!")
            GetProduct.snickers -= 1
