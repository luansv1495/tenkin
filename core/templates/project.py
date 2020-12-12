from core.utils.cli import ColorsCLI
import os,sys,shutil

def template_project_generate(project_path: str):

    items = [
        {'path':'\\public', 'type': 'folder'},
        {'path':'\\public\\index.html', 'type': 'file', 'template': './core/templates/base/html/index.html'},
        {'path':'\\public\\manifest.json', 'type': 'file', 'template': './core/templates/base/json/manifest.json'},
        {'path':'\\public\\favicon.ico', 'type': 'file', 'template': './core/templates/base/assets/favicon.ico'},
        {'path':'\\public\\logo192.png', 'type': 'file', 'template': './core/templates/base/assets/logo192.png'},
        {'path':'\\public\\logo512.png', 'type': 'file', 'template': './core/templates/base/assets/logo512.png'},
        {'path':'\\public\\service-worker.js', 'type': 'file', 'template': './core/templates/base/js/service-worker.js'},
        {'path':'\\src', 'type': 'folder'},
    ]

    if not template_create_folder(folder_path=project_path) == True: 
        return False

    for item in items:
        if item['type'] == 'folder':
            template_create_folder(folder_path=project_path+item['path'])
        elif item['type'] == 'file':
            template_create_file(original = item['template'],target = project_path+item['path'])

    return True

def template_create_file(original: str, target: str):
    try:
        shutil.copyfile(original,target)
    except Exception as err:
        print(ColorsCLI.WARNING + f"{err}!" + ColorsCLI.ENDC)
        sys.exit(0)
    else:
        print(ColorsCLI.OKGREEN + f"O arquivo {target} foi criado!" + ColorsCLI.ENDC)
        return True

def template_create_folder(folder_path: str):
    try:
        os.mkdir(folder_path)
    except Exception:
        print(ColorsCLI.WARNING + f"A pasta {folder_path} ja existe!" + ColorsCLI.ENDC)
        sys.exit(0)
    else:
        print(ColorsCLI.OKGREEN + f"A pasta {folder_path} foi criada!" + ColorsCLI.ENDC)
        return True