from PIL import Image
import numpy as np
import os as os
import matplotlib.pyplot as plt

path = '/home/clement/Documents/TIPE/LUmiere'
listing = os.listdir(path)
l=[]
nom=[]
for file in listing[:-1]:
    nom.append(int(file[2:-4]))
    im = Image.open(path + '/' + file)
    p = np.array(im)
    l.append(p[int(len(p)/2),int(len(p)/2)])
    
print(sorted(l))
l=[9, 150]
nom = [0, 600]
print(sorted(nom))
plt.plot(sorted(nom),sorted(l), label='y=0.235x+9')
plt.legend()
plt.xlabel('luminosité (en lux)')
plt.ylabel('Valeur pixel')
plt.show()
