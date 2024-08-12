from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        names = ['Alice', 'Bob', 'Charlie']  # List of names

        for name in names:
            label = Label(text=name)
            layout.add_widget(label)

        return layout


if __name__ == '__main__':
    DynamicLabelsApp().run()
