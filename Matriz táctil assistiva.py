
from espeak import espeak 
import os

import time


import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)      
#abaixo vamos zerar o contador quando iniciarmos a rasp
contador11 = 0
contador13 = 0
contador14 = 0
contador21 = 0
contador25 = 0
contador26 = 0
contador31 = 0
contador33 = 0
contador34 = 0
contador36 = 0
contador44 = 0
contador46 = 0
contador51 = 0
contador52 = 0
contador53 = 0
contador61 = 0
contador63 = 0
contador64 = 0
contador65 = 0
contador66 = 0
contador71 = 0
contador73 = 0
contador74 = 0
contador75 = 0
contador82 = 0
contador83 = 0
contador85 = 0
contador86 = 0
contador91 = 0
contador92 = 0
contador93 = 0
contador96 = 0
contador101 = 0
contador102 = 0
contador104 = 0
contador106 = 0
contador111 = 0
contador114 = 0
contador116 = 0
contador121 = 0
contador122 = 0
contador126 = 0
contador131 = 0
contador132 = 0
contador133 = 0
contador134 = 0
contador135 = 0
contador141 = 0
contador143 = 0
contador144 = 0
contador146 = 0
#continue a sequencia acima no padrão contadorXX(onde XX são os mesmos numeros que utilizamos nos global)
Y1=14    
Y2=15    
Y3=17
Y4=23
Y5=24
Y6=25
Y7=8
Y8=12
Y9=16
Y10=20
Y11=21
Y12=2
Y13=3
Y14=19
I1=27
I2=22
I3=10
I4=9
I5=5
I6=6

GPIO.setup(Y1,GPIO.OUT)
GPIO.setup(Y2,GPIO.OUT)
GPIO.setup(Y3,GPIO.OUT)
GPIO.setup(Y4,GPIO.OUT)
GPIO.setup(Y5,GPIO.OUT)
GPIO.setup(Y6,GPIO.OUT)
GPIO.setup(Y7,GPIO.OUT)
GPIO.setup(Y8,GPIO.OUT)
GPIO.setup(Y9,GPIO.OUT)
GPIO.setup(Y10,GPIO.OUT)
GPIO.setup(Y11,GPIO.OUT)
GPIO.setup(Y12,GPIO.OUT)
GPIO.setup(Y13,GPIO.OUT)
GPIO.setup(Y14,GPIO.OUT)
GPIO.setup(I1,GPIO.IN)
GPIO.setup(I2,GPIO.IN)
GPIO.setup(I3,GPIO.IN)
GPIO.setup(I4,GPIO.IN)
GPIO.setup(I5,GPIO.IN)
GPIO.setup(I6,GPIO.IN)
#GPIO.setup(I3,GPIO.IN)

#Partida do sistema com as saidas desligadas
GPIO.output(Y1,0)
GPIO.output(Y2,0)
GPIO.output(Y3,0)
GPIO.output(Y4,0)
GPIO.output(Y5,0)
GPIO.output(Y6,0)
GPIO.output(Y7,0)
GPIO.output(Y8,0)
GPIO.output(Y9,0)
GPIO.output(Y10,0)
GPIO.output(Y11,0)
GPIO.output(Y12,0)
GPIO.output(Y13,0)
GPIO.output(Y14,0)

def status_input():
    global contador11
    global contador13
    global contador14
    global contador21
    global contador25
    global contador26
    global contador31
    global contador33
    global contador34
    global contador36
    global contador44
    global contador46
    global contador51
    global contador52
    global contador53
    global contador61
    global contador63
    global contador64
    global contador65
    global contador66
    global contador71
    global contador73
    global contador74
    global contador75
    global contador82
    global contador83
    global contador85
    global contador86
    global contador91
    global contador92
    global contador93
    global contador96
    global contador101
    global contador102
    global contador104
    global contador106
    global contador111
    global contador114
    global contador116
    global contador121
    global contador122
    global contador126
    global contador131
    global contador132
    global contador133
    global contador134
    global contador135
    global contador141
    global contador143
    global contador144
    global contador146
    
    status_I1=GPIO.input(I1)
    status_I2=GPIO.input(I2)
    status_I3=GPIO.input(I3)
    status_I4=GPIO.input(I4)
    status_I5=GPIO.input(I5)
    status_I6=GPIO.input(I6)

    if(GPIO.input(Y1)==True):
	#print("coluna1")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I1.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a1.mp3")
	    contador11 = contador11 + 1 #Acrescentar essas 3 linhas nos locais onde tem a linha "ossystem", se atentando para mundança do número do contador - linha 1
	    print("Pulsos na imagem 11: ",contador11)# = linha 2
	    time.sleep(1.5)# - linha 3
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I1.2")
            
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I1.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a4.mp3")
            contador13 = contador13 + 1 #Acrescentar essas 3 linhas nos locais onde tem a linha "ossystem", se atentando para mundança do número do contador - linha 1
	    print("Pulsos na imagem 13: ",contador13)# - linha 2
	    time.sleep(1.5)# - linha 3
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I1.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a5.mp3")
            contador14 = contador14 + 1
	    print("Pulsos na imagem 14: ",contador14)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I1.5")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I1.6")
    if(GPIO.input(Y2)==True):
	#print("coluna2")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I2.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a2.mp3")
	    contador21 = contador21 + 1
	    print("Pulsos na imagem 21: ",contador21)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I2.2")
            
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I2.3")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I2.4")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I2.5")
            os.system("mpg321 /home/pi/Music/AUDIOS/a7.mp3")
            contador25 = contador25 + 1
	    print("Pulsos na imagem 25: ",contador25)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I2.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a6.mp3")
	    contador26 = contador26 + 1
	    print("Pulsos na imagem 26: ",contador26)
	    time.sleep(1.5)
    if(GPIO.input(Y3)==True):
	#print("coluna3")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I3.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a3.mp3")
	    contador31 = contador31 + 1
	    print(contador31)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I3.2")
            
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I3.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a81.mp3")
            contador33 = contador33 + 1
	    print("Pulsos na imagem 33: ",contador33)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I3.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a91.mp3")
            contador34 = contador34 + 1
	    print("Pulsos na imagem 34: ",contador34)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I3.5")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I3.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a10.mp3")
	    contador36 = contador36 + 1
	    print("Pulsos na imagem 36: ",contador36)
	    time.sleep(1.5)
    if(GPIO.input(Y4)==True):
	#print("coluna4")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I4.1")
	    
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I4.2")
            
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I4.3")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I4.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a11.mp3")
            contador44 = contador44 + 1
	    print("Pulsos na imagem 44: ",contador44)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I4.5")
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I4.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a13.mp3")
	    contador46 = contador46 + 1
	    print("Pulsos na imagem 46: ",contador46)
	    time.sleep(1.5)
    if(GPIO.input(Y5)==True):
	#print("coluna5")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I5.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a8.mp3")
	    contador51 = contador51 + 1
	    print("Pulsos na imagem 51: ",contador51)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I5.2")
            os.system("mpg321 /home/pi/Music/AUDIOS/a9.mp3")
            contador52 = contador52 + 1
	    print("Pulsos na imagem 52: ",contador52)
	    time.sleep(1.5)
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I5.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a12.mp3")
            contador53 = contador53 + 1
	    print("Pulsos na imagem 53: ",contador53)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I5.4")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I5.5")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I5.6")
    if(GPIO.input(Y6)==True):
	#print("coluna6")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I6.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a61.mp3")
	    contador61 = contador61 + 1
	    print("Pulsos na imagem 61: ",contador61)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I6.2")
            
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I6.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a14.mp3")
            contador63 = contador63 + 1
	    print("Pulsos na imagem 63: ",contador63)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I6.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a17.mp3")
            contador64 = contador64 + 1
	    print("Pulsos na imagem 64: ",contador64)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I6.5")
            os.system("mpg321 /home/pi/Music/AUDIOS/a18.mp3")
            contador65 = contador65 + 1
	    print("Pulsos na imagem 65: ",contador65)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I6.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a191.mp3")
	    contador66 = contador66 + 1
	    print("Pulsos na imagem 66: ",contador66)
	    time.sleep(1.5)
    if(GPIO.input(Y7)==True):
	#print("coluna7")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I7.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a15.mp3")
	    contador71 = contador71 + 1
	    print("Pulsos na imagem 71: ",contador71)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I7.2")
            
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I7.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a16.mp3")
            contador73 = contador73 + 1
	    print("Pulsos na imagem 73: ",contador73)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I7.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a19.mp3")
            contador74 = contador74 + 1
	    print("Pulsos na imagem 74: ",contador74)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I7.5")
            os.system("mpg321 /home/pi/Music/AUDIOS/a21.mp3")
            contador75 = contador75 + 1
	    print("Pulsos na imagem 75: ",contador75)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I7.6")
    if(GPIO.input(Y8)==True):
	#print("coluna8")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I8.1")
	    
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I8.2")
            os.system("mpg321 /home/pi/Music/AUDIOS/a15.mp3")
            contador82 = contador82 + 1
	    print("Pulsos na imagem 82: ",contador82)
	    time.sleep(1.5)
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I8.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a20.mp3")
            contador83 = contador83 + 1
	    print("Pulsos na imagem 83: ",contador83)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I8.4")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I8.5")
            os.system("mpg321 /home/pi/Music/AUDIOS/a22.mp3")
            contador85 = contador85 + 1
	    print("Pulsos na imagem 85: ",contador85)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I8.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a23.mp3")
	    contador86 = contador86 + 1
	    print("Pulsos na imagem 86: ",contador86)
	    time.sleep(1.5)
    if(GPIO.input(Y9)==True):
	#print("coluna9")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I9.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a24.mp3")
	    contador91 = contador91 + 1
	    print("Pulsos na imagem 91: ",contador91)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I9.2")
            os.system("mpg321 /home/pi/Music/AUDIOS/a25.mp3")
            contador92 = contador92 + 1
	    print("Pulsos na imagem 92: ",contador92)
	    time.sleep(1.5)
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I9.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a26.mp3")
            contador93 = contador93 + 1
	    print("Pulsos na imagem 93: ",contador93)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I9.4")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I9.5")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I9.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a27.mp3")
	    contador96 = contador96 + 1
	    print("Pulsos na imagem 96: ",contador96)
	    time.sleep(1.5)
    if(GPIO.input(Y10)==True):
	#print("coluna10")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I10.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a34.mp3")
	    contador101 = contador101 + 1
	    print("Pulsos na imagem 101: ",contador101)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I10.2")
            os.system("mpg321 /home/pi/Music/AUDIOS/a28.mp3")
            contador102 = contador102 + 1
	    print("Pulsos na imagem 102: ",contador102)
	    time.sleep(1.5)
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I10.3")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I10.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a29.mp3")
            contador104 = contador104 + 1
	    print("Pulsos na imagem 104: ",contador104)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I10.5")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I10.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a30.mp3")
	    contador106 = contador106 + 1
	    print("Pulsos na imagem 106: ",contador106)
	    time.sleep(1.5)
    if(GPIO.input(Y11)==True):
	#print("coluna11")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I11.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a35.mp3")
	    contador111 = contador111 + 1
	    print("Pulsos na imagem 111: ",contador111)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I11.2")
            
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I11.3")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I11.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a33.mp3")
            contador114 = contador114 + 1
	    print("Pulsos na imagem 114: ",contador114)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I11.5")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I11.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a31.mp3")
	    contador116 = contador116 + 1
	    print("Pulsos na imagem 116: ",contador116)
	    time.sleep(1.5)
    if(GPIO.input(Y12)==True):
	#print("coluna12")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I12.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a36.mp3")
	    contador121 = contador121 + 1
	    print("Pulsos na imagem 121: ",contador121)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I12.2")
            os.system("mpg321 /home/pi/Music/AUDIOS/a37.mp3")
            contador122 = contador122 + 1
	    print("Pulsos na imagem 122: ",contador122)
	    time.sleep(1.5)
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I12.3")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I12.4")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I12.5")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I12.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a32.mp3")
	    contador126 = contador126 + 1
	    print("Pulsos na imagem 126: ",contador126)
	    time.sleep(1.5)
    if(GPIO.input(Y13)==True):
	#print("coluna13")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I13.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a38.mp3")
	    contador131 = contador131 + 1
	    print("Pulsos na imagem 131: ",contador131)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I13.2")
            os.system("mpg321 /home/pi/Music/AUDIOS/a42.mp3")
            contador132 = contador132 + 1
	    print("Pulsos na imagem 132: ",contador132)
	    time.sleep(1.5)
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I13.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a41.mp3")
            contador133 = contador133 + 1
	    print("Pulsos na imagem1331: ",contador133)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I13.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a40.mp3")
            contador134 = contador134 + 1
	    print("Pulsos na imagem 134: ",contador134)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I13.5")
            os.system("mpg321 /home/pi/Music/AUDIOS/a39.mp3")
            contador91 = contador135 + 1
	    print("Pulsos na imagem 135: ",contador135)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I13.6")
    if(GPIO.input(Y14)==True):
	#print("coluna14")
        if((status_I1==True)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I14.1")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a43.mp3")
	    contador141 = contador141 + 1
	    print("Pulsos na imagem 141: ",contador141)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==True)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I14.2")
            
	if((status_I1==False)and(status_I2==False)and(status_I3==True)and(status_I4==False)and(status_I5==False)and(status_I6==False)):
            print("I14.3")
            os.system("mpg321 /home/pi/Music/AUDIOS/a44.mp3")
            contador143 = contador143 + 1
	    print("Pulsos na imagem 143: ",contador143)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==True)and(status_I5==False)and(status_I6==False)):
            print("I14.4")
            os.system("mpg321 /home/pi/Music/AUDIOS/a45.mp3")
            contador144 = contador144 + 1
	    print("Pulsos na imagem 144: ",contador144)
	    time.sleep(1.5)
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==True)and(status_I6==False)):
            print("I14.5")
            
        if((status_I1==False)and(status_I2==False)and(status_I3==False)and(status_I4==False)and(status_I5==False)and(status_I6==True)):
            print("I14.6")
	    os.system("mpg321 /home/pi/Music/AUDIOS/a46.mp3")
	    contador146 = contador146 + 1
	    print("Pulsos na imagem 146: ",contador146)
	    time.sleep(1.5)
    #abaixo temos um código que organiza os contadores e cria uma interface com o usuário para que ele escolha qual dado deseja visualizar
    lista = [0, contador11, contadorXX, contadorXX, contador146]
    #acima coloque todos os contadores naquele mesmo esquema(espaço depois da virgula)
    numerodocontador = int(input("Digite o contador: "))
    lista(numerodocontador)
    
while(1):
    GPIO.output(Y1,1)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()
    
    GPIO.output(Y1,0)
    GPIO.output(Y2,1)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,1)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,1)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,1)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,1)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()


    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,1)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,1)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,1)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,1)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,1)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,1)
    GPIO.output(Y13,0)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,1)
    GPIO.output(Y14,0)
    status_input()

    GPIO.output(Y1,0)
    GPIO.output(Y2,0)
    GPIO.output(Y3,0)
    GPIO.output(Y4,0)
    GPIO.output(Y5,0)
    GPIO.output(Y6,0)
    GPIO.output(Y7,0)
    GPIO.output(Y8,0)
    GPIO.output(Y9,0)
    GPIO.output(Y10,0)
    GPIO.output(Y11,0)
    GPIO.output(Y12,0)
    GPIO.output(Y13,0)
    GPIO.output(Y14,1)
    status_input()
    
    GPIO.cleanup




