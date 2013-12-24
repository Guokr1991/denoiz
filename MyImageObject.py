#!/usr/bin/python

import numpy as np
from scipy import misc, ndimage

from Noises import noises_dict
from Denoising import denoising_dict


class MyImageObject():
	"""
	Python object to contain image objects and methods.
	Working on 512 x 512 B&W images only. (262144 bytes)
	Images stored as flat data, use return methods to get them reshaped.
	"""
	def __init__(self, filename):
		image_data = misc.imread(filename, flatten=True).flatten()
		if len(image_data) != 262144:
			raise Exception("Error: Image must be 512 x 512 pixels big.")
		self.original_filename = filename
		self.original_image = image_data
		self.noisy_image = None
		self.denoised_image = None

	def __str__(self):
		return "MyImageObject::'" + self.original_filename + "'"

	def get_thresholded_image(self, t):
		""" Thressholding around value t """
		return np.array([255 if x > t else 0 for x in self.original_image])

	def return_thresholded_image(self, t=.5):
		return self.get_thresholded_image(t).reshape(512,512)

	# Adding noise.

	def get_noisy_image(self, first_par, second_par, noise_type):
		noise_function = noises_dict.get(noise_type, None)
		noise = noise_function(first_par, second_par)
		return (self.original_image + noise)

	def set_noisy_image(self, noise_pars, noise_type):
		p1, p2 = noise_pars
		self.noisy_image = self.get_noisy_image(p1, p2, noise_type)

	def return_noisy_image(self):
		return self.noisy_image.reshape(512,512)

	# Removing noise.

	def remove_noise(self):
		denoising_filter = denoising_dict.get('median', None)
		self.denoised_image = denoising_filter(self.noisy_image)

	def return_denoised_image(self):
		return self.denoised_image.reshape(512,512)

	# Analysis.

	def return_difference_image(self):
		difference = self.original_image - self.denoised_image
		return difference.reshape(512, 512)


if __name__ == "__main__":
	"""
	noise = gaus_noise(0, 5)
	noise = uniform_noise(-10,10)
	noise = rayleigh_noise(20)
	"""
	noise_type = 'gaus'
	noise_pars = (1, 5,)
	input_filename = "gary_PRAVI.bmp" #"lena.png"
	output_filename = "gary_o" #"lena_o"
	output_filetype = "bmp"

	try:
		im_obj = MyImageObject(input_filename)
		print "Instantiated MyImageObject: ", im_obj
		misc.imsave("IREADTHIS.bmp", im_obj.original_image.reshape(512,512))

		# Adding noise...
		im_obj.set_noisy_image(noise_pars, noise_type)
		print "Added %s noise." % noise_type
		ny_img = im_obj.return_noisy_image()
		ny_filename = output_filename + "_noisy." + output_filetype
		misc.imsave(ny_filename, ny_img)

		# Denoising...
		im_obj.remove_noise()
		print "Removed noise."
		dn_img = im_obj.return_denoised_image()
		dn_filename = output_filename + "_denoised." + output_filetype
		misc.imsave(dn_filename, dn_img)

		# Analysis...
		df_img = im_obj.return_difference_image()
		df_filename = output_filename + "_difference." + output_filetype
		misc.imsave(df_filename, df_img)

	except Exception as e:
		print e