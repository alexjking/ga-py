#!/usr/bin/python

import Chromosome
import random

class GAWithCrossover:

	def __init__(self, populationNum):
		self.populationNum = populationNum

	def run(self):

		#create a population
		population =  [Chromosome.Chromosome() for _ in range(self.populationNum)]
		currentFitness = 0
		generationNum = 0

		while currentFitness < len(Chromosome.Chromosome().CONST_TARGET_STRING):
			#choose a parent chromosome from the highest fitness of two random chromosomes in the population
			randomMemberA = random.choice(population)
			randomMemberB = random.choice(population)
			parentA = None
			if(randomMemberA.calculate_fitness() > randomMemberB.calculate_fitness()):
				parentA = randomMemberA
			else:
				parentA = randomMemberB

			#choose a second parent
			randomMemberA = random.choice(population)
			randomMemberB = random.choice(population)
			parentB = None
			if(randomMemberA.calculate_fitness() > randomMemberB.calculate_fitness()):
				parentB = randomMemberA
			else:
				parentB = randomMemberB

			#create a child  by mutating the crossover of parentA and parentB
			crossover = self.crossover(parentA, parentB)
			child = crossover.mutate()

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

	def crossover(self, parentA, parentB):
		crossoverResult = Chromosome.Chromosome()
		for i in xrange(len(crossoverResult.CONST_TARGET_STRING)):
			if random.random() < 0.5:
				crossoverResult.chromosome[i] = parentA.chromosome[i]
			else:
				crossoverResult.chromosome[i] = parentB.chromosome[i]
		return crossoverResult




if __name__ == '__main__':
	ga = GAWithCrossover(500)
	print ga.run()