from wsgiref.simple_server import make_server
from core.utils.file import get_content
from core.utils.exception import exception_project_in_run
from core.templates.exception import template_project_run_found
from core.templates.project import template_project_generate
from core.utils.cli import cli
import os,sys,click

class WebApp:
    def __init__(self, enviroment, response):
        self.enviroment = enviroment
        self.response = response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type','text/html')]
        self.response(status, response_headers)
        content_tmp = get_content(path=os.getcwd()+"/build/index.html")
        validate = exception_project_in_run(content_tmp)
        content = content_tmp if validate == True else template_project_run_found(error=validate)
        yield content.encode()

@click.command()
@click.option('--host', default='localhost')
@click.option('--port', default=8000)
def run(host,port):
    with make_server(host,port,WebApp) as server:
        print(f"Servidor disponível na porta {port}\nAcesse http://{host}:{port}\nPara finalizar o servidor pressione 'Ctrl-c'")
        server.serve_forever()

@click.command()
@click.option('--project_name',prompt='Project name', type=str)
def create(project_name):
    project_path = os.getcwd() + "\\" + project_name
    template_project_generate(project_path=project_path)

cli.add_command(run)
cli.add_command(create)
if __name__ == "__main__":
    cli()