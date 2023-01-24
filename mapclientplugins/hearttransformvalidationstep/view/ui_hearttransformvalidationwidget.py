# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hearttransformvalidationwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_HeartTransformValidationWidget(object):
    def setupUi(self, HeartTransformValidationWidget):
        if not HeartTransformValidationWidget.objectName():
            HeartTransformValidationWidget.setObjectName(u"HeartTransformValidationWidget")
        HeartTransformValidationWidget.resize(848, 386)
        self.horizontalLayout = QHBoxLayout(HeartTransformValidationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.control_widget = QWidget(HeartTransformValidationWidget)
        self.control_widget.setObjectName(u"control_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_widget.sizePolicy().hasHeightForWidth())
        self.control_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.control_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.continue_push_button = QPushButton(self.control_widget)
        self.continue_push_button.setObjectName(u"continue_push_button")

        self.horizontalLayout_2.addWidget(self.continue_push_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.control_widget)

        self.display_widget = QWidget(HeartTransformValidationWidget)
        self.display_widget.setObjectName(u"display_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.display_widget.sizePolicy().hasHeightForWidth())
        self.display_widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.display_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 47, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.rms_display_label = QLabel(self.display_widget)
        self.rms_display_label.setObjectName(u"rms_display_label")
        font = QFont()
        font.setPointSize(40)
        self.rms_display_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.rms_display_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 47, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.validation_result_label = QLabel(self.display_widget)
        self.validation_result_label.setObjectName(u"validation_result_label")
        font1 = QFont()
        font1.setPointSize(32)
        self.validation_result_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.validation_result_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 47, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addWidget(self.display_widget)


        self.retranslateUi(HeartTransformValidationWidget)

        QMetaObject.connectSlotsByName(HeartTransformValidationWidget)
    # setupUi

    def retranslateUi(self, HeartTransformValidationWidget):
        HeartTransformValidationWidget.setWindowTitle(QCoreApplication.translate("HeartTransformValidationWidget", u"Heart Transform Validation", None))
        self.continue_push_button.setText(QCoreApplication.translate("HeartTransformValidationWidget", u"Continue", None))
        self.rms_display_label.setText(QCoreApplication.translate("HeartTransformValidationWidget", u"TextLabel", None))
        self.validation_result_label.setText(QCoreApplication.translate("HeartTransformValidationWidget", u"TextLabel", None))
    # retranslateUi

