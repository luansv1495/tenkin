
def get_content(path: str) -> str:
    content = None
    try:
        with open(path,'r') as file:
            content = file.read()
            file.close()
    except Exception as identifier:
        return str(identifier.__class__.__name__)
    else:
        return content