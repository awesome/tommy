"""
Unit tests for TProtocol
"""
import unittest
from tommy.core.tprotocol import TRequest

class TestTRequest(unittest.TestCase):
	"""
	Tests for TRequest
	"""
	def setUp(self):
		"""
		Initializes a TRequest for the tests
		"""
		self.trequest = TRequest("I am a text", "test")

	def test_plain_text(self):
		"""
		Test if the text of the TRequest has not been altered
		"""
		self.assertEqual(self.trequest.plain_text, "I am a text")

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