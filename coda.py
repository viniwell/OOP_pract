class Soda:
    def __init__(self, adding):
        self.adding=adding
    def show_my_drink(self):
        if self.adding=='':
            ans=f'Обычная газировка'
        else:
            ans=f'Газировка и {self.adding}'
        return ans
soda=Soda(input())
print(soda.show_my_drink())