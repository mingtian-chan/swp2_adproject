import unittest

import game_manager
from game_manager import GameState

class TestGameManager(unittest.TestCase):

    def setUp(self):
        self.g1 = GameState(name='abcd', experience=0, satiety=0, hygiene=100, drowsiness=100, hp=100)
        self.g1.eat_integral.append(1.1)
        self.g1.eat_integral.append(1.0)

        self.g2 = GameState(name='abcd', experience=0, satiety=59.23618525000001, hygiene=100, drowsiness=100, hp=100)
        self.g2.eat_integral.append(59.23618525000001)

        self.g3 = GameState(name='abcd', experience=0, satiety=0, hygiene=100, drowsiness=100, hp=100)
        self.g3.eat_integral.append(0)

        self.g4 = GameState(name='abcd', experience=0, satiety=80, hygiene=100, drowsiness=100, hp=100)
        self.g4.eat_integral.append(80)

        self.val80 = GameState(name='abcd', experience=0, satiety=100, hygiene=80, drowsiness=80, hp=100)

        self.val20 = GameState(name='abcd', experience=0, satiety=100, hygiene=20, drowsiness=20, hp=100)

    def tearDown(self):
        pass

    # def test_g1(self):  # 작은 값에서 시작하면 큰 값으로 증가합니다.
    #     self.assertEqual(self.g1.satiety,0)
    #     self.g1.eat()
    #     self.assertEqual(self.g1.satiety,59.23618525000001)
    #
    # def test_g2(self):  # 큰 값에서 시작하면 그 증가분은 크지않습니다.
    #     self.g2.eat()
    #     self.assertEqual(self.g2.satiety,64.26279324374127)
    #
    # def test_increasement(self):  # 배고픔이 작을수록 증가량은 더 큽니다.
    #     g3_tmp = self.g3.satiety
    #     g4_tmp = self.g4.satiety
    #     self.g3.eat()
    #     self.g4.eat()
    #     self.assertGreater(self.g3.satiety-g3_tmp, self.g4.satiety-g4_tmp)

    def test_sleepMethod1(self):  # 졸림이 80일때 sleep함수를 사용 할 경우
        self.assertEqual(self.val80.drowsiness, 80)
        self.assertEqual(self.val80.experience, 0)
        self.val80.sleep()
        self.assertEqual(self.val80.hygiene, 80)  # 청결은 80으로 변하지 않고
        self.assertEqual(self.val80.drowsiness, 100)  # 졸림은 100이 되며
        self.assertEqual(self.val80.experience, 5)  # 경험치는 5가 오릅니다.

    def test_sleepMethod2(self):  # 졸림이 20일때 sleep함수를 사용 할 경우
        self.assertEqual(self.val20.drowsiness, 20)
        self.assertEqual(self.val20.experience, 0)
        self.val20.sleep()
        self.assertEqual(self.val20.hygiene, 20)  # 청결은 20으로 변하지 않고
        self.assertEqual(self.val20.drowsiness, 100)  # 졸림은 100이 되며
        self.assertEqual(self.val20.experience, 20)  # 경험치는 20이 오릅니다.

    def test_washMethod1(self):  # 청결이 80일때 wash함수를 사용 할 경우
        self.assertEqual(self.val80.hygiene, 80)
        self.assertEqual(self.val80.experience, 0)
        self.val80.wash()
        self.assertEqual(self.val80.hygiene, 100)  # 청결은 100이 되며
        self.assertEqual(self.val80.drowsiness, 80)  # 졸림은 80으로 변하지 않고
        self.assertEqual(self.val80.experience, 5)  # 경험치는 5가 오릅니다.

    def test_washMethod2(self):  # 청결은 20일때 wash함수를 사용 할 경우
        self.assertEqual(self.val20.hygiene, 20)
        self.assertEqual(self.val20.experience, 0)
        self.val20.wash()
        self.assertEqual(self.val20.hygiene, 100)  # 청결은 1000이 되며
        self.assertEqual(self.val20.drowsiness, 200)  # 졸림은 20으로 변하지 않고
        self.assertEqual(self.val20.experience, 20)  # 경험치는 20이 오릅니다.




if __name__ == '__main__':
    unittest.main()