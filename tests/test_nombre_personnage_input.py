# import pytest
# from kivy.base import EventLoop
# from ui.widgets import NombrePersonnagesInput
# from models.personnages import Personnages
# from kivy.uix.boxlayout import BoxLayout


# def test_pipo():
#     assert 2 + 2 == 4


# @pytest.fixture
# def setup_env():
#     # initialize les widgets kivy
#     if not EventLoop.event_listeners:
#         EventLoop.ensure_window()
#     # Simule quelque personnages pour les tests
#     Personnages.personnages = [
#         ["Anna", "La reine des neiges", 0],
#         ["Olaf", "La reine des neiges", 0],
#         ["Mulan", "Mulan", 0]
#     ]
#     yield
#     # restaure l'état initial
#     Personnages.personnages = []

#     layout = BoxLayout()
#     champ = NombrePersonnagesInput()
#     layout.add_widget(champ)
#     return champ


# def test_accepts_valid_number(setup_env):
#     champ = setup_env
#     champ.text = ""
#     champ.insert_text("2")
#     assert champ.text == "2"


# def test_rejects_invalid_number(setup_env):
#     champ = setup_env
#     champ.text = ""
#     champ.insert_text("5")
#     assert champ.text == ""  # 5 n'est pas un nombre valide car il n'y a que 3 personnages


# def test_rejects_invalid_character(setup_env):
#     champ = setup_env
#     champ.text = ""
#     champ.insert_text("a")
#     assert champ.text == ""  # a n'est pas un nombre
