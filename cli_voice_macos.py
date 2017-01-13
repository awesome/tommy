import speech_recognition as sr
import os
from tommy.core.tommy import Tommy
from tommy.core.tprotocol import TRequest, EmptyTPackage

USER_AGENT = 'cli_voice_macos'


def speak(text):
	"""
	Speak tommy response using mac os say command
	"""
	os.system("say \"{}\"".format(text))


tommy = Tommy()

r = sr.Recognizer()

print('Tommy virtual assistant - v0.1-BETA 2017-01-12 - Alexandre Pécorilla Markiewicz')
print("Press enter and speak")
while True:
	try:
		input('>>>')
		with sr.Microphone() as source:
			audio = r.listen(source)
			text = r.recognize_google(audio)

		trequest = TRequest(text.lower(), USER_AGENT)
		tresponse = tommy.process(trequest)
		speak(tresponse.plain_text)
	except EmptyTPackage:
		pass
	except KeyboardInterrupt:
		speak('goodbye')
		break
