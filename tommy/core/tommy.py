"""
Tommy virtual assistant core module
"""
import importlib, hashlib, json
from config.settings import LOAD_MODULES, MODULES_FOLDER, TOMMY_ROOT, LANG
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
		self.tree = Root()
		# module
		keywords_json = {}
		for module in LOAD_MODULES:
			with open(TOMMY_ROOT + 'modules/{}/keywords/keywords_{}.json'.format(module, LANG)) as keywords_file:
				keywords_json = json.load(keywords_file)

		for method, content in keywords_json.items():
			for call in content['calls']:
				current_node = self.tree
				for keyword in call['keywords']:
					if current_node.has_child(keyword):
						current_node = current_node.get_child(keyword)
					else:
						current_node.add_child(Node(keyword))
						current_node = current_node.get_child(keyword)
				current_node.module = module
				current_node.method = method

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
								if word == keywords[possible_method['word_cursor']]:
									possible_method['nb_keywords'] += 1
									possible_method['word_cursor'] += 1
						id += 1

		# call the correct method in all possible methods
		for module_name, methods in possible_methods.items():
			for method_name, frequency in methods.items():
				if frequency['nb_keywords'] == frequency['keywords_required']:
					method_to_call = frequency['method'].split('-')[0]  # remove id
					used_module = self.modules[module_name]
					response_text = getattr(used_module, method_to_call)()
					return TResponse(response_text, trequest)

		return TResponse("Sorry I don't understand", trequest)


class Node:
	"""
	A node of the Tommy keywords tree
	"""

	def __init__(self, word, *childs, is_variable=False, module=None, method=None):
		"""
		Create a node, set the word associated and the child nodes
		:param word: The word represented by the node
		:param childs: Child nodes (list of another nodes)
		"""
		self.word = word
		if word:
			self.fingerprint = hashlib.sha1(str.encode(self.word)).hexdigest()
		self.childs = list(childs)
		self.is_variable = is_variable

		self.module = module
		self.method = method

	def has_childs(self):
		"True if current node has childs"
		return len(self.childs) > 0

	def has_child(self, word):
		"""True if the node has a child associated with word"""
		for child in self.childs:
			if child.word == word: return True
		return False

	def get_child(self, word):
		"""Get a node's child using a word"""
		for child in self.childs:
			if child.word == word: return child
		return None

	def add_child(self, child):
		"""Add a child to the current node"""
		self.childs.append(child)

	def is_callable(self):
		"""True if a method is callable from this node"""
		return self.module and self.method

	def __str__(self):
		return '<{}>'.format(self.word)


class Root(Node):
	"""Root of the tommy's tree"""

	def __init__(self, *childs):
		"""Instancie a root node without word associated"""
		super(Root, self).__init__(None, *childs)
