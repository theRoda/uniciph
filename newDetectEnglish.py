#!/bin/python
# -*- coding: utf-8 -*-
# newDetectEnglish module
# v0.0.1
# module heavily borrowed from http://inventwithpython.com/hacking (BSD Licensed)

import os

CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \t\n'

def loadDictionary():
	englishWords = []
	try:
		with open('dictionary.txt', 'r') as dictionaryFile:
			for word in dictionaryFile.read().split('\n'):
				englishWords.append(word.strip())
		return englishWords
	except:
		print '[!] dictionary.txt failed to open properly.'

	
ENGLISH_WORDS = loadDictionary()

def removeNonLetters(self):
	lettersOnly = []
	for symbol in self:
		if symbol in CHARSET:
			lettersOnly.append(symbol)
	return ''.join(lettersOnly)

def getEnglishCount(self):
	self = self.upper()
	self = removeNonLetters(self)
	possibleWords = self.split()
	if possibleWords == []:
		return 0.0
	matches = 0
	for word in possibleWords:
		if word in ENGLISH_WORDS:
			matches += 1
	return float(matches) / len(possibleWords)
	
def isEnglish(self, wordPercentage=60, letterPercentage=75):
	wordsMatch = getEnglishCount(self) * 100 >= wordPercentage
	numLetters = len(removeNonLetters(self))
	messageLettersPercentage = float(numLetters) / len(self) * 100
	lettersMatch = messageLettersPercentage >= letterPercentage
	return wordsMatch and lettersMatch
	
