from PIL import Image

def converteps_png():
    image_eps = 'random317186.eps'
    im = Image.open(image_eps)
    fig = im.convert('RGBA')
    image_png= 'logo-rgb.png'
    fig.save(image_png, lossless = True)

path1 = path of folder of images    
path2 = path of folder to save images    

listing = os.listdir(path1)    
for file in listing:
    im = Image.open(path1 + file)    
    im.resize((50,50))                % need to do some more processing here             
    im.save(path2 + file, "JPEG")
