import bottle
import funkcije
import os

pot = os.path.dirname(os.path.realpath(__file__))
os.chdir(pot)

@bottle.get("/")
def zacetna_stran():
    return bottle.template('zacetek.html')

@bottle.get("/dodaj_knjigo")
def dodaj_knigo():
    '''Dodajanje nove knjige'''
    return bottle.template("dodaj_knjigo.html")

@bottle.post("/dodaj_knjigo")
def dodaj_post():
    '''Prebere vnesene podatke in shrani knjigo v bazo'''
    naslov = bottle.request.forms.getunicode("naslov")
    avtor = bottle.request.forms.getunicode("avtor")
    zanr = bottle.request.forms.getunicode("zanr")
    leto_izdaje = bottle.request.forms.getunicode("leto_izdaje")
    zalozba = bottle.request.forms.getunicode("zalozba")
    funkcije.dodaj_knjigo(naslov, avtor, zanr, leto_izdaje, zalozba)
    bottle.redirect("/")
    
@bottle.get("/dodaj_clana")
def dodaj_clana():
    '''Dodajanje novega clana'''
    return bottle.template("dodaj_clana.html")

@bottle.post("/dodaj_clana")
def dodaj_post():
    '''Prebere vnesene podatke in shrani clana v bazo'''
    ime = bottle.request.forms.getunicode("ime")
    priimek = bottle.request.forms.getunicode("priimek")
    starost = bottle.request.forms.getunicode("starost")
    spol = bottle.request.forms.getunicode("spol")
    funkcije.dodaj_clana(ime, priimek, starost, spol)
    bottle.redirect("/")

@bottle.get("/poisci_knjigo")
def poisci_knjigo():
    '''Poisce knjigo glede na izbran parameter in vnesen podatek.'''
    return bottle.template("poisci_knjigo.html")

@bottle.post("/poisci_knjigo")
def poisci_post():
    '''Poisce tabelo ustreznih knjig.'''
    tabela = bottle.request.forms.getunicode("izberi")
    podatek = bottle.request.forms.getunicode("podatek")
    if tabela == '': #ni bila izbrana tabela
        tabela = 'None'
    if podatek == '': #ni bil vnešen podatek
        podatek = 'None'
    bottle.redirect(f"/izpisi_knjige/{podatek}/{tabela}")



@bottle.get("/izpisi_knjige/<podatek>/<tabela>")
def izpisi_knjige(podatek, tabela):
    '''Izpise tabelo ustreznih knjig'''
    if tabela == 'None' or podatek == 'None': #ni podatka ali tabele, izpise ustrezno sporocilo
        return bottle.template("izpisi_knjige.html", pod = {-1:0})
    podatki = funkcije.isci_knjigo(podatek, tabela)
    return bottle.template("izpisi_knjige.html", pod = podatki) #izpise tabelo najdenih knjig

@bottle.get("/izposodi_clanu/<id_knjige>")
def izposodi_clanu(id_knjige):
    '''Vprasa po id-ju clana, kateremu hocemo izposodit izbrano knjigo'''
    return bottle.template("izposodi_clanu.html", knjiga = id_knjige)

@bottle.post("/izposodi_clanu/<id_knjige>")
def izposodi_clanu_post(id_knjige):
    '''Izposodi izbrano knjigo clanu z vnesenim id-jem'''
    id_clana = bottle.request.forms.getunicode("id")
    clan = funkcije.poisci_clana(id_clana) #prever, ce clan v bazi
    if clan is None: #izpise, da ni clana v bazi
        return bottle.template("ni_clana.html", knjiga = id_knjige)
    else: #izposodi knjigo in gre na stran clana
        funkcije.izposodi(id_knjige, id_clana)
        bottle.redirect(f"/izpisi_clana/{id_clana}")

     
@bottle.get("/poisci_clana")
def poisci_clana():
    '''Poisce clana glede na vnesene podatke.'''
    return bottle.template("poisci_clana.html")

@bottle.post("/poisci_clana")
def poisci_post():
    '''Prebere vnesene podatke o clanu.'''
    tabela = bottle.request.forms.getunicode("izberi")
    podatek = bottle.request.forms.getunicode("podatek")
    if tabela == '' or podatek == '': #ni podatka ali izbrane tabele
        id_clana = 'None'
        bottle.redirect(f"/izpisi_clana/{id_clana}")
    if tabela == 'id':
        bottle.redirect(f"/izpisi_clana/{podatek}")
    if tabela == 'ime' or tabela == 'priimek':
        clani = funkcije.poisci_clana_ime(podatek, tabela) #poisce vse clane s podobnim imenom
        if clani == []: #ni najdenih clanov
            bottle.redirect(f"/izpisi_clana/None")
        else: #gre na tabelo za izbrat clana
            return bottle.template('izberi_clana.html', cl = clani)
        

@bottle.get("/izpisi_clana/<id_clana>")
def izpisi_clana(id_clana):
    '''Poisce in izpise podatke clana.'''
    if id_clana == 'None': #ni naslo clana, izpise opozorilo
        return bottle.template("izpisi_clana.html", pod = [], iz = [])
    clan = funkcije.poisci_clana(id_clana)
    izposoje = funkcije.poisci_izposoje_clana(id_clana, False)
    if clan == None:
        clan = []
    return bottle.template("izpisi_clana.html", pod = clan, iz = izposoje)

@bottle.get("/poravnaj_dolg/<id_clana>")
def poravnaj_dolg(id_clana):
    '''Poravna dolg clana'''
    funkcije.poravnaj_dolg(id_clana)
    bottle.redirect(f"/izpisi_clana/{id_clana}")

@bottle.get("/podatki_knjige/<id>/<id_clana>")
def podatki_knjige(id, id_clana):
    '''Izpise podatke ene knjige.'''
    return bottle.template("podatki_knjige.html", pod = funkcije.podatki_knjige(id), id_c = id_clana)

@bottle.get("/vrni_knjigo/<id_clana>/<id_izposoje>")
def vrni_knjigo(id_clana, id_izposoje):
    '''Vrne knjigo.'''
    funkcije.vrni(id_izposoje)
    bottle.redirect(f"/izpisi_clana/{id_clana}")

@bottle.get("/izposodi_knjigo/<id_clana>")
def izposodi_knjigo(id_clana):
    '''Izposodi knjigo z vnesenim id-jem'''
    return bottle.template("izposodi.html", id = id_clana)

@bottle.post("/izposodi_knjigo/<id_clana>")
def izposodi_post(id_clana):
    '''Preveri, ali je vnesen id knjige v bazi ali ce je ze izposojen in izpise napako ali izposodi knjigo.'''
    id_knjige = bottle.request.forms.getunicode("id_knjige")
    obstaja, izposojena = funkcije.preveri(id_knjige)
    if not obstaja: #knjige ni v bazi
        bottle.redirect(f"/knjiga_ne_obstaja/{id_clana}")
    elif izposojena: #knjiga ze izposojena
        bottle.redirect(f"/knjiga_je_izposojena/{id_clana}")
    else:
        funkcije.izposodi(id_knjige, id_clana)
        bottle.redirect(f"/izpisi_clana/{id_clana}")
    

@bottle.get("/knjiga_ne_obstaja/<id_clana>")
def knjiga_ne_obstaja(id_clana):
    '''Knjige ni v bazi.'''
    return bottle.template("knjiga_ne_obstaja.html", id = id_clana)

@bottle.get("/knjiga_je_izposojena/<id_clana>")
def knjiga_je_izposojena(id_clana):
    '''Knjiga je trenutno izposojena.'''
    return bottle.template("knjiga_je_izposojena.html", id = id_clana)


bottle.run(debug = True, reloader = True)