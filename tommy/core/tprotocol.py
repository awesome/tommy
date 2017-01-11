"""
TProtocol
Tommy communication protocol
Allows to communicate with Tommy with precise rules and standards.
"""
import uuid
from datetime import datetime


class TRequest:
	"""
	Represents a query sent to Tommy.
	It's a text wrapper with more informations.
	Tommy only accepts TRequest
	"""

	def __init__(self, plain_text, user_agent):
		"""
		TRequest constructor
		Initializes the various information

		:param plain_text: Original text from the user
		:type plain_text: str
		:param user_agent: User agent used for send the request
		:type user_agent: str
		"""
		self.id = str(uuid.uuid4())  # TRequest identifier
		self.datetime_sending = str(datetime.now()).split('.')[0]
		self.user_agent = user_agent

		self.plain_text = plain_text

		if not self.plain_text:
			raise EmptyTRequest(self)

		self.plain_text.strip()
		self.splited_text = self.plain_text.split(' ')
		self.nb_words = len(self.splited_text)

	def __str__(self):
		"""
		TRequest to string
		"""
		str = "<TRequest #{}> at {} from {} : [{}]".format(self.id, self.datetime_sending, self.user_agent,
														   self.plain_text)
		return str


# Exceptions

class TProtocolError(Exception):
	"""
	Generic TProtocol error
	"""

	def __init__(self, error_msg):
		"""
		Initializes a TProtocol error with a message

		:param error_msg: The error message
		:type error_msg: str
		"""
		self.error_msg = error_msg


class TRequestError(TProtocolError):
	"""
	Generic TRequest error
	"""

	def __init__(self, error_msg, trequest):
		"""
		Initializes a TRequest error with a message and the TRequest concerned

		:param error_msg: The error message
		:param trequest: The TRequest concerned
		:type error_msg: str
		:type trequest: TRequest
		"""
		super(TRequestError, self).__init__(error_msg)
		self.trequest = trequest


class EmptyTRequest(TRequestError):
	"""
	Error for empty TRequest (no text in the request)
	"""

	def __init__(self, trequest):
		"""
		Initializes an EmptyTRequest error with the TRequest concerned

		:param trequest: The TRequest concerned
		:type trequest: TRequest
		"""
		error_msg = "This TRequest is empty"
		super(EmptyTRequest, self).__init__(error_msg, trequest)

	def __str__(self):
		"""
		EmptyTRequest to string
		"""
		return "{} : {}".format(self.error_msg, self.trequest)
