import random
from math import cos, sin, pi
from numba import jit
import numpy as np
from math import pi

@jit(nopython=True)
# Фрактал Мандельброта
def mandelbrot(c, max_iter):
    z = 0j
    for n in range(max_iter):
        if z.real*z.real + z.imag*z.imag > 4:  # Быстрее чем abs(z) > 2
            return n
        z = z*z + c
    return max_iter

@jit(nopython=True)
# Фрактал Жюлиа
def julia(c, z, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

@jit(nopython=True)
# Фрактал Горящего Корабля
def burning_ship(c, max_iter):
    z = 0j
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = (abs(z.real) + 1j*abs(z.imag))**2 + c
    return max_iter

@jit(nopython=True)
# Фрактал Ньютона
def newton(z, max_iter):
    for n in range(max_iter):
        dz = 3*z**2 - 1
        if dz == 0:
            return max_iter
        z_next = z - (z**3 - z)/dz
        if abs(z_next - z) < 1e-6:
            return n
        z = z_next
    return max_iter

@jit(nopython=True)
# Набор Мандельбара (Tricorn)
def tricorn(c, max_iter):
    z = 0j
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = (z.conjugate())**2 + c
    return max_iter

# Фрактальное дерево Пифагора
def pythagoras_tree(x, y, length, angle, depth, max_depth, painter):
    if depth > max_depth or length < 1:  # Добавляем минимальную длину
        return
    
    x2 = x + length * cos(angle)
    y2 = y + length * sin(angle)
    
    # Утолщаем линии в зависимости от глубины
    pen = painter.pen()
    pen.setWidth(max(1, 3 - depth//4))
    painter.setPen(pen)
    
    painter.drawLine(int(x), int(y), int(x2), int(y2))
    
    new_length = length * 0.7
    pythagoras_tree(x2, y2, new_length, angle - pi/4, depth+1, max_depth, painter)
    pythagoras_tree(x2, y2, new_length, angle + pi/4, depth+1, max_depth, painter)

# Кривая Леви
def levy_curve(x1, y1, x2, y2, depth, painter):
    if depth == 0 or ((x2-x1)**2 + (y2-y1)**2) < 4:  # Минимальная длина сегмента
        pen = painter.pen()
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(int(x1), int(y1), int(x2), int(y2))
        return
    
    xm = (x1 + x2) / 2 - (y2 - y1) / 2
    ym = (y1 + y2) / 2 + (x2 - x1) / 2
    
    levy_curve(x1, y1, xm, ym, depth-1, painter)
    levy_curve(xm, ym, x2, y2, depth-1, painter)

# Кривая Коха
def koch_curve(x1, y1, x2, y2, depth, painter):
    if depth == 0:
        painter.drawLine(int(x1), int(y1), int(x2), int(y2))
        return
    
    dx = x2 - x1
    dy = y2 - y1
    
    x3 = x1 + dx/3
    y3 = y1 + dy/3
    
    x4 = x1 + 2*dx/3
    y4 = y1 + 2*dy/3
    
    x5 = x3 + (dx/3)*cos(pi/3) - (dy/3)*sin(pi/3)
    y5 = y3 + (dx/3)*sin(pi/3) + (dy/3)*cos(pi/3)
    
    koch_curve(x1, y1, x3, y3, depth-1, painter)
    koch_curve(x3, y3, x5, y5, depth-1, painter)
    koch_curve(x5, y5, x4, y4, depth-1, painter)
    koch_curve(x4, y4, x2, y2, depth-1, painter)

# Треугольник Серпинского
def sierpinski(x1, y1, x2, y2, x3, y3, depth, painter):
    if depth == 0 or ((x2-x1)**2 + (y2-y1)**2) < 9:  # Минимальный размер треугольника
        pen = painter.pen()
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawLine(int(x1), int(y1), int(x2), int(y2))
        painter.drawLine(int(x2), int(y2), int(x3), int(y3))
        painter.drawLine(int(x3), int(y3), int(x1), int(y1))
        return
    
    x12 = (x1 + x2) / 2
    y12 = (y1 + y2) / 2
    x23 = (x2 + x3) / 2
    y23 = (y2 + y3) / 2
    x31 = (x3 + x1) / 2
    y31 = (y3 + y1) / 2
    
    sierpinski(x1, y1, x12, y12, x31, y31, depth-1, painter)
    sierpinski(x12, y12, x2, y2, x23, y23, depth-1, painter)
    sierpinski(x31, y31, x23, y23, x3, y3, depth-1, painter)
    
# Дракон Хартера-Хейтуэя
def dragon_curve(x1, y1, x2, y2, depth, painter, direction=1):
    if depth == 0:
        painter.drawLine(int(x1), int(y1), int(x2), int(y2))
        return
    
    # Вычисляем новую точку
    dx = x2 - x1
    dy = y2 - y1
    
    xm = x1 + (dx - dy * direction) / 2
    ym = y1 + (dx * direction + dy) / 2
    
    dragon_curve(x1, y1, xm, ym, depth-1, painter, 1)
    dragon_curve(xm, ym, x2, y2, depth-1, painter, -1)

# Ковер Серпинского
def sierpinski_carpet(x, y, size, depth, painter):
    if depth == 0:
        painter.drawRect(int(x), int(y), int(size), int(size))
        return
    
    new_size = size / 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue  # Пропускаем центральный квадрат
            sierpinski_carpet(
                x + i * new_size,
                y + j * new_size,
                new_size,
                depth - 1,
                painter
            )