
## 2024 Nov 30
I need to plan way more and actually do this the way it's taught in economics.
Firms have to have fixed & variable costs that are described by some speed of sale/purchase variable - something like this, really these costs are just goods in a market and the delays should be build into that market, eg. transaction time.
I need to consider from first principles everything that each agent type needs, then look for common denominators.

Eg. Consumers need jobs (these are in a market but are not consumed, only allocated), goods (consumed from a market), and a good mechanism for allocating capital that takes into account saving money as well. 

Consumers need a better purchase function. MARGINAL VALUE!!!! Each consumer has a marginal value function that describes each good, this determines how much they want. 

A more accurate market sim would be fully continuous, not buying as much of everything as possible on every single tick. Consumption! Stockpiling? This also feeds into the marginal value function!

So what do we have? Consumers: Stored quantity of goods, marginal value function, job (allocated good). Maybe they also need an activation energy for changing jobs, how can this be done? This ends up with an education variable or something. Skills variable!

Firms: Fixed & Variable costs are combined into one. These are allocated goods with transaction delays. There also need to be production costs, this ties into stockpiling.

How do I use the price system? I don't have precise supply and demand functions to find equilbriums beforehand - by design.

Why would a firm want to produce more? If marginal cost is less than marginal revenue. What determines marginal cost? Both fixed and variable costs. How do I quantify this?

Does the market converge on maximum revenue? Copilot says it converges to maximum profit. How does a firm know how to maximize profit? It doesn't know its own marginal cost. 

The price line moves as a company changes price and quantity, so the size of the profit triangle changes. Also, we know nothing about the profit rectangle.

Maybe we just look at average cost and price to see if making more is profitable? This converges on zero profit? Well this is what we learn in econ, might be a good heuristic.

So why does profit exist? First, from first principles each production step has to be positive sum, so net gains are made. Maybe there's an added margin on top of just raw cost of production so that a firm accumulates capital. Profit margin, we're learning from first principles here! 

I'm starting to appreciate why Neoclassical economics is actually so important. This is the foundation of all the qualitative statements we make later.

So firms try to maximize profit, how do I implement this? I still have no way of changing the price of a good.

The producers change price themselves to maximize their own profit. This is done to sell the maximum number of goods. This is inherently exploratory behaviour because the firms don't make any predictions themselves. 

Maybe if they aren't selling all their units, they lower their price slightly. This happens gradually over many ticks. And if they're selling out, they produce more. In a large enough system with many firms and consumers, this might work.

Because of stockpiles, firms can lower price and production when they aren't selling out and increase price and production when they are. There needs to be a dominant variable here so that quantity does in fact change and both variables don't cancel out each other. Changing production takes longer than changing price, so price can be tried first in lower changes.

How do I write all this?
Firms:
Allocated Goods, Consumed Goods, Produced Goods.
Produced goods have a set price and quantity and production rate that is based on the consumed and allocated goods.
The price function for the goods is dependent on if they are selling at the same rate of production. Asymptotic changes to price so that it reaches an equilbrium.
Production function is dependent on profit? If positive make more?

There could be an issue with production in that purchasing more allocated costs results in lower short term profit (eg. buying a factory "real estate unit"). If the production function output is high enough to justify the cost, then the firm does it. Activation energy. This is dependent on the added production capacity of the allocated good and the current cost.

Taxes will be interesting to add. Do they actually contribute value or burn capital? Now we're getting past Neocalssical economics.

Consumers:
Allocated Goods, Consumed Goods, Stored Goods.
Allocated goods like jobs need some way to allocate them, education variable? Consumers also need to multiply, maybe this can be done through consumer surplus somehow.
The marginal value function is the important thing. I suppose these functions are unique for every product and I just plot them out in Desmos. Every tick, the consumer takes the action that produces the highest marginal value. The input is the quantity that the consumer already has? 

Does marginal value decrease as you get to better products? The marginal value of a water bottle in the desert seems far higher than a private jet when you're rich. I suppose this is true, so the marginal value of your first private jet has to be lower than the marginal value of all the things you bought before that (not taking into account the activation energy of the price of a jet). 

Will I make population growth inversely proportional to consumer surplus? This is accurate but wtf? I suppose it'll result in interesting equilibria, dark ages. Firms will also need shutdown conditions. People die when they don't work. 