import math

class agent_citizen():
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

class agent_firm():
    def __init__(self, capital, market_goods):
        self.capital = capital
        self.market_goods = market_goods
        self.market_goods_production = {}
        for good in self.market_goods:
            self.market_goods_production[good] = 0
        
    # Decide how much to produce
    def decision(self):
        for good in self.market_goods:
            if (market_goods[good].quantity_demanded - market_goods[good].quantity > 0): self.market_goods_production[good] += 1
            elif (market_goods[good].quantity_demanded - market_goods[good].quantity < 0): self.market_goods_production[good] -= 1
    
    def produce(self):
        for good in self.market_goods:
            market_goods[good].quantity += self.market_goods_production[good]
                

# This is a class that describes the market for a single good, eg. bread
# The market and good itself are integrated into one class
class market_good():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        self.quantity_demanded = 0 # This is the total quantity demanded by the market
        self.unmet_demand = 0 # This is the total demand that was not met by the market
    
    def buy_good(self, quantity):
        bought_quantity = min(quantity, self.quantity)
        self.quantity -= bought_quantity
        self.quantity_demanded += quantity
        if (bought_quantity < quantity): self.unmet_demand += quantity - bought_quantity
        return self.price * bought_quantity
    
    # Ran after a market tick
    def tick_post(self):
        self.quantity_demanded = 0
        self.unmet_demand = 0

class market_function():
    def __init__(self, income_coeffs):
        # This is a polynomials ax^2 + bx + c, the array goes [a, b, c]
        self.income_coeffs = income_coeffs
    
    def __get_consumer_willingness_to_buy__(self, income, price):
        # Calculate the polynomial & set cutoff at 0 with max(0, f(x))
        return max(0, self.income_coeffs[0] ** income + self.income_coeffs[1] * income + self.income_coeffs[2] - price)


market_goods = {}
market_goods["food"] = market_good("food", 1, 0)

market_functions = {}
market_functions["food"] = market_function([1, 1, 2])

agent_citizens = []
agent_citizens.append(agent_citizen(5, ["food"]))

agent_firms = []
agent_firms.append(agent_firm(50, ["food"]))

file = open("output.csv", "w")

file.write("Citizen Capital, Food Quantity Demanded, Food Quantity, Food Unmet Demand, Firm Food Production\n")

for i in range(50):
    agent_firms[0].produce()
    agent_citizens[0].decision()
    
    citizen_capital = agent_citizens[0].capital
    food_quantity_demanded = market_goods["food"].quantity_demanded
    food_quantity = market_goods["food"].quantity
    food_unmet_demand = market_goods["food"].unmet_demand
    firm_food_production = agent_firms[0].market_goods_production["food"]
    
    print("Citizen Capital: " + str(citizen_capital))
    print("Food quantity demanded: " + str(food_quantity_demanded))
    print("Food quantity: " + str(food_quantity))
    print("Food Unmet Demand: " + str(food_unmet_demand))
    print("Firm Food Production: " + str(firm_food_production))
    
    file.write(f"{citizen_capital}, {food_quantity_demanded}, {food_quantity}, {food_unmet_demand}, {firm_food_production}\n")
    
    agent_firms[0].decision()
    
    agent_citizens[0].capital += 5
    
    market_goods["food"].tick_post()
    
    print("")

file.close()