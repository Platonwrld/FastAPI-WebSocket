from fastapi import FastAPI, WebSocket, Request
import uvicorn
import json
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    id = 1
    while True:
        data = await websocket.receive_json()
        await websocket.send_json(f"{id}. {data}")
        id += 1
        


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)