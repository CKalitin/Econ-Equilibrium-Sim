import agents
import goods
import markets

class simulation():
    def __init__(self):
        self.agents = []
        
    def tick(self):
        for agent in self.agents:
            agent.consume_goods()
            
            
agent = agents.agent_citizen(100)

print(agent.consumed_goods_quantities)
print(agent.get_highest_marginal_value_purchase())

agent.consumed_goods_quantities["food"] = 5

print(agent.consumed_goods_quantities)
print(agent.get_highest_marginal_value_purchase())
