# These goods are consumed by agents and bought and sold in the market
# They are not exchanged as instances, only quantitatively - eg. if you buy 5 food, your food quantity goes up by 5
class good_consumed():
    def __init__(self, consumption_per_tick):
        self.consumption_per_tick = consumption_per_tick


# Allocated goods are exchanged by reference, eg. if you buy a house, you get a house object
# Jobs use allocated goods, hence the owner agent and consumer agent variables, these are references to the owner and agent that are useful when buying and selling
class good_allocated():
    def __init__(self, name, price, agent_producer, agent_consumer):
        self.name = name
        self.price = price
        self.agent_producer = agent_producer
        self.agent_consumer = agent_consumer


class good_consumed_marginal_value_function():
    def __init__(self, income_coeffs):
        # This is a polynomials ax^2 + bx + c, the array goes [a, b, c]
        self.income_coeffs = income_coeffs
    
    def get_marginal_value(self, quantity):
        return self.income_coeffs[0] ** quantity + self.income_coeffs[1] * quantity + self.income_coeffs[2]
    

goods_consumed = {}
goods_consumed["food"] = good_consumed(5)
goods_consumed["house"] = good_consumed(0.2)

goods_allocated = {}
goods_allocated["job"] = good_allocated("job", 1, None, None) # For job allocated goods, price is salary per tick

good_marginal_value_functions = {}
good_marginal_value_functions["food"] = good_consumed_marginal_value_function([0, -0.5, 2])
good_marginal_value_functions["house"] = good_consumed_marginal_value_function([0, 1, 1])