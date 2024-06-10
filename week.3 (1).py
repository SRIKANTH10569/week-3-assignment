from collections import deque
class StockTransaction:
    def __init__(self):
        self.purchases = deque()

    def buy(self, shares, price):
        self.purchases.append((shares, price))

    def sell(self, shares, price):
        total_gain = 0
        while shares > 0 and self.purchases:
            old_shares, old_price = self.purchases.popleft()
            if old_shares <= shares:
                gain = (price - old_price) * old_shares
                total_gain += gain
                shares -= old_shares
            else:
                gain = (price - old_price) * shares
                total_gain += gain
                self.purchases.appendleft((old_shares - shares, old_price))
                shares = 0
        return total_gain

def calculate_capital_gain(transactions):
    stock = StockTransaction()
    total_gain = 0
    
    for transaction in transactions:
        action, rest = transaction.split(' ', 1)
        shares, rest = rest.split(' share(s) at $')
        shares = int(shares)
        price = int(rest.split(' each')[0])
        
        if action == 'buy':
            stock.buy(shares, price)
        elif action == 'sell':
            total_gain += stock.sell(shares, price)

    return total_gain

# Sample input sequence
transactions = [
    "buy 100 share(s) at $20 each",
    "buy 20 share(s) at $24 each",
    "buy 200 share(s) at $36 each",
    "sell 150 share(s) at $30 each"
]

total_gain = calculate_capital_gain(transactions)
print(f"Total capital gain (or loss): ${total_gain}")