import funkcije

while True:
    print('\nPozdravljeni!')
    print('Dodaj novega člana: 1')
    print('Dodaj novo knjigo: 2')
    print('Poišči knjigo: 3')
    print('Poišči člana: 4')
    print('Končaj program: 5')
    vr = input('Vnesi število med 1 in 5: ')
    
    if vr not in ['1', '2', '3', '4', '5']:
        print('\nNapačen vnos! Vnesti moraš število med 1 in 5!')
    else:
        if vr == '5':
            break
        
        elif vr == '1': #vrpaša po podatkih novega člana
            print('\nVnesi podatke o članu')
            ime = input('Vnesi ime: ')
            priimek = input('Vnesi priimek: ')
            starost = input('Vnesi starost: ')
            spol = input('Vnesi spol: ')
            funkcije.dodaj_clana(ime, priimek, starost, spol)
            
        elif vr == '2': #vpraša po podatkih nove knjige
            print('\nVnesi podatke o knjigi')
            naslov = input('Vnesi naslov: ')
            avtor = input('Vnesi avtorja: ')
            zanr = input('Vnesi žanr: ')
            leto = input('Vnesi leto izdaje: ')
            zalozba = input('Vnesi založbo: ')
            funkcije.dodaj_knjigo(naslov, avtor, zanr, leto, zalozba)
            
        elif vr == '3':
            while True:
                podatek = None
                podatki = ['naslov', 'avtor', 'zanr', 'zalozba']
                while podatek is None: #sprašuje po parametrih iskanja
                    print('\nPo katerem podatku bi rad iskal?')
                    print('Naslov: 1')
                    print('Avtor: 2')
                    print('Žanr: 3')
                    print('Založba: 4')
                    vr1 = input('Vnesi število od 1 do 4: ')
                    if vr1 not in ['1', '2', '3', '4']:
                        print('\nNapačen vnos! Vnesti moraš število med 1 in 4!')
                    else: #vpraša po podatku iskanja
                        if vr1 == '4':
                            podatek = input('Vnesi založbo: ')
                        else:
                            podatek = input('Vnesi ' + podatki[int(vr1) - 1] + ': ')
                knjige = funkcije.isci_knjigo(podatek, podatki[int(vr1) - 1])
                if len(knjige) == 0:
                    print('\nProgram ni najdel nobenih knjig s temi parametri.')
                else:
                    dolzina_nizov = [0, 0, 0, 0, 0, 0, 0] #dolžine za izpisovanje tabele
                    for knjiga in knjige.values(): #prešteje dolžine nizov
                        for i in range(len(knjiga)):
                            if dolzina_nizov[i] < len(str(knjiga[i])):
                                dolzina_nizov[i] = len(str(knjiga[i]))
                                
                    podatki = ['Id', 'Naslov', 'Avtor', 'Žanr', 'Leto izdaje', 'Založba', 'Izposoja']
                    niz = ''
                    for i in range(7): #glava tabele
                        if dolzina_nizov[i] < len(podatki[i]):
                            dolzina_nizov[i] = len(podatki[i])
                        niz += podatki[i] + ' ' * (dolzina_nizov[i] - len(podatki[i]))
                        if i != 6:
                            niz += ' |'
                            
                    print('\nTabela knjig:')
                    print(niz)

                    for knjiga in knjige.values(): #podatki v tabeli
                        niz = ''
                        for i in range(7):
                            niz += str(knjiga[i]) + ' ' * (dolzina_nizov[i] - len(str(knjiga[i])))
                            if i != 6:
                                niz += ' |'
                        print(niz)
                    
                    naprej = True
                    while True: #če želimo poiskati še kako knjigo
                        print('\nŽeliš poiskati še kako knjigo?')
                        print('Da: 1')
                        print('Ne: 2')
                        vr2 = input('Vnesi 1 ali 2: ')
                        if vr2 not in ['1', '2']:
                            print('\nNisi vnesel 1 ali 2!')
                        else:
                            if vr2 == '1':
                                naprej = False
                            break
                    if naprej:
                        break
        
        elif vr == '4':
            podatek = None
            podatki = ['id', 'ime', 'priimek']
            vr3 = 0
            while podatek is None: #sprašuje po parametrih iskanja
                print('\nPo katerem podatku bi rad iskal?')
                print('Id: 1')
                print('Ime: 2')
                print('Priimek: 3')
                vr3 = input('Vnesi število od 1 do 3: ')
                if vr3 not in ['1', '2', '3']:
                    print('\nNapačen vnos! Vnesti moraš število med 1 in 3!')
                else:
                    podatek = input('Vnesi ' + podatki[int(vr3) - 1] + ': ') #podatek iskanja
                
            id_clana = 0
            if vr3 == '1':
                id_clana = int(podatek)
            else: #izpiše tabelo najdenih članov, izmed katerih izberemo
                clani = funkcije.poisci_clana_ime(podatek, podatki[int(vr3) - 1])
                if len(clani) == 0:
                    print('Program ni našel članov s takimi parametri.')
                else:
                    idji = [] #za preverjanje uporabnikovega vpisa
                    for el in clani: #izpise tabelo
                        print('Id: {0}, Ime: {1}, Priimek: {2}, Starost: {3}, Spol: {4}'.format(el[0], el[1], el[2], el[3], el[4]))
                        idji.append(int(el[0]))
                    idji.append(0)
                    while True: #vpraša uporabnika, katerega člana bi rad izbral
                        id_clana = input('Vnesi id člana izmed zgoraj izpisanimi ali 0, če ni iskanega člana: ')
                        if int(id_clana) not in idji:
                            print('\nNapačen vnos!')
                        else:
                            break
                    id_clana = int(id_clana)
            
            clan = funkcije.poisci_clana(id_clana)
            
            if clan is None: #ni našlo člana
                print('\nTega člana ni v bazi podatkov.')
            else:
                while True:
                    clan = funkcije.poisci_clana(id_clana)
                    print('\nId: {0}\nIme: {1}\nPriimek: {2}\nStarost: {3}\nSpol: {4}\nDolg: {5}'.format(clan[0], clan[1], clan[2], clan[3], clan[4], clan[5]))
                    izbira = None
                    while izbira is None: #vpraša uporabnika, kaj bi rad naredil
                        print('\nKaj bi rad naredil?')
                        print('Poravnaj dolg člana: 1')
                        print('Izposodi knjigo članu: 2')
                        print('Izpiši izposoje člana: 3')
                        print('Nazaj na začetek: 4')
                        vr4 = input('Vpiši število med 1 in 4: ')
                        if vr4 not in ['1', '2', '3', '4']:
                            print('\nIzbrati moraš število med 1 in 4.')
                        else:
                            izbira = vr4
                    
                    if izbira == '1': #poravna dolg
                        funkcije.poravnaj_dolg(clan[0])
                    elif izbira == '2': #izposodi knjigo
                        id_knjige = input('\nVnesi id knjige, ki bi jo rad izposodil: ')
                        obstaja, izposojena = funkcije.preveri(id_knjige)
                        if not obstaja: #ni take knjige
                            print('Knjige s tem id-jem ni v bazi!')
                        elif izposojena: #knjiga že izposojena
                            print('Ta knjiga je že izposojena!')
                        else: #izposodi
                            funkcije.izposodi(id_knjige, clan[0])
                            print('Knjiga je izpsojena.')
                    
                    elif izbira == '3': #izpiše tabelo izposoj člana
                        izposoje = funkcije.poisci_izposoje_clana(int(clan[0]), False)
                        za_vrnt = [] #za preverjanje vnosov uporabnika
                        ostale = [0]
                        if len(izposoje) == 0:
                            print('\nČlan si ni še izposodil nobene knjige')
                        else:
                            dolzine = [11, 9, 14, 12, 13, 9] #za izpis tabele
                            for el in izposoje:#preveri dolžine podatkov v tabeli
                                if el[4] is None:
                                    za_vrnt.append(int(el[0]))
                                else:
                                    ostale.append(int(el[0]))
                                for i in range(len(el)):
                                    if dolzine[i] < len(str(el[i])):
                                        dolzine[i] = len(str(el[i]))
                            niz = '\n'
                            pod = ['Id izposoje', 'Id knjige', 'Datum izposoje', 'Datum vrnitve', 'Zamudnina']
                            for i in range(len(pod)):#sestavi glavo tabele
                                niz += pod[i] + ' ' * (dolzine[i] - len(pod[i]))
                                if i != 4:
                                    niz += ' |'
                            print(niz)
                            for el in izposoje:#izpiše podatke v tabeli
                                niz = ''
                                for i in range(len(el)):
                                    if i < 2:
                                        niz += str(el[i]) + ' ' * (dolzine[i] - len(str(el[i])))
                                    elif i > 2:
                                        niz += str(el[i]) + ' ' * (dolzine[i - 1] - len(str(el[i])))
                                    if i != 5 and i != 2:
                                        niz += ' |'
                                print(niz)
                            
                            while True: #sprašuje, če želi uporabnik vrnt knjigo
                                
                                vr5 = int(input('Če želiš vrniti knjigo, vpiši id izposoje, čene vpiši 0: '))
                                if vr5 not in za_vrnt and vr5 not in ostale:
                                    print('Napačen vnos!')
                                elif vr5 in za_vrnt:
                                    funkcije.vrni(vr5)
                                    break
                                elif vr5 in ostale and vr5 != 0:
                                    print('Knjiga je že vrnjena!')
                                else:
                                    break
                    
                    else:
                        break
                                    
                    