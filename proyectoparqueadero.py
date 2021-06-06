import json

#FUNCIONES

def datos(infousuario): 
    #Toma una lista. Agrega a una lista el nombre y el número de identificación. Solicita información adicional (tipo de usuario, placa,
    #tipo de vehículo, plan de pagos) para agregarla a una lista que contiene los datos del usuario. Cabe resaltar que para evitar que haya
    #inconvenientes en tipos de datos string (mayúsculas, tildes, errores), cada tipo de usuario, vehiculo y plan de pago se identifica con un
    #número que después por medio de condicionales, se pasará a un string. Al final, retorna la lista.
    infousuario.append(nombre)
    infousuario.append(identificacion)
    tu = int(input('Opciones tipos de usuarios: \n 1. Para Estudiante \n 2. Para Profesor \n 3. Para Personal Administrativo \nDigite el número según el tipo de usuario: '))
    if tu==1:
        tipousuario = 'Estudiante'
    elif tu==2:
        tipousuario = 'Profesor'
    else:
        tipousuario = 'Personal Administrativo'
    infousuario.append(tipousuario)
    placa = input('Ingrese la placa del vehículo: ')
    infousuario.append(placa)
    tv = int(input('Opciones para tipo de vehículo: \n 1. Para Automóvil \n 2. Para Automóvil Eléctrico \n 3. Para Motocicleta \n 4. Para Discapacitado\nDigite el número según el tipo de vehículo: '))
    if tv==1:
        tipovehiculo = 'Automóvil'
    elif tv==2:
        tipovehiculo = 'Automóvil Eléctrico'
    elif tv==3:
        tipovehiculo = 'Motocicleta'
    else:
        tipovehiculo = 'Discapacitado'
    infousuario.append(tipovehiculo)
    pp = int(input('Opciones para plan de pago: \n 1. Mensual \n 2. Diario\nDigite el número de acuerdo al plan de pago: '))
    if pp==1:
        planpago = 'Mensualidad'
    else:
        planpago = 'Diario'
    infousuario.append(planpago)
    return infousuario

def pisosdisp(np, uv, tv):
    #Toma la matriz del piso, la matriz con la ubicación y el tipo de vehículo. Cuenta el número de cupos disponibles en un 
    #piso. Para ello entra en un primer ciclo donde recorre las listas y en el segundo, los elementos de las listas; valida si la posición 
    #en la matriz de los pisos esta disponible y si el número en la matriz de la ubicación de los vehículos pertenece al tipo de vehículo 
    #que desee ingresar, si es así lo suma. Retorna el número de cupos.
    cupos = 0
    i1 = 1
    iu1 = 0
    for x in range(len(uv)):
        i2 = 1
        iu2 = 0
        for x in range(10):
            if tv==4:
                if np[i1][i2]=='0' and (uv[iu1][iu2]==1 or uv[iu1][iu2]==tv):
                    cupos+=1
            elif tv==2:
                if np[i1][i2]=='0' and (uv[iu1][iu2]==1 or uv[iu1][iu2]==tv):
                    cupos+=1
            else:
                if np[i1][i2]=='0' and uv[iu1][iu2]==tv:
                    cupos+=1
            i2+=1
            iu2+=1
        i1+=1
        iu1+=1
    return cupos

def posibleubicacion(mp, mu, tv):
    #Toma la matriz de un piso, la matriz con las ubicación y el tipo de vehículo. Empieza con una matriz de prueba con "0"; el tamaño
    #dependerá del piso, ya que el piso 6 es de menor tamaño. Recorre por un ciclo las litas y por el otro los elementos de la lista. Si la 
    #posición esta ocupada o no pertenece al tipo de vehículo, reemplaza con una "X" esa posición en la matriz de prueba, lo que quiere decir 
    #que no esta disponible ese lugar. Imprime la matriz de prueba mostrando las posiciones con "0" y "X".
    if mp==p6:
        md = [
        ['','A','B','C','D','E','F','G','H','I','J'],
        [ 1 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 2 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 3 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 4 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 5 ,'0','0','0','0','0','0','0','0','0','0'],
        ]
    else:
        md = [
        ['','A','B','C','D','E','F','G','H','I','J'],
        [ 1 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 2 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 3 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 4 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 5 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 6 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 7 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 8 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 9 ,'0','0','0','0','0','0','0','0','0','0'],
        [ 10 ,'0','0','0','0','0','0','0','0','0','0'],
        ]
    i1 = 1
    iu1 = 0
    for x in range (len(mu)):
        i2 = 1
        iu2 = 0
        for x in range (10):
            if tv==4:
                if mp[i1][i2]=='0' and (tv!=mu[iu1][iu2] and mu[iu1][iu2]!=1):
                    md[i1][i2]='X'
            elif tv==2:
                if mp[i1][i2]=='0' and (tv!=mu[iu1][iu2] and mu[iu1][iu2]!=1):
                    md[i1][i2]='X'
            else:
                if mp[i1][i2]=='0' and tv!=mu[iu1][iu2]:
                    md[i1][i2]='X'
            if mp[i1][i2]=='X':
                md[i1][i2]='X'
            i2+=1
            iu2+=1
        i1+=1
        iu1+=1
    for r in md:
        print(r)

def columnas (c):
    #Toma una letra que ingresó el usuario. Convierte la letra de la ubicación a un número. Se hace con el fin de posicionar al 
    #vehículo dentro de la fila (lista de la matriz). Retorna el indice de la lista.
    if c == 'A':
        return 1
    if c == 'B':
        return 2
    if c == 'C':
        return 3
    if c == 'D':
        return 4
    if c == 'E':
        return 5
    if c == 'F':
        return 6
    if c == 'G':
        return 7
    if c == 'H':
        return 8
    if c == 'I':
        return 9
    if c == 'J':
        return 10

def cobro(lretiro, nh):
    #Toma una lista con la información del vehículo que se quiera retirar y el número de horas. Valida si el plan de pagos es "Mensualidad"
    #o "Diario" en la última posición de la lista. En caso de que sea "Mensualidad", muestra en pantalla que el usuario no debe 
    #pagar; de lo contrario, extrae de la lista el tipo de usuario para establecer la tarifa y proceder a hacer el cálculo del cobro y 
    #mostrarlo en pantalla. 
    if lretiro[3]=='Mensualidad':
        print('El usuario tiene plan de pago mensual. No debe pagar.')
    else:
        if lretiro[0]=='Estudiante':
            vp = 1000
        elif lretiro[0]=='Profesor':
            vp = 2000
        elif lretiro[0]=='Personal Administrativo':
            vp = 1500
        else:
            vp = 3000
        print('El usuario debe pagar $'+str(vp*nh))

def ocupacion(piso):
    #Toma la matriz de un piso. Recorre las listas de la matriz en el primer ciclo y en el segundo los elementos de la lista. Cuenta: 
    #el número de posiciones totales del piso y las que se encuentran ocupadas o marcadas con "X"; esto para hallar el porcentaje de ocupación
    #del piso. Retorna un porcentaje de ocupación del piso seleccionado.
    c = 0
    po = 0
    i1 = 1
    for x in range(len(piso)-1):
        i2 = 1
        for x in range(10):
            if piso[i1][i2]=='X':
                po+=1
            i2+=1
            c+=1
        i1+=1
    return (po/c)*100

import json

#MATRICES

#Para poder sacar la información de los usuarios que fueron registrados previamente, se acude al manejo de archivos json, posteriormente se abre
#y se carga. Como es un diccionario, se va a pasar a una lista vacía extrayendo los valores y almacerlos en una matriz llamada usuarios.
archivou = open("usuarios.json","r", encoding='utf-8')
usuarios1 = json.load(archivou)

users = []
for x in usuarios1.values():
    users.append(x)

usuarios = users[0]

#Matrices de los pisos: Representan los pisos con columnas y filas de los pisos. Cabe resaltar que la primera lista contiene letras y en el
#indice 0 de las demás listas para poder ubicar los a los vehículos y que el usuario escoja la posición.
p1=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 2 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 3 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 4 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 5 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 6 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 7 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 8 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 9 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 10 ,'0','0','0','0','0','0','0','0','0','0'],
    ]

p2=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 2 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 3 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 4 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 5 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 6 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 7 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 8 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 9 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 10 ,'0','0','0','0','0','0','0','0','0','0'],
    ]

p3=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 2 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 3 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 4 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 5 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 6 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 7 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 8 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 9 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 10 ,'0','0','0','0','0','0','0','0','0','0'],
    ]

p4=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 2 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 3 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 4 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 5 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 6 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 7 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 8 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 9 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 10 ,'0','0','0','0','0','0','0','0','0','0'],
    ]

p5=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 2 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 3 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 4 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 5 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 6 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 7 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 8 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 9 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 10 ,'0','0','0','0','0','0','0','0','0','0'],
    ]

p6=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 2 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 3 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 4 ,'0','0','0','0','0','0','0','0','0','0'],
    [ 5 ,'0','0','0','0','0','0','0','0','0','0'],
    ]


#Matrices para información por piso: Serviran para almacenar información de los usuarios dentro del parqueadero en una posición. Al igual que las
#anteriores matrices de los pisos, contienen números y letras para detectar la ubicación.
pi1=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'','','','','','','','','',''],
    [ 2 ,'','','','','','','','','',''],
    [ 3 ,'','','','','','','','','',''],
    [ 4 ,'','','','','','','','','',''],
    [ 5 ,'','','','','','','','','',''],
    [ 6 ,'','','','','','','','','',''],
    [ 7 ,'','','','','','','','','',''],
    [ 8 ,'','','','','','','','','',''],
    [ 9 ,'','','','','','','','','',''],
    [ 10 ,'','','','','','','','','',''],
    ]

pi2=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'','','','','','','','','',''],
    [ 2 ,'','','','','','','','','',''],
    [ 3 ,'','','','','','','','','',''],
    [ 4 ,'','','','','','','','','',''],
    [ 5 ,'','','','','','','','','',''],
    [ 6 ,'','','','','','','','','',''],
    [ 7 ,'','','','','','','','','',''],
    [ 8 ,'','','','','','','','','',''],
    [ 9 ,'','','','','','','','','',''],
    [ 10 ,'','','','','','','','','',''],
    ]

pi3=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'','','','','','','','','',''],
    [ 2 ,'','','','','','','','','',''],
    [ 3 ,'','','','','','','','','',''],
    [ 4 ,'','','','','','','','','',''],
    [ 5 ,'','','','','','','','','',''],
    [ 6 ,'','','','','','','','','',''],
    [ 7 ,'','','','','','','','','',''],
    [ 8 ,'','','','','','','','','',''],
    [ 9 ,'','','','','','','','','',''],
    [ 10 ,'','','','','','','','','',''],
    ]

pi4=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'','','','','','','','','',''],
    [ 2 ,'','','','','','','','','',''],
    [ 3 ,'','','','','','','','','',''],
    [ 4 ,'','','','','','','','','',''],
    [ 5 ,'','','','','','','','','',''],
    [ 6 ,'','','','','','','','','',''],
    [ 7 ,'','','','','','','','','',''],
    [ 8 ,'','','','','','','','','',''],
    [ 9 ,'','','','','','','','','',''],
    [ 10 ,'','','','','','','','','',''],
    ]

pi5=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'','','','','','','','','',''],
    [ 2 ,'','','','','','','','','',''],
    [ 3 ,'','','','','','','','','',''],
    [ 4 ,'','','','','','','','','',''],
    [ 5 ,'','','','','','','','','',''],
    [ 6 ,'','','','','','','','','',''],
    [ 7 ,'','','','','','','','','',''],
    [ 8 ,'','','','','','','','','',''],
    [ 9 ,'','','','','','','','','',''],
    [ 10 ,'','','','','','','','','',''],
    ]

pi6=  [
    ['','A','B','C','D','E','F','G','H','I','J'],
    [ 1 ,'','','','','','','','','',''],
    [ 2 ,'','','','','','','','','',''],
    [ 3 ,'','','','','','','','','',''],
    [ 4 ,'','','','','','','','','',''],
    [ 5 ,'','','','','','','','','',''],
    ]

vehiculosparqueados = []
#Esta matriz va a contener las listas con la información de los vehículos que se encuentran dentro del parqueadero. Las listas tendrán:
#tipo de usuario, placa, tipo de vehiculo y plan de pagos.


#El programa le dará la bienvenida a la persona que lo maneje y le va a mostrar las acciones que puede ejecutar: registrar un usuario, ingresar 
#un vehículo, retirar un vehículo o generar reportes; cada una está representada con un número. Cuando finalice de ejecutar la acción que
#se desea hacer, le preguntará si desea o no volver a ejecutar esa opción (a excepción de la acción de generar reportes), luego le preguntará si 
#desea volver al menú o salir. En caso de que decida continuar en el menú, se volverá a mostrar las cuatro opciones del menú, de lo contrario, 
#el programa dejará de correr.

print('Bienvenido al sistema de parqueadero de la Pontificia Universidad Javeriana Cali.')
opcionmenu = 0
while opcionmenu!=5:
    menu = eval(input('Opciones del menú: \n 1. Para registrar usuarios. \n 2. Para ingresar un vehículo. \n 3. Para la salida de un vehículo. \n 4. Para generar reportes. \nDigite el número de la opcion que desea ejecutar: '))

    #REGISTRO
    #Esta opción sirve para registrar la información de un usuario en una lista llamada infousuario. 

    if menu==1:
        #Le pedirá el nombre y el número de identificación. Por medio de un ciclo, recorrerá para validar si la identificación ya esta dentro de
        #la matriz usuarios. En caso de que esté, le mostrará en pantalla al usuario que ya esta registrado y romperá el ciclo terminando la 
        #ejecución de esta acción en caso de que no, llama a la función datos para solicitar información y almacernarla en la lista. Ya despues 
        #de tener la lista, la añade a la matriz usuarios.
        v1 = 0
        while v1!=-1:
            infousuario = []
            nombre = input('Ingrese el nombre y apellido del usuario: ')
            identificacion = int(input('Ingrese el documento de identidad del usuario: '))
            res = 1
            i = 0
            for x in range(len(usuarios)):
                if usuarios[i][1]==identificacion:
                    res = 0
                    print('El usuario ya tiene un vehículo registrado.')
                    break
                i+=1
            if res==1:
                m = datos(infousuario)
                usuarios.append(m)
                print('¡REGISTRO EXITOSO! La información ya quedó almacenada.')
            v1 = eval(input('Si ya no desea ingresar usuarios digite -1, de lo contrario cualquier otro número: '))

    #INGRESO
    #Esta opción permite el ingreso del vehículo.

    if menu==2:
        #Primero se va a extraer de un archivo json las ubicaciones de acuerdo al tipo de vehiculo, abrirlo en modo lectura, cargarlo y extraer 
        #los valores del diccionario. Posteriormente en unas variables se va a almacenar la información de cada piso que está expresada en 
        #matrices.
        archivotp = open("tiposvehiculos.json","r")
        tp1 = json.load(archivotp)

        mtp = []
        for x in tp1.values():
            mtp.append(x)

        up1 = mtp[0]
        up2 = mtp[1]
        up3 = mtp[2]
        up4 = mtp[3]
        up5 = mtp[4]
        up6 = mtp[5]
        
        
        #En segundo lugar, le va a solicitar que ingrese la placa, la va a buscar por medio de un ciclo dentro de la matriz de los usuarios 
        #verificando si la matriz existe o no. En caso de que si, le mostrará en pantalla la lista con la información del usuario y se extrae el 
        #tipo de usuario, la placa, el tipo de vehículo y el plan de pago para añadirlos a una lista ingresovehiculo. En caso de que el usuario 
        #no se encuentre registrado, el programa mostrará que no está registrado, sera guardado como visitante, el plan de pago será diario y 
        #se deberá indicar el tipo de vehiculo para igualmente añadirlos a la lista ingresovehiculo. Convertirá el tipo de vehículo a una 
        #variable numérica para hacer un manejo más facil con las matrices de la ubicación según el tipo de vehículo.
        v2=0
        while v2!=-1:
            ingresovehiculo = []
            iplaca = input('Ingrese la placa del vehículo: ')
            i = 0
            valplaca = 0
            for x in range (len(usuarios)):
                if usuarios[i][3]==iplaca:
                    valplaca = 1
                    iusuario = usuarios[i]
                    ingresovehiculo.append(usuarios[i][2])
                    ingresovehiculo.append(iplaca)
                    ingresovehiculo.append(usuarios[i][4])
                    ingresovehiculo.append(usuarios[i][5])
                    print('La placa se encuentra registrada en: '+str(usuarios[i]))
                    break
                i+=1
            if valplaca==0:
                print('La placa no se encuentra registrada.')
                ingresovehiculo.append('Visitante')
                ingresovehiculo.append(iplaca)
                tv = int(input('Opciones de tipo de vehículo: \n 1. Para Automóvil \n 2. Para automóvil eléctrico \n 3. Para Motocicleta \n 4. Para discapacitado\nDigite el número según el tipo de vehículo: '))
                if tv==1:
                    tipovehiculo = 'Automóvil'
                elif tv==2:
                    tipovehiculo = 'Automóvil Eléctrico'
                elif tv==3:
                    tipovehiculo = 'Motocicleta'
                elif tv==4:
                    tipovehiculo = 'Discapacitado'
                ingresovehiculo.append(tipovehiculo)
                ingresovehiculo.append('Diario')
        
            if ingresovehiculo[2]=='Automóvil':
                itvehiculo = 1
            elif ingresovehiculo[2]=='Automóvil Eléctrico':
                itvehiculo = 2
            elif ingresovehiculo[2]=='Motocicleta':
                itvehiculo = 3
            elif ingresovehiculo[2]=='Discapacitado':
                itvehiculo = 4

            #Luego, hará la validación de los cupos, calcula por medio de la función pisosdisp el número de espacios disponibles, en caso de 
            #que en un piso tenga al menos un cupo, le mostrará por pantalla el número de cupos disponibles por piso. En caso de que no existan 
            #cupos, le avisará que no hay cupos y esta opción finaliza.
            pd1 = pisosdisp(p1, up1, itvehiculo)
            pd2 = pisosdisp(p2, up2, itvehiculo)
            pd3 = pisosdisp(p3, up3, itvehiculo)
            pd4 = pisosdisp(p4, up4, itvehiculo)
            pd5 = pisosdisp(p5, up5, itvehiculo)
            pd6 = pisosdisp(p6, up6, itvehiculo)


            if pd1>0 or pd2>0 or pd3>0 or pd4>0 or pd5>0:
                acceso = 0
                print('En el piso 1 hay '+str(pd1)+' cupos disponibles.')
                print('En el piso 2 hay '+str(pd2)+' cupos disponibles.')
                print('En el piso 3 hay '+str(pd3)+' cupos disponibles.')
                print('En el piso 4 hay '+str(pd4)+' cupos disponibles.')
                print('En el piso 5 hay '+str(pd5)+' cupos disponibles.')
                print('En el piso 6 hay '+str(pd6)+' cupos disponibles.')
            
            else:
                acceso = 1
                print('Lo sentimos, no hay cupos disponibles.')

            #Posterior se le preguntará el piso en donde el usuario se desea ubicar, va a entrar a un ciclo donde valida si efectivamente el 
            #usuario escogió un piso con posiciones disponibles. Si ese fue el caso, va a guardar en unas variables la matriz de piso y 
            #la matriz con la información dentro del parqueadero. En caso de que se haya solicitado un piso sin cupos disponibles, le indicará 
            #que el piso no tiene cupos y le volverá asolicitar que ingrese un piso. 
            if acceso==0:
                vp = 0
                while vp==0:
                    pisodeseado = eval(input('Ingrese el número del piso en el que desea parquear: '))
                    if pisodeseado == 1:
                        if pd1>0:
                            pd = p1
                            ud = up1
                            pi = pi1
                            vp = 1
                        else:
                            print('No hay cupos disponibles en este piso. Intente otra vez.')

                    elif pisodeseado == 2:
                        if pd2>0:
                            pd = p2
                            ud = up2
                            pi = pi2
                            vp = 1
                        else:
                            print('No hay cupos disponibles en este piso. Intente otra vez.')
                    
                    elif pisodeseado == 3:
                        if pd3>0:
                            pd = p3
                            ud = up3
                            pi = pi3
                            vp = 1
                        else:
                            print('No hay cupos disponibles en este piso. Intente otra vez.')
                    
                    elif pisodeseado == 4:
                        if pd4>0:
                            pd = p4
                            ud = up4
                            pi = pi4
                            vp = 1
                        else:
                            print('No hay cupos disponibles en este piso. Intente otra vez.')
                    
                    elif pisodeseado == 5:
                        if pd5>0:
                            pd = p5
                            ud = up5
                            pi = pi5
                            vp = 1
                        else:
                            print('No hay cupos disponibles en este piso. Intente otra vez.')

                    else:
                        if pd6>0:
                            pd = p6
                            ud = up6
                            pi = pi6
                            vp = 1
                        else:
                            print('No hay cupos disponibles en este piso. Intente otra vez.')
                        
                #Luego le va a mostrar en pantalla la matriz con las posibles ubicaciones marcadas con "0" que se hizo en la función 
                #posibleubicacion, le solicitará al usuario que ingrese la posición exacta; piso y columna, como es posible que se ingrese mal 
                #la letra o el número, va a intentar hasta que el ingrese como fila un número y en la columna una letra en mayuscula. Para 
                #convertir la letra en un número acude a la función columna. El programa validará que la posición ingresada por el usuario está 
                #disponible, en caso de que no, le solicitará que ingrese nuevamente la posición hasta que ingrese una que esté disponible. 
                #Para finalizar esta opción, se reemplazará la posición por una "X" en la matriz del piso, y se añadirá en la matriz del piso 
                #información, la lista con la información del vehiculo y usuario, y finalmente almacena en vehiculosparqueados la información 
                #que se encuentra en ingresovehiculo.

                print('Los espacios disponibles en el piso '+str(pisodeseado)+' se encuentran marcados con "0"')
                posibleubicacion(pd, ud, itvehiculo)

                validacionespacio = 0
                while validacionespacio == 0:
                    c1 = 0
                    while c1==0:
                        try:
                            fila = int(input('Ingrese el número de la fila: '))
                            c1 = 1
                        except:
                            print("Recuerde que la fila es un valor numérico. Intentelo otra vez.")
                    c2 = 0
                    while c2==0:
                        try:
                            columna = input('Ingrese la letra en mayúscula de la columna: ')
                            if pd[fila][columnas(columna)]=='X' or ud[(fila-1)][(columnas(columna)-1)]!=itvehiculo:
                                print('El espacio se encuentra ocupado o no esta disponible para el tipo de vehículo.\nIntente otra posición.')
                            else:
                                pd[fila][columnas(columna)]='X'
                                pi[fila][columnas(columna)]=ingresovehiculo
                                vehiculosparqueados.append(ingresovehiculo)
                                validacionespacio = 1
                                print('¡INGRESO EXITOSO! El vehículo puede ingresar y ubicarse en el piso y la ubicación que seleccionó.')
                            c2 = 1
                        except:
                            print("Recuerde que la columna es una letra mayúscula. Intentelo otra vez.")

            v2 = eval(input('Digite -1 para parar de ingresar vehículos, de lo contrario cualquier otro número: '))

    #RETIRO
    #Esta opción permite la salida de un vehículo y le indica de acuerdo al plan de pagos si hay que pagar o no, y en caso de que si, el valor, 
    #adicionalmente limpiará el ingreso del vehículo y la posición quedará libre para almacernarla.

    if menu==3:
        #Primero validará que haya vehiculos dentro del parqueadero por medio de la matriz vehiculosparqueados. En caso de que no, le indicará 
        #que no hay vehiculos dentro del parqueadero y le preguntará si desea ejecutar otra opción del menú o finalizar.
        if len(vehiculosparqueados)>0:
            #En caso de que si haya vehiculos le solicitará la placa, y valida si la placa digitada pertenece a un vehiculo que este dentro del 
            #parqueadero por medio de un ciclo, el programa le preguntará hasta que la placa pertenezca a un vehículo dentro del parqueadero. 
            #Posterior le preguntará el número de horas que se mantuvo en el parqueadero, y buscara dentro de la matriz vehiculosparqueados la 
            #placa para obtener la información del usuario y se llamará a la función cobro.
            v3 = 0
            while v3!=-1:
                vplaca = 0     
                while vplaca==0:
                    rplaca = input('Ingrese la placa del vehículo: ')
                    i = 0
                    for x in range(len(vehiculosparqueados)):
                        if rplaca == vehiculosparqueados[i][1]:
                            vplaca =1
                        else:
                            i+=1
                    if vplaca == 0:
                        print('El vehiculo no se encuentra dentro del parqueadero. Intentelo otra vez.')              
                nhoras = eval(input('Ingrese el número de horas que el vehículo estuvo dentro del parqueadero: '))
                rv = 0
                i1 = 0
                while rv==0:
                    if vehiculosparqueados[i1][1]==rplaca:
                        lretiro = vehiculosparqueados[i1]
                        rv = -1
                    else:
                        rv = 0
                        i1+=1
                cobro(lretiro, nhoras)

                #Después, se procede a limpiar la información de las matrices. Para esto, se va a hacer un proceso de busqueda por medio de 
                #condicionales y ciclos que recorreran las listas e indices para encontrar la lista con la información en el piso que se 
                #encontraba el vehículo. Entonces, por medio de una variable va a validar si accede o no a buscar en ese piso, esto quiere decir 
                #que si encuentra la lista en un piso almacene la información del piso correspondiente, se actualiza la variable de busqueda para
                #impedir que entre a los condicionales. Finalmente dejarla en "0" (disponible) la posición en donde se encontraba y libera la 
                #información de la matriz del piso de la información y además, lo elimina la lista vehiculosparqueados.
                
                busqueda = 0
                if busqueda == 0:
                    i1 = 1
                    for x in range(len(p1)-1):
                        i2 = 1
                        for x in range(len(p1)-1):
                            if pi1[i1][i2]==lretiro:
                                piso = p1
                                pisou = pi1
                                f = i1
                                c = i2
                                busqueda = 1
                                break
                            i2+=1
                        i1+=1
                
                if busqueda == 0:
                    i1 = 1
                    for x in range(len(p2)-1):
                        i2 = 1
                        for x in range(len(p2)-1):
                            if pi2[i1][i2]==lretiro:
                                piso = p2
                                pisou = pi2
                                f = i1
                                c = i2
                                busqueda = 1
                                break
                            i2+=1
                        i1+=1
                
                if busqueda == 0:
                    i1 = 1
                    for x in range(len(p3)-1):
                        i2 = 1
                        for x in range(len(p3)-1):
                            if pi3[i1][i2]==lretiro:
                                piso = p3
                                pisou = pi3
                                f = i1
                                c = i2
                                busqueda = 1
                                break
                            i2+=1
                        i1+=1
                
                if busqueda == 0:
                    i1 = 1
                    for x in range(len(p4)-1):
                        i2 = 1
                        for x in range(len(p4)-1):
                            if pi4[i1][i2]==lretiro:
                                piso = p4
                                pisou = pi4
                                f = i1
                                c = i2
                                busqueda = 1
                                break
                            i2+=1
                        i1+=1
                
                if busqueda == 0:
                    i1 = 1
                    for x in range(len(p5)-1):
                        i2 = 1
                        for x in range(len(p5)-1):
                            if pi5[i1][i2]==lretiro:
                                piso = p5
                                pisou = pi5
                                f = i1
                                c = i2
                                busqueda = 1
                                break
                            i2+=1
                        i1+=1
                
                if busqueda == 0:
                    i1 = 1
                    for x in range(len(p6)-1):
                        i2 = 1
                        for x in range(10):
                            if pi6[i1][i2]==lretiro:
                                piso = p6
                                pisou = pi6
                                f = i1
                                c = i2
                                busqueda = 1
                                break
                            i2+=1
                        i1+=1

                piso[f][c]='0'
                pisou[f][c]=''
                vehiculosparqueados.remove(lretiro)

                print('¡RETIRO EXITOSO! Gracias por hacer uso del parqueadero, que tenga un buen día.')

                v3 = eval(input('Ingrese -1 si no desea retirar otro vehículo, de lo contrario, cualquier otro número: '))
        else:
            print('No hay vehiculos parqueados.')

    #REPORTES
    #Esta opción genera los reportes para la Oficina de Servicios Generales. Estos se van a hacer en base a la matriz vehiculosparqueados que 
    #contienen la información de los vehículos dentro de los parqueaderos.
    
    if menu==4:
        #Para el primer informe, por medio de un ciclo de acuerdo a la longitud de la matriz vehiculosparqueados, identifica el indice 0 de la 
        #lista y de acuerdo al tipo de usuario cuenta los va sumando a variables previamente establecidas. Se crea un archivo.txt en escritura y 
        #se añade el writelines para escribir dentro de el.
        tusuario1 = 0
        tusuario2 = 0
        tusuario3 = 0
        tusuario4 = 0

        i = 0
        for x in range(len(vehiculosparqueados)):
            if vehiculosparqueados[i][0]=='Estudiante':
                tusuario1+=1
            elif vehiculosparqueados[i][0]=='Profesor':
                tusuario2+=1
            elif vehiculosparqueados[i][0]=='Personal Administrativo':
                tusuario3+=1
            elif vehiculosparqueados[i][0]=='Visitante':
                tusuario4+=1
            i+=1

        reportetipousuario = open("TiposUsuarios.txt","w")
        reportetipousuario.writelines('Reporte según en tipo de usuario.\n')
        reportetipousuario.writelines('Hay '+str(tusuario1)+' vehiculo(s) parqueados de estudiantes.\n')
        reportetipousuario.writelines('Hay '+str(tusuario2)+' vehiculo(s) parqueados de profesores.\n')
        reportetipousuario.writelines('Hay '+str(tusuario3)+' vehiculo(s) parqueados del personal administrativo.\n')
        reportetipousuario.writelines('Hay '+str(tusuario4)+' vehiculo(s) parqueados de visitantes.')
        reportetipousuario.close()

        #Pasa igual que en el anterior informe con los tipos de vehiculos, que se encuentran en el indice 2.
        vehiculos1 = 0
        vehiculos2 = 0
        vehiculos3 = 0
        vehiculos4 = 0

        i = 0
        for x in range(len(vehiculosparqueados)):
            if vehiculosparqueados[i][2]=='Automóvil':
                vehiculos1+=1
            elif vehiculosparqueados[i][2]=='Automóvil Eléctrico':
                vehiculos2+=1
            elif vehiculosparqueados[i][2]=='Motocicleta':
                vehiculos3+=1
            elif vehiculosparqueados[i][2]=='Discapacitado':
                vehiculos4+=1
            i+=1

        reportetipovehiculo = open("TiposVehiculos.txt","w")
        reportetipovehiculo.writelines('Reporte según el tipo de vehículos\n')
        reportetipovehiculo.writelines('Hay '+str(vehiculos1)+' automóvil(es) dentro del parqueadero.\n')
        reportetipovehiculo.writelines('Hay '+str(vehiculos2)+' automóvil(es) eléctrico(s) dentro del parqueadero.\n')
        reportetipovehiculo.writelines('Hay '+str(vehiculos3)+' motocicleta(s) dentro del parqueadero.\n')
        reportetipovehiculo.writelines('Hay '+str(vehiculos4)+' dispacitado(s) dentro del parqueadero.')
        reportetipovehiculo.close()

        #Para los porcentajes de ocupación, se recurre a la función ocupación que retorna el porcentaje de ocupación de cada piso. Para el 
        #porcentaje total del parqueadero, como existe un piso con 50 cupos, se multiplica ese porcentaje por 50 y se divide por 100 
        #(correspondiente al piso 6) y se suman los porcentajes de los otros parqueaderos.
        ocupaciontotal = (ocupacion(p1)+ocupacion(p2)+ocupacion(p3)+ocupacion(p4)+ocupacion(p5)+((ocupacion(p6)/100)*50))/550

        reporteocupacion = open("Ocupación.txt","w")
        reporteocupacion.writelines('Reporte de opupación del parqueadero'+'\n')
        reporteocupacion.writelines('El porcentaje de ocupación del parqueadero es '+str(ocupaciontotal)+'%.\n')
        reporteocupacion.writelines('El porcentaje de ocupación del piso 1 es del '+str(ocupacion(p1))+'%.\n')
        reporteocupacion.writelines('El porcentaje de ocupación del piso 2 es del '+str(ocupacion(p2))+'%.\n')
        reporteocupacion.writelines('El porcentaje de ocupación del piso 3 es del '+str(ocupacion(p3))+'%.\n')
        reporteocupacion.writelines('El porcentaje de ocupación del piso 4 es del '+str(ocupacion(p4))+'%.\n')
        reporteocupacion.writelines('El porcentaje de ocupación del piso 5 es del '+str(ocupacion(p5))+'%.\n')
        reporteocupacion.writelines('El porcentaje de ocupación del piso 6 es del '+str(ocupacion(p6))+'%.')
        reporteocupacion.close()

        print('¡ACCIÓN EXITOSA! Puede consultar los reportes dentro de la misma ruta de archivos del parqueadero.')

    opcionmenu = eval(input('Si desea salir, digite 5; de lo contrario cualquier otro número: '))


#Cuando el usuario salga del sistema, para que no se pierda la información de los nuevos registros, se procede a volver la matriz usuarios a un
#diccionario, y abrir el archivo json para sobreescribirlo con la nueva matriz.
dicc = {}
dicc["usuarios"] = usuarios
with open("usuarios.json","w", encoding='utf-8') as file:
    json.dump(dicc, file, indent=4, ensure_ascii=False)
    file.close()

print('¡Muchas gracias por hacer uso de nuestro software!')