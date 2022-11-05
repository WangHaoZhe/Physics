a = 1e-7  # 物块与两人质量比
v1 = 0  # 甲速度
v2 = 0  # 乙速度
v = 0  # 物块速度
u = 1  # 推出物块的相对速度, 任取大于零的数即可
n = 0  # 推物块次数


def collide(m_1, m_2, v_1, v_2):  # 两物体质量及碰前速度, 1为左侧物体, 2为右侧物体
    v_1_new = (m_1 * v_1 + m_2 * (v_2 - u)) / (m_1 + m_2)
    v_2_new = (m_1 * (v_1 + u) + m_2 * v_2) / (m_1 + m_2)
    return v_1_new, v_2_new


while v1 >= v:
    v1, v = collide(1, a, v1, v)
    v, v2 = collide(a, 1, v, v2)
    n += 1


ln2 = 2*a*(n-1)  #ln2测量值
print(n)
print(ln2)
