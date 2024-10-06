from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([])

window = QWidget()
window.setWindowTitle('Рандомер 2.0')
window.resize(800, 500)
window.setStyleSheet("background-color: #f0f0f0;")

# Создаем основной макет
main_layout = QVBoxLayout()

# Создаем меню
menu_bar = QMenuBar()
file_menu = menu_bar.addMenu("Файл")
control_menu = menu_bar.addMenu("Управление")

exit_action = QAction("Завершить работу", window)
exit_action.triggered.connect(app.quit)
file_menu.addAction(exit_action)

clear_action = QAction("Очистить", window)
clear_action.triggered.connect(lambda: [line_edit.clear() for line_edit in line_edits])
file_menu.addAction(clear_action)

sleep_action = QAction("Спящий режим", window)
sleep_action.triggered.connect(lambda: QMessageBox.information(window, "Спящий режим", "Программа переходит в спящий режим"))
file_menu.addAction(sleep_action)

control_menu.addAction(clear_action)
control_menu.addAction(exit_action)
control_menu.addAction(sleep_action)

main_layout.setMenuBar(menu_bar)

# Заголовок
title = QLabel("Введите свои варианты ответов, чтобы начать работу рандомера:")
title.setFont(QFont('Arial', 16))
title.setAlignment(Qt.AlignCenter)
main_layout.addWidget(title)

# Создаем сетку для ввода вариантов
grid_layout = QGridLayout()

labels = ["Вариант 1", "Вариант 2", "Вариант 3", "Вариант 4"]
line_edits = []

for i, label_text in enumerate(labels):
    label = QLabel(label_text)
    label.setFont(QFont('Arial', 12))
    line_edit = QLineEdit()
    line_edit.setFont(QFont('Arial', 12))
    line_edit.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px;")
    grid_layout.addWidget(label, i, 0)
    grid_layout.addWidget(line_edit, i, 1)
    line_edits.append(line_edit)

main_layout.addLayout(grid_layout)

# Кнопка
push = QPushButton("Поехали")
push.setFont(QFont('Arial', 14))
push.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px;")
main_layout.addWidget(push)

window.setLayout(main_layout)

commands = []

def assign():
    commands.clear()
    for line_edit in line_edits:
        commands.append(line_edit.text())
    af = randint(0, 3)
    inform = QMessageBox()
    inform.setWindowTitle('Результат')
    inform.setText(f'{commands[af]}\nСпасибо за использование нашей программы')
    inform.exec_()

push.clicked.connect(assign)
window.show()
app.exec_()
