
import numpy as np
import tensorflow as tf

from mcts_core import MctsCore
from muzero_mcts_model import MuZeroMctsModel
from policy import Policy
from network import Network


class MuZeroCollectionPolicy(Policy):
    """Policy for MuZero."""

    def __init__(self, env, network, replay_buffer=None, num_simulations=100, discount=1.,
                 rng: np.random.RandomState = np.random.RandomState()):
        self.network = network
        self.replay_buffer = replay_buffer
        self.model = MuZeroMctsModel(env, self.network)
        # env is used only for the action space.
        self.core = MctsCore(env, self.model, discount=discount)
        self.num_simulations = num_simulations
        self.rng = rng

    def reset(self):
        self.model.reset()

    def get_policy_logits(self):
        self.core.initialize()
        for _ in range(self.num_simulations):
            self.core.rollout()
        policy_logits = tf.convert_to_tensor(self.core.get_policy_distribution())
        # policy_logits = tf.expand_dims(policy_logits, 0)  # batch_size=1
        # print (policy_logits)
        return policy_logits

    def choose_action(self, logits):
        # tf.random.set_seed(self.r_seed)
        # action = tf.random.categorical(logits=tf.math.log(logits), num_samples=1, seed=self.r_seed)
        # self.r_seed += 1
        # action = tf.squeeze(action)
        # action = np.random.choice(a=np.array(logits))
        # return action
        # TODO: break tie randomly.
        action = tf.math.argmax(logits)
        return action

    def action(self):
        return self.choose_action(self.get_policy_logits())

    def run_self_play(self, num_times):
        for _ in range(num_times):
            p = self.get_policy_logits()
            v = self.get_value()
            best_action = self.choose_action(p)
            states, is_final, reward = self.env.step(best_action)
            self.feed_replay_buffer(p, v, best_action, reward)

    def feed_replay_buffer(self, p, v, best_action, reward):
        # TODO: implement this
        pass


