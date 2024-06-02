from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from plyer import gps

class LocationApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Getting location...")
        self.layout.add_widget(self.label)
        return self.layout

    def on_start(self):
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
            gps.start(minTime=1000, minDistance=1)
        except NotImplementedError:
            self.label.text = "GPS not implemented on this platform."

    def on_location(self, **kwargs):
        self.label.text = f"Latitude: {kwargs['lat']}\nLongitude: {kwargs['lon']}"

    def on_status(self, stype, status):
        self.label.text = f"GPS Status: {status}"

if __name__ == '__main__':
    LocationApp().run()