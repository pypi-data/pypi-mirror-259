# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/agents/benchmark_agents/11_EOQ.ipynb.

# %% auto 0
__all__ = ['EOQAgent', 'EOQPolicy']

# %% ../../../nbs/agents/benchmark_agents/11_EOQ.ipynb 4
# General libraries:
import numpy as np

# Mushroom libraries
from mushroom_rl.core import Agent

# %% ../../../nbs/agents/benchmark_agents/11_EOQ.ipynb 6
class EOQAgent(Agent):

    train_directly=True
    train_mode = "direct"

    """
    Agent implementing the Economic Order Quantity (EOQ) policy.

    Args:
        mdp_info (MDPInfo): Information about the Markov Decision Process (MDP).
        s (numpy.ndarray): The fixed ordering cost.
        h (numpy.ndarray): The holding cost per unit per period.
        l (numpy.ndarray): The lead time per product.
        preprocessors (list): List of preprocessors to be applied to the state.
        postprocessors (list): List of postprocessors to be applied to the policy.
        agent_name (str): Name of the agent. If set to None will use some default name.
        precision (int): Number of decimal places to round the demand input to.

    Attributes:
        mdp_info (MDPInfo): Information about the Markov Decision Process (MDP).
        policy (EOQPolicy): The EOQ policy implemented by the agent.

    """


    def __init__(self,
                  mdp_info,
                  s, # fixed ordering cost
                  h, # holding cost per unit per period
                  l = None, # lead time
                  preprocessors = None,
                  postprocessors = None,
                  agent_name = None,
                  precision = 5,
                  **kwargs
        ):

        policy = EOQPolicy(
            d = np.zeros(mdp_info.action_space.shape),
            s = s,
            h = h,
            l = l,
            preprocessors = preprocessors,
            postprocessors = postprocessors
        )

        self.precision=precision

        if agent_name is None:
            self.name = 'EOQAgent'
        else:
            self.name = agent_name

        super().__init__(mdp_info, policy)

    def fit(self, features, demand):

        """ 
        Fit the EOQ policy to the given demand.

        This method allows the EOQ agent to adapt its policy to historic demand data, assuming a fixed demand rate without uncertainty.

        Parameters:
            demand (numpy.ndarray): The demand for each period and product. The array should have the shape (num_products, num_periods).

        Returns:
            None

        """


        assert isinstance(demand, np.ndarray)
        assert demand.ndim == 2

        print(demand.shape)
        print(np.round(np.mean(demand, axis=0), self.precision))

        self.policy.d = np.round(np.mean(demand, axis=0), self.precision)

        self.policy.set_q_star()

class EOQPolicy():

    """
    Policy implementing the Economic Order Quantity (EOQ) strategy.

    Notethat d, s, and h must all have the shape (num_products,)

    Args:
        d (numpy.ndarray): The (average) demand per period for each product.
        s (numpy.ndarray): The fixed ordering cost for each product.
        h (numpy.ndarray): The holding cost per unit per period for each product.
        l (numpy.ndarray): The lead time per product.
        postprocessors (list): List of postprocessors to be applied to the action.

    Attributes:
        d (numpy.ndarray): The (average) demand per period for each product.
        s (numpy.ndarray): The fixed ordering cost for each product.
        h (numpy.ndarray): The holding cost per unit per period for each product.
        l (numpy.ndarray): The lead time per product.
        num_products (int): The number of products.
        q_star (numpy.ndarray): The optimal order quantity per product.
        postprocessors (list): List of postprocessors to be applied to the action.

    """

    def __init__(self,
                 d, 
                 s, 
                 h, 
                 l = None,
                 preprocessors = None,
                 postprocessors = None
                 ):
        self.d = d
        self.s = s
        self.h = h
        self.l = l
        self.num_products = len(s)
        self.q_star = 0.5
        if preprocessors is None:
            self.preprocessors = []
        else:
            self.preprocessors = (preprocessors)
        if postprocessors is None:
            self.postprocessors = []
        else:
            self.postprocessors = (postprocessors)

    def set_q_star(self):
        
        """
        Set the optimal order quantity (q_star) for each product.

        This method calculates and assigns the optimal order quantity based on the EOQ formula.

        Returns:
            None

        """

        self.q_star = np.sqrt((2*self.s*self.d)/self.h)

        print("q_star: ", self.q_star)

    def draw_action(self, input):

        """
        Generate an action based on the current state.

        Returns zero for products which have still sufficient inventory, and the optimal order quantity for products which are running out of stock.

        Parameters:
            input (numpy.ndarray): The current inventory level and potentially order pipeline for each product.

        Returns:
            numpy.ndarray: The action to be taken, indicating the quantity to order for each product.

        """

        action = np.zeros(self.num_products)

        for preprocessor in self.preprocessors:
            input = preprocessor(input)

        if self.l is None:
            action = np.where(input >= self.d, 0, self.q_star)

        else:
            pipeline_vector = input[self.num_products:]
            pipeline = np.reshape(pipeline_vector, (self.num_products, max(self.l)))
            pipeline_sum = np.sum(pipeline, axis=1)
            inventory = input[:self.num_products]
            # print("printing inventory, pipeline, lead time, average demand")
            # print(inventory)
            # print(pipeline_sum)
            inventory_position = inventory + pipeline_sum
            # print(self.l)
            # print(self.d)
            action = np.where((inventory_position-self.l*self.d >= 0), 0, self.q_star)
            # print("action: ", action)

        for postprocessor in self.postprocessors:
            action = postprocessor(action)

        return action
    
    def reset(self):
        pass
