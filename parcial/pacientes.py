#Francisco Belen 46095163
#Funciones relacionadas con el entorno pacientes
from validaciones import * #Importamos las validaciones realizadas

#Dar de alta
def dar_alta(lista_pacientes : list):
    nuevo_paciente = {}
    #Pedimos todos los datos con las validaciones realizadas anteriormente y lo guardamos en la variable correspondiente
    while True:
        id = validar_id(lista_pacientes)
        nuevo_paciente['id'] = id

        nombre = validar_nombre()
        nuevo_paciente['nombre'] = nombre
    
        apellido = validar_apellido()
        nuevo_paciente['apellido'] = apellido
        
        edad = validar_edad()
        nuevo_paciente['edad'] = edad
        
        altura = validar_altura()
        nuevo_paciente['altura'] = altura
        
        peso = validar_peso()
        nuevo_paciente['peso'] = peso
        
        dni = validar_dni()
        nuevo_paciente['dni'] = dni
        
        grupo_sanguineo = validar_grupo_sanguineo()
        nuevo_paciente['grupo'] = grupo_sanguineo
        
        lista_pacientes.append(nuevo_paciente) #Agregamos el diccionario paciente a la lista de diccionarios 
        
        respuesta = input('Desea seguir ingresando datos? ingrese si para continuar: ')
        if respuesta.lower() == 'si':
            continue
        else:
            break
    
#Modificar
def modificar_persona(lista:list)->str:
    
    retorno = ''
    bandera_existe = False
    dni = validar_dni()
    for i in range(len(lista)): #Para cada iteracion dentro de la lista 
        if dni == lista[i]['dni']: #Buscamos si hay un dni en la lista
            bandera_existe = True  #Transformamos el valor de la bandera para indicar que existe
            while True:
                opcion_elegida = input('Elija que dato desea modificar: [nombre-apellido-edad-altura-peso-dni-grupo] (Salir: [e]) ')
                match opcion_elegida:
                    case 'nombre':
                        nombre = validar_nombre()
                        lista[i]['nombre'] = nombre
                        retorno += 'Se modificó el nombre' 
                    case 'apellido':
                        apellido = validar_apellido()
                        lista[i]['apellido'] = apellido
                        retorno += 'Se modificó el apellido' 
                    case 'edad':
                        edad = validar_edad()
                        lista[i]['puesto'] = edad
                        retorno += 'Se modificó la edad' 
                    case 'peso':
                        peso = validar_peso()
                        lista[i]['salario'] = peso
                        retorno += 'Se modificó el peso' 
                    case 'dni':
                        dni = validar_dni()
                        lista[i]['dni'] = dni
                        retorno += 'Se modificó el dni'
                    case 'grupo':
                        grupo_sanguineo = validar_grupo_sanguineo()
                        lista[i]['grupo'] = grupo_sanguineo
                    case 'dni':
                        dni = validar_dni()
                        lista[i]['dni'] = dni
                    case 'e':
                        break
                    case _:
                        print('Opcion no valida, intente de nuevo')
                break #Break dentro del bucle ya que quiere decir que se encontro un valor y no necesita seguir iterando 
        
    if bandera_existe == False: #En el caso que no se haya transformado la bandera quiere decir que no lo encontro
        retorno = 'La persona no existe, no se pudo modificar'
    else:
        if retorno == '':
            retorno = 'No se modificó nada'
    
    return retorno

#Eliminar
def eliminar_paciente(lista:list)->str: #Devuelve un str para unicamente indicar que se realizó la funcion 
    dni = validar_dni()
    persona_a_eliminar = None #Variable donde vamos a guardar la persona que tenga el dni ingresado
    retorno = ''
    
    for persona in lista:
        if dni == persona['dni']:
            persona_a_eliminar = persona
            break
    
    if persona_a_eliminar:
        lista.remove(persona_a_eliminar) #Metodo para eliminar al paciente que se haya elegido
        retorno = 'Se elimino a correctamente'
    else:
        retorno = 'No se encontro la persona'

    return retorno

#Mostrar todos
def mostrar_pacientes(lista:list):
    print('********************************************************')
    print(f'|Nombre|Apellido|Edad|Altura|Peso|DNI|Grupo sanguíneo|')
    for i in range(len(lista)): #Dentro de cada iteracion agregamos los valores de las llaves del diccionario de cada indice
        print(f'|{lista[i]["nombre"]}|{lista[i]["apellido"]}|{lista[i]["edad"]}|{lista[i]["altura"]}|{lista[i]["peso"]}|{lista[i]["dni"]}|{lista[i]["grupo"]}|')
    print('********************************************************')

#bubble sort 

#Manera ascendente
def bubble_sort_ascendente(lista_pacientes, valor_a_comparar):
    pacientes = len(lista_pacientes) #Lista con diccionarios 
    for i in range(pacientes): #Datos dentro de ese diccionario, nombre,apellido,altura,grupo sanguineo,etc
        for j in range(0, pacientes-i-1):
            # Comparamos dos pacientes según la clave dada
            if lista_pacientes[j][valor_a_comparar] > lista_pacientes[j+1][valor_a_comparar]:
                # Intercambiamos si están en el orden incorrecto
                lista_pacientes[j], lista_pacientes[j+1] = lista_pacientes[j+1], lista_pacientes[j]

    return lista_pacientes

#Manera descendente
def bubble_sort_descendente(lista_pacientes, valor_a_comparar):
    pacientes = len(lista_pacientes) 
    for i in range(pacientes): 
        for j in range(0, pacientes-i-1):
            # Comparamos dos pacientes según la clave dada
            if lista_pacientes[j][valor_a_comparar] < lista_pacientes[j+1][valor_a_comparar]:
                # Intercambiamos si están en el orden incorrecto
                lista_pacientes[j], lista_pacientes[j+1] = lista_pacientes[j+1], lista_pacientes[j]

    return lista_pacientes

#menu ordenar pacientes
def ordenar_pacientes(lista:list)->list:
    parametro_comparacion = validar_parametro_comparacion()
    parametro_ascendente_descendente = validar_parametro_asc_des()
 
    match parametro_comparacion: 
        case 'A': #nombre
            if parametro_ascendente_descendente == 'A': #ascendente
                lista_ordenada = bubble_sort_ascendente(lista,'nombre') 
                for linea in lista_ordenada:
                    print(linea)
            else:
                lista_ordenada = bubble_sort_descendente(lista,'nombre') #descendente
                for linea in lista_ordenada:
                    print(linea)
        case 'B': #apellido
            if parametro_ascendente_descendente == 'A':
                lista_ordenada = bubble_sort_ascendente(lista,'apellido') #ascendente
                for linea in lista_ordenada:
                    print(linea)
            else:
                lista_ordenada = bubble_sort_descendente(lista,'apellido') #descendente
                for linea in lista_ordenada:
                    print(linea)
        case 'C': #altura 
            if parametro_ascendente_descendente == 'A':
                lista_ordenada = bubble_sort_ascendente(lista,'altura') #ascendente
                for linea in lista_ordenada:
                    print(linea)
            else:
                lista_ordenada = bubble_sort_descendente(lista,'altura') #descendente
                for linea in lista_ordenada:
                    print(linea)
        case 'D': #grupo sanguineo
            if parametro_ascendente_descendente == 'A':
                lista_ordenada = bubble_sort_ascendente(lista,'grupo') #ascendente
                for linea in lista_ordenada:
                    print(linea)
            else:
                lista_ordenada = bubble_sort_descendente(lista,'grupo') #descendente
                for linea in lista_ordenada:
                    print(linea)
        
#Buscar por DNI
def buscar_por_dni(lista:list):
    paciente_encontrado = False
    dni = int(input('Ingrese su dni: '))
    for i in range(len(lista)):
        if dni == lista[i]['dni']:
            paciente_encontrado = True
            print('Se encontro al paciente')
            print(f'Datos, Nombre: {lista[i]["nombre"]}, Apellido: {lista[i]["apellido"]}, Edad: {lista[i]["edad"]}, Altura: {lista[i]["altura"]}, Peso: {lista[i]["peso"]}, DNI: {lista[i]["dni"]}, Grupo sanguineo: {lista[i]["grupo"]}')
    
    if paciente_encontrado == False:
        print('No se encontro al paciente')
    
#Calculo universal
def promediar_general(lista, tipo):
    acumulador = 0
    contador = 0
    
    for i in range(len(lista)):
        acumulador += lista[i][tipo]
        contador += 1

    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = 0.00
    
    return round(promedio,2)

    
#Calcular promedio (altura-edad-peso)
def calcular_promedio(lista:list):
    while True:
        tipo = validar_tipo()
        
        match tipo:
            case 'A':
                promedio = promediar_general(lista,'altura')
                print(promedio)
            case 'B':
                promedio = promediar_general(lista,'peso')
                print(promedio)
            case 'C':
                promedio = promediar_general(lista,'edad')
                print(promedio)
        
        respuesta = input('Desea seguir observando promedios? ingrese si para continuar: ')
        if respuesta != 'si':
            break
    
#Pasar lista a archivo csv !!

#Calcular donantes
def calcular_donantes(lista:list):  # D.(A/B/AB/0).(P/N) 
    d_a_p = 0 #DONANTE A+
    d_a_n = 0 #DONANTE A-
    d_b_p = 0 #DONANTE B+
    d_b_n = 0 #DONANTE B-
    d_ab_p = 0 #DONANTE AB+
    d_ab_n = 0 #DONANTE AB-
    d_c_p = 0 #DONANTE 0+
    d_c_n = 0 #DONANTE 0-
    for i in range(len(lista)):
        grupo = lista[i]['grupo']
        match grupo:
            case 'A+':
                d_a_p += 1
                d_ab_p += 1
            case 'A-':
                d_a_p += 1
                d_a_n += 1
                d_ab_p += 1
                d_ab_n += 1
            case 'B+':
                d_b_p += 1
                d_ab_p += 1
            case 'B-':
                d_b_n += 1
                d_b_p += 1
                d_ab_n += 1
                d_ab_p += 1
            case 'AB+':
                d_ab_p += 1
            case 'AB-':
                d_ab_p += 1
                d_ab_n += 1
            case '0+':
                d_a_p += 1
                d_b_p += 1
                d_ab_p += 1
                d_c_p += 1
            case '0-':
                d_a_p += 1
                d_a_n += 1
                d_b_p += 1
                d_b_n += 1
                d_ab_p += 1
                d_ab_n += 1
                d_c_p += 1
                d_c_n += 1

    print('Tabla de donantes')
    print('*******************************************')
    print('| A+ | A- | B+ | B- | AB+ | AB- | 0+ | 0- |')
    print(f'| {d_a_p}  | {d_a_p}  | {d_b_p}  | {d_b_n}  | {d_ab_p}   | {d_ab_n}   | {d_c_p}  | {d_c_n}  |')
    print('*******************************************')
    
#PARCIAL 7/6 
#Mostrar grupo sanguineo
def mostrar_por_grupo_sanguineo(lista_pacientes:list):
    c_a_p = 0 #Contador A+
    c_a_n = 0 #Contador A-
    c_b_p = 0 #Contador B+
    c_b_n = 0 #Contador B-
    c_ab_p = 0 #Contador AB+
    c_ab_n = 0 #Contador AB-
    c_c_p = 0 #Contador 0+
    c_c_n = 0 #Contador 0-
    mensaje_ap = 'A+: '
    mensaje_an = 'A-: ' 
    mensaje_bp = 'B+: ' 
    mensaje_bn = 'B-: ' 
    mensaje_abp = 'AB+: ' 
    mensaje_abn = 'AB-: ' 
    mensaje_cp = '0+: ' 
    mensaje_cn = '0-: '  
    lista_por_grupos = []
    for i in range(len(lista_pacientes)):
            grupo = lista_pacientes[i]['grupo']
            nombre = lista_pacientes[i]['nombre']
            apellido = lista_pacientes[i]['apellido']
            match grupo:
                case 'A+':
                    c_a_p += 1
                    mensaje_ap += f'{nombre} {apellido},'
                case 'A-':
                    c_a_n += 1
                    mensaje_an += f'{nombre} {apellido},'
                case 'B+':
                    c_b_p += 1
                    mensaje_bp += f'{nombre} {apellido},'
                case 'B-':
                    c_b_n += 1
                    mensaje_bn += f'{nombre} {apellido},'
                case 'AB+':
                    c_ab_p += 1
                    mensaje_abp += f'{nombre} {apellido},'
                case 'AB-':
                    c_ab_n += 1
                    mensaje_abn += f'{nombre} {apellido},'
                case '0+':
                    c_c_p += 1
                    mensaje_cp += f'{nombre} {apellido},'
                case '0-':  
                    c_c_n += 1
                    mensaje_cn += f'{nombre} {apellido},'
                    
    if c_a_p == 0:
        pass
    else:
        mensaje_ap += f'\nTotal de pacientes con sangre A+: {c_a_p}'
        lista_por_grupos.append(mensaje_ap)
    if c_a_n == 0:
        pass
    else:
        mensaje_an += f'\nTotal de pacientes con sangre A-: {c_a_n}'
        lista_por_grupos.append(mensaje_an)
    if c_b_p == 0:
        pass
    else:
        mensaje_bp += f'\nTotal de pacientes con sangre B+: {c_b_p}'
        lista_por_grupos.append(mensaje_bp)
    if c_b_n == 0:
        pass
    else:
        mensaje_bn += f'\nTotal de pacientes con sangre B-: {c_b_n}'
        lista_por_grupos.append(mensaje_bn)
    if c_ab_p == 0:
        pass
    else:
        mensaje_abp += f'\nTotal de pacientes con sangre AB+: {c_ab_p}'
        lista_por_grupos.append(mensaje_abp)
    if c_ab_n == 0:
        pass
    else:
        mensaje_abn += f'\nTotal de pacientes con sangre AB-: {c_ab_n}'
        lista_por_grupos.append(mensaje_abn)
    if c_c_p == 0:
        pass
    else:
        mensaje_cp += f'\nTotal de pacientes con sangre 0+: {c_c_p}'
        lista_por_grupos.append(mensaje_cp)
    if c_c_n == 0:
        pass
    else:
        mensaje_cn += f'\nTotal de pacientes con sangre 0-: {c_c_n}'
        lista_por_grupos.append(mensaje_cn)
    
    return lista_por_grupos
