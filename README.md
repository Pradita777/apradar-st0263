Descripcion
La idea del proyecto es crear una red pear to pear con un servidor central, esto para que cada pear carge o descargue archivos.
Tecnologías Utilizadas
El proyecto se realizo en Python 3.12.2
Requistos:
grpcio
grpcio-tools
fastapi
uvicorn
docker
Es necesario tener descargadas las librerias anteriores y docker en el computador.
para ejecutar el servidor central:
uvicorn serverc:app --reload
para ejecutar el pserver:
python peer_server.py
para ejecutar el pclient:
python peer_client.py download "nombre_archivo.txt"
python peer_client.py upload "nombre_archivo.txt"

1.	Preguntas que tiene del enunciado (entendimiento del problema)
¿Porque separamos el pear en pclient y pserver?
¿Que metodo es mejor para pasar archivos?
¿En que partes debo meter que logica?
2.	Defina la versión inicial de la arquitectura y tipo de red P2P, revísela con otros compañeros y reciba retroalimentación del profesor.
![image](https://github.com/Pradita777/apradar-st0263/assets/92939800/3c3ce54a-9813-4b0b-a4f1-2472ff3f9108)
Esta la hice con mis compañeros
![image](https://github.com/Pradita777/apradar-st0263/assets/92939800/1f71f0bf-42c8-49d9-8d17-c4e966029060)
Esta es la version final que saque al pensarlo yo solo
3.	Defina los servicios específicos que tendrá cada componente del sistema
Servidor Central:
@app.post("/register"); este metodo agrega al nuevo pear en una lista
@app.get("/search/{filename}", response_model=SearchResult); este metodo busca en la lista y retorna la ip y el puerto del archivo donde esta el archivo
Pserver:
def register_with_central_server(self, ip, port, files), registro con server central
def search_file_on_central_server(self, filename), pregunta al server central por la ubicacion del archivo
def UploadFile(self, request, context) Carga el archivo que le mando el pclient
def DownloadFile(self, request, context) Pasa el archivo al pclient que lo pidio
Pclient:
def upload_file(stub, filename); Sube un nuevo archivo al pserver
def download_file(stub, filename); Descarga un nuevo archivo del pserver que tenga el que busca
4.	Defina las interacciones entre componentes, los tipos de comunicaciones y tipo de middleware especifico que va a emplear (REST API, gRPC, MOM), debe emplear todos estos middlewares.
En el caso de los pserver y pclient se comunican entre si via gRpc y el pserver con el server central via REST API
5.	Defina un plan de desarrollo, desde victorias tempranas, hasta la finalización del proyecto.
Primera victoria: conectar el servidor central con el pserver
Ultima victoria: conectar los pears para pasarse archivos entre ellos
7.	Desarrollo y Pruebas en localhost o AWS
9.	Despliegue los nodos como máquinas virtuales con docker en AWS Academy
![image](https://github.com/Pradita777/apradar-st0263/assets/92939800/1cfc7c88-e595-4f76-a3a5-14218123b3b7)
Para este reto solo lo hice con el servidor central
11.	Realice pruebas en AWS.
Se muestran en el video
13.	Realice la documentación
14.	Entregue y sustente al profesor mediante un video creado por ud donde explique el proceso de diseño, desarrollo y ejecución (no más de 30 mins)
https://eafit.sharepoint.com/:v:/s/siuu/EdTWeUxgiyJHkRD_intHZdoBBmBKSfhWY6zvdonM1hq4mQ?e=hrXef2

