import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock


class ContagemRegressivaApp(App):
    def build(self):
        self.layout = Label(text="10", font_size=72)
        self.contador = 10

        Clock.schedule_interval(self.atualizar_contador, 1)

        return self.layout

    def atualizar_contador(self, dt):
        self.contador -= 1

        if self.contador < 0:
            self.contador = 0
            Clock.unschedule(self.atualizar_contador)

        self.layout.text = str(self.contador)

if __name__ == "__main__":
    ContagemRegressivaApp().run()






'''
import json

def create_dialogs():
    try:
        with open('dialogs.json', 'r') as d:
            a = json.load(d)
            print(a)
    except:
        with open('dialogs.json', 'w') as d:
            dialog = {'Co': 'Aqui voce vai aprender os prmeiros passos para começar no Marketing Digital e conquistar o primeiro 10k.\n\nSelecione um estágio abaixo para começar',
             'Au': "Tudo O que voce precisa saber para o seu desenvolvimento pesssoal para impulsionar o teu performance no Marketing Digital",
             'Es': 'Aprenda estrategias de venda selecionando um dos estagios abaixo:', 'Cr': 'Aprenda a criar conteudos com especialistas:',
             'Or': 'Fazendo o seu orcamento de trafego pago', 'Fa': 'Do que voce esta a espera?\nAprenda a fazer a fazer vendas logo.',
             'Tr': 'Trafego organico, vem connosco', 'Fu': 'Tudo sobre funis, agora'}
            json.dump(dialog, d)


create_dialogs()

'''

'''
<StageSelectPopup>:
    id: 'popup'
    size_hint: 0.9, 0.4
    
    MDRelativeLayout:
        orientation: 'vertical'
        pos_hint: {'x': 0.5, 'y': 0}
        size_hint: None, None
        width: root.width
        height: root.height
        Label:
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            #size_hint_y: 1.4
            text: "Este ee o text"

        MDBoxLayout:
            pos_hint: {'center_x': 0.5}
            size_hint_y: 0.2
            size_hint_x: None
            width: self.minimum_width
            spacing: '10dp'
            MDRaisedButton:
                text: "Estagio 1"
                on_release: app.root.current = 'startingmd'
                #pos_hint: {'bottom_x': 1, 'center_y': 1}
            MDRaisedButton:
                text: "Estagio 2"
                pos_hint_x: 
            MDRaisedButton:
                text: "Estagio 3"
                
    '''