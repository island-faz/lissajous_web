import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow
import math
import random

class Point(object):

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y)


im = Image.new("RGB", (5000,5000))
draw = ImageDraw.Draw(im)

nodeArr = []
for i in range(1500):
	nodeArr.append(Point(random.randint(0 + 100, 5000 - 100), random.randint(0 + 100, 5000 - 100)))

for i in nodeArr:
    for j in nodeArr:
    	if (i.distance(j) < 750):
        	r = random.randint(0, 255)
        	g = random.randint(0, 255)
        	b = random.randint(0, 255)    		    			
	        draw.line((i.getX(), i.getY(), j.getX(), j.getY()), fill=(r,g,b))

im.show()