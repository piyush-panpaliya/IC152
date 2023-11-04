import matplotlib.pyplot as plt
import numpy as np
import random

SIM_COUNT = 50000


def simulate(noOfTrials):
  observations = [random.randint(0, 3) for _ in range(noOfTrials)]
  return np.mean(observations)


def main(noOfTrials):
  sample_means = [simulate(noOfTrials)
                  for _ in range(SIM_COUNT)]
  plt.hist(sample_means, bins=60, density=True, alpha=0.6, color='b')
  plt.title(f'Histogram of Sample Means (Trials: {noOfTrials})')
  plt.show()
  plt.savefig(f'problem3b_{noOfTrials}_50000.png')


main(5)
main(50)
