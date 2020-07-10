from gym.envs.registration import register

from gym_graph_traffic.envs.params import PARAMETERS

register(
    id="GraphTraffic-v0",
    entry_point='gym_graph_traffic.envs:GraphTrafficEnv'
)
