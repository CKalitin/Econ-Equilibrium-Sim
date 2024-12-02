import goods

class market():
    def __init__(self, good_name):
        self.good_name = good_name
        self.sell_orders = {} # Sell orders are stored as a dictionary of agent: [quantity, price]
    
    def append_sell_order(self, agent_producer, quantity, price):
        if agent_producer in self.sell_orders:
            self.sell_orders.quantity += quantity
            self.sell_orders.price = price
        else: self.sell_orders[agent_producer] = sell_order(agent_producer, quantity, price)
    
    def get_lowest_price_sell_order(self):
        return min(self.sell_orders, key=lambda x: self.sell_orders[x].price)
    
    def exercise_buy_order(self, agent_producer, agent_consumer, quantity):
        quantity = min(quantity, self.sell_orders[agent_producer].quantity) # Don't allow negative quantities
        self.sell_orders[agent_producer][0] -= quantity
        agent_producer.capital += self.sell_orders[agent_producer][1] * quantity
        agent_consumer.consumed_goods_quantities[self.good_name] += quantity

 
class sell_order():
    def __init__(self, agent, quantity, price):
        self.agent = agent
        self.quantity = quantity
        self.price = price


markets = {}
for good_name in goods.goods_consumed:
    markets[good_name] = market(good_name)