class NodoIngrediente:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.siguiente = 0  

class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = 0  
        self.siguiente = 0  

class ListaPostres:
    def __init__(self):
        self.cabeza = 0  

    def imprimir_ingredientes(self, nombre_postre):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            print(f"Ingredientes de {nombre_postre}:")
            ingrediente_actual = postre.ingredientes
            if ingrediente_actual != 0:  
                while ingrediente_actual != 0: 
                    print(f"- {ingrediente_actual.ingrediente}")
                    ingrediente_actual = ingrediente_actual.siguiente
            else:
                print("Este postre no tiene ingredientes.")
        else:
            print(f"El postre {nombre_postre} no está en la lista.")

    def insertar_ingrediente(self, nombre_postre):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            while True:
                nuevo_ingrediente = input(f"Agrega un ingrediente para {nombre_postre} (o escribe 'salir' para terminar): ")
                if nuevo_ingrediente.lower() == 'salir':
                    break
                nuevo_nodo_ingrediente = NodoIngrediente(nuevo_ingrediente)
                if postre.ingredientes == 0:  
                    postre.ingredientes = nuevo_nodo_ingrediente
                else:
                    ingrediente_actual = postre.ingredientes
                    while ingrediente_actual.siguiente != 0:  
                        ingrediente_actual = ingrediente_actual.siguiente
                    ingrediente_actual.siguiente = nuevo_nodo_ingrediente
                print(f"Ingrediente '{nuevo_ingrediente}' añadido a {nombre_postre}.")
        else:
            print(f"El postre {nombre_postre} no está en la lista.")

    def eliminar_ingrediente(self, nombre_postre):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            ingrediente_a_eliminar = input(f"Escribe el nombre del ingrediente a eliminar de {nombre_postre}: ")
            ingrediente_actual = postre.ingredientes
            anterior = 0  
            while ingrediente_actual != 0:  
                if ingrediente_actual.ingrediente == ingrediente_a_eliminar:
                    if anterior != 0:  
                        anterior.siguiente = ingrediente_actual.siguiente
                    else:
                        postre.ingredientes = ingrediente_actual.siguiente
                    print(f"Ingrediente '{ingrediente_a_eliminar}' eliminado de {nombre_postre}.")
                    return
                anterior = ingrediente_actual
                ingrediente_actual = ingrediente_actual.siguiente
            print(f"El ingrediente '{ingrediente_a_eliminar}' no se encontró en {nombre_postre}.")
        else:
            print(f"El postre {nombre_postre} no está en la lista.")

    def dar_alta_postre(self, nombre_postre):
        nuevo_postre = NodoPostre(nombre_postre)
        self.insertar_ingrediente(nombre_postre)
        if self.cabeza == 0: 
            self.cabeza = nuevo_postre
        else:
            postre_actual = self.cabeza
            if nombre_postre < postre_actual.nombre:  
                nuevo_postre.siguiente = postre_actual
                self.cabeza = nuevo_postre
            else:
                anterior = 0  
                while postre_actual != 0 and postre_actual.nombre < nombre_postre:  
                    anterior = postre_actual
                    postre_actual = postre_actual.siguiente
                anterior.siguiente = nuevo_postre
                nuevo_postre.siguiente = postre_actual
        print(f"Postre '{nombre_postre}' añadido con sus ingredientes.")

    def dar_baja_postre(self, nombre_postre):
        postre_actual = self.cabeza
        anterior = 0  
        while postre_actual != 0:  
            if postre_actual.nombre == nombre_postre:
                if anterior != 0:  
                    anterior.siguiente = postre_actual.siguiente
                else:
                    self.cabeza = postre_actual.siguiente
                print(f"Postre '{nombre_postre}' eliminado.")
                return
            anterior = postre_actual
            postre_actual = postre_actual.siguiente
        print(f"El postre '{nombre_postre}' no se encuentra en la lista.")
        
    def buscar_postre(self, nombre_postre):
        postre_actual = self.cabeza
        while postre_actual != 0:  
            if postre_actual.nombre == nombre_postre:
                return postre_actual
            postre_actual = postre_actual.siguiente
        return 0 

    def mostrar_postres(self):
        postre_actual = self.cabeza
        if postre_actual == 0: 
            print("No hay postres en la lista.")
            return
        while postre_actual != 0: 
            print(f"Postre: {postre_actual.nombre}")
            self.imprimir_ingredientes(postre_actual.nombre)
            postre_actual = postre_actual.siguiente

    def eliminar_duplicados(self):
        if self.cabeza == 0:
            print("No hay postres en la lista para eliminar duplicados.")
            return

        postre_actual = self.cabeza
        duplicados_eliminados = 0  

        while postre_actual != 0:
            anterior = postre_actual
            siguiente_postre = postre_actual.siguiente
            while siguiente_postre != 0:
                if siguiente_postre.nombre == postre_actual.nombre:
                    anterior.siguiente = siguiente_postre.siguiente
                    duplicados_eliminados += 1
                    print(f"Postre duplicado '{siguiente_postre.nombre}' eliminado.")
                else:
                    anterior = siguiente_postre
                siguiente_postre = siguiente_postre.siguiente
            postre_actual = postre_actual.siguiente

        if duplicados_eliminados == 0:
            print("No se encontraron duplicados en la lista de postres.")
        else:
            print(f"Se eliminaron {duplicados_eliminados} duplicados de la lista de postres.")

lista_postres = ListaPostres()

def menu():
    while True:
        print("\nMenú")
        print("1. Mostrar todos los postres y sus ingredientes")
        print("2. Imprimir ingredientes de un postre")
        print("3. Insertar un ingrediente en un postre")
        print("4. Eliminar un ingrediente de un postre")
        print("5. Dar de alta un nuevo postre")
        print("6. Dar de baja un postre")
        print("7. Eliminar duplicados")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista_postres.mostrar_postres()
        elif opcion == "2":
            nombre_postre = input("Ingrese el nombre del postre: ")
            lista_postres.imprimir_ingredientes(nombre_postre)
        elif opcion == "3":
            nombre_postre = input("Ingrese el nombre del postre al que desea agregar ingredientes: ")
            lista_postres.insertar_ingrediente(nombre_postre)
        elif opcion == "4":
            nombre_postre = input("Ingrese el nombre del postre del que desea eliminar un ingrediente: ")
            lista_postres.eliminar_ingrediente(nombre_postre)
        elif opcion == "5":
            nombre_postre = input("Ingrese el nombre del nuevo postre: ")
            lista_postres.dar_alta_postre(nombre_postre)
        elif opcion == "6":
            nombre_postre = input("Ingrese el nombre del postre a eliminar: ")
            lista_postres.dar_baja_postre(nombre_postre)
        elif opcion == "7":
            lista_postres.eliminar_duplicados()
        elif opcion == "8":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()
