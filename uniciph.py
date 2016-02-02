#!/bin/python
# UniCiph - Universal Cipher Cracking Tool
# theRoda - begin 9/15 

#####
#
# currently tests for: hex, base64, reverse, atbash, caesar, transposition, affine, bacon
#
#####

import re
import sys
import math
import string
import base64
import binascii
import newDetectEnglish
import cryptomath
import affineCipher

herpderp = """
**************************************************
***** UniCiph Universal Cipher Cracking Tool *****
**************************************************
"""

def checkMatch(message, key, cipher):
	message = message.strip()
	if newDetectEnglish.isEnglish(message):
		print(herpderp)
		print('[!] {0} : {1} : Key:{2}'.format(message, cipher, key))
		sys.exit()
	else:
		pass

def testBase64(ciphertext):
	try:
		decoded = base64.decodestring(ciphertext)
		checkMatch(decoded, None, 'Base64')
	except binascii.Error:
		print('Testing Base64: Not Base64')

def testReverse(self):
	decoded = ''
	i = len(self) - 1
	while i >= 0:
		decoded = decoded + self[i]
		i -= 1
	print(decoded + ' : Reverse')
	checkMatch(decoded, None, 'Reverse')
	
def decodeCaesar(key, character):
	if not character.isalpha():
		return(character)
	position = ord(character)
	if position + key < 90:
		position += key
	else:
		position -= key
	return(chr(position))
	
def testCaesar(ciphertext):
	for testkey in range(0,25):
		decoded = ''.join(decodeCaesar(testkey, c) for c in ciphertext.upper())
		print('{0} : Rot{1} Caesar'.format(decoded, testkey))
 		checkMatch(decoded, testkey, 'Caesar')
	
def testTrans(self):
	key = 1
	self = self.strip()
	while key < len(self) / 2:
		numCols = math.ceil(len(self) / float(key))
		numRows = key
		numShaded = (numCols * numRows) - len(self)
		plaintext = [''] * int(numCols)
		col = 0
		row = 0
		for symbol in self:
			plaintext[col] += symbol
			col += 1
			if (col == numCols) or (col == numCols -1 and row >= numRows - numShaded):
				col = 0
				row += 1
		decoded = ''.join(plaintext)
		print(decoded + ' : Transposition : Key{0}').format(key)
		key += 1
		checkMatch(decoded, key, 'Transposition')
		
def testAffine(self):
	for key in range(len(affineCipher.SYMBOLS) ** 2):
		keyA = affineCipher.getKeyParts(key)[0]
		if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
			continue

		decryptedText = affineCipher.decryptMessage(key, self)
		print('Tried Key %s : (%s)' % (key, decryptedText[:40]))
		checkMatch(decryptedText, key, 'Affine')
		
def testAtbash(self):
	AtoM = 'ABCDEFGHIJKLM'
	ZtoN = 'ZYXWVUTSRQPON'
	decoded = ''
	for c in self.upper():
		if c.isalpha():
			if c in AtoM:
				num = AtoM.find(c)
				decoded += ZtoN[num]
			else:
				num = ZtoN.find(c)
				decoded += AtoM[num]
		else:
			decoded += c
	checkMatch(decoded, None, 'Atbash')

def testBacon(self):
	bdict = {}
	decoded = ''
	self = self.lower()
	self = re.sub('[\W\d]', '', self.strip())
	for i in range(0,26):
		tmp = bin(i)[2:].zfill(5)
		tmp = tmp.replace('0', 'a')
		tmp = tmp.replace('1', 'b')
		bdict[tmp] = chr(65+i)
	for i in range(0, len(self)/5):
		decoded = decoded + bdict.get(self[i*5:i*5+5], ' ')
	checkMatch(decoded, None, 'Baconarian') # need to fix decoded. no spaces
	
def testHex(ciphertext):
	cleancipher = cleanHex(ciphertext)
	if all(h in string.hexdigits for h in cleancipher):
		checkMatch(cleancipher.decode('hex'), None, 'Hexadecimal')
	else:
		print('Testing Hex: Ciphertext is not hex.')
		pass

def cleanHex(ciphertext):
	return(ciphertext.replace(' ', '').replace('0x', '').replace(':', '').replace('\\x', '').strip())

def main():
	try:
		with open(sys.argv[1], 'r') as ciphertext:
			ctext = ciphertext.read()
			ctext = ctext.strip()
	except:
		print('Invalid argument supplied')
		sys.exit()
	testHex(ctext)
	testReverse(ctext)
	testBase64(ctext)
	testAtbash(ctext)
	#testBacon(ctext) bacon is breaking
	testCaesar(ctext)
	testTrans(ctext)
	testAffine(ctext)
	print(herpderp)
	print('No matches found.')

if __name__ == '__main__':
	main()
