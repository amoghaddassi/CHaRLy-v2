from psychopy import visual, event
import time

def drawBlankTask(win, tutorial = False):
	"""Draws a blank template for a trial. This includes drawing
	the machine, both stars, and the key history box."""
	if tutorial:
		machine = visual.ImageStim(
			win = win,
			image = "./assets/tutorial/machine.png")
		machine.size = [machine.size[0] * .7, machine.size[0] * .7]
	else:
		machine = visual.ImageStim(
			win = win,
			image = "./assets/machine.jpg")
	machine.draw()

	if not tutorial:
		window_cover = visual.Rect(
			win = win,
			fillColor = [1, 1, 1],
			pos = [-35, -40],
			width = 135,
			height = 65)
		window_cover.draw()
	key_hist = visual.Rect(
		win = win,
		width = 250,
		height = 75,
		pos = [0, -250],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	key_hist.draw()

	key_divide = visual.Line(
		win = win,
		start = [0, -287.5],
		end = [0, -212.5],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	key_divide.draw()

def blankScreen(win):
	"""Wipes the screen inbetween trials."""
	win.flip()

def setGoalStar(win, star):
	if (star == 1): #highlights correct star
		highlightStar(win, "./assets/black-star.png")
	elif (star == 2):
		highlightStar(win, "./assets/orange-star.png")
	elif (star == 3):
		highlightStar(win, "./assets/blue-star.png")
	elif (star == 4):
		highlightStar(win, "./assets/gray-star.png")
	elif (star == 5):
		highlightStar(win, "./assets/brown-star.png")
	elif (star == 6):
		highlightStar(win, "./assets/cream-star.png")

def setGoalCoin(win):
	highlightStar(win, "./assets/tutorial/coin.png")

def drawGear(win, itemsOnScreen):
	"""Draws the gear stimulus."""
	if itemsOnScreen == 0:
		x = -60
	else:
		x = 0
	gear = visual.ImageStim(
		win = win,
		image = "./assets/gear.jpg",
		pos = [x, -40])
	gear.size = [gear.size[0] * .7, gear.size[1] * .7]
	gear.draw()

def drawLight(win, itemsOnScreen):
	"""Draws the light stimulus."""
	if itemsOnScreen == 0:
		x = -60
	else:
		x = 0
	light = visual.ImageStim(
		win = win,
		image = "./assets/light.jpg",
		pos = [x, -40])
	light.size = [light.size[0] * .7, light.size[1] * .7]
	light.draw()

def drawPower(win, itemsOnScreen):
	"""Draws the power stimulus."""
	if itemsOnScreen == 0:
		x = -60
	else:
		x = 0
	power = visual.ImageStim(
		win = win,
		image = "./assets/power.jpg",
		pos = [x, -40])
	power.size = [power.size[0] * .07, power.size[1] * .07]
	power.draw()

def drawFan(win, itemsOnScreen):
	"""Draws the fan stimulus."""
	if itemsOnScreen == 0:
		x = -60
	else:
		x = 0
	fan = visual.ImageStim(
		win = win,
		image = "./assets/fan.jpg",
		pos = [x, -40])
	fan.size = [fan.size[0] * .1, fan.size[1] * .1]
	fan.draw()

def drawHammer(win):
	hammer = visual.ImageStim(
			win = win,
			image = "./assets/tutorial/hammer.png",
			pos = [-60, 30])
	hammer.draw()

def drawChisel(win):
	chisel = visual.ImageStim(
			win = win,
			image = "./assets/tutorial/chisel.png",
			pos = [60, 30])
	chisel.draw()

def highlightStar(win, img):
	star = visual.ImageStim(
		win = win,
		image = img,
		pos = [0, 300])
	star.draw()
	highlightBox = visual.Rect(
		win = win,
		width = 110,
		height = 110,
		pos = [0, 300],
		lineColor = [-1, -1, -1],
		lineWidth = 5)
	highlightBox.draw()
	return highlightBox

def unlockStar(win, img):
	star = visual.ImageStim(
		win = win,
		image = img,
		pos = [-100, -150])
	star.draw()

def unlockCoin(win, img):
	"""Same logic as unlockStar, but for the tutorial machine."""
	star = visual.ImageStim(
		win = win,
		image = img,
		pos = [100, -150])
	star.draw()
 
def highlightAndUnlock(win, img):
	highlightBox = highlightStar(win, img)
	highlightBox.fillColor = [0, 1, 0]
	highlightBox.opacity = .3
	highlightBox.draw()

def pointCounter(win, points):
	"""Draws a point counter for the given number of 
	points."""
	scoreText = visual.TextStim(
		win = win,
		text = "Points: " + str(points),
		pos = [0, 200],
		color = [-1, -1, -1],
		bold = True)
	scoreText.draw()

def showKeys(win, keys):
	"""Will display all entries of keys (list of chars) in the 
	key stroke box. Assumes first entry of keys was first key 
	pressed in the trial."""
	keys = keys.copy()
	if (keys and type(keys[0]) == int):
		#need to convert to letters
		keyMap = {1: "d", 2: "f", 3: "j", 4: "k", -1: "NA"}
		for i in range(len(keys)):
			keys[i] = keyMap[keys[i]]
	keyStims = []
	for i in range(len(keys)):
		#create the text
		if keys[i] != "NA":
			keyText = visual.ImageStim(
				win = win,
				image = "./assets/" + keys[i] + ".png",
				pos = [-95 + i*60, -250])
			keyText.size = [keyText.size[0] * .25, keyText.size[1] * .25]
		else:
			keyText = visual.TextStim(
			win = win,
			text = keys[i].upper(),
			pos = [-95 + i*60, -250],
			color = [-1, -1, -1])
		#add key to the list
		keyStims.append(keyText)

	for keyText in keyStims:
		keyText.draw()

def showKeysTutorial(win, keys):
	"""Will display all entries of keys (list of chars) in the 
	key stroke box. Assumes first entry of keys was first key 
	pressed in the trial."""
	keys = keys.copy()
	if (keys and type(keys[0]) == int):
		#need to convert to letters
		keyMap = {1: "d", 2: "f", 3: "j", 4: "k"}
		for i in range(len(keys)):
			keys[i] = keyMap[keys[i]]
	keyStims = []
	for i in range(len(keys)):
		#create the text
		if keys[i] != "NA":
			keyText = visual.ImageStim(
				win = win,
				image = "./assets/tutorial/" + keys[i] + ".png",
				pos = [-95 + i*60, -250])
			keyText.size = [keyText.size[0] * .25, keyText.size[1] * .25]
		else:
			keyText = visual.TextStim(
			win = win,
			text = keys[i].upper(),
			pos = [-95 + i*60, -250],
			color = [-1, -1, -1])
		#add key to the list
		keyStims.append(keyText)

	for keyText in keyStims:
		keyText.draw()

def getKeys():
	keyMap = {"d": 1, "f": 2, "j": 3, "k": 4}
	keys = event.waitKeys(keyList = ["d", "f", "j", "k", "1"])
	#if (len(keys) > 1):
		#raise Exception("Don't press more than 1 key at a time!")
	if (keys[0] in keyMap):
		return keyMap[keys[0]]
	elif (keys[0] == "1"):
		exit("Exit key pressed")
	return -1

def getKeysTutorial():
	keyMap = {"u": 1, "i": 2, "o": 3, "p": 4}
	keys = event.waitKeys(keyList = ["u", "i", "o", "p"])
	return keyMap[keys[0]]

def breakScreen(win):
	breakText = visual.TextStim(
		win = win,
		text = "Enjoy a break from the task! \n \n The goal star will now change color. \n \n Press any key when you're ready to start.",
		pos = [0, 20],
		color = [-1, -1, -1],
		height = 45)
	breakText.draw()
	win.flip()
	time.sleep(.5)
	event.waitKeys()

def spaceToContinue(win):
	text = "[Press space to continue]"
	textStim = visual.TextStim(
		win = win,
		text = text,
		pos = [0, -350],
		color = [-1, -1, -1],
		height = 25)
	textStim.draw()
