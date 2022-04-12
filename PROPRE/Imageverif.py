import imageio as iio

nom = 'I002557'
im = iio.imread(nom+'.bmp')
iio.imsave('im'+'B.jpg',im)
