import numpy as np
from PIL import Image, ImageOps
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})


# install pillow using:
# pip3 install pillow
# if above does not work and you are on windows, try:-
# py -m pip3 install pillow

# importing Image and ImageOps from PIL

# creating image object:
imInp = Image.open('problem1cInput.jpg')

# converting imInp to grayscale:
imGrayscale = ImageOps.grayscale(imInp)

# converting image to numpy array
pixels2D = np.array(imGrayscale)
print(pixels2D.shape)

# showing/saving image
# imGrayscale.show()
# imGrayscale.save('problem1cOutput.jpg')
plt.rcParams.update({'font.size': 12})


def plot(hist, name, display_name, ylabel):
  plt.title(display_name)
  plt.xlabel("grayscale value")
  plt.ylabel(ylabel)
  plt.grid(True)
  plt.hist(hist, bins=len(pixels2D[0]) // 2 + 1, color='#0504aa',
           alpha=0.7, density=True)
  plt.tight_layout()
  plt.savefig(f"{name}.png")
  plt.show()


# Write code for finding histogram here:
plot(pixels2D.flatten(), "problem1ci",
     "Histogram of grayscale image", 'pixel xount')
# Write code for finding histogram of difference of pixel's intensity
# with its left neighbour here:

finalHist = pixels2D.flatten().astype(np.int16)
histPlot = np.zeros(len(finalHist))
for i in range(1, len(finalHist)):
  histPlot[i] = finalHist[i] - finalHist[i - 1]
plot(histPlot, "problem1cii",
     "Histogram of difference in image with left neighbour", 'pixel intensity difference')
