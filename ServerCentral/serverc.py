from fastapi import FastAPI, Body
from typing import List, Tuple
from pydantic import BaseModel

app = FastAPI()

# Almacén de información sobre pares y archivos
peer_data = {}


class PeerRegistrationRequest(BaseModel):
    ip: str
    port: int
    files: List[str]


class SearchResult(BaseModel):
    message: str
    peers_with_file: List[Tuple[str, int]]


@app.post("/register")
async def register_peer(peer_info: PeerRegistrationRequest):
    print(f"Received registration request. IP: {peer_info.ip}, Port: {peer_info.port}, Files: {peer_info.files}")
    peer_data[(peer_info.ip, peer_info.port)] = peer_info.files
    print("Peer registered:", {"ip": peer_info.ip, "files": peer_info.files})
    print(peer_data)
    return {"message": "Peer registered successfully"}


@app.get("/search/{filename}", response_model=SearchResult)
async def search_file(filename: str) -> SearchResult:
    # Buscar entre los pares para encontrar el archivo
    peers_with_file = [(ip, port) for (ip, port), file_list in peer_data.items() if filename in file_list]

    if not peers_with_file:
        return {"message": "File not found", "peers_with_file": []}
    
    return {"message": "File found", "peers_with_file": peers_with_file}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
