import KeyPressModule as kp
from djitellopy import tello
import cv2
import time
from  time import sleep


kp.init() #pygame pencerimiz aktif olarak çalışacak
me=tello.Tello() #tello objemizi yarattık
me.connect() #tello drone bağlantımızı sağladık
print(me.get_battery()) #pil durumunu kontrol ediyoruz
global img
me.streamon()
def getKeyboardInput():
    lr,fb,up,yv=0,0,0,0 #sol-sağ,ileri-geri,yukarı-aşağı,rotasyon değerleri
    speed=30

    #klavye üzerinde her sol ok tuşuna bastığınız zaman drone 50 -speed ile sol yöne gidecektir.
    # + ise sağ yön anlamına gelir
    if kp.getKey("LEFT"): lr= -speed
    elif kp.getKey("RIGHT"): lr = speed

    #ileri geri gitmek içinde aynı mantık vardır + speed ileri - speed geri gitmek için kullanılır
    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    #alçalmak ve yükselmek için de aynı mantığı kullanıyoruz
    if kp.getKey("w"): up = speed
    elif kp.getKey("s"): up = -speed

    #drone saat yönünde ve ters yönde çevirmek için:
    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv= -speed

    #motorları kapatmak için:
    if kp.getKey("q"):
        me.land()
        time.sleep(3)
    #motorları durdurmak için :
    if kp.getKey("e"):
        me.takeoff()

    if kp.getKey("z"):
        cv2.imwrite(f"Images/{time.time()}.jpg",img)
        time.sleep(0.3)

    return [lr,fb,up,yv]

while True:
    vals=getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)