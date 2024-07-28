from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from views.client_list import ClientListView
from views.client_form import ClientFormView
from views.map_view import MapView
from views.calendar_view import CalendarView
from database import Database

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        client_list_btn = Button(
            text="Lista klientów",
            on_press=self.show_client_list
        )
        layout.add_widget(client_list_btn)
        
        add_client_btn = Button(
            text="Dodaj klienta",
            on_press=self.show_client_form
        )
        layout.add_widget(add_client_btn)
        
        map_btn = Button(
            text="Mapa klientów",
            on_press=self.show_map
        )
        layout.add_widget(map_btn)
        
        calendar_btn = Button(
            text="Kalendarz",
            on_press=self.show_calendar
        )
        layout.add_widget(calendar_btn)
        
        self.add_widget(layout)

    def show_client_list(self, instance):
        self.manager.current = 'client_list'

    def show_client_form(self, instance):
        self.manager.current = 'client_form'

    def show_map(self, instance):
        self.manager.current = 'map'

    def show_calendar(self, instance):
        self.manager.current = 'calendar'

class CRMApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ClientListView(name='client_list'))
        sm.add_widget(ClientFormView(name='client_form'))
        sm.add_widget(MapView(name='map'))
        sm.add_widget(CalendarView(name='calendar'))
        return sm

if __name__ == '__main__':
    CRMApp().run()