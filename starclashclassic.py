# StarClash: RPSRPG

import random



def levelCheck(shipStats):
		shieldUpgradeIndex = {1:3,2:4,3:5}
		if shipStats.hPLevel < 5 and shipStats.hPUpgrade == shipStats.hPLevel:
			return True

		elif shipStats.hPUpgrade == 5:
			return True
	
		try:
			if shipStats.shieldUpgrade == shieldUpgradeIndex[shipStats.shieldLevel]:
				return True
		except KeyError:
			return False


		if shipStats.damageLevel < 5 and shipStats.damageUpgrade == shipStats.damageLevel:
			return True

		elif shipStats.damageUpgrade == 5:
			return True

		return False
				
				

class ShipStats:

	def __init__(self):
		self.hPUpgrade = 0
		self.shieldUpgrade = 0
		self.damageUpgrade = 0

		self.hPLevel = 1
		self.shieldLevel = 1
		self.damageLevel = 1
		
	def addHP(self):
		self.hPUpgrade += 1
		leveled = levelCheck(self)
		if leveled:
			self.hPLevel += 1
			self.hPUpgrade = 0
			return True
		return False
	def addShield(self):
		self.shieldUpgrade += 1
		leveled = levelCheck(self)
		if leveled:
			self.shieldLevel += 1
			self.shieldUpgrade = 0
			return True
		return False
	def addDamage(self):
		self.damageUpgrade += 1
		leveled = levelCheck(self)
		if leveled:
			self.damageLevel += 1
			self.damageUpgrade = 0
			return True
		return False

	def returnSkillPoints(self, isLevels = False):
		if isLevels:
			return [self.hPLevel, self.shieldLevel, self.damageLevel]
		else:
			return [self.hPUpgrade, self.shieldUpgrade, self.damageUpgrade]


class EnemyShip():

	def __init__(self, roundNumber):
		self.myStats = ShipStats()
		self.attackStatusNum = 0

		self.attackStatus = ""
		self.maxShieldCooldown = 6 - self.myStats.shieldLevel
		self.activeShieldCooldown = 0
		self.isCharged = False
		self.shieldAttempted = False
		
		skillPoints = round((random.random()+.25) * roundNumber)
		self.hitPoints = skillPoints


		while skillPoints > 0:
			if self.myStats.shieldLevel != 5:
				decideSkill = random.randint(1,5)
				if decideSkill == 1:
					self.myStats.addDamage()
				elif decideSkill == 2:
					if self.myStats.addShield():
						self.maxShieldCooldown = 6 - self.myStats.shieldLevel
				else:
					self.myStats.addHP()

			else:
				decideSkill = random.randint(1,4)
				if decideSkill == 1:
					self.myStats.addDamage()
				else:
					self.myStats.addHP()

			skillPoints -= 1


		self.hitPoints = self.myStats.hPLevel
		

class PlayerShip():

	def __init__(self):

		self.experiencePoints = 0
		self.xpToLevel = 10
		self.level = 1
		self.myStats = ShipStats()

		self.hitPointsMax = self.myStats.hPLevel * 5 + 5
		self.hitPoints = self.hitPointsMax

		self.attackStatus = ""
		self.maxShieldCooldown = 6 - self.myStats.shieldLevel
		self.activeShieldCooldown = 0
		self.isCharged = False
		self.shieldAttempted = False


class HighScore():

	def __init__(self, name, level, shipsDestroyed):

		self.name = name
		self.level = level
		self.shipsDestroyed = shipsDestroyed

def byKillsKey(highScore):
	return highScore.shipsDestroyed
		
def numConversion(baseNum):
	numDictionary = {0: "zero" , 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40 : "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
	finalString = ""

	if baseNum >= 100:
		largestNum = int(str(baseNum)[0])
		finalString += numDictionary[largestNum] + " hundred and "
		baseNum -= largestNum * 100

	if baseNum >= 10:
		largestNum = int(str(baseNum)[0]) * 10
		finalString += numDictionary[largestNum] + "-"
		baseNum -= largestNum

	if baseNum > 0:
		finalString += numDictionary[baseNum]


	return finalString

def levelNeeded(stats):
	levelList = ["|                          |","|                          |","|                          |","|                          |","|                          |"]
	shieldUpgradeIndex = {1:3,2:4,3:5}
	maxStat = False

	if stats.hPLevel < 5:
		for i in range(0,stats.hPLevel):
			levelIndex = list(levelList[i])
			levelIndex[5] = 'o'
			levelList[i] = "".join(levelIndex)
	else:
		for i in range(0,5):
			levelIndex = list(levelList[i])
			levelIndex[5] = 'o'
			levelList[i] = "".join(levelIndex)
			
	if stats.damageLevel < 5:
		for i in range(0, stats.damageLevel):
			levelIndex = list(levelList[i])
			levelIndex[14] = 'o'
			levelList[i] = "".join(levelIndex)
	else:
		for i in range(0, 5):
			levelIndex = list(levelList[i])
			levelIndex[14] = 'o'
			levelList[i] = "".join(levelIndex)
	try:
		for i in range(0,shieldUpgradeIndex[stats.shieldLevel]):
			levelIndex = list(levelList[i])
			levelIndex[23] = 'o'
			levelList[i] = "".join(levelIndex)
	except KeyError:
			maxStat = True
	
	for i in range(0, stats.hPUpgrade):
		levelIndex = list(levelList[i])
		levelIndex[5] = '*'
		levelList[i] = "".join(levelIndex)
		
	for i in range(0, stats.damageUpgrade):
		levelIndex = list(levelList[i])
		levelIndex[14] = '*'
		levelList[i] = "".join(levelIndex)

	if(maxStat):
		for i in range(0,5):
			levelIndex = list(levelList[i])
			levelIndex[23] = '*'
			levelList[i] = "".join(levelIndex)
	else:
		for i in range(0, stats.shieldUpgrade):
			levelIndex = list(levelList[i])
			levelIndex[23] = '*'
			levelList[i] = "".join(levelIndex)

	return levelList

def requestName(score):
	print("You earned a spot on the high score list!")							
	while True:
		newName = input("Enter a three character name to add to the list. ")
		newName = newName.upper()
		if len(newName) < 3:
			print("Not a valid name.")
			continue
		newName = newName[0:3]
		break

	score.name = newName

	return score

def main():

	shipListDefault = ["","\--","   \----", "         }", "   /---- ","/--"]
	shipList = shipListDefault
	roundNumber = 1
	levelList = []


	enemyShip = EnemyShip(roundNumber)
	playerShip = PlayerShip()

	print("An enemy ship has appeared from hyperspace! Engage weaponds.")
	print(" ")
	print("Type the corresponding key displayed in the menu to attack, charge, or shield.")
	print("If you attack at the same time the enemy does, you will both be hurt.")
	print("If you charge and are not hit, you will get a special power attack to guarantee a triple hit next turn.")
	print("Watch out! If your enemy gains a charge, you will not know until they fire.")
	print("If you shield and they attack, you will gain an absorption power boost, allowing you to fire a charged attack next turn.")
	print("Be careful! Your shield has a multi-turn cooldown and until it recharges,you will not be able to shield again, even if you didn't block anything with your shot.")

	while True:

		print("_____________________")
		for i in range(len(shipList)):
			print("      " + shipList[i])
		print("_____________________")
		print(" ")
		print("~~~~~~~~~~~~~~~~~~~~~")
		if playerShip.hitPoints >= 100:
			print("| Your Health: " + str(playerShip.hitPoints)  + "  |")
		elif playerShip.hitPoints >= 10:
			print("| Your Health: " + str(playerShip.hitPoints)  + "   |")
		else:
			print("| Your Health: " + str(playerShip.hitPoints)  + "    |")
		if enemyShip.hitPoints >= 100:
			print("| Enemy Health: " + str(enemyShip.hitPoints)  + " |")
		elif enemyShip.hitPoints >= 10:
			print("| Enemy Health: " + str(enemyShip.hitPoints) + "  |")
		else:
			print("| Enemy Health: " + str(enemyShip.hitPoints) + "   |")
		print("|                   |")
		print("| A = Attack        |")
		print("| C = Charge        |")
		print("| S = Shield        |")
		print("~~~~~~~~~~~~~~~~~~~~~")

		if playerShip.isCharged == True:
			print("You have a charge available, fire it if you wish, or shield instead.")
			print("")

		if playerShip.activeShieldCooldown > 0:
			print("Your shield has cool down of " + numConversion(playerShip.activeShieldCooldown) + " turns. You must wait to use it again or nothing will happen.")
			print("")
		
		while True:
			try:
				playerShip.attackStatus = input("Type the corresponding key displayed in the menu to attack, charge, or shield. ")
				if(playerShip.attackStatus == "a"):
					playerShip.attackStatus = "A"
				elif(playerShip.attackStatus == "c"):
					playerShip.attackStatus = "C"
				elif(playerShip.attackStatus == "s"):
					playerShip.attackStatus = "S"
				elif playerShip.attackStatus == "A" or playerShip.attackStatus == "S" or playerShip.attackStatus == "C":
					playerShip.attackStatus = playerShip.attackStatus
				elif playerShip.attackStatus == "ome":
					playerShip.hitPoints = 0
				else:
					raise RuntimeError
			except RuntimeError:
				print("Not a valid option.")
				print('')
				continue
			break
		
		
		print("")

		
		if enemyShip.activeShieldCooldown == 0:
			if enemyShip.isCharged:
				enemyShip.attackStatusNum = random.randint(1,4)
				if(enemyShip.attackStatusNum == 1 or enemyShip.attackStatusNum == 2 or enemyShip.attackStatusNum == 3):
					enemyShip.attackStatus = "A"
				elif(enemyShip.attackStatusNum == 4):
					enemyShip.attackStatus = "S"
			else:
				enemyShip.attackStatusNum = random.randint(1,3)
				if(enemyShip.attackStatusNum == 1):
					enemyShip.attackStatus = "A"
				elif(enemyShip.attackStatusNum == 2):
					enemyShip.attackStatus = "C"
				elif(enemyShip.attackStatusNum == 3):
					enemyShip.attackStatus = "S"
		else:
			if enemyShip.isCharged:
				enemyShip.attackStatus = "A"
			else:
				enemyShip.attackStatusNum = random.randint(1,2)
				if(enemyShip.attackStatusNum == 1):
					enemyShip.attackStatus = "A"
				elif(enemyShip.attackStatusNum == 2):
					enemyShip.attackStatus = "C"

		print(" ")
		print(" ")


		if playerShip.attackStatus == "A" and enemyShip.attackStatus == "A":
			if (playerShip.isCharged):
				dealtDamage = playerShip.myStats.damageLevel * 3
				enemyShip.hitPoints -= dealtDamage
				playerShip.isCharged = False
				print("You fire a charged volley, and deals " + numConversion(dealtDamage) + " damage.")
			else:
				dealtDamage = playerShip.myStats.damageLevel
				enemyShip.hitPoints -= dealtDamage
				print("You fire a volley, and deal " + numConversion(dealtDamage) + " damage")
			if (enemyShip.isCharged):
				dealtDamage = enemyShip.myStats.damageLevel * 3
				playerShip.hitPoints -= dealtDamage
				enemyShip.isCharged = False
				print("The enemy fires a charged volley, and deals " + numConversion(dealtDamage) +" damage.")
			else:
				dealtDamage = enemyShip.myStats.damageLevel
				print("The emeny fires a volley, and deals " + numConversion(dealtDamage) + " damage.")
				playerShip.hitPoints -= dealtDamage
	
		elif playerShip.attackStatus == "C" and enemyShip.attackStatus == "A":
			if (enemyShip.isCharged):
				dealtDamage = enemyShip.myStats.damageLevel * 4
				print("While charging a powerful volley, the enemy fires a charged volley, dealing " + numConversion(dealtDamage) + " damage.")
				playerShip.hitPoints -= dealtDamage
				enemyShip.isCharged = False
			else:
				dealtDamage = enemyShip.myStats.damageLevel * 2
				print("While charging a powerful volley, the enemy fires, dealing " + numConversion(dealtDamage) + " damage.")
				playerShip.hitPoints -= dealtDamage
		elif playerShip.attackStatus == "S" and enemyShip.attackStatus == "A":
			
			if playerShip.activeShieldCooldown == 0:
				if enemyShip.isCharged:
					print("You block a powerful volley, the shot overcharges your absorption device and you gain no charge.")
					enemyShip.isCharged = False
				else:
					print("You block a powerful volley, and gain a charge to use next turn.")
					playerShip.isCharged = True

			else:
				print("You can't shield, you still have a cooldown of " + str(playerShip.activeShieldCooldown))
				
			playerShip.activeShieldCooldown = playerShip.maxShieldCooldown
			playerShip.shieldAttempted = True

		elif playerShip.attackStatus == "A" and enemyShip.attackStatus == "C":
			if playerShip.isCharged:
				dealtDamage = playerShip.myStats.damageLevel * 4
				print("You fire a charged volley while the enemy was charging, dealing" + numConversion(dealtDamage) + "damage.")
				enemyShip.hitPoints -= dealtDamage
				playerShip.isCharged = False
			else:
				dealtDamage = playerShip.myStats.damageLevel * 3
				print("You fire a volley while the enemy charges, dealing "+ numConversion(dealtDamage) +" damage.")
				enemyShip.hitPoints -= dealtDamage
		elif playerShip.attackStatus == "A" and enemyShip.attackStatus == "S":
			if playerShip.isCharged:
				print("The enemy shielded your powerful volley.")
				playerShip.isCharged = False
				enemyShip.isCharged = False
			else:
				print("The enemy shielded your volley.")
				enemyShip.isCharged = True
			enemyShip.activeShieldCooldown = enemyShip.maxShieldCooldown
			enemyShip.shieldAttempted = True

		elif playerShip.attackStatus == "C" and enemyShip.attackStatus == "C":
			print("You charge a powerful volley.")
			playerShip.isCharged = True
			enemyShip.isCharged = True

		elif playerShip.attackStatus == "C" and enemyShip.attackStatus == "S":
			print("You charge a powerful volley.")
			playerShip.isCharged = True
			enemyShip.activeShieldCooldown = enemyShip.maxShieldCooldown
			enemyShip.shieldAttempted = True

		elif playerShip.attackStatus == "S" and enemyShip.attackStatus == "C":
			if playerShip.activeShieldCooldown == 0:
				print("You shield for an upcomming attack, but none are fired.")
				playerShip.activeShieldCooldown = playerShip.maxShieldCooldown
			else:
				print("You can't shield, you still have a cooldown of " + str(playerShip.activeShieldCooldown))
			playerShip.isCharged = False
			enemyShip.isCharged = True
		elif playerShip.attackStatus == "S" and enemyShip.attackStatus == "S":
			if playerShip.activeShieldCooldown == 0:
				print("You shield for an upcomming attack, but none are fired.")
				playerShip.activeShieldCooldown = playerShip.maxShieldCooldown
			else:
				print("You can't shield, you still have a cooldown of " + str(playerShip.activeShieldCooldown))
			playerShip.isCharged = False
			enemyShip.isCharged = False
			enemyShip.activeShieldCooldown = enemyShip.myStats.damageLevel
		else:
			print("Your indecisiveness provides the perfect oportunity for your enemy to hit you with a powerful blast!")
			playerShip.hitPoints -= enemyShip.myStats.damageLevel * 2
		
		if not playerShip.shieldAttempted:
			if playerShip.activeShieldCooldown != 0:
				playerShip.activeShieldCooldown -= 1
		else:
			playerShip.shieldAttempted = False
		if not enemyShip.shieldAttempted:
			if enemyShip.activeShieldCooldown != 0:
				enemyShip.activeShieldCooldown -= 1
		else:
			enemyShip.shieldAttempted = False
		

		print(" ")
		print(" ")

		if playerShip.hitPoints <= 0:
			break

		if enemyShip.hitPoints <= 0:
			print("With that shot, the enemy's ship is destroyed!")
			playerShip.experiencePoints += roundNumber
			print("You gained " + str(roundNumber) + " experience points!")

			while playerShip.experiencePoints >= playerShip.xpToLevel:
				playerShip.level += 1
				playerShip.experiencePoints -= playerShip.xpToLevel
				playerShip.hitPoints = playerShip.hitPointsMax
				playerShip.activeShieldCooldown = 0
				playerShip.xpToLevel += (playerShip.level * 3)
				print("You leveled up to Level " + str(playerShip.level) + '!')
				print('')
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print("|    H        D        S   |")
				for i in levelNeeded(playerShip.myStats):
					print(i)
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				leveled = False
				upgradeChoice = ''
				while True:
					try:
						upgradeChoice = input("Select a component of your ship to upgrade using the menu, select H for health, D for damage, and S for shields! ")
						if upgradeChoice == 'H' or upgradeChoice =='h':
							leveled = playerShip.myStats.addHP()
							if leveled:
								print("Congratulations! You leveled up your ship's health, providing you with an additional five hit points!")
								playerShip.hitPointsMax = playerShip.myStats.hPLevel * 5 + 5
						elif upgradeChoice == 'D' or upgradeChoice == 'd':
							leveled = playerShip.myStats.addDamage()
							if leveled:
								print("Congratulations! You leveled up your ship's weapons, providing you with an additional point of damage!")
						elif (upgradeChoice == 'S' or upgradeChoice =='s' ) and playerShip.myStats.shieldLevel != 4:
							leveled = playerShip.myStats.addShield()
							playerShip.maxShieldCooldown = 6 - playerShip.myStats.shieldLevel
							if leveled:
								print("Congratulations! You leveled up your ship's shield generators, decreasing their usage cooldown by one!")
						elif upgradeChoice == 'S' or upgradeChoice == 's':
							print("That component has already reached its maximum level!")
							raise RuntimeError
						else:
							raise RuntimeError
					except RuntimeError:
						print("Enter a valid component type to continue.")
						print('')
						continue
					break
				playerShip.hitPoints = playerShip.hitPointsMax

			print('')
			print("You now have a total of " + str(playerShip.experiencePoints) + " XP, with " + str(playerShip.xpToLevel) + " XP needed for your next level")
			roundNumber += 1
			print("")
			print("")
			print("Just as you think the battle is over, another ship appears from hyperspace.")
			enemyShip = EnemyShip(roundNumber)

	if enemyShip.hitPoints <= 0:
		print("As both ships fire, the damage sustained from the fight proves too demanding and both ships split apart.")
		roundNumber += 1
		print("After " + str(roundNumber) + " ships destroyed, you are destroyed.")
	else:
		print("After " + str((roundNumber - 1 )) + " ships destroyed, with that volley, you are killed.")

	print("You were Level " + str(playerShip.level) + " when you were defeated.")
	print('')

	while True:
		try:
			newScore = HighScore("",playerShip.level,roundNumber-1)
			f = open("highscores.txt")


			highScoreList = []
			while True:
				try:
					readScoreRaw = f.readline()
					readScore = readScoreRaw.split()
					highScoreList.append(HighScore(readScore[0], int(readScore[1]), int(readScore[2])))
				except IndexError:
					break
			highScoreList = sorted(highScoreList, key= byKillsKey)
			highScoreList = list(reversed(highScoreList))


			for i in highScoreList:
				if newScore.shipsDestroyed >= i.shipsDestroyed and len(highScoreList) > 1:
					newScore = requestName(newScore)
					highScoreList.append(newScore)
					highScoreList = sorted(highScoreList, key= byKillsKey)
					highScoreList = list(reversed(highScoreList))

					if len(highScoreList) > 10:
						highScoreList.pop()
					break
				if newScore.shipsDestroyed >= i.shipsDestroyed:
					newScore = requestName(newScore)
					if len(highScoreList) > 10:
						highScoreList.pop()
					highScoreList.append(newScore)
					break


			f.close()

			f = open("highscores.txt", 'w')

			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("|        High Score        |")
			print("| Name     Level     Kills |")
			for i in highScoreList:
				printedRecord = "| " + i.name + "      " + str(i.level)
				printedRecord += (10 - len(str(i.level)))*' '
				printedRecord += str(i.shipsDestroyed)
				printedRecord += (6- len(str(i.shipsDestroyed)))*' ' + '|'
				print(printedRecord)
				f.write(str(i.name) + ' ' + str(i.level) + ' ' + str(i.shipsDestroyed) + '\n')
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

			f.close()		
			break

		except OSError:
			try:
				f = open("highscores.txt", 'w')

				for i in range(10):
					f.write("PLR 1 1\n")

				f.close()
				continue
			except OSError:
				print("Failed to open or create highscore database. Check admin privilages at script location.")
				break


main()