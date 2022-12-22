# -*- coding: utf-8 -*-

"""
Erstellt am: Wed Sep 14 17:21:06 2022
@Author: T. Haberland

1. Der erste Kontakt mit Klassen:

    Erstellen Sie eine Klasse namens Passagier, die den Namen, das Alter und die Nationalität einer Person enthält.
    Erzeugen Sie einige Instanzen dieser Klasse mit Beispieldaten und testen Sie diese.
    Geben Sie die Personendaten aus, die in den zuvor erzeugten Instanzen gespeichert sind.
    Definieren Sie eine Liste, welche die Passagier-Klasse als Elementtyp verwendet und
    füllen Sie die Liste mit Beispieldaten.
    Geben Sie das zweite Element der Liste aus.
    Geben Sie die gesamte Liste aus.

2. Erweitern Sie das Programm der vorhergehenden Übung:

    Implementieren Sie eine Methode, die den Namen des Passagiers ausgibt, und rufen Sie sie auf.
    Implementieren Sie zwei Methoden, die jeweils das Alter des Passagiers neu setzen bzw. ausgeben. Im ersten Fall soll das neu zu setzende Alter der Methode als Parameter übergeben werden. Rufen Sie die Methoden auf.

3.
Betrachten Sie wieder die Klasse Passagier.

    Ergänzen Sie die Passagier-Klasse um ein statisches Element, das die Passagieranzahl enthält, und sorgen Sie für die Aktualisierung der Passagieranzahl, wenn eine neue Instanz der Passagier-Klasse erzeugt oder gelöscht wird.
    Erzeugen oder löschen Sie einige Instanzen der Klasse und geben Sie jeweils nach der Erzeugung die Anzahl der Passagiere aus.
    Ergänzen Sie ein statisches Element, das die Anzahl der Passagiere enthält, die mindestens 18 Jahre alt sind. Prüfen Sie die fehlerfreie Aktualisierung des Elementes beim Erzeugen und Löschen von Instanzen.

4. Verwenden Sie die zuvor definierte Klasse Passagier.

    Ersetzen Sie alle in der Klasse verwendeten Variablennamen, außer den statischen Datenfeldern, durch private Namen.
    Versuchen Sie, die privaten Variablen direkt „von außen“ zu beschreiben oder zu lesen und beobachten Sie, welche Fehlermeldung erscheint.
    Implementieren Sie Methoden, mit denen jede Komponente der privaten Passagierdaten  gelesen bzw. neu gesetzt werden kann und rufen Sie die Methoden auf.
    Ändern Sie nun die Namen der statischen Datenfelder mit der Passagieranzahl und der Passagierzahl über 18 Jahre in private Namen. Ändern Sie die Methoden zum Auslesen der betreffenden Werte entsprechend und rufen Sie diese auf.
    Erzeugen und löschen Sie einige Instanzen der Klasse Passagier. Prüfen Sie nach jedem Erzeugen und Löschen einer Instanz, ob die Passagieranzahlen die richtigen Werte aufweisen.

"""


class Passagier:
    __passagierzaehler = 0  # statisch
    __passagierzaehler_18_oder_aelter = 0  # statisch

    def __init__(self, name, alter, nationalitaet):  # konstruktor
        self.__name = name
        self.__alter = alter
        self.__nationalitaet = nationalitaet
        if alter >= 18:
            Passagier.__passagierzaehler_18_oder_aelter += 1
        Passagier.__passagierzaehler += 1

    def __del__(self):  # destruktor
        if self.__alter >= 18:
            Passagier.__passagierzaehler_18_oder_aelter -= 1
        Passagier.__passagierzaehler -= 1

    def get_passagierzaehler(self=0):  # statisch
        return Passagier.__passagierzaehler

    def get_passagierzaehler18(self=0):  # statisch
        return Passagier.__passagierzaehler_18_oder_aelter

    def get_name(self):
        return self.__name

    def set_name(self, name):
        assert name != ""
        self.__name = name

    def get_alter(self):
        return self.__alter

    def set_alter(self, alter):
        assert alter != int(alter)
        self.__alter = alter

    def get_nationalitaet(self):
        return self.__nationalitaet

    def set_nationalitaet(self, nationalitaet):
        assert nationalitaet != ""
        self.__nationalitaet = nationalitaet

    def __str__(self):
        return self.__name + ", " + str(self.__alter) + ", nationalität: " + self.__nationalitaet

    def __repr__(self):
        return str([self.__name, self.__alter, self.__nationalitaet])
