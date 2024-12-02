import agents

class simulation():
    def __init__(self):
        self.agents = []
        
    def tick(self):
        for agent in self.agents:
            agent.consume_goods()
            
agent_citizen = agents.agent_citizen(100)
agent_firm = agents.agent_firm(100)
agent_firm.append_sell_order("job", 1, 1)

agent_citizen.buy_good("job", 1)

for allocated_good in agent_citizen.allocated_goods:
    print(allocated_good.name)