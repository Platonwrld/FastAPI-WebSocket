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
        data_1 = await websocket.receive_json()
        data_2 = {}
        data_2[id] = data_1['id']
        data_2 = json.dumps(data_2)
        await websocket.send_json(data_2)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)