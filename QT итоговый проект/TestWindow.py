from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget

from TestMenu import TestMenu
from Pictures import Picture
from TestGameField import GameField

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Super Tic Tac Toe")
        self.setGeometry(100, 100, 800, 800)

        self.layout1 = QHBoxLayout()
        self.widget = QWidget()
        self.gameField = GameField()
        self.menuBar = TestMenu(self)
        self.setMenuBar(self.menuBar)
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.layout1)

        self.picture1 = Picture(self, 1)
        self.picture2 = Picture(self, 2)

        self.layout1.addWidget(self.picture1, 15)
        self.layout1.addWidget(self.gameField, 30)
        self.layout1.addWidget(self.picture2, 15)

        self.menuBar.addLoadActionHandler(self.gameField.loadGameState)
        self.menuBar.addSaveActionHandler(self.gameField.saveGameState)
        self.menuBar.addSaveColorsActionHandler(self.gameField.saveColorSettings)
        self.menuBar.addLoadColorsActionHandler(self.gameField.loadColorSettings)
        self.menuBar.addSaveProfileActionHandler(self.saveProfiles)
        self.menuBar.addLoadProfileActionHandler(self.loadProfiles)

    def saveProfiles(self):
        self.picture1.saveProfile()
        self.picture2.saveProfile()

    def loadProfiles(self):
        self.picture1.loadProfile()
        self.picture2.loadProfile()