#from art import *
#tprint('GREAT\nWEEKEND\nAHEAD')
import pyfiglet
import random

font=random.choice(pyfiglet.FigletFont.getFonts())
ascii_art=pyfiglet.figlet_format('GREAT WEEKEND AHEAD!',font=font)
hello_message=f"{ascii_art}\nGREAT WEEKEND AHEAD!{ascii_art}"
print(hello_message)
