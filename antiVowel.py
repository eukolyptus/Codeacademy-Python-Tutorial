def anti_vowel(text):
	antiText = "";

	for i in range(len(text)):
		if (text[i] == "a" or text[i] == "A" or\
			text[i] == "e" or text[i] == "E" or\
			text[i] == "i" or text[i] == "I" or\
			text[i] == "o" or text[i] == "O" or\
			text[i] == "u" or text[i] == "U"):
			pass
		else:
			antiText = antiText + text[i]

	return antiText

def anti_vowel2(text):
	antiText = "";

	for i in range(len(text)):
		if text[i] in "aeiou" or text[i] in "AEIOU":
			pass
		else:
			antiText = antiText + text[i]

	return antiText

print "========================================"
print "TYPE 1"
print "Variation 1: ", anti_vowel("hello")
print "Variation 2: ", anti_vowel("HeLlO")
print "Variation 3: ", anti_vowel("hElLo")
print "Variation 4: ", anti_vowel("HELLO")

print "========================================"
print "TYPE 2"
print "Variation 1: ", anti_vowel2("hello")
print "Variation 2: ", anti_vowel2("HeLlO")
print "Variation 3: ", anti_vowel2("hElLo")
print "Variation 4: ", anti_vowel2("HELLO")