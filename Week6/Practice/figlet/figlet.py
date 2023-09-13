from pyfiglet import Figlet
from cs50 import get_string
import sys
from random import randrange as rand

figlet = Figlet()
fontList = figlet.getFonts()
randFont = rand(len(fontList))

if len(sys.argv) == 1:
    s = get_string("Input: ")
    figlet.setFont(font = figlet.getFonts()[randFont])
    print (figlet.renderText(s))
    sys.exit(0)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--f"] and sys.argv[2] in fontList:
    s = get_string("Input: ")
    figlet.setFont(font = sys.argv[2])
    print (figlet.renderText(s))
    sys.exit(0)

else:
    print("Invalid usage")
    sys.exit(1)