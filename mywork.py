import pyttsx3
import os
pyttsx3.speak("Welcome to the HelpDesk")

while True:
	print("Chat with me and I will help you to get your requirements:",end='')
	p=input()

	if(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("chrome" in p) or ("google chrome" in p)):
		os.system("chrome")
		pyttsx3.speak("Chrome is launched")


	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("mozilla" in p) or ("firefox" in p)):
		os.system("Firefox")
		pyttsx3.speak("Firefox is launched")


	elif(("run" in p) or ("music" in p)  or ("launch" in p) or ("open" in p)) and ("spotify" in p):
		os.system("spotify")
		pyttsx3.speak("Spotify is launched")


	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("notepad" in p) or ("text editor" in p) or ("writing pad" in p)):
		os.system("Notepad")
		pyttsx3.speak("Notepad is launched")


	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("command" in p) or ("cmd" in p)):
		os.system("Command Prompt")
		pyttsx3.speak("Command Prompt is launched")


	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("Word" in p) or ("Microsoft Word" in p)):
		os.system("Word")
		pyttsx3.speak("Word is launched")


	elif(("run" in p) or ("draw" in p) or ("launch" in p) or ("open" in p)) and ("paint" in p): 
		os.system("Paint")
		pyttsx3.speak("Pint is launched")


	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("join" in p)) and (("zoom" in p) or ("meeting" in p)):
		os.system("Zoom")
		pyttsx3.speak("Zoom is launched")


	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("join" in p) or ("connect" in p)) and ("Team Viewer" in p):
		os.system("Team Viewer")
		pyttsx3.speak("Team Viewer is launched")


	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("slack" in p) or ("channel" in p)):
		os.system("Slack")
		pyttsx3.speak("Slack is launched")


	elif("exit" in p) or ("quit" in p):
		break
		

	else:
		print("I donot have support for this ")
	