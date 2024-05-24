# uniciph
Universal Cipher Bruteforce and Analysis Tool

Credit to http://inventwithpython.com/hacking for the english detection ideas.
<br><br>
*usage: python uniciph.py*
<br><br>
* Current features:
  * Brute force
    * Base64
    * Reverse
    * Atbash
    * Caesar
    * Hex
    * Single byte XOR
    * Hex Prefilter
  * Analysis
    * IC
    * Hammming Distance
    * String Encoding Detection: Hex


* Roadmap:
  * take key(s) as argument
  * take key(s) file as argument
  * agparse/logging
  * repeating key XOR
  * runtime argument to set min letters and words in detectEnglish
  * cipher identification
  * railfence 
  * baconian
  * affine
  * transposition
  * bifid
  * columnar transposition
  * double transposition
  * playfair
  * Übchi
  * vigenere
  * frequency analysis
  * Cohen's kappa test
  * Chi test
  * general performance improvements
<br><br>
note: When using newDetectEnglish(), the default is to require 60% words and 75% letters to return a match. The ideal values can vary greatly depending on plaintext length and contents. These values can be tweaked in the isEnglish() function, or when calling isEnglish() eg. `isEnglish(cleartext, 50, 80)` would require 50% words and 80% letters.
