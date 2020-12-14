import os,mimetypes,asyncio,sys
from tenkin.exceptions import handler_message
from tenkin.helper import generate_css_from_list

class TenkinApp:
    def __init__(self):
        self.public_folder = "public"
        self.source_folder = "src"
        self.source_filename = "main.py"
        self.public_filename = "index.html"
        self.style_filename = "style.css"
        self.source_path = os.path.join(os.getcwd(), self.source_folder)
        self.project_path = os.path.join(os.getcwd(), self.public_folder)

    async def __call__(self,scope, receive, send):
        req_path, req_type = await self.make_request_path(filename=scope['path'][1:])

        if os.path.exists(req_path):
            await self.response(req_type=req_type,req_path=req_path,send=send)
        else:
            await self.handler_404_exception(send=send)

    async def make_request_path(self, filename: str):
        req_path = os.path.join(self.project_path, filename)
        if '.' not in req_path.split(os.path.sep)[-1]:
            req_path = os.path.join(req_path, self.public_filename)
            
        req_type = mimetypes.guess_type(req_path)[0]

        return req_path, req_type

    async def make_project(self):
        source = os.path.join(self.source_path,self.source_filename)
        
        if not os.path.exists(source):
            raise RuntimeError(handler_message(message="O caminho pra o projeto esta incorreto!",type="WARNING"))
        
        sys.path.append(self.source_path)
        
        from main import App

        app = App()

        return await self.join_project_source(source=app.generate_html())

    async def make_project_style(self):
        sys.path.append(self.source_path)

        from main import App

        app = App()

        css_tag_list = app.generate_css(current_tree=[])[-1]

        return generate_css_from_list(tag_list=css_tag_list)

    async def join_project_source(self,source: str):
        from bs4 import BeautifulSoup

        with open(os.path.join(self.project_path,self.public_filename)) as html_file:
            source_soup = BeautifulSoup(source, features='html.parser')
            root_soup = BeautifulSoup(html_file.read(), features='html.parser')
            html_file.close()
            root_div = root_soup.find(id="root")
            root_div.append(source_soup.div)
            new_html = root_soup.prettify()
        return new_html

    async def response(self, req_type: str, req_path: str, send):
        if os.path.basename(req_path) == self.public_filename:
            response = await self.make_project()
            response = response.encode()
        elif os.path.basename(req_path) == self.style_filename:
            response = await self.make_project_style()
            response = response.encode()
        else:
            response = open(req_path, "rb").read()

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', req_type],
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': response,
        })

    async def handler_404_exception(self, send):
        await send({
            'type': 'http.response.start',
            'status': 404,
            'headers': [
                [b'content-type', b'text/plain'],
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': b'not found',
        })