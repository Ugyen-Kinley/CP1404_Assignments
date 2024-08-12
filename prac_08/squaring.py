from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty


class SquareNumberApp(App):
    result = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.result_label = None
        self.input_number = None

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.input_number = TextInput(id='input_number', text='', multiline=False)
        self.result_label = Label(text=self.result, color=(1, 0, 1, 1))
        self.info_label = Label(text='Enter a number and press "Square"')

        layout.add_widget(self.input_number)
        layout.add_widget(Button(text='Square', on_press=self.calculate))
        layout.add_widget(self.result_label)
        layout.add_widget(self.info_label)

        return layout

    def calculate(self, instance):
        try:
            number = float(self.input_number.text)
            self.result = str(number ** 2)
        except ValueError:
            self.result = '0.0'


if __name__ == '__main__':
    SquareNumberApp().run()
