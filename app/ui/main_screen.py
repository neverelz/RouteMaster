from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class RouteMasterScreenManager(ScreenManager):
    pass


class RouteMasterApp(App):
    def build(self):
        sm = RouteMasterScreenManager()
        from ui.booking_screen import BookingScreen
        from ui.route_screen import RouteScreen
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(BookingScreen(name='booking'))
        sm.add_widget(RouteScreen(name='route'))
        return sm


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Пример интерфейса для главного экрана
        layout.add_widget(Button(text="Перейти к бронированию", on_press=self.go_to_booking))
        layout.add_widget(Button(text="Выйти", on_press=self.exit_app))

        self.add_widget(layout)

    def go_to_booking(self, instance):
        # Логика перехода на экран бронирования
        self.manager.current = 'booking'

    def exit_app(self, instance):
        # Логика выхода из приложения
        App.get_running_app().stop()
