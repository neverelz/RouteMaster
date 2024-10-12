import os
from dotenv import load_dotenv
from kivy_garden.mapview import MapView, MapMarker, MapSource
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from plyer import gps

# Загрузка API ключей
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

class RouteMasterScreenManager(ScreenManager):
    pass

class RouteMasterApp(App):
    def build(self):
        sm = RouteMasterScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Настройка кастомного источника тайлов для Яндекс.Карт
        yandex_map_source = MapSource(
            url="https://core-renderer-tiles.maps.yandex.net/tiles?l=map&v=21.05.20&x={x}&y={y}&z={z}&scale=1&lang=ru_RU",
            tile_size=256,
            image_ext="png",
            attribution="© Яндекс.Карты"
        )

        # Настройка карты
        self.map_view = MapView(zoom=10, lat=55.751244, lon=37.618423, map_source=yandex_map_source)
        layout.add_widget(self.map_view)

        # Кнопка для отображения текущей геолокации
        #layout.add_widget(Button(text="Показать мою геолокацию", on_press=self.show_location))
        #layout.add_widget(Button(text="Выйти", on_press=self.exit_app))

        self.add_widget(layout)

    def show_location(self, instance):
        # Запрашиваем текущую геолокацию
        try:
            gps.configure(on_location=self.on_location)  # Настройка функции обратного вызова
            gps.start()
        except Exception as e:
            print(f"Ошибка: {e}")

    def on_location(self, location):
        # Добавление маркера на карту с текущими координатами
        lat = location['latitude']
        lon = location['longitude']

        # Удаление предыдущих маркеров (если нужно)
        self.map_view.clear_markers()

        # Добавление нового маркера
        marker = MapMarker(lat=lat, lon=lon)
        self.map_view.add_marker(marker)

        # Центрируем карту на текущей геолокации
        self.map_view.center_on(lat, lon)

        # Остановка GPS после получения координатов
        gps.stop()

    def exit_app(self, instance):
        App.get_running_app().stop()


