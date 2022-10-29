class Product:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, ingredients, cost):
        # Initialize the new instance
        self.ingredients = ingredients
        self.cost = cost

    def __repr__(self) -> str:
        return f"(Składniki={self.ingredients}, Koszt={self.cost})"
    #
    # @property
    # def ingredients(self):
    #     return self.ingredients
    #
    # @property
    # def cost(self):
    #     return self.cost
    #
    # @cost.setter
    # def cost(self, value):
    #     self.cost = value

#BUT without polluting the class namespace with get and set methods for each attribute.
#You retain external direct access to the variable by using ._bar instead of .bar.
#https://realpython.com/python-class-constructor/