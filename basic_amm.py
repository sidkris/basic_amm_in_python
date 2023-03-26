"""
a basic implementation of an Automated Market Maker (AMM) in Python using the Uniswap algorithm
"""

class AMM:
  
    def __init__(self, token_reserve, eth_reserve):
        self.token_reserve = token_reserve
        self.eth_reserve = eth_reserve

    def eth_to_token(self, eth_amount):
        token_amount = (eth_amount * self.token_reserve) / (self.eth_reserve + eth_amount)
        self.token_reserve += token_amount
        self.eth_reserve += eth_amount
        return token_amount

    def token_to_eth(self, token_amount):
        eth_amount = (token_amount * self.eth_reserve) / (self.token_reserve + token_amount)
        self.token_reserve += token_amount
        self.eth_reserve += eth_amount
        return eth_amount



amm = AMM(token_reserve=1000, eth_reserve=10)

# Convert 1 ETH to tokens
token_amount = amm.eth_to_token(1)
print("Received tokens:", token_amount)

# Convert 100 tokens to ETH
eth_amount = amm.token_to_eth(100)
print("Received ETH:", eth_amount)
