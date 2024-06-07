#Francisco Belen 46095163
from pacientes import * #Importamos las funciones del menú

flag_datos_ingresados = False #Bandera para permitir o no las opciones de la 2 a la 7
lista_pacientes = [] #Lista donde se guardaran los diccionarios
while True:
        print("\nMENU CLINICA NANI")
        print("A. DAR ALTA PACIENTE/S")
        print("B. MODIFICAR PACIENTE/S")
        print("C. ELIMINAR PACIENTE/S")
        print("D. MOSTRAR PACIENTE/S")
        print("E. ORDENAR PACIENTE/S")
        print("F. BUSQUEDA POR DNI")
        print("G. CALCULAR PROMEDIO")
        print("H. CALCULAR DONANTES")
        print("I. SALIR")
        
        opcion = input("Seleccione una opción: ").upper()
        
        #Estructura de control match para manejar las opciones 
        match opcion:
            case 'A': 
                dar_alta(lista_pacientes)
                flag_datos_ingresados = True
            case 'B': 
                if flag_datos_ingresados == True:
                    retorno = modificar_persona(lista_pacientes)
                    print(retorno)
                else:
                    print("Debe ingresar datos")
            case 'C': 
                if flag_datos_ingresados == True: 
                    retorno = eliminar_paciente(lista_pacientes)
                    print(retorno)
                else:
                    print("Debe ingresar datos")
            case 'D': 
                if flag_datos_ingresados == True:
                    mostrar_pacientes(lista_pacientes)
                else:
                    print("Debe ingresar datos")
            case 'E': 
                if flag_datos_ingresados == True:
                    ordenar_pacientes(lista_pacientes)
                else:
                    print("Debe ingresar datos")
            case 'F': 
                if flag_datos_ingresados == True:
                    buscar_por_dni(lista_pacientes)
                else:
                    print("Debe ingresar datos")
            case 'G': 
                if flag_datos_ingresados == True:
                    calcular_promedio(lista_pacientes)
                else:
                    print("Debe ingresar datos")
            case 'H': 
                if flag_datos_ingresados == True:
                    calcular_donantes(lista_pacientes)
                else:
                    print("Debe ingresar datos")
            case 'I':
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

