#!/usr/bin/python3

import requests
from pwn import *
from PIL import Image
import pytesseract
import pdb

#variables globales
url = "http://helpdesk.delivery.htb/captcha.php"

def makeRequest():

	s = requests.session()
	r = s.get(url)


	f= open("image.png","wb")
	f.write(r.content)
	f.close()

	captcha_text = pytesseract.image_to_string(Image.open("image.png"))

	log.info("El valor del captcha es %s" %captcha_text)

if __name__ == '__main__':

	makeRequest()
