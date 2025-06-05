from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QGroupBox, QLabel, 
                            QComboBox, QSpinBox, QDoubleSpinBox, QPushButton,
                            QHBoxLayout, QSlider)
from PyQt5.QtCore import pyqtSignal, Qt
from core.fractal_types import FractalType
from PyQt5.QtWidgets import QTextBrowser

FRACTAL_DESCRIPTIONS = {
    "Множество Мандельброта": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Множество Мандельброта</h3>
        
        <p><b>🔹 Математическое определение:</b><br>
        Множество всех комплексных чисел <i>c</i>, для которых рекуррентная последовательность:<br>
        <center><i>zₙ₊₁ = zₙ² + c</i>, при <i>z₀ = 0</i></center><br>
        остаётся ограниченной при <i>n → ∞</i>.</p>
        
        <p><b>🔹 Историческая справка:</b><br>
        • 1918-1920: Первые исследования Гастоном Жюлиа и Пьером Фату<br>
        • 1979: Бенуа Мандельброт впервые визуализировал множество<br>
        • 1985: Первые цветные визуализации с помощью компьютеров IBM</p>
        
        <p><b>🔹 Ключевые свойства:</b></p>
        <ul style="list-style-type: square;">
            <li><u>Самоподобие</u>: Граница содержит бесконечное количество уменьшенных копий всего множества</li>
            <li><u>Фрактальная размерность</u>: 2 (по Хаусдорфу) для границы множества</li>
            <li><u>Связь с динамическими системами</u>: Характеризует устойчивость квадратичных отображений</li>
            <li><u>Основная гипотеза</u>: Множество локально связно (не доказано)</li>
        </ul>
        
        <p><b>🔹 Применения:</b></p>
        <ol>
            <li>Компьютерная графика и алгоритмы визуализации</li>
            <li>Теория хаоса и нелинейных динамических систем</li>
            <li>Фрактальный анализ финансовых рынков</li>
            <li>Генерация procedural-текстур в играх</li>
        </ol>
        
        <p style="font-style: italic; color: #7f8c8d;">
        Интересный факт: При увеличении границы множества можно обнаружить бесконечное разнообразие самоподобных структур.
        </p>
    </div>
    """,

    "Множество Жюлиа": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Множество Жюлиа</h3>
        
        <p><b>🔹 Формальное определение:</b><br>
        Для фиксированного комплексного параметра <i>c</i>, множество Жюлиа — это множество начальных точек <i>z₀</i>, для которых последовательность:<br>
        <center><i>zₙ₊₁ = zₙ² + c</i></center><br>
        остаётся ограниченной.</p>
        
        <p><b>🔹 Классификация:</b></p>
        <table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
            <tr>
                <th>Тип</th>
                <th>Условие</th>
                <th>Свойства</th>
            </tr>
            <tr>
                <td>Связное</td>
                <td>c ∈ M (Мандельброта)</td>
                <td>Односвязная область</td>
            </tr>
            <tr>
                <td>Пыль Кантора</td>
                <td>c ∉ M</td>
                <td>Совершенное, нигде не плотное</td>
            </tr>
        </table>
        
        <p><b>🔹 Методы исследования:</b></p>
        <ul>
            <li>Теория потенциала и гармонические меры</li>
            <li>Методы Монте-Карло для анализа границ</li>
            <li>Теория нормальных форм для бифуркаций</li>
        </ul>
        
        <p><b>🔹 Визуальные особенности:</b><br>
        Каждое значение <i>c</i> порождает уникальный фрактал. При <i>c</i> из разных областей множества Мандельброта получаются качественно разные структуры.</p>
    </div>
    """,

    "Горящий корабль": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Фрактал «Горящий корабль»</h3>
        
        <p><b>🔹 Математическая модель:</b><br>
        Модификация множества Мандельброта с итерационной формулой:<br>
        <center><i>zₙ₊₁ = (|Re(zₙ)| + i|Im(zₙ)|)² + c</i></center></p>
        
        <p><b>🔹 Особенности:</b></p>
        <ul>
            <li><u>Неаналитичность</u>: Оператор модуля делает отображение неголоморфным</li>
            <li><u>Симметрия</u>: Зеркальная симметрия относительно действительной оси</li>
            <li><u>Визуальная структура</u>: Напоминает корабль с мачтами и парусами</li>
        </ul>
        
        <p><b>🔹 Исследовательские аспекты:</b></p>
        <ol>
            <li>Анализ точек бифуркации для неголоморфных отображений</li>
            <li>Вычисление точной фрактальной размерности границ</li>
            <li>Сравнение с классическим множеством Мандельброта</li>
        </ol>
        
        <p style="background-color: #f8f9fa; padding: 10px; border-left: 3px solid #e74c3c;">
        <b>Историческая заметка:</b> Фрактал получил название из-за характерного вида при определённых значениях параметров, напоминающего горящий корабль с отражением в воде.
        </p>
    </div>
    """,

    "Фрактал Ньютона": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Фрактал Ньютона</h3>
        
        <p><b>🔹 Математическая основа:</b><br>
        Визуализация сходимости метода Ньютона для уравнения:<br>
        <center><i>f(z) = z³ - 1 = 0</i></center><br>
        с итерационной формулой:<br>
        <center><i>zₙ₊₁ = zₙ - f(zₙ)/f'(zₙ)</i></center></p>
        
        <p><b>🔹 Теоретические аспекты:</b></p>
        <ul style="list-style-type: square;">
            <li>Бассейны притяжения корней образуют фрактальные границы</li>
            <li>Демонстрирует эффект "застревания" в ложных минимумах</li>
            <li>Для любого многочлена степени ≥3 возникает фрактальная структура</li>
            <li>Чувствительность к начальным условиям вблизи границ бассейнов</li>
        </ul>
        
        <p><b>🔹 Исследовательские задачи:</b></p>
        <table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
            <tr>
                <th>Проблема</th>
                <th>Методы исследования</th>
            </tr>
            <tr>
                <td>Оценка площади фрактальных границ</td>
                <td>Методы Монте-Карло</td>
            </tr>
            <tr>
                <td>Скорость сходимости в различных областях</td>
                <td>Теория динамических систем</td>
            </tr>
        </table>
        
        <p style="background-color: #f8f9fa; padding: 10px; border-left: 3px solid #3498db;">
        <b>Применение:</b> Тестовый пример для анализа алгоритмов оптимизации и изучения явления "фрактальной неустойчивости" численных методов.
        </p>
    </div>
    """,

    "Трикорн": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Фрактал Трикорн (Мандельбар)</h3>
        
        <p><b>🔹 Формальное определение:</b><br>
        Множество комплексных чисел <i>c</i>, для которых последовательность:<br>
        <center><i>zₙ₊₁ = (z̄ₙ)² + c</i> (где z̄ — сопряжение)</center><br>
        остаётся ограниченной.</p>
        
        <p><b>🔹 Геометрические особенности:</b></p>
        <div style="display: flex; justify-content: space-between;">
            <div style="width: 48%;">
                <p><u>Симметрия:</u></p>
                <ul>
                    <li>Трехлучевая симметрия</li>
                    <li>Отражение относительно вещественной оси</li>
                </ul>
            </div>
            <div style="width: 48%;">
                <p><u>Размерность:</u></p>
                <ul>
                    <li>Фрактальная размерность ≈1.7</li>
                    <li>Гауссова кривизна границы</li>
                </ul>
            </div>
        </div>
        
        <p><b>🔹 Сравнение с Мандельбротом:</b></p>
        <table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
            <tr>
                <th>Характеристика</th>
                <th>Мандельброт</th>
                <th>Трикорн</th>
            </tr>
            <tr>
                <td>Формула</td>
                <td>z² + c</td>
                <td>(z̄)² + c</td>
            </tr>
            <tr>
                <td>Симметрия</td>
                <td>Ось вещественных чисел</td>
                <td>Трехлучевая</td>
            </tr>
        </table>
        
        <p style="font-style: italic; color: #7f8c8d; margin-top: 15px;">
        Интересный факт: Название "Трикорн" происходит от характерной трехлучевой структуры основного кардиоида фрактала.
        </p>
    </div>
    """,

    "Дерево Пифагора": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Дерево Пифагора</h3>
        
        <p><b>🔹 Геометрическое построение:</b></p>
        <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
            <div style="width: 48%;">
                <p><u>Шаги построения:</u></p>
                <ol>
                    <li>Начальный квадрат</li>
                    <li>Построение прямоугольного треугольника</li>
                    <li>Добавление квадратов на катетах</li>
                    <li>Рекурсивное повторение</li>
                </ol>
            </div>
            <div style="width: 48%;">
                <p><u>Параметры:</u></p>
                <ul>
                    <li>Угол ветвления: обычно 45°</li>
                    <li>Коэффициент масштабирования: √2/2</li>
                    <li>Глубина рекурсии: 5-12</li>
                </ul>
            </div>
        </div>
        
        <p><b>🔹 Связь с теоремой Пифагора:</b><br>
        Площадь родительского квадрата (S) равна сумме площадей двух дочерних квадратов (S₁ + S₂), что непосредственно следует из теоремы Пифагора.</p>
        
        <p><b>🔹 Вариации:</b></p>
        <ul>
            <li><u>Классическое:</u> 45° угол ветвления</li>
            <li><u>Обобщенное:</u> Произвольные углы</li>
            <li><u>Стохастическое:</u> Случайные вариации параметров</li>
        </ul>
        
        <div style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; margin-top: 10px;">
            <p><b>Применение в образовании:</b><br>
            Наглядная демонстрация связи алгебры (теорема Пифагора) и геометрии (фрактальные структуры).</p>
        </div>
    </div>
    """,

    "Кривая Леви": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Кривая Леви</h3>
        
        <p><b>🔹 Рекурсивное построение:</b></p>
        <div style="display: flex; justify-content: space-between;">
            <div style="width: 48%;">
                <p><u>Итерационный процесс:</u></p>
                <ol>
                    <li>Шаг 0: отрезок</li>
                    <li>Шаг n: замена каждого отрезка двумя под 90°</li>
                </ol>
            </div>
            <div style="width: 48%;">
                <p><u>Формальные параметры:</u></p>
                <ul>
                    <li>Угол поворота: 90°</li>
                    <li>Коэффициент масштабирования: 1/√2</li>
                </ul>
            </div>
        </div>
        
        <p><b>🔹 Асимптотические свойства:</b></p>
        <table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%; margin: 10px 0;">
            <tr>
                <th>Характеристика</th>
                <th>Значение</th>
            </tr>
            <tr>
                <td>Длина кривой</td>
                <td>lim<sub>n→∞</sub> L<sub>n</sub> = ∞</td>
            </tr>
            <tr>
                <td>Площадь охвата</td>
                <td>lim<sub>n→∞</sub> S<sub>n</sub> = 0</td>
            </tr>
            <tr>
                <td>Фрактальная размерность</td>
                <td>2</td>
            </tr>
        </table>
        
        <p><b>🔹 Приложения:</b></p>
        <ul>
            <li>Моделирование молниевых разрядов</li>
            <li>Анализ трещинообразования в материалах</li>
            <li>Проектирование фрактальных антенн</li>
        </ul>
        
        <p style="font-style: italic; color: #7f8c8d; margin-top: 10px;">
        Историческая справка: Впервые описана французским математиком Полем Леви в 1938 году.
        </p>
    </div>
    """,

    "Треугольник Серпинского": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Треугольник Серпинского</h3>
        
        <p><b>🔹 Способы построения:</b></p>
        <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
            <div style="width: 32%;">
                <p><u>1. Рекурсивное удаление:</u></p>
                <ol>
                    <li>Начальный треугольник</li>
                    <li>Удаление центрального</li>
                    <li>Повтор для оставшихся</li>
                </ol>
            </div>
            <div style="width: 32%;">
                <p><u>2. L-система:</u></p>
                <ul>
                    <li>Аксиома: F--F--F</li>
                    <li>Правило: F → F--F--F--ff</li>
                </ul>
            </div>
            <div style="width: 32%;">
                <p><u>3. Хаотическая игра:</u></p>
                <ul>
                    <li>Выбор случайной вершины</li>
                    <li>Переход к середине</li>
                    <li>Итеративный процесс</li>
                </ul>
            </div>
        </div>
        
        <p><b>🔹 Топологические свойства:</b></p>
        <ul>
            <li>Универсальный фрактал среди одномерных компактов</li>
            <li>Нетривиальная гомология в размерности 0</li>
            <li>Фрактальная размерность: log₂3 ≈ 1.585</li>
        </ul>
        
        <p><b>🔹 Обобщения:</b></p>
        <table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%;">
            <tr>
                <th>Название</th>
                <th>Размерность</th>
                <th>Формула</th>
            </tr>
            <tr>
                <td>Тетраэдр Серпинского</td>
                <td>3D</td>
                <td>Рекурсивное удаление октаэдров</td>
            </tr>
            <tr>
                <td>Пирамида Серпинского</td>
                <td>3D</td>
                <td>Обобщение на пирамиды</td>
            </tr>
        </table>
        
        <div style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; margin-top: 10px;">
            <p><b>Применение:</b> Тестовый объект в теории меры, фрактальной геометрии и компьютерной графике.</p>
        </div>
    </div>
    """,

    "Кривая Хартера-Хейтуэя (Дракон)": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Кривая Хартера-Хейтуэя (Дракон)</h3>
        
        <p><b>🔹 Алгоритм построения:</b></p>
        <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
            <div style="width: 48%;">
                <p><u>Рекурсивный метод:</u></p>
                <ol>
                    <li>Начальный отрезок</li>
                    <li>Замена на два под 90°</li>
                    <li>Чередование направлений</li>
                </ol>
            </div>
            <div style="width: 48%;">
                <p><u>Параметры:</u></p>
                <ul>
                    <li>Угол поворота: 90°</li>
                    <li>Масштабный коэффициент: 1/√2</li>
                    <li>Глубина рекурсии: 10-15</li>
                </ul>
            </div>
        </div>
        
        <p><b>🔹 Удивительные свойства:</b></p>
        <ul>
            <li>Несамопересекается при бесконечном числе итераций</li>
            <li>Может быть описана системой итерируемых функций (IFS)</li>
            <li>Появляется в структуре некоторых квазикристаллов</li>
            <li>Заполняет часть плоскости с размерностью 2</li>
        </ul>
        
        <p><b>🔹 Исторический контекст:</b></p>
        <div style="background-color: #f8f9fa; padding: 10px; border-radius: 5px;">
            <p>Впервые исследована NASA в 1960-х годах при анализе траекторий полётов. Название "дракон" появилось из-за сходства с мифологическим существом при определённых углах поворота.</p>
        </div>
        
        <p style="margin-top: 15px;"><b>🔹 Приложения:</b></p>
        <ol>
            <li>Моделирование биологических структур</li>
            <li>Проектирование фрактальных антенн</li>
            <li>Генерация procedural-текстур</li>
        </ol>
    </div>
    """,

    "Ковёр Серпинского": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Ковёр Серпинского</h3>
        
        <p><b>🔹 Построение:</b></p>
        <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
            <div style="width: 48%;">
                <p><u>Итерационный процесс:</u></p>
                <ol>
                    <li>Начальный квадрат</li>
                    <li>Деление на 9 частей</li>
                    <li>Удаление центрального</li>
                    <li>Повтор для оставшихся</li>
                </ol>
            </div>
            <div style="width: 48%;">
                <p><u>Формальные параметры:</u></p>
                <ul>
                    <li>Коэффициент масштабирования: 1/3</li>
                    <li>Количество копий: 8</li>
                    <li>Фрактальная размерность: log₃8 ≈ 1.8928</li>
                </ul>
            </div>
        </div>
        
        <p><b>🔹 Математические характеристики:</b></p>
        <table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%; margin-bottom: 15px;">
            <tr>
                <th>Свойство</th>
                <th>Значение</th>
            </tr>
            <tr>
                <td>Площадь</td>
                <td>lim<sub>n→∞</sub> S<sub>n</sub> = 0</td>
            </tr>
            <tr>
                <td>Связность</td>
                <td>Полностью несвязный</td>
            </tr>
            <tr>
                <td>Универсальность</td>
                <td>Универсален для планарных кривых</td>
            </tr>
        </table>
        
        <p><b>🔹 Приложения:</b></p>
        <ul>
            <li>Модель пористых сред и перколяции</li>
            <li>Прототип фрактальных антенн</li>
            <li>Тестовый объект в теории меры</li>
        </ul>
        
        <p style="font-style: italic; color: #7f8c8d; margin-top: 10px;">
        Интересный факт: Ковёр Серпинского является двумерным аналогом множества Кантора и сохраняет многие его свойства.
        </p>
    </div>
    """,
    
    "Снежинка Коха": """
    <div style="font-family: 'Times New Roman'; line-height: 1.6;">
        <h3 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px;">Снежинка Коха</h3>
        
        <p><b>🔹 Геометрическое построение:</b></p>
        <ol>
            <li>Начальная фигура: равносторонний треугольник</li>
            <li>Каждая сторона делится на 3 равные части</li>
            <li>Центральная часть заменяется двумя отрезками, образующими новый равносторонний треугольник</li>
            <li>Процесс повторяется рекурсивно для всех новых отрезков</li>
        </ol>
        <p><b>🔹 Парадоксальные свойства:</b></p>
        <table border="1" cellpadding="5" style="border-collapse: collapse; width: 100%; margin-bottom: 15px;">
            <tr>
                <th>Характеристика</th>
                <th>Значение</th>
            </tr>
            <tr>
                <td>Длина</td>
                <td>lim<sub>n→∞</sub> L<sub>n</sub> = ∞</td>
            </tr>
            <tr>
                <td>Площадь</td>
                <td>lim<sub>n→∞</sub> S<sub>n</sub> = 8/5 S<sub>0</sub></td>
            </tr>
            <tr>
                <td>Фрактальная размерность</td>
                <td>log<sub>3</sub>4 ≈ 1.26186</td>
            </tr>
        </table>        
        <p><b>🔹 Историческое значение:</b></p>
        <ul>
            <li>Первый описанный фрактал (1904, Хельге фон Кох)</li>
            <li>Контрпример в анализе: непрерывная, но нигде не дифференцируемая кривая</li>
            <li>Прототип для построения более сложных фрактальных кривых</li>
        </ul>        
        <p><b>🔹 Применения:</b></p>
        <div style="background-color: #f8f9fa; padding: 10px; border-radius: 5px;">
            • Моделирование береговых линий<br>
            • Создание фрактальных антенн<br>
            • Компьютерная графика и генерация текстур
        </div>
    </div>
    """
}

class FractalControls(QWidget):
    render_requested = pyqtSignal()
    save_requested = pyqtSignal()
    reset_requested = pyqtSignal()
    color_map_changed = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.setup_connections()
    
    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Кнопки управления
        self.create_buttons(layout)
        
        # Слайдер для зума
        self.zoom_slider = QSlider(Qt.Horizontal)
        self.zoom_slider.setRange(1, 100)  # 1-100% zoom
        self.zoom_slider.setValue(50)      # Начальное значение (соответствует scale=1.0)
        self.zoom_slider.setTickInterval(10)
        self.zoom_slider.setTickPosition(QSlider.TicksBelow)
        
        zoom_group = QGroupBox("Масштабирование")
        zoom_layout = QVBoxLayout()
        zoom_layout.addWidget(QLabel("Уровень масштабирования:"))
        zoom_layout.addWidget(self.zoom_slider)
        zoom_group.setLayout(zoom_layout)
        layout.insertWidget(1, zoom_group)  # Помещаем после кнопок
        
        # Выбор типа фрактала
        self.create_fractal_type_controls(layout)
        
        # Описание фрактала
        self.fractal_description = QTextBrowser()
        self.fractal_description.setOpenExternalLinks(True)
        self.fractal_description.setStyleSheet("""
            QTextBrowser {
                font-family: 'Times New Roman';
                font-size: 12pt;
                line-height: 1.4;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
            h3 {
                color: #2c3e50;
                border-bottom: 1px solid #eee;
                padding-bottom: 5px;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                margin: 10px 0;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 5px;
                text-align: left;
            }
        """)
        layout.addWidget(self.fractal_description)
        # Параметры Julia
        self.create_julia_controls(layout)
        # Настройки рендеринга
        render_group = QGroupBox("Параметры")
        render_layout = QVBoxLayout()
        # Максимальное количество итераций
        self.max_iter = QSpinBox()
        self.max_iter.setRange(10, 5000)
        self.max_iter.setValue(100)
        render_layout.addWidget(QLabel("К-во итераций (для комплексных фракталов):"))
        render_layout.addWidget(self.max_iter)
        
        # Глубина рекурсии
        self.depth = QSpinBox()
        self.depth.setRange(1, 15)
        self.depth.setValue(5)
        render_layout.addWidget(QLabel("Глубина рекурсии (Для геометрических фракталов):"))
        render_layout.addWidget(self.depth)
        
        render_group.setLayout(render_layout)
        layout.addWidget(render_group)
        # Цветовые схемы
        self.create_color_controls(layout)
        # Помощь
        self.create_help_section(layout)
        
        layout.addStretch()
    
    def get_params(self):
        params = {
            'fractal_type': self.fractal_type.currentData(),
            'max_iter': self.max_iter.value(),
            'depth': self.depth.value()
        }
        
        if params['fractal_type'] == FractalType.JULIA:
            params['c'] = complex(
                self.julia_real.value(),
                self.julia_imag.value())
                
        return params
    
    def create_buttons(self, layout):
        btn_layout = QHBoxLayout()
        
        self.render_btn = QPushButton("Отрисовать Фрактал")
        self.render_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        
        self.reset_btn = QPushButton("Вид по-умолчанию")
        self.reset_btn.setStyleSheet("background-color: #f44336; color: white;")
        
        self.save_btn = QPushButton("Сохранить изображения")
        self.save_btn.setStyleSheet("background-color: #2196F3; color: white;")
        
        btn_layout.addWidget(self.render_btn)
        btn_layout.addWidget(self.reset_btn)
        btn_layout.addWidget(self.save_btn)
        layout.addLayout(btn_layout)
    
    def create_fractal_type_controls(self, layout):
        type_group = QGroupBox("Фрактал")
        type_layout = QVBoxLayout()
        
        self.fractal_type = QComboBox()
        
        # Начальный пустой пункт
        self.fractal_type.addItem("--Выберите фрактал--", None)
        
        # Комплексные фракталы
        self.fractal_type.addItem("--Комплексные фракталы--", None)
        self.fractal_type.addItem("Множество Мандельброта", FractalType.MANDELBROT)
        self.fractal_type.addItem("Множество Жюлиа", FractalType.JULIA)
        self.fractal_type.addItem("Горящий корабль", FractalType.BURNING_SHIP)
        self.fractal_type.addItem("Фрактал Ньютона", FractalType.NEWTON)
        self.fractal_type.addItem("Трикорн", FractalType.TRICORN)

        # Геометрические фракталы
        self.fractal_type.addItem("--Геометрические фракталы--", None)
        self.fractal_type.addItem("Дерево Пифагора", FractalType.PYTHAGORAS_TREE)
        self.fractal_type.addItem("Кривая Леви", FractalType.LEVY_CURVE)
        self.fractal_type.addItem("Треугольник Серпинского", FractalType.SIERPINSKI)
        self.fractal_type.addItem("Кривая Хартера-Хейтуэя (Дракон)", FractalType.DRAGON_CURVE)
        self.fractal_type.addItem("Ковёр Серпинского", FractalType.SIERPINSKI_CARPET)

        # Системные фракталы
        self.fractal_type.addItem("Снежинка Коха", FractalType.KOCH_SNOWFLAKE)

        self.fractal_type.model().item(0).setEnabled(False)
        self.fractal_type.model().item(1).setEnabled(False)
        self.fractal_type.model().item(7).setEnabled(False)
        
        type_layout.addWidget(self.fractal_type)
        type_group.setLayout(type_layout)
        layout.addWidget(type_group)
    
    def create_depth_controls(self, layout):
        self.depth_group = QGroupBox("Fractal Depth")
        depth_layout = QVBoxLayout()
        
        self.depth = QSpinBox()
        self.depth.setRange(1, 15)
        self.depth.setValue(5)
        depth_layout.addWidget(QLabel("Глубина рекурсии"))
        depth_layout.addWidget(self.depth)
        
        self.depth_group.setLayout(depth_layout)
        layout.addWidget(self.depth_group)
    
    def create_julia_controls(self, layout):
        self.julia_group = QGroupBox("Параметры Жюлиа")
        julia_layout = QVBoxLayout()
        
        self.julia_real = QDoubleSpinBox()
        self.julia_real.setRange(-2, 2)
        self.julia_real.setValue(-0.7)
        self.julia_real.setSingleStep(0.01)
        julia_layout.addWidget(QLabel("Действительная часть:"))
        julia_layout.addWidget(self.julia_real)
        
        self.julia_imag = QDoubleSpinBox()
        self.julia_imag.setRange(-2, 2)
        self.julia_imag.setValue(0.27)
        self.julia_imag.setSingleStep(0.01)
        julia_layout.addWidget(QLabel("Мнимая часть:"))
        julia_layout.addWidget(self.julia_imag)
        
        self.julia_group.setLayout(julia_layout)
        self.julia_group.hide()
        layout.addWidget(self.julia_group)
    
    def create_render_controls(self, layout):
        render_group = QGroupBox("Render Settings")
        render_layout = QVBoxLayout()
        
         # Для комплексных фракталов
        self.max_iter = QSpinBox()
        self.max_iter.setRange(10, 5000)
        self.max_iter.setValue(100)
        render_layout.addWidget(QLabel("Max iterations (10-5000):"))
        render_layout.addWidget(self.max_iter)
        
        # Для рекурсивных фракталов
        self.depth = QSpinBox()
        self.depth.setRange(1, 15)
        self.depth.setValue(5)
        render_layout.addWidget(QLabel("Recursion depth (1-15):"))
        render_layout.addWidget(self.depth)
        
        render_group.setLayout(render_layout)
        layout.addWidget(render_group)
    
    def create_color_controls(self, layout):
        color_group = QGroupBox("Цветовая схема (для комплексных фракталов)")
        color_layout = QVBoxLayout()
        
        self.color_scheme = QComboBox()
        self.color_scheme.addItems(["Classic", "Rainbow", "Fire", "Ocean", "Forest", "Violet"])
        color_layout.addWidget(self.color_scheme)
        color_group.setLayout(color_layout)
        layout.addWidget(color_group)
    
    def create_help_section(self, layout):
        help_group = QGroupBox("Помощь")
        help_layout = QVBoxLayout()
        
        help_text = """
        <b>Управление:</b><br>
        • Левый клик + перетаскивание: Панорамирование        
        <b>Параметры:</b><br>
        • Макс. итераций: 10-5000 (для комплексных фракталов)<br>
        • Глубина рекурсии: 1-15<br>
        - Серпинский: макс. 10<br>
        - Кох: макс. 7<br>
        - Дерево: макс. 12<br>
        <b>Примечание:</b><br>
        Область отрисовки изображения: <br>
        x: [-2.5: 2.5] <br>
        y: [-2.5: 2.5]  
        """
        
        help_label = QLabel(help_text)
        help_label.setWordWrap(True)
        help_layout.addWidget(help_label)
        help_group.setLayout(help_layout)
        layout.addWidget(help_group)
    
    def setup_connections(self):
        """Connect signals and slots"""
        # Первоначальная проверка при запуске
        self.toggle_julia_params()
        self.fractal_type.currentIndexChanged.connect(self.toggle_julia_params)
        self.fractal_type.currentIndexChanged.connect(self.update_fractal_description)
        self.color_scheme.currentTextChanged.connect(
            lambda: self.color_map_changed.emit(self.color_scheme.currentText()))
        
        self.render_btn.clicked.connect(self.render_requested.emit)
        self.reset_btn.clicked.connect(self.reset_requested.emit)
        self.save_btn.clicked.connect(self.save_requested.emit)
    
    def toggle_julia_params(self):
        fractal_type = self.fractal_type.currentData()
        
        # Блокировка кнопки, если фрактал не выбран
        self.render_btn.setEnabled(fractal_type is not None)
        
        if fractal_type == FractalType.JULIA:
            self.julia_group.show()
        else:
            self.julia_group.hide()
            
        # Обновляем допустимый диапазон глубины
        if fractal_type is not None:
            self.depth.setRange(1, fractal_type.max_depth)
        
    def create_zoom_controls(self, layout):
        zoom_group = QGroupBox("Zoom Control")
        zoom_layout = QVBoxLayout()
        
        # Добавляем кнопки для быстрого масштабирования
        btn_layout = QHBoxLayout()
        self.zoom_out_btn = QPushButton("-")
        self.zoom_in_btn = QPushButton("+")
        self.reset_zoom_btn = QPushButton("Reset Zoom")
        
        btn_layout.addWidget(self.zoom_out_btn)
        btn_layout.addWidget(self.zoom_in_btn)
        btn_layout.addWidget(self.reset_zoom_btn)
        
        self.zoom_slider = QSlider(Qt.Horizontal)
        self.zoom_slider.setRange(1, 100)
        self.zoom_slider.setValue(50)
        
        zoom_layout.addLayout(btn_layout)
        zoom_layout.addWidget(self.zoom_slider)
        zoom_group.setLayout(zoom_layout)
        layout.addWidget(zoom_group)
        
    def update_fractal_description(self):
        """Обновляет описание выбранного фрактала"""
        fractal_name = self.fractal_type.currentText()
        description = FRACTAL_DESCRIPTIONS.get(fractal_name, """
            <div style="text-align:center; padding:20px;">
                <h3>Описание отсутствует</h3>
                <p>Выберите другой фрактал для просмотра информации</p>
            </div>
        """)
        
        # Прокручиваем к началу при обновлении
        self.fractal_description.setHtml(description)
        self.fractal_description.verticalScrollBar().setValue(0)