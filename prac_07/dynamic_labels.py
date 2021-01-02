from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.name_to_phone:
            temp = Label(text=name)
            self.root.ids.entries.add_widget(temp)
        return self.root


DynamicWidgetsApp().run()
