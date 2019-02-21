from abc import ABCMeta, abstractmethod


class ChainLink(object, metaclass=ABCMeta):
    def __init__(self):
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    def successor_handle(self, request):
        self.successor.handle(request)

    @abstractmethod
    def handle(self, request):
        pass


class Chain(object, metaclass=ABCMeta):
    def __init__(self):
        pass

    def handle(self, request):
        pass

    @abstractmethod
    def fail(self):
        pass
