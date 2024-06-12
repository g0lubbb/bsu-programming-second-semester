import json
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QGridLayout, QMessageBox, QColorDialog, QVBoxLayout, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPainter, QColor

class GameButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(60, 60)
        self.setFont(QFont('Arial', 24))
        self.setStyleSheet("font-size: 24px")

class Cell(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 200)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.buttons = [
            [GameButton() for _ in range(3)] for _ in range(3)
        ]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(lambda _, x_of_button=i, y_of_button=j: self.buttonClicked(x_of_button, y_of_button))
                self.layout.addWidget(self.buttons[i][j], i, j)
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.isActive = False

        self.winnerLabel = QLabel(self)
        self.winnerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.winnerLabel.setFont(QFont('Arial', 144))
        self.winnerLabel.setStyleSheet("font-size: 88px; color: lightgrey;")
        self.winnerLabel.setGeometry(8, 8, 195, 195)
        self.winnerLabel.hide()

    def buttonClicked(self, x, y):
        if not self.parentWidget().gameActive or self.board[x][y] != '' or not self.isActive:
            return

        self.board[x][y] = self.parentWidget().currentPlayer
        self.buttons[x][y].setText(self.parentWidget().currentPlayer)
        self.buttons[x][y].setStyleSheet(f"color: {self.parentWidget().colors[self.parentWidget().currentPlayer]};")
        if self.checkWinner():
            self.winner = self.parentWidget().currentPlayer
            self.showWinnerInCell(self.winner)
            self.isActive = False
        self.parentWidget().setNextActiveCell(x, y)
        self.parentWidget().currentPlayer = 'O' if self.parentWidget().currentPlayer == 'X' else 'X'
        self.parentWidget().checkGlobalGameEnd()

    def checkWinner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def showWinnerInCell(self, winner):
        self.winnerLabel.setText(winner)
        self.winnerLabel.setStyleSheet(f"color: {self.parentWidget().colors[winner]}; font-size: 96px;")
        self.winnerLabel.show()

    def resetBoard(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText('')
                self.buttons[i][j].setStyleSheet("font-size: 24px;")
        self.winnerLabel.hide()
        self.winner = None
        self.isActive = False

    def setColors(self, colors):
        self.colors = colors

    def setActive(self, active):
        self.isActive = active
        if active:
            self.setStyleSheet("background-color: white;")
        else:
            self.setStyleSheet("background-color: lightgrey;")

    def isDraw(self):
        if self.winner is None and all(all(cell != '' for cell in row) for row in self.board):
            return True
        return False

class GameField(QWidget):
    def __init__(self):
        super().__init__()
        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        
        self.cells = [[Cell(self) for _ in range(3)] for _ in range(3)]
        self.currentPlayer = 'X'
        self.colors = {'X': 'black', 'O': 'black'}
        self.backgroundColor = QColor("grey")
        self.gameActive = False
        self.gameLoaded = False

        for i in range(3):
            for j in range(3):
                self.gridLayout.addWidget(self.cells[i][j], i, j)
                self.cells[i][j].setActive(True)

        self.initUI()

    def initUI(self):
        self.controlLayout = QVBoxLayout()
        
        self.xColorButton = QPushButton('Выбрать цвет для X')
        self.xColorButton.clicked.connect(self.selectXColor)
        self.controlLayout.addWidget(self.xColorButton)

        self.oColorButton = QPushButton('Выбрать цвет для O')
        self.oColorButton.clicked.connect(self.selectOColor)
        self.controlLayout.addWidget(self.oColorButton)

        self.backgroundColorButton = QPushButton('Выбрать цвет фона поля')
        self.backgroundColorButton.clicked.connect(self.selectBackgroundColor)
        self.controlLayout.addWidget(self.backgroundColorButton)

        self.startButton = QPushButton('Начать игру')
        self.startButton.clicked.connect(self.startGame)
        self.controlLayout.addWidget(self.startButton)

        self.gridLayout.addLayout(self.controlLayout, 3, 0, 1, 3)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.backgroundColor)

    def selectBackgroundColor(self):
        colorDialog = QColorDialog()
        color = colorDialog.getColor()
        if color.isValid():
            self.backgroundColor = color
            self.update()

    def selectXColor(self):
        colorDialog = QColorDialog()
        color = colorDialog.getColor()
        if color.isValid():
            self.colors['X'] = color.name()

    def selectOColor(self):
        colorDialog = QColorDialog()
        color = colorDialog.getColor()
        if color.isValid():
            self.colors['O'] = color.name()

    def startGame(self):
        self.setColors(self.colors)
        self.gameActive = True
        self.setStartButtonActive(False)
        for i in range(3):
            for j in range(3):
                self.cells[i][j].setActive(True)

    def setColors(self, colors):
        self.colors = colors
        for row in self.cells:
            for cell in row:
                cell.setColors(colors)

    def setActiveCell(self, x, y):
        for i in range(3):
            for j in range(3):
                self.cells[i][j].setActive(False)
        if not self.cells[x][y].winner:
            self.cells[x][y].setActive(True)

    def setNextActiveCell(self, x, y):
        if self.cells[x][y].winner or all(all(cell != '' for cell in row) for row in self.cells[x][y].board):
            for i in range(3):
                for j in range(3):
                    if not self.cells[i][j].winner:
                        self.cells[i][j].setActive(True)
        else:
            self.setActiveCell(x, y)

    def resetGame(self):
        for i in range(3):
            for j in range(3):
                self.cells[i][j].resetBoard()
        for i in range(3):
            for j in range(3):
                self.cells[i][j].setActive(True)
        self.currentPlayer = 'X'
        self.gameActive = False
        self.gameLoaded = False
        self.setStartButtonActive(True)

    def setStartButtonActive(self, active):
        self.startButton.setEnabled(active)

    def checkOverallWinner(self):
        for row in range(3):
            if self.cells[row][0].winner == self.cells[row][1].winner == self.cells[row][2].winner and self.cells[row][0].winner is not None:
                return self.cells[row][0].winner
        for col in range(3):
            if self.cells[0][col].winner == self.cells[1][col].winner == self.cells[2][col].winner and self.cells[0][col].winner is not None:
                return self.cells[0][col].winner
        if self.cells[0][0].winner == self.cells[1][1].winner == self.cells[2][2].winner and self.cells[0][0].winner is not None:
            return self.cells[0][0].winner
        if self.cells[0][2].winner == self.cells[1][1].winner == self.cells[2][0].winner and self.cells[0][2].winner is not None:
            return self.cells[0][2].winner
        return False

    def checkDraw(self):
        for row in self.cells:
            for cell in row:
                if cell.isDraw():
                    return True
        return False

    def checkGlobalGameEnd(self):
        winner = self.checkOverallWinner()
        if winner:
            self.showWinnerMessage(f"Игрок {winner} победил во всей игре!")
            self.resetGame()
        elif self.checkDraw():
            self.showDrawMessage("Ничья во всей игре!")
            self.resetGame()

    def showWinnerMessage(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("Победитель")
        msgBox.setInformativeText(message)
        msgBox.setFixedSize(300, 200)
        msgBox.exec()

    def showDrawMessage(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText("Результат игры")
        msgBox.setInformativeText(message)
        msgBox.setFixedSize(300, 200)
        msgBox.exec()

    def saveGameState(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Сохранить состояние игры", "", "JSON Files (*.json)")

        if file_path:
            game_state = {
                'currentPlayer': self.currentPlayer,
                'board': [[cell.board for cell in row] for row in self.cells],
                'winners': [[cell.winner for cell in row] for row in self.cells],
                'gameActive': self.gameActive
            }
            with open(file_path, 'w') as file:
                json.dump(game_state, file, indent=4)

    def loadGameState(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Загрузить состояние игры", "", "JSON Files (*.json)")

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    game_state = json.load(file)
                    self.currentPlayer = game_state['currentPlayer']
                    self.gameActive = game_state['gameActive']
                    for i in range(3):
                        for j in range(3):
                            self.cells[i][j].board = game_state['board'][i][j]
                            self.cells[i][j].winner = game_state['winners'][i][j]
                            for x in range(3):
                                for y in range(3):
                                    self.cells[i][j].buttons[x][y].setText(self.cells[i][j].board[x][y])
                                    if self.cells[i][j].board[x][y] != '':
                                        self.cells[i][j].buttons[x][y].setStyleSheet(
                                            f"color: {self.colors[self.cells[i][j].board[x][y]]};"
                                        )
                            if self.cells[i][j].winner:
                                self.cells[i][j].showWinnerInCell(self.cells[i][j].winner)
                            else:
                                self.cells[i][j].winnerLabel.hide()
                    self.setColors(self.colors)
                    self.update()
                    if self.gameActive:
                        self.setNextActiveCell(0, 0)
                    self.setStartButtonActive(False)
                    self.gameLoaded = True
            except FileNotFoundError:
                QMessageBox.warning(self, "Load Game", "No saved game found!")

    def saveColorSettings(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Сохранить цветовые настройки", "", "JSON Files (*.json)")

        if file_path:
            color_settings = {
                'colors': self.colors,
                'backgroundColor': self.backgroundColor.name()
            }
            with open(file_path, 'w') as file:
                json.dump(color_settings, file, indent=4)

    def loadColorSettings(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Загрузить цветовые настройки", "", "JSON Files (*.json)")

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    color_settings = json.load(file)
                    self.colors = color_settings['colors']
                    self.backgroundColor = QColor(color_settings['backgroundColor'])
                    self.setColors(self.colors)
                    self.update()
            except FileNotFoundError:
                QMessageBox.warning(self, "Load Colors", "No saved colors found!")
    