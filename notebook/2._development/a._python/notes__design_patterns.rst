.. _kTgPHYa7Mf:

=======================================
Design Patterns
=======================================

Creational
=======================================

* Abstract factory
* Builder
* Dependency injection
* Lazy initialization
* Multiton
* Object pool
* Prototype
* Resource acquisition is initialization (RAII)
* Singleton


Factory method
---------------------------------------

Factory Method is a creational design pattern used to create concrete
implementations of a common interface.

* Implement multiple classes with a common interface but different behaviors
* Object creation in a single factory for easy extension

.. code-block:: python

    # https://realpython.com/factory-method-python/

    class SpotifyService:
        def __init__(self, access_code):
            self._access_code = access_code

        def test_connection(self):
            print(f'Accessing Spotify with {self._access_code}')


    class SpotifyServiceBuilder:
        def __init__(self):
            self._instance = None

        def __call__(self, spotify_client_key, spotify_client_secret, **_ignored):
            if not self._instance:
                access_code = self.authorize(
                    spotify_client_key, spotify_client_secret)
                self._instance = SpotifyService(access_code)
            return self._instance

        def authorize(self, key, secret):
            return 'SPOTIFY_ACCESS_CODE'


    class PandoraService:
        pass


    class PandoraServiceBuilder:
        pass


    class ObjectFactory:
        def __init__(self):
            self._builders = {}

        def register_builder(self, key, builder):
            self._builders[key] = builder

        def create(self, key, **kwargs):
            builder = self._builders.get(key)
            if not builder:
                raise ValueError(key)
            return builder(**kwargs)

    factory = object_factory.ObjectFactory()
    factory.register_builder('SPOTIFY', SpotifyServiceBuilder())


    spotify = music.factory.create('SPOTIFY', **config)
    spotify.test_connection()


**Tutorials:**

* `The Factory Pattern in Python // Separate creation from use <https://youtu.be/s_4ZrtQs8Do>`_



Structural
=======================================

* Adapter, Wrapper, or Translator
* Bridge
* Composite
* Decorator
* Extension object
* Facade
* Flyweight
* Front controller
* Marker
* Module
* Proxy
* Twin


Behavioral
=======================================

* Blackboard
* Chain of responsibility
* Intepreter
* Interator
* Mediator
* Memento
* Null object
* Servant
* Specification
* State
* Template method
* Visitor


Command
---------------------------------------

The command pattern is used to encapsulate all information needed to perform an
action or trigger an event at a later time.

.. code-block:: python

    # https://github.com/ArjanCodes/2021-command-transactions
    # with_transaction

    @dataclass
    class BankController:
        ledger: list[Transaction] = field(default_factory=list)
        current: int = 0

        def register(self, transaction: Transaction) -> None:
            del self.ledger[self.current :]
            self.ledger.append(transaction)
            self.current += 1

        def undo(self) -> None:
            if self.current > 0:
                self.current -= 1

        def redo(self) -> None:
            if self.current < len(self.ledger):
                self.current += 1

        def compute_balances(self) -> None:
            for transaction in self.ledger[: self.current]:
                transaction.execute()

    @dataclass
    class Deposit:
        account: Account
        amount: int

        @property
        def transfer_details(self) -> str:
            return f"${self.amount/100:.2f} to account {self.account.name}"

        def execute(self) -> None:
            self.account.deposit(self.amount)
            print(f"Deposited {self.transfer_details}")


    bank = Bank()
    controller = BankController()

    account1 = bank.create_account("ArjanCodes")

    controller.register(Deposit(account1, 100000))
    controller.undo()
    controller.redo()


**Tutorials:**

* `Implementing Undo And Redo With The Command Design Pattern <https://youtu.be/FM71_a3txTo>`_
* `How To Make The Command Pattern More Flexible With One Simple Change <https://youtu.be/rGu33Tk0tCM>`_


Observer
---------------------------------------

aka Publisher/Subscriber

Allows multiple subscribers to register receive events from a single publisher.

Provides for loose coupling between publishers and subscribers.

.. code-block:: python

    # https://github.com/arjancodes/betterpython
    # 4 - Observer Pattern - api v2

    subscribers = dict()

    def subscribe(event_type: str, fn):
        if not event_type in subscribers:
            subscribers[event_type] = []
        subscribers[event_type].append(fn)

    def post_event(event_type: str, data):
        if not event_type in subscribers:
            return
        for fn in subscribers[event_type]:
            fn(data)

    def handle_user_registered_event(user):
        post_slack_message("sales",
            f"{user.name} has registered with email address {user.email}.
                Please spam this person incessantly.")

    def setup_slack_event_handlers():
        subscribe("user_registered", handle_user_registered_event)
        subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)

    def register_new_user(name: str, password: str, email: str):
        user = create_user(name, password, email)
        post_event("user_registered", user)


    setup_slack_event_handlers()
    register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")


**Docs:**

* `Django Signals <https://docs.djangoproject.com/en/4.0/topics/signals/>`_

**Tutorials:**

* `Observer Pattern Tutorial: I NEVER knew events were THIS powerful <https://youtu.be/oNalXg67XEE>`_


Strategy
---------------------------------------

A behavioral software design pattern that enables selecting an algorithm at
runtime. Instead of implementing a single algorithm directly, code receives
run-time instructions as to which in a family of algorithms to use.

:ref:`You can use functions in Python <UiQKzwRTeu>` in place of classes if the strategy doesn't
store state.

.. code-block:: python

    # https://www.geeksforgeeks.org/strategy-method-python-design-patterns/

    class Item:

        """Constructor function with price and discount"""

        def __init__(self, price, discount_strategy = None):

            """take price and discount strategy"""

            self.price = price
            self.discount_strategy = discount_strategy

        """A separate function for price after discount"""

        def price_after_discount(self):

            if self.discount_strategy:
                discount = self.discount_strategy(self)
            else:
                discount = 0

            return self.price - discount

        def __repr__(self):

            statement = "Price: {}, price after discount: {}"
            return statement.format(self.price, self.price_after_discount())

    """function dedicated to On Sale Discount"""
    def on_sale_discount(order):

        return order.price * 0.25 + 20

    """function dedicated to 20 % discount"""
    def twenty_percent_discount(order):

        return order.price * 0.20

    """main function"""
    if __name__ == "__main__":

        print(Item(20000))

        """with discount strategy as 20 % discount"""
        print(Item(20000, discount_strategy = twenty_percent_discount))

        """with discount strategy as On Sale Discount"""
        print(Item(20000, discount_strategy = on_sale_discount))


**Tutorials:**

* `Variations Of The Strategy Pattern // Using Python features! <https://youtu.be/n2b_Cxh20Fw>`_


Concurrency
=======================================

* Active object
* Balking
* Binding properties
* Compute kernel
* Double-checked locking
* Event-based asynchronous
* Guarded suspension
* Join
* Lock
* Messaging design pattern (MDP)
* Monitor object
* Reactor
* Read-write block
* Scheduler
* Thread pool
* Thread-specific storage
* Safe Concurrency with Exclusive Ownership
* CPU atomic operation


References
=======================================

#. `Software design pattern <https://en.wikipedia.org/wiki/Software_design_pattern>`_
