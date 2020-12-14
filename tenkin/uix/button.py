from tenkin.uix.styles import button as md_style

class Button:
    def __init__(self,id: str = None,value: str = '', style: dict = md_style):
        self.id = id
        self.class_name = 'button'
        self.class_effect_names = ['button:hover','button:active']
        self.value = value
        self.style = style

    def generate_html(self):
        id = f" id=\'{self.id}\'" if self.id else ''
        return f"<button{id} type=\"button\" class=\"{self.class_name}\">{self.value}</button>"

    def generate_css(self,current_tree: list):
        if self.class_name in current_tree:
            return current_tree
        else:
            current_tree.append(self.class_name)
            current_tree.extend(self.class_effect_names)
            return current_tree