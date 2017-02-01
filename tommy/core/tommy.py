"""
Tommy virtual assistant core module
"""
import importlib
from config.settings import LOAD_MODULES, MODULES_FOLDER
from tommy.core.tprotocol import TResponse


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
			imported_module = importlib.import_module(MODULES_FOLDER + '.' + module + '.core')
			self.modules[module] = imported_module.Core()

		self.nb_modules = len(self.modules)

	def process(self, trequest):
		"""
		Find the correct module and method to call from a trequest
		:param trequest: TRequest sended by user
		:type trequest: TRequest
		"""
		splited_text = trequest.splited_text

		possible_methods = {}

		for module in LOAD_MODULES:
			possible_methods[module] = {}

		# iterate on each words
		for word in splited_text:
			# iterate on modules
			for module_name, module_instance in self.modules.items():
				# iterate on each methods
				for method_name, method_definition in module_instance.keywords.items():
					# iterate on calls
					id = 0  # unique identifier for same methods but different calls
					# iterate on each calls
					for call in method_definition['calls']:
						keywords = call['keywords']
						method_name_with_id = method_name + '-{}'.format(id)
						if method_name_with_id not in possible_methods[module_name]:
							if word == keywords[0]:
								possible_methods[module_name][method_name_with_id] = {
									'method': method_name,
									'nb_keywords': 1,
									'keywords_required': len(keywords),
									'word_cursor': 1
								}
						else:
							possible_method = possible_methods[module_name][method_name_with_id]
							if possible_method['word_cursor'] < possible_method['keywords_required']:
								if word == keywords[possible_method['word_cursor']] or keywords[
									possible_method['word_cursor']] == '%s':
									possible_method['nb_keywords'] += 1
									possible_method['word_cursor'] += 1
						id += 1

		# call the correct method in all possible methods
		for module_name, methods in possible_methods.items():
			for method_name, frequency in methods.items():
				if frequency['nb_keywords'] == frequency['keywords_required']:
					method_to_call = frequency['method'].split('-')[0]  # remove id
					used_module = self.modules[module_name]
					tresponse = getattr(used_module, method_to_call)(splited_text)
					tresponse.trequest = trequest
					return tresponse

		return TResponse("Sorry I don't understand", trequest)
