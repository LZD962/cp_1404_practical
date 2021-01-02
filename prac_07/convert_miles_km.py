from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR = 1.60


class MilesConverterApp(App):
    km_str = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, mile):
        try:
            self.km_str = str(float(mile) * FACTOR)
        except:
            self.km_str = '0.0'

    def handle_increment(self, mile, change):
        try:
            self.root.ids.mile.text = str(float(mile) + change)
        except:
            self.root.ids.mile.text = '0.0'


MilesConverterApp().run()
