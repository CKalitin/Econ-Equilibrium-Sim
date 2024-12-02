import goods

# Citizen agents have capital, allocated goods, and stockpile consumed goods
class agent_citizen():
    def __init__(self, capital):
        self.capital = capital
        self.allocated_goods = {}
        self.consumed_goods_quantities = {}
        
        for key in goods.good_marginal_value_functions:
            self.consumed_goods_quantities[key] = 0
    
    # Iterate over every consumed good and return the good purchase that returns the highest marginal value (Highest instantaneous slope)
    def get_highest_marginal_value_purchase(self):
        marginal_values = {}
        for key, value in goods.good_marginal_value_functions.items():
            marginal_values[key] = value.get_marginal_value(self.consumed_goods_quantities[key])
        print(marginal_values)
        return max(marginal_values, key=marginal_values.get) # Copilot!
            
agent = agent_citizen(100)

print(agent.consumed_goods_quantities)
print(agent.get_highest_marginal_value_purchase())

agent.consumed_goods_quantities["food"] = 5

print(agent.consumed_goods_quantities)
print(agent.get_highest_marginal_value_purchase())