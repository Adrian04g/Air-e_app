# I-C_SEGUIMIENTO-OPERTIVO

## ⚠️Advertencia La documentacion puede estar desactualizada⚠️

## Descripción
Aplicacion web para donde se gestionaran la solicitudes de los PRST en donde se hace anlisis, informe y facturas de los proyectos

## Objetivos del proyecto
1. Llevar el proceso del area a un software (en este caso una apliacion web)
2. Registro y control de documentación técnica y administrativa.
3. Seguimiento de avances y estados de los proyectos.
4. Generación de reportes y condltas de factura.

## Características principales
- Gestión 
- registro
- asignacion de proyectos.
- control de facturas
 

## Instalación

1. Clona el repositorio:
	```
	git clone https://github.com/Adrian04g/I-C_SEGUIMIENTO-OPERTIVO.git
	```
2. Instala dependencias:
	```
	- pip install django
		Django es un framework de desarollo enfocado mas en el back-end
		- https://www.djangoproject.com/
			por medio del enlace encontrara toda la documentacion del framework
	- pip install django-select2
		django-select2 es una libreria para personalizacion, en este proyecto se usa para modificar los formularios
	- pip install mysqlclient
		conector necesario para las modificaciones en la base de datos, en este caso estamos usando MySql
	```
3. Realiza migraciones:
	```
	python manage.py makemigrations
	python manage.py migrate
	```
4. Crea un superusuario:
	```
	python manage.py createsuperuser
	```
5. Ejecuta el servidor:
	```
	python manage.py runserver
	```

## Uso
- Accede a la interfaz en `http://localhost:8000/`.
- Ingresa con tu usuario y comienza a gestionar proyectos.

## Descripcion corta de django
````
1. Proyecto en django
Para desarrollar una aplicacion web en django se crea un proyecto con el siguiente comando django-admin startproject seguido del nombre del proyecto, para este proyecto se vio de esta manera (python django-admin starproject INF_CE)
Se crea una carpeta donde se desarrollara todo y una subcarpeta con el mismo nombre donde se gestiona la configuracion del proyecto
````
![alt text](READMEimg/image.png)
![alt text](READMEimg/image-1.png)
La subcarpeta se crea sin la carpeta templates ni static
````
2. app en django 
En django se le llama app a las diferntes partes de la aplicacion.
manage.py startapp seguido del nombre que quieras poner se usa para crear las diferentes app
asi se veria el comando para crear la interfaz login (python manage.py startapp login)
archivos que se crear al ejcutar el comando
- __ini__.py
	No se modifica
- admin.py
	Aqui se configura la interfaz administrativa
- apps.py
	no se modifica
- models.py
	Se crear los modelos de nuestra app
- test.py
	Aqui se hacen las pruebas unitarias
- urls.py
	Aqui se registran las urls
- views.py 
	Se maneja lo visual de las plantilla
````
![alt text](READMEimg/image4.png)
````
Nota: la carpeta migrations es una carpeta de control de version que se cre automaticamente al hacer migrationes.
- python manage.py makemigrations
- python manage.py migrate
Estos comando se utilizan cuando se crean, modifican o se elimina algun modelo
````
## Estructura del proyecto
- `INF_CE/static/`: Archivos CSS y JS personalizados.
- `INF_CE/templates/`: Plantillas HTML.
## `INF_CE/settings`: Configuracion del proyecto
![alt text](<READMEimg/Captura de pantalla 2025-09-19 142730.png>)
````
Aqui se registran las app creadas y tambien en este caso la libreria que vamos a utiizar
````
## `INF_CE/urls`: Urls a nivel proyecto
![alt text](<READMEimg/Captura de pantalla 2025-09-19 142947.png>)
````
Se regitran las urls de las apps y eeste caso la libreria que vamos a utilizar
````
## `login/`: Aplicación para el control de inicio de sesion
### login/views.py
````
Para el login no es necesario los modelos
````
#### Esta funcion obliga a el usuario a iniciar sesion
![alt text](READMEimg/image2.png)
#### Esta funcion verifica los datos del ususario al iniciar sesion
![alt text](<READMEimg/Captura de pantalla 2025-09-19 141450.png>)
````
Es necesario importar las siguientes clase que trae django
````
![alt text](<READMEimg/Captura de pantalla 2025-09-19 143446.png>)
### login/urls.py
![alt text](<READMEimg/Captura de pantalla 2025-09-19 143257.png>)

## `indexapp/`: Aplicación para trabajar los ingresos de proyectos
### indexapp/admin.py
````
En este archivo se registran los modelos y se puede configurar algunas cosas de la interfaz admin
````
### indexapp/models.py
![alt text](<READMEimg/Captura de pantalla 2025-09-19 144757.png>)
````
Este modelo representa los datos que ingresa la ejecutivas para registrar un proyecto, este modelo tiene su clase formulario en el archivo forms.py en donde se aplicar algunos estilos y funciones
````
#### class cableoperadores
![alt text](<READMEimg/Captura de pantalla 2025-09-19 145534.png>)
````
Esta clase se utiliza para tener una tabla de los cableoperadores la cual no tiene vista y los datos se manejan desde la intefaz admin 
````
#### indexapp/views.py
![alt text](<READMEimg/Captura de pantalla 2025-09-19 151900.png>)
````
Aqui se crean las diferentes vistas, en este caso se se hizo una pagina para crear y otra para ver
````
## `Asignacion/`: Aplicación para asignar los proyectos ya sea a escritorio o a terreno
### Asignacion/models.py
![alt text](<READMEimg/Captura de pantalla 2025-09-19 150441.png>)
````
Modelo para el manejo CRUD de los proyectos asignados
````
### Asignacion/views.py
![alt text](<READMEimg/Captura de pantalla 2025-09-19 150854.png>)
````
Aqui se crean las diferentes vistas, en este caso se se hizo una pagina para crear y otra para ver
````