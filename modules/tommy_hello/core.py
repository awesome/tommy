"""
Tommy Hello module
Just for fun
"""
from config.settings import USER_INFOS
from tommy.core.module import Module


class Core(Module):
	"""
	Core of tommy_hello module
	"""

	def __init__(self):
		super(Core, self).__init__('tommy_hello')

	def hello(self):
		return self.random_translation("hello").format(USER_INFOS['username'])

	def how_are_you(self):
		return self.random_translation("how_are_you")

	def who_are_you(self):
		return self.random_translation("who_are_you")

