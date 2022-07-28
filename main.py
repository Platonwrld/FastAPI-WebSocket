from fastapi import FastAPI, WebSocket
import uvicorn
import pickle

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    id = 1
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"{id}. {data}")
        id += 1



if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)