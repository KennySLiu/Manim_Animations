from manim import *


class Register(VGroup):
    def __init__(self, h=0.8, w=0.8, txt=""):
        super().__init__()
        self.databox = RectTxt(txt=txt, h=h, w=w)
        self.downstream_register = None

        self.active_data = None
        self.next_data = None
        self.add(self.databox)

    def set_active_data(self, newdata):
        if (self.active_data is not None):
            raise AssertionError("active data is already set.")

        self.active_data = newdata 
        self.add(self.active_data)

    def update_next_data(self, next_data):
        self.next_data = next_data

    def set_downstream_register(self, ds_reg):
        self.downstream_register = ds_reg

    def clock_tick(self):
        if ( (self.downstream_register is not None) and
            (self.active_data is not None)
        ):
            self.active_data.move_to(self.downstream_register.get_rect().get_center())
            self.downstream_register.update_next_data( self.active_data )

        if (self.active_data is not None):
            self.remove( self.active_data )

        self.active_data = self.next_data

        if (self.active_data is not None):
            self.add(self.active_data)

        if (self.downstream_register is not None):
            self.downstream_register.clock_tick()

    def get_rect(self):
        return self.databox

    def move_to(self, coords):
        self.databox.move_to(coords)




class FIFO(VGroup):
    def __init__(self, fifo_depth=3):
        super().__init__()
        self.head_coords = (0, 0, 0)
        self.fifo_depth = fifo_depth
        self.fifo = [Register(txt="") for i in range(0,fifo_depth)]

        self.fifo[0].move_to( (-2, -1, 0) )
        for i in range(0, self.fifo_depth-1):
            self.fifo[i].set_downstream_register(
                            self.fifo[i+1]
            )
            self.fifo[i+1].next_to( self.fifo[i].get_rect(), RIGHT, buff=0 )

        for i in range(0, self.fifo_depth):
            self.add( self.fifo[i] )


    def insert_head(self, data):
        self.clock_tick()
        data.move_to(self.head_coords)
        self.fifo[0].set_active_data(data)


    def clock_tick(self):
        self.fifo[0].clock_tick()


    def move_to(self, coords):
        self.head_coords = coords
        self.fifo[0].move_to(self.head_coords)
        for i in range(0, self.fifo_depth-1):
            self.fifo[i+1].next_to( self.fifo[i].get_rect(), RIGHT, buff=0 )





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

    def move_to(self, coords):
        self.circle.move_to(coords)
        self.txt.move_to(coords)


