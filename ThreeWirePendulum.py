up_ab = eval(input("上圆盘AB"))
up_bc = eval(input("上圆盘BC"))
up_ac = eval(input("上圆盘AC"))

down_ab = eval(input("下圆盘AB"))
down_bc = eval(input("下圆盘BC"))
down_ac = eval(input("下圆盘AC"))

h = eval(input("上下圆盘间距离平均值"))
t_0 = eval(input("未放置物体的转动周期"))

circle_in = eval(input("圆环内径"))
circle_out = eval(input("圆环外径"))
t_circle = eval(input("放置圆盘的转动周期"))

cylinder_x = eval(input("两圆柱体间的距离"))
cylinder_d = eval(input("圆柱体直径"))
t_cylinder = eval(input("放置圆柱体的转动周期"))

# 给定条件
down_m = 358.5  # 下圆盘质量(g)
cylinder_m = 200  # 圆柱体质量(g)
circle_m = 385.5  # 圆环质量(g)
g = 9.8  # 重力加速度(m*s^-2)
pi = 3.1415  # pi

# 初始化
up_r = 0.0  # 上圆盘外径
down_r = 0.0  # 下圆盘外径
j_0 = 0.0  # 未放置物体的转动惯量
j_circle = 0.0  # 放置圆环的转动惯量
circle_j = 0.0  # 圆环的转动惯量
j_cylinder = 0.0  # 放置圆柱体的转动惯量
cylinder_j = 0.0  # 圆柱体绕中心轴的转动惯量

def Circumcircle(a, b, c):
    s = ((a+b+c)*(a+b-c)*(b+c-a)*(a+c-b))**(0.5)
    r = a*b*c/s
    return r  # 圆盘半径(mm)


def MomentOfInertia(m, t):
    j = ((down_m+m)*g*up_r*down_r*t**2)/(4.0*pi**2*h)*10**(-6)
    return j  # 转动惯量(kg*m^2)


up_r = Circumcircle(up_ab, up_bc, up_ac)
down_r = Circumcircle(down_ab, down_bc, down_ac)

j_0 = MomentOfInertia(0.0, t_0)
j_circle = MomentOfInertia(circle_m, t_circle)
j_cylinder = MomentOfInertia(2*cylinder_m, t_cylinder)

circle_j = j_circle - j_0
cylinder_j = j_cylinder - j_0 - cylinder_m*(cylinder_x-cylinder_d)**2/4*10**-9


print("上圆盘半径"+str(round(up_r, 1)))
print("下圆盘半径"+str(round(down_r, 1)))
print("下圆盘未放置物体的转动惯量"+str(round(j_0, 4)))
print("下圆盘放置圆环的转动惯量"+str(round(j_circle, 4)))
print("圆环的转动惯量"+str(round(circle_j, 4)))
print("下圆盘放置圆柱体的转动惯量"+str(round(j_cylinder, 4)))
print("圆柱体绕中心的转动惯量"+str(round(cylinder_j, 4)))
