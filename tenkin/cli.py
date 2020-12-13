import os,sys,click
from app import TenkinApp

app = TenkinApp()

@click.command()
@click.option('--host', "-h", default='localhost', help="The interface to bind to.")
@click.option('--port', "-p", default=8000, help="The port to bind to.")
def run(host,port):
    from uvicorn import run

    with run('cli:app',host=host, port=port,reload=True,workers=8,debug=True):
        print(f"Servidor disponível na porta {port}")
        print(f"Acesse http://{host}:{port}")
        print("Para finalizar o servidor pressione 'Ctrl-c'")

@click.command()
@click.option('--project_name',prompt='Project name', type=str)
def create(project_name):
    import templates

    project_path = os.path.join(os.getcwd(),project_name)

    templates.create_project(project_path=project_path)

@click.group()
def main():
    pass

main.add_command(run)
main.add_command(create)
if __name__ == "__main__":
    main()