# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(534, 386)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Window.sizePolicy().hasHeightForWidth())
        Window.setSizePolicy(sizePolicy)
        self.widget = QWidget(Window)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 11, 518, 362))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 15))
        self.label.setMaximumSize(QSize(16777215, 15))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dirEdit = QLineEdit(self.widget)
        self.dirEdit.setObjectName(u"dirEdit")
        self.dirEdit.setMinimumSize(QSize(0, 30))
        self.dirEdit.setMaximumSize(QSize(16777215, 30))
        self.dirEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.dirEdit, 1, 0, 1, 1)

        self.loadFilesButton = QPushButton(self.widget)
        self.loadFilesButton.setObjectName(u"loadFilesButton")
        self.loadFilesButton.setMinimumSize(QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        self.loadFilesButton.setFont(font)

        self.gridLayout.addWidget(self.loadFilesButton, 1, 2, 1, 1)

        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.srcFileList = QListWidget(self.widget1)
        self.srcFileList.setObjectName(u"srcFileList")

        self.verticalLayout.addWidget(self.srcFileList)

        self.splitter.addWidget(self.widget1)
        self.widget2 = QWidget(self.splitter)
        self.widget2.setObjectName(u"widget2")
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.dstFileList = QListWidget(self.widget2)
        self.dstFileList.setObjectName(u"dstFileList")

        self.verticalLayout_2.addWidget(self.dstFileList)

        self.splitter.addWidget(self.widget2)

        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 15))
        self.label_4.setMaximumSize(QSize(16777215, 15))

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.prefixEdit = QLineEdit(self.widget)
        self.prefixEdit.setObjectName(u"prefixEdit")
        self.prefixEdit.setMinimumSize(QSize(0, 30))
        self.prefixEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.prefixEdit, 4, 0, 1, 1)

        self.extensionLabel = QLabel(self.widget)
        self.extensionLabel.setObjectName(u"extensionLabel")
        self.extensionLabel.setMinimumSize(QSize(0, 30))
        self.extensionLabel.setMaximumSize(QSize(16777215, 30))
        self.extensionLabel.setFont(font)

        self.gridLayout.addWidget(self.extensionLabel, 4, 1, 1, 1)

        self.renameFilesButton = QPushButton(self.widget)
        self.renameFilesButton.setObjectName(u"renameFilesButton")
        self.renameFilesButton.setMinimumSize(QSize(0, 30))
        self.renameFilesButton.setMaximumSize(QSize(16777215, 30))
        self.renameFilesButton.setFont(font)

        self.gridLayout.addWidget(self.renameFilesButton, 4, 2, 1, 1)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 3)


        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"RP Renamer", None))
        self.label.setText(QCoreApplication.translate("Window", u"Last Source Directory:.", None))
        self.loadFilesButton.setText(QCoreApplication.translate("Window", u"&Load Files", None))
        self.label_2.setText(QCoreApplication.translate("Window", u"Files to Rename", None))
        self.label_3.setText(QCoreApplication.translate("Window", u"Renamed Files", None))
        self.label_4.setText(QCoreApplication.translate("Window", u"Filename Prefix:", None))
        self.prefixEdit.setText(QCoreApplication.translate("Window", u"Rename your files to\u2026.", None))
        self.extensionLabel.setText(QCoreApplication.translate("Window", u".jpg", None))
        self.renameFilesButton.setText(QCoreApplication.translate("Window", u"&Rename", None))
    # retranslateUi

