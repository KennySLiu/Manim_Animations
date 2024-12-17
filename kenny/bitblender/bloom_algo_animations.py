from manim import *
import k_common_manim_objects as kmobjs
import random
random.seed(3)

BV_LEN = 15
NUM_HASH = 3

############################
############################
### NOTE: CALL THIS BY USING:
### manim -pql $(filename).py insertions
### manim -pql $(filename).py queries
############################
############################


"""
HELPFUL TUTORIAL: https://www.youtube.com/watch?v=KHGoFDB-raE
SOME LINKS:
    - Quickstart: https://docs.manim.community/en/stable/tutorials/quickstart.html
    - A Deep Dive: https://docs.manim.community/en/stable/guides/deep_dive.html#adding-mobjects-to-the-scene
    - MOBJECTS documentation: https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html
"""




class BitVector(VGroup):
    def __init__(self):
        super().__init__()
        self.b = [
            kmobjs.RectTxt("0", h=0.8, w=0.8) for i in range(0, BV_LEN)
        ]

        self.b[0].move_to((-5, -2.5, 0))
        for i in range(1, BV_LEN):
            self.b[i].next_to(self.b[i-1].get_rect(), RIGHT, buff=0)

        for i in range(BV_LEN):
            self.add(self.b[i])

    def change_idx(self, idx, txt):
        self.b[idx].change_content(txt)
        self.b[idx].change_fill(0.4)

    def get_idx(self, idx):
        return self.b[idx]

    def change_position(self, pos):
        self.b[0].move_to(pos)
        for i in range(1, BV_LEN):
            self.b[i].next_to(self.b[i-1].get_rect(), RIGHT, buff=0)




class test(Scene):
    def construct(self):
        bv = BitVector()

        self.play(
            bv.animate.change_position( (-1, 2, 3) )
        )



class insertions(Scene):
    def construct(self):

        input_data = kmobjs.RectTxt("data1")
        input_data.move_to((0, 2, 0))

        ### Drawing hash functions
        hashes = [kmobjs.CircTxt("#") for i in range(0, NUM_HASH)]
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
                        ).add_tip()
            )

        for i in range(0, NUM_HASH):
            self.play(  Create(arrows[i]),
                        bitvect.animate.change_idx(bv_idces[i], "1")
            )

        self.play(  FadeOut(arrows[0]),
                    FadeOut(arrows[1]),
                    FadeOut(arrows[2])
        )

        self.wait()









class queries(Scene):
    def construct(self):

        input_data = kmobjs.RectTxt("query1", h=0.8, w=2.5)
        input_data.move_to((0, 3, 0))
        aggregate = kmobjs.RectTxt("AND")
        aggregate.move_to((-2, -3, 0))
        resultbox = kmobjs.RectTxt("")
        resultbox.move_to((2, -3, 0))
        resultbox.change_color(BLUE, 0.4)

        ### Drawing hash functions
        hashes = [kmobjs.CircTxt("#") for i in range(0, NUM_HASH)]
        hashes[0].set_fill(BLUE, opacity=0.2)
        hashes[1].set_fill(RED, opacity=0.2)
        hashes[2].set_fill(GREEN, opacity=0.2)
        hashes[0].move_to((-1, 1.5, 0))
        hashes[1].move_to(( 0, 1.5, 0))
        hashes[2].move_to(( 1, 1.5, 0))



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

        bitvect.change_position((-5, -1, 0))
        bitvect.change_idx(1, "1")
        bitvect.change_idx(2, "1")
        bitvect.change_idx(4, "1")
        bitvect.change_idx(7, "1")
        bitvect.change_idx(12, "1")
        bitvect.change_idx(13, "1")

        self.play(  Create(input_data),
                    Create(hashes[0]),
                    Create(hashes[1]),
                    Create(hashes[2]),
                    Create(bitvect),
                    Create(d2h_lines[0]),
                    Create(d2h_lines[1]),
                    Create(d2h_lines[2]),
                    Create(aggregate),
                    Create(resultbox)
        )
        self.wait()

        ###########################
        ### QUERY BV, #1
        ###########################

        result_arrow = Line(start = aggregate.get_right(),
                            end = resultbox.get_left(),
                            buff=0
                        ).add_tip()
        hash2bv_arrows = []
        bv2agg_arrows = []
        bv_idces = [1, 4, 12]

        for i in range(0, NUM_HASH):
            hash2bv_arrows.append(Line(start = hashes[i].get_bottom(),
                               end=bitvect.get_idx(bv_idces[i]).get_top(),
                               buff=0
                          ).add_tip()
            )
            bv2agg_arrows.append(Line(start = bitvect.get_idx(bv_idces[i]).get_bottom(),
                               end=aggregate.get_top(),
                               buff=0
                          ).add_tip()
            )

        for i in range(0, NUM_HASH):
            self.play(  Create(hash2bv_arrows[i]),
                        Create(bv2agg_arrows[i]),
            )

        self.play(  Create(result_arrow),
                    resultbox.animate.change_content("1")
        )

        self.play(  FadeOut(hash2bv_arrows[0]),
                    FadeOut(hash2bv_arrows[1]),
                    FadeOut(hash2bv_arrows[2]),
                    FadeOut(bv2agg_arrows[0]),
                    FadeOut(bv2agg_arrows[1]),
                    FadeOut(bv2agg_arrows[2]),
                    FadeOut(result_arrow),
                    input_data.animate.change_content("query2")
        )


        ###########################
        ### QUERY BV, #2
        ###########################

        result_arrow = Line(start = aggregate.get_right(),
                            end = resultbox.get_left(),
                            buff=0
                        ).add_tip()
        hash2bv_arrows = []
        bv2agg_arrows = []
        bv_idces = [4, 10, 13]
        for i in range(0, NUM_HASH):
            hash2bv_arrows.append(Line(start = hashes[i].get_bottom(),
                               end=bitvect.get_idx(bv_idces[i]).get_top(),
                               buff=0
                          ).add_tip()
            )
            bv2agg_arrows.append(Line(start = bitvect.get_idx(bv_idces[i]).get_bottom(),
                               end=aggregate.get_top(),
                               buff=0
                          ).add_tip()
            )

        for i in range(0, NUM_HASH):
            self.play(  Create(hash2bv_arrows[i]),
                        Create(bv2agg_arrows[i]),
            )

        self.play(  Create(result_arrow),
                    resultbox.animate.change_content("0")
        )

        self.play(  FadeOut(hash2bv_arrows[0]),
                    FadeOut(hash2bv_arrows[1]),
                    FadeOut(hash2bv_arrows[2]),
                    FadeOut(bv2agg_arrows[0]),
                    FadeOut(bv2agg_arrows[1]),
                    FadeOut(bv2agg_arrows[2]),
                    FadeOut(result_arrow)
        )

        self.wait()


