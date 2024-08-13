from manim import *
import k_common_manim_objects as kmobjs
import random
random.seed(3)


class test(Scene):
    def construct(self):
        tmp = kmobjs.tmptester()
        tmp.add_cir("a")
        tmp.add_rec("b")
        tmp.add_rec("c")

        self.play(
            Create(tmp)
        )

        self.play(
            tmp.animate.move_last_obj( (-1, 2, 0) )
        )
        tmp.add_cir("d")
        self.play(
            tmp.animate.move_last_obj( (-1, 1, 0) )
        )



class unshuffle_unmix_data(Scene):
    def construct(self):
        X0 = -6
        Y0 = -3
        Y1 = -1
        Y2 = 1
        Y3 = 3
        SY0 = 2
        SY1 = 0
        SY2 = -2
        WAIT_TIME = 0.3

        unshuf = kmobjs.RectTxt("UN\nSHUF", h=7, w=3, txt_offset=(0,0,0) )
        p0 = kmobjs.FIFO_boxes(fifo_depth=6)
        p1 = kmobjs.FIFO_boxes(fifo_depth=6)
        p2 = kmobjs.FIFO_boxes(fifo_depth=6)
        p3 = kmobjs.FIFO_boxes(fifo_depth=6)
        partitions = [p0, p1, p2, p3]
        s0 = kmobjs.FIFO_boxes(fifo_depth=3)
        s1 = kmobjs.FIFO_boxes(fifo_depth=3)
        s2 = kmobjs.FIFO_boxes(fifo_depth=3)
        streams = [s0, s1, s2]

        unshuf.move_to( (X0+7, 0, 0) )
        partitions[0].move_to( (X0, Y0, -5) )
        partitions[1].move_to( (X0, Y1, -5) )
        partitions[2].move_to( (X0, Y2, -5) )
        partitions[3].move_to( (X0, Y3, -5) )
        streams[0].move_to( (X0+9, SY0, -5) )
        streams[1].move_to( (X0+9, SY1, -5) )
        streams[2].move_to( (X0+9, SY2, -5) )
        streams[0].set_color( YELLOW_E, opacity=0.5 )
        streams[1].set_color( BLUE, opacity=0.5  )
        streams[2].set_color( RED, opacity=0.5  )

        pkts = []
        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=YELLOW_E) )
        tmp.append( kmobjs.FIFO_pkt("1", color=YELLOW_E) )
        tmp.append( kmobjs.FIFO_pkt("2", color=YELLOW_E) )
        pkts.append(tmp)

        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=BLUE) )
        tmp.append( kmobjs.FIFO_pkt("1", color=BLUE) )
        tmp.append( kmobjs.FIFO_pkt("2", color=BLUE) )
        pkts.append(tmp)

        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=RED) )
        tmp.append( kmobjs.FIFO_pkt("1", color=RED) )
        tmp.append( kmobjs.FIFO_pkt("2", color=RED) )
        pkts.append(tmp)

        for i in range(0, len(pkts[0])):
            pkts[0][i].move_to( (X0+5-3*i, Y3, 0) )

        for i in range(0, len(pkts[1])):
            pkts[1][i].move_to( (X0+4-3*i, Y3, 0) )

        for i in range(0, len(pkts[2])):
            pkts[2][i].move_to( (X0+3-3*i, Y3, 0) )

        pkts[2][2].move_to( (X0+3, Y2, 0) )


        self.play(
            Create(unshuf)
            ,Create(partitions[0])
            ,Create(partitions[1])
            ,Create(partitions[2])
            ,Create(partitions[3])
            ,Create(streams[0])
            ,Create(streams[1])
            ,Create(streams[2])
            ,Create(pkts[0][0])
            ,Create(pkts[0][1])
            ,Create(pkts[0][2])
            ,Create(pkts[1][0])
            ,Create(pkts[1][1])
            ,Create(pkts[1][2])
            ,Create(pkts[2][0])
            ,Create(pkts[2][1])
            ,Create(pkts[2][2])
        )

        self.wait(WAIT_TIME)
        self.play(
            pkts[0][0].animate.move_rel(  (2, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_rel( (1, 0, 0) )
            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )
            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (1, 0, 0) )
        )

        self.wait(WAIT_TIME)
        self.play(
            pkts[0][0].animate.move_mix(  (2, SY0, 0), 'raa' )
            ,pkts[1][0].animate.move_rel( (2, 0, 0) )
            ,pkts[2][0].animate.move_rel( (1, 0, 0) )
            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )
            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (1, 0, 0) )
        )

        self.wait(WAIT_TIME)
        self.play(
            pkts[0][0].animate.move_rel(  (1, 0, 0) )
            ,pkts[1][0].animate.move_mix( (2, SY1, 0), 'raa' )
            ,pkts[2][0].animate.move_rel( (2, 0, 0) )
            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )
            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (2, 0, 0) )
        )

        self.wait(WAIT_TIME)
        self.play(
            pkts[0][0].animate.move_rel(  (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_mix( (2, SY2, 0), 'raa' )
            ,pkts[0][1].animate.move_rel( (2, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )
            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (0, 0, 0) )
        )

        self.wait(WAIT_TIME)
        self.play(
            pkts[0][0].animate.move_rel(  (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_rel( (1, 0, 0) )
            ,pkts[0][1].animate.move_mix( (2, SY0, 0), 'raa' )
            ,pkts[1][1].animate.move_rel( (2, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )
            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (0, 0, 0) )
        )

        self.wait(WAIT_TIME)
        self.play(
            pkts[0][0].animate.move_rel(  (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_rel( (1, 0, 0) )
            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_mix( (2, SY1, 0), 'raa' )
            ,pkts[2][1].animate.move_rel( (2, 0, 0) )
            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (0, 0, 0) )
        )

        self.wait(WAIT_TIME)
        self.play(
            pkts[0][0].animate.move_rel(  (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_rel( (1, 0, 0) )
            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_mix( (2, SY2, 0), 'raa' )
            ,pkts[0][2].animate.move_rel( (2, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (0, 0, 0) )
        )

        self.wait(WAIT_TIME)
        self.play(
            pkts[0][0].animate.move_rel(  (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_rel( (1, 0, 0) )
            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )
            ,pkts[0][2].animate.move_mix( (2, SY0, 0), 'raa' )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_mix( (2, SY2, 0), 'raa' )
        )


        self.wait(5*WAIT_TIME)










class arbiter_mixing_data(Scene):
    def construct(self):
        X0 = -1
        TOP_Y = 3
        MID_Y = 1
        BOT_Y = -1
        WAIT_TIME = 0.3

        arbiter = kmobjs.RectTxt("ARB", h=7, w=2, txt_offset=(0,1,0) )
        p0 = kmobjs.FIFO_boxes(fifo_depth=6)
        p1 = kmobjs.FIFO_boxes(fifo_depth=6)
        p2 = kmobjs.FIFO_boxes(fifo_depth=6)
        p3 = kmobjs.FIFO_boxes(fifo_depth=6)
        partitions = [p0, p1, p2, p3]

        partitions[0].move_to( (X0, TOP_Y, 0) )
        partitions[1].move_to( (X0, MID_Y, 0) )
        partitions[2].move_to( (X0, BOT_Y, 0) )
        partitions[3].move_to( (X0, BOT_Y-2, 0) )
        arbiter.move_to( (X0-2, 0, 0) )

        pkts = []
        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=YELLOW_E) )
        tmp.append( kmobjs.FIFO_pkt("1", color=YELLOW_E) )
        tmp.append( kmobjs.FIFO_pkt("2", color=YELLOW_E) )
        pkts.append(tmp)

        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=BLUE) )
        tmp.append( kmobjs.FIFO_pkt("1", color=BLUE) )
        tmp.append( kmobjs.FIFO_pkt("2", color=BLUE) )
        pkts.append(tmp)

        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=RED) )
        tmp.append( kmobjs.FIFO_pkt("1", color=RED) )
        tmp.append( kmobjs.FIFO_pkt("2", color=RED) )
        pkts.append(tmp)

        for i in range(0, len(pkts[0])):
            pkts[0][i].move_to( (-i+X0-2, 2, 0) )

        for i in range(0, len(pkts[1])):
            pkts[1][i].move_to( (-i+X0-2, 0, 0) )

        for i in range(0, len(pkts[2])):
            pkts[2][i].move_to( (-i+X0-2, -2, 0) )

        self.play(
            Create(arbiter)
            ,Create(partitions[0])
            ,Create(partitions[1])
            ,Create(partitions[2])
            ,Create(partitions[3])
            ,Create(pkts[0][0])
            ,Create(pkts[0][1])
            ,Create(pkts[0][2])
            ,Create(pkts[1][0])
            ,Create(pkts[1][1])
            ,Create(pkts[1][2])
            ,Create(pkts[2][0])
            ,Create(pkts[2][1])
            ,Create(pkts[2][2])
        )

        self.wait(WAIT_TIME)

        self.play(
            pkts[0][0].animate.move_to( (X0-1, TOP_Y+0.5, 0) )
            ,pkts[1][0].animate.move_to( (X0-1, TOP_Y+0, 0) )
            ,pkts[2][0].animate.move_to( (X0-1, TOP_Y-0.5, 0) )
        )

        self.wait(WAIT_TIME)

        self.play(
            pkts[0][0].animate.move_to( (X0-0, TOP_Y+0, 0) )
            #,pkts[1][0].animate.move_to( (X0-1, TOP_Y+0, 0) )
            #,pkts[2][0].animate.move_to( (X0-1, TOP_Y-1, 0) )

            ,pkts[0][1].animate.move_to( (X0-2, TOP_Y+0.5, 0) )
            ,pkts[1][1].animate.move_to( (X0-2, TOP_Y+0, 0) )
            ,pkts[2][1].animate.move_to( (X0-2, TOP_Y-0.5, 0) )
        )

        self.wait(WAIT_TIME)

        self.play(
            pkts[0][0].animate.move_to( (X0+1, TOP_Y+0, 0) )
            ,pkts[1][0].animate.move_to( (X0, TOP_Y+0, 0) )
            #,pkts[2][0].animate.move_to( (X0-1, TOP_Y-1, 0) )

            ,pkts[0][1].animate.move_to( (X0-2, TOP_Y+0.5, 0) )
            ,pkts[1][1].animate.move_to( (X0-2, TOP_Y-0.0, 0) )
            ,pkts[2][1].animate.move_to( (X0-2, TOP_Y-0.5, 0) )

            ,pkts[0][2].animate.move_to( (X0-3, TOP_Y+0.3, 0) )
            ,pkts[1][2].animate.move_to( (X0-3, TOP_Y-0.3, 0) )
            ,pkts[2][2].animate.move_to( (X0-1, MID_Y, 0) )
        )

        self.wait(WAIT_TIME)

        self.play(
            pkts[0][0].animate.move_to( (X0+2, TOP_Y+0, 0) )
            ,pkts[1][0].animate.move_to( (X0+1, TOP_Y+0, 0) )
            ,pkts[2][0].animate.move_to( (X0-0, TOP_Y+0, 0) )

            ,pkts[0][1].animate.move_to( (X0-1, TOP_Y+0.5, 0) )
            ,pkts[1][1].animate.move_to( (X0-1, TOP_Y-0.0, 0) )
            ,pkts[2][1].animate.move_to( (X0-1, TOP_Y-0.5, 0) )

            ,pkts[0][2].animate.move_to( (X0-2, TOP_Y+0.3, 0) )
            ,pkts[1][2].animate.move_to( (X0-2, TOP_Y-0.3, 0) )
            ,pkts[2][2].animate.move_to( (X0-0, MID_Y, 0) )
        )

        self.wait(WAIT_TIME)

        self.play(
            pkts[0][0].animate.move_to( (X0+3, TOP_Y+0, 0) )
            ,pkts[1][0].animate.move_to( (X0+2, TOP_Y+0, 0) )
            ,pkts[2][0].animate.move_to( (X0+1, TOP_Y+0, 0) )

            ,pkts[0][1].animate.move_to( (X0+0, TOP_Y+0, 0) )
            ,pkts[1][1].animate.move_to( (X0-1, TOP_Y-0.0, 0) )
            ,pkts[2][1].animate.move_to( (X0-1, TOP_Y-0.5, 0) )

            ,pkts[0][2].animate.move_to( (X0-2, TOP_Y+0.3, 0) )
            ,pkts[1][2].animate.move_to( (X0-2, TOP_Y-0.3, 0) )
            ,pkts[2][2].animate.move_to( (X0+1, MID_Y, 0) )
        )

        self.wait(WAIT_TIME)

        self.play(
            pkts[0][0].animate.move_to( (X0+4, TOP_Y+0, 0) )
            ,pkts[1][0].animate.move_to( (X0+3, TOP_Y+0, 0) )
            ,pkts[2][0].animate.move_to( (X0+2, TOP_Y+0, 0) )

            ,pkts[0][1].animate.move_to( (X0+1, TOP_Y+0, 0) )
            ,pkts[1][1].animate.move_to( (X0+0, TOP_Y+0, 0) )
            ,pkts[2][1].animate.move_to( (X0-1, TOP_Y-0.5, 0) )

            ,pkts[0][2].animate.move_to( (X0-2, TOP_Y+0.3, 0) )
            ,pkts[1][2].animate.move_to( (X0-2, TOP_Y-0.3, 0) )
            ,pkts[2][2].animate.move_to( (X0+2, MID_Y, 0) )
        )

        self.wait(WAIT_TIME)

        self.play(
            pkts[0][0].animate.move_to( (X0+5, TOP_Y+0, 0) )
            ,pkts[1][0].animate.move_to( (X0+4, TOP_Y+0, 0) )
            ,pkts[2][0].animate.move_to( (X0+3, TOP_Y+0, 0) )

            ,pkts[0][1].animate.move_to( (X0+2, TOP_Y+0, 0) )
            ,pkts[1][1].animate.move_to( (X0+1, TOP_Y+0, 0) )
            ,pkts[2][1].animate.move_to( (X0+0, TOP_Y+0, 0) )

            ,pkts[0][2].animate.move_to( (X0-1, TOP_Y+0.3, 0) )
            ,pkts[1][2].animate.move_to( (X0-1, TOP_Y-0.3, 0) )
            ,pkts[2][2].animate.move_to( (X0+3, MID_Y, 0) )
        )

        self.wait(WAIT_TIME)




















