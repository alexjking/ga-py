#!/usr/bin/python

import string
import random
import math

#Chromosome represented by a string of characters
class Chromosome:

	CONST_TARGET_STRING = "me thinks it is like a weasel"
	CONST_MUTATION_RATE = 1.0/len(CONST_TARGET_STRING) 

	chromosome = list("")

	def __init__(self):
		self.chromosome = [random.choice(string.ascii_lowercase) for _ in xrange(len(self.CONST_TARGET_STRING))]
	

	def mutate(self):
		child = Chromosome()
		for i in xrange(len(self.CONST_TARGET_STRING)):
			if(random.random() < self.CONST_MUTATION_RATE):
				child.chromosome[i] = random.choice(string.ascii_lowercase)
				print("mutating")
			else:
				child.chromosome[i] = self.chromosome[i]
		return child

	def calculate_fitness(self):
		fitness = 0
		for i in xrange(len(self.CONST_TARGET_STRING)):
			if(self.CONST_TARGET_STRING[i] == self.chromosome[i]):
				fitness += 1
		return fitness

	def to_string(self):
		fitness = self.calculate_fitness()
		print "{} fit={}".format(''.join(self.chromosome), fitness) 



if __name__ == '__main__':
	chromosome = Chromosome()
	chromosome.to_string()
	chromosome = chromosome.mutate()
	chromosome.to_string()
