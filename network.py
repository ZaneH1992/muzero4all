from network_initializer import NetworkInitializer

#This is just a placeholder
class Action(object):
    """ Class that represent an action of a game."""

    def __init__(self, index: int):
        self.index = index

    def __hash__(self):
        return self.index

    def __eq__(self, other):
        return self.index == other.index

    def __gt__(self, other):
        return self.index > other.index

'''
    Interface for the output of the Network
'''
class NetworkOutput(typing.NamedTuple):
    value: float
    reward: float
    policy_logits: Dict[Action, float]
    hidden_state: List[float]

'''
    Generic network class, pass in the initializer for game model (Tic Tac Toe, or Atari)
    to build the model.
'''
class Network(object):

    def __init__(self, initializer: NetworkInitializer):
        (prediction_network, dynamics_network, representation_network) = initializer.initialize()
        self.representation = representation_network
        self.dynamics = dynamics_network
        self.prediction = prediction_network

    def initial_inference(self, image) -> NetworkOutput:
        # representation + prediction function
        return NetworkOutput(0, 0, {}, [])

    def recurrent_inference(self, hidden_state, action) -> NetworkOutput:
        # dynamics + prediction function
        return NetworkOutput(0, 0, {}, [])

    def get_weights(self):
        # Returns the weights of this network.
        return []

    def training_steps(self) -> int:
        # How many steps / batches the network has been trained for.
        return 0
