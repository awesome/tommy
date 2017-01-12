"""
Module package
Standards for every tommy modules
"""
import re
from config.settings import TOOMY_ROOT, LANG


class Module:
	"""
	Superclass for all the modules
	"""

	def __init__(self, module_name):
		"""
		Initialize a new module, load keywords and translations
		:param module_name:
		"""
		self.keywords = TOOMY_ROOT + '/modules/{}/keywords/keywords_{}.json'.format(module_name, LANG)
		self.translations = TOOMY_ROOT + '/modules/{}/translations/translations_{}.json'.format(module_name, LANG)
		self.module_name = module_name