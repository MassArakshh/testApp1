import asyncio
import random
from time import sleep

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        img = Image(source='sky.jpg',
            size_hint=(1,5),
            pos_hint = {'center_x':.5, 'center_y':.5})
        return img


red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]
hz = [1,1,1,1]

class LayoutEx(App):
    def build(self):
        layout = BoxLayout(padding=5, spacing=3)
        colors = [red, green, blue, purple, hz]

        for i in range(6):
            btn = Button(text="Button #%s" % (i+1), background_color=random.choice(colors))
            # i= i + 1
            layout.add_widget(btn)
        return layout


class ButtonApp(App):
    def build(self):
        button = Button(text="Hello!",
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5}
                        # on_press=self.on_press_button
                        )
        button.bind(on_press=self.on_press_button)
        return button

    def on_press_button(self, instance):
         # img = Image(source='sky.jpg',
         #             size_hint=(1, 5),
         #             pos_hint={'center_x': .5, 'center_y': .5})
         # return img
         print('Вы нажали кнопку!')
         # app = MainApp()
         # app.run()
        # return app


class ButtontwoApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('Вы нажали кнопку!')


class TestwidgetApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False,
                                  readonly=True,
                                  halign="right",
                                  font_size=55)
        main_layout.add_widget(self.solution)

        big_buttons = Button(text="Press!",
                             pos_hint={'center_x': .5, 'center_y': .5})

        big_buttons.bind(on_press=self.on_solution)
        main_layout.add_widget(big_buttons)

        return main_layout

    def on_solution(self, instance):
       self.solution.text = ""
       # sleep(5)
       text = ["Fuck!","Hello!","What?","Who?","Well..."]
       if text:
         solution = random.choice(text)+" you!"

             # text + " off!"
         self.solution.text = solution





if __name__ == '__main__':

    # app=MainApp().run()
    # app.run()

    # app=LayoutEx().run()
    # app=ButtonApp().run()
    # app=ButtontwoApp().run()
    app=TestwidgetApp().run()