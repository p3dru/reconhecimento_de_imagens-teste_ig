from screen_manager import ScreenManager


def run():
    while True:
        if ScreenManager.is_app_focused(app_title_name = "instagram"):              #se o título da janela em foco, for o que queremos executar, executa a verificação
            coordinates = ScreenManager.search_image_on_screen(image_to_search="teste.png")
            for coordinate in coordinates:
                print(coordinate)                               #printa as coordenadas da imagem na tela

run()