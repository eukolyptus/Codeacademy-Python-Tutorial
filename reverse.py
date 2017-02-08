"""
Function reverse returns a reversed text
"""

def reverse(text):
	strLen = len(text)
	reversed = ""

	for i in range(strLen):
		reversed = text[i] + reversed

	return reversed


print reverse("hello")