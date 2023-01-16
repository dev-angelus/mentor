#find area of triangle using coordinates of 6 vertices

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def area(self):

        area = (self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2)) / 2

        print(f'The area of triangle is {area}')

        with open('area.txt', 'a') as f:
            f.write(f'The area of triangle is {area}\n')

    def vertices(self):
        A_sqr = ((pow((self.x2 - self.x1), 2) + pow((self.y2 - self.y1), 2)))
        B_sqr = ((pow((self.x3 - self.x2), 2) + pow((self.y3 - self.y2), 2)))
        C_sqr = ((pow((self.x3 - self.x1), 2) + pow((self.y3 - self.y1), 2)))

        if (A_sqr == B_sqr + C_sqr or (B_sqr == A_sqr + C_sqr) or (C_sqr == B_sqr + A_sqr)):
            print('TRUE - This is right-angled triangle')
        else:
            print('FALSE - This is not right-angled triangle')

        with open('truefalse.txt', 'a') as f:
            if (A_sqr == B_sqr + C_sqr or (B_sqr == A_sqr + C_sqr) or (C_sqr == B_sqr + A_sqr)):
                f.write('TRUE - This is right-angled triangle\n')
            else:
                f.write('FALSE - This is not right-angled triangle\n')


fig1 = Triangle(13, -1, -9, 3, -3, -9)
fig2 = Triangle(2, 3, 4, 3, 3, 1)

fig1.area()
fig2.area()

fig1.vertices()
fig2.vertices()
