"""
Tommy Date
Standard module for date and time
"""
import calendar
from datetime import datetime
from tommy.core.module import Module

class Core(Module):
	"""
	Core of tommy_date module
	"""
	def __init__(self):
		super(Core, self).__init__('tommy_date')

	def current_date(self):
		"""
		Return the current date
		"""
		day = datetime.now().strftime("%d")
		month = calendar.month_name[int(datetime.now().strftime("%m"))]
		year = datetime.now().strftime("%Y")

		cur_date = day + ' ' + month + ' ' + year

		return self.random_translation("current_date").format(cur_date)

