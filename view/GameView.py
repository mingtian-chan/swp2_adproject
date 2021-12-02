import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from qtpy import QtGui, QtCore
from PyQt5.QtCore import *
import MainView


class GameWidget(QWidget):
    def __init__(self, parent=None):
        # super().__init__()
        super(GameWidget, self).__init__(parent)
        self.thisWindow = self
        self.init_ui()

    def init_ui(self):
        self.resize(550, 650)
        self.setWindowTitle("미니게임")

        self.setStyleSheet("background-color: rgb(214, 210, 196);")
        self.show()

        BTN_STYLE_SHEET = "background-color: rgb(247, 218, 217)"

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

        computer_label = QLabel('Computer')
        computer_label.setMaximumHeight(50)
        computer_label.setStyleSheet("color:rgb(67, 67, 67);")
        computer_label.setAlignment(Qt.AlignCenter)
        computer_label.setFont(QtGui.QFont("HY엽서M", 20))

        computer_icon = QtGui.QIcon('../resource/icon/rock.png')
        computer_btn = QPushButton()
        computer_btn.setStyleSheet("background-color: rgb(255, 245, 218);")
        computer_btn.setMaximumWidth(320)
        computer_btn.setMaximumHeight(320)
        computer_btn.setIconSize(QSize(260, 260))
        computer_btn.setIcon(computer_icon)

        speak_label = QLabel('     이겼다 !!')
        speak_label.setStyleSheet("color:rgb(67, 67, 67);")
        speak_label.setFont(QtGui.QFont("HY엽서M", 20))

        exit_icon = QtGui.QIcon('../resource/icon/exit.png')
        exit_btn = QPushButton()
        exit_btn.setMaximumWidth(50)
        exit_btn.setMaximumHeight(50)
        exit_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        exit_btn.setStyleSheet("background-color: rgb(214, 210, 196);")
        exit_btn.setIconSize(QSize(45, 45))
        exit_btn.setIcon(exit_icon)

        rock_icon = QtGui.QIcon('../resource/icon/rock.png')
        rock_btn = QPushButton()
        rock_btn.setMaximumWidth(90)
        rock_btn.setMaximumHeight(80)
        rock_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        rock_btn.setStyleSheet(BTN_STYLE_SHEET)
        rock_btn.setIconSize(QSize(70, 70))
        rock_btn.setIcon(rock_icon)

        scissor_icon = QtGui.QIcon('../resource/icon/scissor.png')
        scissor_btn = QPushButton()
        scissor_btn.setMaximumWidth(90)
        scissor_btn.setMaximumHeight(80)
        scissor_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        scissor_btn.setStyleSheet(BTN_STYLE_SHEET)
        scissor_btn.setIconSize(QSize(70, 70))
        scissor_btn.setIcon(scissor_icon)

        paper_icon = QtGui.QIcon('../resource/icon/hand.png')
        paper_btn = QPushButton()
        paper_btn.setMaximumWidth(90)
        paper_btn.setMaximumHeight(80)
        paper_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        paper_btn.setStyleSheet(BTN_STYLE_SHEET)
        paper_btn.setIconSize(QSize(70, 70))
        paper_btn.setIcon(paper_icon)

        food_label = QLabel('가위')
        food_label.setMaximumHeight(20)
        food_label.setStyleSheet("color:rgb(67, 67, 67);")
        food_label.setAlignment(Qt.AlignCenter)
        food_label.setFont(QtGui.QFont("HY엽서M", 15))

        wash_label = QLabel('바위')
        wash_label.setMaximumHeight(20)
        wash_label.setStyleSheet("color:rgb(67, 67, 67);")
        wash_label.setAlignment(Qt.AlignCenter)
        wash_label.setFont(QtGui.QFont("HY엽서M", 15))

        sleep_label = QLabel('보')
        sleep_label.setMaximumHeight(20)
        sleep_label.setStyleSheet("color:rgb(67, 67, 67);")
        sleep_label.setAlignment(Qt.AlignCenter)
        sleep_label.setFont(QtGui.QFont("HY엽서M", 15))

        hbox0 = QHBoxLayout()
        hbox0.addWidget(level_label)
        hbox0.addWidget(exp_label)

        hbox0_5 = QHBoxLayout()
        hbox0_5.addWidget(computer_label)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(computer_btn)

        hbox1_2 = QHBoxLayout()
        hbox1_2.addStretch(1)
        hbox1_2.addWidget(speak_label)
        hbox1_2.addStretch(1)
        hbox1_2.addStretch(1)
        hbox1_2.addWidget(exit_btn)
        hbox1_2.addStretch(1)


        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(scissor_btn)
        hbox2.addStretch(1)
        hbox2.addWidget(rock_btn)
        hbox2.addStretch(1)
        hbox2.addWidget(paper_btn)
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
        vbox.addLayout(hbox0_5)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox1_2)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

        exit_btn.clicked.connect(self.exit_clicked)

    def exit_clicked(self):
        self.thisWindow = MainView.MainWidget()
        self.thisWindow.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GameWidget()
    ex.show()
    sys.exit(app.exec_())