# -*- coding: utf-8 -*-
# rprename/views.py

"""This module provides the RP Renamer main window."""

from PySide6.QtWidgets import QWidget

from .ui.window import Ui_Window

class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        #  self.ui = Ui_Window()
        self._setupUI()

    def _setupUI(self):
        #  self.ui.setupUi(self)
        self.setupUi(self)
