from tenkin.uix.styles import container as md_style
class Container:
    def __init__(self,id: str = None,childrens: str = '', style: dict = md_style):
        self.id = id
        self.class_name = 'container'
        self.childrens = childrens
        self.style = style

    def generate_html(self):
        id = f" id=\'{self.id}\'" if self.id else ''
        return f"<div{id} class=\"{self.class_name}\">{''.join([child.generate_html() for child in self.childrens])}</div>"

    def generate_css(self,current_tree: list):
        if self.class_name in current_tree:
            return current_tree
        else:
            #, f".{self.class_name} {self.style}", [child.generate_css(current_tree=current_tree) for child in self.childrens]
            current_tree.append(self.class_name)
            return [child.generate_css(current_tree=current_tree) for child in self.childrens]