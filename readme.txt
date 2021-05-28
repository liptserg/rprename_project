Преобразование файла ui в py
QT6
uic -o window.py -g python window.ui
QT5
pyuic5 -o window.py window.ui

Можно ui грузить так
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      uic.loadUi('mainwindow.ui', self)

Класс windows в view.py можно определить так:
# rprename/views.py
# Snip...

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Window()
        self._setupUI()

    def _setupUI(self):
        self.ui.setupUi(self)

