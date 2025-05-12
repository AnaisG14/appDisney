import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Personnages:
    personnages = [
            ["Anna", "La reine des neiges", 0],
            ["Olaf", "La reine des neiges", 0],
            ["Mulan", "Mulan", 0],
            ["Elsa", "La reine des neiges", 0],
            ["Manny", "L'âge de glace", 0],
            ["Sid", "l'âge de glace", 0],
            ["Diego", "l'âge de glace", 0],
            ["Hans", "la reine des neige", 0],
            ["Kristoff", "la reine des neige", 0],
            ["Shang", "Mulan", 0],
            ["Mushu", "Mulan", 0],
            ["Yao", "Mulan", 0],
            ["Ling", "Mulan", 0],
            ["Raiponce", "Raiponce", 0],
            ["Flynn Rider", "Raiponce", 0],
            ["Gothel", "Raiponce", 0],
            ["Joie", "Vice Versa", 0],
            ["Riley", "Vice Versa", 0],
            ["Tristesse", "Vice versa", 0],
            ["Colère", "Vice Versa", 0],
            ["Embarra", "Vice Versa", 0],
            ["Ennui", "Vice Versa", 0],
            ["Anxiété", "Vice Versa", 0],
            ["Envie", "Vice Versa", 0],
            ["Dégout", "Vice Versa", 0],
            ["Peur", "Vice Versa", 0],
            ["Sisu", "Raya et le dernier dragon", 0],
            ["Raya", "Raya et le dernier dragon", 0],
            ["Rémy", "Ratatouille", 0],
            ["Cendrillon", "Cendrillon", 0],
            ["Anastasie", "Cendrillon", 0],
            ["Javotte", "Cendrillon", 0],
            ["Duchesse", "les aristochats", 0],
            ["Marie", "Les aristochats", 0],
            ["Toulouse", "les aristochats", 0],
            ["Berlioz", "les aristochats", 0],
            ["Belle", "la belle et la bête", 0],
            ["La Bête", "la belle et la bête", 0],
            ["Gaston", "la belle et la bête", 0],
            ["Lumière", "la belle et la bête", 0],
            ["Big Ben", "la belle et la bête", 0],
            ["Clochard", "la belle et le clochard", 0],
            ["Lady", "la belle et le clochard", 0],
            ["Aurore", "la belle au bois dormant", 0],
            ["Maléfique", "la belle au bois dormant", 0],
            ["Prince Philippe", "la belle au bois dormant", 0],
            ["Peter Pan", "peter pan", 0],
            ["Capitaine Crochet", "peter pan", 0],
            ["Mouche", "peter pan", 0],
            ["Wendy", "peter pan", 0],
            ["Anastasia", "anastasia", 0],
            ["Jasmine", "aladdin", 0],
            ["Aladdin", "aladdin", 0],
            ["Génie", "aladdin", 0],
            ["Cruella", "les 101 dalmatiens", 0],
            ["Perdita", "les 101 dalmatiens", 0],
            ["Pongo", "les 101 dalmatiens", 0],
            ["Blanche Neige", "blanche neige", 0],
            ["Joyeux", "blanche neige", 0],
            ["Simplet", "blanche neige", 0],
            ["Dormeur", "blanche neige", 0],
            ["Grincheux", "blanche neige", 0],
            ["Prof", "blanche neige", 0],
            ["Atchoum", "blanche neige", 0],
            ["Timide", "blanche neige", 0],
            ["Mowgli", "le livre de la jungle", 0],
            ["Kaa", "le livre de la jungle", 0],
            ["Baloo", "le livre de la jungle", 0],
            ["Bagheera's", "le livre de la jungle", 0],
            ["Robin des bois", "Robin des bois", 0],
            ["Belle Marianne", "Robin des bois", 0],
            ["Frère Tuck", "Robin des bois", 0],
            ["Prince Jean", "Robin des bois", 0],
            ["Winnie", "winnie l'ourson", 0],
            ["Bourriquet", "winnie l'ourson", 0],
            ["Tigrou", "winnie l'ourson", 0],
            ["Porcinet", "winnie l'ourson", 0],
            ["Gru", "moi moche et méchant", 0],
            ["Vector", "moi moche et méchant", 0],
            ["Agnès", "moi moche et méchant", 0],
            ["Margo", "moi moche et méchant", 0],
            ["Edith", "moi moche et méchant", 0],
            ["Rouky", "Rox et Rouky", 0],
            ["Rox", "Rox et Rouky", 0],
            ["Ariel", "La petite sirène", 0],
            ["Ursula", "La petite sirène", 0],
            ["Sébastien", "La petite sirène", 0],
            ["Polochon", "La petite sirène", 0],
            ["Eric", "La petite sirène", 0],
            ["Simba", "le roi lion", 0],
            ["Timon", "le roi lion", 0],
            ["Pumbaa", "le roi lion", 0],
            ["Quasimodo", "le bossu de notre dame", 0],
            ["Esmeralda", "le bossu de notre dame", 0],
            ["Frollo", "le bossu de notre dame", 0],
            ["Woody", "toy story", 0],
            ["buzz L'éclair", "toy story", 0],
            ["Andy", "toy story", 0],
            ["Monsieur patate", "toy story", 0],
            ["Pocahontas", "Pocahontas", 0],
            ["Vaiana", "vaiana", 0],
            ["hei hei", "vaiana", 0],
            ["maui", "vaiana", 0],
            ["Hercules", "Hercules", 0],
            ["Megara", "Hercules", 0],
            ["Hadès", "Hercules", 0],
            ["Peine", "Hercules", 0],
            ["Panique", "Hercules", 0],
            ["Pegaze", "Hercules", 0],
            ["Bob", "monste et compagnie", 0],
            ["Sully", "monste et compagnie", 0],
            ["Lilo", "lilo et stitch", 0],
            ["Stitch", "lilo et stitch", 0],
            ["Nemo", "le monde de nemo", 0],
            ["Dory", "le monde de nemo", 0],
            ["Bambi", "Bambi", 0],
            ["Panpan", "Bambi", 0],
            ["Fleur", "Bambi", 0],
            ["Bruno", "Encanto", 0],
            ["Mirabel", "Encanto", 0],
            ["Dumbo", "Merlin l'enchanteur", 0],
            ["Mufasa", "Le roi lion", 0],
            ["Mickey", "Mickey mouse", 0],
            ["Donald", "Mickey mouse", 0],
            ["Dingo", "Mickey mouse", 0],
            ["Pluto", "Mickey mouse", 0],
            ["Yoda", "Star Wars", 0],
            ["Luke", "Star Wars", 0],
            ["Chewbacca", "Star Wars", 0],
            ["R2D2", "Star Wars", 0],
            ["Golum", "Le seigneur des anneaux", 0],
            ["Gandalf", "Le seigneur des anneaux", 0],
            ["Aragorn", "Le seigneur des anneaux", 0],
            ["Legolas", "Le seigneur des anneaux", 0],
            ["Gimli", "Le seigneur des anneaux", 0],
            ["Frodon", "Le seigneur des anneaux", 0],
            ["Mario", "Mario", 0],
            ["Luigi", "Mario", 0],
            ["Peach", "Mario", 0],
            ["Bowser", "Mario", 0],
            ["Link", "Zelda", 0],
            ["Yoshi", "Mario", 0],
            ["Zelda", "Zelda", 0],
            ["Un minion", "Moi moche et méchant", 0],
            ["Astérix", "Astérix", 0],
            ["Idefix", "Astérix", 0],
            ["Falbala", "Astérix", 0],
            ["Panoramix", "Astérix", 0],
            ["Obelix", "Astérix", 0],
            ["Harry Potter", "Harry Potter", 0],
            ["Hermione Granger", "Harry Potter", 0],
            ["Ron Weasley", "Harry Potter", 0],
            ["Agrid", "Harry Potter", 0],
            ["Scooby-Doo", "Scooby-Doo", 0],
            ["Sami", "Scooby-Doo", 0],
            ["Véra", "Scooby-Doo", 0],
            ["Jack Sparow", "Pirate des Caraïbes", 0],
            ["Le kraken", "Pirate des Caraïbes", 0],
            ["Alvin", "Alvin et les shipmunskes", 0],
            ["Titeuf", "Titeuf", 0],
            ["Poséidon", "Percy Jackson", 0],
            ["Spiderman", "Spiderman", 0],
            ["Thor", "Thor", 0],
        ]
    personnages_en_jeu = []
    manche_en_cours = False


class Page1(Screen):

    def __init__(self, **kwargs):
        super(Page1, self).__init__(**kwargs)
        layout = GridLayout(cols=1)
        layout.add_widget(Label(text="Avec combien de personnage souhaitez-vous jouer :", font_size=50))
        self.nombre_personnages = TextInput(multiline=False, font_size=50, size_hint=(1, 0.5))
        layout.add_widget(self.nombre_personnages)
        button1 = Button(text="Valider", font_size=50)
        layout.add_widget(button1)
        button1.bind(on_press=self.goPage2)
        self.add_widget(layout)

    def goPage2(self, value):
        random.shuffle(Personnages.personnages)
        Personnages.personnages_en_jeu = Personnages.personnages[0:int(self.nombre_personnages.text)]
        self.manager.current = 'page2'


class Page2(Screen):
    label1 = Label(text='', font_size=50)
    label2 = Label(text='', font_size=50)
    label3 = Label(text='', font_size=50)
    index = 0
    index_manche = 1
    button = Button(text="Démarrer la manche", font_size=50)
    manche_en_cours = False
    layout = GridLayout(cols=1)
    button4 = Button(text="Valider", font_size=50)
    button3 = Button(text="passer", font_size=50)

    def __init__(self, **kwargs):
        super(Page2, self).__init__(**kwargs)
        button2 = Button(text="Nouvelle partie", font_size=50, on_press=self.goPage1)
        self.layout.add_widget(button2)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.label3)
        self.button.bind(on_press=self.choisirPersonnage)
        self.layout.add_widget(self.label1)
        self.layout.add_widget(self.button3)
        self.button3.bind(on_press=self.passer)
        self.layout.add_widget(self.button4)
        self.button4.bind(on_press=self.valider)
        self.add_widget(self.layout)

    def choisirPersonnage(self, value):
        if not self.manche_en_cours:
            self.demarrer_manche()
        if self.index <= len(Personnages.personnages_en_jeu) - 1:
            personnage = self.afficherPersonnage()
            if personnage:
                self.label1.text = personnage
                try:
                    self.layout.add_widget(self.button3)
                    self.layout.add_widget(self.button4)
                except Exception:
                    pass
            else:
                self.index = 0
                self.manche_en_cours = False
                self.label1.text = 'Manche terminée !'
                self.button.text = 'Démarrer une nouvelle manche'
        else:
            self.index = 0
            self.manche_en_cours = False
            self.label1.text = 'Manche terminée !'
            self.button.text = 'Démarrer une nouvelle manche'

    def demarrer_manche(self):
        self.label3.text = f"Manche {self.index_manche}"
        nombre_personnages_restant = len([p for p in Personnages.personnages_en_jeu if isinstance(p, list) and len(p) == 3 and p[2] == 0])
        # nombre_personnages_restant = len([p for p in Personnages.personnages_en_jeu if p[2] == 0])
        if nombre_personnages_restant == 0:
            self.index_manche += 1
            self.label3.text = f"Manche {self.index_manche}"
            for p in Personnages.personnages_en_jeu:
                p[2] = 0
            random.shuffle(Personnages.personnages_en_jeu)
        self.button.text = "Personnage suivant"
        self.manche_en_cours = True

    def afficherPersonnage(self):
        """affiche le personnage s'il n'a pas encore été trouvé, none sinon"""
        personnage = Personnages.personnages_en_jeu[self.index]
        print(personnage)
        if personnage[2] == 0:
            return f"{self.index + 1} - {personnage[0]} (dans {personnage[1]}) : {personnage[2]}"
        else:
            self.index += 1
            if self.index <= len(Personnages.personnages_en_jeu) - 1:
                return self.afficherPersonnage()
            else:
                return None

    def passer(self, value):
        self.index += 1
        self.layout.remove_widget(self.button4)
        self.layout.remove_widget(self.button3)

    def valider(self, value):
        Personnages.personnages_en_jeu[self.index][2] = 1
        self.index += 1
        self.layout.remove_widget(self.button4)
        self.layout.remove_widget(self.button3)

    def goPage1(self, value):
        Personnages.personnages_en_jeu = []
        self.manager.current = 'page1'


class DisneyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Page1(name='page1'))
        sm.add_widget(Page2(name='page2'))
        return sm


if __name__ == '__main__':
    DisneyApp().run()
