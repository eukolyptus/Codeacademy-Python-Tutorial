"""
Function censor takes two strings, text and word, as input.
It should return the text with the word you chose replaced with
asterisks.
"""

def censor(text, word):
	text = text
	word = word
	wordLen = len(word)
	textLen = len(text)
	replace = ""
	result = ""

	for i in range(wordLen):
		replace = replace + "*"

	for i in range(textLen - wordLen):
		if text[i : i + wordLen] == word:
			text = text.replace(text[i : i + wordLen], replace)


	return text



print censor("this hack is wack hack", "hack")