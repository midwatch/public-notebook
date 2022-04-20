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
* Observer or Pub/Sub
* Servant
* Specification
* State
* Strategy
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
