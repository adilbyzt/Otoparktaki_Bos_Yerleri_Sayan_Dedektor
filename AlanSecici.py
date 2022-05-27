import cv2
import pickle
import numpy as np
from subprocess import call

pos_matrix = np.zeros((2,2),np.int)
counter = 0
try:
    with open('Koordinat','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]

def mouseClick(events,x,y,flags,params):
    global counter
    if events==cv2.EVENT_LBUTTONDOWN:
        pos_matrix[counter] = x,y 
        counter = counter + 1
        
        
    if events==cv2.EVENT_RBUTTONDOWN:           #fareye sağ tıklanıldığında içerisine girer
        for i,pos in enumerate(posList):
            
            if (pos[0]<x<pos[2] or pos[0]>x>pos[2]) and (pos[1]<y<pos[3] or pos[1]>y>pos[3]): 
                                                   #x1--> pos[0] , y1 --> pos[1] , x2 --> pos[2] , y2 -->pos[3] 
                                                   #silmek için sağ tıklanılan yerin kordinatı x ve y 'dir.
                print("Seçilen Bölge Silindi...")  
                posList.pop(i)                     #tıklanılan yerin kordinatı seçilen yerin kordinatının arasındaysa
                                                   #tuple daki o kordinatları sil yani rectangleyi kaldır.
                                                
            
    with open('Koordinat','wb') as f:          
        pickle.dump(posList,f)
    
    

while True:
    img=cv2.imread("Live.png") 
    
    if counter == 2: # sadece 2 noktaya tıklandığında içerisine girer ve tupleye değerleri kaydeder
        starting_x = pos_matrix[0][0] #x1 kordinatının kayıt edildiği matrisin değerini starting_x değişkenine atıyoruz
        starting_y = pos_matrix[0][1]
 
        ending_x = pos_matrix[1][0]
        ending_y = pos_matrix[1][1]     
        posList.append((starting_x,starting_y,ending_x,ending_y))  #tuple içerisine x1,y1,x2,y2 değişkenlerini atıyoruz
        print("Yeni Bölge Eklendi")
        counter=0                           #2 nokta seçildikten ve tupleye eklendikten sonra sayacı sıfırla
        
    for pos2 in posList: cv2.rectangle(img, (pos2[0], pos2[1]), (pos2[2], pos2[3]), (255, 0, 0), 2) #tuple içerisindekileri çiz
    
    cv2.imshow("Bos Alan Secim",img)     #resmi görüntüle
    cv2.setMouseCallback("Bos Alan Secim",mouseClick)
    k = cv2.waitKey(1)
    if k == ord('q'):           #q tuşuna basıldığında programı kapat
        break
    if k == ord('n'):
        call(["python", "Live.py"])
        break
        
cv2.destroyAllWindows()
