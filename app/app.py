import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
from ui.main_screen import RouteMasterApp

if __name__ == "__main__":
    RouteMasterApp().run()
