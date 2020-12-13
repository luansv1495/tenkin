import os,mimetypes,asyncio

class TenkinApp:
    def __init__(
        self
    ):
        self.public_path = "public"
        self.project_path = os.path.join(os.getcwd(), self.public_path)

    async def __call__(self,scope, receive, send):
        req_path, req_type = await self.make_request_path(filename=scope['path'][1:])

        if os.path.exists(req_path):
            await send({
                'type': 'http.response.start',
                'status': 200,
                'headers': [
                    [b'content-type', req_type],
                ]
            })
            await send({
                'type': 'http.response.body',
                'body': open(req_path, "rb").read(),
            })
        else:
            await self.handler_404_exception(send=send)

    async def make_request_path(self, filename: str):
        req_path = os.path.join(self.project_path, filename)
        if '.' not in req_path.split(os.path.sep)[-1]:
            req_path = os.path.join(req_path, 'index.html')
            
        req_type = mimetypes.guess_type(req_path)[0]

        return req_path, req_type

    async def response(self, req_type: str, req_path: str, send):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', req_type],
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': open(req_path, "rb").read(),
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