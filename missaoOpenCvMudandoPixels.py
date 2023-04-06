# importando a biblioteca opencv 
import cv2
# usando a função imread() para lê a imagem 
imagem = cv2.imread('exemplo.jpg')
#veja que a ordem BGR e não RGB
(b, g, r) = imagem[0, 0] 
# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)
# Espera pressionar qualquer tecla
cv2.waitKey(0) 
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida2.jpg", imagem)
# imprime as cores de determinado pixel
print('O pixel (0, 0) tem as seguintes cores:')
# mostra as cores e os valores dos pixels
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
