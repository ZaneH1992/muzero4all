
import time
import unittest
import tensorflow as tf

from basic_mcts_model import BasicMctsModel
from mcts_policy import MctsPolicy
from pacman_det_env import PacmanDetEnv
from gym.envs.atari import atari_env
from network_initializer import TicTacToeInitializer, AtariInitializer, PacManInitializer
from network import Network
from muzero_collection_policy import MuZeroCollectionPolicy
from muzero_eval_policy import MuZeroEvalPolicy
from replay_buffer import ReplayBuffer
from tic_tac_toe_env import TicTacToeEnv


TRAIN_ITERATIONS = 200

PLAY_ITERATIONS = 5

NUM_TRAIN_STEPS = 20
NUM_UNROLL_STEPS = 5

initializer = AtariInitializer()
env = PacmanDetEnv(screen_images=True)
env.reset()

network = Network(initializer)
replay_buffer = ReplayBuffer()
col_policy = MuZeroCollectionPolicy(env, network, replay_buffer,
                                    num_simulations=50, max_moves=2000, discount=0.999)
eval_policy = MuZeroEvalPolicy(env, network, replay_buffer)

for train_iter in range(TRAIN_ITERATIONS):
    print('STARTING TRAINING ITERATION #{}'.format(train_iter))
    tf.summary.experimental.set_step(train_iter)
    for play_iter in range(PLAY_ITERATIONS):
        print('STARTING PLAY ITERATION #{}'.format(play_iter))
        start_time = time.time()
        col_policy.run_self_play(render=True)
        end_time = time.time()
        print('Self Play Iteration Runtime: {}'.format(end_time - start_time))
    eval_policy.train(NUM_TRAIN_STEPS, NUM_UNROLL_STEPS)

# TODO: pacman, save weights, tensorboard

idx = 0
total_reward = 0
env.reset()
while True:
    start_time = time.time()
    print('Starting action calculation')
    action = eval_policy.action()
    states, is_final, reward = env.step(action)
    total_reward += reward
    end_time = time.time()
    print('Action at iter %s: %s\nReward: %s\n'
        'TotalReward: %s\nCalc time: %s\n\n' 
        % (idx, action, reward, total_reward, 
            end_time - start_time))
    env.render()
    if is_final:
        print("Hit is_final!")
        break
    idx += 1
