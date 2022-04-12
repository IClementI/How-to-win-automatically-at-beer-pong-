import imageio as iio
from matplotlib import pyplot as plt

def convertbmp(x='guigui.bmp'): 
    im = iio.imread(x)
    iio.imsave(x+'B.jpg',im)
    return im

guiguil = convertbmp()
plt.imshow(guiguil)
plt.show()
