from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')

Builder.load_string("""
<MenuScreen>:
    Image:
        source: 'download.jpg'
        size: self.texture_size
    BoxLayout:
        Button:
            size_hint: [.7, .05]
            text: 'Профиль'   
        Button:
            size_hint: [.7, .05]
            text: 'Услуги'
            on_press: 
                root.manager.current = 'settings'
        Button:
            size_hint: [.7, .05]
            text: 'О нас'
            on_press:
                root.manager.current = 'our me'
<SettingsScreen>:
    BoxLayout:
        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            Button:
                size_hint: [1, .05]
                font_size: '10'
                text: 'Бронирование'
                on_press:
                    root.manager.current = 'bron'
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            Button:
                size_hint: [1, .05]
                font_size: '10'
                text: 'Ресторан'
        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'top'
            Button:
                size_hint: [1, .05]
                font_size: '10'
                text: 'Спа и фитнес'
    AnchorLayout:
        BoxLayout:
            Button:
                size_hint: [.7, .05]
                text: 'Профиль'  
                on_press: 
                    root.manager.current = 'menu'
            Button:
                size_hint: [.7, .05]
                text: 'Услуги'       
                on_press: 
                    root.manager.current = 'settings'
            Button:
                size_hint: [.7, .05]
                text: 'О нас'   
                on_press:
                    root.manager.current = 'our me'
<OurMe>:
    BoxLayout:
        Button:
            size_hint: [1, .05]
            text: 'Профиль'
            on_press: 
                root.manager.current = 'menu'
        Button:
            size_hint: [1, .05]
            text: 'Услуги'
            on_press: 
                root.manager.current = 'settings'
        Button:
            size_hint: [1, .05]
            text: 'О нас'

<Bron>:
    Button:
        size_hint: [.3, .05]
        text: 'Назад'
        on_press:
            root.manager.current = 'settings'
    AnchorLayout:
        anchor_x: 'center'
        anchot_y: 'center'
        AnchorLayout:
            size_hint: [.9, .5]
            anchor_x: 'left'
            anchor_y: 'center'
            GridLayout:
                cols: 2
                rows: 6
                Label:
                    text: 'Прибытие'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                Label:
                    text: 'Ночи'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                Label:
                    text: 'Отъезд'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                Label:
                    text: 'Взрослые'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle' 
                Label:
                    text: 'Дети'
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                Button:
                    text: 'Поиск доступных комнат'
                    font_size: 10
                    on_press:
                        root.manager.current = 'pass'
<Pass>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'vertical'
            size_hint: [1, .45]
            AnchorLayout:
                Label:
                    text: 'Бронирование'
                    padding: [20, 20]
                    valign: 'bottom'
            Button:
                text: '07 Now 2022 - 8 Now 2022, 1 Ночи'
                font_size: 12
                on_press:
                    root.manager.current = 'bron'



        AnchorLayout:
            padding: [20, 90]
            Button:
                text: 'Bron'
        GridLayout:
            size_hint: [1, .05]
            cols: 3
            rows: 1
            Button:
                text: 'Назад'
                on_press:
                    root.manager.current = 'bron'
            Widget:

            Widget:

""")


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class OurMe(Screen):
    pass


class Bron(Screen):
    pass


class Pass(Screen):
    pass


class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(OurMe(name='our me'))
        sm.add_widget(Bron(name='bron'))
        sm.add_widget(Pass(name='pass'))
        return sm


if __name__ == '__main__':
    MyApp().run()
