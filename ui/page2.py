from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from models.personnages import Personnages
import random


class Page2(Screen):
    index = 0
    index_manche = 1
    manche_en_cours = False
    duree_manche = 90

    def __init__(self, **kwargs):
        super(Page2, self).__init__(**kwargs)
        self.timer_count = self.duree_manche
        self.timer_in_progress = False
        self.timer_event = None
        self.timer.text = f"Temps restant : {self.timer_count} secondes"

    def _reset_state(self):
        self.timer_count = self.duree_manche
        self.timer_in_progress = False
        self.timer_event = None
        self.index = 0
        self.index_manche = 1
        self.manche_en_cours = False
        self.timer.text = f"Temps restant : {self.timer_count} secondes"
        self.button_start.text = 'Démarrer la manche'
        self.button_start.opacity = 1
        self.button_start.disabled = False

    def start_timer(self):
        if self.timer_event:
            self.timer_event.cancel()
        if self.timer_count == 0:
            self.timer_count = self.duree_manche
        if not self.manche_en_cours or self.timer_count == 0:
            self.timer_count = self.duree_manche
        self.timer_in_progress = True
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def pause_timer(self):
        if self.button_pause.text == "Pause":
            self.button_pause.text = "Reprendre"
            self.timer_in_progress = False
            if self.timer_event:
                self.timer_event.cancel()
        else:
            self.button_pause.text = "Pause"
            self.timer_in_progress = True
            self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if not self.timer_in_progress:
            self.timer_event.cancel()
            return

        if self.timer_count == 0:
            self.timer.text = "Temps écoulé !"
            self.timer_in_progress = False
            self.timer_event.cancel()
            # reprendre la manche avec l'équipe suivante
            self.index += 1
            self.label1.text = 'Temps écoulé !'
            self.button_start.text = 'Joueur suivant'
            self.button_start.opacity = 1
            self.button_start.disabled = False
            self.ids.button_passer.opacity = 0
            self.ids.button_passer.disabled = True
            self.ids.button_valider.opacity = 0
            self.ids.button_valider.disabled = True
            return

        self.timer.text = f"{self.timer_count} secondes"
        self.timer_count -= 1

    def choisirPersonnage(self):
        """choisit un personnage à afficher, si la manche n'est pas en cours, démarre une nouvelle manche"""
        # si la manche n'est pas en cours, démarre une nouvelle manche
        if not self.manche_en_cours and self.button_start.text != 'Joueur suivant':
            self.demarrer_manche()

        # si la manche est cours, on redémarre le timer
        if self.manche_en_cours and self.button_start.text == 'Joueur suivant':
            self.timer.text = f"Temps restant : {self.timer_count} secondes"
            self.button_start.opacity = 0
            self.button_start.disabled = True
            self.start_timer()

        # si l'index le permet, on affiche le personnage suivant
        print(len(Personnages.personnages_en_jeu), self.index)
        # if self.index <= len(Personnages.personnages_en_jeu) - 1:
        try:
            personnage = self.afficherPersonnage()
            if personnage:
                self.label1.text = personnage
            else:
                self.fin_de_manche()
        # else:
        except IndexError:
            self.fin_de_manche()

    def demarrer_manche(self):
        self.label3.text = f"Manche {self.index_manche}"
        self.button_start.opacity = 0
        self.button_start.disabled = True
        nombre_personnages_restant = len([p for p in Personnages.personnages_en_jeu if (isinstance(p, list) and
                                                                                        len(p) == 3 and p[2] == 0)])
        random.shuffle(Personnages.personnages_en_jeu)
        if nombre_personnages_restant == 0:
            self.index_manche += 1
            self.label3.text = f"Manche {self.index_manche}"

            for p in Personnages.personnages_en_jeu:
                p[2] = 0
        self.manche_en_cours = True
        self.start_timer()

    def fin_de_manche(self, reprendre=False):
        nb_perso_restant = len([p for p in Personnages.personnages_en_jeu if (isinstance(p, list) and
                                                                              len(p) == 3 and p[2] == 0)])
        self.index = 0
        self.manche_en_cours = False
        if self.index_manche < 3 and not nb_perso_restant:
            self.label1.text = 'Manche terminée !'
            self.button_start.text = 'Démarrer la manche suivante'
            self.button_start.opacity = 1
            self.button_start.disabled = False
        elif nb_perso_restant:
            self.label1.text = 'Il reste des personnages à trouver !'
            self.button_start.text = 'Reprendre la manche'
            self.button_start.opacity = 1
            self.button_start.disabled = False
        else:
            self.button_start.opacity = 0
            self.button_start.disabled = True
            self.label1.text = 'Toutes les manches sont terminées !'
        self.ids.button_passer.opacity = 0
        self.ids.button_passer.disabled = True
        self.ids.button_valider.opacity = 0
        self.ids.button_valider.disabled = True
        self.timer_in_progress = False
        self.timer_count = self.duree_manche
        if self.timer_event:
            self.timer_event.cancel()

    def afficherPersonnage(self):
        """affiche le personnage s'il n'a pas encore été trouvé, none sinon"""
        try:
            personnage = Personnages.personnages_en_jeu[self.index]
        except IndexError:
            return None
        if personnage[2] == 0:
            self.ids.button_passer.opacity = 1
            self.ids.button_passer.disabled = False
            self.ids.button_valider.opacity = 1
            self.ids.button_valider.disabled = False
            return f"{personnage[0]} \n (dans {personnage[1]})"
        else:
            self.index += 1
            return self.afficherPersonnage()

    def passer(self):
        self.index += 1
        self.choisirPersonnage()

    def valider(self):
        Personnages.personnages_en_jeu[self.index][2] = 1
        self.index += 1
        self.choisirPersonnage()

    def goPage1(self, value):
        Personnages.personnages_en_jeu = []
        self.manager.current = 'page1'
