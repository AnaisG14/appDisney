from kivy.uix.textinput import TextInput
from models.personnages import Personnages
from kivy.factory import Factory


class NombrePersonnagesInput(TextInput):
    """
    Champ de saisie pour entrer le nombre de personnnages à jouer.
    Seuls les chiffres sont autorisés et la valeur ne peut pas dépasser le nombre
    de personnages disponibles dans Personnages.personnages."""

    def insert_text(self, substring: str, from_undo: bool = False) -> None:
        """
        Insère du texte dans le champ de saisie si c'est un chiffre et que la valeur totale
        reste dans les limites autorisées.
        Args:
            substring (str): Le texte à insérer.
            from_undo (bool): Indique si l'insertion provient d'une action d'annulation.
        """
        if not substring.isdigit():
            return
        nouveau_texte = self.text + substring
        try:
            valeur = int(nouveau_texte)
            if 0 <= valeur <= len(Personnages.personnages):
                return super().insert_text(substring, from_undo=from_undo)
        except ValueError:
            return


Factory.register("NombrePersonnagesInput", cls=NombrePersonnagesInput)
