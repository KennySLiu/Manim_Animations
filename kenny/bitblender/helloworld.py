from manim import *

### NOTE: CALL THIS BY USING: manim -pql helloworld.py CreateCircle

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen



class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency
        #circle.rotate(PI/4)

        square = Square()  # create a square

        square.set_fill(BLUE_A, opacity=0.8)
        square.next_to(circle, UP, buff=0.5)

        self.play(Create(square))  # animate the creation of the square
        self.play(square.animate.rotate(PI / 4))
        self.play(square.animate.rotate(PI / 4))
        self.play(square.animate.rotate(-3 * PI / 4))
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
        self.wait()


class test(Scene):
    def construct(self):
        NUM_HASH = 3;
        data_in = [Circle(radius=0.1) for i in range(0, NUM_HASH)]
        self.play(Create(VGroup(data_in[0], data_in[1], data_in[2])))








