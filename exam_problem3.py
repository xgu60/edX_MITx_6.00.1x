import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    CURRENTRABBITPOP += int(CURRENTRABBITPOP * (1.0 - float(CURRENTRABBITPOP)/MAXRABBITPOP))
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    if CURRENTRABBITPOP > 10:
        rabbitPopRatio = float(CURRENTRABBITPOP)/MAXRABBITPOP
        CURRENTRABBITPOP -= int(CURRENTFOXPOP * rabbitPopRatio)
        CURRENTFOXPOP = int(CURRENTFOXPOP * (1.0 + rabbitPopRatio/3 - (1.0 - rabbitPopRatio)*0.9))
        if CURRENTRABBITPOP < 10:
            CURRENTRABBITPOP = 10
        if CURRENTFOXPOP < 10:
            CURRENTFOXPOP = 10
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbitList = []
    foxList = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitList.append(CURRENTRABBITPOP)
        foxList.append(CURRENTFOXPOP)
    return (rabbitList, foxList)

populations = runSimulation(200)
rabbit = populations[0]
fox = populations[1]
steps = list(xrange(200))
#pylab.figure(1)
#pylab.plot(steps, rabbit)
#pylab.plot(steps, fox)
#pylab.show()

coeff = pylab.polyfit(range(len(rabbit)), rabbit, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbit))))
pylab.show()