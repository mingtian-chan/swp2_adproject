import random
import sys
import pickle

from PyQt5 import Qt
from PyQt5.QtWidgets import *
import PyQt5.QtGui as QtGui
from PyQt5.QtCore import *
import view.GameView as GameView
import view.DifficultyView as DifficultyView
from game_manager import GameState

import pathlib
import math
import time
icon_basepath = pathlib.Path(__file__).parents[1].absolute()
icon_basepath = icon_basepath.joinpath("resource/icon")
class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.savefilename = 'Tamago.dat'
        self.active_window = self
        self.game_state: GameState = GameState()
        self.readTamago()
        self.init_ui()

        self.tick_timer = QTimer(self)
        self.tick_timer.setInterval(10)
        self.tick_timer.timeout.connect(self.ui_tick)
        self.tick_timer.start(10)
        self.tick_invertal = self.game_state.get_tick()
        self.last_tick_time = time.time()

        self.rotate_timer = QTimer(self)
        self.rotate_timer.setInterval(750)
        self.rotate_timer.timeout.connect(self.rotate_character)
        self.rotate_timer.start(750)


    def init_ui(self):
        self.resize(600, 720)
        self.setWindowTitle("다마고치")

        self.setStyleSheet("background-color: rgb(253, 255,188);")
        self.show()

        BTN_STYLE_SHEET = "background-color: rgb(255, 220, 184)"

        level_label = QLabel(f'Level: {math.floor(self.game_state.experience / self.game_state.xp_per_level)}')
        level_label.setMaximumHeight(50)
        level_label.setStyleSheet("color:rgb(67, 67, 67);")
        level_label.setAlignment(Qt.AlignCenter)
        level_label.setFont(QtGui.QFont("HY엽서M", 20))
        self.level_label = level_label

        exp_label = QLabel(f'EXP : {self.game_state.experience % self.game_state.xp_per_level}')
        exp_label.setMaximumHeight(50)
        exp_label.setStyleSheet("color:rgb(67, 67, 67);")
        exp_label.setAlignment(Qt.AlignCenter)
        exp_label.setFont(QtGui.QFont("HY엽서M", 20))
        self.exp_label = exp_label

        character_icon = QtGui.QIcon(str(icon_basepath.joinpath('character.png')))

        self.character_btn = QPushButton()
        self.character_btn.setStyleSheet("background-color: rgb(255, 255,255);")
        self.character_btn.setMaximumWidth(500)
        self.character_btn.setMaximumHeight(350)
        self.character_btn.setIcon(character_icon)
        self.character_btn.setIconSize(1.3 * QSize(self.character_btn.width(), self.character_btn.height()))

        speak_label = QLabel('배고파요 ㅠㅠ')
        speak_label.setStyleSheet("color:rgb(67, 67, 67);")
        speak_label.setFont(QtGui.QFont("HY엽서M", 20))

        game_icon = QtGui.QIcon(str(icon_basepath.joinpath('game.png')))
        game_btn = QPushButton()
        game_btn.setMaximumWidth(90)
        game_btn.setMaximumHeight(80)
        game_btn.setStyleSheet(BTN_STYLE_SHEET)
        game_btn.setIconSize(QSize(70,70))
        game_btn.setIcon(game_icon)
        self.game_btn = game_btn

        food_icon = QtGui.QIcon(str(icon_basepath.joinpath('food.png')))
        food_btn = QPushButton()
        food_btn.setMaximumWidth(90)
        food_btn.setMaximumHeight(80)
        food_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        food_btn.setStyleSheet(BTN_STYLE_SHEET)
        food_btn.setIconSize(QSize(70, 70))
        food_btn.setIcon(food_icon)
        food_btn.clicked.connect(self.game_state.eat)
        self.food_btn = food_btn

        wash_icon = QtGui.QIcon(str(icon_basepath.joinpath('wash.png')))
        wash_btn = QPushButton()
        wash_btn.setMaximumWidth(90)
        wash_btn.setMaximumHeight(80)
        wash_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        wash_btn.setStyleSheet(BTN_STYLE_SHEET)
        wash_btn.setIconSize(QSize(70, 70))
        wash_btn.setIcon(wash_icon)
        self.wash_btn = wash_btn


        sleep_icon = QtGui.QIcon(str(icon_basepath.joinpath('sleep.png').resolve()))
        sleep_btn = QPushButton()
        sleep_btn.setMaximumWidth(90)
        sleep_btn.setMaximumHeight(80)
        sleep_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sleep_btn.setStyleSheet(BTN_STYLE_SHEET)
        sleep_btn.setIconSize(QSize(70, 70))
        sleep_btn.setIcon(sleep_icon)
        sleep_btn.clicked.connect(self.game_state.sleep)
        self.sleep_btn = sleep_btn

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
        wash_btn.clicked.connect(self.game_state.wash)

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

        hp_label = QLabel('체력')
        hp_label.setMaximumWidth(40)
        hp_label.setStyleSheet("color:rgb(67, 67, 67);")
        hp_label.setAlignment(Qt.AlignCenter)
        hp_label.setFont(QtGui.QFont("HY엽서M", 10))

        experience_label = QLabel('경험치')
        experience_label.setMaximumWidth(40)
        experience_label.setStyleSheet("color:rgb(67, 67, 67);")
        experience_label.setAlignment(Qt.AlignCenter)
        experience_label.setFont(QtGui.QFont("HY엽서M", 10))

        satiety_label = QLabel('포만감')
        satiety_label.setMaximumWidth(40)
        satiety_label.setStyleSheet("color:rgb(67, 67, 67);")
        satiety_label.setAlignment(Qt.AlignCenter)
        satiety_label.setFont(QtGui.QFont("HY엽서M", 10))

        hygiene_label = QLabel('청결')
        hygiene_label.setMaximumWidth(40)
        hygiene_label.setStyleSheet("color:rgb(67, 67, 67);")
        hygiene_label.setAlignment(Qt.AlignCenter)
        hygiene_label.setFont(QtGui.QFont("HY엽서M", 10))

        drowsiness_label = QLabel('졸림')
        drowsiness_label.setMaximumWidth(40)
        drowsiness_label.setStyleSheet("color:rgb(67, 67, 67);")
        drowsiness_label.setAlignment(Qt.AlignCenter)
        drowsiness_label.setFont(QtGui.QFont("HY엽서M", 10))

        font_maxwidth = QtGui.QFontMetrics(QtGui.QFont("HY엽서M", 10)).boundingRect("|" * 25).width()

        hp_bar = QLineEdit()
        hp_bar.setReadOnly(True)
        hp_bar.setText("|" * int(self.game_state.hp / 4))
        hp_bar.setFixedWidth(font_maxwidth)
        self.hp_bar = hp_bar

        experience_bar = QLineEdit()
        experience_bar.setReadOnly(True)
        experience_bar.setText("|" * int(self.game_state.experience % self.game_state.xp_per_level / 4))
        experience_bar.setFixedWidth(font_maxwidth)
        self.experience_bar = experience_bar

        satiety_bar = QLineEdit()
        satiety_bar.setReadOnly(True)
        satiety_bar.setText("|" * int(self.game_state.satiety / 4))
        satiety_bar.setFixedWidth(font_maxwidth)
        self.satiety_bar = satiety_bar

        hygiene_bar = QLineEdit()
        hygiene_bar.setReadOnly(True)
        hygiene_bar.setText("|" * int(self.game_state.hygiene / 4))
        hygiene_bar.setFixedWidth(font_maxwidth)
        self.hygiene_bar = hygiene_bar

        drowsiness_bar = QLineEdit()
        drowsiness_bar.setReadOnly(True)
        drowsiness_bar.setText("|" * int(self.game_state.drowsiness / 4))
        drowsiness_bar.setFixedWidth(font_maxwidth)
        self.drowsiness_bar = drowsiness_bar


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

        displayLayout.addWidget(self.character_btn)

        barLayout.addWidget(hp_label, 1, 0)
        barLayout.addWidget(hp_bar, 1, 1)
        barLayout.addWidget(experience_label, 2, 0)
        barLayout.addWidget(experience_bar, 2, 1)
        barLayout.addWidget(satiety_label, 3, 0)
        barLayout.addWidget(satiety_bar, 3, 1)
        barLayout.addWidget(hygiene_label, 4, 0)
        barLayout.addWidget(hygiene_bar, 4, 1)
        barLayout.addWidget(drowsiness_label, 5, 0)
        barLayout.addWidget(drowsiness_bar, 5, 1)


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

    def rotate_character(self):
        char_icons = ["character.png", "character_rot_negative.png", "character_rot_positive.png"]

        self.character_btn.setIcon(QtGui.QIcon(str(icon_basepath.joinpath(random.choice(char_icons)))))

    def disable_button(self):
        self.food_btn.setDisabled(True)
        self.sleep_btn.setDisabled(True)
        self.wash_btn.setDisabled(True)
        self.game_btn.setDisabled(True)


    def ui_tick(self):
        # print('틱이 발동했다 1')  # tick-1 unittest 관련
        if time.time() * 1000 - self.last_tick_time < self.game_state.get_tick():
            # print('틱이 발동했다 2')  # tick-1 unittest 관련
            return
        self.last_tick_time = time.time() * 1000
        if self.active_window != self:
            if self.active_window.running:
                # print('틱이 다른 화면에서 작동했다.')  # tick-1 unittest 관련
                return
            else:
                self.game_state = self.active_window.game_state
                self.active_window = self
                print("return active to self")
        self.game_state.tick()
        self.update_labels_and_bars()
        # print('lables_and_bars()가 작동했음') # test_tick_2 관련
        if self.game_state.gameOver():  # 수정사항(12/13 : game_state의 hp = 0 대신 gameOver() 함수를 사용해서 캡슐화 진행했습니다.
            QMessageBox.warning(self, "Tamago", f"당신의 타마고치가 죽었습니다.\n레벨: {math.floor(self.game_state.experience / self.game_state.xp_per_level)} 경험치: {self.game_state.experience % self.game_state.xp_per_level}")
            self.tick_timer.stop()
            print('틱 타이머가 멈췄습니다.')  # test_tick_1 관련
            self.write_highscore()
            dv = DifficultyView.DifficultyView(self.game_state)
            self.active_window = dv
            dv.show()
            self.disable_button()

    def update_labels_and_bars(self):
        self.level_label.setText(f'Level: {math.floor(self.game_state.experience / self.game_state.xp_per_level)}')
        self.exp_label.setText(f'EXP : {self.game_state.experience % self.game_state.xp_per_level}')
        self.experience_bar.setText("|" * int(self.game_state.experience % self.game_state.xp_per_level / 4))
        self.hp_bar.setText("|" * int(self.game_state.hp / 4))
        self.satiety_bar.setText("|" * int(self.game_state.satiety / 4))
        self.hygiene_bar.setText("|" * int(self.game_state.hygiene / 4))
        self.drowsiness_bar.setText("|" * int(self.game_state.drowsiness / 4))

    def game_clicked(self):
        self.active_window = GameView.RPSGameWidget(game_state=self.game_state)
        self.active_window.show()

    def keyPressEvent(self, event):  # 나가는 이벤트 중복임 하나로 뭉치자.
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.writeSaveFile()
        self.close()

    def readTamago(self):
        try:
            with open(self.savefilename, "rb") as f:
                tamagodat = pickle.load(f)
                if self.game_state.gameOver():
                    raise Exception
                self.game_state = GameState(name=tamagodat["name"], experience=tamagodat["experience"], satiety=tamagodat["satiety"],
                                            hygiene=tamagodat["hygiene"], drowsiness=tamagodat["drowsiness"], hp=tamagodat["hp"])
                # print('저장된 파일이 있습니다. 불러오기를 진행합니다.') test_start_2에서 사용함
        except:
            text, ok = QInputDialog.getText(self, "Tamago", "타마고치의 이름을 입력해주세요")  # error 너무 긴 글자를 넣을 시 나중 결과창이 깨짐
            if ok:
                self.game_state = GameState(name=text)
                # print('저장된 파일이 없습니다. 입력된 이름으로 새로운 개체를 만듭니다. ') test_start_1, 3 에서 사용
            else:

                print('취소버튼을 눌렀습니다. 게잉을 종료합니다.')  # error 현재 에러사항으로 종료되지않음
                self.close()




    def writeSaveFile(self):
        with open(self.savefilename, 'wb') as f:
            pickle.dump({"name": self.game_state.name, "experience": self.game_state.experience, "satiety": self.game_state.satiety,
                         "hygiene": self.game_state.hygiene, "drowsiness": self.game_state.drowsiness,
                         "hp": self.game_state.hp}, f)

    def write_highscore(self):
        try:
            with open("scores.dat", "rb") as f:
                tamagodat = pickle.load(f)
                found = False
                for t in tamagodat:
                    if t["name"] == self.game_state.name:
                        t["score"] = math.floor(self.game_state.experience / self.game_state.xp_per_level)
                        found = True
                        break
                if not found:
                    tamagodat.append({"name": self.game_state.name, "level": math.floor(self.game_state.experience / self.game_state.xp_per_level)})
        except:
            tamagodat = [{"name": self.game_state.name, "level": math.floor(self.game_state.experience / self.game_state.xp_per_level)}]

        with open("scores.dat", "wb") as f:
            pickle.dump(tamagodat, f)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())