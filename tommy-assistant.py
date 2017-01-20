import os
import speech_recognition as sr
from tkinter import *
from tommy.core.tprotocol import TRequest, EmptyTPackage
from tommy.core.tommy import Tommy
from config.settings import TOMMY_ROOT, BACKGROUND_COLOR
from PIL import ImageTk, Image


def speak_macos(text):
	os.system("say \"{}\"".format(text))


class TommyInterface(Frame):
	def __init__(self, window):
		Frame.__init__(self, window, width=200, height=300)
		self.configure(background=BACKGROUND_COLOR)
		self.pack(fill=BOTH, expand=True)  # Tommy interface filled the window (need expand)

		self.tommy = Tommy()
		self.recognizer = sr.Recognizer()

		# Title
		self.title = Label(self, text="Tommy", font=('Monaco', 30), pady=10)
		self.title.configure(foreground="white", background=BACKGROUND_COLOR)
		self.title.pack()

		# Text box
		self.plain_text = StringVar()
		self.text_box = Entry(self, textvariable=self.plain_text)
		self.text_box.configure(background="#D3DFDD")
		self.text_box.config(highlightbackground=BACKGROUND_COLOR)  # change padding color
		self.text_box.bind('<Return>', lambda _: self.process(self.plain_text.get()))  # Bind to enter button
		self.text_box.pack()

		# Button speak
		self.microphone_icon = ImageTk.PhotoImage(file=TOMMY_ROOT + '/medias/images/tommy/microphone.gif')
		self.button_speak = Button(self, text="Speak", width=20, height=40, pady=50, command=self.listen)
		self.button_speak.config(highlightbackground=BACKGROUND_COLOR,
								 image=self.microphone_icon)  # change padding color
		self.button_speak.pack(pady=10)

	def process(self, plain_text):
		if hasattr(self, "label_question") and hasattr(self, "label_response"):
			self.label_question.destroy()
			self.label_response.destroy()
		try:
			trequest = TRequest(plain_text.lower().strip())
			self.label_question = Label(self, text=plain_text, wraplength=150, background=BACKGROUND_COLOR,
										font=("Times", 15, "bold"), pady=10)
			self.label_question.pack()

			tresponse = self.tommy.process(trequest)
			self.label_response = Label(self, text=tresponse.plain_text, wraplength=150, background=BACKGROUND_COLOR)
			self.label_response.pack()

			speak_macos(tresponse.plain_text)
		except EmptyTPackage:
			pass
		self.text_box.delete(0, 'end')

	def listen(self):
		try:
			with sr.Microphone() as source:
				audio = self.recognizer.listen(source)
				plain_text = self.recognizer.recognize_google(audio)
				self.process(plain_text)
		except sr.UnknownValueError:
			pass


window = Tk()
window.title("Tommy")
window.attributes('-topmost', True)  # The window is always visible in the foreground
window.geometry("200x300")
window.resizable(0, 0)
window.attributes("-alpha", 0.95)  # transparency

interface = TommyInterface(window)
interface.pack()
interface.mainloop()
