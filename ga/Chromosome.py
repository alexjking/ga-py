#!/usr/bin/python

import string
import random

#Chromosome represented by a string of characters
class Chromosome:

	CONST_TARGET_STRING = "me thinks it is like a weasel"

	chromosome = ""

	def __init__(self):
		self.chromosome = ''.join(random.choice(string.ascii_lowercase) for _ in xrange(len(self.CONST_TARGET_STRING)))

if __name__ == '__main__':
	chromosome = Chromosome()
	print chromosome.chromosome
