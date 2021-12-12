import random
import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import *
import PyQt5.QtGui as QtGui
from PyQt5.QtCore import *
import pathlib
from game_manager import GameState
icon_basepath = pathlib.Path(__file__).parents[1].absolute()
icon_basepath = icon_basepath.joinpath("resource/icon")

class RPSGameWidget(QWidget):
    def __init__(self, parent=None, game_state=None):
        # super().__init__()
        super(RPSGameWidget, self).__init__(parent)
        self.game_state = game_state
        self.thisWindow = self
        self.running = True
        self.init_ui()
        self.disable_button()

    def init_ui(self):
        self.resize(550, 650)
        self.setWindowTitle("미니게임")

        self.setStyleSheet("background-color: rgb(214, 210, 196);")
        self.show()

        BTN_STYLE_SHEET = "background-color: rgb(247, 218, 217)"

        self.level_label = QLabel(f'Level: {int(self.game_state.experience / self.game_state.xp_per_level)}')
        self.level_label.setMaximumHeight(50)
        self.level_label.setStyleSheet("color:rgb(67, 67, 67);")
        self.level_label.setAlignment(Qt.AlignCenter)
        self.level_label.setFont(QtGui.QFont("HY엽서M", 20))

        self.exp_label = QLabel(f'EXP : {self.game_state.experience % self.game_state.xp_per_level}')
        self.exp_label.setMaximumHeight(50)
        self.exp_label.setStyleSheet("color:rgb(67, 67, 67);")
        self.exp_label.setAlignment(Qt.AlignCenter)
        self.exp_label.setFont(QtGui.QFont("HY엽서M", 20))

        computer_label = QLabel('Computer')
        computer_label.setMaximumHeight(50)
        computer_label.setStyleSheet("color:rgb(67, 67, 67);")
        computer_label.setAlignment(Qt.AlignCenter)
        computer_label.setFont(QtGui.QFont("HY엽서M", 20))

        computer_icon = QtGui.QIcon(str(icon_basepath.joinpath('rock.png')))
        self.computer_btn = QPushButton()
        self.computer_btn.setStyleSheet("background-color: rgb(255, 245, 218);")
        self.computer_btn.setMaximumWidth(320)
        self.computer_btn.setMaximumHeight(320)
        self.computer_btn.setIconSize(QSize(260, 260))
        self.computer_btn.setIcon(computer_icon)
        self.computer_btn.setDisabled(True)  # setDisabled(True)를 하니까 화면이 회색이 됨 - 버튼은 안 눌러지지만 회색됨



        self.speak_label = QLabel('     이겼다 !!')
        self.speak_label.setStyleSheet("color:rgb(67, 67, 67);")
        self.speak_label.setFont(QtGui.QFont("HY엽서M", 20))

        exit_icon = QtGui.QIcon(str(icon_basepath.joinpath('exit.png')))
        exit_btn = QPushButton()
        exit_btn.setMaximumWidth(50)
        exit_btn.setMaximumHeight(50)
        exit_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        exit_btn.setStyleSheet("background-color: rgb(214, 210, 196);")
        exit_btn.setIconSize(QSize(45, 45))
        exit_btn.setIcon(exit_icon)

        rock_icon = QtGui.QIcon(str(icon_basepath.joinpath('rock.png')))
        rock_btn = QPushButton()
        rock_btn.setMaximumWidth(90)
        rock_btn.setMaximumHeight(80)
        rock_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        rock_btn.setStyleSheet(BTN_STYLE_SHEET)
        rock_btn.setIconSize(QSize(70, 70))
        rock_btn.setIcon(rock_icon)
        rock_btn.clicked.connect(lambda x: self.play_rps("rock"))
        self.rock_btn = rock_btn

        scissor_icon = QtGui.QIcon(str(icon_basepath.joinpath('scissor.png')))
        scissor_btn = QPushButton()
        scissor_btn.setMaximumWidth(90)
        scissor_btn.setMaximumHeight(80)
        scissor_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        scissor_btn.setStyleSheet(BTN_STYLE_SHEET)
        scissor_btn.setIconSize(QSize(70, 70))
        scissor_btn.setIcon(scissor_icon)
        scissor_btn.clicked.connect(lambda x: self.play_rps("scissor"))
        self.scissor_btn = scissor_btn

        paper_icon = QtGui.QIcon(str(icon_basepath.joinpath('hand.png')))
        paper_btn = QPushButton()
        paper_btn.setMaximumWidth(90)
        paper_btn.setMaximumHeight(80)
        paper_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        paper_btn.setStyleSheet(BTN_STYLE_SHEET)
        paper_btn.setIconSize(QSize(70, 70))
        paper_btn.setIcon(paper_icon)
        paper_btn.clicked.connect(lambda event: self.play_rps("hand"))
        self.paper_btn = paper_btn

        scissor_label = QLabel('가위')
        scissor_label.setMaximumHeight(20)
        scissor_label.setStyleSheet("color:rgb(67, 67, 67);")
        scissor_label.setAlignment(Qt.AlignCenter)
        scissor_label.setFont(QtGui.QFont("HY엽서M", 15))

        rock_label = QLabel('바위')
        rock_label.setMaximumHeight(20)
        rock_label.setStyleSheet("color:rgb(67, 67, 67);")
        rock_label.setAlignment(Qt.AlignCenter)
        rock_label.setFont(QtGui.QFont("HY엽서M", 15))

        paper_label = QLabel('보')
        paper_label.setMaximumHeight(20)
        paper_label.setStyleSheet("color:rgb(67, 67, 67);")
        paper_label.setAlignment(Qt.AlignCenter)
        paper_label.setFont(QtGui.QFont("HY엽서M", 15))

        hbox0 = QHBoxLayout()
        hbox0.addWidget(self.level_label)
        hbox0.addWidget(self.exp_label)

        hbox0_5 = QHBoxLayout()
        hbox0_5.addWidget(computer_label)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.computer_btn)

        hbox1_2 = QHBoxLayout()
        hbox1_2.addStretch(1)
        hbox1_2.addWidget(self.speak_label)
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
        hbox3.addWidget(scissor_label)
        hbox3.addStretch(1)
        hbox3.addWidget(rock_label)
        hbox3.addStretch(1)
        hbox3.addWidget(paper_label)
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

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.exit_clicked()

    def exit_clicked(self):
        self.running = False
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def play_rps(self, player_choice):
        choices = ["rock", "hand", "scissor"]
        cpu = random.choice(choices)
        computer_icon = QtGui.QIcon(str(icon_basepath.joinpath(f'{cpu}.png')))
        self.computer_btn.setIcon(computer_icon)
        print(player_choice, cpu)
        if cpu == player_choice:
            self.speak_label.setText("     비겼다!!")
        elif (cpu == "hand" and player_choice == "scissor") or (cpu == "rock" and player_choice == "hand") or (cpu == "scissor" and player_choice == "rock"):
            self.game_state.increment_xp(10)
            self.speak_label.setText("     이겼다!!")
        elif (player_choice == "hand" and cpu == "scissor") or (player_choice == "rock" and cpu == "hand") or (player_choice == "scissor" and cpu == "rock"):
            self.game_state.increment_xp(-10)
            self.speak_label.setText("     졌다!!")

        self.exp_label.setText(f'EXP : {self.game_state.experience % self.game_state.xp_per_level}')
        self.level_label.setText(f'Level: {int(self.game_state.experience / self.game_state.xp_per_level)}')


    def disable_button(self):  # 얘는 어디에 연결해야 될까요
        try:
            if self.game_state.gameOver():
                self.rock_btn.setDisabled(True)
                self.scissor_btn.setDisabled(True)
                self.paper_btn.setDisabled(True)
                print('Game button Disabled')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RPSGameWidget(None, GameState())
    ex.show()
    sys.exit(app.exec_())