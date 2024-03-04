from concurrent import futures
import grpc
import peer_pb2
import peer_pb2_grpc
import requests

class PeerService(peer_pb2_grpc.PeerServiceServicer):
    def __init__(self, central_server_url):
        self.central_server_url = central_server_url

    def register_with_central_server(self, ip, port, files):
        data = {"ip": ip, "port": port, "files": files}
        try:
            print(f"Sending registration request to {self.central_server_url}/register with data: {data}")
            headers = {"Content-Type": "application/json"}
            response = requests.post(f"{self.central_server_url}/register", json=data, headers=headers)
            response.raise_for_status()
            print("Server central registration response:", response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error registering with server central: {e}")

    def search_file_on_central_server(self, filename):
        try:
            response = requests.get(f"{self.central_server_url}/search/{filename}")
            response.raise_for_status()

            if response.status_code == 200:
                file_info = response.json()
                print("Información del archivo encontrada:", file_info)
                # Devolver una tupla con la IP y el puerto
                return (file_info["ip"], file_info["port"])
            else:
                print("Archivo no encontrado en el servidor central")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error al buscar el archivo en el servidor central: {e}")
            return None


    def UploadFile(self, request, context):
        print(f"Received file: {request.filename}")

        # Registrar archivo en el servidor central
        self.register_with_central_server("127.0.0.1", 50050, [request.filename])

        return peer_pb2.Response(message="File uploaded successfully")

    def DownloadFile(self, request, context):
        content = b"Sample file content"

        # Buscar información sobre el archivo en el servidor central
        file_info = self.search_file_on_central_server(request.filename)

        # Si se encuentra el archivo en el servidor central, devolver la IP y el puerto
        if file_info:
            return peer_pb2.FileLocation(ip=file_info["ip"], port=file_info["port"], filename=request.filename)
        else:
            return peer_pb2.Response(message="File not found")

def serve():
    central_server_url = "http://54.92.204.191:8000"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    peer_pb2_grpc.add_PeerServiceServicer_to_server(PeerService(central_server_url), server)
    server.add_insecure_port('[::]:50050')
    print("Server listening on [::]:50050")

    # Obtener dirección IP del servidor para registrarse en el servidor central
    import socket
    ip = socket.gethostbyname(socket.gethostname())

    # Obtener la lista de archivos del servidor para registrarse en el servidor central
    files = ["example.txt", "example2.txt"]

    # Registrar el servidor en el servidor central al inicio
    PeerService(central_server_url).register_with_central_server(ip, 50050, files)

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()