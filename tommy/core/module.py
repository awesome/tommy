"""
Module package
Standards for every tommy modules
"""
import json, random
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
		# load keywords
		with open(TOOMY_ROOT + '/modules/{}/keywords/keywords_{}.json'.format(module_name, LANG)) as keywords:
			self.keywords = json.load(keywords)

		# load translations
		with open(TOOMY_ROOT + '/modules/{}/translations/translations_{}.json'.format(module_name,
																					  LANG)) as translations:
			self.translations = translations

		self.module_name = module_name

	def random_translation(self, method_name):
		"""
		Return a random translation for a method
		:param method_name: name of the method
		:return:
		"""
		return random.choice(self.translations[method_name])
