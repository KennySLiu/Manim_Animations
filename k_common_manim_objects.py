from manim import *

class RectTxt(VGroup):
    def __init__(self, txt, h=0.8, w=1.8):
        super().__init__()
        self.txtidx = 0
        self.txt = Text(txt)
        self.rect = Rectangle(height=h, width=w)
        self.txt.add_updater(lambda m : m.move_to(self.rect.get_center()))
        self.add(self.rect, self.txt)

    def change_content(self, txt):
        self.remove(self.txt)
        self.txt = Text(txt)
        self.txt.add_updater(lambda m : m.move_to(self.rect.get_center()))
        self.add(self.txt)

    def get_rect(self):
        return self.rect

    def change_color(self, color, opacity):
        self.rect.set_fill(color, opacity=opacity)

    def change_fill(self, opacity):
        self.rect.set_fill(WHITE, opacity=opacity)



### REFERENCE: https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html, search for "CircleWithContent"
class CircTxt(VGroup):
    def __init__(self, txt, radius=0.4):
        super().__init__()
        self.txt = Text(txt)
        self.circle = Circle(radius=radius)
        self.txt.add_updater(lambda m : m.move_to(self.circle.get_center()))
        self.add(self.circle, self.txt)


