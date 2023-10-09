import pyautogui #detecta eventos/acoes
import keyboard #parte do mouse
altura = 600
largura = 500
captura =(360, 320, altura, largura)
ecra = pyautogui.screenshot(region=captura) #procedimento para detectar

def identifica_vermelho(imagem): #identificando vermelho
    altura_imagem , largura_imagem = imagem.size
    for x in range(0, altura_imagem):
        for y in range(0, largura_imagem):
            if imagem.getpixel((x, y)) == (255, 0, 0):
                return x, y
    
while not keyboard.is_pressed('m'): #ao encontrar vermelho...
    pixel_vermelho = identifica_vermelho(ecra)
    if pixel_vermelho:
        pyautogui.moveTo(pixel_vermelho[0]+captura[0], pixel_vermelho[1]+captura[1])
        pyautogui.mouseDown()#mover mouse e clicar
    pyautogui.sleep(0.016)
    ecra = pyautogui.screenshot(region=captura)
#pyautogui.moveTo(largura,altura, duration=0.1)