# import Kivy
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

'''
Textinput:
https://kivy.org/docs/api-kivy.uix.textinput.html
Unicode, multiline, cursor navigation, selection and clipboard features are supported.
'''

class TestTextInputApp(App):
# layout
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        # button
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        
        # label
        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)

        # text input
        self.txt1 = TextInput(text='', multiline=True)
        (self.txt1).bind(text=self.on_text)
        layout.add_widget(self.txt1)

        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "Keywords: " + self.txt1.text

# text changed function
    def on_text(self, instance, value):
        print('Instance:',instance,' Value:',value,' Text written: ', self.txt1.text)

# run app
if __name__ == "__main__":
    TestTextInputApp().run()
 # join all items in a list into 1 big string
