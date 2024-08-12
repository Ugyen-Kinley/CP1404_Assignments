from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty


class MilesToKmApp(App):
    result = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.result_label = None
        self.miles_input = None

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.miles_input = TextInput(id='input_miles', text='', multiline=False)
        self.result_label = Label(text=self.result)
        self.info_label = Label(text='Enter miles and press "Convert"')

        top_section = BoxLayout(orientation='horizontal')
        top_section.add_widget(Button(text='Up', on_press=self.increment))
        top_section.add_widget(self.miles_input)
        top_section.add_widget(Button(text='Down', on_press=self.decrement))

        layout.add_widget(top_section)
        layout.add_widget(Button(text='Convert', on_press=self.convert))
        layout.add_widget(self.result_label)
        layout.add_widget(self.info_label)

        return layout

    def convert(self, instance):
        try:
            miles = float(self.miles_input.text)
            km = miles * 1.60934
            self.result = str(km)
        except ValueError:
            self.result = '0.0'

    def increment(self, instance):
        try:
            miles = float(self.miles_input.text) + 1
        except ValueError:
            miles = 1
        self.miles_input.text = str(miles)
        self.convert(instance)

    def decrement(self, instance):
        try:
            miles = float(self.miles_input.text) - 1
        except ValueError:
            miles = -1
        self.miles_input.text = str(miles)
        self.convert(instance)


if __name__ == '__main__':
    MilesToKmApp().run()
