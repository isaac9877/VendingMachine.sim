class Change:
    change = 0

    @staticmethod
    def cal_coins(changes):
        change_string = ""
        quarters, rem_quarters = 0, 0
        dimes, rem_dimes = 0, 0
        nickels, rem_nickels = 0, 0
        pennies = 0

        quarters = changes // 25
        rem_quarters = changes % 25
        change_string += str(quarters) + " quarters\n"

        if rem_quarters != 0:
            dimes = rem_quarters // 10
            rem_dimes = rem_quarters % 10
            change_string += str(dimes) + " dimes\n"

        if rem_dimes != 0:
            nickels = rem_dimes // 5
            rem_nickels = rem_dimes % 5
            change_string += str(nickels) + " nickels\n"

        if rem_nickels != 0:
            pennies = rem_nickels
            change_string += str(pennies) + " pennies\n"

        return change_string

    @staticmethod
    def change():
        purchase_balance = Purchase()
        total = Payment().total
        change_display = ""
        if total > purchase_balance.balance:
            Change.change = total - purchase_balance.balance
            change_display = Change.cal_coins(Change.change)
        else:
            change_display = "Enter more money"
            Payment().payment()

        return change_display
