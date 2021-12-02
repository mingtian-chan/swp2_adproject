import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore
from PyQt5.QtCore import *
import GameView


class MainWidget(QWidget):
    def __init__(self, parent=None):
        # super().__init__()
        super(MainWidget, self).__init__(parent)
        self.thisWindow = self
        self.init_ui()
        self.tamagodat = []
        self.savefilename = 'Tamago.dat'
        self.readTamago()


    def init_ui(self):
        self.resize(550, 650)
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
        character_btn.setMaximumWidth(400)
        character_btn.setMaximumHeight(280)
        character_btn.setIconSize(QSize(270, 270))
        character_btn.setIcon(character_icon)

        speak_label = QLabel('배고파요 ㅠㅠ')
        speak_label.setStyleSheet("color:rgb(67, 67, 67);")
        speak_label.setFont(QtGui.QFont("HY엽서M", 20))

        game_icon = QtGui.QIcon('../resource/icon/game.png')
        game_btn = QPushButton()
        game_btn.setMaximumWidth(100)
        game_btn.setMaximumHeight(70)
        game_btn.setStyleSheet(BTN_STYLE_SHEET)
        game_btn.setIconSize(QSize(65, 65))
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

        hbox0 = QHBoxLayout()
        hbox0.addWidget(level_label)
        hbox0.addWidget(exp_label)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(character_btn)

        hbox1_2 = QHBoxLayout()
        hbox1_2.addStretch(1)
        hbox1_2.addWidget(speak_label)
        hbox1_2.addStretch(1)
        hbox1_2.addWidget(game_btn)
        hbox1_2.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(food_btn)
        hbox2.addStretch(1)
        hbox2.addWidget(wash_btn)
        hbox2.addStretch(1)
        hbox2.addWidget(sleep_btn)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(food_label)
        hbox3.addStretch(1)
        hbox3.addWidget(wash_label)
        hbox3.addStretch(1)
        hbox3.addWidget(sleep_label)
        hbox3.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addSpacing(2)
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox1_2)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)


        self.setLayout(vbox)

    def closeEvent(self, event):
        self.writeSaveFile()

    def readTamago(self):
        try:
            fH = open(self.savefilename, 'rb')
        except FileNotFoundError as e:
            self.tamagodat = []
            return

    def game_clicked(self):
        self.thisWindow = GameView.GameWidget()
        self.thisWindow.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        try:
            self.tamagodat = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    def writeSaveFile(self):
        fH = open(self.savefilename, 'wb')
        pickle.dump(self.tamagodat, fH)
        fH.close()
    #
    # def keyPressEvent(self, event):  # 나가는 이벤트 중복임 하나로 뭉치자.
    #     if event.key() == Qt.Key_Escape:
    #         self.dbmanager.save()
    #         self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())