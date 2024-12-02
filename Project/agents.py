import goods
import markets

# Citizen agents have capital, allocated goods, and stockpile consumed goods
class agent_citizen():
    def __init__(self, capital):
        self.capital = capital
        self.allocated_goods = {}
        self.consumed_goods_quantities = {}
        
        for key in goods.goods_consumed:
            self.consumed_goods_quantities[key] = 0
    
    # Run every tick
    def consume_goods(self):
        for key, value in goods.goods_consumed.items():
            self.consumed_goods_quantities[key] -= value.consumption_per_tick
    
    # Run every tick
    def buy_highest_marginal_value_good(self):
        good_name = self.get_highest_marginal_value_purchase()
        print(good_name)
        self.buy_good(good_name, 1)
    
    def buy_good(self, good_name, quantity):
        lowest_price_sell_order = markets.markets[good_name].get_lowest_price_sell_order()
        markets.markets[good_name].exercise_buy_order(lowest_price_sell_order, self, quantity)
    
    # Return name of highest marginal value good (Greatest instantaneous slope)
    def get_highest_marginal_value_purchase(self):
        marginal_values = {}
        for key, value in goods.good_marginal_value_functions.items():
            marginal_values[key] = value.get_marginal_value(self.consumed_goods_quantities[key])
        print(marginal_values)
        return max(marginal_values, key=marginal_values.get) # Copilot!
    
            