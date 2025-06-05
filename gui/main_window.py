from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, 
                            QFileDialog, QMessageBox)
from PyQt5.QtGui import QImageWriter
from .controls import FractalControls
from .canvas import FractalCanvas
from core.fractal_types import FractalType

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_connections()
        self.setWindowTitle("Fractal_Visualizer_Kz_E_A")
    
    def init_ui(self):
        """Initialize main window UI"""
        self.setGeometry(100, 100, 1200, 900)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(5, 5, 5, 5)
        
        # Fractal display canvas
        self.canvas = FractalCanvas()
        main_layout.addWidget(self.canvas, stretch=4)
        
        # Control panel
        self.controls = FractalControls()
        main_layout.addWidget(self.controls, stretch=1)
    
    def setup_connections(self):
        """Подключаем все сигналы и слоты"""
        # Рендеринг по кнопке
        self.controls.render_requested.connect(self.reset_and_render)
        
        self.controls.fractal_type.currentIndexChanged.connect(
            lambda: self.render_with_current_params())
        
        # Остальные соединения сброс, сохранение, цветовая схема
        self.controls.reset_requested.connect(self.canvas.reset_view)
        self.controls.save_requested.connect(self.save_fractal_image)
        self.controls.color_map_changed.connect(
            lambda name: self.canvas.set_color_map(name))
        
        self.controls.zoom_slider.valueChanged.connect(self.canvas.set_zoom_level)
        
        # Автоматический рендеринг при изменении параметров
        self.controls.fractal_type.currentIndexChanged.connect(
            lambda: self.render_with_current_params())
        self.controls.max_iter.valueChanged.connect(
            lambda: self.render_with_current_params())
        self.controls.depth.valueChanged.connect(
            lambda: self.render_with_current_params())
        self.controls.julia_real.valueChanged.connect(
            lambda: self.render_with_current_params())
        self.controls.julia_imag.valueChanged.connect(
            lambda: self.render_with_current_params())
    
    def render_with_current_params(self):
        """Рендеринг с текущими параметрами"""
        params = self.controls.get_params()
    
        if params['fractal_type'] in [
            FractalType.MANDELBROT,
            FractalType.JULIA,
            FractalType.BURNING_SHIP,
            FractalType.NEWTON,
            FractalType.TRICORN
        ]:
        # Комплексные фракталы
            self.canvas.render_fractal(
                fractal_type=params['fractal_type'],
                max_iter=params['max_iter'],
                **{k: v for k, v in params.items() 
                if k not in ['fractal_type', 'max_iter', 'depth']})
                          
        elif params['fractal_type'] == FractalType.KOCH_SNOWFLAKE:
            # Снежинка Коха
            self.canvas.render_fractal(
                fractal_type=params['fractal_type'],
                depth=params['depth'])
                
        else:
            # Геометрические фракталы
            self.canvas.render_fractal(
                fractal_type=params['fractal_type'],
                depth=params['depth'])
  
    def reset_and_render(self):
        """Сбрасывает вид и запускает рендеринг"""
        params = self.controls.get_params()
        if params['fractal_type'] in [
            FractalType.MANDELBROT, 
            FractalType.JULIA,
            FractalType.BURNING_SHIP,
            FractalType.NEWTON,
            FractalType.TRICORN
        ]:
            self.canvas.reset_view()  # Сначала сбрасываем вид
            self.controls.zoom_slider.setValue(50)  # Сбрасываем слайдер в среднее положение
        self.render_with_current_params()  # Затем рендерим
    
    def save_fractal_image(self):
        """Save current fractal image to file"""
        if self.canvas.image.isNull():
            QMessageBox.warning(self, "Warning", "No fractal to save!")
            return
        
        formats = ";;".join([f"{str(f.data(), 'utf-8')} (*.{str(f.data(), 'utf-8')})" 
                            for f in QImageWriter.supportedImageFormats()])
        
        filename, selected_filter = QFileDialog.getSaveFileName(
            self, "Save Fractal Image", "", formats)
        
        if filename:
            # Ensure proper file extension
            format_ext = selected_filter.split('*.')[-1].split(')')[0]
            if not filename.endswith(f".{format_ext}"):
                filename += f".{format_ext}"
            
            if not self.canvas.image.save(filename):
                QMessageBox.critical(self, "Error", "Failed to save image!")
            else:
                QMessageBox.information(self, "Success", "Image saved successfully!")