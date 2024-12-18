from manim import *
import k_common_manim_objects as kmobjs
import random
random.seed(3)



class unsep_arb(Scene):
    def construct(self):
        X0 = -1
        TOP_Y = 3
        MID_Y = 1
        BOT_Y = -1
        Y0 = 3
        Y1 = 1
        Y2 = -1
        Y3 = -3
        WAIT_TIME = 0.5

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
            ChangeSpeed( AnimationGroup(
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
            ),
            speedinfo={50:50}
            )
        )

        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_to( (X0, Y0, 0) )
            #,pkts[1][0].animate.move_rel( (1, 0, 0) )
            #,pkts[2][0].animate.move_rel( (1, 0.5, 0) )

            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            #,pkts[1][1].animate.move_rel( (1, 0, 0) )
            #,pkts[2][1].animate.move_rel( (1, 0, 0) )

            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            #,pkts[1][2].animate.move_rel( (1, 0, 0) )
            #,pkts[2][2].animate.move_rel( (1, 0, 0) )
        )

        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_rel( (1, 0, 0) )
            ,pkts[1][0].animate.move_to( (X0, Y0, 0) )
            #,pkts[2][0].animate.move_rel( (1, 0.5, 0) )

            ,pkts[0][1].animate.move_to ( (X0, Y1, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            #,pkts[2][1].animate.move_rel( (1, 0, 0) )

            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            #,pkts[2][2].animate.move_rel( (1, 0, 0) )
        )


        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_rel( (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_to ( (X0, Y0, 0) )

            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_to ( (X0, Y2, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )

            ,pkts[0][2].animate.move_to ( (X0, Y3, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (1, 0, 0) )
        )


        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_rel( (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_rel( (1, 0, 0) )

            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_to ( (X0, Y3, 0) )

            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_to ( (X0, Y0, 0) )
            ,pkts[2][2].animate.move_rel( (1, 0, 0) )
        )


        self.wait(WAIT_TIME)
        self.wait(WAIT_TIME)
        self.wait(WAIT_TIME)
        self.wait(WAIT_TIME)
















class separated_arb(Scene):
    def construct(self):
        XS = -2     ## X value for the separator
        XA = 1      ## X value for the arbiter for each partition
        XP = 3      ## X value for the Partitions.
        X1 = XA-1   ## X value before the arbiter

        Y0 = 3
        Y1 = 1
        Y2 = -1
        Y3 = -3

        WAIT_TIME = 0.8

        ##################
        ### Create all of our objects.
        separator = kmobjs.RectTxt("Sep.", h=7, w=2, txt_offset=(0,1,0) )
        a0 = kmobjs.RectTxt("Arb", h=1.5, w=1.5, txt_offset=(-0.7,-0.7,0) )
        a1 = kmobjs.RectTxt("Arb", h=1.5, w=1.5, txt_offset=(-0.7,-0.7,0) )
        a2 = kmobjs.RectTxt("Arb", h=1.5, w=1.5, txt_offset=(-0.7,-0.7,0) )
        a3 = kmobjs.RectTxt("Arb", h=1.5, w=1.5, txt_offset=(-0.7,-0.7,0) )
        p0 = kmobjs.FIFO_boxes(fifo_depth=3)
        p1 = kmobjs.FIFO_boxes(fifo_depth=3)
        p2 = kmobjs.FIFO_boxes(fifo_depth=3)
        p3 = kmobjs.FIFO_boxes(fifo_depth=3)
        arbiters = [a0, a1, a2, a3]
        partitions = [p0, p1, p2, p3]

        ### Streams from Arb-Separator to Arb-Singlepartitions.
        lines = []
        lines.append( [] )
        lines.append( [] )
        lines.append( [] )
        lines[0].append( Line(color=YELLOW_E) )
        lines[0].append( Line(color=YELLOW_E) )
        lines[0].append( Line(color=YELLOW_E) )
        lines[0].append( Line(color=YELLOW_E) )
        lines[1].append( Line(color=BLUE) )
        lines[1].append( Line(color=BLUE) )
        lines[1].append( Line(color=BLUE) )
        lines[1].append( Line(color=BLUE) )
        lines[2].append( Line(color=RED) )
        lines[2].append( Line(color=RED) )
        lines[2].append( Line(color=RED) )
        lines[2].append( Line(color=RED) )


        ##################
        ### Moving all of our objects

        separator.move_to( (XS, 0, 0) )


        for i in range(len(lines[0])):
            lines[0][i].put_start_and_end_on( 
                (X1-1,      Y0-2*i+0.5, 0),
                (X1+0.5,    Y0-2*i+0.5, 0)
            )
        for i in range(len(lines[1])):
            lines[1][i].put_start_and_end_on( 
                (X1-1,      Y0-2*i, 0),
                (X1+0.5,    Y0-2*i, 0)
            )
        for i in range(len(lines[2])):
            lines[2][i].put_start_and_end_on( 
                (X1-1,      Y0-2*i-0.5, 0),
                (X1+0.5,    Y0-2*i-0.5, 0)
            )


        arbiters[0].move_to( (XA, Y0, 0) )
        arbiters[1].move_to( (XA, Y1, 0) )
        arbiters[2].move_to( (XA, Y2, 0) )
        arbiters[3].move_to( (XA, Y3, 0) )

        partitions[0].move_to( (XP, Y0, 0) )
        partitions[1].move_to( (XP, Y1, 0) )
        partitions[2].move_to( (XP, Y2, 0) )
        partitions[3].move_to( (XP, Y3, 0) )

        pkts = []
        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=YELLOW_E) )
        tmp.append( kmobjs.FIFO_pkt("1", color=YELLOW_E) )
        tmp.append( kmobjs.FIFO_pkt("2", color=YELLOW_E) )
        tmp.append( kmobjs.FIFO_pkt("3", color=YELLOW_E) )
        tmp.append( kmobjs.FIFO_pkt("4", color=YELLOW_E) )
        pkts.append(tmp)

        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=BLUE) )
        tmp.append( kmobjs.FIFO_pkt("1", color=BLUE) )
        tmp.append( kmobjs.FIFO_pkt("2", color=BLUE) )
        tmp.append( kmobjs.FIFO_pkt("3", color=BLUE) )
        tmp.append( kmobjs.FIFO_pkt("4", color=BLUE) )
        pkts.append(tmp)

        tmp = []
        tmp.append( kmobjs.FIFO_pkt("0", color=RED) )
        tmp.append( kmobjs.FIFO_pkt("1", color=RED) )
        tmp.append( kmobjs.FIFO_pkt("2", color=RED) )
        tmp.append( kmobjs.FIFO_pkt("3", color=RED) )
        tmp.append( kmobjs.FIFO_pkt("4", color=RED) )
        pkts.append(tmp)

        for i in range(0, len(pkts[0])):
            pkts[0][i].move_to( (-i+XS-2, 2, 0) )

        for i in range(0, len(pkts[1])):
            pkts[1][i].move_to( (-i+XS-2, 0, 0) )

        for i in range(0, len(pkts[2])):
            pkts[2][i].move_to( (-i+XS-2, -2, 0) )

        self.play(
            ChangeSpeed( AnimationGroup(
                 Create(separator)
                ,Create(lines[0][0])
                ,Create(lines[0][1])
                ,Create(lines[0][2])
                ,Create(lines[0][3])
                ,Create(lines[1][0])
                ,Create(lines[1][1])
                ,Create(lines[1][2])
                ,Create(lines[1][3])
                ,Create(lines[2][0])
                ,Create(lines[2][1])
                ,Create(lines[2][2])
                ,Create(lines[2][3])
                ,Create(arbiters[0])
                ,Create(arbiters[1])
                ,Create(arbiters[2])
                ,Create(arbiters[3])
                ,Create(partitions[0])
                ,Create(partitions[1])
                ,Create(partitions[2])
                ,Create(partitions[3])
                ,Create(pkts[0][0])
                ,Create(pkts[0][1])
                ,Create(pkts[0][2])
                ,Create(pkts[0][3])
                ,Create(pkts[0][4])
                ,Create(pkts[1][0])
                ,Create(pkts[1][1])
                ,Create(pkts[1][2])
                ,Create(pkts[1][3])
                ,Create(pkts[1][4])
                ,Create(pkts[2][0])
                ,Create(pkts[2][1])
                ,Create(pkts[2][2])
                ,Create(pkts[2][3])
                ,Create(pkts[2][4])
            ),
            speedinfo={50:50}
            )
        )




        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_rel( (2, 0, 0) )
            ,pkts[1][0].animate.move_rel( (2, 0, 0) )
            ,pkts[2][0].animate.move_rel( (2, 0, 0) )

            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )

            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (1, 0, 0) )

            ,pkts[0][3].animate.move_rel( (1, 0, 0) )
            ,pkts[1][3].animate.move_rel( (1, 0, 0) )
            ,pkts[2][3].animate.move_rel( (1, 0, 0) )

            ,pkts[0][4].animate.move_rel( (1, 0, 0) )
            ,pkts[1][4].animate.move_rel( (1, 0, 0) )
            ,pkts[2][4].animate.move_rel( (1, 0, 0) )
        )



        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_to ( (X1, Y0+0.5, 0) )
            ,pkts[1][0].animate.move_to ( (X1, Y0+0, 0) )
            ,pkts[2][0].animate.move_to ( (X1, Y0-0.5, 0) )

            ,pkts[0][1].animate.move_rel( (2, 0, 0) )
            ,pkts[1][1].animate.move_rel( (2, 0, 0) )
            ,pkts[2][1].animate.move_rel( (2, 0, 0) )

            ,pkts[0][2].animate.move_rel( (1, 0, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (1, 0, 0) )

            ,pkts[0][3].animate.move_rel( (1, 0, 0) )
            ,pkts[1][3].animate.move_rel( (1, 0, 0) )
            ,pkts[2][3].animate.move_rel( (1, 0, 0) )

            ,pkts[0][4].animate.move_rel( (1, 0, 0) )
            ,pkts[1][4].animate.move_rel( (1, 0, 0) )
            ,pkts[2][4].animate.move_rel( (1, 0, 0) )
        )


        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_rel( (3, -0.5, 0) )
            #,pkts[1][0].animate.move_rel( (0, 0, 0) )
            #,pkts[2][0].animate.move_rel( (0, 0, 0) )

            ,pkts[0][1].animate.move_to ( (X1, Y1+0.5, 0) )
            ,pkts[1][1].animate.move_to ( (X1, Y2, 0) )
            ,pkts[2][1].animate.move_to ( (X1, Y3-0.5, 0) )

            ,pkts[0][2].animate.move_rel( (2, 0, 0) )
            ,pkts[1][2].animate.move_rel( (2, 0, 0) )
            ,pkts[2][2].animate.move_rel( (2, 0, 0) )

            ,pkts[0][3].animate.move_rel( (1, 0, 0) )
            ,pkts[1][3].animate.move_rel( (1, 0, 0) )
            ,pkts[2][3].animate.move_rel( (1, 0, 0) )

            ,pkts[0][4].animate.move_rel( (1, 0, 0) )
            ,pkts[1][4].animate.move_rel( (1, 0, 0) )
            ,pkts[2][4].animate.move_rel( (1, 0, 0) )
        )


        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_rel( (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (3, 0, 0) )
            #,pkts[2][0].animate.move_rel( (0, 0, 0) )

            ,pkts[0][1].animate.move_rel( (3, -0.5, 0) )
            ,pkts[1][1].animate.move_rel( (3, 0, 0) )
            ,pkts[2][1].animate.move_rel( (3, +0.5, 0) )

            ,pkts[0][2].animate.move_to ( (X1, Y0+0.5, 0) )
            ,pkts[1][2].animate.move_to ( (X1, Y2+0.0, 0) )
            ,pkts[2][2].animate.move_to ( (X1, Y2-0.5, 0) )

            ,pkts[0][3].animate.move_rel( (2, 0, 0) )
            ,pkts[1][3].animate.move_rel( (2, 0, 0) )
            ,pkts[2][3].animate.move_rel( (2, 0, 0) )

            ,pkts[0][4].animate.move_rel( (1, 0, 0) )
            ,pkts[1][4].animate.move_rel( (1, 0, 0) )
            ,pkts[2][4].animate.move_rel( (1, 0, 0) )
        )


        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_rel( (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_rel( (3, 0.5, 0) )

            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )

            #,pkts[0][2].animate.move_rel( (0, 0, 0) )
            ,pkts[1][2].animate.move_rel( (3, 0, 0) )
            #,pkts[2][2].animate.move_rel( (0, 0, 0) )

            ,pkts[0][3].animate.move_to ( (X1, Y2+0.5, 0) )
            ,pkts[1][3].animate.move_to ( (X1, Y2+0.0, 0) )
            ,pkts[2][3].animate.move_to ( (X1-1, Y2-0.5, 0) )

            ,pkts[0][4].animate.move_rel( (2, 0, 0) )
            ,pkts[1][4].animate.move_rel( (2, 0, 0) )
            ,pkts[2][4].animate.move_rel( (2, 0, 0) )
        )


        self.wait(WAIT_TIME)
        self.play(
             pkts[0][0].animate.move_rel( (1, 0, 0) )
            ,pkts[1][0].animate.move_rel( (1, 0, 0) )
            ,pkts[2][0].animate.move_rel( (1, 0, 0) )

            ,pkts[0][1].animate.move_rel( (1, 0, 0) )
            ,pkts[1][1].animate.move_rel( (1, 0, 0) )
            ,pkts[2][1].animate.move_rel( (1, 0, 0) )

            ,pkts[0][2].animate.move_rel( (3, -0.5, 0) )
            ,pkts[1][2].animate.move_rel( (1, 0, 0) )
            ,pkts[2][2].animate.move_rel( (3, +0.5, 0) )

            #,pkts[0][3].animate.move_rel( (X1, Y2+0.5, 0) )
            #,pkts[1][3].animate.move_rel( (X1, Y2+0.0, 0) )
            ,pkts[2][3].animate.move_rel( (1, 0, 0) )

            ,pkts[0][4].animate.move_to ( (X1, Y0+0.5, 0) )
            ,pkts[1][4].animate.move_to ( (X1, Y0+0.0, 0) )
            ,pkts[2][4].animate.move_to ( (X1, Y0-0.5, 0) )
        )




        self.wait(WAIT_TIME)
        self.wait(WAIT_TIME)
        self.wait(WAIT_TIME)
        self.wait(WAIT_TIME)





















