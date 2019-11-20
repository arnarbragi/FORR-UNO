


#----------------------- Notandi gerir -----------------------
    if len(spilNotandi)>=2: #ef notandi hefur fleiri en 2 spil þá gerir það UNO að false
        UNO=False
    while notandiUmferd: #loop sem runnar þangað til að notandi er búinn að gera
        tel=1
        print("-"*5, "SPIL Á HENDI", "-"*5)
        for x in spilNotandi:
            print(str(tel)+".",x)#prenta öll spilin sem notandi hefur á hendi
            tel+=1
        print("0. Draga")#notandi ýtir á 0 ef hann vill draga
        print("100. UNO")#notandi velur 100 til þess að segja olsen. þetta þarf að gera áður en þú setur út spilið
        print("1000. UNO UNO")#notandi velur 1000 til þess að segja olsen olsen. þarf að gera áður en síðasta spilið er sett út
        print()
        numer=int(input("Sláðu inn númer spilsins sem þú vilt nota: "))#tek inn hvað notandi vill gera
        print()
        if numer==0: #ef valið er 0 þá dregur notandi
            if len(spilastokkur)==0: #ef engin spil eru eftir í spilastokkinum er kastbunkanum snúið við
                for i in range(len(kastbunki)):
                    if kastbunki[i].nr == 0: #tek út öll spil sem ég bý til með áttunni
                        kastbunki.pop(i)
                for z in range(1,109):
                    faera = kastbunki.pop(z)
                    spilastokkur.insert(0,faera)
            leyfilegt=True
            #finn út hvort notandi geti gert eitthvað því ekki má draga nema þú getir ekki gert
            for y in range(len(spilNotandi)):
                if kastbunki[0].tegund == spilNotandi[y].tegund or kastbunki[0].nr == spilNotandi[y].nr or spilNotandi[y].nr==12 or spilNotandi[y].nr==13:
                    leyfilegt=False
            if leyfilegt: #ef hann má draga þá...
                dreginSpil=0
                for x in range(3): #lykkja sem runnar þrisvar svo hægt sé að draga 3 spil í mesta lagi
                    draga=spilastokkur.pop(0)#tek efst af spilastokkinum
                    print("Þú dróst",draga)#prenta út spilið sem notandi dró
                    spilNotandi.append(draga) #set spilið í hönd notanda
                    #ef hann getur sett út spilið þá er spilið sett út
                    if kastbunki[0].tegund == spilNotandi[numer-1].tegund or kastbunki[0].nr == spilNotandi[numer-1].nr or spilNotandi[numer-1].nr==12 or spilNotandi[numer-1].nr==13:
                        print("Þú settir út",spilNotandi[numer-1])
                        settUt = spilNotandi.pop(numer-1)
                        kastbunki.insert(0,settUt)
                        if settUt.nr == 12: # ef spilið er partý er notanda leyft að velja tegundina sem hann vill breyta í
                            print("1. Gulur")
                            print("2. Rauður")
                            print("3. Grænn")
                            print("4. Blár")
                            print()
                            litaVal=int(input("Sláðu inn tölu tegundarinnar sem þú vilt breyta í: "))# tek inn val notanda
                            if litaVal==1: #til þess að breyta um ttegund bý ég til spil sem er í þeirri tegund með töluna 0
                                print("Þú breyttir í Gulan")
                                settUt = Spil(1,0)
                                kastbunki.insert(0,settUt)
                            elif litaVal==2:
                                print("Þú breyttir í Rauðan")
                                settUt = Spil(2,0)
                                kastbunki.insert(0,settUt)
                            elif litaVal==3:
                                print("Þú breyttir í Grænan")
                                settUt = Spil(3,0)
                                kastbunki.insert(0,settUt)
                            elif litaVal==4:
                                print("Þú breyttir í Bláan")
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
        elif numer==100: #ef notandi velur að segja uno
            if len(spilNotandi)==2: #checkar hvort notandi hafi 2 spil á hendi
                leyfilegt=False
                for y in range(len(spilNotandi)):
                    #sér hvort notandi geti sett út spil 
                    if kastbunki[0].tegund == spilNotandi[y].tegund or kastbunki[0].nr == spilNotandi[y].nr or spilNotandi[y].nr == 12 or spilNotandi[y].nr == 13:
                        leyfilegt=True
                if leyfilegt:
                    UNO=True #uno er orðið satt
                    print("Notandi segir UNO!")
                else:
                    print("Þú getur ekki sagt UNO núna")
            else:
                print("Þú getur ekki sagt UNO núna") #ef hann annaðhvort hefur of mörg spil eða getur ekki gert þá má hann ekki segja olsen
            print()
        elif numer==1000:#ef notandi velur að segja uno uno
            if len(spilNotandi)==1:#sér hvort notandi hafi bara eitt spil eftir
                leyfilegt=False
                for y in range(len(spilNotandi)):
                    #sér hvort hann geti sett út síðasta spilið
                    if kastbunki[0].tegund == spilNotandi[y].tegund or kastbunki[0].nr == spilNotandi[y].nr or spilNotandi[y].nr == 12 or spilNotandi[y] == 13:
                        leyfilegt=True
                if leyfilegt:
                    UNOUNO=True #unouno er orðið satt
                    print("Notandi segir UNO UNO!!!")
                else:
                    print("Þú getur ekki sagt UNO UNO núna")
            else:
                print("Þú getur ekki sagt UNO UNO núna")#ekki má segja uno uno ef þú hefur fleiri en eitt spil eða ef þú getur ekki gert
            print()
        #ef notandi velur spil þá...
        else:
            #skoðar hvort hægt sé að nota spilið
            if kastbunki[0].tegund == spilNotandi[numer-1].tegund or kastbunki[0].nr == spilNotandi[numer-1].nr or spilNotandi[numer-1].nr == 12 or spilNotandi[numer-1].nr == 13:
                print("Þú settir út",spilNotandi[numer-1])
                settUt = spilNotandi.pop(numer-1)#tekur spilið úr hendi notanda
                kastbunki.insert(0,settUt)#setur spilið efst í kastbunkann
                if settUt.nr == 12: #ef sett er út partý má notandi velja tegund
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
                notandiUmferd=False #endar umferð notanda
                if len(spilNotandi)==1:#skoða hvort notandi gleymdi að segja uno
                    if UNO:
                        pass
                    else:#ef notandi gleymir að segja uno er hann látinn draga 3 spil
                        print("Þú gleymdir að segja UNO og þarft að draga 3 spil")
                        for x in range(3):
                            draga=spilastokkur.pop(0)
                            print("Þú dróst",draga)
                            spilNotandi.append(draga)
                if len(spilNotandi)==0:#skoða hvort notandi gleymdi að segja uno uno
                    if UNOUNO:
                        tolvaUmferd=False
                        break
                    else: #ef notandi gleymir er hann látinn draga 3 spil
                        print("Þú gleymdir að segja UNO UNO og þarft að draga 3 spil")
                        for x in range(3):
                            draga=spilastokkur.pop(0)
                            print("Þú dróst",draga)
                            spilNotandi.append(draga)
                break
            else:
                print("Þú getur ekki sett út þetta spil, veldu aftur")#ef ekki er hægt að setja út spilið sem notandi velur
            print()
