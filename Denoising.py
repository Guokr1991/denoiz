from scipy import ndimage

"""
Denoising filter functions.
"""
def median_filter(input_data, window=3):
	input_2d = input_data.reshape(512,512)
	w_size = (window, window)
	output_2d = ndimage.filters.median_filter(input_2d, size=w_size, mode='mirror')
	return output_2d.flatten()


"""
The function passed to ndimage.generic_filter must map an array to a scalar. The array will be 1-dimensional, and contain the values from im which have been "selected" by the footprint.
"""


"""
Types of denoising that can be applied.
"""
denoising_dict = {
	'median' : median_filter,
}

