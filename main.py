from wsgiref import simple_server, util
from core.templates.project import template_project_generate
from core.utils.cli import cli
import os,sys,click,mimetypes

class WebApp:
    def __init__(self, enviroment, response):
        self.enviroment = enviroment
        self.response = response

    def __iter__(self):
        path = os.getcwd()+"\\public"

        fn = os.path.join(path, self.enviroment['PATH_INFO'][1:])
        if '.' not in fn.split(os.path.sep)[-1]:
            fn = os.path.join(fn, 'index.html')
            
        type = mimetypes.guess_type(fn)[0]

        if os.path.exists(fn):
            self.response('200 OK', [('Content-Type', type)])
            return util.FileWrapper(open(fn, "rb"))
        else:
            self.response('404 Not Found', [('Content-Type', 'text/plain')])
            return [b'not found']

@click.command()
@click.option('--host', default='localhost')
@click.option('--port', default=8000)
def run(host,port):
    with simple_server.make_server(host,port,WebApp) as server:
        print(f"Servidor disponível na porta {port}\nAcesse http://{host}:{port}\nPara finalizar o servidor pressione 'Ctrl-c'")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down.")
            server.server_close()

@click.command()
@click.option('--project_name',prompt='Project name', type=str)
def create(project_name):
    project_path = os.getcwd() + "\\" + project_name
    template_project_generate(project_path=project_path)

cli.add_command(run)
cli.add_command(create)
if __name__ == "__main__":
    cli()