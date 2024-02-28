"""
币种配置
"""


class CoinPriceLimit:

    def __init__(self, coin, price, min_limit, max_limit) -> None:
        self.coin = coin
        self.price = price
        self.min_limit = min_limit
        self.max_limit = max_limit

    def __str__(self) -> str:
        return f'coin: {self.coin}, price: {self.price}, min_limit: {self.min_limit}, max_limit: {self.max_limit} \n'

    def __repr__(self) -> str:
        return self.__str__()
