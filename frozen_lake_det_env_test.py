
import unittest

from gym.envs.toy_text.frozen_lake import LEFT
from gym.envs.toy_text.frozen_lake import RIGHT
from gym.envs.toy_text.frozen_lake import DOWN
from gym.envs.toy_text.frozen_lake import UP
from frozen_lake_det_env import FrozenLakeDetEnv


class FrozenLakeDetEnvTest(unittest.TestCase):

    def setUp(self):
        self.env = FrozenLakeDetEnv()

    def tearDown(self):
        self.env.env.close()

    def test_init(self):
        self.assertEqual('\nSFFF\nFHFH\nFFFH\nHFFG\n', self.env.get_real_states())

    def test_reset_get_states(self):
        actions = [RIGHT, RIGHT]
        for action in actions:
            new_states, is_final, reward = self.env.step(action)
        self.assertEqual([RIGHT, RIGHT], self.env.get_states())
        self.assertEqual([RIGHT, RIGHT], new_states)
        self.assertEqual([], self.env.reset())
        self.assertEqual('\nSFFF\nFHFH\nFFFH\nHFFG\n', self.env.get_real_states())
        self.assertEqual([], self.env.get_states())

    def test_set_states(self):
        self.env.set_states([RIGHT, RIGHT])
        self.assertEqual([RIGHT, RIGHT], self.env.get_states())
        self.assertEqual('  (Right)\nSFFF\nFHFH\nFFFH\nHFFG\n', self.env.get_real_states())
        self.env.set_states([RIGHT, RIGHT, DOWN, DOWN, DOWN])

        new_states, is_final, reward = self.env.step(RIGHT)

        self.assertTrue(is_final)
        self.assertEqual(1.0, reward)
        self.assertEqual([RIGHT, RIGHT, DOWN, DOWN, DOWN, RIGHT], new_states)
        self.assertEqual('  (Right)\nSFFF\nFHFH\nFFFH\nHFFG\n', self.env.get_real_states())
        # self.env.env.render()

    def test_win(self):
        actions = [RIGHT, RIGHT, DOWN, DOWN, DOWN]
        for action in actions:
            new_states, is_final, reward = self.env.step(action)
        self.assertFalse(is_final)
        self.assertEqual(0.0, reward)
        self.assertEqual(actions, new_states)
        self.assertEqual('  (Down)\nSFFF\nFHFH\nFFFH\nHFFG\n', self.env.get_real_states())

        new_states, is_final, reward = self.env.step(RIGHT)

        self.assertTrue(is_final)
        self.assertEqual(1.0, reward)
        self.assertEqual(actions + [RIGHT], new_states)
        self.assertEqual('  (Right)\nSFFF\nFHFH\nFFFH\nHFFG\n', self.env.get_real_states())
        # self.env.env.render()

    def test_hole(self):
        actions = [RIGHT, DOWN]
        for action in actions:
            new_states, is_final, reward = self.env.step(action)
        self.assertTrue(is_final)
        self.assertEqual(0.0, reward)  # NOTE: reward is not negative
        self.assertEqual(actions, new_states)
        self.assertEqual('  (Down)\nSFFF\nFHFH\nFFFH\nHFFG\n', self.env.get_real_states())
        # self.env.env.render()


if __name__ == '__main__':
    unittest.main()
