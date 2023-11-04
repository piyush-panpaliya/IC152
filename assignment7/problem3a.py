import numpy as np
import matplotlib.pyplot as plt
import random


colors = ['red', 'green', 'blue', 'yellow']


def simulate(n):
  outcomes = []
  for i in range(n):
    outcomes.append(random.randint(0, 3))
  return outcomes


def getfrequency(outcomes, n):
  relative_frequencies = [[], [], [], []]
  counts = [0, 0, 0, 0]
  for trial in range(1, n + 1):
    observed_values = outcomes[:trial]
    currentVal = observed_values[-1]
    counts[currentVal] += 1
    for i in range(4):
      relative_frequencies[i].append(counts[i] / trial)
  return relative_frequencies


def plot(relative_frequencies, n):
  for i in range(4):
    plt.plot(range(1, n + 1), relative_frequencies[i],
             label=i, color=colors[i])
    plt.legend(loc='upper right')
  plt.savefig('problem3a_' + str(n) + '.png')
  # plt.show()
  plt.close()


def main():
  lisOfTriial = [50, 500, 5000, 50000]
  for trialNo in lisOfTriial:
    outcomes = simulate(trialNo)
    relative_frequencies = getfrequency(outcomes, trialNo)
    plot(relative_frequencies, trialNo)


main()
