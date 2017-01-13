import os
import speech_recognition as sr
from tkinter import *
from tommy.core.tprotocol import TRequest, EmptyTPackage
from tommy.core.tommy import Tommy


def speak_macos(text):
	os.system("say \"{}\"".format(text))


class TommyInterface(Frame):
	def __init__(self, window):
		Frame.__init__(self, window, width=300, height=600)
		self.tommy = Tommy()
		self.pack(fill=BOTH)
		self.title = Label(self, text="Tommy", font=(None, 40), padx=20, pady=20).pack()
		self.r = sr.Recognizer()

		self.plain_text = StringVar()
		self.text_box = Entry(self, width=30, textvariable=self.plain_text)
		self.text_box.pack()
		self.text_box.bind('<Return>', lambda _: self.process_text())

		self.button_process = Button(text='Send', width=20, pady=30, command=self.process_text).pack()
		self.button_speak = Button(text="Speak", width=20, pady=30, command=self.listen).pack()

	def process_text(self):
		try:
			trequest = TRequest(self.plain_text.get().lower().strip())
			tresponse = self.tommy.process(trequest)
			with open('tmp.log', 'a') as logs:
				logs.write("TRequest sended : {}\n".format(trequest.__str__()))
				logs.write("TResponse receveid for {} : {}\n".format(trequest.id, tresponse.__str__()))
			speak_macos(tresponse.plain_text)
		except EmptyTPackage:
			pass
		self.text_box.delete(0, 'end')

	def listen(self):
		try:
			with sr.Microphone() as source:
				audio = self.r.listen(source)
				text = self.r.recognize_google(audio)

			trequest = TRequest(text.lower().strip())
			tresponse = self.tommy.process(trequest)
			with open('tmp.log', 'a') as logs:
				logs.write("TRequest sended : {}".format(trequest.__str__()))
				logs.write("TResponse receveid for {} : {}".format(trequest.id, tresponse.__str__()))
			speak_macos(tresponse.plain_text)
		except EmptyTPackage:
			pass
		except sr.UnknownValueError:
			self.text_box.delete(0, 'end')


window = Tk()
window.title("Tommy virtual assistant")
interface = TommyInterface(window)

interface.mainloop()
