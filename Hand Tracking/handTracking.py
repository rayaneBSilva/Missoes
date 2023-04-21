# importando biblioteca cv2
import cv2
import mediapipe as mp

# criando variavel video para ser usada, para abrir a nossa webcam
video = cv2.VideoCapture(0)
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils 

while True:
    check,img = video.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h,w,_ = img.shape
    point = []
    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
            for id,cord in enumerate(points.landmark):
                cx,cy = int(cord.x*w), int(cord.y*h)
                point.append((cx,cy))

        fingers = [8,12,16,20]
        cont = 0
        if points:
            if point[4][0] < point[2][0]:
                cont += 1
            for x in fingers:
                if point[x][1] < point[x -2][1]:
                    cont += 1

        cv2.rectangle(img,(80,10),(200,100),(255,0,0),-1)
        cv2.putText(img,str(cont),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)

    cv2.imshow("Imagem", img)
    cv2.waitKey(1)