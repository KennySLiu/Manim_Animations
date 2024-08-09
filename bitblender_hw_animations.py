from manim import *
import k_common_manim_objects as kmobjs
import random
random.seed(3)



class test(Scene):
    def construct(self):

        testfifo = kmobjs.FIFO(fifo_depth=3)
        testfifo.move_to((-2, 0, 0))
        packet_1 = kmobjs.CircTxt("1", radius=0.3)

        self.play(
                Create(testfifo)
        )

        testfifo.insert_head(packet_1)
        self.play(
                testfifo.animate.clock_tick()
        )
        #packet_2 = kmobjs.CircTxt("2", radius=0.3)
        #self.play(
        #        testfifo.animate.insert_head(packet_2)
        #)

        self.wait()




