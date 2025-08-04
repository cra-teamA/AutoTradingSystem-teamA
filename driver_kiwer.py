from base_driver import Driver
from kiwer_api import KiwerAPI


class KiwerDriver(Driver):
    def __init__(self):
        self.kiwerapi = KiwerAPI()

    def login(self, id, password):
        self.kiwerapi.login(id, password)

    def buy(self, code, price, qty):
        self.kiwerapi.buy(code, qty, price)

    def sell(self, code, price, qty):
        self.kiwerapi.sell(code, qty, price)

    def get_price(self, code):
        return self.kiwerapi.current_price(code)

if __name__=='__main__':
    kw = KiwerDriver()
    kw.login('aa','bb')