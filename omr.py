import cv2
import numpy as np
img=cv2.imread('omr_img.jpg')
im=cv2.resize(img,(500,500))
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
n=cv2.fastNlMeansDenoising(gray,100)
edge=cv2.Canny(n,25,50)
circle=cv2.HoughCircles(edge,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
thresh=cv2.threshold(n, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
circle=np.uint16(np.around(circle))
circles=[[],[],[]]
for i in circle[0,:]:
	cv2.circle(n,(i[0],i[1]),i[2],(0,255,0),2,cv2.LINE_AA)
for i in circle[0,:]:
	if i[1]<=200 :
		circles[0].append(i)
	elif i[1]>200 and i[1]<=300 :
		circles[1].append(i)
	elif i[1]>300 and i[1]<500 :
		circles[2].append(i)
c=[[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
z=0
for i in circles:
		for j in i:
			if j[0]<=100:
				c[z][0].append(j)
			if j[0]<=200 and j[0]>=100:
				c[z][1].append(j)
			if j[0]<=400 and j[0]>=200:
				c[z][2].append(j)
			if j[0]>=400:
				c[z][3].append(j)
		z+=1
t=[]
key=['A','B','C']
q=0
crt=wrg=0
for i in c:
	q+=1
	for x in i:
		for y in x:
			y=list(y)
		roi=(y[0]-y[2],y[0]+y[2],y[1]-y[2],y[1]+y[2])
		crop=thresh[roi[2]:roi[3],roi[0]:roi[1]]
		t.append(cv2.countNonZero(crop))
	ans=max(t)
	opt=t.index(ans)+1
	if opt==1:
		op='A'
	elif opt==2:
		op='B'
	elif opt==3:
		op='C'
	else:
		op='D'
	if ans>=1000:
		if key[q-1]==op:
			print(q,".",op,"- CORRECT")
			crt+=1
		else:
			print(q,".",op,"- WRONG")
			print("Correct answer :",key[q-1])
			wrg+=1
	else:
		print(q,".","No circle is shaded")
		wrg+=1
	t.clear()
print("\nNo of correct answers:",crt)
print("\nNo of wrong answers:",wrg)
