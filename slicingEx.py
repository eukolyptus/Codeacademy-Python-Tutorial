"""
word = "Python"

print("++++++++++++++++++++++++++++++++++++++++++")
print ("Word: \t\t\t", word)
print ("Word length is: \t", len(word))
print (word[0:2])
print (word[2:6])

print("++++++++++++++++++++++++++++++++++++++++++")
x = 15
for i in range(2,x-1,1):
	print(i)
"""

x = 4
for i in range(2, x-1, 1):
	if (x % i) == 0:
		print (i)
		print ("True")

