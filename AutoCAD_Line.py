#install comtypes using
#python -m pip install comtypes

#Python imports
import os
import comtypes.client
from comtypes import comerror
from comtypes.client import CreateObject, GetActiveObject

def main():
	#open file
	try:
		#Get AutoCAD running instanct
		acad = GetActiveObject("AutoCAD.Application.20")
		state = true
	#Not running
	except(OSError, COMError):
		acad = GetActiveObject("AutoCAD.Application.20", dynamic = false)
		state = false

	#if opened, with one active drawing
	if state:
		doc = acad.Documents.Items(0)
	else
		filepath = "E:/Replace/With/Directory/myDWG.dwg"
		doc = acad.Documents.Open(filepath)

	#draw line, in this example, from (0,0) to (5,5)
	command_str = '._line 0,0 5,5 ' #the last space == ENTER
					#all commands end with space

	#send command to the drawing
	doc.SendCommand(command_str)

#Python exec
if __name__ == '__main__:
	main()
