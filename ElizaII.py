"""
asking = True
while asking:
	answer = input("How are you? Please type how you feel or 'Q' to quit: ")
	
	if str.lower(answer) == "good" or str.lower(answer) == "q":
		asking = False
	else:
		print(answer.replace("I","You"))
		print("That's not what I'm asking for...please answer \"good or somthing else\"")
print("Thank you")
"""
asking = True
rplist = {"i":"you","me":"you","my":"your","am":"are"}
newAnswer = ""
while asking:
	answer = input("How are you? Please type how you feel or 'Q' to quit: ")
	
	if str.lower(answer) == "good" or str.lower(answer) == "q":
		asking = False
	else:
		answerlist = answer.split()
		for item in answerlist:
			#if i== rplist.keys():
			#if item in rplist:
			#    answer.replace(item, rplist[item])
			if item == "i":
				item = "you"
			if item == "me":
				item = "you"
			if item == "my":
				item = "your"
			if item == "am":
				item = "are"
			# end of if statement
			newAnswer = newAnswer + item + " "
		print(newAnswer)
			
		print("That's not what I'm asking for...please answer \"good or somthing else\"")
print("Thank you")