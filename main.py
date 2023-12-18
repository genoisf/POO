#créé par Francis Genois et Ulysse Doyon
#créé en 2023
#POO partie 2

import random

def rouler_de_dé():
    dé1 = random.randint(1,6)
    dé2 = random.randint(1,6)
    dé3 = random.randint(1,6)
    dé4 = random.randint(1,6)
    if dé1 <= dé2 and dé1 <= dé3 and dé1 <= dé4:
        return dé2+dé3+dé4
    elif dé2 <= dé1 and dé2 <= dé3 and dé2 <= dé4:
        return dé1+dé3+dé4
    elif dé3 <= dé1 and dé3 <= dé2 and dé3 <= dé4:
        return dé1 + dé2 + dé4
    elif dé4 <= dé1 and dé4 <= dé2 and dé4 <= dé3:
        return dé1 + dé2 + dé3

class NPC:
    def __init__(self):
        self.pv = 20
        self.nom = ""
        self.race = ""
        self.espèce = ""
        self.profession = ""
        self.armure = random.randint(1,12)
        self.force = rouler_de_dé()
        self.agilité = rouler_de_dé()
        self.constitution = rouler_de_dé()
        self.intelligence = rouler_de_dé()
        self.charisme = rouler_de_dé()
        self.sagesse = rouler_de_dé()
    def afficher(self):
        print(npc.pv, "\n"
              , npc.nom, "\n"
              , npc.race, "\n"
              , npc.espèce, "\n"
              , npc.profession, "\n"
              , npc.armure, "\n"
              , npc.force, "\n"
              , npc.agilité, "\n"
              , npc.constitution, "\n"
              , npc.intelligence, "\n"
              , npc.charisme, "\n"
              , npc.sagesse, )

class HÉROS(NPC):
    def attaquer(self, cible):
        cible.subir(random(1.6))
    def subir(self, dommage):
        self.pv -= dommage

class KOBOLD(NPC):
    def attaquer(self, cible):
        cible.subir(random(1.6))
    def subir(self, dommage):
        self.pv -= dommage


npc = NPC()
kobold = KOBOLD()