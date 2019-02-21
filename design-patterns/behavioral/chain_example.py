from . import Chain, ChainLink


class ConcreteChain(Chain):
    def __init__(self):
        super().__init__(ConcreteChainLinkOne())

    def fail(self):
        return 'Fail'

class ConcreateChainLinkOne(ChainLink):
    def __init__(self):
        super().__init__()
        self.set_successor(ConcreateChainLinkTwo())

    def handle(self, request):
        if request == 'handle_one':
            return "Handled in chain link one"
        else:
            return self.successor_handle(request)

class ConcreteChainLinkTwo(ChainLink):
    def __init__(self):  # Override init to set a successor on initialization.
        super().__init__()  # first call ChainLinks init
        self.set_successor(ConcreteChainLinkThree())  # Set the successor of this chain link
        # to a ConcreteChainLinkThree instance.

    def handle(self, request):  # Implement the handle method.
        if request == 'handle_two':
            return "Handled in chain link two"
        else:
            return self.successor_handle(request)  # If this ChainLink can't handle a request
            # ask its successor to handle it
            # (the ConcreteChainLinkThree instance)

class ConcreteChainLinkThree(ChainLink): # This object is a ChainLink

    def handle(self, request): # Implement the handle method.
        if request == 'handle_three':
            return "Handled in chain link three"
        else:
            return self.successor_handle(request) # If this ChainLink can't handle the request,
                                                  # ask its successor to handle it.
                                                  # (Has no successor so will raise AttributeError)
                                                  # (This exception is caught and will call a Chains fail method)
