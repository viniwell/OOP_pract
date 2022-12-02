class Human:
    default_name="Alexandr"
    default_age='21'
    def __init__(self, name=default_name, age=default_age):
        self.name=name
        self.age=age
        self._money=0
        self._house=[]
    def info(self):
        print(f'Name-{self.name}\nAge-{self.age}\nProperty-{self._house}\nMoney-{self._money}')
    @staticmethod
    def default_info():
        print(f'Name-{Human.default_name}\nAge-{Human.default_age}')
    def make_deal(self, house, price):
            self._money-=price
            self._house.append(house)
    def earn_money(self):
        self._money+=1000
    def buy_house(self, house):
        price=house.final_price()
        if self._money>=price:
            self.make_deal(house=house, price=house.final_price())
            print('Succes')
        else:
            print('Not enough amount of money')
class House:
    def __init__(self, area, price):
        self._price=price
        self._area=area
    def final_price(self, sale=int(input())):
        return int(self._price*(100-sale)/100)
class SmallHouse(House):
    def __init__(self):
        super().__init__(area=40, price=int(input()))
Human.default_info()
human=Human()
human.info()
smallhouse=SmallHouse()
human.buy_house(house=smallhouse)
human.earn_money()
human.earn_money()
human.earn_money()
human.earn_money()
human.buy_house(house=smallhouse)
human.info()




        