class triangechecker:
    def __init__(self,a,b,c):
        self.a=int(a)
        self.b=int(b)
        self.c=int(c)
    def is_triangle(self):
        if self.a>0 and self.b>0 and self.c>0:
            if self.a<self.b+self.c and self.b<self.a+self.c and self.c<self.a+self.b:
                print('Ура, можно построить треугольник!')
            else:
                print('Жаль, но из этого треугольник не сделать')
        else:
            print('С отрицательными числами(или 0) ничего не выйдет!')
triangle=triangechecker(int(input()),int(input()),int(input()))
triangle.is_triangle()