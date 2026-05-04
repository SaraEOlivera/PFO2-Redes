
# Sistema de Gestión de Tareas con API y Base de Datos

El sistema está compuesto por un servidor API Flask que implementa una API REST con diferentes endpoints como /registro y /login. Se realiza una autenticación básica con hash de contraseñas y guarda los datos en una base de datos de SQLite

##  El servidor cuenta con lo siguiente:
- función para registrar usuarios y almacenarlos en una base de datos con contraseñas hasheadas
- función para iniciar sesión con verificación de credenciales
- las contraseñas no se almacenan en texto plano sino que se utiliza werkzeug para hashearlas

## Requisitos
- Python 3.8 o superior 
- Librerías utilizadas: flask, werkzeug, SQLite (incluída en Python) 

## Instalación del sistema

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd <PFO 2>
   ```

2. **Instalar dependencias:**
   ```bash
   pip install flask
   ```

## Cómo ejecutar el proyecto en VS Code

1. Abre carpeta del proyecto en VS Code.
2. Ejecuta el script principal:
   ```bash
   python servidor.py
   ```

## Instrucciones para probar el sistema

1. Realizar pruebas con Postman:
 - POST /registro
 - POST /login
 - GET /
- GET /tareas
   ```JSON
 	{ 
	  "usuario" : "ana",
	  "clave": "1111"
	}
      ```


## Sara E. Olivera
- Para la Segunda Práctica Formativa de Programación sobre Redes
