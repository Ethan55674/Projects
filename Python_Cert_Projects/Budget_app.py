# This program creates a budget tracker using a Category class.
# Each Category object stores transactions in a ledger and can handle deposits,
# withdrawals, transfers, balance calculations, and formatted output.
# The create_spend_chart function analyzes spending from multiple categories
# and creates a visual chart showing the percentage spent in each category.


class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
    def deposit(self,amount, desc = ""):
        self.ledger.append({'amount': amount, 'description': desc})
        
    def withdraw(self,amount, desc = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': desc})
            return True
        else:
            return False
    def get_balance(self):
        balance = 0
        for dictionary in self.ledger:
            balance +=  dictionary['amount']
        return balance
    def transfer(self, amount, class_name):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {class_name.name}")
            class_name.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False
    def check_funds(self,amount):
        if self.get_balance() < amount:
            return False
        else:
            return True
    def __str__(self):
        title = self.name.center(30, "*")
        total_ledger = ""
        for item in self.ledger:
            description = item['description'][:23]
            total_ledger += description.ljust(23," ")
            total_ledger += str("{:.2f}".format(item['amount'])).rjust(7," ") 
            total_ledger += "\n"
        return f"{title}\n{total_ledger}Total: {self.get_balance():.2f}"
    
    

def create_spend_chart(categories):
    chart = ""
    chart += "Percentage spent by category\n"
    category_total = []
    total_spent = 0
    for category in categories:
        cat_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                cat_spent += abs(item['amount'])
                total_spent += abs(int(item['amount']))
        category_total.append(cat_spent)
    percentages = []
    for item in category_total:
        item = int(item / total_spent * 100)
        item = item // 10 * 10
        percentages.append(item)
    
    for i in range(100,-10,-10):
        row = f"{i:3}|"
        for item in percentages:
            if item >= i:
                row += " o "
            else:
                row += "   "
        row += " "
        chart += row + "\n"
    test_length = ""
    max_length = 0
    
    max_length = max(len(category.name) for category in categories)
    hypens = "-" * (len(categories) * 3 + 1)
    chart += "    " + hypens + "\n"
    
    for i in range(max_length):
        row = " "
        for category in categories:
            if i < len(category.name):
                row += category.name[i] + "  "
            else:
                row += "   "
        chart += "    " + row + "\n"
    return chart.rstrip("\n")




class_1 = Category("Micah")
class_2 = Category("Ethan")
class_3 = Category("Viviana")
class_4 = Category("Stitch")
class_1.deposit(100)
class_2.deposit(100)

class_1.withdraw(65,"groceries")
class_2.withdraw(30,"restaurant and more food for dessert")


print(create_spend_chart([class_1,class_2,class_3,class_4]))
