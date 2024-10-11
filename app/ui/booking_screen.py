from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class BookingScreen(Screen):
    def __init__(self, **kwargs):
        super(BookingScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Пример интерфейса для экрана бронирования
        layout.add_widget(Label(text="Экран бронирования"))
        layout.add_widget(Button(text="Назад", on_press=self.go_back))

        self.add_widget(layout)

    def go_back(self, instance):
        # Логика возврата на главный экран
        self.manager.current = 'main'
