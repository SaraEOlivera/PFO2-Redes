
import requests 

def pedir_datos():
    datos = {
        "usuario" : input("Ingrese su nombre de usuario: "),
        "clave" : input("Ingrese su contraseña: ")
    }
    return datos

def registrarse():
    registro = "http://127.0.0.1:5000/registro"
    datos = pedir_datos()
    solicitud_registro = requests.post(registro, json=datos)
    print(solicitud_registro.text)

def login():
    login = "http://127.0.0.1:5000/login"
    datos = pedir_datos()
    solicitud_login = requests.post(login, json=datos)

    if solicitud_login.url == "http://127.0.0.1:5000/tareas":
        print(solicitud_login.text)
        return True
    else:
        print(solicitud_login.text)
        return False


def menu():
    resultado = requests.get("http://127.0.0.1:5000/")  
    print(resultado.text)
    print("Ingrese las opciones correspondientes")
    print("""
          1 - Registrarse
          2 - Iniciar sesion
          3 - Salir
    """)
    while True:
        opcion = input("Opcion: ")
        if opcion == "1":
            registrarse()
        elif opcion == "2":
            if login():
                break
        elif opcion == "3":
            print("Fin del programa")
            break
        else: 
            print("Opcion incorrecta")

if __name__ == "__main__":
    menu()