#!/usr/bin/python

import numpy as np
from scipy import misc, ndimage

gary = misc.imread('gary', flatten=True)
misc.imsave("gary1.bmp", gary)
gary_flat = gary.flatten()

def thres(gary_flat, t=100):tips
	""" Thressholding """
	gary2 = np.array([255 if x > t else 0 for x in gary_flat]).reshape(512,512)
	return gary2

def add_noise(gary_flat, i=1.0):
	"""
	Gaus : np.random.normal(mean, std_dev, num_elems)
	Uniform : np.random.uniform(low=0.0, high=1.0, size=1)
	Rayleigh : np.random.rayleigh(scale=1.0, size=None)
	"""
	noise = np.random.rayleigh(scale=i, size=gary_flat.size)
	return (gary_flat + noise).reshape(512,512)

gary_noise = add_noise(gary_flat,50)

misc.imsave("gary2.bmp", gary_noise)

gary_denoised = ndimage.filters.median_filter(gary_noise, size=(3,3), mode='mirror')

misc.imsave("gary3.bmp", gary_denoised)

gary_diff = gary - gary_denoised
misc.imsave("gary4.bmp", gary_diff)


"""
The function passed to ndimage.generic_filter must map an array to a scalar. The array will be 1-dimensional, and contain the values from im which have been "selected" by the footprint.
"""