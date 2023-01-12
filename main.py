import asyncio
import random
from time import sleep

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

red     = [1, 0, 0, 1]
green   = [0, 1, 0, 1]
blue    = [0, 0, 1, 1]
purple  = [1, 0, 1, 1]
gray    = [1, 1, 1, 1]

pap1 = "Ну пап!!! Что далать?"
pap2 = "А делать-то что?"
pap3 = "Ну и...?"
pap4 = "А точнее?"
pap4 = "Ну пожалуйста!"

answers = ["поспи.", "поешь.", "надо подумать!", "а надо ли?", "тебе все по плечу!", "это все не то...", "а как надо?",
        "это тайна\nпокрытая макром!", "танцуй!", "включи Мозг!", "у мамы спроси.", "Плохо", "Думай", "Ага", "а как ты сама думаешь?"]


class MainApp(App):
    def build(self):
        img = Image(source='sky.jpg',
            size_hint=(1,5),
            pos_hint = {'center_x':.5, 'center_y':.5})
        return img


class ButtontwoApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('Вы нажали кнопку!')


class AskBallApp(App):

    def build(self):
        colors = [red, green, blue, purple, gray]
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(multiline=False,
                                  readonly=True,
                                  halign="center",
                                  font_size=55)

        main_layout.add_widget(self.solution)

        self.big_buttons = Button(text="Пап, чо делать?",
                             pos_hint={'center_x': .5, 'center_y': .5},
                             background_color=random.choice(colors)
                             )

        # big_buttons.bind(on_press=self.on_solution)
        self.big_buttons.bind(on_press=self.clocked_switch)

        # big_buttons.bind(on_release=self.clocked_switch)

        main_layout.add_widget(self.big_buttons)

        return main_layout

    def clocked_switch(self, instanse):
        self.solution.text = ""
        self.big_buttons.text = "Дай подумать..."
        self.big_buttons.disabled=True
        Clock.schedule_once(self.on_solution, 3)
    def on_solution(self, instance):
       # instance.text = "Жди..."
       question = [pap1,pap2,pap3,pap4]
       colors = [red, green, blue, purple, gray]


       text = answers
       if text:
        # instance.text = "Жди..."
        # sleep(3)
        textCh = random.choice(text)
        if textCh.find(".") > 0:
            solution = "Лис, " + textCh
        elif textCh.find("!") > 0:
            solution = "Алиса, " + textCh
        elif textCh.find("?") > 0:
            solution = "Алисочка, " + textCh
        else:
            solution = textCh + "."
        # text + " off!"
        self.solution.text = solution
        self.big_buttons.text = random.choice(question)
        self.big_buttons.background_color = random.choice(colors)
        self.big_buttons.disabled=False


if __name__ == '__main__':
     app=AskBallApp().run()