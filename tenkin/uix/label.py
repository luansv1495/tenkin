from tenkin.uix.styles import label as md_style

class Label:
    def __init__(self,id: str = None,text: str = '', style: dict = md_style):
        self.id = id
        self.class_name = 'label'
        self.text = text
        self.style = style

    def generate_html(self):
        id = f" id=\'{self.id}\'" if self.id else ''
        return f"<p{id} class=\"{self.class_name}\">{self.text}</p>"

    def generate_css(self,current_tree: list):
        if self.class_name in current_tree:
            return current_tree
        else:
            current_tree.append(self.class_name)
            return current_tree