from base_driver import Driver
from nemo_api import NemoAPI

SMALL_TIME = 0.0001
class NemoDriver(Driver):
    def __init__(self):
        self.api = NemoAPI()
    def login(self, id, password):
        try:
            self.api.cerification(id, password)
            print("login success")
        except:
            raise ValueError("login fail")

    def buy(self, code, price, qty):
        self.api.purchasing_stock(code, price, qty)
        print("success to purchase")

    def sell(self, code, price, qty):
        self.api.selling_stock(code, price, qty)
        print("success to sell")

    def get_price(self, code, minute):
        self.api.get_market_price(code, SMALL_TIME)
        return self.api.get_market_price(code, SMALL_TIME)  # 테스트용 더미 데이터