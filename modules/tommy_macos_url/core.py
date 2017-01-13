"""
Tommy URL opener for macos
Standard module for url on macos
"""
import os
from tommy.core.module import Module


class Core(Module):
	"""
	Core of tommy_macos_url module
	"""

	def __init__(self):
		super(Core, self).__init__('tommy_macos_url')

	def open_google(self):
		"""
		Open google on browser
		"""
		os.system('open https://www.google.com')
		return self.random_translation("open_google")

	def open_facebook(self):
		"""
		Open facebook on browser
		:return:
		"""
		os.system('open https://www.facebook.com')
		return self.random_translation("open_facebook")
