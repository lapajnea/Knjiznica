import sqlite3 as dbapi
from datumi import Datum
import funkcije
import os

pot = os.path.dirname(os.path.realpath(__file__))
os.chdir(pot)
con = dbapi.connect('baza.db', uri=False)
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS knjiga;")
cur.execute('''CREATE TABLE knjiga (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naslov TEXT NOT NULL,
    avtor TEXT NOT NULL,
    zanr TEXT NOT NULL,
    leto_izdaje INTEGER NOT NULL,
    zalozba TEXT NOT NULL
);''')

cur.execute("DROP TABLE IF EXISTS clan;")
cur.execute('''CREATE TABLE clan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ime TEXT NOT NULL,
    priimek TEXT NOT NULL,
    starost INTEGER NOT NULL,
    spol TEXT NOT NULL,
    dolg INTEGER NOT NULL
);''')

cur.execute("DROP TABLE IF EXISTS izposoja;")
cur.execute('''CREATE TABLE izposoja (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    knjiga INTEGER NOT NULL REFERENCES knjiga (id),
    clan INTEGER NOT NULL REFERENCES clan (id),
    datum_izposoje DATE NOT NULL,
    datum_vracila DATE,
    zamudnina INTEGER
);''')


with open('podatki\knjige.txt', 'r', encoding="utf8") as knjige: #doda podatke o knjigah
    vrstica = knjige.readline()
    while vrstica != '':
        knjiga = vrstica.split('\t')
        cur.execute("""INSERT INTO knjiga (naslov, avtor, zanr, leto_izdaje, zalozba)
                    VALUES (?, ?, ?, ?, ?)""", (knjiga[0], knjiga[1], knjiga[2], knjiga[3], knjiga[4].rstrip()))
        vrstica = knjige.readline()

with open('podatki\clani.txt', 'r', encoding="utf8") as clani: #doda podatke o clanih
    vrstica = clani.readline()
    while vrstica != '':
        clan = vrstica.split('\t')
        ime = clan[0].split(' ')
        cur.execute("""INSERT INTO clan (ime, priimek, starost, spol, dolg)
                    VALUES (?, ?, ?, ?, 0)""", (ime[0], ime[1], clan[1], clan[2].rstrip()))
        vrstica = clani.readline()



with open('podatki\izposoja.txt', 'r') as izposoje: #doda podatke o izposojah
    vrstica = izposoje.readline()
    while vrstica != '':
        pod = vrstica.rstrip().split('\t')
        datum_iz = pod[2].split('/') #pretvoti datum v pravilen format
        datum_izposoje = Datum(int(datum_iz[0]), int(datum_iz[1]), int(datum_iz[2]))
        zamudnina = 0
        if pod[3] == 'NULL': #ni se vrnjena knjiga
            cur.execute("""INSERT INTO izposoja (knjiga, clan, datum_izposoje, zamudnina) 
                        VALUES (?, ?, ?, ?)""", (pod[0], pod[1], str(datum_izposoje), zamudnina))
        else:
            datum_iz = pod[3].split('/') #je vrnjena knjiga, izracuna zamudnino
            datum_vrnitve = Datum(int(datum_iz[0]), int(datum_iz[1]), int(datum_iz[2]))
            zamudnina = funkcije.izracunaj_zamudnino(datum_izposoje, datum_vrnitve)
        
            cur.execute("""INSERT INTO izposoja (knjiga, clan, datum_izposoje, datum_vracila, zamudnina) 
                        VALUES (?, ?, ?, ?, ?)""", (pod[0], pod[1], str(datum_izposoje), str(datum_vrnitve), zamudnina))
        vrstica = izposoje.readline()
    
    
    con.commit()
    cur.close()
    con.close()

