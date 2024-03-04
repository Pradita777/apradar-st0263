# info de la materia: Topicos Especias En Telematica
#
# Estudiante(s): Andres Prada Rodriguez, apradar@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
# Reto 1 y 2 Conexión pear to pear
#
# 1. breve descripción de la actividad
# El proyecto "pserver", "pclient" y "server central" es un sistema distribuido que permite a los clientes cargar y descargar archivos a través de un servidor central y una red de pares (peers). Los pares actúan como nodos en la red y almacenan una copia de los archivos disponibles para compartir.
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
### Cumpli con crear el servidor central, el pserver y el pclient, la comunicacion entre el pserver y el servidor central, montar a docker el servidor central y montarlo a una instancia de aws, que al conectarse con el pserver lo agregara a su lista.
## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
### No logre conectar el pclient con otro pserver para el download de archivos, no logre el logout del servidor central, no logre montar a docker el pserver y el pclient, como tampoco los monte a aws.
# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
### El diseño de alto nivel del proyecto se basa en una arquitectura cliente-servidor distribuida, donde el servidor central actúa como punto centralizado de coordinación y los pares gestionan el almacenamiento y distribución de archivos.
# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
### Se uso Python 3.12.2 
### Requistos: grpcio grpcio-tools fastapi uvicorn docker Es necesario tener descargadas las librerias anteriores y docker en el computador. 
## como se compila y ejecuta.
### para ejecutar el servidor central: uvicorn serverc:app --reload 
### para ejecutar el pserver: python peer_server.py 
### para ejecutar el pclient: python peer_client.py download "nombre_archivo.txt" python peer_client.py upload "nombre_archivo.txt"
## detalles del desarrollo.
### Pserver (Peer Server) 
### El servidor de pares se implementó utilizando el lenguaje de programación Python y el framework de desarrollo de aplicaciones web FastAPI. 
### Se diseñó para manejar las solicitudes de carga y descarga de archivos de los clientes mediante comunicación RPC utilizando gRPC. 
### Se definieron los métodos UploadFile y DownloadFile en el servicio gRPC PeerService para manejar las solicitudes de carga y descarga de archivos, respectivamente. 
### Se utilizó la biblioteca concurrent.futures para manejar las conexiones concurrentes entrantes y salientes.
### Pclient (Peer Client)
### El cliente de pares se implementó como una interfaz de línea de comandos (CLI) utilizando el lenguaje de programación Python y la biblioteca gRPC para comunicarse con el servidor de pares.
### Se implementaron los métodos upload_file y download_file para permitir a los usuarios cargar y descargar archivos desde la línea de comandos.
### Se utilizó la biblioteca argparse para analizar los argumentos de la línea de comandos proporcionados por el usuario.
### Server Central
### El servidor central se implementó como una aplicación web utilizando el framework FastAPI para manejar las solicitudes de registro de pares y búsquedas de archivos.
### Se definieron las rutas /register y /search/{filename} para manejar las solicitudes de registro de pares y búsquedas de archivos, respectivamente.
### Se utilizó la biblioteca requests para realizar solicitudes HTTP a los pares y coordinar el registro y la búsqueda de archivos en la red.
### detalles técnicos
### Lenguaje de Programación: Python
### Frameworks y Bibliotecas:
### FastAPI: Framework web para construir APIs rápidas con Python.
### gRPC: Framework para la implementación de servicios RPC (Remote Procedure Call).
### Requests: Biblioteca HTTP para realizar solicitudes web en Python.
### Herramientas:
### Concurrency in Python: Módulo concurrent.futures para manejar la concurrencia en Python.
### Argument Parsing: Biblioteca argparse para analizar los argumentos de la línea de comandos.
### Entorno de Desarrollo:
### Sistema Operativo: Windows, Ubuntu
### Entorno de Desarrollo: VisualStudio
### Herramientas de Control de Versiones: Git
### Dependencias del Proyecto:
#### fastapi
#### grpcio
#### requests
#### concurrent.futures
### ![image](https://github.com/Pradita777/pradita777-st0263/assets/92939800/df0c36aa-d252-4dbf-8c8e-f0263bffd350)
# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
# IP o nombres de dominio en nube o en la máquina servidor.
### Se uso AWS para este proyecto, tambien se trabajo de forma local, no se uso dominio se trabajo por ip.
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
### Para el uso de AWS es necesario que cada puerto que vayamos a usar lo definamos en las llaves de seguridad de las instancias si no no podremos comunicarnos con el puerto, es importante en el pserver cambiar la ip del servidor central cada que cambie.
## como se lanza el servidor.
### uvicorn serverc:app --reload 
## una mini guia de como un usuario utilizaría el software o la aplicación
### https://eafit.sharepoint.com/:v:/s/siuu/EdTWeUxgiyJHkRD_intHZdoBBmBKSfhWY6zvdonM1hq4mQ?e=hrXef2
# referencias:
## url de donde tomo info para desarrollar este proyecto
### https://chat.openai.com 
### https://github.com/st0263eafit/st0263-241/blob/main/README-template.md

# Actividades del taller: 
## 1.	Preguntas que tiene del enunciado (entendimiento del problema)
### ¿Porque separamos el pear en pclient y pserver?
### ¿Que metodo es mejor para pasar archivos?
### ¿En que partes debo meter que logica?
## 2.	Defina la versión inicial de la arquitectura y tipo de red P2P, revísela con otros compañeros y reciba retroalimentación del profesor.
### Esta la hice con mis compañeros
### ![image](https://github.com/Pradita777/apradar-st0263/assets/92939800/3c3ce54a-9813-4b0b-a4f1-2472ff3f9108)
### Esta es la version final que saque al pensarlo yo solo
### ![image](https://github.com/Pradita777/apradar-st0263/assets/92939800/1f71f0bf-42c8-49d9-8d17-c4e966029060)
## 3.	Defina los servicios específicos que tendrá cada componente del sistema
### Servidor Central:
### @app.post("/register"); este metodo agrega al nuevo pear en una lista
### @app.get("/search/{filename}", response_model=SearchResult); este metodo busca en la lista y retorna la ip y el puerto del archivo donde esta el archivo
### Pserver:
### def register_with_central_server(self, ip, port, files), registro con server central
### def search_file_on_central_server(self, filename), pregunta al server central por la ubicacion del archivo
### def UploadFile(self, request, context) Carga el archivo que le mando el pclient
### def DownloadFile(self, request, context) Pasa el archivo al pclient que lo pidio
### Pclient:
### def upload_file(stub, filename); Sube un nuevo archivo al pserver
### def download_file(stub, filename); Descarga un nuevo archivo del pserver que tenga el que busca
## 4.	Defina las interacciones entre componentes, los tipos de comunicaciones y tipo de middleware especifico que va a emplear (REST API, gRPC, MOM), debe emplear todos estos middlewares.
### En el caso de los pserver y pclient se comunican entre si via gRpc y el pserver con el server central via REST API
## 5.	Defina un plan de desarrollo, desde victorias tempranas, hasta la finalización del proyecto.
### Primera victoria: conectar el servidor central con el pserver
### Ultima victoria: conectar los pears para pasarse archivos entre ellos
## 7. 	Desarrollo y Pruebas en localhost o AWS
## 9.	Despliegue los nodos como máquinas virtuales con docker en AWS Academy
### Para este reto solo lo hice con el servidor central
### ![image](https://github.com/Pradita777/apradar-st0263/assets/92939800/1cfc7c88-e595-4f76-a3a5-14218123b3b7)
## 11.	Realice pruebas en AWS.
### Se muestran en el video
## 13.	Realice la documentación
## 14.	Entregue y sustente al profesor mediante un video creado por ud donde explique el proceso de diseño, desarrollo y ejecución (no más de 30 mins)
### https://eafit.sharepoint.com/:v:/s/siuu/EdTWeUxgiyJHkRD_intHZdoBBmBKSfhWY6zvdonM1hq4mQ?e=hrXef2
