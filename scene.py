import os
from manim import *


class BlendedTrailer(Scene):
    def construct(self):
        butterfly = ImageMobject("images/wikijs-butterfly.png").to_corner(5.5 * DOWN)
        butterfly_logo = ImageMobject("images/wikijs-butterfly_logo.png").to_corner(LEFT + UP)
        title = Text(r"This is Blended MINT", font_size=50, color=WHITE, font="Noto Sans").to_corner(7 * DOWN)
        title_end = Text(r"Blended MINT", font_size=50, color=WHITE, font="Noto Sans").to_corner(7 * DOWN)
        self.play(FadeIn(butterfly, shift=DOWN, run_time=3), Write(title))
        self.wait()

        transform_title = Text("Blended MINT", font_size=20, font="Noto Sans")
        transform_title.to_corner(UP + (-2.3 * RIGHT - 0.2 * DOWN))
        self.play(
            Transform(title, transform_title),
            FadeOut(butterfly, shift=DOWN, run_time=1),
            FadeIn(butterfly_logo)
        )
        self.wait(2)
        size1 = 25
        why = Text("This wiki is a search for the answers to two questions:",
                   font_size=size1, color=WHITE, font="Noto Sans")
        q1 = Text("How can we as course organizers make the best use\nof the precious time in the classroom?",
                  font_size=size1, color=WHITE, font="Noto Sans")
        q2 = Text("What parts of teaching can be digitized\nfor use outside the classroom?",
                  font_size=size1, color=WHITE, font="Noto Sans")
        visit = Text("Visit us at:",
                     font_size=size1, color=WHITE, font="Noto Sans")
        url = Text("somefancyadress.uzh.ch",
                   font_size=35, color=GREY, font="Noto Sans").to_edge(DOWN - 4 * UP)

        self.play(FadeIn(why))
        self.wait()
        self.play(FadeOut(why))
        self.wait()
        self.play(FadeIn(q1))
        self.wait(2)
        self.play(FadeOut(q1))
        self.wait()
        self.play(FadeIn(q2))
        self.wait(3)
        self.play(FadeOut(q2))
        self.wait()
        self.play(FadeIn(visit))
        self.wait()
        self.play(FadeIn(url))
        self.wait()
        self.play(FadeOut(visit, url, title, butterfly_logo))
        self.play(FadeIn(butterfly, title_end))
        self.wait()
        self.play(FadeOut(butterfly, title_end, run_time=3))
        self.wait()


class ButterflyTest1(Scene):
    def construct(self):
        butterfly = ImageMobject("images/wikijs-butterfly.png")
        background = ImageMobject("images/nature_stock.jpg")
        self.add(background)
        self.play(FadeIn(butterfly))
        self.wait()


if __name__ == '__main__':
    command = "manim -pqh scene.py BlendedTrailer"  # command to be executed
    res = os.system(command)  # return value of the manim command
    print("Returned Value: ", res)
