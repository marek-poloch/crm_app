from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        return MDLabel(
            text="Hello, KivyMD!", halign="center", text_colour=(1, 1, 1, 1)
                       )

MainApp().run()

