import cv2
import matplotlib.pyplot as plt

image_path = "city image 1.png"
image = cv2.imread(image_path)
imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_=imageRGB.shape

rect1width,rect1height = 54,175
topleft1 = (390,70)
bottomright1  = (topleft1[0]+rect1width,topleft1[1]+rect1height)
cv2.rectangle(imageRGB,topleft1,bottomright1,(0,255,255),3)


centerx = topleft1[0] + rect1width //2
centery = topleft1[1] + rect1height //2

cv2.circle(imageRGB,(centerx,centery),15,(0,255,0),-1)
cv2.line(imageRGB,(centerx,centery),(topleft1[0],topleft1[1]),(0,255,6),3)
cv2.putText(imageRGB,"center1",(topleft1[0],topleft1[1]-15),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2,cv2.LINE_AA)

#print(height,width)
plt.figure(figsize=(12,8))
plt.imshow(imageRGB)
plt.title("Anotations")
plt.axis("off")
plt.show()
