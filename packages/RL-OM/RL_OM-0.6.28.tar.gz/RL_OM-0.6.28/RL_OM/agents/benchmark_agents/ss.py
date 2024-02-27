# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/agents/benchmark_agents/12_SS.ipynb.

# %% auto 0
__all__ = ['SSAgent', 'SSPolicy']

# %% ../../../nbs/agents/benchmark_agents/12_SS.ipynb 4
# General libraries:
import numpy as np
from scipy.stats import norm
from tqdm import tqdm

# Mushroom libraries
from mushroom_rl.core import Agent

# %% ../../../nbs/agents/benchmark_agents/12_SS.ipynb 6
class SSAgent(Agent):

    """
    Agent implementing the QR policy.

    # TODO adjust description

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
                  mdp,
                  s, # fixed ordering cost
                  h, # holding cost per unit per period
                  l, # lead time
                  p, # penalty cost per unit
                  unit_size = 0.01,
                  preprocessors = None,
                  postprocessors = None,
                  agent_name = None,
                  precision = 5,
                  num_iterations_per_parameter = 12,
                  include_l = True,
                  algorithm = "brute_0_1", # "brute_0_1": brute force for demand between 0 and 1 and unit-size <1, "brute_variable": brute force for demand large 1 and unit size 1 
                  search_space = 3 # applies only for brute_variable - grid size in multiple of average demand
        ):

        mdp._mdp_info.horizon = mdp.demand.shape[0]
        mdp.reset(0)

        policy = SSPolicy(
            d = None,
            s = s,
            h = h,
            l = l,
            p = p,
            mdp = mdp,
            unit_size = unit_size,
            preprocessors = preprocessors,
            postprocessors = postprocessors,
            num_iterations_per_parameter = num_iterations_per_parameter,
            include_l = include_l,
            algorithm = algorithm,
            search_space = search_space
        )

        self.precision=precision

        if agent_name is None:
            self.name = 'SSAgent'
        else:
            self.name = agent_name
        
        self.train_directly=True
        self.train_mode = "direct"

        super().__init__(mdp_info, policy)


    def fit(self, features = None, demand=None):

        """ 
        Fit the QR policy to the given demand.

        # TODO adjust description

        This method allows the EOQ agent to adapt its policy to historic demand data, assuming a fixed demand rate without uncertainty.

        Parameters:
            demand (numpy.ndarray): The demand for each period and product. The array should have the shape (num_products, num_periods).

        Returns:
            None
        """

        assert isinstance(demand, np.ndarray)
        assert demand.ndim == 2

        self.policy.set_s_S(demand, self._preprocessors[0])

class SSPolicy():

    """
    Policy implementing the QR strategy.

    Notethat d, s, and h must all have the shape (num_products,)

    # TODO adjust description

    Args:
        d (numpy.ndarray): The (average) demand per period for each product.
        s (numpy.ndarray): The fixed ordering cost for each product.
        h (numpy.ndarray): The holding cost per unit per period for each product.
        l (numpy.ndarray): The lead time per product.
        postprocessors (list): List of postprocessors to be applied to the action.

    Attributes:
        d (numpy.ndarray): The (average) demand per period for each product.
        s (numpy.ndarray): The fixed ordering cost for each product.
        h (numpy^.ndarray): The holding cost per unit per period for each product.
        l (numpy.ndarray): The lead time per product.
        num_products (int): The number of products.
        q_star (numpy.ndarray): The optimal order quantity per product.
        postprocessors (list): List of postprocessors to be applied to the action.

    """

    def __init__(self,
                 d, 
                 s, 
                 h, 
                 l, 
                 p,
                 mdp,
                 unit_size = 0.01,
                 preprocessors = None,
                 postprocessors = None,
                 num_iterations_per_parameter = 12,
                 include_l = True,
                 algorithm = "brute_0_1", # "brute_0_1": brute force for demand between 0 and 1 and unit-size <1, "brute_0_1": brute force for demand large 1 and unit size 1
                 search_space = 3 # applies only for brute_variable - grid size in multiple of average demand
                 ):
        self.d = d
        self.c_s = s
        self.h = h
        self.l = l
        self.p = p
        self.unit_size = unit_size
        self.num_products = len(s)

        if preprocessors is None:
            self.preprocessors = []
        else:
            self.preprocessors = (preprocessors)
        if postprocessors is None:
            self.postprocessors = []
        else:
            self.postprocessors = (postprocessors)

        self.mdp = mdp

        self.num_iterations_per_parameter = num_iterations_per_parameter

        self.include_l = include_l

        self.s = 0.5 # initial value
        self.S = 0.5 # initial value

        self.algorithm = algorithm
        self.search_space = search_space
    
    def set_and_calculate_grid(self, s, S, step_size, plot=False):

        s_candidates = np.arange(s-step_size*self.num_iterations_per_parameter, s+step_size*self.num_iterations_per_parameter, step_size)
        S_candidates = np.arange(S-step_size*self.num_iterations_per_parameter, S+step_size*self.num_iterations_per_parameter, step_size)

        # only use positive or zero candidates
        s_candidates = s_candidates[s_candidates >= -0.1]
        S_candidates = S_candidates[S_candidates >= 0]

        cost_matrix = np.zeros((len(s_candidates), len(S_candidates)))

        best_s, best_S, best_cost, _ = self.calculate_grid(s_candidates, S_candidates)

        return best_s, best_S, best_cost

    def calculate_grid(self, s_candidates, S_candidates):
    
        cost_matrix = np.zeros((len(s_candidates), len(S_candidates)))

        for i, s_candidate in enumerate(s_candidates):
            for j, S_candidate in enumerate(S_candidates):
                cost_value = self.run_simulation(s_candidate, S_candidate)

                cost_matrix[i, j] = cost_value
                print("s:", np.round(s_candidate,2), "S:", np.round(S_candidate,2), "cost:", np.round(cost_value))

        best_cost = np.min(cost_matrix)
        best_s_index, best_S_index = np.unravel_index(np.argmin(cost_matrix), cost_matrix.shape)
        best_s = s_candidates[best_s_index]
        best_S = S_candidates[best_S_index]

        print("max s index:", len(s_candidates), "best s index:", best_s_index)
        print("max S index:", len(S_candidates), "best S index:", best_S_index)

        print("best s and S:", best_s, best_S)

        if best_s_index == 0 or best_s_index == len(s_candidates)-1:
            warn_edge = True
        elif best_S_index == 0 or best_S_index == len(S_candidates)-1:
            warn_edge = True
        else:
            warn_edge = False

        return best_s, best_S, best_cost, warn_edge
    
    def run_simulation(self, s, S):

        total_cost = 0

        state = self.mdp.reset(0)

        for t in range(self.mdp.info.horizon):

            state = self.preprocessor(state)
            action = self.draw_action_train(state, s, S)
                
            state, reward, _, _ = self.mdp.step(action)
            
            total_cost += -reward

        return total_cost

    def set_s_S(self, demand, preprocessor):
        
        """
        Set the optimal order quantity (q_star) for each product.

        This method calculates and assigns the optimal order quantity based on the EOQ formula.

        Returns:
            None

        """

        self.preprocessor = preprocessor

        if self.algorithm == "brute_0_1":

            self.s, self.S, cost = self.set_and_calculate_grid(self.s, self.S, step_size = self.unit_size*10)
            print("iteration 1:", "s:", self.s, "S:", self.S, "cost:", cost)
            self.s, self.S, cost = self.set_and_calculate_grid(self.s, self.S, step_size = self.unit_size*3)
            print("iteration 2:", "s:", self.s, "S:", self.S, "cost:", cost)
            self.s, self.S, cost = self.set_and_calculate_grid(self.s, self.S, step_size = self.unit_size)
            print("iteration 4:", "s:", self.s, "S:", self.S, "cost:", cost)
        
        elif self.algorithm == "brute_variable":
            self.run_brute_variable(demand)
        
        else:
            # error
            raise ValueError("Algorithm not implemented")
    
    def run_brute_variable(self, demand):

        # starting reorder point average demand times lead time
        self.s = np.mean(demand) * np.max(self.l)
        eoq = np.sqrt(2 * np.mean(demand) * self.c_s/self.h)
        self.S = eoq + self.s

        self.s = np.round(self.s)
        self.S = np.round(self.S)

        # define search space

        unit_size = 10
        counter_outer = 0

        while unit_size >= 1:

            if counter_outer == 0:
                unit_size = np.mean(demand)*self.search_space/10
                # print("unit_sie:", unit_size)
                unit_size = np.maximum(unit_size, 1)
                # print("unit_sie:", unit_size)
                unit_size = np.round(unit_size)

                # print("unit size:", unit_size)

            warn_edge = True
            counter = 0
            while warn_edge:
                search_space_s = np.arange(self.s-unit_size*10, self.s+unit_size*10, unit_size)
                search_space_S = np.arange(self.S-unit_size*10, self.S+unit_size*10, unit_size)

                # print("averfage demand:", np.mean(demand))
                # print("search space s:", search_space_s)
                # print("search space S:", search_space_S)

                # only use positive or zero candidates
                search_space_s = search_space_s[search_space_s >= -0.1]
                search_space_S = search_space_S[search_space_S >= 0]
                self.s, self.S, cost, warn_edge = self.calculate_grid(search_space_s, search_space_S)

                # print("s:", self.s, "S:", self.S, "cost:", cost)

                counter += 1
                if counter > 10:
                    print("Warning: search space too large, no convergence")
                    break

            if unit_size == 1:
                break
        
            counter_outer += 1

            unit_size = unit_size/3
            unit_size = np.maximum(unit_size, 1)
            unit_size = np.round(unit_size)

    def draw_action(self, input):

        """
        Generate an action based on the current state.

        # TODO adjust description

        Returns zero for products which have still sufficient inventory, and the optimal order quantity for products which are running out of stock.

        Parameters:
            input (numpy.ndarray): The current inventory level and potentially order pipeline for each product.

        Returns:
            numpy.ndarray: The action to be taken, indicating the quantity to order for each product.

        """

        for preprocessor in self.preprocessors:
            input = preprocessor(input)

        if self.include_l:
            total_inventory_position = np.sum(input)
            if total_inventory_position <= self.s:
                q = self.S - total_inventory_position
            else:
                q = 0 
        else:
            print("Only policy based on total inventory position implemented")
        
        #print(input, total_inventory_position, self.s, self.S, q)

        action = np.array([q])

        for postprocessor in self.postprocessors:
            action = postprocessor(action)

        return action
    
    def draw_action_train(self, input, s, S):

        """
        Generate an action based on the current state.

        # TODO adjust description

        Returns zero for products which have still sufficient inventory, and the optimal order quantity for products which are running out of stock.

        Parameters:
            input (numpy.ndarray): The current inventory level and potentially order pipeline for each product.

        Returns:
            numpy.ndarray: The action to be taken, indicating the quantity to order for each product.

        """

        #print("R:", R, "Q:", Q)

        for preprocessor in self.preprocessors:
            input = preprocessor(input)

        if self.include_l:
            total_inventory_position = np.sum(input)
            if total_inventory_position <= s:
                q = S - total_inventory_position
            else:
                q = 0 

        #print(input, total_inventory_position, self.s, self.S, q)
                        
        action = np.array([q])

        for postprocessor in self.postprocessors:
            action = postprocessor(action)

        return action
    
    def reset(self):
        pass
