from flask import Flask, request, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def crear_db():
    try:
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        cursor.execute("""
            create table if not exists registros(
                id integer primary key autoincrement, 
                usuario text,
                clave text 
                )
            """) 
        conexion.commit()
        conexion.close()
    except sqlite3.OperationalError as e:
        print(f"No se puede completar la operacion. DB no accesible. Error: {e}")
    except sqlite3.Error as e:
        print(f"Error en la BD: {e}")
    except Exception as e:
        print(f"Hubo un error inesperado: {e}")
    finally:
        if conexion:
            conexion.close()


def guardar_usuarios(usuario, clave): 
    try:
        conexion = sqlite3.connect("usuarios.db")   
        cursor = conexion.cursor()

        cursor.execute("""
            insert into registros(usuario, clave)
            values(?,?)
            """, (usuario, clave))
    
        conexion.commit()
        conexion.close()
    except sqlite3.IntegrityError as e:
        print("Error de integridad: {e}")
    except sqlite3.Error as e:
        print(f"Error en la BD: {e}")
    except Exception as e:
        print(f"Error {e}")
    finally:
        if conexion:
            conexion.close()
    

#  instancia de aplicación Flask
servidor = Flask(__name__)

#crear ruta
@servidor.route("/") #raiz del sitio
def inicio():
    return "PFO 2 - Programacion sobre Redes "


@servidor.route("/registro", methods=['POST']) 
def registrar_usuarios():
    datos = request.json 
    usuario = datos.get("usuario")
    clave = datos.get("clave")  
    hash_psw = generate_password_hash(clave)
    guardar_usuarios(usuario, hash_psw) 
    return "Usuario registrado correctamente"


@servidor.route("/login", methods=['POST'])
def iniciar_sesion():
    conexion = None
    try:
        credenciales = request.json 

        usuario = credenciales.get("usuario")
        clave = credenciales.get("clave")
        if usuario == None or clave == None:
            return "Faltan datos"
        conexion = sqlite3.connect("usuarios.db")   
        cursor = conexion.cursor()
        cursor.execute("""
            select clave from registros where usuario = ?
        """, (usuario,))

        clave_almacenada = cursor.fetchone()
        if clave_almacenada == None:
            return "Usuario inexistente"
        else:
            check_password_hash(clave_almacenada[0], clave) #true/false

        if check_password_hash(clave_almacenada[0], clave):
            return redirect(url_for('mostrar_tareas'))
        return "Datos ingresados incorrectos"
    except sqlite3.Error as e:
        print(f"Error en la BD: {e}")
    finally:
        if conexion:
            conexion.close()



    
@servidor.route("/tareas", methods=['GET'])
def mostrar_tareas():
    return "<h1>Bienvenido</h1><h2>Estas son tus tareas</h2>"


if __name__ == "__main__":
    crear_db()
    servidor.run()

