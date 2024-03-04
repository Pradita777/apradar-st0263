import sys
import grpc
import peer_pb2
import peer_pb2_grpc

def upload_file(stub, filename):
    response = stub.UploadFile(peer_pb2.FileData(filename=filename))
    print(response.message)

def download_file(stub, filename):
    response = stub.DownloadFile(peer_pb2.FileName(filename=filename))
    print(f"Downloaded file content: {response.content}")

def run(method, *args):
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = peer_pb2_grpc.PeerServiceStub(channel)
        if method == 'upload':
            upload_file(stub, *args)
        elif method == 'download':
            download_file(stub, *args)
        else:
            print("Método no reconocido. Use 'upload' o 'download'.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python peer_client.py <método> [argumentos]")
        sys.exit(1)
    method = sys.argv[1]
    args = sys.argv[2:]
    run(method, *args)