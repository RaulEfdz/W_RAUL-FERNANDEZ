from difflib import SequenceMatcher as SM
import random
SensivilidadDeBusqueda = 0.8
Muestras_De_Entrenamiento = 2
lista = []
LIS =[]
APT=[]
Xv = 0
W_People_Out  = open("Memory.txt", "w")
W_People_Out.write('')
W_People_Out.close()

W_People_Out  = open("SubD.txt", "w")
W_People_Out.write('')
W_People_Out.close()

W_People_Out  = open("people.out", "w")
W_People_Out.write('')
W_People_Out.close()

def Fase_1():
    print('\n\n\n.......Fase 1 ==> ENTRENAMIENTO SUPERVISADO DEL ALGORITMO.........\n')
    A=input('Agrega algunas palabras claves almenos 2 ejemplo ==> engineering developers : ')
    W_People_Out  = open("Memory.txt", "w")
    W_People_Out.write(A)
    W_People_Out.close()

    R_People_In  = open("people.in" , "r")
    for linea in R_People_In.readlines():
        lista.append(linea)
    for x in range(Muestras_De_Entrenamiento):
        KW_1 = random.choice(lista) 
        TS = KW_1.split("|")
        personalid      = TS[0]
        name            = TS[1]
        lastname        = TS[2]
        currentrole     = TS[3]
        country         = TS[4]
        industry        = TS[5]
        nrecomendations = TS[6]
        nconnections    = TS[7]
        LI=(currentrole+' '+industry+' ')
        lis = LI.split(" ")
        lis = list(set(lis))
        for x, y in enumerate(lis):
            if y == ' ':
                lis.pop(x)
            if len(y)<=3:
                lis.pop(x)
        lis = " ".join(lis)
        A = input('\n\n\n\n' +KW_1 +'\n'+' El usuario de arriba se relaciona con el resultado que espera? S/N : ')
        if A == 'S' or A == 's' :
            R_People_Out = open("Memory.txt", "r")
            RP=R_People_Out.read()
            RP=''.join(RP)
            R_People_Out.close()

            W_People_Out  = open("Memory.txt", "w")
            W_People_Out.write(RP+' '+lis)
            W_People_Out.close()

            R_People_Out = open("people.out", "r")
            RP=R_People_Out.read()
            RP=''.join(RP)
            R_People_Out.close()
            W_People_Out  = open("people.out", "w")
            W_People_Out.write(RP+'\n'+personalid)
            W_People_Out.close()

    R_People_Out = open("Memory.txt", "r")
    RP=R_People_Out.read()
    RP=''.join(RP)
    R_People_Out.close()
    if len(RP) <5:
            Fase_1()
    else:
        Fase_2()


def Fase_2():
    print('\n\n ........Fase 2 ==> FILTRO Y CLASIFICACION DE USUARIOS......... \n\n  ')
    for x in range(1):
        print('Fase 2')
        ReadMemory = open("Memory.txt", "r")
        RM = ReadMemory.read()
        RM = RM.split(" ")
        for x, y in enumerate(RM):
            if len(y)<=3:
                RM.pop(x)
        ReadMemory.close()
    
        R_People_In  = open("people.in" , "r")
        for linea in R_People_In.readlines():
            TS = linea.split("|")
            personalid      = TS[0]
            name            = TS[1]
            lastname        = TS[2]
            currentrole     = TS[3]
            country         = TS[4]
            industry        = TS[5]
            nrecomendations = TS[6]
            nconnections    = TS[7]
    
            currentrole = currentrole.split(" ")
            industry = industry.split(" ")
            Lista=['']
            currentrole=' '.join(currentrole)
            industry=' '.join(industry)
            lista = (currentrole+' '+industry+' ')
            lista = lista.split(" ")
            lista = list(set(lista))
            lista = " ".join(lista)
            lista = lista.split(" ")
            lista = list(set(lista))
            for x, y in enumerate(lista):
                if len(y)<=3:
                    lista.pop(x)
            if int(nconnections) == 0:
                nconnections = 1
            if int(nrecomendations) == 0:
                nrecomendations = 1

            for w in RM:
                for q in lista:
                    Relacion = SM(None, w, q).ratio()

                    if Relacion > 0.7:
                        V = int(nconnections)*int(nrecomendations)
                        APT.append(personalid+'|'+str(V)+'|'+str(Relacion))
                    
        AP = list(set(APT))               
        # print(AP)
        Result = []
        for q in AP:
            TS = q.split("|")
            personalid      = TS[0]
            Vv              = TS[1]
            RelacionV       = TS[2]
            if len(Result) <100:
                if float(RelacionV ) >=0.9:
                     Result.append(personalid)
            else:
                print('Procesando...')  
                break

        if len(Result) <100:
            for q in AP:
                TS = q.split("|")
                personalid      = TS[0]
                Vv              = TS[1]
                RelacionV       = TS[2]
                if len(Result) <100:
                    if float(RelacionV ) >=0.8:
                        if float(RelacionV ) <0.9:
                            Result.append(personalid)
                else:
                    print('Procesando...')  
                    break
            
        if len(Result) <100:
            for q in AP:
                TS = q.split("|")
                personalid      = TS[0]
                Vv              = TS[1]
                RelacionV       = TS[2]
                if len(Result) <100:
                    if float(RelacionV ) >=0.7:
                        if float(RelacionV ) <0.8:
                            Result.append(personalid)
                else:
                    print('Procesando...') 
                    break
        print('\n\n Fase 3 ==> PRESENTACION DE USUARIOS POTENCIALES \n\n  ')
        print(Result)  
        print('\n\n-----------Proceso completado el resultado esta en people.out-------------')         
        WRITEpeopleOUT   = open("people.out" , "w")
        WRITEpeopleOUT.write('\n'.join(Result))
        WRITEpeopleOUT.close()

   

Fase_1()