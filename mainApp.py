import math
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem

Window.size = (500, 700)


class ContentDialog(BoxLayout):
    pass


class Content(BoxLayout):
    pass


class HomeScreen(Screen):
    pass


class Quadratic(Screen):

    def store(self, equation):
        try:
            self.a = ''
            self.b = ''
            self.c = ''
            out = str(equation).split(",")
            self.a = int(out[0])
            self.b = int(out[1])
            self.c = int(out[2])

        except Exception:
            self.quadEntry.text = ""

    def quadCalc(self, a, b, c):
        try:
            self.eval = f"{a}x² + {b}x + {c}"
            self.discri = (self.b*self.b)-(4*self.a * self.c)
            if self.discri >= 0:
                self.sol1 = (((-self.b) + math.sqrt(self.discri)) / (2 * self.a))
                self.sol2 = (((-self.b) - math.sqrt(self.discri)) / (2 * self.a))
                self.first.text = f"{-self.sol1}"
                self.second.text = f"{-self.sol2}"
                self.second.cursor = (1, 1)

            else:
                show = mainApp().show_root_error()
                show()
                self.quadEntry.text = ""

        except Exception:
            self.quadEntry.text = ""


class BasicCalculator(Screen):

    def round(self, num):
        try:
            base = num[7]
            num = num[0:7]
            if int(base) >= 5:
                new = int(num) + 1
                return str(new)
            else:
                return num
        except Exception:
            return num

    def limitoutput(self, output):
        try:
            out = str(output).split(".")
            tens = out[0]
            dec = out[1]
            dec = self.round(dec)
            self.display.text = tens + "." + dec
        except Exception:
            return output

    def calculate(self, equation):
        if equation:
            try:
                self.display.text = str(eval(equation))
            except Exception:
                self.display.text = "Error"

    def retrieve(self, history):
        self.historyID.text = history


class BMI(Screen):
    pass


sm = ScreenManager(transition=SwapTransition())
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(Quadratic(name='quad'))
sm.add_widget(BasicCalculator(name='basic'))
sm.add_widget(BMI(name='bmi'))


class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class mainApp(MDApp):
    dialog = None

    def show_root_error(self):
        self.theme_cls.theme_style = "Dark"
        if not self.dialog:
            self.dialog = MDDialog(
                title="Error",
                text="The roots are imaginary. Try again.",
                buttons=[
                    MDRaisedButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color="white",
                        md_bg_color="#b2173a",
                        on_release=self.hide_dialog
                    )
                ],
            )
            self.dialog.open()

    def show_rgb_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="This feature is yet to be added.",
                buttons=[
                    MDRaisedButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color="white",
                        md_bg_color="#b2173a",
                        on_release=self.hide_dialog
                    )
                ],
            )
            self.dialog.open()

    def hide_dialog(self, obj):
        self.dialog.dismiss()

    def build(self):
        self.icon = 'logo.png'
        self.theme_cls.theme_style = "Dark"
        return


mainApp().run()
