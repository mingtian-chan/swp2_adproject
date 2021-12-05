import sys
import pickle

from PyQt5 import Qt
from PyQt5.QtWidgets import *
import PyQt5.QtGui as QtGui
from PyQt5.QtCore import *
import view.GameView as GameView
from game_manager import GameState

class MainWidget(QWidget):
    def __init__(self, parent=None):
        # super().__init__()
        super(MainWidget, self).__init__(parent)
        self.thisWindow = self
        self.init_ui()
        self.savefilename = 'Tamago.dat'
        self.gamestate = None
        self.readTamago()

    def init_ui(self):
        self.resize(600, 720)
        self.setWindowTitle("다마고치")

        self.setStyleSheet("background-color: rgb(253, 255,188);")
        self.show()

        BTN_STYLE_SHEET = "background-color: rgb(255, 220, 184)"

        level_label = QLabel('Level: ?')
        level_label.setMaximumHeight(50)
        level_label.setStyleSheet("color:rgb(67, 67, 67);")
        level_label.setAlignment(Qt.AlignCenter)
        level_label.setFont(QtGui.QFont("HY엽서M", 20))

        exp_label = QLabel('EXP : ???')
        exp_label.setMaximumHeight(50)
        exp_label.setStyleSheet("color:rgb(67, 67, 67);")
        exp_label.setAlignment(Qt.AlignCenter)
        exp_label.setFont(QtGui.QFont("HY엽서M", 20))

        character_icon = QtGui.QIcon('../resource/icon/character.png')
        character_btn = QPushButton()
        character_btn.setStyleSheet("background-color: rgb(255, 255,255);")
        character_btn.setMaximumWidth(500)
        character_btn.setMaximumHeight(350)
        character_btn.setIconSize(QSize(500, 350))
        character_btn.setIcon(character_icon)

        speak_label = QLabel('배고파요 ㅠㅠ')
        speak_label.setStyleSheet("color:rgb(67, 67, 67);")
        speak_label.setFont(QtGui.QFont("HY엽서M", 20))

        game_icon = QtGui.QIcon('../resource/icon/game.png')
        game_btn = QPushButton()
        game_btn.setMaximumWidth(90)
        game_btn.setMaximumHeight(80)
        game_btn.setStyleSheet(BTN_STYLE_SHEET)
        game_btn.setIconSize(QSize(70,70))
        game_btn.setIcon(game_icon)


        food_icon = QtGui.QIcon('../resource/icon/food.png')
        food_btn = QPushButton()
        food_btn.setMaximumWidth(90)
        food_btn.setMaximumHeight(80)
        food_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        food_btn.setStyleSheet(BTN_STYLE_SHEET)
        food_btn.setIconSize(QSize(70, 70))
        food_btn.setIcon(food_icon)

        wash_icon = QtGui.QIcon('../resource/icon/wash.png')
        wash_btn = QPushButton()
        wash_btn.setMaximumWidth(90)
        wash_btn.setMaximumHeight(80)
        wash_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        wash_btn.setStyleSheet(BTN_STYLE_SHEET)
        wash_btn.setIconSize(QSize(70, 70))
        wash_btn.setIcon(wash_icon)

        sleep_icon = QtGui.QIcon('../resource/icon/sleep.png')
        sleep_btn = QPushButton()
        sleep_btn.setMaximumWidth(90)
        sleep_btn.setMaximumHeight(80)
        sleep_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sleep_btn.setStyleSheet(BTN_STYLE_SHEET)
        sleep_btn.setIconSize(QSize(70, 70))
        sleep_btn.setIcon(sleep_icon)

        food_label = QLabel('밥 먹기')
        food_label.setMaximumHeight(20)
        food_label.setStyleSheet("color:rgb(67, 67, 67);")
        food_label.setAlignment(Qt.AlignCenter)
        food_label.setFont(QtGui.QFont("HY엽서M", 15))

        wash_label = QLabel('씻기')
        wash_label.setMaximumHeight(20)
        wash_label.setStyleSheet("color:rgb(67, 67, 67);")
        wash_label.setAlignment(Qt.AlignCenter)
        wash_label.setFont(QtGui.QFont("HY엽서M", 15))

        sleep_label = QLabel('자기')
        sleep_label.setMaximumHeight(20)
        sleep_label.setStyleSheet("color:rgb(67, 67, 67);")
        sleep_label.setAlignment(Qt.AlignCenter)
        sleep_label.setFont(QtGui.QFont("HY엽서M", 15))

        game_label = QLabel('놀기')
        game_label.setMaximumHeight(20)
        game_label.setStyleSheet("color:rgb(67, 67, 67);")
        game_label.setAlignment(Qt.AlignCenter)
        game_label.setFont(QtGui.QFont("HY엽서M", 15))

        statusLayout = QGridLayout()
        displayLayout = QGridLayout()
        barLayout = QGridLayout()
        buttonLayout = QGridLayout()

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(statusLayout, 0, 0, 1, 2)
        mainLayout.addLayout(displayLayout, 1, 0, 2, 2)
        mainLayout.addLayout(barLayout, 3, 0, 3, 1)
        mainLayout.addLayout(buttonLayout, 3, 1, 3, 2)

        statusLayout.addWidget(level_label,0, 0)
        statusLayout.addWidget(exp_label, 0, 1)

        displayLayout.addWidget(character_btn)

        buttonLayout.addWidget(food_btn, 0, 0)
        buttonLayout.addWidget(food_label, 1, 0)
        buttonLayout.addWidget(game_btn, 0, 1)
        buttonLayout.addWidget(game_label, 1, 1)
        buttonLayout.addWidget(wash_btn, 2, 0)
        buttonLayout.addWidget(wash_label,3, 0)
        buttonLayout.addWidget(sleep_btn, 2, 1)
        buttonLayout.addWidget(sleep_label, 3, 1)

        game_btn.clicked.connect(self.game_clicked)

        self.setLayout(mainLayout)

    def game_clicked(self):
        print("clciekd")
        self.thisWindow = GameView.GameWidget()
        self.thisWindow.show()

    def keyPressEvent(self, event):  # 나가는 이벤트 중복임 하나로 뭉치자.
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.writeSaveFile()

    def readTamago(self):
        try:
            fH = open(self.savefilename, 'rb')
        except FileNotFoundError as e:
            self.gamestate = GameState()
            return

        try:
            tamagodat = pickle.load(fH)
        except:
            self.gamestate = GameState()
        else:
            self.gamestate = GameState(tamagodat["experience"], tamagodat["satiety"], tamagodat["hygiene"], tamagodat["drowsiness"], tamagodat["hp"])
        fH.close()

    def writeSaveFile(self):
        fH = open(self.savefilename, 'wb')
        pickle.dump({"experience": self.gamestate.experience, "satiety": self.gamestate.satiety, "hygiene": self.gamestate.hygiene, "drowsiness": self.gamestate.drowsiness, "hp": self.gamestate.hp}, fH)
        fH.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())