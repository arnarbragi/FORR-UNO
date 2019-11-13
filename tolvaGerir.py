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
