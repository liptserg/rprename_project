# -*- coding: utf-8 -*-
# rprename/views.py

"""This module provides the RP Renamer main window."""

from collections import deque
from pathlib import Path

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QFileDialog, QWidget
from .rename import Renamer
from .ui.window import Ui_Window

FILTERS = ";;".join(
    (
        "PNG Files (*.png)",
        "JPEG Files (*.jpeg)",
        "JPG Files (*.jpg)",
        "GIF Files (*.gif)",
        "Text Files (*.txt)",
        "Python Files (*.py)",
    )
)


class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        #  self.ui = Ui_Window() if class Window without Ui_Window
        self._files = deque()
        self._filesCount = len(self._files)
        self._setupui()
        self._connectSignalsSlots()

    def _setupui(self):
        #  self.ui.setupUi(self)
        self.setupUi(self)

    def _connectSignalsSlots(self):
        self.loadFilesButton.clicked.connect(self.loadFiles)
        self.renameFilesButton.clicked.connect(self.renameFiles)

    def loadFiles(self):
        self.dstFileList.clear()
        if self.dirEdit.text():
            initDir = self.dirEdit.text()
        else:
            initDir = str(Path.home())
        files, filter = QFileDialog.getOpenFileNames(
            self, "Choose Files to Rename", initDir, filter=FILTERS
        )
        if len(files) > 0:
            fileExtension = filter[filter.index("*") : -1]
            self.extensionLabel.setText(fileExtension)
            srcDirName = str(Path(files[0]).parent)
            self.dirEdit.setText(srcDirName)
            for file in files:
                self._files.append(Path(file))
                self.srcFileList.addItem(file)
            self._filesCount = len(self._files)

    def renameFiles(self):
        self._runRenamerThread()

    def _runRenamerThread(self):
        prefix = self.prefixEdit.text()
        self._thread = QThread()
        self._renamer = Renamer(
            files=tuple(self._files),
            prefix=prefix,
        )
        self._renamer.moveToThread(self._thread)
        # Rename
        self._thread.started.connect(self._renamer.renameFiles)
        # Update state
        self._renamer.renamedFile.connect(self._updateStateWhenFileRenamed)
        # Clean up
        self._renamer.finished.connect(self._thread.quit)
        self._renamer.finished.connect(self._renamer.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        # Run the thread
        self._thread.start()

    def _updateStateWhenFileRenamed(self, newFile):
        self._files.popleft()
        self.srcFileList.takeItem(0)
        self.dstFileList.addItem(str(newFile))

#TODO log4cplus:ERROR No appenders could be found for logger (DSL).
#TODO log4cplus:ERROR Please initialize the log4cplus system properly.