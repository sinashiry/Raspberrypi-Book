from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.check_var_1 = BooleanVar()
		self.check_var_2 = BooleanVar()
		self.check_var_3 = BooleanVar()
		check_1 = Checkbutton(frame, text='Pin 17',
		command=self.update_1,
		variable=self.check_var_1, onvalue=True, offvalue=False)
		check_2 = Checkbutton(frame, text='Pin 27',
		command=self.update_2,
		variable=self.check_var_2, onvalue=True, offvalue=False)
		check_3 = Checkbutton(frame, text='Pin 22',
		command=self.update_3,
		variable=self.check_var_3, onvalue=True, offvalue=False)
		check_1.grid(row=1)
		check_2.grid(row=2)
		check_3.grid(row=3)
	def update_1(self):
		GPIO.output(17, self.check_var_1.get())
	def update_2(self):
		GPIO.output(27, self.check_var_2.get())
	def update_3(self):
		GPIO.output(22, self.check_var_3.get())

root = Tk()
root.wm_title('On / Off Switchs')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
