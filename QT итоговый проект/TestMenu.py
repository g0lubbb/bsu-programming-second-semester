from PyQt6.QtWidgets import QWidget, QMessageBox, QMenuBar, QMenu
from PyQt6.QtGui import QAction

class TestMenu(QMenuBar):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setMinimumSize(300, 1)

        self.mainMenu = QMenu("Edit")
        self.infoMenu = QMenu("Info")
        self.addMenu(self.mainMenu)
        self.addMenu(self.infoMenu)
        
        self.loadMenuAction = QAction("Load game ->")
        self.mainMenu.addAction(self.loadMenuAction)

        self.saveMenuAction = QAction("Save game ->")
        self.mainMenu.addAction(self.saveMenuAction)

        self.loadColorsAction = QAction("Load Colors ->")
        self.mainMenu.addAction(self.loadColorsAction)

        self.saveColorsAction = QAction("Save Colors ->")
        self.mainMenu.addAction(self.saveColorsAction)

        self.loadProfileAction = QAction("Load User Info ->")
        self.mainMenu.addAction(self.loadProfileAction)

        self.saveProfileAction = QAction("Save User Info ->")
        self.mainMenu.addAction(self.saveProfileAction)

        self.dropdownEditMenu = QMenu("Dropdown")
        self.gameInfoAction = QAction("Game Information")
        self.aboutDevelopersAction = QAction("About Developers")
        self.dropdownEditMenu.addAction(self.gameInfoAction)
        self.dropdownEditMenu.addAction(self.aboutDevelopersAction)
        self.infoMenu.addMenu(self.dropdownEditMenu)

        self.gameInfoAction.triggered.connect(self.showGameInformation)
        self.aboutDevelopersAction.triggered.connect(self.showAboutDevelopers)

    def addLoadActionHandler(self, handler):
        self.loadMenuAction.triggered.connect(handler)

    def addSaveActionHandler(self, handler):
        self.saveMenuAction.triggered.connect(handler)
    
    def addSaveColorsActionHandler(self, handler):
        self.saveColorsAction.triggered.connect(handler)
    
    def addLoadColorsActionHandler(self, handler):
        self.loadColorsAction.triggered.connect(handler)

    def addSaveProfileActionHandler(self, handler):
        self.saveProfileAction.triggered.connect(handler)

    def addLoadProfileActionHandler(self, handler):
        self.loadProfileAction.triggered.connect(handler)

    def showGameInformation(self):
        game_info = (
            "Rules of the Game:\n\n"
            "1. The game is played on a grid that's 3 squares by 3 squares.\n"
            "2. You are X, your friend is O. Players take turns putting their marks in empty squares.\n"
            "3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n"
            "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a draw."
        )
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("Game Information")
        msgBox.setInformativeText(game_info)
        msgBox.setFixedSize(400, 300)
        msgBox.exec()

    def showAboutDevelopers(self):
        developers_info = (
            "Developed by:\n\n"
            "Golub Dmitry\n"
            "\nContact: gdima2739@gmail.com\n"
            "\nTeacher: Evgeniy Derevyago\n"
        )
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("About Developers")
        msgBox.setInformativeText(developers_info)
        msgBox.setFixedSize(400, 200) 
        msgBox.exec()