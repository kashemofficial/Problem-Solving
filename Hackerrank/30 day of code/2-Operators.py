class Operators:
    def __init__(self,meal_cost,tip_percent,tax_percent):
        self.meal_cost = meal_cost
        self.tip_percent = tip_percent
        self.tax_percent = tip_percent
        tip = (meal_cost * tip_percent)/100
        tax = (meal_cost * tax_percent)/100
        total_cost = (meal_cost+tip+tax)
        print(round(total_cost))
if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    Operators(meal_cost,tip_percent,tax_percent)





