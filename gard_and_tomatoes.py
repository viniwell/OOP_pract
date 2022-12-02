import random
class Tomato:
    states=['Отсутствует', 'Цветение', 'Зеленый', 'Красный']
    def __init__(self,index):
        self._index=index
        self._state=0
    def grow(self):
        if self._state<3:
            self._state+=1
        else:
            self._state=3
    def is_ripe(self):
        if self._state==3:
            True
        else:
            False
    def __str__(self):
        ans=f'Tomato {self._index} is {Tomato.states[self._state]}'
        return ans
class Tomatobush:
    x=0
    def __init__(self, amount):
        self.amount=int(amount)
        self.tomatoes=[]
        for i in range(self.amount):
            tomato=Tomato(i)
            self.tomatoes.append(tomato)
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        ans=[]
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
                break
            else:
                return True
    def give_away_all(self):
        self.tomatoes=[]
class Gardener:
    def __init__(self, name, tomatobush):
        self.name=name
        self._plant=tomatobush
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        for tomato in self._plant.tomatoes:
            print(tomato)
        print('Gardener finished')
    def harvest(self):
        print('Gardener is harvesting')
        if self._plant.all_are_ripe():
            print('Harvesting was done!')
            self._plant.give_away_all()
        else:
            print('Too early!')
    @staticmethod
    def knowledge_base():
        print('Harvest time for tomatoes should ideally occur')
        print('when the fruit is a mature green and')
        print('then allowed to ripen off the vine.')
        print('This prevents splitting or bruising')
        print('and allows for a measure of control over the ripening process.')
def main():
    Gardener.knowledge_base()
    tomatobush=Tomatobush(int(input()))
    gardener=Gardener('Sashko', tomatobush)
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.harvest()
main()


