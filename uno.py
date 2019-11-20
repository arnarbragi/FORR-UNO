#Höfundur Arnar Bragi Bragason og Jökull Freysteinsson
#UNO

import random
from spil import Spil


class Galdraspil:
    def draga2(self):
        for x in range(2):  # lykkja sem runnar þrisvar svo hægt sé að draga 3 spil í mesta lagi
            draga = spilastokkur.pop(0)  # tek efst af spilastokkinum
            print("Þú dróst", draga)  # prenta út spilið sem notandi dró
            if notandiUmferd == True:
                spilTolva1.append(draga) # set spilið í hönd
                tolva1Umferd = False
            elif tolva1Umferd == True and notandiUmferd == False:
                spilTolva2.append(draga)
                tolva2Umferd = False
            elif tolva2Tumferd == True and tolva1Umferd == False:
                spilTolva3.append(draga)
                tolva3Umferd = False
            elif tolva3Umferd == True and tolvaUmferd2 == False:
                print("Tölva3 lætur þig draga 2 spil")
                spilNotandi.append(draga)
                notandiUmferd = False

    def skipp(self):
        if notandiUmferd == True:
            tolva1Umferd = False
        elif tolva1Umferd == True and notandiUmferd == False:
            tolva2Umferd = False
        elif tolva2Umferd == True and tolva1Umferd == False:
            tolva3Umferd = False
        elif tolva3Umferd == True and tolva2Umferd == False:
            print("Tölva 3 bannar þér að gera ")
            notandiUmferd = False
    def party: #vantar fyrir tölvurnar
        print("1. Gulur")
        print("2. Rauður")
        print("3. Grænn")
        print("4. Blár")
        print()
        attaVal=int(input("Sláðu inn tölu tegundarinnar sem þú vilt breyta í: "))
        if attaVal==1:
            print("Þú breyttir í Gulan")
            settUt = Spil(1,0)
            kastbunki.insert(0,settUt)
        elif attaVal==2:
            print("Þú breyttir í Rauðan")
            settUt = Spil(2,0)
            kastbunki.insert(0,settUt)
        elif attaVal==3:
            print("Þú breyttir í Grænan")
            settUt = Spil(3,0)
            kastbunki.insert(0,settUt)
        elif attaVal==4:
            print("Þú breyttir í Bláan")
            settUt = Spil(4,0)
            kastbunki.insert(0,settUt)

    def party4(): #Óklárað
        for x in range(4):
                draga = spilastokkur.pop(0)  # tek efst af spilastokkinum
            if notandiUmferd == True:
                
                tolva1Umferd = False
            elif tolva1Umferd == True and notandiUmferd == False:
                tolva2Umferd = False
            elif tolva2Umferd == True and tolva1Umferd == False:
                tolva3Umferd = False
            elif tolva3Umferd == True and tolva2Umferd == False:
                print("Þú dróst", draga)  # prenta út spilið sem notandi dró
                notandiUmferd = False

            

tilvik = Spil(0,0)
spilastokkur = tilvik.geraSpilastokk()


spilNotandi=[] #bý til lista fyrir spilin á hendi notanda
spilTolva1=[] #bý til lista fyrir spilin á hendi tölvunnar
spilTolva2=[] 
spilTolva3=[]
kastbunki=[] #bý til lista fyrir öll spilin sem búið er að nota

for x in range(7): #gef notanda og tölvu fimm spil
    spilNotandi.append(spilastokkur.pop(0))
    spilTolva1.append(spilastokkur.pop(0))
    spilTolva2.append(spilastokkur.pop(0))
    spilTolva3.append(spilastokkur.pop(0))
kastbunki.append(spilastokkur.pop(0)) #set út eitt spil á borðið
print()

print("Spil Notanda:")
for x in spilNotandi:
    print(x)
print()
print("Spil Tölvu 1:")
for x in spilTolva1:
    print(x)
print()
print("Spil Tölvu 2:")
for x in spilTolva2:
    print(x)
print()
print("Spil Tölvu 3:")
for x in spilTolva3:
    print(x)
print()



UNO=False #bý til boolean breytur fyrir hvort notandi eða tölva hafi fengið olsen eða olsen olsen
UNOUNO=False
tolva1UNO=False
tolva1UNOUNO=False
tolva2UNO=False
tolva2UNOUNO=False
tolva3UNO=False
tolva3UNOUNO=False
#loop sem runnar þangað til að annaðhvort notandi eða tölva vinna
while len(spilNotandi)>=1 and len(spilTolva1)>=1 and len(spilTolva2)>=1 and len(spilTolva3)>=1:
    print("-"*5, "SPIL Á BORÐI", "-"*5)
    print(kastbunki[0])#prenta spilið sem var sett út síðast
    print()
    notandiUmferd=True
    tolva1Umferd=True
    tolva2Umferd=True
    tolva3Umferd=True
    
    #----------------------- Notandi gerir -----------------------
    if len(spilNotandi)>=2: #ef notandi hefur fleiri en 2 spil þá gerir það Olsen að false
        OLSEN=False
    while notandiUmferd: #loop sem runnar þangað til að notandi er búinn að gera
        tel=1
        print("-"*5, "SPIL Á HENDI", "-"*5)
        for x in spilNotandi:
            print(str(tel)+".",x)#prenta öll spilin sem notandi hefur á hendi
            tel+=1
        print("0. Draga")#notandi ýtir á 0 ef hann vill draga
        print("100. OLSEN")#notandi velur 100 til þess að segja olsen. þetta þarf að gera áður en þú setur út spilið
        print("1000. OLSEN OLSEN")#notandi velur 1000 til þess að segja olsen olsen. þarf að gera áður en síðasta spilið er sett út
        print()
        numer=int(input("Sláðu inn númer spilsins sem þú vilt nota: "))#tek inn hvað notandi vill gera
        print()
        if numer==0: #ef valið er 0 þá dregur notandi
            if len(spilastokkur)==0: #ef engin spil eru eftir í spilastokkinum er kastbunkanum snúið við
                for i in range(len(kastbunki)):
                    if kastbunki[i].nr == 0: #tek út öll spil sem ég bý til með áttunni
                        kastbunki.pop(i)
                for z in range(1,53):
                    faera = kastbunki.pop(z)
                    spilastokkur.insert(0,faera)
            leyfilegt=True
            #finn út hvort notandi geti gert eitthvað því ekki má draga nema þú getir ekki gert
            for y in range(len(spilNotandi)):
                if kastbunki[0].tegund == spilNotandi[y].tegund or kastbunki[0].nr == spilNotandi[y].nr or spilNotandi[y].nr==8:
                    leyfilegt=False
            if leyfilegt: #ef hann má draga þá...
                dreginSpil=0
                for x in range(3): #lykkja sem runnar þrisvar svo hægt sé að draga 3 spil í mesta lagi
                    draga=spilastokkur.pop(0)#tek efst af spilastokkinum
                    print("Þú dróst",draga)#prenta út spilið sem notandi dró
                    spilNotandi.append(draga) #set spilið í hönd notanda
                    #ef hann getur sett út spilið þá er spilið sett út
                    if kastbunki[0].tegund == spilNotandi[numer-1].tegund or kastbunki[0].nr == spilNotandi[numer-1].nr or spilNotandi[numer-1].nr==8:
                        print("Þú settir út",spilNotandi[numer-1])
                        settUt = spilNotandi.pop(numer-1)
                        kastbunki.insert(0,settUt)
                        if settUt.nr == 8: # ef spilið er átta er notanda leyft að velja tegundina sem hann vill breyta í
                            print("1. Hjarta")
                            print("2. Spaði")
                            print("3. Tígull")
                            print("4. Lauf")
                            print()
                            attaVal=int(input("Sláðu inn tölu tegundarinnar sem þú vilt breyta í: "))# tek inn val notanda
                            if attaVal==1: #til þess að breyta um ttegund bý ég til spil sem er í þeirri tegund með töluna 0
                                print("Þú breyttir í Hjarta")
                                settUt = Spil(1,0)
                                kastbunki.insert(0,settUt)
                            elif attaVal==2:
                                print("Þú breyttir í Spaða")
                                settUt = Spil(2,0)
                                kastbunki.insert(0,settUt)
                            elif attaVal==3:
                                print("Þú breyttir í Tígul")
                                settUt = Spil(3,0)
                                kastbunki.insert(0,settUt)
                            elif attaVal==4:
                                print("Þú breyttir í Lauf")
                                settUt = Spil(4,0)
                                kastbunki.insert(0,settUt)
                        notandiUmferd=False #enda umferð notanda
                        break
                    dreginSpil+=1
                if notandiUmferd:
                    if dreginSpil==3:#ef dregin eru þrjú spil ertu látinn segja pass
                        svar=input("Viltu segja pass?(j/n)")
                        if svar=="j" or svar=="J":
                            print("Notandi segir PASS")
                        else:
                            print("Þú þarft að segja pass") #ég veit... ég er mjög fyndinn :)
                            print("Notandi segir PASS")
                        print()
                        break
                break
            else:
                print("Þú getur sett út spil")
            print()
        elif numer==100: #ef notandi velur að segja olsen
            if len(spilNotandi)==2: #checkar hvort notandi hafi 2 spil á hendi
                leyfilegt=False
                for y in range(len(spilNotandi)):
                    #sér hvort notandi geti sett út spil 
                    if kastbunki[0].tegund == spilNotandi[y].tegund or kastbunki[0].nr == spilNotandi[y].nr or spilNotandi[y].nr == 8:
                        leyfilegt=True
                if leyfilegt:
                    OLSEN=True #olsen er orðið satt
                    print("Notandi segir OLSEN!")
                else:
                    print("Þú getur ekki sagt OLSEN núna")
            else:
                print("Þú getur ekki sagt OLSEN núna") #ef hann annaðhvort hefur of mörg spil eða getur ekki gert þá má hann ekki segja olsen
            print()
        elif numer==1000:#ef notandi velur að segja olsen olsen
            if len(spilNotandi)==1:#sér hvort notandi hafi bara eitt spil eftir
                leyfilegt=False
                for y in range(len(spilNotandi)):
                    #sér hvort hann geti sett út síðasta spilið
                    if kastbunki[0].tegund == spilNotandi[y].tegund or kastbunki[0].nr == spilNotandi[y].nr or spilNotandi[y].nr == 8:
                        leyfilegt=True
                if leyfilegt:
                    OLSENOLSEN=True #olsen olsen er orðið satt
                    print("Notandi segir OLSEN OLSEN!!!")
                else:
                    print("Þú getur ekki sagt OLSEN OLSEN núna")
            else:
                print("Þú getur ekki sagt OLSEN OLSEN núna")#ekki má segja olsen olsen ef þú hefur fleiri en eitt spil eða ef þú getur ekki gert
            print()
        #ef notandi velur spil þá...
        else:
            #skoðar hvort hægt sé að nota spilið
            if kastbunki[0].tegund == spilNotandi[numer-1].tegund or kastbunki[0].nr == spilNotandi[numer-1].nr or spilNotandi[numer-1].nr == 8:
                print("Þú settir út",spilNotandi[numer-1])
                settUt = spilNotandi.pop(numer-1)#tekur spilið úr hendi notanda
                kastbunki.insert(0,settUt)#setur spilið efst í kastbunkann
                if settUt.nr == 8: #ef sett er út átta má notandi velja tegund
                    print("1. Hjarta")
                    print("2. Spaði")
                    print("3. Tígull")
                    print("4. Lauf")
                    print()
                    attaVal=int(input("Sláðu inn tölu tegundarinnar sem þú vilt breyta í: "))
                    if attaVal==1:
                        print("Þú breyttir í Hjarta")
                        settUt = Spil(1,0)
                        kastbunki.insert(0,settUt)
                    elif attaVal==2:
                        print("Þú breyttir í Spaða")
                        settUt = Spil(2,0)
                        kastbunki.insert(0,settUt)
                    elif attaVal==3:
                        print("Þú breyttir í Tígul")
                        settUt = Spil(3,0)
                        kastbunki.insert(0,settUt)
                    elif attaVal==4:
                        print("Þú breyttir í Lauf")
                        settUt = Spil(4,0)
                        kastbunki.insert(0,settUt)
                notandiUmferd=False #endar umferð notanda
                if len(spilNotandi)==1:#skoða hvort notandi gleymdi að segja olsen
                    if OLSEN:
                        pass
                    else:#ef notandi gleymir að segja olsen er hann látinn draga 3 spil
                        print("Þú gleymdir að segja OLSEN og þarft að draga 3 spil")
                        for x in range(3):
                            draga=spilastokkur.pop(0)
                            print("Þú dróst",draga)
                            spilNotandi.append(draga)
                if len(spilNotandi)==0:#skoða hvort notandi gleymdi að segja olsen olsen
                    if OLSENOLSEN:
                        tolvaUmferd=False
                        break
                    else: #ef notandi gleymir er hann látinn draga 3 spil
                        print("Þú gleymdir að segja OLSEN OLSEN og þarft að draga 3 spil")
                        for x in range(3):
                            draga=spilastokkur.pop(0)
                            print("Þú dróst",draga)
                            spilNotandi.append(draga)
                break
            else:
                print("Þú getur ekki sett út þetta spil, veldu aftur")#ef ekki er hægt að setja út spilið sem notandi velur
            print()

    print("-"*5, "SPIL Á BORÐI", "-"*5)
    print(kastbunki[0])#prenta spilið sem var sett út síðast
    print()
    '''
    #----------------------- Tölva gerir -----------------------
    tolvaDraga=False
    while tolvaUmferd:#lykkja sem runnar þangað til tölvan er búin að gera
        if len(spilTolva)==2:#ef tölvan hefur 2 spil eftir og getur sett út spil þá segir hún olsen
            leyfilegt=False
            for y in range(len(spilTolva)):
                if kastbunki[0].tegund == spilTolva[y].tegund or kastbunki[0].nr == spilTolva[y].nr or spilTolva[y].nr == 8:
                    leyfilegt=True
                if leyfilegt:
                    tolvaOLSEN=True
                    print("Tölva segir OLSEN!")
                    break
        if len(spilTolva)==1:#ef tölva hefur eitt spil eftir og getur sett það út segir hún olsen olsen
            leyfilegt=False
            for y in range(len(spilTolva)):
                if kastbunki[0].tegund == spilTolva[y].tegund or kastbunki[0].nr == spilTolva[y].nr or spilTolva[y].nr == 8:
                    leyfilegt=True
                if leyfilegt:
                    tolvaOLSENOLSEN=True
                    print("Tölva segir OLSEN OLSEN!!!")
        for y in range(len(spilTolva)):
            #tölvan fer í gegnum spilin sín og setur út fyrsta spilið sem hún getur
            if kastbunki[0].tegund == spilTolva[y].tegund or kastbunki[0].nr == spilTolva[y].nr or spilTolva[y].nr == 8:
                print("Tölvan setti út",spilTolva[y])
                settUt2 = spilTolva.pop(y)
                kastbunki.insert(0,settUt2)
                if settUt2.nr == 8: # ef tölvan setur út áttu velur hún randomly tegund
                    attaVal=random.randint(1,4)
                    if attaVal==1:
                        print("Tölvan breytti í Hjarta")
                        settUt = Spil(1,0)
                        kastbunki.insert(0,settUt)
                    elif attaVal==2:
                        print("Tölvan breytti í Spaða")
                        settUt = Spil(2,0)
                        kastbunki.insert(0,settUt)
                    elif attaVal==3:
                        print("Tölvan breytti í Tígul")
                        settUt = Spil(3,0)
                        kastbunki.insert(0,settUt)
                    elif attaVal==4:
                        print("Tölvan breytti í Lauf")
                        settUt = Spil(4,0)
                        kastbunki.insert(0,settUt)
                tolvaUmferd=False #enda umferð tölvunnar
                break
            else:
                if len(spilTolva)==1: #ef það er eitt spil eftir og ekki er hægt að setja það út dregur tölvan spil
                    tolvaDraga=True
                elif y == (len(spilTolva)-1):
                    tolvaDraga=True #ef tölvan getur ekki notað neitt af spilunum sínum dregur hún
                    break
                else:
                    pass #ef ekki er hægt að nota spilið en tölvan er ekki búin að skoða öll spilin fer hún á næsta spil
            if tolvaDraga: #ef tölvan þarf að draga þá...
                if len(spilastokkur)==0:#ef engin spil eru í spilastokknum þá sný ég kastbunkanum við
                    for i in range(len(kastbunki)):
                        if kastbunki[i].nr == 0:#eyði öllum spilum sem ég bý til með áttunni
                            kastbunki.pop(i)
                    for z in range(1,53):
                        faera = kastbunki.pop(z)
                        spilastokkur.insert(0,faera)
                dreginSpil=0
                for x in range(3):#lykkja sem runnar þrisvar svo hægt sé að draga 3 spil í mesta lagi
                    draga=spilastokkur.pop(0)#tek spil úr spilastokknum
                    print("Tölva dró")#segi að tölvan hafi dregið en ekki hvað hún dró. Þetta er keppni
                    spilTolva.append(draga)#set spilið í hendi tölvunnar
                    if kastbunki[0].tegund == draga.tegund or kastbunki[0].nr == draga.nr or draga.nr == 8: #ef hægt er að ssetja út spilið setur tölvan spilið út
                        print("Tölvan setti út",draga)
                        settUt = spilTolva.pop(-1)
                        kastbunki.insert(0,settUt)
                        if settUt.nr == 8: #ef tölvan setur út átta velur hún random tegund
                            attaVal=random.randint(1,4)
                            if attaVal==1:
                                print("Tölvan breytti í Hjarta")
                                settUt = Spil(1,0)
                                kastbunki.insert(0,settUt)
                            elif attaVal==2:
                                print("Tölvan breytti í Spaða")
                                settUt = Spil(2,0)
                                kastbunki.insert(0,settUt)
                            elif attaVal==3:
                                print("Tölvan breytti í Tígul")
                                settUt = Spil(3,0)
                                kastbunki.insert(0,settUt)
                            elif attaVal==4:
                                print("Tölvan breytti í Lauf")
                                settUt = Spil(4,0)
                                kastbunki.insert(0,settUt)
                            tolvaUmferd=False
                        break
                    dreginSpil+=1
                if tolvaUmferd:
                    if dreginSpil == 3:#ef tölvan dregur 3 spil og getur ennþá ekki gert segir hún pass
                        print("Tölvan segir PASS")
                tolvaUmferd=False
                break
        print()

if len(spilNotandi)==0:#ef notandi kláraði spilin sín/vann
    print("ÞÚ VANNST!!! TIL HAMINGJU!!!")
elif len(spilTolva)==0:#ef tölvan kláraði spilin sín/vann
    print("TÖLVAN VANN!!! Gengur betur næst!")
'''
