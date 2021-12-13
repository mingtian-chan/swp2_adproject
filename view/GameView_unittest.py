import unittest
from GameView import RPSGameWidget

class TestGameView(unittest.TestCase):
    def setUp(self):
        self.test = RPSGameWidget

    def tearDown(self):
        pass

    def test_play_rps(self):
        self.test.play_rps(self,'rock')
