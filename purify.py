def purify(list):
	result = list

	for item in list:
		#print item
		if item % 2 != 0:
			print item
			result.remove(item)

	print "final: ", result
	return result



print purify([4,5,5,4])


"""
meow = [1,2,3,3,3]
meow.remove(3)
meow.remove(3)
print meow
"""

