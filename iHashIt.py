#!/usr/bin/env python3
# iHashIt by GoDzM4TT3O | Hash your string!
from __future__ import absolute_import
from __future__ import print_function
import hashlib, console
def main():
	method = str(console.input_alert("iHashIt by GoDzM4TT3O", "Enter a hash method (type list to get a list of available hash methods, extra for more info.)\nExample: md5"))
	if method == 'list':
		list = console.alert("iHashIt by GoDzM4TT3O", "List of available hash methods:\n\n'blake2b'\n'sha384'\n'sha256'\n'sha512'\n'md5'\n'blake2s'\n'sha3_224'\n'sha1'\n'sha3_512'\n'sha3_256'\n'shake_256'\nsha224'\n'sha3_384'\n'shake_128'")
	if method == 'extra':
		console.alert("iHashIt by GoDzM4TT3O", "Created on Wednesday, 22 August 2018 by GoDzM4TT3O on Pythonista 3, for Python 3.\nMade using hashlib library.\nLICENSE: GNU GPL v3.0\n----------\nHow does it work?\n1. User input using console.input_alert(\"iHashIt\", \"Description of user input\") and putting it into a variable\n2. Converting user input (which is a string) to a bytearray (I called it bytestring lol) in order to make hashing with user input (string) possible.\n3. Using hashlib for the rest.\n----------\nHUGE SHOUTOUT to Omz::software for creating Pythonista! I\'m a total noob, but at least I created some cool scripts with it, also using its great documentation!")
	string = console.input_alert("iHashIt", "Enter a string to hash")
	bytestring = bytearray(string, "utf-8")
	if method == 'md5':
			m = hashlib.md5()
			m.update(b""+bytestring)
			print("Your [MD5] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'blake2b':
			m = hashlib.blake2b()
			m.update(b""+bytestring)
			print("Your [BLAKE2B] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha384':
			m = hashlib.sha384()
			m.update(b""+bytestring)
			print("Your [SHA384] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha256':
			m = hashlib.sha256()
			m.update(b""+bytestring)
			print("Your [SHA256] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha512':
			m = hashlib.sha512()
			m.update(b""+bytestring)
			print("Your [SHA512] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'blake2s':
			m = hashlib.blake2s()
			m.update(b""+bytestring)
			print("Your [BLAKE2S] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha3_224':
			m = hashlib.sha3_224()
			m.update(b""+bytestring)
			print("Your [SHA3_224] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha1':
			m = hashlib.sha1()
			m.update(b""+bytestring)
			print("Your [SHA1] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha3_512':
			m = hashlib.sha3_512()
			m.update(b""+bytestring)
			print("Your [SHA3_512] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha3_256':
			m = hashlib.sha3_256()
			m.update(b""+bytestring)
			print("Your [SHA3_256] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'shake_256':
			m = hashlib.shake_256()
			m.update(b""+bytestring)
			print("Your [SHAKE_256] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha224':
			m = hashlib.sha224()
			m.update(b""+bytestring)
			print("Your [SHA224] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'sha3_384':
			m = hashlib.sha3_384()
			m.update(b""+bytestring)
			print("Your [SHA3_384] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	elif method == 'shake_128':
			m = hashlib.shake_128()
			m.update(b""+bytestring)
			print("Your [SHAKE_128] hashed string is:", m.hexdigest(), "\nDigest size: ", m.digest_size, "\nBlock size: ", m.block_size, "\n\n")
	else:
		print("Unknown hashing method")
		return 1
	print("iHashIt by GoDzM4TT3O")

if __name__ == '__main__':
	main()
