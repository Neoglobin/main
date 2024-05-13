class Tomato:
    states = {0: "отсутствует", 1: "цветение", 2: "зелёный", 3: "красный"}
    def __init__(self, _index):
        '''
        :param _index: Защищённый атрибут
        :param _state: Защищённый атрибут
        '''
        self._index = _index
        self._state = 0 # Начальное состояние - "отсутствует"

    def grow(self):
        # Продвигает помидор на следующий этап зрелости, если это возможно.
        if self._state < len(self.states) - 1:
            self._state += 1

    def is_ripe(self):
        # Проверяет, достиг ли помидор зрелости.
        if self._state == 3:
            return self._state

class TomatoBush:
    def __init__(self, count):
        '''
        Инициализация куста помидоров.
        :param count: Количество помидоров на кусте
        '''''
        self.tomatoes = [Tomato(i) for i in range(count)]

    def grow_all(self):
        # Продвигает все помидоры в кусте на следующий этап зрелости.
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Проверяет, все ли помидоры в кусте достигли зрелости.
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Очищает куст от помидоров.
        self.tomatoes = []

class Gardener:
    def __init__(self, name, tomato_bush):
        '''
        Инициализация садовода.

        :param name: Имя садовода.
        :param tomato_bush: Куст помидоров, который будет ухаживать садовод.
        '''
        self.name = name
        self._plant = tomato_bush

    def work(self):
        # Ухаживает за кустом помидоров, продвигая их на следующий этап зрелости.
        self._plant.grow_all()

    def harvest(self):
        # Собирает урожай, если все помидоры достигли зрелости.
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Весь урожай собран")
        else:
            print("Не всё созрело!")

    @staticmethod
    # Статический метод для вывода базовой информации о садоводстве.
    def kwnowledge_base(self):
        print("Основные задачи садоводства: получение продукции нужной кондиции в количестве, "
              "обеспечивающем рентабельность производства; сохранение и улучшение плодородия почвы; "
              "защита насаждений от неблагоприятных природных условий и вредителей и болезней. "
              "Для решения этих задач садоводство использует различные методы и технологии, такие "
              "как подбор сортов, выбор места посадки, обработка почвы, внесение удобрений, полив, "
              "обрезка, защита от вредителей и болезней и др.")



Gardener.kwnowledge_base(staticmethod)

brush = TomatoBush(4)
gardener = Gardener("Vasya", brush)

gardener.work()
gardener.harvest()

gardener.work()
gardener.work()

gardener.harvest()




















