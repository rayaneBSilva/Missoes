# importando a biblioteca opencv 
import cv2
# lendo uma imagem do computador com a função imread()
imagem = cv2.imread('exemplo.jpg')
# faz um loop alinhado para percorrer linhas e colunas,
# o primeiro for irá percorrer as linhas e o segundo as colunas
for y in range(0, imagem.shape[0]): 
    for x in range(0, imagem.shape[1]): 
        imagem[y, x] = (x%256,y%256,x%256)
# abre a imagem com a função imshow()
cv2.imshow("Imagem modificada", imagem)
# espera pressionar qualquer tecla 
cv2.waitKey(0)
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida4.jpg", imagem)
