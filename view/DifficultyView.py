import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import pickle
import math

class DifficultyView(QWidget):
    def __init__(self, game_state):
        super(DifficultyView, self).__init__(None)
        self.game_state = game_state
        self.running = True
        self.scoreboard_info = self.get_scoreboard()
        self.create_widgets()

    def create_widgets(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.level_slider = QSlider(Qt.Horizontal)
        self.level_slider.setMinimum(0)
        self.level_slider.setMaximum(self.game_state.expected_levels)
        self.level_slider.setValue(math.floor(self.game_state.expected_levels / self.game_state.xp_per_level))
        self.level_slider.valueChanged.connect(self.changeValue)

        self.text_box = QTextEdit()
        self.text_box.setReadOnly(True)
        self.text_box.setAlignment(Qt.AlignLeft)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.level_slider)
        layout.addWidget(self.text_box)
        self.setLayout(layout)
        self.plot(self.game_state.difficulty_factor)

    def plot(self, difficulty):
        xvals = np.linspace(0.1, 100.0, 100)
        y_satiety_loss = self.game_state.satiety_loss_func(xvals)
        y_drowsiness_loss = self.game_state.drowsiness_loss_func(xvals)
        y_eat_gain_func = self.game_state.eat_gain_func(xvals, difficulty)
        y_hp_loss = self.game_state.hp_loss_func(xvals)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(xvals, y_satiety_loss, "r", label="satiety_loss")
        ax.plot(xvals, y_drowsiness_loss, "g", label="drowsiness_loss")
        ax.plot(xvals, y_eat_gain_func, "b", label="eat_effect")
        ax.plot(xvals, y_hp_loss, "c", label="hp_loss")
        ax.legend()
        self.canvas.draw()

        information = f""" 최종 난이도 계수는 {difficulty:.4f}이며, 0을 가장 쉬운 난이도, 1을 설계상 가장 어려운 난이도로 볼 경우 {((self.game_state.base_difficulty_factor - difficulty)/(self.game_state.base_difficulty_factor - self.game_state.max_difficulty_factor)):.2f}에 해당하는 난이도입니다."""
        information += self.scoreboard_info
        self.text_box.setText(information)

    def get_scoreboard(self):
        scoreboard_info = "\n-----순위표-----"
        scoreboard_info += f"\n이름- 레벨\n"
        try:
            with open("scores.dat", "rb") as f:
                tamagodat = pickle.load(f)

            scoreboard_info += "\n".join(f"{tg['name']} - {tg['level']}" for tg in sorted(tamagodat, key= lambda x: x["level"], reverse=True))
        except:
            return ""
        return scoreboard_info

    def changeValue(self):
        level = self.level_slider.value()
        difficulty = self.game_state.base_difficulty_factor + level * (self.game_state.base_difficulty_factor - self.game_state.max_difficulty_factor) / -self.game_state.expected_levels
        self.plot(difficulty)

    def closeEvent(self, a0) -> None:
        self.running = False
        self.close()

if __name__ == '__main__':
    import sys
    from game_manager import GameState
    app = QApplication(sys.argv)
    dv = DifficultyView(GameState())
    dv.show()
    sys.exit(app.exec_())