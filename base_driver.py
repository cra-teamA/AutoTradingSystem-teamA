from abc import abstractmethod, ABC

class Driver(ABC):
    def __init__(self):
        ...
    @abstractmethod
    def buy(self, stock_code, count, price):
        ...
    @abstractmethod
    def sell(self, stock_code, count, price):
        ...
    @abstractmethod
    def login(self, id, password):
        ...
    @abstractmethod
    def get_price(self, stock_code):
        ...