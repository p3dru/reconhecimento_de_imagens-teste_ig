from screen_manager import ScreenManager


def run():
    while True:
        coordinates = ScreenManager.get_all_matches_by_image(image_to_search="teste.png")
        for coordinate in coordinates:
            print(coordinate)


run()