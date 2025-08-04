from base_driver import Driver

class MockDriver(Driver):
    def login(self, id, password):
        if id == "id" and password == "pw":
            print("login success")
        else:
            raise ValueError("login fail")

    def buy(self, code, price, qty):
        print("success to purchase")

    def sell(self, code, price, qty):
        print("success to sell")

    def get_price(self, code):
        return 1000  # 테스트용 더미 데이터