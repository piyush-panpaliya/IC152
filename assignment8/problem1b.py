from matplotlib import pyplot as plt
import numpy as np
# plt.rcParams.update({'font.size': 22})

# References:-
# https://note.nkmk.me/en/python-pillow-imagedraw/
# https://datacarpentry.org/image-processing/05-creating-histograms/

# creates circle in matrix of dimension size x size
# boundary may be used of problem1b.py


def getDist(x, y, size):
  return np.sqrt((x - size // 2)**2 + (y - size // 2)**2)


def circle(size, centre=0, boundary=128):
  kernel_2D = 255 * np.ones((size, size))
  interp = list(range(boundary))  # may be used for problem1b.py
  for i in range(size):
    for j in range(size):
      # if distance from centre is less than radius, make values 0
      if (i - size / 2)**2 + (j - size / 2)**2 <= (size / 2)**2:
        kernel_2D[i, j] = 128 * getDist(i, j, size) // (size // 2)
  kernel_2D[size // 2, size // 2] = centre
  histList = []
  for i in range(size):
    for j in range(size):
      if kernel_2D[i, j] < 255:
        histList.append(kernel_2D[i, j])

  # begining a subplot with 1 row and 2 columns
  # for showing circle in 1st column
  plt.subplot(1, 2, 1)

  # displaying image with bilinear interpolation (do display nicely) and gray colormap.
  # colormap: maps pixel indensity data to the actual color values.
  # color values are displayed using imshow.
  plt.imshow(kernel_2D, interpolation='bilinear', cmap='gray')
  plt.title("Image")

  # continuing subplot with 1 row and 2 columns
  # for showing histogram in 2nd column
  plt.subplot(1, 2, 2)
  plt.title("Grayscale Histogram")
  plt.xlabel("grayscale value")
  plt.ylabel("pixel count")
  plt.grid(True)
  # plt.xlim((0.0, 250.0))  # <- named arguments do not work here
  plt.hist(histList, bins=boundary // 2 + 1, color='#0504aa',
           alpha=0.7, rwidth=0.6, align='mid', density=True)
  plt.tight_layout()

  # resizing figure for maximized window
  figure = plt.gcf()  # get current figure
  figure.set_size_inches(16, 12)

  plt.savefig('problem1b.png')
  plt.show()  # comment this line and uncomment next to save image
  # plt.savefig('problem1bOp.png', bbox_inches='tight')# change this to problem1bOp.png

  return kernel_2D


# main program:
circle(255)
