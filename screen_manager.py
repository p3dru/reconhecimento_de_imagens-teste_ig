import pyautogui
import logging
import cv2
import win32gui


class ScreenManager:
    
    @staticmethod
    def is_app_focused(app_title_name: str):                    #verifica o nome da janela
        active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()    #pega o nome da janela atual e seta como minúscula
        return app_title_name in active_window_title                #verifica com true ou false

    @staticmethod
    def click_on_screen(coordinate_to_click: int):
        pyautogui.click(coordinate_to_click)        #para clicar na imagem alvo que aparece na tela
    
    @staticmethod
    def scroll_on_screen(value_to_scroll: int):
        pyautogui.scroll(value_to_scroll)           #para rolar a tela afim de buscar novas imagens

    @staticmethod                                               #serve para não precisar instanciar a classe
    def search_image_on_screen(image_to_search: str):
        try:
            return pyautogui.locateAllOnScreen(image=image_to_search, grayscale=True, confidence=0.9) #pyautogui.locateAllOnScreen para verificar na tela inteira do computador
            #confidence é uim parâmetro que verifica, em uma escala de 0 à 1 o nível de fidelidade da imagem
            #grayscale deixa a imagem em tons de cinza
        except Exception as ex:
            logging.info(f"Imagem não encontrada. Erro: {ex}")   #informa o erro
