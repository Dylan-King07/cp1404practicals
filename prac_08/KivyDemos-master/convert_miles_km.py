from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """Convert miles to kms using a kivy app"""
    km = StringProperty()

    def build(self):
        """Build GUI"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Handle to convert miles to km"""
        miles = self.get_miles()
        kilometers = miles * MILES_TO_KM
        self.km = f"{kilometers:.3f}"

    def handle_increment(self, change):
        """Increase or decrease miles by 1"""
        miles_input = self.get_miles() + change
        self.root.ids.input_miles.text = str(miles_input)
        self.handle_convert()

    def get_miles(self):
        """Get miles text input, error check and convert to float"""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()

