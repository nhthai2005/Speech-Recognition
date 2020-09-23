import speech_recognition
import pyttsx3
from datetime import date, datetime

#Robot nghe
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""


# Test get audio
#with speech_recognition.WavFile("output.wav") as source:              # use "test.wav" as the audio source
#    robot_ear.adjust_for_ambient_noise(source)         # listen for 1 second to calibrate the energy threshold for ambient noise levels
#   audio = robot_ear.record(source)
# End test audio
while True:
	with speech_recognition.Microphone() as mic:
		print ("Robot: I'm Listening")
		robot_ear.adjust_for_ambient_noise(mic)         # listen for 1 second to calibrate the energy threshold for ambient noise levels
		audio = robot_ear.listen(mic)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print ("You: " + you)
	# Robot suy nghi
	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello Thai. How are you? What are you doing?"
	elif "today" in you:
		today = date.today()
		robot_brain=today.strftime("%B %d, %Y")
		#print(robot_brain)
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds ")
		#print(robot_brain)
		# Textual month, day and year	
	elif "robot" in you:
		robot_brain = "Hello Thai. Why do you say me Robot? I'm not Robot! I'm your friend."
	elif "bye" in you:
		robot_brain = "Good bye Thai"
		robot_mouth.say(robot_brain)
		print ("Robot: " + robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "I don't know what you say"
	print ("Robot: " + robot_brain)


	# Robot tra loi

	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
