import numpy as np
def random_walk(l, N):

    teta = np.random.uniform(0, 2 * np.pi, N)
    dx = l * np.cos(teta)
    dy = l * np.sin(teta)
    
    x = np.cumsum(dx)
    y = np.cumsum(dy)
    
    return x, y