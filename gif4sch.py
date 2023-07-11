from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window

Window.size = (600, 400)
# (Window.width, Window.height)
Window.borderless = 1

class MyApp(App):
    def build(self):
        i = Image(source='chomping-cat.gif',
                  size_hint=(Window.width, Window.height),
                  pos_hint={'center_x': .5, 'center_y': .5})
        return i

if __name__ == '__main__':
    app = MyApp()
    app.run()













