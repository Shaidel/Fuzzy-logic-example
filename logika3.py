import numpy as np
import matplotlib.pyplot as plt

ZbX=np.zeros((5,101))
ZbY=np.zeros((4,101))
ZbZ=np.zeros ((18,61))

ZmmTemp = float(input("Podaj temperaturę: "))
ZmTemp = int(ZmmTemp)
ZmmWilg = float(input("Podaj wilgotnosc: "))
ZmWilg = int(ZmmWilg)

L = 0
M = 0

for i in range(0,101):
    
    x=i/2
    ZbX[0,i]=x
    
    #zimno
    if x>= 0 and x<=5 :
        uA=1
    elif x>=5 and x<=15:
        uA=(15-x)/(15-5)
    else:
        uA=0
    ZbX[1,i] = uA
    
    #letnio
    if x>=5 and x<=15:
        uB = (x-5)/(15-5)
    elif x>=15 and x<=25:
        uB = (25-x)/(25-15)
    else: 
        uB=0
    ZbX[2,i]=uB
    
    #ciepło
    if x>=15 and x<=25:
        uC = (x-15)/(25-15)
    elif x>=25 and x<=35:
        uC = (35-x)/(35-25)
    else: 
        uC=0
    ZbX[3,i]=uC
    
    #gorąco
    if x>=25 and x<=35:
        uD=(x-25)/(35-25);
    elif x>=35 and x<=150:
        uD=1;
    else: 
        uD = 0;
    ZbX[4,i]=uD;
    
for i in range(0,101):
    
    y=i
    ZbY[0,i]=y
    
    #mała
    if y>= 0 and y<=25 :
        uE=1
    elif y>=25 and y<=50:
        uE=(50-y)/(50-25)
    else:
        uE=0
    ZbY[1,i] = uE
    
    #srednia
    if y>=25 and y<=50:
        uF = (y-25)/(50-25)
    elif y>=50 and y<=100:
        uF = (100-y)/(100-50)
    else: 
        uF=0
    ZbY[2,i]=uF
    
    #duża
    if y>=50 and y<=100:
        uG = (y-50)/(100-50)
    else: 
        uG=0
    ZbY[3,i]=uG
    
    
#podpunkt C - Zm*2, bo krok dyskretyzacji 0,5, zapis uA = X(2,(Zm*2)+1) pod zmienną uA podstawia
#elemtent tablicy z wiersza 2 i kolumny adekwatnej dla inputa Zm
uAr = ZbX[1,(ZmTemp*2)]
uBr = ZbX[2,(ZmTemp*2)]
uCr = ZbX[3,(ZmTemp*2)]
uDr = ZbX[4,(ZmTemp*2)]

#print("Temp zimno")
print(uAr) # po prostu wyświetla wynik na konsoli
print(uBr)
print(uCr)
print(uDr)

uEr = ZbY[1,(ZmWilg)]
uFr = ZbY[2,(ZmWilg)]
uGr = ZbY[3,(ZmWilg)]

print(uEr) # po prostu wyświetla wynik na konsoli
print(uFr)
print(uGr)

for i in range(0,61):   #termy wyjsciowe Czas Podlewania
     #Y
    z=i
    ZbZ[0,i]=z
    
    #minimum
    if z>= 0 and z<=15 :
        uH=(15-z)/(15-0)
    else: 
        uH = 0
    ZbZ[1,i] = uH
    
     #krótki
    if z>=0 and z<=15:
        uI = (z-0)/(15-0)
    elif z>=15 and z<=30:
        uI = (30-z)/(30-15)
    else: 
        uI=0
    ZbZ[2,i]=uI
    
     #sredni
    if z>=15 and z<=30:
        uJ = (z-15)/(30-15)
    elif z>=30 and z<=45:
        uJ = (45-z)/(45-30)
    else: 
        uJ=0
    ZbZ[3,i]=uJ
    
     #długi
    if z>=30 and z<=45:
        uK = (z-30)/(45-30)
    elif z>=45 and z<=60:
        uK = (60-z)/(60-45)
    else: 
        uK=0
    ZbZ[4,i]=uK
    
    
    #maximum
    if z>=45 and z<=60:
        uL = (z-45)/(60-45)
    else: 
        uL=0
    ZbZ[5,i]=uL
    
    #R1
    if z>= 0 and z<=15 :
        uR1=(15-z)/(15-0)
    else: 
        uR1 = 0
    if uR1 > max(min(uAr,uGr),min(uBr,uGr)): #baza reguł z podpunktu D bazująca na zmiennej uA
        uR1 = max(min(uAr,uGr),min(uBr,uGr))
    
    ZbZ[6,i]=uR1
    
    #R2
    if z>=0 and z<=15:
        uR2 = (z-0)/(15-0)
    elif z>=15 and z<=30:
        uR2 = (30-z)/(30-15)
    else: 
        uR2=0
    if uR2 > max(min(uAr,uFr),min(uBr,uFr),min(uCr,uGr)): #baza reguł z podpunktu D bazująca na zmiennej uA
        uR2 = max(min(uAr,uFr),min(uBr,uFr),min(uCr,uGr))
    ZbZ[7,i]=uR2
    
    #R3
    if z>=15 and z<=30:
        uR3 = (z-15)/(30-15)
    elif z>=30 and z<=45:
        uR3 = (45-z)/(45-30)
    else: 
        uR3=0
    if uR3 > max(min(uAr,uEr),min(uCr,uFr),min(uDr,uGr)): #baza reguł z podpunktu D bazująca na zmiennej uA
        uR3 = max(min(uAr,uEr),min(uCr,uFr),min(uDr,uGr))
    ZbZ[8,i]=uR3
    
    #R4
    if z>=30 and z<=45:
        uR4 = (z-30)/(45-30)
    elif z>=45 and z<=60:
        uR4 = (60-z)/(60-45)
    else: 
        uR4=0
    if uR4 > max(min(uBr,uEr),min(uCr,uEr),min(uDr,uFr)): #baza reguł z podpunktu D bazująca na zmiennej uA
        uR4 = max(min(uBr,uEr),min(uCr,uEr),min(uDr,uFr))
    ZbZ[9,i]=uR4
    
    #R5
    if z>=45 and z<=60:
        uR5 = (z-45)/(60-45)
    else: 
        uR5=0
    if uR5 > min(uDr,uEr):
        uR5 = min(uDr,uEr)
    ZbZ[10,i]=uR5
    
    ZbZ[11,i]= max(ZbZ[6,i],ZbZ[7,i],ZbZ[8,i],ZbZ[9,i],ZbZ[10,i]) # podpunkt E, czyli zsumowanie bazy reguł z podpunktu D
    #f
    L = L + (ZbZ[0,i] *ZbZ[11,i]) # działania dla podpunktu F
    M= M+ZbZ[11,i]   
    
    
YO = L/M   
print (YO)
    


plt.subplot(5,1,1)
plt.plot(ZbX[0,:],ZbX[1,:],'r')
plt.plot(ZbX[0,:],ZbX[2,:],'b')
plt.plot(ZbX[0,:],ZbX[3,:],'g')
plt.plot(ZbX[0,:],ZbX[4,:],'y')
plt.axis([0,50,0,1.1])
plt.xlabel('Temperatura [C]')
plt.ylabel('u(Temperatura)')

plt.subplot(5,1,2)
plt.plot(ZbY[0,:],ZbY[1,:],'r')
plt.plot(ZbY[0,:],ZbY[2,:],'b')
plt.plot(ZbY[0,:],ZbY[3,:],'g')
plt.axis([0,100,0,1.1])
plt.xlabel('Wilgotnoć [%]')
plt.ylabel('u(Wilgotnoć)')

plt.subplot(5,1,3)
plt.plot(ZbZ[0,:],ZbZ[1,:],'r')
plt.plot(ZbZ[0,:],ZbZ[2,:],'b')
plt.plot(ZbZ[0,:],ZbZ[3,:],'g')
plt.plot(ZbZ[0,:],ZbZ[4,:],'y')
plt.plot(ZbZ[0,:],ZbZ[5,:],'c')
plt.axis([0,60,0,1.1])
plt.xlabel('Czas podlewania [m]')
plt.ylabel('u(Czas podlewania)')

plt.subplot(5,1,4)
plt.plot(ZbZ[0,:],ZbZ[6,:],'r')
plt.plot(ZbZ[0,:],ZbZ[7,:],'b')
plt.plot(ZbZ[0,:],ZbZ[8,:],'g')
plt.plot(ZbZ[0,:],ZbZ[9,:],'y')
plt.plot(ZbZ[0,:],ZbZ[10,:],'c')
plt.axis([0,60,0,1.1])
plt.xlabel('Czas podlewania [m]')
plt.ylabel('u(Czas podlewania)')

plt.subplot(5,1,5)
plt.plot(ZbZ[0,:],ZbZ[11,:],'r')
plt.axis([0,60,0,1.1])
plt.xlabel('Czas podlewania [m]')
plt.ylabel('u(Czas podlewania)')