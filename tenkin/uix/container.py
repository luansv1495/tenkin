class Container:
    def __init__(self,id: str = None,children: str = ''):
        self.id = id
        self.children = children

    def generate(self):
        id = f" id=\'{self.id}\'" if self.id else ''
        return f"<div{id}>{self.children.generate()}</div>"