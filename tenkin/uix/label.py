class Label:
    def __init__(self,id: str = None,text: str = ''):
        self.id = id
        self.text = text

    def generate(self):
        id = f" id=\'{self.id}\'" if self.id else ''
        return f"<p{id}>{self.text}</p>"