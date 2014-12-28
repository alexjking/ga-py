#!/usr/bin/python

import Chromosome
import random

class GAWithoutCrossover:

	def __init__(self, populationNum, mutationRate):
		self.populationNum = populationNum
		self.mutationRate = mutationRate

	def run(self):

		#create a population
		population =  [Chromosome.Chromosome(mutation=self.mutationRate) for _ in range(self.populationNum)]
		currentFitness = 0
		generationNum = 0

		while currentFitness < len(Chromosome.Chromosome().CONST_TARGET_STRING):
			#choose a parent chromosome from the highest fitness of two random chromosomes in the population
			randomMemberA = random.choice(population)
			randomMemberB = random.choice(population)
			parent = None
			if(randomMemberA.calculate_fitness() > randomMemberB.calculate_fitness()):
				parent = randomMemberA
			else:
				parent = randomMemberB

			#create a child from the parent
			child = parent.mutate()
			childFitness = child.calculate_fitness()
			if childFitness > currentFitness:
				currentFitness = childFitness

			#choose a chromosome to be replaced with the generated child
			randomMemberA = random.choice(population)
			randomMemberB = random.choice(population)
			if(randomMemberA.calculate_fitness() > randomMemberB.calculate_fitness()):
				randomMemberB.set_chromosome(child.chromosome)
			else:
				randomMemberA.set_chromosome(child.chromosome)
			
			#increment the generation number
			generationNum += 1

		return generationNum


if __name__ == '__main__':
	ga = GAWithoutCrossover(500)
	print ga.run()