import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

'''
Textinput widget is used
https://kivy.org/docs/api-kivy.uix.textinput.html
Unicode, multiline, cursor navigation, selection and clipboard features are supported.
'''

class TestTextInputApp(App):
# layout
    def build(self):
        '''
        Method called to build up the UI. Defines all the widgets involved
        '''
        # BoxLayout arranges widgets in an adjacent manner, either vertically or horizontally
        layout = BoxLayout(padding=10, orientation='vertical')

        # button
        btn1 = Button(text="Display Selection")
        # define callback for button press
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        
        # label1
        self.lbl1 = Label(text="Curent selection: ")
        layout.add_widget(self.lbl1)

        # label2
        # self.lbl2 = Label(text="")
        # layout.add_widget(self.lbl2)

        # text input 1
        self.txt1 = TextInput(text='Type here ...', multiline=True)
        (self.txt1).bind(text=self.on_text)
        layout.add_widget(self.txt1)

        return layout

# button click callback
    def buttonClicked(self,btn):
        '''
        When button is clicked, display the highlighted text in
        '''
        # self.lbl1.text = "Keywords: " + self.txt1.text
        self.lbl1.text = "Current selection: " + self.txt1.selection_text

# text changed callback 
    def on_text(self, instance, value):
        '''
        Update different UI widget (label) realtime with the entered text from text input 1
        '''
        # print('Instance:',instance,' Value:',value)
        # self.lbl2.text = "Repeat text: " + value

# run app
if __name__ == "__main__":
    TestTextInputApp().run()
 # join all items in a list into 1 big string
