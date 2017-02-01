"""
Tommy Hello module
Just for fun
"""
from tommy.core.module import Module
from tommy.core.tprotocol import TResponse
import requests

class Core(Module):
	"""
	Core of tommy_hello module
	"""

	def __init__(self):
		super(Core, self).__init__('tommy_time')

	def what_time_is_it_in(self, splited_text):
		city = ''
		for i in range(5, len(splited_text)):
			city += splited_text[i]

		response = requests.get('https://timezoneapi.io/api/address/?{}'.format(city))
		data = response.json()

		time = data['data']['addresses'][0]['datetime']['time']
		time_splited = time.split(':')[0:2]
		time = time_splited[0] + ':' + time_splited[1]

		return TResponse(self.random_translation("what_time_is_it_in").format(city, time))

