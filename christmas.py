class Pizza:

    def __init__(self):
        self._cheese = None
        self._greens = None
        self._name = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_cheese(self, cheese):
        self._cheese = cheese

    def get_cheese(self):
        return self._cheese

    def set_greens(self, greens):
        self._greens = greens

    def get_greens(self):
        return self._greens

    def info(self):
        print("Name:", self._name, "\nServings of cheese:", self._cheese, "\nServings of greens:", self._greens)


class ItalianPizza(Pizza):

    def __init__(self):

        super().__init__()
        self.__thickness = None
        self.__cheeserinds = None


    def set_thickness(self, thickness):
        self.__thickness = thickness

    def get_thickness(self):
        return self.__thickness

    def set_cheeserinds(self, cheeserinds):
        self.__cheeserinds = cheeserinds

    def get_cheeserinds(self):
        return self.__cheeserinds


    def info(self):
        super().info()
        print("Thickness:", self.__thickness, "\nCheese rinds:", self.__cheeserinds)


Neapolitan = ItalianPizza()
Neapolitan.set_name('Neapolitan')
Neapolitan.set_cheese(2)
Neapolitan.set_greens(2)
Neapolitan.set_thickness(1)
Neapolitan.set_cheeserinds(True)
Neapolitan.info()
print("\n")

Roman = ItalianPizza()
Roman.set_name('Roman')
Roman.set_cheese(0)
Roman.set_greens(4)
Roman.set_thickness(2)
Roman.set_cheeserinds(False)
Roman.info()
print("\n")

classical = ItalianPizza()
classical.set_name('Classical')
classical.set_cheese(100)
classical.set_greens(0)
classical.set_thickness(1)
classical.set_cheeserinds(True)
classical.info()
print("\n")

panpizza = ItalianPizza()
panpizza.set_name('Pan pizza')
panpizza.set_cheese(0)
panpizza.set_greens(0)
panpizza.set_thickness(5)
panpizza.set_cheeserinds(False)
panpizza.info()
print("\n")