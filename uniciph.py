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
import base64
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
		print('[!]'+message+' : '+cipher+' : Key:'+str(key))
		sys.exit()
	else:
		pass
		
def testBase64(self):
	try:
		decoded = base64.b64decode(self)
	except:
		decoded = 'aaaaaa' # hacky fix for checkMatch reference before assignment when try fails. needs work
	checkMatch(decoded, None, 'Base64')
		
def testReverse(self):
	decoded = ''
	i = len(self) - 1
	while i >= 0:
		decoded = decoded + self[i]
		i -= 1
	print(decoded + ' : Reverse')
	checkMatch(decoded, None, 'Reverse')	
	
def testCaesar(ciphertext):
	for testkey in range(0,25):
		decoded = ''
		for c in ciphertext.upper():
			if not c.isalpha():
				decoded += c
				continue
			c = ord(c)
			decoded += chr(c + testkey if (c + testkey) < 90 else c - testkey)
		print('{0} : Rot{1} Caesar').format(decoded, str(testkey))
		checkMatch(decoded, testkey, 'Ceasar')
	
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
	
def testHex(self):
	if re.search('(x|\\\\x)[0-9a-fA-F]{2}|\\b[0-9a-fA-F]+\\b', self): # x00 \x00 00 
		self = self.replace('\\x', '')
		self = self.replace('x', '')
	elif re.search('(0x)[0-9a-fA-F]{2}|\\b[0-9a-fA-F]+\\b', self):
		self = self.replace('0x', '') # 0x00 still needs work
	else:
		pass
	print self
	try:
		guess = self.decode('hex')
	except:
		guess = 'aaaa' # hacky fix like in testB64
	checkMatch(guess, None, 'Hexadecimal')
	
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
