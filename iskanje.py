import sqlite3 as dbapi

def isci_knjigo(podatek, tabela):
    '''Poisce knjige avtorja'''
    con = dbapi.connect('baza.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM knjiga WHERE ? like ? ", (tabela, '%' + podatek + '%'))
    rezultat = cur.fetchall()
    cur.close()
    con.close()
    if len(rezultat) == 0:
        return rezultat
    else:
        knjige = []
        for el in rezultat:
            knjige.append(f'{el[0]}, {el[1]}, {el[2]}, {el[3]}, {el[4]}')
        return knjige

