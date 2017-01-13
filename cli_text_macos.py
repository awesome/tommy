# SPEAK WITH TOMMY FROM COMMAND LINE
# WORKS ONLY ON MAC OS
from tommy.core.tommy import Tommy
from tommy.core.tprotocol import TRequest, EmptyTPackage
import os

USER_AGENT = 'cli_text_macos'
tommy = Tommy()

def speak(text):
	"""
	Speak method, say text using mac os 'say' command
	:param text: the text to say
	"""
	os.system("say \"{}\"".format(text))


print('Tommy virtual assistant - v0.1-BETA 2017-01-12 - Alexandre Pécorilla Markiewicz')

while True:
	try:
		text = input('>>>')
		trequest = TRequest(text, USER_AGENT)
		tresponse = tommy.process(trequest)
		speak(tresponse.plain_text)
	except EmptyTPackage:
		pass
	except KeyboardInterrupt:
		speak('goodbye')
		break
