import random

hp = 100
inventory = []
moblin = "alive"
lynel = "alive"
ganon = "alive"

def main():
	print("Let's go on an adventure.........\n")
	start()

def map():
	#print using \t to make evenly print
	# 6 room options that you can either go right or left or up or down
	print("\n\nEntrance\tGuard's Chamber\t\tDining Hall")
	print()
	print("Library\t\tZelda's Study\t\tSanctum(Ganon)\n")

def inv():
	#print all elements on the same line for cleanness 
	for elem in inventory:
		print("'" + elem+ "'", end=" ")
	print()

def start():
	global hp
	#print map so you can see your options
	map()
	print("\n\nYou are standing in a dark room in the entrance to Ganon's castle.\n")
	print("You must battle your way to defeat him and save Princess Zelda")
	print("You have zero weapons or armor and must fight to survive")
	print("In each room you travel to, there will be hidden objects that you must 'search' the room for")
	print("There will also be enemies you run into that you must battle")
	print("Health points:", hp)
	#while loop so they can do multiple things in the room
	answer = "search"
	while answer == "search" or answer == "move" or answer == "inventory":
		answer = input("\nWhat would you like to do? 'search', 'move', or 'inventory' ")
		if answer == "inventory":
			#show items
			inv()
		elif answer == "search":
			#search the room but if already found the item, cannot get again
			if "Master Sword" not in inventory and "Helmet" not in inventory:
				print("You have found the Master Sword and a basic helmet so you won't perish immediately")
				hp += 5
				print("Health points:", hp)
				inventory.append("Master Sword")
				inventory.append("Helmet")
			else:
				print("You found nothing")
		elif answer == "move":
			where = input("\nOkay, where would you like to go? 'Guard's Chamber' or 'Library' ")
			if where.lower() == "guard's chamber" or where.lower() == "guards chamber":
				#guard room
				guard()
				# set answer to empty so when the stack unfolds, the loops stop
				answer = ""
			elif where.lower() == "library":
				#library
				library()
				answer = ""
			else:
				answer = ""
				end_game("You didn't type something properly!\nGame over!!!\nRestart")
		else:
			answer = ""
			end_game("You didn't type something properly!\nGame over!!!\nRestart")


def guard():
	global hp, moblin
	#print map so you can see your options
	map()
	print("\n\nYou have entered a chamber where the guards would prepare themselves for battle by adorning themselves with gear.")
	print("Maybe there's something you can take!")
	print("But wait, there's a big Moblin all the way across the room. Maybe you can take something before having to fight.")

	answer = "search"
	while answer == "search" or answer == "fight" or answer == "inventory" or answer == "move":
		#give option to move or fight depending if moblin is dead
		if moblin == "alive":
			answer = input("\nWhat do you do? 'search', 'fight', 'inventory' ")
		elif moblin == "dead":
			answer = input("\nWhat do you do? 'search', 'move', 'inventory' ")
		if answer == "inventory":
			#show items
			inv()
		elif answer == "search":
			#search the room but if already found the item, cannot get again
			if "Chest Plate" not in inventory:
				print("\nYou have found a chest plate for more protection")
				inventory.append("Chest Plate")
				hp += 10
				print("Health points:", hp)
			if moblin == "dead":
				print("\nWoah! The moblin dropped a heart piece!")
				print("Your health increases by 20")
				hp += 20
				print("Health points:", hp)
		elif answer == "fight":
			if moblin == "alive": #only fight if it is alive
				moblinhp = 40
				print("\nHealth points:", hp)
				print("Moblin health points:", moblinhp)
				print("Moblin sees you charging and prepares to attack")
				if "Master Sword" in inventory: #only fight if you have the sword
					while moblinhp > 0: #loop while he's still alive
						print("\nMoblin makes a hit!! Blood is drawn :(")
						hp -= random.randint(1,5) #random damage to me
						print("Health points:", hp)
						print("\nYou slash the master sword and strike the moblin")
						moblinhp -= random.randint(10,30) #random damage to enemy
						print("Moblin health points:", moblinhp)
						if moblinhp > 0:
							h = input("\nHit 'enter' for another strike")
						else: # we are done
							print("Moblin defeated!!! Amazing work! Maybe he left you something?")
							moblin = "dead"
				else:
					end_game("You are not prepared for this fight and you perish upon first Moblin strike.")
					
			else:
				print("\nEnemy is dead, you don't need to fight")
		elif answer == "move":
			where = input("\nWhere would you like to go? 'Dining Hall', 'Entrance', 'Zelda's Study' ")
			if where.lower() == "zelda's study" or where.lower() == "zeldas study":
				#zelda
				zelda()
				answer = ""
			elif where.lower() == "entrance":
				#entrance
				start()
				answer = ""
			elif where.lower() == "dining hall":
				#dining hall
				dining()
				answer = ""
			else:
				answer = ""
				end_game("You didn't type something properly!\nGame over!!!\nRestart")
			
		else:
			answer = ""
			end_game("You didn't type something properly!\nGame over!!!\nRestart")

def library():
	global hp
	#print map so you can see your options
	map()
	print("\nYou have entered a room with floor to ceiling books with table's to sit and rest")
	print("\nThere isn't an enemy in sight. Phew...")
	print("\nHealth points:", hp)
	#while loop so they can do multiple things in the room
	answer = "search"
	while answer == "search" or answer == "move" or answer == "inventory":
		answer = input("\nWhat would you like to do? 'search', 'move', or 'inventory' ")
		if answer == "inventory":
			#show items
			inv()
		elif answer == "search":
			#search the room but if already found the item, cannot get again
			if "Iron Pants" not in inventory and "Light Arrows" not in inventory:
				print("\nYou have found Light Arrows and Iron Pants!")
				print("These light arrows may prove useful against Ganon!")
				hp += 10
				print("Health points:", hp)
				inventory.append("Light Arrows")
				inventory.append("Iron Pants")
			else:
				print("You found nothing")
		elif answer == "move":
			where = input("\nOkay, where would you like to go? 'Zelda's Study' or 'Entrance' ")
			if where.lower() == "zelda's study" or where.lower() == "zeldas study":
				#zelda's study
				zelda()
				answer = ""
			elif where.lower() == "entrance":
				#entrance
				start()
				answer = ""
			else:
				answer = ""
				end_game("You didn't type something properly!\nGame over!!!\nRestart")
		else:
			answer = ""
			end_game("You didn't type something properly!\nGame over!!!\nRestart")


def dining():
	global hp
	#print map so you can see your options
	map()
	print("\nYou have the dining room. This is where Zelda and her family would eat with guests before Ganon took control of the castle.")
	print("It has become dusty and devoid of food.")
	print("\nThere isn't an enemy in sight. Phew...")
	print("\nHealth points:", hp)
	#while loop so they can do multiple things in the room
	answer = "search"
	while answer == "search" or answer == "move" or answer == "inventory":
		answer = input("\nWhat would you like to do? 'search', 'move', or 'inventory' ")
		if answer == "inventory":
			#show items
			inv()
		elif answer == "search":
			#search the room but if already found the item, cannot get again
			if "Gauntlets" not in inventory:
				print("\nYou have found Gauntlets!")
				hp += 10
				print("Health points:", hp)
				inventory.append("Gauntlets")
			else:
				print("You found nothing")
		elif answer == "move":
			where = input("\nOkay, where would you like to go? 'Guard's Chamber' or 'Sanctum' (only enter the chamber with Ganon if you are sure you will succeed) ")
			if where.lower() == "guard's chamber" or where.lower() == "guards chamber":
				#guard's room
				guard()
				answer = ""
			elif where.lower() == "sanctum":
				#ganon
				sanctum()
				answer = ""
			else:
				answer = ""
				end_game("You didn't type something properly!\nGame over!!!\nRestart")
		else:
			answer = ""
			end_game("You didn't type something properly!\nGame over!!!\nRestart")

def zelda():
	global hp, lynel
	#print map so you can see your options
	map()
	print("\n\nYou have entered Zelda's room, including her chambers and her personal items.")
	print("Maybe there's something you can take!")
	print("But wait, there's a big Lynel all the way across the room. Maybe you can take something before having to fight. Be careful, Lynels are strong and scary enemies")

	answer = "search"
	while answer == "search" or answer == "fight" or answer == "inventory" or answer == "move":
		#give option to move or fight depending if lynel is dead
		if lynel == "alive":
			answer = input("\nWhat do you do? 'search', 'fight', 'inventory' ")
		elif lynel == "dead":
			answer = input("\nWhat do you do? 'search', 'move', 'inventory' ")
		if answer == "inventory":
			#show items
			inv()
		elif answer == "search":
			#search the room but if already found the item, cannot get again
			if "Mirror Shield" not in inventory:
				print("\nYou have found a Mirror Shield!\nWoah and it gave restored some health :)")
				hp += 5
				print("Health points:", hp)
				inventory.append("Mirror Shield")
			if lynel == "dead":
				print("\nWoah! The lynel dropped a heart piece!")
				print("Your health increases by 20")
				hp += 20
				print("Health points:", hp)
		elif answer == "fight":
			if lynel == "alive": #only fight if it is alive
				lynelhp = 70
				print("\nHealth points:", hp)
				print("Lynel health points:", lynelhp)
				print("Lynel sees you charging and prepares to attack")
				if "Master Sword" in inventory and "Mirror Shield" in inventory: #only fight if you have the sword and shield
					while lynelhp > 0: #loop while he's still alive
						print("\nLynel charges and knocks you onto your back!!")
						hp -= random.randint(5,10) #random damage to me
						print("Health points:", hp)
						print("\nYou parry another hit to knock back the Lynel and  slash the master sword to strike")
						lynelhp -= random.randint(10,30) #random damage to enemy
						print("Lynel health points:", lynelhp)
						if lynelhp > 0:
							h = input("\nHit 'enter' for another strike")
						else: # we are done
							print("Lynel defeated!!! Amazing work! Maybe he left you something?")
							lynel = "dead"
				else:
					answer = ""
					end_game("You are not prepared for this fight and you perish upon first Lynel strike.")
					
			else:
				print("\nEnemy is dead, you don't need to fight")
		elif answer == "move":
			where = input("\nWhere would you like to go? 'Library', 'Guard's Chamber', 'Sanctum' (only enter the chamber with Ganon if you are sure you will succeed) ")
			if where.lower() == "guard's chamber" or where.lower() == "guards chamber":
				#guard's room
				guard()
				answer = ""
			elif where.lower() == "library":
				#library
				library()
				answer = ""
			elif where.lower() == "sanctum":
				#ganon
				sanctum()
				answer = ""
			else:
				answer = ""
				end_game("You didn't type something properly!\nGame over!!!\nRestart")
			
		else:
			answer = ""
			end_game("You didn't type something properly!\nGame over!!!\nRestart")


def sanctum():
	global hp, ganon
	#print map so you can see your options
	map()
	print("\n\nYou have entered the Sanctum. Your bones shiver at the thought of having to defeat ganon")
	print("Maybe there's something you can take...?")

	answer = "search"
	while answer == "search" or answer == "fight" or answer == "inventory":
		if ganon == "alive":
			answer = input("\nWhat do you do? 'search', 'fight', 'inventory' ")
		elif ganon == "dead":
			answer = input("\nWhat do you do? 'search', 'inventory' ")
		if answer == "inventory":
			#show items
			inv()
		elif answer == "search":
			#only get if ganon is dead
			if ganon == "dead":
				print("\nWoah! The ganon left a heart container!")
				print("Your health is restored")
				hp = 100
				print("Health points:", hp)
				answer = ""
				play_again()
			if ganon == "alive":
				print("\nYou found nothing")
		elif answer == "fight":
			if ganon == "alive": #only fight if it is alive
				ganonhp = 100
				print("\nHealth points:", hp)
				print("Ganon health points:", ganonhp)
				print("Ganon comes down from the ceiling of the sanctum and is primed for action")
				if "Master Sword" in inventory and "Mirror Shield" in inventory and "Light Arrows" in inventory: #only fight if you have the sword, shield, and arrows
					while ganonhp > 0: #loop while he's still alive
						print("\nGanon charges and blasts you backwards!!")
						hp -= random.randint(10,20) #random damage to me
						print("Health points:", hp)
						print("\nYou parry another hit, shoot ganon with a light arrow, and slash the master sword until ganon reacts")
						ganonhp -= random.randint(10,20) #random damage to enemy
						print("Ganon health points:", ganonhp)
						if ganonhp > 0:
							h = input("\nHit 'enter' for another strike")
						else: # we are done
							print("Ganon defeated!!! I'm utterly shocked. But you survived! Maybe he left you something?")
							ganon = "dead"
				else:
					answer = ""
					end_game("You are not prepared for this fight and you perish upon first Lynel strike.")
					
			else:
				print("\nGanon is dead, you don't need to fight")
		
		else:
			answer = ""
			end_game("You didn't type something properly!\nGame over!!!\nRestart")



def end_game(message):
	print(message)
	play_again()


def play_again():
	global hp
	inventory.clear()
	answer = input("Do you want to play again? y or n ")
	if answer == "y":
			hp = 100
			start()
	else:
			print("Good playing with you :)")


main()
