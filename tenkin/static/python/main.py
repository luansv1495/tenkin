from tenkin.uix.container import Container
from tenkin.uix.label import Label

class App(Container):
    def __init__(self):
        Container.__init__(self)
        self.childrens = [
            Label(text = "Ola gente"),
        ]