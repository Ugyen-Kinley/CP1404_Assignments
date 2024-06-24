from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button


def handle_name_button(instance):
    print("Hello", instance.text)


class KivyDemo(App):
    status_text = StringProperty("Hello. Click the buttons :)")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counter = 0
        self.names = ["Lindsay", "Osmond", "Paul"]

    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('kivy_layout.kv')
        for name in self.names:
            button = Button(text=name)
            button.bind(on_press=handle_name_button)
            self.root.ids.names_box.add_widget(button)
        return self.root

    def handle_press(self, amount):
        self.counter += amount
        self.status_text = f"The count is: {self.counter}"


KivyDemo().run()
