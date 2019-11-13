class Spil():
    #init fall sem tekur inn tvær tölur, ein sem stendur fyrir tegund og hin fyrir númerið á spilinu. skilar spili
    def __init__(self,t,n):
        self.tegund = t
        self.nr = n
    #fall sem prentar út spilið á réttan hátt. Breytir tegunda tölum í tegund og öllum nr tölum yfir 10 í viðeigandi karakter
    def __str__(self):
        tegund = ""
        nr = ""
        if self.tegund == 1:
            tegund = "Gulur"
        elif self.tegund == 2:
            tegund = "Rauður"
        elif self.tegund == 3:
            tegund = "Grænn"
        elif self.tegund == 4:
            tegund = "Blár"
        elif self.tegund == 0:
            tegund = "Svart"
            
        if self.nr == 10:
            nr = "Draga 2"
        elif self.nr == 11:
            nr = "Snúa við"
        elif self.nr == 12:
            nr = "skipp"
        elif self.nr == 13:
            nr = "Partý"
        elif self.nr == 14:
            nr = "Partý +4"
        else:
            nr = str(self.nr)
        return tegund + " " + nr
    #notar init fallið til þess að búa til spilastokk með 52 spilum
    def geraSpilastokk(self):
        l = []
        for t in range(1,5):
            s0 = Spil(t,0)
            l.append(s0)
            for m in range(2):
                for n in range(1,13):
                    s1= Spil(t,n)
                    l.append(s1)
        for x in range(4):
            sParty = Spil(0,13)
            sParty4 = Spil(0,14)
            l.append(sParty)
            l.append(sParty4)
        random.shuffle(l)#stokkar spilastokkinn
        return l
    #tekur inn lista af spilum og prentar út öll spilin
    def synaSpil(l):
        for x in l:
            print(x)
