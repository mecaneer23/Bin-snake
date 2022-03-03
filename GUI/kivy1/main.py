from kivy.app import App

from kivy.uix.button import Button

class KivyButton(App):

    def build(self):

        return Button(text="Welcome to LikeGeeks!", background_color=(155,0,51,53))

KivyButton().run()