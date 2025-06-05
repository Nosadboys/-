from PyQt5.QtGui import QColor

class ColorMaps:
    def __init__(self):
        self.maps = {
            'Classic': self.create_classic_colormap(),
            'Rainbow': self.create_rainbow_colormap(),
            'Fire': self.create_fire_colormap(),
            'Ocean': self.create_ocean_colormap(),
            'Forest': self.create_forest_colormap(),
            'Violet': self.create_violet_colormap()
        }
    
    def __getitem__(self, key):
        return self.maps[key]
    
    def create_classic_colormap(self):
        """Классическая оранжево-черная цветовая схема"""
        return [QColor(int(255 * (i/255)**0.3), 
                      int(255 * (i/255)**1.5), 
                      int(255 * (i/255)**3.0)) for i in range(256)]
    
    def create_rainbow_colormap(self):
        """Радужная цветовая схема"""
        colors = []
        for i in range(256):
            h = i / 255 * 0.7  # Hue от 0 до 0.7 (красный до синего)
            s = 1.0
            v = 1.0 if i < 230 else 0.3  # Темнее для последних итераций
            color = QColor.fromHsvF(h, s, v)
            colors.append(color)
        return colors
    
    def create_fire_colormap(self):
        """Красно-желтая огненная схема"""
        return [QColor(min(255, int(255 * (i/255)**0.5 + 100)),
                min(255, int(120 * (i/255)**1.2)),
                min(255, int(50 * (i/255)**2.0))) for i in range(256)]
    
    def create_ocean_colormap(self):
        """Сине-зеленая морская схема"""
        return [QColor(int(50 * (i/255)**0.5),
                      int(100 + 100 * (i/255)**1.5),
                      int(150 + 100 * (i/255)**0.8)) for i in range(256)]
    
    def create_forest_colormap(self):
        """Зеленая лесная схема"""
        return [QColor(int(50 * (i/255)**0.3),
                      int(100 + 150 * (i/255)**1.2),
                      int(80 * (i/255)**0.5)) for i in range(256)]
    
    def create_violet_colormap(self):
        """Фиолетово-розовая схема"""
        return [QColor(int(150 + 100 * (i/255)**0.8),
                      int(50 * (i/255)**1.5),
                      int(150 + 100 * (i/255)**0.5)) for i in range(256)]
    
    def names(self):
        """Возвращает список доступных цветовых схем"""
        return list(self.maps.keys())