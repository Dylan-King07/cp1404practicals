from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App for dynamic creation of labels"""

    def __init__(self, **kwargs):
        """Initialise App"""
        super().__init__(**kwargs)
        self.names = ["Dylan", "Bailey", "Alicia", "Elliott", "Domenic", "Jack", "Daniel", "Hayden"]

    def build(self):
        """Build Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Labels for names and add them to the GUI"""
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)


DynamicLabelsApp().run()
