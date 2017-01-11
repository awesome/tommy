"""
TProtocol
Tommy communication protocol
Allows to communicate with Tommy with precise rules and standards.
"""
import uuid
from datetime import datetime


class TPackage:
	"""
	Superclass for TRequest and TResponse
	"""

	def __init__(self, plain_text):
		"""
		Initialize a TPackage with an id, a datetime and a plain text
		"""
		self.id = str(uuid.uuid4())
		self.datetime_created = str(datetime.now()).split('.')[0]
		self.plain_text = plain_text

		if not self.plain_text:
			raise EmptyTPackage(self)

		self.plain_text = self.plain_text.strip()

	def __str__(self):
		"""
		TPackage to string
		"""
		return "[<{} #{}> at {} : ({})]".format(self.__class__.__name__, self.id, self.datetime_created,
											  self.plain_text)


class TRequest(TPackage):
	"""
	Represents a query sent to Tommy.
	It's a text wrapper with more informations.
	Tommy only accepts TRequest
	"""

	def __init__(self, plain_text, user_agent=None):
		"""
		TRequest constructor
		Initializes the various information

		:param plain_text: Original text from the user
		:type plain_text: str
		:param user_agent: User agent used for send the request
		:type user_agent: str
		"""
		super(TRequest, self).__init__(plain_text)
		self.user_agent = user_agent
		self.splited_text = self.plain_text.split(' ')
		self.nb_words = len(self.splited_text)


class TResponse(TPackage):
	"""
	Represent a response sent by Tommy
	It's a text wrapper with more informations.
	Tommy only sends TResponse
	"""

	def __init__(self, plain_text, trequest):
		"""
		TResponse constructor
		Initializes the various information

		:param response_text: The response's text
		:param trequest: The TRequest causing the TResponse
		:type: str
		"""
		super(TResponse, self).__init__(plain_text)
		self.trequest = trequest

		if not self.trequest:
			raise TResponseWithoutRequest(self)


# Exceptions

class TProtocolError(Exception):
	"""
	Generic TProtocol error
	"""

	def __init__(self, error_msg, tpackage):
		"""
		Initializes a TProtocol error with a message

		:param error_msg: The error message
		:param tpackage: The tpackage concerned
		:type error_msg: str
		:type tpackage: TPackage
		"""
		self.error_msg = error_msg
		self.tpackage = tpackage
		self.datetime_raised = str(datetime.now()).split('.')[0]


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
		super(TRequestError, self).__init__(error_msg, trequest)


class TResponseError(TProtocolError):
	"""
	Generic TResponse error
	"""

	def __init__(self, error_msg, tresponse):
		"""
		Initializes a TResponse error with a message and the TResponse concerned

		:param error_msg: The error message
		:param tresponse: The TResponse concerned
		:type error_msg: str
		:type tresponse: TResponse
		"""
		super(TResponseError, self).__init__(error_msg, tresponse)


class EmptyTPackage(TProtocolError):
	"""
	Error for empty TPackage (no palin_text in the package)
	"""

	def __init__(self, tpackage):
		"""
		Initializes an EmptyTPackage error with the TPackage concerned

		:param tpackage: The TPackage concerned
		:type tpackage: TPackage
		"""
		error_msg = "This TPackage is empty"
		super(EmptyTPackage, self).__init__(error_msg, tpackage)

	def __str__(self):
		"""
		EmptyTPackage to string
		"""
		return "{} : {}".format(self.error_msg, self.tpackage)


class TResponseWithoutRequest(TResponseError):
	"""
	Raised when a TResponse doesn't have a TRequest
	"""

	def __init__(self, tresponse):
		"""
		Initialize a TResponseWithoutRequest error with the TResponse concerned

		:param tresponse: The TResponse concerned
		:type tresponse: TResponse
		"""
		error_msg = "This TResponse doesn't have a TRequest"
		super(TResponseWithoutRequest, self).__init__(error_msg, tresponse)

	def __str__(self):
		"""
		TResponseWithoutRequest to string
		"""
		return "{} : {}".format(self.error_msg, self.tpackage)
