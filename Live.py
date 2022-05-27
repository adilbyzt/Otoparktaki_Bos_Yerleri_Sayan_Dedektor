import cv2
import numpy as np
import pickle


cap=cv2.VideoCapture('Live.mp4')

with open('Koordinat','rb') as f:
    posList=pickle.load(f)
    
frame_counter = 0
def check(imgPro):
    spaceCount=0
    for pos in posList:
        if pos[0]<pos[2]:    #dikdörtgen çizilen alan eğer önce sol üst sonra sağ alta basılarak seçildiyse if içerisine gir
            crop=imgPro[pos[1]:pos[3],pos[0]:pos[2]]  
        else:                #dikdörtgen çizilen alan eğer önce sağ alt sonra sol üste basılarak seçildiyse veya diğer şekilde else içerisine gir 
            crop=imgPro[pos[3]:pos[1],pos[2]:pos[0]]
            
        count=cv2.countNonZero(crop)
        toplampixel=(pos[2]-pos[0])*(pos[3]-pos[1])
        toplampixel = abs(toplampixel)
        esikpixel=toplampixel/5
        print("-----------------------")
        print("toplam pixel:"+str(toplampixel))
        print("count:"+str(count))
        print("esikpixel:"+str(esikpixel))
        print("-----------------------")
        
        if count<esikpixel:  
            spaceCount+=1
            color=(0,255,0)   #alan boş demek
            thick=5
        else:
            color=(0,0,255)   #alan dolu demek
            thick=2

        cv2.rectangle(img,(pos[0],pos[1]),(pos[2],pos[3]),color,thick) 
    cv2.rectangle(img,(45,30),(330,75),(58, 151, 94),-1)
    cv2.putText(img,f'Bos Alan: {spaceCount}/{len(posList)}',(50,60),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,255,255),2)

while True:
    ret,img=cap.read()
    if not ret:
        print("Video Bitti....")
        break
    if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0 
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(3,3),1)
    Thre=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    blur=cv2.medianBlur(Thre,5)
    kernel=np.ones((3,3),np.uint8)
    dilate=cv2.dilate(blur,kernel,iterations=1)
    """
    cv2.imshow("1-gray",gray)
    cv2.imshow("2-gaus blur",blur)
    cv2.imshow("3-Threshold",Thre)
    cv2.imshow("4-Median Blur",blur)
    """
    cv2.imshow("5-dilate",dilate)
    
    check(dilate)
    cv2.imshow("Video Ekranı",img)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
    
    
cv2.destroyAllWindows()
