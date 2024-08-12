from manim import *



class tmptester(VGroup):
    def __init__(self):
        super().__init__()
        self.objs = []

    def add_cir(self, data):
        self.objs.append(CircTxt(data, radius=0.3))
        self.add(self.objs[-1])

    def add_rec(self, data):
        self.objs.append(RectTxt(data, h=0.8, w=0.8))
        self.add(self.objs[-1])

    def move_last_obj(self, coords):
        self.objs[-1].move_to(coords)


class FIFO_pkt(VGroup):
    def __init__(self, txt, color, opacity=0.8, fifo_idx=0):
        super().__init__()
        self.pkt = CircTxt(txt, radius=0.3)
        self.fifo_idx = 0
        self.add(self.pkt)
        self.pkt.set_fill(color, opacity=opacity)
        self.pkt.txtcolor(WHITE, txtopacity=1)

    def move_to(self, coords):
        self.pkt.move_to(coords)



class FIFO_boxes(VGroup):
    def __init__(self, fifo_depth=3):
        super().__init__()
        self.head_coords = (-2,-1,0)
        self.fifo_depth = fifo_depth
        self.boxes = [RectTxt(txt="",h=1.0,w=1.0)
                            for i in range(0,fifo_depth)
        ]

        self.boxes[0].move_to( self.head_coords )
        for i in range(0, self.fifo_depth-1):
            self.boxes[i].set_downstream_register(
                            self.boxes[i+1]
            )
            self.boxes[i+1].next_to( self.boxes[i].get_rect(), RIGHT, buff=0 )

        for i in range(0, self.fifo_depth):
            self.add( self.boxes[i] )


    def move_to(self, coords):
        self.head_coords = coords
        self.boxes[0].move_to(self.head_coords)
        for i in range(0, self.fifo_depth-1):
            self.boxes[i+1].next_to( self.boxes[i].get_rect(), RIGHT, buff=0 )





class RectTxt(VGroup):
    def __init__(self, txt, h=0.8, w=1.8, txt_offset=(0,0,0)):
        super().__init__()
        self.txtidx = 0
        self.txt = Text(txt)
        self.txt_offset = txt_offset
        self.rect = Rectangle(height=h, width=w)
        self.txt.add_updater(lambda m : m.move_to(self.rect.get_center() + self.txt_offset))
        self.add(self.rect, self.txt)

    def change_content(self, txt):
        self.remove(self.txt)
        self.txt = Text(txt)
        self.txt.add_updater(lambda m : m.move_to(self.rect.get_center() + self.txt_offset))
        self.add(self.txt)

    def get_rect(self):
        return self.rect

    def get_center(self):
        return self.rect.get_center()

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
        #self.txt.add_updater(lambda m : m.move_to(self.circle.get_center()))
        self.add(self.circle, self.txt)

    def move_to(self, coords):
        self.circle.move_to(coords)
        self.txt.move_to( (coords[0], coords[1], coords[2]+1) )

    def txtcolor(self, txtcolor, txtopacity):
        self.txt.set_fill(color=txtcolor, opacity=txtopacity)


