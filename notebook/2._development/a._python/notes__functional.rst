.. _2rZhcv48HZ:

=======================================
Functional Programming
=======================================

Functional programming decomposes a problem into a set of functions. Ideally,
functions only take inputs and produce outputs, and don’t have any internal
state that affects the output produced for a given input.

Python functions are first class objects of type callable.

Strategy Pattern
=======================================

If you're not too attached to using classes and you don't store state then
functions provde a great way to achieve the same results as the strategy
pattern.

.. code-block:: python

    TradingStrategyFunction = Callable[[list[int]], bool]   # function signature

    def should_buy_avg(prices: list[int], window_size: int) -> bool:
        # business logic

    def should_sell_minmax(prices: list[int], max_price: int) -> bool:
        # business logic

    class Exchange:

        def __init__(self) -> None:
            self.connected = False

        def connect(self) -> None:
            self.connected = True

        def get_market_data(self, symbol: str) -> list[int]:
            # business logic

        def buy(self, symbol: str, amount: int) -> None:
            # business logic

        def sell(self, symbol: str, amount: int) -> None
            # business logic

    @dataclass
    class TradingBot:

        exchange: Exchange
        buy_strategy: TradingStrategyFunction
        sell_strategy: TradingStrategyFunction

        def run(self, symbol: str) -> None:
            prices = self.exchange.get_market_data(symbol)
            should_buy = self.buy_strategy(prices)
            should_sell = self.sell_strategy(prices)

            # business logic

    def main() -> None:
        exchange = Exchange()
        exchange.connect()

        buy_strategy = functools.partial(should_buy_avg, window_size=4)
        sell_strategy = functools.partial(should_sell_minmax, max_price=35_000_00)

        bot = TradingBot(exchange, buy_strategy, sell_strategy)

        bot.run(symbol)


References
=======================================

#. `Functional Programming <https://en.wikipedia.org/wiki/Functional_programming>`_
#. `Functools Library <https://docs.python.org/3/library/functools.html>`_
#. `Functional Programming HOWTO <https://docs.python.org/3/howto/functional.html>`_
#. `You Can Do Really Cool Things With Functions In Python <https://youtu.be/ph2HjBQuI8Y>`_
