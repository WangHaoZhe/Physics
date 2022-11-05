import math as ms

# 常量
pi = 3.14159265
d = 0.005
eta = 1.83e-5
s = 0.002
ro = 981 - 1.293
g = 9.794
b = 8.22e-3
p = 1.013e5
e = 1.602e-19

# 输入
flag = int(input('模式（动态1、静态0）：'))
u = float(input('输入电压：'))
t_f = float(input('输入f时间：'))
if flag:
    t_r = float(input('输入r时间：'))

# 运算
r_0 = ms.sqrt((9 * eta * s) / (2 * g * ro * t_f))
part_a = 9 * ms.sqrt(2) * pi * d
part_b = ms.sqrt(ms.pow(eta * s, 3) / (ro * g))
if flag:
    part_c = ms.pow(t_f, -0.5) * ms.pow(u, -1) * (ms.pow(t_f, -1) + ms.pow(t_r, -1))
else:
    part_c = ms.pow(t_f, -1.5) * ms.pow(u, -1)
part_d = ms.pow(1 + b / (p * r_0), -1.5)

# 结果
q = part_d * part_c * part_b * part_a
t = q / e
e_e = q / round(t)
errors = 100 * (e_e - e) / e

# 输出
print('油滴带电为{}\n倍数为{}\n估计电量为{}\n相对误差为{}\n'.format(q, t, e_e, errors))