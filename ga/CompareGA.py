import GAWithCrossover
import GAWithoutCrossover
import HillClimber

CONST_NUM_RUNS = 5
CONST_POPULATION = 500

def get_crossover_average():
	return reduce(lambda x,y: x+y, [GAWithCrossover.GAWithCrossover(CONST_POPULATION).run() for _ in xrange(CONST_NUM_RUNS)]) / CONST_NUM_RUNS

def get_ga_without_crossover_average():
	return reduce(lambda x,y: x+y, [GAWithoutCrossover.GAWithoutCrossover(CONST_POPULATION).run() for _ in xrange(CONST_NUM_RUNS)]) / CONST_NUM_RUNS

def get_hill_climber_average():
	return reduce(lambda x,y: x+y, [HillClimber.HillClimber().run() for _ in xrange(CONST_NUM_RUNS)]) / CONST_NUM_RUNS


if __name__ == '__main__':
	print get_crossover_average()
	print get_ga_without_crossover_average()
	print get_hill_climber_average()