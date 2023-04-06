# importando a biblioteca opencv 
import cv2
# lê a imagem com a função imread()
imagem = cv2.imread('exemplo.jpg')
# faz um loop alinhado usando for, para varrer todos os 
# pixels da imagem linha por linha.
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (100,0,0)
# Mostra a imagem com a função imshow
cv2.imshow("Imagem modificada", imagem)
#espera pressionar qualquer tecla
cv2.waitKey(0) 
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida3.jpg", imagem)