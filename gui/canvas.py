import numpy as np
from PyQt5.QtWidgets import QWidget, QProgressBar, QVBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QImage, QPixmap, QColor, QPen
from PyQt5.QtCore import Qt, QPointF, QPoint
from core.fractal_types import FractalType
from core.algorithms import *
from core.color_maps import ColorMaps

class FractalCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(600, 600)
        self.color_maps = ColorMaps()
        self.current_color_map = 'Classic'
        self.fractal_data = None
        self.image = QImage()
        self.dragging = False
        self.last_pos = QPoint()
        
        # Добавляем прогресс-бар
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.hide()
        
        # Основной лейаут
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        
        self.setLayout(layout)
        
        
        
        self.reset_view()

    def reset_view(self):
        #Reset zoom and pan to default values"""
        self.x_min, self.x_max = -2.5, 2.5
        self.y_min, self.y_max = -2.5, 2.5
        self.base_width = self.x_max - self.x_min
        self.base_height = self.y_max - self.y_min
        self.scale = 1.0
        self.pan_offset = QPointF(0, 0)
        self.update()

    def resize(self, width, height):
        """Изменяет размер холста с сохранением пропорций"""
        self.setFixedSize(width, height)
        self.updateGeometry()

    def resizeEvent(self, event):
        # Сохраняем текущий центр и соотношение сторон
        old_center_x = (self.x_min + self.x_max) / 2
        old_center_y = (self.y_min + self.y_max) / 2
        old_aspect = self.base_width / self.base_height
        
        # Получаем новый размер виджета
        new_width = self.width()
        new_height = self.height()
        
        # Рассчитываем новое соотношение сторон
        new_aspect = new_width / new_height
        
        if new_aspect > old_aspect:
            # Окно шире, чем текущее соотношение - регулируем по высоте
            new_height = new_width / old_aspect
            self.resize(new_width, int(new_height))
        else:
            # Окно уже или такое же - регулируем по ширине
            new_width = new_height * old_aspect
            self.resize(int(new_width), new_height)
        
        # Пересчитываем границы с сохранением центра
        new_width = self.x_max - self.x_min
        new_height = self.y_max - self.y_min
        
        if new_aspect > old_aspect:
            # Добавляем ширину, сохраняя высоту
            extra_width = (new_aspect - old_aspect) * new_height
            self.x_min = old_center_x - (new_width + extra_width) / 2
            self.x_max = old_center_x + (new_width + extra_width) / 2
        else:
            # Добавляем высоту, сохраняя ширину
            extra_height = (1/new_aspect - 1/old_aspect) * new_width
            self.y_min = old_center_y - (new_height + extra_height) / 2
            self.y_max = old_center_y + (new_height + extra_height) / 2
        
        self.base_width = self.x_max - self.x_min
        self.base_height = self.y_max - self.y_min
        
        # Если есть изображение, перерисовываем его
        if not self.image.isNull():
            self.update()
    
    def get_current_view(self):
        """Calculate current view boundaries"""
        x_center = (self.x_min + self.x_max) / 2
        y_center = (self.y_min + self.y_max) / 2
        
        x_range = self.base_width / self.scale
        y_range = self.base_height / self.scale
        
        x_min = x_center - x_range/2 + self.pan_offset.x() * x_range
        x_max = x_center + x_range/2 + self.pan_offset.x() * x_range
        y_min = y_center - y_range/2 + self.pan_offset.y() * y_range
        y_max = y_center + y_range/2 + self.pan_offset.y() * y_range
        
        return x_min, x_max, y_min, y_max

    def render_complex_fractal(self, fractal_type, max_iter, **params):
        width, height = self.width(), self.height()
        x_min, x_max, y_min, y_max = self.get_current_view()
        self.x_min, self.x_max = -2.5, 2.5
        self.y_min, self.y_max = -2.5, 2.5
        self.base_width = self.x_max - self.x_min
        self.base_height = self.y_max - self.y_min
        self.scale = 1.0
        
        # Показываем прогресс-бар
        self.progress_bar.show()
        self.progress_bar.setValue(0)
        
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        fractal = np.zeros((height, width), dtype=np.int32)
        
        fractal_func = {
            FractalType.MANDELBROT: mandelbrot,
            FractalType.JULIA: julia,
            FractalType.BURNING_SHIP: burning_ship,
            FractalType.NEWTON: newton,
            FractalType.TRICORN: tricorn
        }.get(fractal_type, mandelbrot)
        
        for i in range(height):
            # Обновляем прогресс
            self.progress_bar.setValue(int(100 * i / height))
            QApplication.processEvents()  # Обновляем UI
            
            if fractal_type == FractalType.JULIA:
                c = params.get('c', -0.7 + 0.27j)
                for j in range(width):
                    fractal[i,j] = fractal_func(c, x[j] + 1j*y[i], max_iter)
            else:
                for j in range(width):
                    fractal[i,j] = fractal_func(x[j] + 1j*y[i], max_iter)
        
        self.fractal_data = fractal
        self.create_image()
        self.progress_bar.hide()  # Скрываем прогресс-бар после завершения
        self.update()
    
    def render_geometric_fractal(self, fractal_type, depth):
        # Создаем изображение с антиалиасингом
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.image.fill(Qt.transparent)
        
        painter = QPainter(self.image)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        
        # Настройка пера для более четкого отображения
        pen = QPen()
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        
        if fractal_type == FractalType.PYTHAGORAS_TREE:
            painter.setPen(QColor(0, 100, 0))
            pen.setWidth(2)
            painter.setPen(pen)
            # Увеличиваем базовый размер и глубину
            pythagoras_tree(
                self.width()//2, self.height()-10,
                self.height()//5, -pi/2, 0, depth, painter)
        
        elif fractal_type == FractalType.LEVY_CURVE:
            painter.setPen(QColor(150, 0, 0))
            # Увеличиваем размер и добавляем отступы
            size = min(self.width()*0.5 , self.height()) * 0.7
            x1, y1 = self.width()/2 - size/2, self.height()/2 + size/4
            x2, y2 = self.width()/2 + size/2, self.height()/2 + size/4
            levy_curve(x1, y1, x2, y2, depth, painter)
        
        elif fractal_type == FractalType.SIERPINSKI:
            painter.setPen(QColor(100, 0, 100))
            # Увеличиваем размер и добавляем сглаживание
            size = min(self.width(), self.height()) * 0.9
            x1, y1 = self.width()/2, self.height()/2 - size/2
            x2, y2 = self.width()/2 - size/2, self.height()/2 + size/2
            x3, y3 = self.width()/2 + size/2, self.height()/2 + size/2
            sierpinski(x1, y1, x2, y2, x3, y3, depth, painter)
        
        elif fractal_type == FractalType.DRAGON_CURVE:
            pen.setColor(QColor(70, 130, 180))  # Steel blue
            pen.setWidth(2)
            painter.setPen(pen)
            size = min(self.width(), self.height()) * 0.7
            x1, y1 = self.width()/2 - size/3, self.height()/2
            x2, y2 = self.width()/2 + size/3, self.height()/2
            dragon_curve(x1, y1, x2, y2, depth, painter)
            
        elif fractal_type == FractalType.SIERPINSKI_CARPET:
            pen.setColor(QColor(139, 69, 19))  # Brown
            pen.setWidth(1)
            painter.setPen(pen)
            size = min(self.width(), self.height()) * 0.8
            x = (self.width() - size) / 2
            y = (self.height() - size) / 2
            sierpinski_carpet(x, y, size, depth, painter)
        
        painter.end()
        self.update()

    def render_koch_snowflake(self, depth):
        """Исправленный рендеринг снежинки Коха"""
        size = min(self.width(), self.height())
        self.image = QImage(size, size, QImage.Format_RGB32)
        self.image.fill(Qt.white)
        
        painter = QPainter(self.image)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QColor(0, 0, 200))
        
        base_size = size * 0.8
        
        x1, y1 = size/2 - base_size/2, size/2 + base_size/3
        x2, y2 = size/2 + base_size/2, size/2 + base_size/3
        x3, y3 = size/2, size/2 - base_size/2
        
        # Всегда используем полный алгоритм, но с оптимизацией
        koch_curve(x1, y1, x2, y2, depth, painter)
        koch_curve(x2, y2, x3, y3, depth, painter)
        koch_curve(x3, y3, x1, y1, depth, painter)
        
        painter.end()
        self.update()

    def render_optimized_koch(self, x1, y1, x2, y2, x3, y3, depth, painter):
        """Упрощённый алгоритм для больших глубин"""
        if depth <= 0:
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))
            painter.drawLine(int(x2), int(y2), int(x3), int(y3))
            painter.drawLine(int(x3), int(y3), int(x1), int(y1))
            return
        
        # Упрощённый алгоритм с меньшим количеством рекурсивных вызовов
        size = ((x2-x1)**2 + (y2-y1)**2)**0.5
        if size < 2:  # Минимальный размер сегмента
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))
            painter.drawLine(int(x2), int(y2), int(x3), int(y3))
            painter.drawLine(int(x3), int(y3), int(x1), int(y1))
            return
        
        # Рисуем только основные линии без детализации
        painter.drawLine(int(x1), int(y1), int(x2), int(y2))
        painter.drawLine(int(x2), int(y2), int(x3), int(y3))
        painter.drawLine(int(x3), int(y3), int(x1), int(y1))
    
    def render_fractal(self, fractal_type, max_iter=100, depth=5, **params):
        self.fractal_type = fractal_type
        
         # Автоматическая подстройка глубины
        depth = min(depth, fractal_type.max_depth)
        
        if fractal_type in [FractalType.MANDELBROT, FractalType.JULIA, 
                    FractalType.BURNING_SHIP, FractalType.NEWTON, 
                    FractalType.TRICORN]:
            self.render_complex_fractal(fractal_type, max_iter, **params)
            
        elif fractal_type == FractalType.KOCH_SNOWFLAKE:
            self.render_koch_snowflake(depth)
            
        else:
            self.render_geometric_fractal(fractal_type, depth)

    def create_image(self):
        """Create QImage from fractal data"""
        if self.fractal_data is None:
            return
            
        height, width = self.fractal_data.shape
        self.image = QImage(width, height, QImage.Format_RGB32)
        
        max_val = self.fractal_data.max()
        if max_val == 0:
            max_val = 1
        
        color_map = self.color_maps[self.current_color_map]
        
        for i in range(height):
            for j in range(width):
                val = self.fractal_data[i,j]
                if val == max_val:
                    self.image.setPixel(j, i, QColor(0, 0, 0).rgb())
                else:
                    color_idx = min(255, int(255 * val / max_val))
                    self.image.setPixel(j, i, color_map[color_idx].rgb())

    def paintEvent(self, event):
        """Отрисовка с центрированным масштабированием"""
        painter = QPainter(self)
        
        if not self.image.isNull():
            painter.save()
            
            # Вычисляем смещение с учетом масштаба и панорамирования
            offset_x = (self.width() - self.image.width() * self.scale) / 2
            offset_y = (self.height() - self.image.height() * self.scale) / 2
            
            # Применяем смещение панорамирования
            offset_x += self.pan_offset.x() * self.image.width() * self.scale
            offset_y += self.pan_offset.y() * self.image.height() * self.scale
            
            painter.translate(offset_x, offset_y)
            painter.scale(self.scale, self.scale)
            
            pixmap = QPixmap.fromImage(self.image)
            painter.drawPixmap(0, 0, pixmap)
            painter.restore()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging and not self.last_pos.isNull():
            delta = event.pos() - self.last_pos
            self.last_pos = event.pos()
            
            norm_dx = delta.x() / self.width() / self.scale
            norm_dy = delta.y() / self.height() / self.scale
            
            self.pan_offset += QPointF(norm_dx, norm_dy)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def wheelEvent(self, event):
        """Отключаем стандартное поведение колесика мыши"""
        pass

    def set_color_map(self, name):
        """Set current color map and redraw"""
        self.current_color_map = name
        if self.fractal_data is not None:
            self.create_image()
            self.update()
            
    def set_zoom_level(self, value):
        """Устанавливаем масштаб с центрированием относительно центра изображения"""
        # Сохраняем предыдущий центр
        old_center = self.pan_offset
        
        # Преобразуем значение ползунка в масштаб (логарифмическая шкала)
        min_scale, max_scale = 0.01, 100.0  # Увеличиваем диапазон масштабирования
        log_scale = np.log10(min_scale) + (np.log10(max_scale) - np.log10(min_scale)) * (value - 1) / 99
        new_scale = 10 ** log_scale
        
        # Корректируем смещение для сохранения центра
        if self.scale != 0:
            scale_factor = new_scale / self.scale
            self.pan_offset = QPointF(
                old_center.x() * scale_factor,
                old_center.y() * scale_factor
            )
        
        self.scale = new_scale
        self.update()         

