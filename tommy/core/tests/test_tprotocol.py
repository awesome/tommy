"""
Unit tests for TProtocol
"""
import unittest
from tommy.core.tprotocol import TPackage, TRequest, TResponse, EmptyTPackage


class TestTPackage(unittest.TestCase):
	"""
	Test for TPackage
	"""

	def setUp(self):
		"""
		Initialize a TPackage for the test
		"""
		self.tpackage = TPackage("I am a TPackage")

	def test_empty_plain_text(self):
		"""
		Test if an EmptyPackage exception is raised if plain_text is empty
		"""
		self.assertRaises(EmptyTPackage, TPackage, None)

	def test_blank_plain_text(self):
		"""
		Test if an EmptyPackage exception is raised if plain_text is blank
		"""
		self.assertRaises(EmptyTPackage, TPackage, '')

	def test_plain_text(self):
		"""
		Test if the text of the TPackage has not been altered
		"""
		self.assertEqual(self.tpackage.plain_text, "I am a TPackage")


class TestTRequest(unittest.TestCase):
	"""
	Tests for TRequest
	"""

	def setUp(self):
		"""
		Initializes a TRequest for the tests
		"""
		self.trequest = TRequest("I am a text", "test")

	def test_user_agent(self):
		"""
		Test if the text of the TRequest has not been altered
		"""
		self.assertEqual(self.trequest.user_agent, "test")

	def test_splited_text(self):
		"""
		Test the splited text list
		"""
		self.assertEqual(self.trequest.splited_text[0], "I")
		self.assertEqual(self.trequest.splited_text[1], "am")
		self.assertEqual(self.trequest.splited_text[2], "a")
		self.assertEqual(self.trequest.splited_text[3], "text")

	def test_nb_words(self):
		"""
		Test the number of words
		"""
		self.assertEqual(self.trequest.nb_words, 4)


class TestTResponse(unittest.TestCase):
	"""
	Tests for TResponse
	"""

	def setUp(self):
		"""
		Initializes a TResponse for the tests
		"""
		self.trequest = TRequest('Random request')
		self.tresponse = TResponse("I am a text", self.trequest)

	def test_tresponse_trequest_instance(self):
		"""
		Test if the TRequest of the TResponse has'nt been altered
		"""
		self.assertEqual(self.tresponse.trequest, self.trequest)
