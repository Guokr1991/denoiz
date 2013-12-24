import numpy as np

"""
Methods that return flat arrays of various noise samples.
"""
def gaus_noise(mean, std_dev, num_elems=262144):
	""" Gaus : np.random.normal(mean, std_dev, num_elems) """
	return np.random.normal(loc=mean, scale=std_dev, size=num_elems)

def uniform_noise(low=0.0, high=1.0, num_elems=262144):
	""" Uniform : np.random.uniform(low=0.0, high=1.0, num_elems=1) """
	return np.random.uniform(low, high, num_elems)

def rayleigh_noise(scale=1.0, ignored=None, num_elems=262144):
	""" Rayleigh : np.random.rayleigh(scale=1.0, size=None) """
	return np.random.rayleigh(scale, size=num_elems)


"""
Types of noises that can be added.
"""
noises_dict = {
	'gaus' : gaus_noise,
	'uniform' : uniform_noise,
	'rayleigh' : rayleigh_noise,
}