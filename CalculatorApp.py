from kivymd.app import MDApp
from kivy.uix.widget import Widget


class Windows(Widget):

    def calculate(self, equation):
        if equation:
            try:
                self.display.text = str(eval(equation))
            except Exception:
                self.display.text = "Invalid output"


class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.3
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Windows()

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


CalculatorApp().run()
