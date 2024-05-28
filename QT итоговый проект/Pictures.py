from PyQt6.QtWidgets import QLabel, QPushButton, QFileDialog, QWidget, QVBoxLayout, QLineEdit
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
import json
import os

class Picture(QWidget):
    def __init__(self, parent, number_of_player):
        super().__init__(parent)
        self.number_of_player = number_of_player
        self.fileName = ""

        self.button = QPushButton("Open")
        self.button.clicked.connect(self.showImage)
        
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setFont(QFont('Arial', 12))  

        self.player = QLabel(f"Player {number_of_player}")
        self.player.setFont(QFont('Arial', 20))  

        self.layout.addWidget(self.player)

        self.playerName = QLineEdit("Enter Username")
        self.playerName.setFont(QFont('Arial', 16))  
        self.layout.addWidget(self.playerName)

        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.layout.addWidget(self.button)
        self.layout.addWidget(QLabel())

    def showImage(self):
        self.file = QFileDialog()
        self.fileName = self.file.getOpenFileName()[0]
        if self.fileName:
            self.pixmap = QPixmap(self.fileName)
            self.pixmap = self.pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
            self.label.setPixmap(self.pixmap)

    def saveProfile(self, filename="profiles.json"):
        profile_data = {
            f"player_{self.number_of_player}": {
                "username": self.playerName.text(),
                "avatar": self.fileName
            }
        }

        if os.path.exists(filename):
            with open(filename, "r") as file:
                data = json.load(file)
        else:
            data = {}

        data.update(profile_data)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def loadProfile(self, filename="profiles.json"):
        if not os.path.exists(filename):
            return

        with open(filename, "r") as file:
            data = json.load(file)

        profile_data = data.get(f"player_{self.number_of_player}", {})
        username = profile_data.get("username", "Username")
        avatar = profile_data.get("avatar", "")

        self.playerName.setText(username)
        if avatar:
            self.fileName = avatar
            self.pixmap = QPixmap(self.fileName)
            self.pixmap = self.pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
            self.label.setPixmap(self.pixmap)