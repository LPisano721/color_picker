"""
Program: colorpicker.py
Author: Luigi Pisano 10/14/20
example from page 287-288

Simple python GUI based program that showcases the color chooser widget
"""

from breezypythongui import EasyFrame
import tkinter.colorchooser


class ColorPicker(EasyFrame):
	"""Displays the result of picking a color."""

	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Color Chooser Demo")

		# Labels and output fields
		self.addLabel(text= "R", row = 0, column = 0)
		self.addLabel(text= "G", row = 1, column = 0)
		self.addLabel(text= "B", row = 2, column = 0)
		self.addLabel(text= "Color", row = 3, column = 0)

		self.r = self.addIntegerField(value = 0, row = 0, column = 1)
		self.g = self.addIntegerField(value = 0, row = 1, column = 1)
		self.b = self.addIntegerField(value = 0, row = 2, column = 1)
		self.hex = self.addTextField(text = "#000000", row = 3, column = 1)

	 	# Canvas widget with an initial black color background
		self.canvas = self.addCanvas(row = 0, column = 2, rowspan = 4, width = 50, background = "#000000")

		# Command button
		self.addButton(text = "Pick a Color", row = 4, column = 0, columnspan = 3, command = self.chooseColor)

	# Event handling method
	def chooseColor(self):
		"""Pops up a color chooser from the OS and outputs the results."""
		colorTuple = tkinter.colorchooser.askcolor()
		if not colorTuple[0]:
			return
		((r, g, b), hexString) = colorTuple
		self.r.setNumber(int(r))
		self.g.setNumber(int(g))
		self.b.setNumber(int(b))
		self.hex.setText(hexString)
		self.canvas["background"] = hexString

def main():
	"""Instantiates and pops up the window>"""
	ColorPicker().mainloop()

#Global call to the main function
main()
