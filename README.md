# Trabajo Final Adquisición de datos
El presente trabajo consiste en una aplicación Web hecha en Python 3.6, Flask 0.12, Scrapy 1.15 y MongoDB. La aplicación funciona de la siguiente manera: 
1. Visita URL
2. Extrae links
3. Visita los links
4. Extrae información
5. Almacena en MongoDB
6. Vuelve a 1

Hasta llegar a un criterio de corte. 

## Dependencias
Es necesario tener instalado docker y docker-compose

## Configuración
Crear un archivo .env con las siguientes variables: 
SPIDER_TIME_LIMIT=30
MONGO_HOST=mongodb
MONGO_COLLECTION=adquisicion_db

Ya viene con el repo el volumen que tiene creada la base de datos y la collection. Por lo que se deberá crear. Lo que es necesario modificar a los efectos de hacer un prueba más o menos largo es el SPIDER_TIME_LIMIT que se define el criterio de corte en segundos. 

Nota: Si luego de buildear la aplicación se cambia alguna variable de entorno entonces debe ejecutarse

`docker-compose up --build --force-recreate`

## Instalación

`git clone https://github.com/makx/flask_scrapy_mongodb_tp_final.git .`

`docker-compose up`

Se levantan dos containers: 
- app en el puerto 9000 del host local
- mongodb en el puerto 8001 del host local

## Ejecución
Abrir el navegador en http://localhost:9000

## Conexión con la base de datos
Se puede utilizar  [robomongo]:https://robomongo.org/



