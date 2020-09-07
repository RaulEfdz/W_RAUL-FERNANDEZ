from difflib import SequenceMatcher as SM
L_MEM=[]
o=100
# Entrenamiento
def Fase_1():
    print('I Fase 1')
    R_People_Out = open("People_Out.txt", "r")
    RP=R_People_Out.read()
    RP=''.join(RP)
    # print(len(RP))
    R_People_Out.close()
    if len(RP) == 0:
        W_People_Out  = open("People_Out.txt" , "w")
        W_People_Out.write(' ')
        W_People_Out.close()

    MemoryR = open("Memory.txt", "r")
    R_MemoryR = MemoryR.read()
    R_MemoryR =''.join(R_MemoryR)
    # print(len(R_MemoryR))
    MemoryR.close()
    if len(R_MemoryR) == 0:
        print('\n \nFase 1 ==> Entrenamiento')
        print('\n -Este algoritmo necesita una entrada minima de palabras claves para luego ir aprendiendo de forma autonoma')
        print('\n -Ejemplo de palabras claves: engineering softwere ...')
        Kw= input('\n  +Agrega algunas palabras claves: ')
        MemoryW  = open("Memory.txt" , "w")
        MemoryW.write(Kw)
        MemoryW.close()
        Fase_2()
    else:
        Fase_2()

# Proceso
def Fase_2():
 
    for x in range(2):
         
         MemoryR = open("Memory.txt" , "r")
         MEM = []
         # Memory.read()
         # recorrer txt
         for linea in MemoryR.readlines():
             # print(linea)
             # TS = linea.split(" ")
             TS = linea.split("\n")
             # print(TS)
             TS= " ".join(TS)
             MEM.append(TS)
         # print('Lista',MEM)
         MEM= " ".join(MEM)
         # print('cadena',MEM)
         MEM = MEM.split(" ")
         # print('LAS',MEM)
         for e, i in enumerate(MEM):
             if i == '':
                 MEM.pop(e)
             if len(i )==1:
                 MEM.pop(e)
             if len(i )==2:
                 MEM.pop(e)
         MEM = list(set(MEM))
        #  MEM.append(Refe)
         MemoryR.close()   
    
    # Escribir en memory
    MemoryW  = open("Memory.txt" , "w")
    L_MEM = MEM
    MEM = " ".join(MEM)
    MemoryW.write(MEM)
    MemoryW.close()
    # print('MEM = '+MEM)
    # print(L_MEM)
    
    # cto gestion teleport desarrollador software jefe co-founder funcional manager engineering
    
                    
    
    R_People_In  = open("People_In.txt" , "r")
    # R_People_Out.read()
    # recorrer txt
    for linea in R_People_In.readlines():
        # print(linea)
    
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
        # print(currentrole)
        for e in currentrole:
            for i in L_MEM:
                print(e+' = '+i)
                # print(id(e),id(i))
                A = SM(None, e, i).ratio()
                # print(A)
                if A==1.0:
                #     print(personalid)
                    #SALIDAS
                    People_Out   = open("People_Out.txt" , "r")
                    R_People_Out = People_Out.read()
                    RL_People_Out = People_Out.read()
                    R_People_Out = "".join(R_People_Out)
                    # Escribir en Salidas
                    People_Out2   = open("People_Out.txt" , "r")
                    for i in People_Out2.readlines():
                        # print('i = '+i+"p = "+personalid)
                        A = SM(None, i, personalid).ratio()
                        # print('ASA ',A)
                        if A>=0.8:
                            print(personalid, "Id existente")
                            Fase_3()
                            
                        if A<=0.8:
                            W_People_Out = open("People_Out.txt", "w")
                            W_People_Out.write(personalid+'\n'+ R_People_Out )
                            W_People_Out.close()  
    
                            R_Memory = open("Memory.txt", "r")
                            R_Memory_r=R_Memory.read()
                            W_Memory = open("Memory.txt", "w")
                            R_Memory_r = "".join(R_Memory_r)
                            W_Memory.write(R_Memory_r+' '+industry)
                            W_Memory.close()  
                            R_Memory.close()  
                          
                    People_Out.close()
                    People_Out2.close()
    
    Ret= open("People_Out.txt" , "r") 
    MEM = []
    # Memory.read()
    # recorrer txt
    for linea in Ret.readlines():
        # print(linea)
        # TS = linea.split(" ")
        TS = linea.split("\n")
        # print(TS)
        TS= " ".join(TS)
        MEM.append(TS)
    # print('Lista',MEM)
    MEM= " ".join(MEM)
    # print('cadena',MEM)
    MEM = MEM.split(" ")
    # print('LAS',MEM)
    for e, i in enumerate(MEM):
        if i == '':
            MEM.pop(e)
        if len(i )==1:
            MEM.pop(e)
        if len(i )==2:
            MEM.pop(e)
    MEM = list(set(MEM))
    # MEM.append(Refe)
    Ret.close()   
    # Escribir en memory
    Wet  = open("People_Out.txt" , "w")
    L_MEM = MEM
    MEM = "\n".join(MEM)
    Wet.write(MEM)
    Wet.close()
    # print('MEM = '+MEM)
    # print(L_MEM)
    
    MemoryR = open("Memory.txt" , "r")
    MEM = []
    # Memory.read()
    # recorrer txt
    for linea in MemoryR.readlines():
        # print(linea)
        # TS = linea.split(" ")
        TS = linea.split("\n")
        # print(TS)
        TS= " ".join(TS)
        MEM.append(TS)
        # print('Lista',MEM)
        MEM= " ".join(MEM)
        # print('cadena',MEM)
        MEM = MEM.split(" ")
        # print('LAS',MEM)
        for e, i in enumerate(MEM):
            if i == '':
                MEM.pop(e)
            if len(i )==1:
                MEM.pop(e)
            if len(i )==2:
                 MEM.pop(e)
        MEM = list(set(MEM))
        # MEM.append(Refe)
        MemoryR.close()   
    
    # Escribir en memory
    MemoryW  = open("Memory.txt" , "w")
    L_MEM = MEM
    MEM = " ".join(MEM)
    MemoryW.write(MEM)
    MemoryW.close()
    # print('MEM = '+MEM)
    # print(L_MEM)
    
    
    
    
    R_People_In  = open("People_In.txt" , "r")
    # R_People_Out.read()
    # recorrer txt
    for linea in R_People_In.readlines():
        # print(linea)
    
        TS = linea.split("|")
        
        personalid      = TS[0]
        name            = TS[1]
        lastname        = TS[2]
        currentrole     = TS[3]
        country         = TS[4]
        industry        = TS[5]
        nrecomendations = TS[6]
        nconnections    = TS[7]
        industry = industry.split(" ")
        # print(currentrole)
        for e in industry:
            for i in L_MEM:
                # print(e+' = '+i)
                # print(id(e),id(i))
                A = SM(None, e, i).ratio()
                # print(A)
                if A==1.0:
                #     print(personalid)
                    #SALIDAS
                    People_Out   = open("People_Out.txt" , "r")
                    R_People_Out = People_Out.read()
                    RL_People_Out = People_Out.read()
                    R_People_Out = "".join(R_People_Out)
                    # Escribir en Salidas
                    People_Out2   = open("People_Out.txt" , "r")
                    for i in People_Out2.readlines():
                        # print('i = '+i+"p = "+personalid)
                        A = SM(None, i, personalid).ratio()
                        # print('ASA ',A)
                        if A>=0.8:
                            print(personalid, "Id existente")
                            Fase_3()
                            
                        if A<=0.8:
                            W_People_Out = open("People_Out.txt", "w")
                            W_People_Out.write(personalid+'\n'+ R_People_Out )
                            W_People_Out.close()  
    
                            R_Memory = open("Memory.txt", "r")
                            R_Memory_r=R_Memory.read()
                            W_Memory = open("Memory.txt", "w")
                            R_Memory_r = "".join(R_Memory_r)
                            W_Memory.write(R_Memory_r+' '+currentrole)
                            W_Memory.close()  
                            R_Memory.close()  
                          
                    People_Out.close()
                    People_Out2.close()
    
    Ret= open("People_Out.txt" , "r") 
    MEM = []
    # Memory.read()
    # recorrer txt
    for linea in Ret.readlines():
        # print(linea)
        # TS = linea.split(" ")
        TS = linea.split("\n")
        # print(TS)
        TS= " ".join(TS)
        MEM.append(TS)
    # print('Lista',MEM)
    MEM= " ".join(MEM)
    # print('cadena',MEM)
    MEM = MEM.split(" ")
    # print('LAS',MEM)
    for e, i in enumerate(MEM):
        if i == '':
            MEM.pop(e)
        if len(i )==1:
            MEM.pop(e)
        if len(i )==2:
            MEM.pop(e)
    MEM = list(set(MEM))
    # MEM.append(Refe)
    Ret.close()   
    # Escribir en memory
    Wet  = open("People_Out.txt" , "w")
    L_MEM = MEM
    MEM = "\n".join(MEM)
    Wet.write(MEM)
    Wet.close()
    # print('MEM = '+MEM)
    # print(L_MEM)
    
    MemoryR = open("Memory.txt" , "r")
    MEM = []
    # Memory.read()
    # recorrer txt
    for linea in MemoryR.readlines():
        # print(linea)
        # TS = linea.split(" ")
        TS = linea.split("\n")
        # print(TS)
        TS= " ".join(TS)
        MEM.append(TS)
        # print('Lista',MEM)
        MEM= " ".join(MEM)
        # print('cadena',MEM)
        MEM = MEM.split(" ")
        # print('LAS',MEM)
        for e, i in enumerate(MEM):
            if i == '':
                MEM.pop(e)
            if len(i )==1:
                MEM.pop(e)
            if len(i )==2:
                 MEM.pop(e)
        MEM = list(set(MEM))
        # MEM.append(Refe)
        MemoryR.close()   
    
    # Escribir en memory
    MemoryW  = open("Memory.txt" , "w")
    L_MEM = MEM
    MEM = " ".join(MEM)
    MemoryW.write(MEM)
    MemoryW.close()
    # print('MEM = '+MEM)
    # print(L_MEM)

#Limites Y Resultados

def Fase_3():
    
    k=0
    People_OutR = open("People_Out.txt", "r")
    # People_OutRR = People_OutR.read()
    #  People_OutRR =''.join(People_OutRR)
    # People_OutRR=str(rPeople_OutRR)
    # People_OutRR="\n".str(rPeople_OutRR)
    for e in People_OutR.readlines():
        k=1+k
    People_OutR.close()    
    k=k-1
    # print(k)
    if k >=int(o):
        People_OutR = open("People_Out.txt", "r")
        People_OutRR = People_OutR.read()
        People_OutRR=People_OutRR.split('\n')
        People_OutW = open("People_Out.txt", "w")
        People_OutRR.pop(0)
        People_OutWk = "\n".join(People_OutRR)
        People_OutW.write(People_OutWk)
        People_OutW.close()  
        # print(People_OutRR)
        Fase_3()
    else:
        print ('Correcto, dirigete a People_Out.txt para ver los resultados')
        People_OutR = open("People_Out.txt", "r")
        People_OutRR = People_OutR.read()
        print(People_OutRR)

# Accion
for x in range(2):
     Fase_1()

MemoryR = open("Memory.txt" , "r")
MEM = []
    # Memory.read()
    # recorrer txt
for linea in MemoryR.readlines():
    # print(linea)
    # TS = linea.split(" ")
    TS = linea.split("\n")
    # print(TS)
    TS= " ".join(TS)
    MEM.append(TS)
    # print('Lista',MEM)
    MEM= " ".join(MEM)
    # print('cadena',MEM)
    MEM = MEM.split(" ")
    # print('LAS',MEM)
    for e, i in enumerate(MEM):
        if i == '':
            MEM.pop(e)
        if len(i )==1:
            MEM.pop(e)
        if len(i )==2:
             MEM.pop(e)
    MEM = list(set(MEM))
    # MEM.append(Refe)
    MemoryR.close()   

# Escribir en memory
MemoryW  = open("Memory.txt" , "w")
L_MEM = MEM
MEM = " ".join(MEM)
MemoryW.write(MEM)
MemoryW.close()
o=input('Cunatos id desea ver en el resultado?, ejemplo: 100 o 5: ')
Fase_3()

f=input('Quires agregar nuevas palabras claves? presions S/N') 
if  f == 'S' or f == 's':
    Kw= input('\n Agrega alguna palabras claves: ')
    MemoryW  = open("Memory.txt" , "w") 
    MemoryR = open("Memory.txt", "r")
    R_MemoryR = MemoryR.read()
    R_MemoryR =''.join(R_MemoryR)
    MemoryR.close()
    MemoryW.write(R_MemoryR+Kw)
    MemoryW.close()
    Fase_2()
