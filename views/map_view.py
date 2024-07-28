from kivymd.uix.screen import MDScreen
from kivy_garden.mapview import MapView as KivyMapView, MapMarker
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from utils.geocoding import get_coordinates

class MapView(MDScreen):
    def __init__(self, db, **kwargs):
        super().__init__(**kwargs)
        self.db = db
        
        self.map = KivyMapView(zoom=11, lat=52.2297, lon=21.0122)  # Przykładowe współrzędne dla Warszawy
        self.add_widget(self.map)
        
        self.load_clients_button = MDRectangleFlatButton(
            text="Załaduj klientów",
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            on_release=self.load_clients
        )
        self.add_widget(self.load_clients_button)

    def load_clients(self, instance):
        self.map.remove_all_markers()
        clients = self.db.get_clients()
        for client in clients:
            lat, lon = get_coordinates(client[4])  # Zakładamy, że adres jest w piątej kolumnie
            if lat and lon:
                marker = MapMarker(lat=lat, lon=lon, on_release=lambda x, c=client: self.show_client_info(c))
                self.map.add_marker(marker)

    def show_client_info(self, client):
        dialog = MDDialog(
            title=client[1],  # Imię i nazwisko
            text=f"Telefon: {client[2]}\nEmail: {client[3]}\nAdres: {client[4]}\nKod pocztowy: {client[5]}\nEtap Kanban: {client[7]}",
            size_hint=(0.8, 0.4),
            buttons=[MDRectangleFlatButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()