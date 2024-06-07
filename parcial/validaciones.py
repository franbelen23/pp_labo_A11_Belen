#Francisco Belen 46095163
#Funciones relacionadas a la Entrada , e ingresos de usuario. 

#Validar id
def validar_id(lista:list): 
    if lista: #Si hay datos dentro de la lista
        nuevo_id = lista[-1]['id'] + 1 #Incrementamos uno al ultimo valor de la lista
    else:
        nuevo_id = 1 #Inicializamos en cero
        
    return nuevo_id

#Pedir id - caso de modificaciones (NO ES NECESARIA)
def pedir_id() -> int:
    id = input('Ingrese su id: ')
    while id is None or id == '' or id.isdigit() == False or int(id) < 0:
        id = input('Ingrese correctamente su id: ')
    
    return int(id) #Retorna la variable parseada

#Validar nombre - str 20 carac. max
def validar_nombre():
    nombre = input('Ingrese su nombre [max.20 caracteres]: ') #Ingreso del usuario mediante la funcion incorporada input
    while nombre.isalpha() == False or nombre is None or nombre == '' or nombre.isdigit() or len(nombre) > 20: #Valida que este todo correcto y no se ingresen numeros y/o signos
        nombre = input('Ingrese correctamente su nombre [max.20 caracteres]: ') 

    return nombre.capitalize() #Retorna la variable con el metodo que transforma la primera letra a imprenta mayuscula

#Validar apellido - str 20 carac. max
def validar_apellido():
    apellido = input('Ingrese su apellido [max.20 caracteres]: ') #Ingreso del usuario mediante la funcion incorporada input
    while apellido.isalpha() == False or apellido is None or apellido == '' or len(apellido) > 20:  #Valida que este todo correcto y no se ingresen numeros y/o signos
        apellido = input('Ingrese correctamente su apellido [max.20 caracteres]: ') 

    return apellido.capitalize()  #Retorna la variable con el metodo que transforma la primera letra a imprenta mayuscula

#Validar edad - int > 1 , < 120 años
def validar_edad():
    edad = input('Ingrese su edad [1-120]: ') #Ingreso del usuario mediante la funcion incorporada input
    while edad.isdigit() == False or int(edad) < 1 or int(edad) > 120 or edad is None or edad == '': #Valida y compara que no se ingresen ni letras ni simbolos y respeta los limites
        edad = input('Ingrese correctamente su edad [1-120]: ')
    
    return int(edad) #Retorna la variable parseada

#Validar altura - int > 30 , < 230 cm
def validar_altura():
    altura = input('Ingrese su altura en cm [30-230]: ') #Ingreso del usuario mediante la funcion incorporada input
    while altura.isdigit() == False or int(altura) > 230 or int(altura) < 30 or altura is None or altura == '': #Valida y compara que no se ingresen ni letras ni simbolos y respeta los limites
        altura = input('Ingrese correctamente su altura en cm [30-230]: ')
    
    return int(altura) #Retorna la variable parseada

#Validar peso - float > 10, < 300 kg 
def validar_peso():
    peso = input('Ingrese su peso en kg [10-300]: ') #Ingreso del usuario mediante la funcion incorporada input
    while peso.isdecimal() == False or float(peso) < 10 or float(peso) > 300 or peso is None or peso == '':
        peso = input('Ingrese correctamente su peso en kg [10-300]: ')
    peso = float(peso) #Variable parseada
    
    return round(peso,2) #Redondea el flotante en 2 decimales luego de la coma

#Validar DNI - int, > 0, < 47 millones
def validar_dni():
    dni = input('Ingrese su DNI [0-47000000]: ') #Ingreso del usuario mediante la funcion incorporada input
    while dni.isdigit() == False and int(dni) < 0 or int(dni) > 47000000 or dni is None or dni == '': #Valida y compara que no se ingresen ni letras ni simbolos y respeta los limites
        dni = input('Ingrese correctamente su DNI [0-47000000]: ')
    
    return int(dni) #Retorna la variable parseada

#Validar grupo sanguineo str [A - B - AB - 0] +/-
def validar_grupo_sanguineo():
    letra = input('Ingrese su grupo sanguineo [A - B - AB - 0]: ').upper() #Ingreso del usuario mediante la funcion incorporada input y metodo upper para transformar la letra a Imprenta mayusucula
    while letra not in ('A','B','AB','0') or letra is None or letra == '' : #Valida que este entre los caracteres que se pide unicamente
        letra = input('Ingrese correctamente su grupo sanguineo [A - B - AB - 0]: ')
    
    signo = input('Ingrese signo [+,-]: ')
    while signo not in ('+','-') or signo is None or signo == '' :
        signo = input('Ingrese correctamente su signo [+,-]: ') #Valida que este entre los simbolos que se pide unicamente
    
    grupo_sanguineo = letra+signo #Concatena los valores pedidos
    
    return grupo_sanguineo

#Bubble sort - ordenar pacientes
def validar_parametro_comparacion():
    parametro_comparacion = input('Ingrese el valor que quiere usar para comparar: [A.nombre-B.apellido-C.altura-D.grupo sanguíneo]').upper() #Ingreso del usuario mediante la funcion incorporada input y metodo upper para transformar la letra a Imprenta mayusucula
    while parametro_comparacion not in ('A' or 'B' or 'C' or 'D') or parametro_comparacion is None or parametro_comparacion == '': #Valida que este entre los caracteres que se pide unicamente
        parametro_comparacion = input('Ingrese correctamente el valor que quiere usar para comparar: [A.nombre-B.apellido-C.altura-D.grupo sanguíneo]').upper()

    return parametro_comparacion
        
def validar_parametro_asc_des():
    parametro_ascendente_descendente = input('Ingrese el orden en que quiere ordenarlo: [A.ascendente-B.descendente]').upper() #Ingreso del usuario mediante la funcion incorporada input y metodo upper para transformar la letra a Imprenta mayusucula
    while parametro_ascendente_descendente not in ('A' or 'B') or parametro_ascendente_descendente is None or parametro_ascendente_descendente == '': #Valida que este entre los caracteres que se pide unicamente
        parametro_ascendente_descendente = input('Ingrese correctamente el orden en que quiere ordenarlo: [A.ascendente-B.descendente]').upper()

    return parametro_ascendente_descendente

def validar_tipo():
    tipo = input('Ingrese el tipo de promedio que quiere realizar [A.altura-B.peso-C.edad]: ').upper() #Ingreso del usuario mediante la funcion incorporada input y metodo upper para transformar la letra a Imprenta mayusucula
    while tipo not in ('A' or 'B' or 'C') or tipo is None or tipo == '': #Valida que este entre los caracteres que se pide unicamente
        tipo = input('Ingrese correctamente el tipo de promedio que quiere realizar [A.altura-B.peso-C.edad]: ').upper()
    
    return tipo