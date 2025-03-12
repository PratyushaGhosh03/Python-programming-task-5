import random

class VirtualStockMarket:
    def __init__(self):
        self.stock_price = 100

    def update_price(self):
        change = random.uniform(-5, 5)
        self.stock_price += change
        return round(self.stock_price, 2)

# Example usage
market = VirtualStockMarket()
for _ in range(5):
    print(market.update_price())
