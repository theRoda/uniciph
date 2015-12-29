# uniciph
Universal Cipher Bruteforce Tool
#### warning: project still in alpha.. goofy stuff lies yonder
Credit to http://inventwithpython.com/hacking for the inspiration and currently a bulk of the code in the support modules.
<br><br>
*usage: python2 uniciph.py < cipherfile >*
<br><br>
* working:
  * base64
  * reverse
  * atbash
  * caesar (mostly)
  * hex (mostly)
* fixing: 
  * baconian
  * affine
  * transposition
  * caesar edge cases
  * hex case '0x'
2. next: 
  * XOR
  * railfence
  * bifid
  * columnar transposition
  * double transposition
  * playfair
  * Übchi
  * vigenere
  * keyed vigenere
  * Friedman IC
  * import ciphertext from multi-line file
  * frequency analysis
  * Cohen's kappa test
  * Chi test
  * take key(s) as argument
  * take key(s) file as argument
  * parallelize
<br><br>
note: When using newDetectEnglish(), the default is to require 60% words and 75% letters to return a match. I am still trying to find the best ratio for each. These values can be tweaked in the isEnglish() function, or when calling isEnglish() eg. `isEnglish(cleartext, 50, 80)` would require 50% words and 80% letters.
