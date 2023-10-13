import requests
class Usuarios:
    def __init__(self, nombreUsuario, contraseña, edad, saldo):
        self.nombreUsuario = nombreUsuario
        self.contraseña = contraseña
        self.edad = edad
        self.saldo = saldo

    def DesplegarDatosUsuario(self):
        pass

    def Recompensa(self, costo, saldo):
        return 0

    def __del__(self):
        print("La memoria del objeto Usuario se ha liberado...")

class Estudiante(Usuarios):
    def __init__(self, Escuela, Matricula, Grado, nombreUsuario, contraseña, edad, saldo):
        super().__init__(nombreUsuario, contraseña, edad, saldo)
        self.Escuela = Escuela
        self.Matricula = Matricula
        self.Grado = Grado

    def Descuento(self, costo):
        descuento = costo * 0.50
        return descuento

    def Recompensa(self, costo):
        recompensa = costo * 0.05
        return recompensa

    def DesplegarDatosUsuario(self):
        print(f"Username: {self.nombreUsuario} Age: {self.edad} Money: {self.saldo} School {self.Escuela} Grade {self.Grado} School Number {self.Matricula}")

    def __del__(self):
        print("Se ha liberado la memoria de la clase Estudiante...")

class TerceraEdad(Usuarios):
    def __init__(self, nombreUsuario, contraseña, edad, saldo):
        super().__init__(nombreUsuario, contraseña, edad, saldo)

    def Descuento(self, costo):
        descuento = costo * 0.50
        return descuento

    def Recompensa(self, costo):
        recompensa = costo * 0.05
        return recompensa

    def DesplegarDatosUsuario(self):
        print(f"Username: {self.nombreUsuario} Age: {self.edad} Money: {self.saldo}")

    def __del__(self):
        print("La memoria de la clase tercera edad ha sido liberada...")

class UsuarioGeneral(Usuarios):
    def __init__(self, nombreUsuario, contraseña, edad, saldo):
        super().__init__(nombreUsuario, contraseña, edad, saldo)

    def Recompensa(self, costo):
        recompensa = costo * 0.05
        return recompensa

    def DesplegarDatosUsuario(self):
        print(f"Username: {self.nombreUsuario} Age: {self.edad} Money: {self.saldo}")

    def __del__(self):
        print("La memoria del objeto Usuario General ha sido liberada...")

def obtener_ruta(origin, destination):
    api_url = "https://www.mapquestapi.com/directions/v2/route"
    key = "iSbemi1OPlV3aOG59FxzsiHJd67rSOA9"

    params = {
        "key": key,
        "from": origin,
        "to": destination,
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    return data

opc = 'y'

while opc != 'n':
    print("Bienvenido a MetroMoney")
    opc2 = int(input("1. Crear Usuario: "))

    if opc2 == 1:
        username = input("Introduzca el nombre del usuario: ")
        password = input("Introduzca la contraseña que desea utilizar: ")
        age = int(input("Introduzca su edad: "))
        u1 = Usuarios(username, password, age, 0)

        opc3 = int(input("Escoja el tipo de usuario que es: 1. General 2. Estudiante 3. Tercera Edad: "))

        if opc3 == 1:
            ug1 = UsuarioGeneral(u1.nombreUsuario, u1.contraseña, u1.edad, 0)
            opc4 = int(input("Elija la opción que desea ejecutar: 1. Transportes 2. Usuario 3. Wallet: "))

            if opc4 == 1:
                opc5 = int(input("Menú de rutas: 1. Ruta ITT-C99 Ruta 2. Ruta ITT-T22202: "))

                if opc5 == 1:
                    origin = "Tijuana, Bugambilia 99"
                    destination = "Tijuana, Instituto Tecnologico de Tijuana Tomas Aquino"
                    ruta = obtener_ruta(origin, destination)

                    if ruta["info"]["statuscode"] == 0:
                        trip_duration = ruta["route"]["formattedTime"]
                        distance = ruta["route"]["distance"] * 1.61

                        print("=================================================================================")
                        print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
                        print(f"Duración del viaje: {trip_duration}.")
                        print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
                        print("=================================================================================")
                        print("Indicaciones del viaje")

                        for step in ruta["route"]["legs"][0]["maneuvers"]:
                            distance_remaining = distance - step["distance"] * 1.61
                            print(step["narrative"] + " (" + str("{:.2f}".format(distance_remaining) + " Km faltantes)"))
                            distance = distance_remaining
                    else:
                        print("Hubo un error al obtener la ruta.")
                elif opc5 == 2:
                    origin = "Tijuana, Atotonilco 22206"
                    destination = "Tijuana, Instituto Tecnologico de Tijuana Tomas Aquino"
                    ruta = obtener_ruta(origin, destination)

                    if ruta["info"]["statuscode"] == 0:
                        trip_duration = ruta["route"]["formattedTime"]
                        distance = ruta["route"]["distance"] * 1.61

                        print("=================================================================================")
                        print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
                        print(f"Duración del viaje: {trip_duration}.")
                        print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
                        print("=================================================================================")
                        print("Indicaciones del viaje")

                        for step in ruta["route"]["legs"][0]["maneuvers"]:
                            distance_remaining = distance - step["distance"] * 1.61
                            print(step["narrative"] + " (" + str("{:.2f}".format(distance_remaining) + " Km faltantes)"))
                            distance = distance_remaining
                    else:
                        print("Hubo un error al obtener la ruta.")
            elif opc4 == 2:
                ug1.DesplegarDatosUsuario()
            elif opc4 == 3:
                pass
            else:
                print("La opción que introdujo no está disponible o no es correcta.")

        elif opc3 == 2:
            escuela = input("Introduzca el nombre de la escuela: ")
            matricula = input("Introduzca la matrícula: ")
            grado = input("Introduzca el grado: ")
            E1 = Estudiante(escuela, matricula, grado, u1.nombreUsuario, u1.contraseña, u1.edad, 0)

            opc4 = int(input("Elija la opción que desea ejecutar: 1. Transportes 2. Usuario 3. Wallet: "))

            if opc4 == 1:
                opc5 = int(input("Menú de rutas: 1. Ruta ITT-C99 Ruta 2. Ruta ITT-T22202: "))
                if opc5 == 1:
                    origin = "Tijuana, Bugambilia 99"
                    destination = "Tijuana, Instituto Tecnologico de Tijuana Tomas Aquino"
                    ruta = obtener_ruta(origin, destination)

                    if ruta["info"]["statuscode"] == 0:
                        trip_duration = ruta["route"]["formattedTime"]
                        distance = ruta["route"]["distance"] * 1.61

                        print("=================================================================================")
                        print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
                        print(f"Duración del viaje: {trip_duration}.")
                        print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
                        print("=================================================================================")
                        print("Indicaciones del viaje")

                        for step in ruta["route"]["legs"][0]["maneuvers"]:
                            distance_remaining = distance - step["distance"] * 1.61
                            print(step["narrative"] + " (" + str("{:.2f}".format(distance_remaining) + " Km faltantes)"))
                            distance = distance_remaining
                    else:
                        print("Hubo un error al obtener la ruta.")
                elif opc5 == 2:
                    origin = "Tijuana, Atotonilco 22206"
                    destination = "Tijuana, Instituto Tecnologico de Tijuana Tomas Aquino"
                    ruta = obtener_ruta(origin, destination)

                    if ruta["info"]["statuscode"] == 0:
                        trip_duration = ruta["route"]["formattedTime"]
                        distance = ruta["route"]["distance"] * 1.61

                        print("=================================================================================")
                        print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
                        print(f"Duración del viaje: {trip_duration}.")
                        print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
                        print("=================================================================================")
                        print("Indicaciones del viaje")

                        for step in ruta["route"]["legs"][0]["maneuvers"]:
                            distance_remaining = distance - step["distance"] * 1.61
                            print(step["narrative"] + " (" + str("{:.2f}".format(distance_remaining) + " Km faltantes)"))
                            distance = distance_remaining
                    else:
                        print("Hubo un error al obtener la ruta.")
                else:
                    print("Opción no válida...")
            elif opc4 == 2:
                E1.DesplegarDatosUsuario()
            elif opc4 == 3:
                pass
            else:
                print("La opción que introdujo no está disponible o no es correcta.")

        elif opc3 == 3:
            if u1.edad >= 60:
                T1 = TerceraEdad(u1.nombreUsuario, u1.contraseña, u1.edad, 0)

                opc4 = int(input("Elija la opción que desea ejecutar: 1. Transportes 2. Usuario 3. Wallet: "))

                if opc4 == 1:
                    opc5 = int(input("Menú de rutas: 1. Ruta ITT-C99 Ruta 2. Ruta ITT-T22202: "))

                    if opc5 == 1:
                        origin = "Tijuana, Bugambilia 99"
                        destination = "Tijuana, Instituto Tecnologico de Tijuana Tomas Aquino"
                        ruta = obtener_ruta(origin, destination)

                        if ruta["info"]["statuscode"] == 0:
                            trip_duration = ruta["route"]["formattedTime"]
                            distance = ruta["route"]["distance"] * 1.61

                            print("=================================================================================")
                            print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
                            print(f"Duración del viaje: {trip_duration}.")
                            print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
                            print("=================================================================================")
                            print("Indicaciones del viaje")

                            for step in ruta["route"]["legs"][0]["maneuvers"]:
                                distance_remaining = distance - step["distance"] * 1.61
                                print(step["narrative"] + " (" + str("{:.2f}".format(distance_remaining) + " Km faltantes)"))
                                distance = distance_remaining
                        else:
                            print("Hubo un error al obtener la ruta.")
                    elif opc5 == 2:
                        origin = "Tijuana, Atotonilco 22206"
                        destination = "Tijuana, Instituto Tecnologico de Tijuana Tomas Aquino"
                        ruta = obtener_ruta(origin, destination)

                        if ruta["info"]["statuscode"] == 0:
                            trip_duration = ruta["route"]["formattedTime"]
                            distance = ruta["route"]["distance"] * 1.61

                            print("=================================================================================")
                            print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
                            print(f"Duración del viaje: {trip_duration}.")
                            print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
                            print("=================================================================================")
                            print("Indicaciones del viaje")

                            for step in ruta["route"]["legs"][0]["maneuvers"]:
                                distance_remaining = distance - step["distance"] * 1.61
                                print(step["narrative"] + " (" + str("{:.2f}".format(distance_remaining) + " Km faltantes)"))
                                distance = distance_remaining
                        else:
                            print("Hubo un error al obtener la ruta.")
                else:
                    print("Opción no válida...")
            else:
                print("Lo sentimos, la opción Tercera Edad está disponible solo para personas mayores de 60 años.")
        else:
            print("La opción que introdujo no está disponible o no es correcta.")

        opc = input("Desea reiniciar el programa? (y/n): ")
    else:
        print("El dato que introdujo no es válido. Presione <ENTER> para continuar.")
        opc = input("Desea volver a repetir el programa? (y/n): ")
