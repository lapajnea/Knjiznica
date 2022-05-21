# Knjižnica
Avtorja: Tomaž Tratnik in Andreja Lapajne

Naredila sva primer programa, ki bi ga lahko uporabljali zaposleni v knjižnjici. Uporabnik ima možnost vpogleda v bazo knjig, članov ter aktivnost članov (izposoje, zamudnine,...). 

Najino bazo sestavljajo tri tabele. Baza knjig, baza članov ter baza izposoj. Baze so med seboj povezane. 
V prvi bazi hranimo podatke o knjigah: id, naslov, avtor, žanr, leto izadje, založba. 
V drugi bazi imamo podatke o članih: id, ime in priimek, starost ter spol (M/Ž). 
V tretji bazi pa hranimo podatke o izposojah:id,  izposojena knjiga, član, datum izposoje, datum vracila, dolg.

Podatke o knjigah sva pridobila iz spletne strani https://www.cobiss.si/, podatki o članih in izposojah pa so izmišljeni.

![knjiznica](https://user-images.githubusercontent.com/44202510/158472836-4415530f-1616-4880-9e2d-9947193daca3.png)
