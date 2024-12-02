import agents
import goods
import markets

class simulation():
    def __init__(self):
        self.agents = []
        
    def tick(self):
        for agent in self.agents:
            agent.consume_goods()
            
            
agent_citizen = agents.agent_citizen(100)
agent_firm = agents.agent_firm(100)
agent_firm.append_sell_order("food", 10, 1)

agent_citizen.buy_highest_marginal_value_good()

print(agent_citizen.capital)
print(agent_citizen.consumed_goods_quantities)
print(agent_firm.capital)