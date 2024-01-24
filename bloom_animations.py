from manim import *
import random
random.seed(3)

"""
HELPFUL TUTORIAL: https://www.youtube.com/watch?v=KHGoFDB-raE
SOME LINKS:
    - Quickstart: https://docs.manim.community/en/stable/tutorials/quickstart.html
    - A Deep Dive: https://docs.manim.community/en/stable/guides/deep_dive.html#adding-mobjects-to-the-scene
    - MOBJECTS documentation: https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html
"""

BV_LEN = 15
NUM_HASH = 3

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

    def change_fill(self):
        self.rect.set_fill(WHITE, opacity=0.4)



### REFERENCE: https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html, search for "CircleWithContent"
class CircTxt(VGroup):
    def __init__(self, txt, radius=0.4):
        super().__init__()
        self.txt = Text(txt)
        self.circle = Circle(radius=radius)
        self.txt.add_updater(lambda m : m.move_to(self.circle.get_center()))
        self.add(self.circle, self.txt)





class BitVector(VGroup):
    def __init__(self):
        super().__init__()
        self.b = [
            RectTxt("0", h=0.8, w=0.8) for i in range(0, BV_LEN)
        ]

        self.b[0].move_to((-5, -2.5, 0))
        for i in range(1, BV_LEN):
            self.b[i].next_to(self.b[i-1].get_rect(), RIGHT, buff=0)

        for i in range(BV_LEN):
            self.add(self.b[i])

    def change_idx(self, idx, txt):
        self.b[idx].change_content(txt)
        self.b[idx].change_fill()

    def get_idx(self, idx):
        return self.b[idx]





class test(Scene):
    def construct(self):

        input_data = RectTxt("data1")
        input_data.move_to((0, 2, 0))
        
        ### Drawing hash functions
        hashes = [CircTxt("#") for i in range(0, NUM_HASH)]
        hashes[0].set_fill(BLUE, opacity=0.2)
        hashes[1].set_fill(RED, opacity=0.2)
        hashes[2].set_fill(GREEN, opacity=0.2)
        hashes[0].move_to((-1, 0.5, 0))
        hashes[1].move_to(( 0, 0.5, 0))
        hashes[2].move_to(( 1, 0.5, 0))



        ### Drawing lines from data -> hash functions
        d2h_lines = []
        for i in range(0, NUM_HASH):
            d2h_lines.append(
                Line(start = input_data.get_bottom(),
                     end=hashes[i].get_top(),
                     buff=0,
                ).add_tip()
            )

        bitvect = BitVector()


        self.play(  Create(input_data),
                    Create(hashes[0]),
                    Create(hashes[1]),
                    Create(hashes[2]),
                    Create(bitvect),
                    Create(d2h_lines[0]),
                    Create(d2h_lines[1]),
                    Create(d2h_lines[2])
        )
        self.wait()

        ###########################
        ### POPULATE BV, INPUT 1
        ###########################

        arrows = []
        bv_idces = []
        for i in range(0, NUM_HASH):
            bv_idces.append(random.randrange(0, BV_LEN))
            arrows.append(Line(start = hashes[i].get_bottom(), 
                               end=bitvect.get_idx(bv_idces[i]).get_top(),
                               buff=0
                          ).add_tip()
            )

        for i in range(0, NUM_HASH):
            self.play(  Create(arrows[i]),
                        bitvect.animate.change_idx(bv_idces[i], "1")
            )

        self.play(  FadeOut(arrows[0]),
                    FadeOut(arrows[1]),
                    FadeOut(arrows[2]),
                    input_data.animate.change_content("data2")
        )





        ###########################
        ### POPULATE BV, INPUT 2
        ###########################

        arrows = []
        bv_idces = []
        for i in range(0, NUM_HASH):
            bv_idces.append(random.randrange(0, BV_LEN))
            arrows.append(Line(start = hashes[i].get_bottom(), 
                               end=bitvect.get_idx(bv_idces[i]).get_top(), 
                               buff=0
            ))

        for i in range(0, NUM_HASH):
            self.play(  Create(arrows[i]),
                        bitvect.animate.change_idx(bv_idces[i], "1")
            )

        self.play(  FadeOut(arrows[0]),
                    FadeOut(arrows[1]),
                    FadeOut(arrows[2])
        )







        self.wait()


