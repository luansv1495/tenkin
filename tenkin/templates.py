import os,shutil
from tenkin.exceptions import handler_message

items = [
        {'path':'\\public', 'type': 'folder'},
        {'path':'\\public\\index.html', 'type': 'file', 'template': './static/html/index.html'},
        {'path':'\\public\\main.js', 'type': 'file', 'template': './static/js/main.js'},
        {'path':'\\public\\manifest.json', 'type': 'file', 'template': './static/json/manifest.json'},
        {'path':'\\public\\favicon.ico', 'type': 'file', 'template': './static/assets/favicon.ico'},
        {'path':'\\public\\logo192.png', 'type': 'file', 'template': './static/assets/logo192.png'},
        {'path':'\\public\\logo512.png', 'type': 'file', 'template': './static/assets/logo512.png'},
        {'path':'\\public\\service-worker.js', 'type': 'file', 'template': './static/js/service-worker.js'},
        {'path':'\\src', 'type': 'folder'},
        {'path':'\\src\\main.py', 'type': 'file', 'template': './static/python/main.py'},
]

def _create_file(original: str, target: str):
    try:
        shutil.copyfile(original,target)
    except Exception as err:
        raise RuntimeError(handler_message(message=f"{err}!",type='FAIL'))
    else:
        handler_message(message=f"O arquivo {target} foi criado!",write=True)
        return True

def _create_folder(folder_path: str) -> bool:
    try: 
        os.mkdir(folder_path)
    except Exception: 
        raise RuntimeError(handler_message(message=f"A pasta {folder_path} ja existe!",type='FAIL'))
    else:
        handler_message(message=f"A pasta {folder_path} foi criada!",write=True)
        return True

def create_project(project_path: str):
    if not _create_folder(folder_path=project_path) == True: 
        return False

    for item in items:
        if item['type'] == 'folder':
            _create_folder(folder_path=project_path+item['path'])
        elif item['type'] == 'file':
            _create_file(original = item['template'],target = project_path+item['path'])
                
    return True
