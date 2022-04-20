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
* Command
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
