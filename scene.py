from manim import *
config.tex_template = TexTemplateLibrary.simple
from math import comb

class Ligne(Scene):
    def construct(self):
        title = Text("Marches aléatoires d'une fourmi", color = BLUE)
        title.next_to(ORIGIN, direction=UP, aligned_edge=DOWN)

        subtitle = Text("Henri Drouhin, Constance Sarrazin").scale(0.4)
        subtitle.next_to(ORIGIN, direction=DOWN, aligned_edge=UP)

        subsubtitle = Text("Maths en jean").scale(0.25)
        subsubtitle.next_to(subtitle, direction=DOWN, aligned_edge=UP)

        self.play(Write(title), FadeIn(subtitle), FadeIn(subsubtitle))
        self.wait()
        self.remove(subtitle,subsubtitle)

        newtitle = Text("Marches aléatoires d'une fourmi", color = BLUE).scale(0.5)
        newtitle.to_edge(UP).to_edge(LEFT)
        part1 = Text("Le long d'une ligne").scale(0.75)
        part1.next_to(newtitle, direction=DOWN, aligned_edge=UP)

        self.play(Transform(title, newtitle))
        self.play(FadeIn(part1))

        item = Circle(radius = 0.05, color = DARK_GRAY, fill_opacity=1).move_to([-6.5,2,0])
        expl = Text('On cherche le nombre de chemins\nque peut prendre la fourmi pour\naller de l\'origine à un point donné.', stroke_width=0.5, color=GRAY).scale(0.4).next_to(part1, direction=DOWN, aligned_edge=UP).shift(DOWN*(1/2))

        self.play(FadeIn(item),Write(expl, run_time=0.7))

        numberline = NumberLine(color = WHITE, numbers_with_elongated_ticks=[], include_numbers=True, width = 7).to_edge(UP).to_edge(RIGHT)
        numberline.shift([0,-0.1,0])
        sepline = Line([-0.8,-3.7,0],[-0.8,3.7,0], stroke_width = 0.3)

        self.play(FadeIn(numberline), FadeIn(sepline))
        self.wait(2)

        num = [[str(comb(k, i)) for i in range(k+1)] for k in range(7)]
        x0 = 3.13
        y0 = 3
        stepx = 0.48
        stepy = -0.7
        coord = [[[x0 + (2*i - k)*stepx, y0+(k+1)*stepy, 0] for i in range(k+1)] for k in range(7)]
        zeros = [[[coord[k][i][0]+stepx, coord[k][i][1], 0] for i in range(len(coord[k])-1)] for k in range(len(coord))]
        anim = []

        for k in range(len(coord)):
            for i in range(len(coord[k])):
                anim.append(Write(MathTex(num[k][i]).scale(0.7).move_to(coord[k][i])))
            for j in range(len(zeros[k])):
                anim.append(Write(MathTex('0', color = GRAY).scale(0.5).move_to(zeros[k][j])))
            self.play(*anim, run_time=0.5)
            anim = []

        self.play(Write(Text('On reconnait le triangle de Pascal.', color = BLUE).move_to(coord[6][3]).shift(DOWN).scale(0.6)))
        
        formula = MathTex('{n\choose k} = {{n-1}\choose {k-1}}+{{n-1}\choose {k}}', color = WHITE).scale(0.7).next_to(expl, direction=DOWN, aligned_edge=UP).shift(DOWN)
        rectanglee = SurroundingRectangle(formula, color = BLUE)
        
        self.play(ShowCreation(rectanglee), Write(formula), Write(Text('Relation de Pascal', color=BLUE).scale(0.6).next_to(rectanglee, direction=UP, aligned_edge=UP)))
        
        item2 = Circle(radius = 0.05, color = DARK_GRAY, fill_opacity=1).move_to([-6.5,-1.1,0])
        conclu = Text('Il est alors facile de montrer que\nle nombre de chemins de l\'origine\nau point d\'abscisse x après t pas\nest :', stroke_width=0.5, color=GRAY).scale(0.4).next_to(rectanglee, direction=DOWN, aligned_edge=DOWN).shift(DOWN*3/4).align_to(expl, LEFT, alignment_vect=LEFT)
        
        self.play(FadeIn(item2), Write(conclu, run_time=1))

        conclusion = MathTex('{t \choose \\frac{x+t}{2}}', color = WHITE).next_to(formula, direction=DOWN, aligned_edge=UP).shift(2*DOWN)
        rectangle2 = SurroundingRectangle(conclusion, color = BLUE)
        
        self.play(Write(conclusion), ShowCreation(rectangle2))
        self.wait(5)

class Prob(Scene):
    arguments = {
            "bar_names" : list(range(-10, 11)),
            "width" : 12
        }
    def construct(self):
        newtitle = Text("Marches aléatoires d'une fourmi", color = BLUE).scale(0.5)
        newtitle.to_edge(UP).to_edge(LEFT)
        part1 = Text("Le long d'une ligne").scale(0.75)
        part1.next_to(newtitle, direction=DOWN, aligned_edge=UP)
        self.add(newtitle, part1)
        subtitle = Tex('Exemple pour $t=10$', color = GRAY).scale(0.8).next_to(part1, direction=DOWN)
        self.add(subtitle)
        loi = [1/(2**10), 0, 10/(2**10), 0, 45/(2**10), 0, 120/(2**10), 0, 210/(2**10), 0, 252/(2**10), 0, 210/(2**10), 0, 120/(2**10), 0, 45/(2**10), 0, 10/(2**10), 0, 1/(2**10)]
        chart = BarChart(values=loi, **self.arguments).to_corner(LEFT+DOWN)
        prob = MathTex('p(x=k)={t\choose \\frac{k+t}{2}} \\times \\frac{1}{2^t}')
        box = SurroundingRectangle(prob, color=BLUE)
        conditions = Tex('avec $\lvert k \\rvert \leq t$ et $k$ et $t$ de même parité', color=GRAY).scale(0.7).next_to(box, direction=UP)
        self.play(Write(prob), Write(chart), ShowCreation(box), Write(conditions))
        self.wait(5)
