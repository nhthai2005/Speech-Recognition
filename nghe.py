import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print ("Robot: I'm Listening")
	robot_ear.adjust_for_ambient_noise(mic)         # listen for 1 second to calibrate the energy threshold for ambient noise levels
	audio = robot_ear.listen(mic)
try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""
print ("You: " + you)