from abc import abstractmethod, ABC


class MockDriver(ABC):
    def __init__(self, driver: MockDriver):
        self.driver = driver
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
    def get_price(self, id, password, stock_code):
        ...

