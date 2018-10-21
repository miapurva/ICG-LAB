import random
from PIL import Image
import cv2

a = [[0 for x in range(500)] for y in range(500)]

class im:
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue

for i in range(0,500):
	for j in range(0,500):
		a[i][j] = random.randint(0,255)

f = [[0 for x in range(500)] for y in range(500)]

for i in range(1,499):
	for j in range(1,499):
		if (i%2 == 0 and j%2 == 0): #Red
			f[i][j] = im(a[i][j],round((a[i][j-1]+a[i][j+1]+a[i-1][j]+a[i+1][j])/4),round((a[i-1][j-1]+a[i-1][j+1]+a[i+1][j-1]+a[i+1][j+1])/4))

		elif (i%2 == 1 and j%2 == 1): #Blue
			f[i][j] = im(round((a[i-1][j-1]+a[i-1][j+1]+a[i+1][j-1]+a[i+1][j+1])/4),round((a[i][j-1]+a[i][j+1]+a[i-1][j]+a[i+1][j])/4),a[i][j])

		elif (i%2 == 1 or j%2 == 1): #Green
			f[i][j] = im(round((a[i-1][j]+a[i+1][j])/2),round((a[i-1][j-1]+a[i-1][j+1]+a[i+1][j-1]+a[i+1][j+1]+a[i][j])/5),round((a[i][j-1]+a[i][j+1])/2))

img = Image.new('RGB', (500,500), "black")
pixels = img.load()		
for i in range(498):
	for j in range(498):
		pixels[i,j] = (int(f[i+1][j+1].red),int(f[i+1][j+1].green),int(f[i+1][j+1].blue))
img.show()

#print(f[1][1].red, f[1][1].green, f[1][1].blue)