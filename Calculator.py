
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text="Hello",
                    pos_hint={"center_x": 0.2, "center_y": 0.5},
                    text_color= "white",
                    line_color="blue",
                ),
                MDRectangleFlatButton(
                    text="World",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    text_color= "white",
                    line_color = "white",
                ),
                MDRectangleFlatButton(
                    text="Pota",
                    pos_hint={"center_x": 0.8, "center_y": 0.5},
                    text_color="white",
                ),
            )
        )


MainApp().run()
