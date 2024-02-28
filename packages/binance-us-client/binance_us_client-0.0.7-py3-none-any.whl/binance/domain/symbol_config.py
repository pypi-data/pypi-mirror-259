"""
币对配置
"""


class Symbol:
    """
    币对配置，base_coin quote_coin 的价格及限额
    """

    def __init__(self, base_coin, base_coin_price, base_min_limit, base_max_limit,
                 quote_coin, quote_coin_price, quote_min_limit, quote_max_limit) -> None:
        self.base_coin = base_coin
        self.base_coin_price = base_coin_price
        self.base_min_limit = base_min_limit
        self.base_max_limit = base_max_limit
        self.quote_coin = quote_coin
        self.quote_coin_price = quote_coin_price
        self.quote_min_limit = quote_min_limit
        self.quote_max_limit = quote_max_limit
        self.symbol = f'{base_coin}{quote_coin}'

    def __str__(self) -> str:
        return f'symbol: {self.symbol}, base_coin: {self.base_coin}, base_coin_price: {self.base_coin_price}, base_min_limit: {self.base_min_limit}, base_max_limit: {self.base_max_limit}, quote_coin: {self.quote_coin}, quote_coin_price: {self.quote_coin_price}, quote_min_limit: {self.quote_min_limit}, quote_max_limit: {self.quote_max_limit} \n'

    def __repr__(self) -> str:
        return self.__str__()

    def get_reverse(self):
        """
        get a new reverse symbol of self
        """
        return Symbol(
            self.quote_coin,
            self.quote_coin_price,
            self.quote_min_limit,
            self.quote_max_limit,
            self.base_coin,
            self.base_coin_price,
            self.base_min_limit,
            self.base_max_limit
        )

    def reverse(self):
        """reverse self"""
        reverse = self.get_reverse()
        self.base_coin = reverse.base_coin
        self.base_coin_price = reverse.base_coin_price
        self.base_min_limit = reverse.base_min_limit
        self.base_max_limit = reverse.base_max_limit
        self.quote_coin = reverse.quote_coin
        self.quote_coin_price = reverse.quote_coin_price
        self.quote_min_limit = reverse.quote_min_limit
        self.quote_max_limit = reverse.quote_max_limit
        self.symbol = reverse.symbol
        return self

    def get_reverse_symbol(self):
        """
        get a reverse symbol
        """
        return self.quote_coin + self.base_coin
