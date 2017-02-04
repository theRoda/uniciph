#/usr/bin/env python
# -*- coding: utf-8 -*-

# supplement module to uniciph.py

import sys
import string
from collections import Counter


# http://letterfrequency.org/
english = 'etaoinsrhldcumfpgwybvkxjqz'
religious = 'etiaonsrhldcumfpywgbvkxjqz'
scientific = 'etaionsrhlcdumfpgybwvkxqjz'
fiction = 'etaohnisrdluwmcgfypvkbjxzq'
spanish = 'eaosrnidlctumpbgyívqóhfzjéáñxúüwk'
german = 'enisratdhulcgmobwfkzvüpäßjöyqx'
french = 'esaitnrulodcmpévqfbghjàxèyêzçôùâûîœwkïëüæñ'

def decodedFreq(decoded):
	# return string of letters from most frequent to least
	freqlist = []
	freq = Counter(decoded.lower())
	for f in range(0, len(freq)):
		high = max(freq, key=freq.get)
		freqlist += high
		del freq[high]
	exclude = set(string.punctuation)
	return ''.join(q for q in map(lambda s: s.strip(), freqlist) if q not in exclude)

def getLanguage(decodedfreq):
	# try to determine language by betting frequency health
	# currently just returns English frequency health
	freqHealth = 0
	for topletters in english[:6]:
		if topletters in decodedfreq[:6]:
			freqHealth += 1
	for bottomletters in english[-6:]:
		if bottomletters in decodedfreq[-6:]:
			freqHealth += 1
	return freqHealth
	

# some test strings
decoded = 'Security at the expense of usability comes at the expense of security.'
decodedf = '''La sécurité au détriment de la facilité d'utilisation se fait au détriment de la sécurité .'''

#print decodedFreq(decodedf)
#print getLanguage(decodedFreq(decodedf))
