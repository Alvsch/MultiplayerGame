import game
mode = input("Join/Create: ")
if mode.lower() == "join":
	import client
elif mode.lower() == "create":
	import server
else:
	print("Not a valid choice")