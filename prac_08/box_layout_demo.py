from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class BoxLayoutDemo(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.name_input = TextInput(id='input_name', text='', multiline=False)
        self.output_label = Label(id='output_label', text='')

        layout.add_widget(Button(text='Clear', on_press=self.clear))
        layout.add_widget(Button(text='Greet', on_press=self.greet))
        layout.add_widget(Label(text='Enter your name', color=(1, 1, 0, 1)))
        layout.add_widget(self.name_input)
        layout.add_widget(self.output_label)

        return layout

    def greet(self, instance):
        self.output_label.text = f"Hello {self.name_input.text}"

    def clear(self, instance):
        self.name_input.text = ''
        self.output_label.text = ''


if __name__ == '__main__':
    BoxLayoutDemo().run()
