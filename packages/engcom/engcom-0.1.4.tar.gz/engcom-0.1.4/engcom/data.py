"""Module that generates data sets"""
import numpy as np


def step_response(
    time=None,
    ntime=101,
    maxtime=10,
    noisy=True,
    system_order=2,
    damping_ratio=0.5,
    natural_freq=1,
    time_constant=1,
):
    """Returns simulated step response data through time"""
    # Time
    if not time:
        time = np.linspace(0, maxtime, ntime)
    elif type(time) != np.ndarray:
        time = np.array(time)
    # Response Definition
    if system_order > 2:
        raise (ValueError("Paremeter system_order must be < 3."))
    if system_order == 1:
        def response(t):
            return np.exp(-t / time_constant)
    elif system_order == 2:
        l1 = (
            -damping_ratio * natural_freq
            + natural_freq * np.emath.sqrt(damping_ratio**2 - 1)
        )
        l2 = (
            -damping_ratio * natural_freq
            - natural_freq * np.emath.sqrt(damping_ratio**2 - 1)
        )
        def response(t):
            return (
                1
                / natural_freq**2
                * (
                    1
                    - 1
                    / (l2 - l1)
                    * (l2 * np.exp(l1 * t) - l1 * np.exp(l2 * t))
                )
            )

    # Response and Noise
    y = np.real(response(time))
    u = np.ones(y.shape)
    if noisy:
        std = 0.01 * max(y)
        y = y + std * np.random.standard_normal(y.shape)
    return {
        "time": time,
        "input": u,
        "output": y
    }

def policy_adoption():
    """Returns predicted probability data for policy adoption 
    vs percent of group in favor of policy. 
    Groups: average citizens and economic elites
    
    From Martin Gilens and Benjamin I. Page article
    Testing Theories of American Politics: Elites, Interest Groups, and Average Citizens
    http://dx.doi.org/10.1017/S1537592714001595
    Values read visually from Figure 1
    """
    percent_favoring_policy_change = np.array(range(10,110,10))
    predicted_prob_of_adoption_average = np.array([0.3, 0.3, 0.31, 0.31, 0.31, 0.31, 0.31, 0.32, 0.32, 0.33])
    predicted_prob_of_adoption_elite = np.array([0.01, 0.13, 0.2, 0.25, 0.3, 0.33, 0.37, 0.42, 0.48, 0.6])
    return {
        "percent_favoring_policy": percent_favoring_policy_change,
        "adoption_average": predicted_prob_of_adoption_average,
        "adoption_elite": predicted_prob_of_adoption_elite,
    }
    
def ideal_gas(
    V=None,
    T=None,
    n=1, 
    R=8.3145,
    noisy=True,
):
    """Returns ideal gas law data (Pressure vs Volume and Pressure)"""
    def pressure(V, n=1, R=8.3145, T=273.15):
        """Ideal gas law"""
        return n * R * T / V
    if V is None:
        V = np.linspace(1, 2, 11)
    elif type(V) == int:
        V = np.linspace(1, 2, V)
    elif type(V) == range:
        V = np.array(V)
    V = np.reshape(V, (len(V), 1))
    if T is None:
        T = np.linspace(273.15, 573.15, 4)
    elif type(T) == int:
        T = np.linspace(273.15, 573.15, T)
    elif type(T) == range:
        T = np.array(T)
    T = np.reshape(T, (1, len(T)))
    P = pressure(V, T)
    if noisy:
        if type(noisy) == int or type(noisy) == float:
            std = noisy * (np.max(P) - np.min(P))  # Standard deviation is scaled by noisy
        else:
            std = 0.01 * (np.max(P) - np.min(P))
        P = P + std * np.random.standard_normal(P.shape)
    return {
        "volume": V,
        "temperature": T,
        "pressure": P,
    }

def movie_ratings_binned():
    """The author's movie rating frequencies for 89 movies, 
    in 10 bins of size 1 from 0-10
    """
    return np.array([0, 1, 6, 6, 18, 18, 20, 13, 5, 2])