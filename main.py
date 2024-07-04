from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.button import MDRectangleFlatButton, MDFloatingActionButton
from kivy.uix.popup import Popup
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.dialog import MDDialog
from kivy.animation import Animation
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.clock import Clock
from kivy.properties import StringProperty, ColorProperty, NumericProperty
from kivy.clock import Clock
import json
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("gpsdezk.kv")

class MenuComponent(MDRelativeLayout):
    #bkg_color = StringProperty("#87CEFA")
    img = StringProperty("")

class FAB(MDFloatingActionButton):
    bg_normal_color = StringProperty("#87CEFA")
    blocked_color = StringProperty("#808080")
    num_level = NumericProperty(1)
    btn_level = NumericProperty(0)

    '''
    btn_level - indicates the idex o the button to facilitate
    the the request of information on the dialogs dictionare
    based on the stage.

    num_level - indiacates the number of button acorrding to the total of levels
    '''
    pass

class Menu(Screen):
    dialogs = {'Co': [['playing.mp4','Aqui você vai aprender os primeiros passos para começar no Marketing Digital e conquistar o primeiro 10k.\n\nO Marketing Digital é todo o conjunto de técnicas usadas para convencer e vender por meio da internet...'],
                      ['10k.mp4', 'Segundo estágio de como começar no marketing digital'],
                      ['playing.mp4', 'Terceiro estágio de como começar no marketing digital']],
             'Au': [['10k.mp4',"Tudo O que você precisa saber para o seu desenvolvimento pessoal para impulsionar o teu performance no Marketing Digital, vai aprender aqui"],
                    ['playing.mp4',
                     'O alho, tempero milenar com aroma inconfundível e sabor marcante, transcende a mera culinária para se consagrar como um ingrediente essencial na cultura gastronômica global.\n\nMais do que um simples condimento, o alho ostenta propriedades medicinais e fitoterápicas há muito reconhecidas, tecendo um elo profundo entre saúde, bem-estar e sabor.'],
                    [['10k.mp4',"Ultimo estagio de auto-desenvolvimento"]]],
             'Es': 'As estrategias de venda que muitos especilista do mercado usam sao as que vais aprende agora:',
             'Cr': 'Aprenda a criar conteudos com especialistas:',
             'Or': 'Fazendo o seu orcamento de trafego pago',
             'Fa': 'Do que voce esta a espera?\nAprenda a fazer vendas logo.',
             'Tr': 'Trafego organico, vem connosco',
             'Fu': 'Tudo sobre funis, agora'}
    List = []

    def printer(self, instance, b):
        Clock.unschedule(self.breath, 1)

    def on_enter(self, *args):
        try:
            with open('level.json', 'r') as current_lvl:
                lvl = json.load(current_lvl)
                self.target = self.ids[f"btn{lvl}"]

        except:
            pass
        Clock.schedule_interval(self.breath, 1)        

        self.scroll = self.ids.menu_scroll
        self.scroll.bind(on_scroll_move=self.printer)

    def on_pre_leave(self, *args):
        Clock.unschedule(self.breath, 1)

    def check_acess(self):
        pass

    def breath(self, obj):
        anim = Animation(size_hint=(0.11,0.11), t='in_quad', duration = .5) + Animation(size_hint=(0.1, 0.1), t='in_quad', duration = .5)
        anim.start(self.target)
    
    def select_stage(self, texto):
        category = self.dialogs[texto[0:2]]
        btn1 = MDRectangleFlatButton(text = 'Estagio 1')
        btn1.bind(on_release= lambda x: self.call_screen(x, 'lectures'))
        btn2 = MDRectangleFlatButton(text= 'Estagio 2')
        btn3 = MDRectangleFlatButton(text='Estagio 2')
        self.dialog = MDDialog(title= texto, text = category, radius = (20,0,20,0), buttons=[btn1, btn2, btn3])
        #self.List.append()
        #print(self.dialogs.keys())
        self.dialog.open()

    def call_screen(self, obj, choice):
        self.manager.current = choice
        self.dialog.dismiss()

class LectureScreen(Screen):
    topic = StringProperty('')
    vid_source = StringProperty('')
    current_level = NumericProperty(0)
    thumbnail = StringProperty('')

    #def on_end(self, instance, value):
        #if self.video.position == self.video.duration:
            #print('end of game')
            #pass

    #def on_enter(self, *args):
        #self.video = self.ids.videoplayer
        #self.video.bind(position=self.on_end)

    def on_pre_leave(self, *args):
        self.ids.videoplayer.state = "stop"

class ChatScreen(Screen):
    pass
        
class GpsDezk(MDApp):
    Level = NumericProperty(1)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            with open('level.json', 'r') as lvl:
                self.Level = json.load(lvl)

        except:
            with open('level.json', 'w') as lvl:
                json.dump(self.Level, lvl)
        

    def check_elegibility(self, btn_number, topic, btn_lvl):
        if btn_number <= self.Level:
            self.open_and_show_lecture(topic, btn_number, btn_lvl)
            

        else:
            self.dialog = MDDialog(title = "Acesso não autorizado",
                                   text = f'Deve terimar o nivel {btn_number-1} antes de iniciar este nivel'
                                   , radius = (20,7,20,7))
            self.dialog.open()

    def open_and_show_lecture(self, topic, btn_number, btn_level):
        self.sm.remove_widget(self.lecturescreen)
        self.lecturescreen = LectureScreen(
            name="lectures", topic="", vid_source="")
        self.sm.add_widget(self.lecturescreen)

        self.lecturescreen.topic = topic
        self.lecturescreen.current_level = btn_number
        self.lecturescreen.thumbnail = 'feature_graphic.png'
    

        for i in self.home.dialogs.keys():
            if topic[0:2] == i:
                self.lecturescreen.vid_source = self.home.dialogs[i][btn_level][0]
                self.lesson_description = MDLabel(adaptive_height = True,
                                                  halign='justify', valign='top')
                self.lesson_description.text = self.home.dialogs[i][btn_level][1]
                
                self.lesson_container = self.lecturescreen.ids.content_container
                self.lesson_container.add_widget(self.lesson_description)
                break

        self.sm.current = 'lectures'

    def level_update(self, current_lvl):
        
        if current_lvl == self.Level:
            with open('level.json', 'w') as old_lvl:
                self.Level +=1
                json.dump(self.Level, old_lvl)
                
        self.sm.current = 'menu'

    def back_home(self):
        self.sm.current = 'menu'

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.sm = ScreenManager(transition=NoTransition())
        self.home = Menu(name="menu")
        self.sm.add_widget(self.home)

        self.lecturescreen = LectureScreen(name='lectures')
        self.sm.add_widget(self.lecturescreen)

        return self.sm

'''
s ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 
 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 
 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
'''

if __name__=='__main__':
    GpsDezk().run()