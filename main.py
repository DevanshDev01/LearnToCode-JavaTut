import kivy
from kivy.app import App
from kivy.uix.label import Label
from live.uix.button import Button


class LearnJava(App):
    def build(self):
        return Button(text='Hello Word!')



if __name__=='__main__':
    LearnJava().run()
    

