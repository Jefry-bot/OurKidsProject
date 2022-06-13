from PySide6.QtCore import Qt

class GeneralCustomUi:
    def __init__(self, ui) -> None:
        self.ui = ui

        self.remove_default_tittle_bar()

    def remove_default_tittle_bar(self):
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.setWindowFlag(Qt.FramelessWindowHint) 