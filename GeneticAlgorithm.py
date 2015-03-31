from random import randint
import math

def mutate(offspring):
	#mutation involves swapping two genes.
    offspring_len = len(offspring)
    bit_to_change = randint(0,offspring_len-1)
    bit_to_change2 = randint(0,offspring_len-1)
    print str(bit_to_change) + " " + str(bit_to_change2)
    tmp = offspring[bit_to_change]
    newoffspring  = offspring[:bit_to_change] + offspring[bit_to_change2]  + offspring[bit_to_change+1:]
    newoffspring  = newoffspring[:bit_to_change2] + tmp  + newoffspring[bit_to_change2+1:]
    return newoffspring

def crossover(parent1,parent2):
	#crossover involves finding a random partition everything to left of which is taken from
	#one parent and everything to right of which is taken from another parent.
    par_len = len(parent1)
    par_len2 = len(parent2)
    if par_len > par_len2:
        crossover_pt = randint(0,par_len2)
        return parent2[0:crossover_pt] + parent1[crossover_pt:]
    else:
        crossover_pt = randint(0,par_len)
        return parent1[0:crossover_pt] + parent2[crossover_pt:]

def selectTwo(chromosomes,fitnessValues):
	#select the two chromosomes with the highest fitnessValues
    max = 0
    max2 = 0
    idx = 0
    idx2 = 0
    cnt = 0
    for fitnessValue in fitnessValues:
        if fitnessValue > max:
            max2 = max
            idx2 = idx
            idx = cnt
            max = fitnessValue
        cnt+=1
    return (chromosomes[idx],chromosomes[idx2]) 
	

def endConditionNotSatisfied(chromosomes):
	#end condition is that all chromosomes only have ones
    for chromosome in chromosomes:
        len_chromosome = len(chromosome)
        if chromosome.count('1') != len_chromosome:
            return False
    return True

def evaluateFitness(chromosomes):
	#fitness is determined by the number of ones in the chromosome string
	fitnessValues = []
	for chromosome in chromosomes:
		fitnessValues.append(chromosome.count('1'))
	return fitnessValues

def generateRandomChromosomes(n):
	#randomly chose a number between 0 and 2^30 -1. Then use its binary representation in string format
	#to represent chromosome.
    randomChromosomes = []
    for i in range(0,n):
        choice = randint(0,math.pow(2,30)-1)
        randomChromosomes.append(bin(choice)[2:])
    return randomChromosomes
        
def GeneticAlgorithm:
	#[Start] Generate random population of n chromosomes (suitable solutions for the problem)
	#[Fitness] Evaluate the fitness f(x) of each chromosome x in the population
	#[New population] Create a new population by repeating following steps until the new population is complete
	#[Selection] Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)
	#[Crossover] With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.
	#[Mutation] With a mutation probability mutate new offspring at each locus (position in chromosome).
	#[Accepting] Place new offspring in a new population
	#[Replace] Use new generated population for a further run of algorithm
	#[Test] If the end condition is satisfied, stop, and return the best solution in current population
	#[Loop] Go to step 2
	n = 5
	chromosomes = generateRandomChromosomes(n)
	fitnessValues = evaluateFitness(chromosomes)
	while(endConditionNotSatisfied(chromosomes)):
		(parent1,parent2) = selectTwo(chromosomes,fitnessValues)
		offspring = crossover(parent1,parent2)
		mutate(offspring)
		chromosomes.remove(parent1)
		chromosomes.remove(parent2)
		chromosomes.append(offspring)
		
		
	
	