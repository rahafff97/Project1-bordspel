kaart_Image =[]
def setup():
   size(800,800 )
   global kaart_Image
   for i in range (13):
         kaart_Image.append(loadImage (str(i)+".jpg") )

def draw ():
    background(loadImage("backgroundd.jpg"))
    j=0
    for he in range (4):
        for wd in range (5):
            if j < 13:
                image(kaart_Image[j],wd*150,100+(he*200))
                j+=1
