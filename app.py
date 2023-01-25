from screen_manager import ScreenManager
import random
import time
import keyboard


def run():
    total_follows_count = 0

    while True:
        if ScreenManager.is_app_focused(app_title_name = "instagram"):              #se o título da janela em foco, for o que queremos executar, executa a verificação
            coordinates = ScreenManager.search_image_on_screen(image_to_search="teste.png")
            for coordinate in coordinates:
                total_follows_count += 1
                ScreenManager.click_on_screen(coordinate_to_click=coordinate)
                time.sleep(random.randint(1, 2))

            ScreenManager.scroll_on_screen(value_to_scroll=-400)
            time.sleep(random.randint(1, 2))
            print(f"Total de follows até o momento: {total_follows_count}")
        
        if keyboard.is_pressed("ESC"):          #verifica se o "ESC" está pressionado no momento
            print("Saindo do programa")
            break                               #sai do loop

run()