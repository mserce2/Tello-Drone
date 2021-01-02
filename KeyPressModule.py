import pygame


def init():
    pygame.init()
    #pygame için ekranımızı ayarlıyoruz
    win = pygame.display.set_mode((600, 600))
    bg = pygame.image.load("csd.png")
    win.blit(bg,(0,0))

#Basılan tuşları yakalamak için:
def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey=getattr(pygame,"K_{}".format(keyName))
    print("K_{}".format(keyName))
    if keyInput[myKey]:
        ans=True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("sol tuşuna basıldı")
    if getKey("RIGHT"):
        print("sağ tuşa basıldı")
    if getKey("UP"):
        print("up tuşa basıldı")

if __name__ =="__main__":
    init()
    while True:
        main()









