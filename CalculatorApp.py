from kivy.app import App
from kivy.uix.widget import Widget


class Windows(Widget):

    def calculate(self, equation):
        if equation:
            try:
                self.display.text = str(eval(equation))
            except Exception:
                self.display.text = "Invalid output"

    def retrieve(self, history):
        self.historyID.text = history


class CalculatorApp(App):
    def build(self):
        return Windows()


CalculatorApp().run()
