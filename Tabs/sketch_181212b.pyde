tabs = [0, 1, 2, 3, 4]
names = ['Spelergegevens', 'Duel', 'Rad', 'Kaartregels', 'Rad']
click = 0
def Spelergegevens():
    background (139,87,66)

def Duel():
    background (255,235,205)

def Rad1():
    background (178,223,238)
def Kaartregels():
     global kaart
     kaart = []
     for i in range (1,14):
         kaart.append(loadImage(str(i)+".jpg"))
     background(loadImage("backgroundd.jpg"))
     j = 0
     for heigh in range(4):
             for wed in range(5):
                 if j < 13:
                     image(kaart[j],wed*150,100+(heigh*200))
                     j+=1
     fill(140,0,0)
     Font = createFont ("Arial Bold Italic", 14)
     textFont(Font)
     textAlign (LEFT)
     Aas = text(" Een pion uit het\n startveld op eigen\n startpositie (vlag\n icoontje) zetten of\n een pion een plaats\n vooruit zetten.",0,150)
     Twee = text(" Bij deze kaart moet\n je je pion twee\n stappen vooruit\n zetten.",150,160)
     Drie = text(" Bij deze kaart moet\n je je pion drie\n stappen vooruit\n zetten.",150*2,160)
     Vier = text(" Bij deze kaart moet\n je je pion vier\n stappen achteruit\n zetten.",150*3,160)
     Vijf = text(" Bij deze kaart moet\n je je pion vijf\n stappen vooruit\n zetten.",150*4,160)
     Zes = text(" Bij deze kaart moet\n je je pion zes\n stappen vooruit\n zetten.",0,360)
     Zeven = text(" Bij deze kaart kan\n je je pion zeven\n stappen vooruit\n zetten of splietsen\n over twee pionnen.",150,360)
     Acht = text(" Bij deze kaart moet\n je je pion acht\n stappen vooruit\n zetten.",150*2,360)
     Negen = text(" Bij deze kaart moet\n je je pion negen\n stappen vooruit\n zetten.",150*3,360)
     Tien =  text(" Bij deze kaart moet\n je je pion tien\n stappen vooruit\n zetten.",150*4,360)
     Boer = text(" Een eigen pion\n met een pion van\n een andere speler\n omruilen.",0,560)
     Vrouw = text(" Een pion twaalf\n plaatsen vooruit\n zetten.",150,560)
     Heer = text(" Een pion uit het\n startveld op eigen\n startpositie(vlag\n icoontje) zetten.",150*2,560)
def Rad2():
    background(125,158,192)

    
def setup():
    size(800, 800)
    background(0)
    noStroke()
    fill(102)

def rectangel():
    global names
    global tabs
    for tab in tabs:
        fill(139,0,0)
        stroke(150)
        rect(50+tabs[tab]*150, 10, 100, 50)
    for x in range(len(names)):   
        fill(252,252,252)
        Font = createFont ("Arial Bold Italic", 13)
        textFont(Font)
        textAlign(CENTER)
        text(names[x], 50+(x*150), 30, 100, 50)
def mousePressed():
    global tabs
    if mouseButton == LEFT:
        if mouseX > 50 and mouseX < 150 and mouseY > 10 and mouseY < 60:
            Spelergegevens()
        if mouseX > 200 and mouseX < 300 and mouseY > 10 and mouseY < 60:
            Duel()
        if mouseX > 350 and mouseX < 450 and mouseY > 10 and mouseY < 60:
            Rad1()
        if mouseX > 500 and mouseX < 600 and mouseY > 10 and mouseY < 60:   
            Kaartregels()
        if mouseX > 650 and mouseX < 750 and mouseY > 10 and mouseY < 60: 
            Rad2()
        

            
def draw():
    mousePressed()
    rectangel()

    
            
