#!/usr/bin/python

import Chromosome

class HillClimber:

	def run(self):
		generation = 0
		chromosome = Chromosome.Chromosome()
		while chromosome.calculate_fitness() < len(chromosome.CONST_TARGET_STRING):
			child = chromosome.mutate()
			if child.calculate_fitness() > chromosome.calculate_fitness():
				chromosome = child
			generation += 1
		return generation


if __name__ == '__main__':
	climber = HillClimber()
	print climber.run()