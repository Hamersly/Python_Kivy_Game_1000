from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import random

class RootScreen(ScreenManager):
    pass

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class GameApp(App):
    def Game_rules(self):
        file = open('Game.txt', encoding='utf8')
        return (file.read())

    def Obgon(self):
        if self.obgon != 1 and self.ochki > self.enemyochki:
            self.enemyochki += -50
            self.obgon = 1
            self.Label3_4()
        elif self.obgon != 0 and self.ochki < self.enemyochki:
            self.ochki += -50
            self.obgon = 0
            self.Label3_3()
        else:
            pass

    def Win(self):
        if self.ochki >= 1000:
            s = str(self.s1 + self.ochki)
            self.label_3 = '+  %s ' % (s)
            self.label_3_3 = 'WIN!'
        elif self.enemyochki >= 1000:
            s = str(self.s1 + self.enemyochki)
            self.label_3_2 = '+  %s ' % (s)
            self.label_3_4 = 'WIN!'
        self.s = 0
        self.s1 = 0
        self.ochki = 0
        self.enemyochki = 0
        self.bolt = 0
        self.enemybolt = 0
        self.kubiki = 5
        self.nachalo = 0
        self.enemynachalo = 0
        # self.label_1 = ''
        # self.label_2 = ''
        # self.label_3 = ''
        # self.label_3_2 = ''
        # self.label_4 = ''
        self.ochered = ''

    def New_game(self):
        self.s = 0
        self.s1 = 0
        self.ochki = 0
        self.enemyochki = 0
        self.bolt = 0
        self.enemybolt = 0
        self.kubiki = 5
        self.nachalo = 0
        self.enemynachalo = 0
        self.obgon = 2
        self.label_1 = ''
        self.label_2 = ''
        self.label_3 = ''
        self.label_3_2 = ''
        self.label_3_3 = ''
        self.label_3_4 = ''
        self.label_4 = ''
        self.ochered = random.randint(0, 1)

    s = 0
    s1 = 0
    ochki = 0
    enemyochki = 0
    bolt = 0
    enemybolt = 0
    kubiki = 5
    nachalo = 0
    enemynachalo = 0
    obgon = 2
    label_1 = ''
    label_2 = ''
    label_3 = ''
    label_3_2 = ''
    label_3_3 = ''
    label_3_4 = ''
    label_4 = ''
    ochered = random.randint(0, 1)

    def Label1(self):
        return self.label_1

    def Label2(self):
        return self.label_2

    def Label3(self):
        return self.label_3

    def Label3_2(self):
        return self.label_3_2

    def Label3_3(self):
        return self.label_3_3

    def Label3_4(self):
        return self.label_3_4

    def Label4(self):
        return self.label_4

    def Ochered(self):
        self.ochered = 1

    def R(self):
        self.label_3_3 = ''
        self.label_2 = ''
        b = []
        for i in range(self.kubiki):
            a = random.randint(1, 6)
            b.append(a)
        self.label_1 = '  '.join([str(i) for i in b])
        if b.count(1) == 1:
            self.s += 10
        elif b.count(1) == 2:
            self.s += 20
        elif b.count(1) == 3:
            self.s += 100
        elif b.count(1) == 4:
            self.s += 200
        elif b.count(1) == 5:
            self.s += 1000
        for i in range(b.count(1)):
            self.kubiki -= 1
        if b.count(2) == 3:
            self.s += 20
        elif b.count(2) == 4:
            self.s += 40
        elif b.count(2) == 5:
            self.s += 200
        if b.count(2) >= 3:
            for i in range(b.count(2)):
                self.kubiki -= 1
        if b.count(3) == 3:
            self.s += 30
        elif b.count(3) == 4:
            self.s += 60
        elif b.count(3) == 5:
            self.s += 300
        if b.count(3) >= 3:
            for i in range(b.count(3)):
                self.kubiki -= 1
        if b.count(4) == 3:
            self.s += 40
        elif b.count(4) == 4:
            self.s += 80
        elif b.count(4) == 5:
            self.s += 400
        if b.count(4) >= 3:
            for i in range(b.count(4)):
                self.kubiki -= 1
        if b.count(5) == 1:
            self.s += 5
        elif b.count(5) == 2:
            self.s += 10
        elif b.count(5) == 3:
            self.s += 50
        elif b.count(5) == 4:
            self.s += 100
        elif b.count(5) == 5:
            self.s += 500
        for i in range(b.count(5)):
            self.kubiki -= 1
        if b.count(6) == 3:
            self.s += 60
        elif b.count(6) == 4:
            self.s += 120
        elif b.count(6) == 5:
            self.s += 600
        if b.count(6) >= 3:
            for i in range(b.count(6)):
                self.kubiki -= 1
        if b == [1, 2, 3, 4, 5]:
            self.s += 125
        elif b == [2, 3, 4, 5, 6]:
            self.s += 250
        self.label_4 = ''
        a = self.s1
        self.s1 += self.s
        self.s = 0
        if a == self.s1:
            self.s1 = 0
            self.bolt += 1
            self.label_3_3 = ' Болт %s ' % (self.bolt)
            self.kubiki = 5
            s = str(self.s1)
            self.label_2 = '+  %s ' % (s)
            self.ochered = 0
            if self.bolt > 2:
                self.label_3_3 = 'Болт 3'
                self.ochki -= 50
                cb = str(self.ochki)
                self.label_3 = 'You#  %s ' % (cb)
                self.bolt = 0
                self.kubiki = 5
                s = str(self.s1)
                self.label_2 = '+  %s ' % (s)
                self.ochered = 0
            self.Enemy_bot()
        elif self.s1 + self.ochki == 555:
            self.label_4 = ' САМОСВАЛ!'
            self.ochki = 0
            cb = str(self.ochki)
            self.label_3 = 'You#  %s ' % (cb)
            self.s = 0
            self.s1 = 0
            self.kubiki = 5
            s = str(self.s1)
            self.label_2 = '+  %s ' % (s)
        s = str(self.s1)
        self.label_2 = '+  %s ' % (s)

        if self.kubiki == 0:
            self.kubiki = 5

    def Pas(self):
        if self.s1!=0:
            self.Obgon()
            if 0 <= (self.ochki + self.s1) < 50 and self.nachalo == 0:
                self.label_4 = 'Необходимо набрать не менее 50'
            else:
                self.nachalo = 1
                if 200 <= self.ochki <= 300 and self.ochki + self.s1 < 300:
                    self.label_4 = 'Доберись до 300.'
                elif 600 <= self.ochki <= 700 and self.ochki + self.s1 < 700:
                    self.label_4 = 'Доберись до 700.'
                elif 880 <= self.ochki and self.ochki + self.s1 < 1000:
                    self.label_4 = 'Набери 1000 !'
                else:
                    self.ochki += self.s1
                    self.s1 = 0
                    self.s = 0
                    if self.ochki >= 1000:
                        self.Win()
                    elif 200 <= self.ochki < 300:
                        c = str(self.ochki)
                        d = 'You:#  %s' % (c)
                        self.label_3 = d
                        self.label_3_3 = 'БОЧКА!'
                        self.label_2 = '0'
                        self.kubiki = 5
                        # self.bolt = 0
                    elif 600 <= self.ochki < 700:
                        c = str(self.ochki)
                        d = 'You:#  %s' % (c)
                        self.label_3 = d
                        self.label_3_3 = 'БОЧКА!'
                        self.label_2 = '0'
                        self.kubiki = 5
                        # self.bolt = 0
                    elif 880 <= self.ochki < 1000:
                        c = str(self.ochki)
                        d = 'You:#  %s' % (c)
                        self.label_3 = d
                        self.label_3_3 = 'БОЧКА!'
                        self.label_2 = '0'
                        self.kubiki = 5
                        # self.bolt = 0
                    else:
                        c = str(self.ochki)
                        d = 'You:#  %s  ' % (c)
                        self.label_3 = d
                        self.label_2 = '0'
                        self.kubiki = 5
                    self.ochered = 0
        else:
            pass

    def Enemy_R(self):
        self.label_3_4 = ''
        b = []
        for i in range(self.kubiki):
            a = random.randint(1, 6)
            b.append(a)
        self.label_1 = '  '.join([str(i) for i in b])
        if b.count(1) == 1:
            self.s += 10
        elif b.count(1) == 2:
            self.s += 20
        elif b.count(1) == 3:
            self.s += 100
        elif b.count(1) == 4:
            self.s += 200
        elif b.count(1) == 5:
            self.s += 1000
        for i in range(b.count(1)):
            self.kubiki -= 1
        if b.count(2) == 3:
            self.s += 20
        elif b.count(2) == 4:
            self.s += 40
        elif b.count(2) == 5:
            self.s += 20
        if b.count(2) >= 3:
            for i in range(b.count(2)):
                self.kubiki -= 1
        if b.count(3) == 3:
            self.s += 30
        elif b.count(3) == 4:
            self.s += 60
        elif b.count(3) == 5:
            self.s += 300
        if b.count(3) >= 3:
            for i in range(b.count(3)):
                self.kubiki -= 1
        if b.count(4) == 3:
            self.s += 40
        elif b.count(4) == 4:
            self.s += 80
        elif b.count(4) == 5:
            self.s += 400
        if b.count(4) >= 3:
            for i in range(b.count(4)):
                self.kubiki -= 1
        if b.count(5) == 1:
            self.s += 5
        elif b.count(5) == 2:
            self.s += 10
        elif b.count(5) == 3:
            self.s += 50
        elif b.count(5) == 4:
            self.s += 100
        elif b.count(5) == 5:
            self.s += 500
        for i in range(b.count(5)):
            self.kubiki -= 1
        if b.count(6) == 3:
            self.s += 60
        elif b.count(6) == 4:
            self.s += 120
        elif b.count(6) == 5:
            self.s += 600
        if b.count(6) >= 3:
            for i in range(b.count(6)):
                self.kubiki -= 1
        if b == [1, 2, 3, 4, 5]:
            self.s += 125
        elif b == [2, 3, 4, 5, 6]:
            self.s += 250
        self.label_4 = ''
        a = self.s1
        self.s1 += self.s
        self.s = 0
        if a == self.s1:
            self.s1 = 0
            self.enemybolt += 1
            self.label_3_4 = ' Болт %s ' % (self.enemybolt)
            self.kubiki = 5
            s = str(self.s1)
            self.label_2 = '+  %s ' % (s)
            if self.enemybolt > 2:
                self.label_3_4 = 'Болт 3'
                self.enemyochki -= 50
                cb = str(self.enemyochki)
                self.label_3_2 = 'Bot:#  %s ' % (cb)
                self.enemybolt = 0
                self.kubiki = 5
                s = str(self.s1)
                self.label_2 = '+  %s ' % (s)
            self.ochered = 1
        elif self.s1 + self.enemyochki == 555:
            self.label_3_4 = ' САМОСВАЛ!'
            self.enemyochki = 0
            cb = str(self.enemyochki)
            self.label_3 = 'Bot  #%s ' % (cb)
            self.s = 0
            self.s1 = 0
            self.kubiki = 5
            s = str(self.s1)
            self.label_2 = '+  %s ' % (s)
            self.ochered = 1
            self.enemybolt = 0
        else:
            s = str(self.s1)
            self.label_2 = '+  %s ' % (s)
        if self.kubiki == 0:
            self.kubiki = 5

    def Enemy_Pas(self):
        self.Obgon()
        self.enemyochki += self.s1
        self.s1 = 0
        self.s = 0
        if self.enemyochki >= 1000:
            self.Win()
        elif 200 <= self.enemyochki < 300:
            enemy_c = str(self.enemyochki)
            enemy_d = 'Bot:#  %s' % (enemy_c)
            self.label_3_2 = enemy_d
            self.label_3_4 = 'БОЧКА!'
            self.label_2 = '0'
            self.kubiki = 5
        elif 600 <= self.enemyochki < 700:
            enemy_c = str(self.enemyochki)
            enemy_d = 'Bot:#  %s' % (enemy_c)
            self.label_3_2 = enemy_d
            self.label_3_4 = 'БОЧКА!'
            self.label_2 = '0'
            self.kubiki = 5
        elif 880 <= self.enemyochki < 1000:
            enemy_c = str(self.enemyochki)
            enemy_d = 'Bot:#  %s' % (enemy_c)
            self.label_3_2 = enemy_d
            self.label_3_4 = 'БОЧКА!'
            self.label_2 = '0'
            self.kubiki = 5
        else:
            c = str(self.ochki)
            d = 'You:#  %s  ' % (c)
            self.label_3 = d
            enemy_c = str(self.enemyochki)
            enemy_d = 'Bot:#  %s  ' % (enemy_c)
            self.label_3_2 = enemy_d
            self.label_2 = '0'
            self.kubiki = 5

    def Enemy_bot(self):
        if self.ochered == 0:
            if 0 <= self.enemyochki < 50 and self.enemynachalo == 0:
                while (self.enemyochki + self.s1) <= 50 and self.ochered == 0:
                    self.Enemy_R()
                    self.Label1()
                    self.Label2()
                    self.Label3_2()
                    self.Label3_4()
                    self.Label4()
                self.Enemy_Pas()
            elif 200 <= self.enemyochki < 300:
                while (self.enemyochki + self.s1) <= 300 and self.ochered == 0:
                    self.Enemy_R()
                    self.Label1()
                    self.Label2()
                    self.Label3_2()
                    self.Label3_4()
                    self.Label4()
                self.Enemy_Pas()
            elif 600 <= self.enemyochki < 700:
                while (self.enemyochki + self.s1) <= 700 and self.ochered == 0:
                    self.Enemy_R()
                    self.Label1()
                    self.Label2()
                    self.Label3_2()
                    self.Label3_4()
                    self.Label4()
                self.Enemy_Pas()
            elif 880 <= self.enemyochki < 1000:
                while (self.enemyochki + self.s1) <= 1000 and self.ochered == 0:
                    self.Enemy_R()
                    self.Label1()
                    self.Label2()
                    self.Label3_2()
                    self.Label3_4()
                    self.Label4()
                self.Enemy_Pas()
            else:
                self.Enemy_R()
                self.Label1()
                self.Label2()
                self.Label3_2()
                self.Label3_4()
                self.Label4()
                a = int()
                while a == 0:
                    a = random.randint(0, 1)
                    if a == 0:
                        self.Enemy_R()
                        self.Label1()
                        self.Label2()
                        self.Label3_2()
                        self.Label3_4()
                        self.Label4()
                self.Enemy_Pas()
        else:
            pass

    def build(self):
        return RootScreen()

if __name__ == '__main__':
    GameApp().run()
