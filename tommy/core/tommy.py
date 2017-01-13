"""
Tommy virtual assistant core module
"""
import importlib
from config.settings import LOAD_MODULES, MODULES_FOLDER

class Tommy:
	"""
	Tommy class
	Tommy virtual assistant is an instance of this class
	"""

	def __init__(self):
		"""
		Load modules indicated in settings.LOAD_MODULES list
		"""
		self.modules = {}
		for module in LOAD_MODULES:
			imported_module = importlib.import_module(MODULES_FOLDER + '.' + module)
			self.modules[module] = imported_module

		self.nb_modules = len(self.modules)

