import random
from kivy.uix.screenmanager import Screen
from models.personnages import Personnages


class Page1(Screen):

    def __init__(self, **kwargs):
        super(Page1, self).__init__(**kwargs)
        self.label_input.text += f"(Entre 1 et {len(Personnages.personnages)})"

    def goPage2(self, value):
        random.shuffle(Personnages.personnages)
        if not self.nombre_personnages.text:
            return
        Personnages.personnages_en_jeu = Personnages.personnages[0:int(self.nombre_personnages.text)]

        # réinitialisation de la page 2
        page2 = self.manager.get_screen('page2')
        page2._reset_state()
        self.manager.current = 'page2'
