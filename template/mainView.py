import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore
from PyQt5.QtCore import *


class MainWidget(QWidget):
    def __init__(self, parent=None):
        # super().__init__()
        super(MainWidget, self).__init__(parent)
        self.thisWindow = self
        self.init_ui()

    def init_ui(self):
        self.resize(550, 650)
        self.setWindowTitle("다마고치")

        self.setStyleSheet("background-color: rgb(245, 231, 253);")
        self.show()

        icon_size = QSize(200, 200)
        BTN_STYLE_SHEET = "background-color: rgb(233, 211, 245, 100)"

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
        character_btn.setMaximumWidth(400)
        character_btn.setMaximumHeight(350)
        character_btn.setIconSize(QSize(250, 250))
        character_btn.setIcon(character_icon)

        speak_label = QLabel('배고파요 ㅠㅠ')
        speak_label.setMaximumHeight(50)
        speak_label.setStyleSheet("color:rgb(67, 67, 67);")
        speak_label.setAlignment(Qt.AlignCenter)
        speak_label.setFont(QtGui.QFont("HY엽서M", 20))

        food_icon = QtGui.QIcon('../resource/icon/food.png')
        food_btn = QPushButton()
        food_btn.setMaximumWidth(100)
        food_btn.setMaximumHeight(100)
        food_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        food_btn.setStyleSheet(BTN_STYLE_SHEET)
        food_btn.setIconSize(QSize(70, 70))
        food_btn.setIcon(food_icon)

        wash_icon = QtGui.QIcon('../resource/icon/wash.png')
        wash_btn = QPushButton()
        wash_btn.setMaximumWidth(100)
        wash_btn.setMaximumHeight(110)
        wash_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        wash_btn.setStyleSheet(BTN_STYLE_SHEET)
        wash_btn.setIconSize(QSize(70, 70))
        wash_btn.setIcon(wash_icon)

        sleep_icon = QtGui.QIcon('../resource/icon/sleep.png')
        sleep_btn = QPushButton()
        sleep_btn.setMaximumWidth(100)
        sleep_btn.setMaximumHeight(110)
        sleep_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sleep_btn.setStyleSheet(BTN_STYLE_SHEET)
        sleep_btn.setIconSize(QSize(70, 70))
        sleep_btn.setIcon(sleep_icon)

        hbox0 = QHBoxLayout()
        hbox0.addWidget(level_label)
        hbox0.addWidget(exp_label)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(character_btn)

        hbox1_2 = QHBoxLayout()
        hbox1_2.addWidget(speak_label)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(food_btn)
        hbox2.addSpacing(1)
        hbox2.addWidget(wash_btn)
        hbox2.addSpacing(1)
        hbox2.addWidget(sleep_btn)

        # hbox3 = QHBoxLayout()
        # hbox3.addWidget(quiz_btn)
        # hbox3.addSpacing(10)
        # hbox3.addWidget(repeat_btn)
        vbox = QVBoxLayout()
        vbox.addSpacing(9)
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox1_2)
        vbox.addLayout(hbox2)
        # vbox.addLayout(hbox3)


        self.setLayout(vbox)



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.dbmanager.save()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())