# -*- coding: utf-8 -*-
"""
Erstellt am: Wed Sep 14 18:44:44 2022
@Author: T. Haberland
"""

from passagiere import Passagier

pass01 = Passagier("Hermann", 35, "deutsch")
pass02 = Passagier("Marie", 32, "niederländisch")
pass03 = Passagier("Mourat", 52, "türkisch")
pass04 = Passagier("Helene", 47, "deutsch")
pass05 = Passagier("Aische", 27, "türkisch")
pass06 = Passagier("Torben", 17, "deutsch")
pass07 = Passagier("Luisa", 16, "deutsch")
pass08 = Passagier("Julia", 18, "deutsch")

print(pass01)
print(pass01.get_name())
print(pass01.get_alter())
print(pass01.get_nationalitaet())
pass01.set_alter('34')
print(pass01.get_alter())

passagier_liste = [pass01, pass02, pass03, pass04, pass05, pass06, pass07, pass08]

print(passagier_liste[1])

for passagier in passagier_liste:
    print(passagier.get_name())

passagier_liste[1].set_name("Maria")

print(passagier_liste[1].get_name())
print(pass02.get_name())

print("Die Gesamtanzahl der Passagiere ist", str(Passagier.get_passagierzaehler()) + ",", end=" ")
print("davon sind", Passagier.get_passagierzaehler18(), "mindestens 18 Jahre alt.")

passagier_liste.remove(pass03)
del (pass03)

print("Die Gesamtanzahl der Passagiere ist", str(Passagier.get_passagierzaehler()) + ",", end=" ")
print("davon sind", Passagier.get_passagierzaehler18(), "mindestens 18 Jahre alt.")

for passagier in passagier_liste:
    print(passagier.get_name())
