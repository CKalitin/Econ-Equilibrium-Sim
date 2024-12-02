import goods

class market():
    def __init__(self, good_name, is_allocated_good=False):
        self.good_name = good_name
        self.is_allocated_good = is_allocated_good
        self.sell_orders = {} # Sell orders are stored as a dictionary (agent, sell_order class)
    
    def append_sell_order(self, agent_producer, quantity, price):
        if agent_producer in self.sell_orders:
            self.sell_orders.quantity += quantity
            self.sell_orders.price = price
        else: self.sell_orders[agent_producer] = sell_order(agent_producer, quantity, price)
    
    # TODO I will have to check if quantity is available
    def get_lowest_price_sell_order(self):
        return min(self.sell_orders, key=lambda x: self.sell_orders[x].price)
    
    def get_highest_price_sell_order(self):
        return max(self.sell_orders, key=lambda x: self.sell_orders[x].price)
    
    def exercise_buy_order_consumed(self, agent_producer, agent_consumer, quantity):
        if self.is_allocated_good:
            self.exercise_buy_order_allocated(agent_producer, agent_consumer)
            return
        
        quantity = min(quantity, self.sell_orders[agent_producer].quantity) # Don't allow negative quantities
        quantity = min(quantity, agent_consumer.capital // self.sell_orders[agent_producer].price) # Don't allow buying more than you can afford, double slash (//) does floor division
        
        self.sell_orders[agent_producer].quantity -= quantity
        agent_producer.capital += self.sell_orders[agent_producer].price * quantity
        agent_consumer.consumed_goods_quantities[self.good_name] += quantity
        agent_consumer.capital -= self.sell_orders[agent_producer].price * quantity
        
    def exercise_buy_order_allocated(self, agent_producer, agent_consumer):
        self.sell_orders[agent_producer].quantity -= 1
        good = goods.good_allocated(self.good_name, self.sell_orders[agent_producer].price, agent_producer, agent_consumer) # Create new allocated good
        agent_consumer.allocated_goods.append(good)
        agent_producer.allocated_goods.append(good)

 
class sell_order():
    def __init__(self, agent, quantity, price, good_name=""):
        self.agent = agent
        self.quantity = quantity
        self.price = price


markets = {}
for good_name in goods.goods_consumed:
    markets[good_name] = market(good_name)
for good_name in goods.goods_allocated:
    markets[good_name] = market(good_name, True)