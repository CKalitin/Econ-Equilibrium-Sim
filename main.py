import math

class agent():
    def __init__(self, capital, market_goods):
        self.capital = capital
        self.market_goods = market_goods

    def decision(self):
        # Decide how much capital to allocation to each market_good for this tick
        
        willingness_to_buy = {}
        
        # Get willingness to buy for each good
        for good_name in self.market_goods:
            market_function = market_functions[good_name] # Get the market function for this good
            willingness_to_buy[good_name] = market_function.__get_consumer_willingness_to_buy__(self.capital, market_goods[good_name].price)
        
        # Get relative willingness' to buy
        relative_willingness_to_buy = {}
        total_willingness_to_buy = 0
        for good_name in willingness_to_buy: total_willingness_to_buy += willingness_to_buy[good_name] # Get total willingness to buy
        for good_name in willingness_to_buy: relative_willingness_to_buy[good_name] = willingness_to_buy[good_name] / total_willingness_to_buy # Compute relative willingess' to buy
        
        # Allocate capital to each good
        # For now, the agent spends all available money on all the goods, because quantity purchased is discrete some money will be left over (round down) and if none of the good is available, no money spent
        for good_name in self.market_goods:
            quantity = math.floor(self.capital * relative_willingness_to_buy[good_name] / market_goods[good_name].price)
            self.capital -= market_goods[good_name].buy_good(quantity)

# This is a class that describes the market for a single good, eg. bread
# The market and good itself are integrated into one class
class market_good():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def buy_good(self, quantity):
        bought_quantity = min(quantity, self.quantity)
        self.quantity -= bought_quantity
        return self.price * bought_quantity

class market_function():
    def __init__(self, income_coeffs):
        # This is a polynomials ax^2 + bx + c, the array goes [a, b, c]
        self.income_coeffs = income_coeffs
    
    def __get_consumer_willingness_to_buy__(self, income, price):
        # Calculate the polynomial & set cutoff at 0 with max(0, f(x))
        return max(0, self.income_coeffs[0] ** income + self.income_coeffs[1] * income + self.income_coeffs[2] - price)


market_goods = {}
market_goods["food"] = market_good("food", 1, 100)

market_functions = {}
market_functions["food"] = market_function([1, 1, 2])

citizen_agents = []
citizen_agents.append(agent(50, ["food"]))

print(market_goods["food"].quantity)

citizen_agents[0].decision()

print(market_goods["food"].quantity)
