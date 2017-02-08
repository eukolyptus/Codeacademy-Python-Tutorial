dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#print ("dict[Name]: ", dict["Name"])
#print ("dict[Age]: ", dict["Age"])
#print ("dict[Class]: ", dict["Class"])

for item in dict:
	item_name = item
	#print (item_name)
	print ("dict[" + item_name + "]: %s" % dict[item])
