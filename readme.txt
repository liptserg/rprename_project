�������������� ����� ui � py
QT6
uic -o window.py -g python window.ui
QT5
pyuic5 -o window.py window.ui

����� ui ������� ���
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      uic.loadUi('mainwindow.ui', self)

