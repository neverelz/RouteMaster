from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder

# Подключение KV файла (если вы используете .kv для описания интерфейса)
Builder.load_file('route_master.kv')


class MainScreen(Screen):
    pass


class BookingScreen(Screen):
    pass


class TripDetailScreen(Screen):
    pass


class RouteMasterScreenManager(ScreenManager):
    pass


class RouteMasterApp(App):
    def build(self):
        # Инициализация ScreenManager
        sm = RouteMasterScreenManager()

        # Добавляем экраны в ScreenManager
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(BookingScreen(name='booking'))
        sm.add_widget(TripDetailScreen(name='trip_detail'))

        # Возвращаем ScreenManager, чтобы он отображал первый экран
        return sm


# Запуск приложения
if __name__ == '__main__':
    RouteMasterApp().run()
