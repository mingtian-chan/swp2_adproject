import unittest
from game_manager import GameState

class TestGameManager(unittest.TestCase):

    def setUp(self):
        self.eat_sat0 = GameState(name='abcd', experience=0, satiety=0, hygiene=100, drowsiness=100, hp=100)
        self.eat_sat0.eat_integral.append(1.0)

        self.eat_sat60 = GameState(name='abcd', experience=0, satiety=60, hygiene=100, drowsiness=100, hp=100)
        self.eat_sat60.eat_integral.append(60.0)

        self.val80 = GameState(name='abcd', experience=0, satiety=100, hygiene=80, drowsiness=80, hp=100)

        self.val20 = GameState(name='abcd', experience=0, satiety=100, hygiene=20, drowsiness=20, hp=100)

    def tearDown(self):
        pass

    def test_eat_sat0(self):  # 작은 값에서 시작하면 증가량은 큽니다.
        self.assertEqual(self.eat_sat0.satiety,0)  # 배고픔이 0인 경우
        self.eat_sat0.eat()
        self.assertEqual(self.eat_sat0.satiety,29.648025000000004)  # 증가량 = 29.648025000000004
        self.assertGreater(self.eat_sat0.experience,0)


    def test_eat_sat60(self):  # 큰 값에서 시작하면 그 증가량은 작습니다.
        self.assertEqual(self.eat_sat60.satiety, 60)  # 배고픔이 60인 경우
        self.eat_sat60.eat()
        self.assertEqual(self.eat_sat60.satiety,64.84)  # 증가량 = 4.84
        self.assertGreater(self.eat_sat60.experience,0)

    def test_eat_compare(self):  # 배고픔 수치가 낮을수록 배고픔 증가량은 더 큽니다.
        g3_tmp = self.eat_sat0.satiety  # 배고픔이 0인 경우
        g4_tmp = self.eat_sat60.satiety  # 배고픔이 60인 경우
        self.eat_sat0.eat()
        self.eat_sat60.eat()
        self.assertGreater(self.eat_sat0.satiety-g3_tmp, self.eat_sat60.satiety-g4_tmp)

    def test_sleepMethod1(self):  # 졸림이 80일때 sleep함수를 사용 할 경우
        self.assertEqual(self.val80.drowsiness, 80)
        self.assertEqual(self.val80.experience, 0)
        self.val80.sleep()
        self.assertEqual(self.val80.hygiene, 80)  # 청결은 80으로, 변하지 않고
        self.assertEqual(self.val80.drowsiness, 100)  # 졸림은 100이 되며
        self.assertEqual(self.val80.experience, 5)  # 경험치는 5가 오릅니다.

    def test_sleepMethod2(self):  # 졸림이 20일때 sleep함수를 사용 할 경우
        self.assertEqual(self.val20.drowsiness, 20)
        self.assertEqual(self.val20.experience, 0)
        self.val20.sleep()
        self.assertEqual(self.val20.hygiene, 20)  # 청결은 20으로, 변하지 않고
        self.assertEqual(self.val20.drowsiness, 100)  # 졸림은 100이 되며
        self.assertEqual(self.val20.experience, 20)  # 경험치는 20이 오릅니다.

    def test_washMethod1(self):  # 청결이 80일때 wash함수를 사용 할 경우
        self.assertEqual(self.val80.hygiene, 80)
        self.assertEqual(self.val80.experience, 0)
        self.val80.wash()
        self.assertEqual(self.val80.hygiene, 100)  # 청결은 100이 되며
        self.assertEqual(self.val80.drowsiness, 80)  # 졸림은 80으로, 변하지 않고
        self.assertEqual(self.val80.experience, 5)  # 경험치는 5가 오릅니다.

    def test_washMethod2(self):  # 청결은 20일때 wash함수를 사용 할 경우
        self.assertEqual(self.val20.hygiene, 20)
        self.assertEqual(self.val20.experience, 0)
        self.val20.wash()
        self.assertEqual(self.val20.hygiene, 100)  # 청결은 100이 되며
        self.assertEqual(self.val20.drowsiness, 20)  # 졸림은 20으로, 변하지 않고
        self.assertEqual(self.val20.experience, 20)  # 경험치는 20이 오릅니다.

if __name__ == '__main__':
    unittest.main()