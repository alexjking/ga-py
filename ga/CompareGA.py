import GAWithCrossover
import GAWithoutCrossover
import HillClimber
import matplotlib.pyplot as plt
import numpy as np

CONST_NUM_RUNS = 5
CONST_POPULATION = 500

def get_crossover_average(mutationRate=None):
	return reduce(lambda x,y: x+y, [GAWithCrossover.GAWithCrossover(CONST_POPULATION, mutationRate).run() for _ in xrange(CONST_NUM_RUNS)]) / CONST_NUM_RUNS

def get_ga_without_crossover_average(mutationRate=None):
	return reduce(lambda x,y: x+y, [GAWithoutCrossover.GAWithoutCrossover(CONST_POPULATION, mutationRate).run() for _ in xrange(CONST_NUM_RUNS)]) / CONST_NUM_RUNS

def get_hill_climber_average():
	return reduce(lambda x,y: x+y, [HillClimber.HillClimber().run() for _ in xrange(CONST_NUM_RUNS)]) / CONST_NUM_RUNS

def get_hill_climber_results():
	results = []
	for i in xrange(CONST_NUM_RUNS):
		results.append(HillClimber.HillClimber().run())
	return results

def get_ga_results():
	results = []
	for i in xrange(CONST_NUM_RUNS):
		results.append(GAWithoutCrossover.GAWithoutCrossover(CONST_POPULATION).run())
	return results

def get_ga_crossover_results(mutationRate=None):
	results = []
	for i in xrange(CONST_NUM_RUNS):
		results.append(GAWithCrossover.GAWithCrossover(CONST_POPULATION, mutationRate).run())
	return results

def generate_fitness_mutation_rate_graph():

	ga_results = list()
	crossover_results = list()
	mutation_rate_list = list()

	for i in xrange(1, 10):
		mutationRate = 0.01*i
		print mutationRate
		mutation_rate_list.append(mutationRate)
		crossover_results.append(get_crossover_average(mutationRate))
		ga_results.append(get_ga_without_crossover_average(mutationRate))

	print mutation_rate_list
	print crossover_results

	plt.axis([0, 0.2, 0, 60000])
	plt.plot(mutation_rate_list, crossover_results)
	plt.plot(mutation_rate_list, ga_results)
	plt.show()

	#print reduce(lambda x,y: x+y, [GAWithCrossover.GAWithCrossover(CONST_POPULATION, 1.0/29).run() for _ in xrange(CONST_NUM_RUNS)]) / CONST_NUM_RUNS



def generate_population_fitness_graph():

	populationSize = list()

	crossoverAverageGenerations = list()
	gaAverageGenerations = list()
	hillClimberAverageGenerations = list()

	hill_error = np.zeros((2,49))
	crossover_error = np.zeros((2,49))
	ga_error = np.zeros((2,49))
	
	counter = 0

	for i in xrange(10, 500, 10):
		print i
		populationSize.append(i)
		CONST_POPULATION = i
		

		hill = get_hill_climber_results()
		hill_average = np.mean(hill)
		hillClimberAverageGenerations.append(hill_average)
		hill_error[0][counter] = np.absolute(min(hill) - hill_average )
		hill_error[1][counter] = np.absolute(max(hill) - hill_average )

		crossover = get_ga_crossover_results()
		crossover_average = np.mean(crossover)
		crossoverAverageGenerations.append(crossover_average)
		crossover_error[0][counter] = np.absolute(min(crossover) - crossover_average )
		crossover_error[1][counter] = np.absolute(max(crossover) - crossover_average )

		ga = get_ga_results()
		ga_average = np.mean(ga)
		gaAverageGenerations.append(ga_average)
		ga_error[0][counter] = np.absolute(min(ga) - ga_average )
		ga_error[1][counter] = np.absolute(max(ga) - ga_average )

		counter += 1



	plt.errorbar(populationSize, hillClimberAverageGenerations, yerr=hill_error, label='Hill Climber')
	plt.errorbar(populationSize, crossoverAverageGenerations, yerr=crossover_error, label='GA with crossover')
	plt.errorbar(populationSize, gaAverageGenerations, yerr=ga_error, label='GA w/o crossover')

	plt.legend()
	plt.title('Number of generations to optimise string for different population sizes.')


	plt.ylabel("Num. Generations")
	plt.xlabel("Population Size")
	plt.axis([0, 500, 0, 60000])
	plt.show()



if __name__ == '__main__':
	#generate_population_fitness_graph()
	#print get_crossover_average()
	#print get_ga_without_crossover_average()
	#print get_hill_climber_average()
	generate_fitness_mutation_rate_graph()