def je_prestopno(leto):
    if leto % 4 == 0:
        if leto % 100 == 0:
            if leto % 400 == 0:
                return True
            return False
        return True
    else:
        return False
    
def stevilo_dni(leto):
    if je_prestopno(leto):
        return 366
    else:
        return 365
    
def dolzine_mesecev(leto):
    if je_prestopno(leto):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Datum():
    def __init__(self, dan, mesec, leto):
        self.dan = dan
        self.mesec = mesec
        self.leto = leto
    
    def __str__(self):
        if self.dan < 10:
            dan = '0' + str(self.dan)
        else:
            dan = self.dan
        if self.mesec < 10:
            mesec = '0' + str(self.mesec)
        else:
            mesec = self.mesec
        return '{}-{}-{}'.format(self.leto, mesec, dan)
    
    def __repr__(self):
        return 'Datum({}, {}, {})'.format(self.dan, self.mesec, self.leto)
    
    def je_veljaven(self):
        if self.mesec < 1 or self.mesec > 12:
            return False
        st_dni = dolzine_mesecev(self.leto)[self.mesec - 1]
        if self.dan < 1 or self.dan > st_dni:
            return False
        return True
    
    def __lt__(self, other):
        if self.leto < other.leto:
            return True
        elif self.leto == other.leto:
            if self.mesec < other.mesec:
                return True
            elif self.mesec == other.mesec:
                if self.dan < other.dan:
                    return True
        return False
    
    def __eq__(self, other):
        return (self.dan, self.mesec, self.leto) == (other.dan, other.mesec, other.leto)
    
    def dan_v_letu(self):
        meseci = dolzine_mesecev(self.leto)
        st = self.dan
        for i in range(0, self.mesec - 1):
            st += meseci[i]
        return st
    
    def razlika(self, other):
        if self.leto == other.leto:
            return self.dan_v_letu() - other.dan_v_letu()
        if self > other:
            razlika = self.dan_v_letu() + stevilo_dni(other.leto) - other.dan_v_letu()
            for i in range(other.leto + 1, self.leto):
                razlika += stevilo_dni(i)
        else:
            razlika = other.dan_v_letu() + stevilo_dni(self.leto) - self.dan_v_letu()
            for i in range(self.leto + 1, other.leto):
                razlika += stevilo_dni(i)
            razlika *= -1
        return razlika