# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arayüzPart3xECiUN.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(872, 681)
        MainWindow.setStyleSheet(u"background-color: #f0f4f8; /* G\u00f6rseldeki a\u00e7\u0131k mavi/gri ton */")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.StackWidget = QStackedWidget(self.centralwidget)
        self.StackWidget.setObjectName(u"StackWidget")
        self.StackWidget.setMinimumSize(QSize(750, 500))
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.verticalLayout_4 = QVBoxLayout(self.LoginPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Logo = QLabel(self.LoginPage)
        self.Logo.setObjectName(u"Logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMinimumSize(QSize(200, 100))
        self.Logo.setMaximumSize(QSize(200, 100))
        self.Logo.setStyleSheet(u"background-color: #f0f4f8; /* G\u00f6rseldeki a\u00e7\u0131k mavi/gri ton */")
        self.Logo.setPixmap(QPixmap(u"../../../../Desktop/Yeni klas\u00f6r/QT projects/VTYS/proje ad\u0131mlar/Ekran g\u00f6r\u00fcnt\u00fcs\u00fc 2025-12-08 131220.png"))
        self.Logo.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.Logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Baslik = QLabel(self.LoginPage)
        self.Baslik.setObjectName(u"Baslik")
        sizePolicy.setHeightForWidth(self.Baslik.sizePolicy().hasHeightForWidth())
        self.Baslik.setSizePolicy(sizePolicy)
        self.Baslik.setMinimumSize(QSize(400, 50))
        self.Baslik.setMaximumSize(QSize(400, 50))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(240, 244, 248, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        self.Baslik.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Bodoni MT"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.Baslik.setFont(font)
        self.Baslik.setStyleSheet(u"font: 700 14pt \"Bodoni MT\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.Baslik.setTextFormat(Qt.TextFormat.AutoText)
        self.Baslik.setScaledContents(False)
        self.Baslik.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.Baslik, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.GirisFrame = QFrame(self.LoginPage)
        self.GirisFrame.setObjectName(u"GirisFrame")
        sizePolicy.setHeightForWidth(self.GirisFrame.sizePolicy().hasHeightForWidth())
        self.GirisFrame.setSizePolicy(sizePolicy)
        self.GirisFrame.setMinimumSize(QSize(400, 350))
        self.GirisFrame.setMaximumSize(QSize(400, 900))
        self.GirisFrame.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border-radius: 15px; /* K\u00f6\u015feleri yuvarlat\u0131r */\n"
"    border: 1px solid #e0e0e0;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.GirisFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.GirisFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"border: transparent")
        self.label.setWordWrap(False)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.GirisFrame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"   border: 1px solid #ccc;\n"
"\n"
"\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: #333333; /* Yaz\u0131 rengini KOYU GR\u0130/S\u0130YAH yapar */\n"
"    background-color: #ffffff; /* Arka plan\u0131 BEYAZ yapar */\n"
"}\n"
"/* A\u00e7\u0131lan listenin kendisi */\n"
"QComboBox QAbstractItemView {\n"
"    color: #333333; /* Liste elemanlar\u0131n\u0131n yaz\u0131 rengi */\n"
"    background-color: #ffffff; /* Liste arka plan\u0131 */\n"
"    selection-background-color: #2b5cff; /* \u00dczerine gelince mavi olsun */\n"
"    selection-color: white; /* Se\u00e7ili olan\u0131n yaz\u0131s\u0131 beyaz olsun */\n"
"}")

        self.verticalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(self.GirisFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"color: rgb(0,0,0);\n"
"border:transparent\n"
"")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.GirisFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    background-color: #f9f9f9; /* Hafif gri arka plan */\n"
"    color: #333333; /* Yaz\u0131 rengini KOYU GR\u0130/S\u0130YAH yapar - \u00c7\u00d6Z\u00dcM BU SATIRDA */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2b5cff;\n"
"    background-color: #ffffff; /* T\u0131klay\u0131nca arka plan tam beyaz olsun */\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.GirisFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setStyleSheet(u"color: rgb(0,0,0);\n"
"border:transparent\n"
"")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.GirisFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    background-color: #f9f9f9; /* Hafif gri arka plan */\n"
"    color: #333333; /* Yaz\u0131 rengini KOYU GR\u0130/S\u0130YAH yapar - \u00c7\u00d6Z\u00dcM BU SATIRDA */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2b5cff;\n"
"    background-color: #ffffff; /* T\u0131klay\u0131nca arka plan tam beyaz olsun */\n"
"}")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.pushButton = QPushButton(self.GirisFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #2b5cff; /* O parlak mavi renk */\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1a45d0; /* \u00dczerine gelince koyula\u015fs\u0131n */\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.GirisFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.StackWidget.addWidget(self.LoginPage)
        self.investorPage = QWidget()
        self.investorPage.setObjectName(u"investorPage")
        self.verticalLayout_3 = QVBoxLayout(self.investorPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.investorPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(795, 0))
        self.scrollArea.setStyleSheet(u"scrollArea {\n"
"    background-color: transparent; /* Kendisi \u015feffaf olsun */\n"
"    border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 811, 918))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 80))
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 10, 49, 16))
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 91, 71))
        self.label_5.setPixmap(QPixmap(u"../../../../Desktop/Yeni klas\u00f6r/QT projects/VTYS/proje ad\u0131mlar/Ekran g\u00f6r\u00fcnt\u00fcs\u00fc 2025-12-08 152749.png"))
        self.KullaniciAdiLabel = QLabel(self.widget_2)
        self.KullaniciAdiLabel.setObjectName(u"KullaniciAdiLabel")
        self.KullaniciAdiLabel.setGeometry(QRect(120, 50, 91, 16))
        self.KullaniciAdiLabel.setStyleSheet(u"color: rgb(0,0,0)\n"
"")
        self.YatirimciPaneliLabel = QLabel(self.widget_2)
        self.YatirimciPaneliLabel.setObjectName(u"YatirimciPaneliLabel")
        self.YatirimciPaneliLabel.setGeometry(QRect(100, 20, 141, 16))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.YatirimciPaneliLabel.setFont(font1)
        self.YatirimciPaneliLabel.setStyleSheet(u"color : rgb(150,150,150)\n"
"")
        self.ExitButton = QPushButton(self.widget_2)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setGeometry(QRect(660, 25, 131, 31))
        self.ExitButton.setStyleSheet(u"color: rgb(0,0,0)\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../../Desktop/Yeni klas\u00f6r/QT projects/VTYS/proje ad\u0131mlar/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ExitButton.setIcon(icon)
        self.ExitButton.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.widget_2)

        self.SekmeGecisFrame = QFrame(self.scrollAreaWidgetContents)
        self.SekmeGecisFrame.setObjectName(u"SekmeGecisFrame")
        self.SekmeGecisFrame.setMinimumSize(QSize(0, 90))
        self.SekmeGecisFrame.setStyleSheet(u"/* 1. \u00dc\u00c7 BUTON \u0130\u00c7\u0130N ORTAK TEMEL AYARLAR */\n"
"QPushButton#HesaplarimveBakiyeButon,\n"
"QPushButton#IslemGecmisiButon,\n"
"QPushButton#PortfoyDurumuButon {\n"
"    border: none;\n"
"	background:none;\n"
"    background-color: transparent; /* Normal halde \u015feffaf */\n"
"    color: rgb(129, 129, 129);\n"
"	color:rgb(0,0,0);\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    padding-bottom: 15px;\n"
"    padding-top: 15px;\n"
"    border-bottom: 3px solid transparent;\n"
"    text-align: left;\n"
"}\n"
"\n"
"/* 2. MOUSE \u00dcZER\u0130NE GEL\u0130NCE (HOVER) */\n"
"QPushButton#HesaplarimveBakiyeButon:hover,\n"
"QPushButton#IslemGecmisiButon:hover,\n"
"QPushButton#PortfoyDurumuButon:hover {\n"
"    color: #101828;\n"
"    background-color: transparent; /* Hover'da da arka plan gelmesin */\n"
"}\n"
"\n"
"/* 3. BUTONA BASILI TUTULDU\u011eUNDA (PRESSED) - Sorunu \u00c7\u00f6zen K\u0131s\u0131m */\n"
"QPushButton#HesaplarimveBakiyeButon:pressed,\n"
"QPushButton#IslemGecmisiBut"
                        "on:pressed,\n"
"QPushButton#PortfoyDurumuButon:pressed {\n"
"    background-color: transparent; /* Bas\u0131nca mavi kutu \u00e7\u0131kmas\u0131n\u0131 engeller */\n"
"}\n"
"\n"
"/* 4. BUTON SE\u00c7\u0130L\u0130 OLDU\u011eUNDA (CHECKED) - Sorunu \u00c7\u00f6zen K\u0131s\u0131m */\n"
"QPushButton#HesaplarimveBakiyeButon:checked,\n"
"QPushButton#IslemGecmisiButon:checked,\n"
"QPushButton#PortfoyDurumuButon:checked {\n"
"    color: #2b5cff;\n"
"    border-bottom: 3px solid #2b5cff;\n"
"    background-color: transparent; /* Se\u00e7iliyken arka plan\u0131 \u015feffaf zorla */\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.SekmeGecisFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.HesaplarimveBakiyeButon = QPushButton(self.SekmeGecisFrame)
        self.HesaplarimveBakiyeButon.setObjectName(u"HesaplarimveBakiyeButon")
        self.HesaplarimveBakiyeButon.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.HesaplarimveBakiyeButon.setStyleSheet(u"")
        self.HesaplarimveBakiyeButon.setCheckable(True)
        self.HesaplarimveBakiyeButon.setChecked(True)
        self.HesaplarimveBakiyeButon.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.HesaplarimveBakiyeButon)

        self.IslemGecmisiButon = QPushButton(self.SekmeGecisFrame)
        self.IslemGecmisiButon.setObjectName(u"IslemGecmisiButon")
        self.IslemGecmisiButon.setStyleSheet(u"")
        self.IslemGecmisiButon.setCheckable(True)
        self.IslemGecmisiButon.setAutoExclusive(True)
        self.IslemGecmisiButon.setFlat(True)

        self.horizontalLayout.addWidget(self.IslemGecmisiButon)

        self.PortfoyDurumuButon = QPushButton(self.SekmeGecisFrame)
        self.PortfoyDurumuButon.setObjectName(u"PortfoyDurumuButon")
        self.PortfoyDurumuButon.setStyleSheet(u"")
        self.PortfoyDurumuButon.setCheckable(True)
        self.PortfoyDurumuButon.setAutoExclusive(True)
        self.PortfoyDurumuButon.setFlat(True)

        self.horizontalLayout.addWidget(self.PortfoyDurumuButon)


        self.verticalLayout_5.addWidget(self.SekmeGecisFrame)

        self.infoOfInvestor = QFrame(self.scrollAreaWidgetContents)
        self.infoOfInvestor.setObjectName(u"infoOfInvestor")
        self.infoOfInvestor.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.infoOfInvestor.sizePolicy().hasHeightForWidth())
        self.infoOfInvestor.setSizePolicy(sizePolicy1)
        self.infoOfInvestor.setMinimumSize(QSize(0, 125))
        self.infoOfInvestor.setStyleSheet(u"/* Ana Mavi Kart */\n"
"QFrame#infoOfInvestor {\n"
"    /* Soldan sa\u011fa modern mavi gradient */\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #2563eb, stop:1 #4f46e5);\n"
"\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u0130\u00e7indeki Ba\u015fl\u0131k Yaz\u0131lar\u0131 (\u00d6rn: \"Toplam Bakiye\") */\n"
"QLabel#toplambakiye{\n"
"    color: #e0e7ff; /* Hafif soluk beyaz */\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"}\n"
"\n"
"/* \u0130\u00e7indeki De\u011ferler (\u00d6rn: \"\u20ba850.000\") */\n"
"QLabel#toplambakiye1 {\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    font-size: 24px;\n"
"}")
        self.toplambakiye = QLabel(self.infoOfInvestor)
        self.toplambakiye.setObjectName(u"toplambakiye")
        self.toplambakiye.setGeometry(QRect(30, 10, 91, 16))
        self.toplambakiye.setStyleSheet(u"background-color: transparent; ")
        self.toplambakiye1 = QLabel(self.infoOfInvestor)
        self.toplambakiye1.setObjectName(u"toplambakiye1")
        self.toplambakiye1.setGeometry(QRect(30, 30, 131, 21))
        self.toplambakiye1.setStyleSheet(u"background-color: transparent; ")
        self.RiskProfiliFrame = QFrame(self.infoOfInvestor)
        self.RiskProfiliFrame.setObjectName(u"RiskProfiliFrame")
        self.RiskProfiliFrame.setGeometry(QRect(250, 60, 219, 49))
        self.RiskProfiliFrame.setStyleSheet(u"QFrame#RiskProfiliFrame {\n"
"    background-color: rgba(255, 255, 255, 0.15); /* %15 G\u00f6r\u00fcn\u00fcrl\u00fckte Beyaz (Cam Efekti) */\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#riskprofili{\n"
"    background-color: transparent; /* Yaz\u0131lar\u0131n arkas\u0131 \u015feffaf kals\u0131n */\n"
"    color: white;\n"
"}\n"
"QLabel#riskprofili1{\n"
"    background-color: transparent; /* Yaz\u0131lar\u0131n arkas\u0131 \u015feffaf kals\u0131n */\n"
"    color: white;\n"
"}")
        self.RiskProfiliFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RiskProfiliFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.riskprofili = QLabel(self.RiskProfiliFrame)
        self.riskprofili.setObjectName(u"riskprofili")
        self.riskprofili.setGeometry(QRect(10, 2, 81, 16))
        self.riskprofili1 = QLabel(self.RiskProfiliFrame)
        self.riskprofili1.setObjectName(u"riskprofili1")
        self.riskprofili1.setGeometry(QRect(10, 28, 81, 21))
        self.BrokerinfoFrame = QFrame(self.infoOfInvestor)
        self.BrokerinfoFrame.setObjectName(u"BrokerinfoFrame")
        self.BrokerinfoFrame.setGeometry(QRect(480, 60, 219, 49))
        self.BrokerinfoFrame.setStyleSheet(u"QFrame#BrokerinfoFrame {\n"
"    background-color: rgba(255, 255, 255, 0.15); /* %15 G\u00f6r\u00fcn\u00fcrl\u00fckte Beyaz (Cam Efekti) */\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#sorumlubroker{\n"
"    background-color: transparent; /* Yaz\u0131lar\u0131n arkas\u0131 \u015feffaf kals\u0131n */\n"
"    color: white;\n"
"}\n"
"QLabel#sorumlubroker1{\n"
"    background-color: transparent; /* Yaz\u0131lar\u0131n arkas\u0131 \u015feffaf kals\u0131n */\n"
"    color: white;\n"
"}")
        self.BrokerinfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BrokerinfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.sorumlubroker = QLabel(self.BrokerinfoFrame)
        self.sorumlubroker.setObjectName(u"sorumlubroker")
        self.sorumlubroker.setGeometry(QRect(10, 2, 91, 16))
        self.sorumlubroker1 = QLabel(self.BrokerinfoFrame)
        self.sorumlubroker1.setObjectName(u"sorumlubroker1")
        self.sorumlubroker1.setGeometry(QRect(10, 28, 101, 16))
        self.HesapSayisiFrame = QFrame(self.infoOfInvestor)
        self.HesapSayisiFrame.setObjectName(u"HesapSayisiFrame")
        self.HesapSayisiFrame.setGeometry(QRect(20, 60, 219, 49))
        self.HesapSayisiFrame.setStyleSheet(u"QFrame#HesapSayisiFrame {\n"
"    background-color: rgba(255, 255, 255, 0.15); /* %15 G\u00f6r\u00fcn\u00fcrl\u00fckte Beyaz (Cam Efekti) */\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#HesapSayisi{\n"
"    background-color: transparent; /* Yaz\u0131lar\u0131n arkas\u0131 \u015feffaf kals\u0131n */\n"
"    color: white;\n"
"}\n"
"QLabel#HesapSayisi1{\n"
"    background-color: transparent; /* Yaz\u0131lar\u0131n arkas\u0131 \u015feffaf kals\u0131n */\n"
"    color: white;\n"
"}")
        self.HesapSayisiFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HesapSayisiFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.HesapSayisi = QLabel(self.HesapSayisiFrame)
        self.HesapSayisi.setObjectName(u"HesapSayisi")
        self.HesapSayisi.setGeometry(QRect(10, 0, 91, 16))
        self.HesapSayisi1 = QLabel(self.HesapSayisiFrame)
        self.HesapSayisi1.setObjectName(u"HesapSayisi1")
        self.HesapSayisi1.setGeometry(QRect(10, 28, 101, 16))

        self.verticalLayout_5.addWidget(self.infoOfInvestor)

        self.HesaplarimInfo = QLabel(self.scrollAreaWidgetContents)
        self.HesaplarimInfo.setObjectName(u"HesaplarimInfo")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.HesaplarimInfo.setFont(font2)
        self.HesaplarimInfo.setStyleSheet(u"color:rgb(0,0,0)\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.HesaplarimInfo)

        self.HesaplarimInfoFrame = QFrame(self.scrollAreaWidgetContents)
        self.HesaplarimInfoFrame.setObjectName(u"HesaplarimInfoFrame")
        self.HesaplarimInfoFrame.setStyleSheet(u"/* ANA KART (Beyaz alan) */\n"
"QFrame#HaplarimInfoFrame {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #eaecf0;\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"/* \u00dcst ikon alan\u0131 */\n"
"QFrame#IconFrame {\n"
"    background-color: #eef4ff;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* GENEL YAZI AYARI */\n"
"QLabel {\n"
"    background: transparent;\n"
"    color: #101828;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"/* Hesap No */\n"
"QLabel#HesapNoLabel1 {\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Yat\u0131r\u0131m Hesab\u0131 alt yaz\u0131 */\n"
"QLabel#YatirimHesabiLabel {\n"
"    font-size: 13px;\n"
"    color: #667085;\n"
"}\n"
"\n"
"/* Sa\u011fdaki Bakiye Ba\u015fl\u0131\u011f\u0131 */\n"
"QLabel#BakiyeBaslikLabel {\n"
"    font-size: 12px;\n"
"    color: #667085;\n"
"}\n"
"\n"
"/* Sa\u011fdaki Bakiye De\u011feri */\n"
"QLabel#BakiyeLabel1 {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #101828;\n"
"}\n"
"\n"
"/* \u00dc"
                        "\u00c7 ALT KART (A\u00e7\u0131l\u0131\u015f Tarihi, Komisyon, Durum) */\n"
"QFrame#HesaplarimInfoFrame1,\n"
"QFrame#HesaplarimInfoFrame2,\n"
"QFrame#HesaplarimInfoFrame3 {\n"
"    background-color: #f9fafb;\n"
"    border-radius: 12px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Alt Kart Ba\u015fl\u0131klar\u0131 (A\u00e7\u0131l\u0131\u015f Tarihi \u2014 Komisyon Plan\u0131 \u2014 Durum) */\n"
"QLabel#HesapAcilisBaslik,\n"
"QLabel#KomisyonBaslik,\n"
"QLabel#DurumBaslik {\n"
"    font-size: 13px;\n"
"    color: #667085;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"/* \u0130\u00e7 de\u011ferler */\n"
"QLabel#HesapAcilisDeger,\n"
"QLabel#KomisyonDeger,\n"
"QLabel#DurumDeger {\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"    color: #101828;\n"
"}\n"
"\n"
"/* Komisyon alt a\u00e7\u0131klama (Min \u20ba50 - %1) */\n"
"QLabel#KomisyonAltYazi {\n"
"    font-size: 12px;\n"
"    color: #667085;\n"
"}\n"
"\n"
"/* ye\u015fil Aktif Rozeti */\n"
"QLabel#DurumLabel1 {\n"
"    background-color: #d1fadf;\n"
"    color: #0"
                        "27a48;\n"
"    border-radius: 12px;\n"
"    padding: 4px 12px;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.HesaplarimInfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HesaplarimInfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.HesaplarimInfoFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.HesaplarimInfoFrame1 = QFrame(self.HesaplarimInfoFrame)
        self.HesaplarimInfoFrame1.setObjectName(u"HesaplarimInfoFrame1")
        sizePolicy.setHeightForWidth(self.HesaplarimInfoFrame1.sizePolicy().hasHeightForWidth())
        self.HesaplarimInfoFrame1.setSizePolicy(sizePolicy)
        self.HesaplarimInfoFrame1.setMinimumSize(QSize(0, 160))
        self.HesaplarimInfoFrame1.setStyleSheet(u"background:rgb(255,255,255)")
        self.HesaplarimInfoFrame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.HesaplarimInfoFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.HesapNoLabel = QLabel(self.HesaplarimInfoFrame1)
        self.HesapNoLabel.setObjectName(u"HesapNoLabel")
        self.HesapNoLabel.setGeometry(QRect(20, 10, 53, 16))
        self.HesapNoLabel1 = QLabel(self.HesaplarimInfoFrame1)
        self.HesapNoLabel1.setObjectName(u"HesapNoLabel1")
        self.HesapNoLabel1.setGeometry(QRect(80, 8, 74, 22))
        self.BakiyeLabel = QLabel(self.HesaplarimInfoFrame1)
        self.BakiyeLabel.setObjectName(u"BakiyeLabel")
        self.BakiyeLabel.setGeometry(QRect(740, 10, 34, 16))
        self.BakiyeLabel.setStyleSheet(u"top:right")
        self.YatirimHesabiLabel = QLabel(self.HesaplarimInfoFrame1)
        self.YatirimHesabiLabel.setObjectName(u"YatirimHesabiLabel")
        self.YatirimHesabiLabel.setGeometry(QRect(40, 30, 82, 18))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        self.YatirimHesabiLabel.setFont(font3)
        self.BakiyeLabel1 = QLabel(self.HesaplarimInfoFrame1)
        self.BakiyeLabel1.setObjectName(u"BakiyeLabel1")
        self.BakiyeLabel1.setGeometry(QRect(700, 30, 73, 24))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        self.BakiyeLabel1.setFont(font4)
        self.BakiyeLabel1.setMidLineWidth(0)
        self.HesaplarimInfoFrame2 = QFrame(self.HesaplarimInfoFrame1)
        self.HesaplarimInfoFrame2.setObjectName(u"HesaplarimInfoFrame2")
        self.HesaplarimInfoFrame2.setGeometry(QRect(-1, 50, 781, 84))
        self.HesaplarimInfoFrame2.setStyleSheet(u"\n"
"QFrame#HesapAcilisFrame,\n"
"QFrame#HesapDurumFrame,\n"
"QFrame#KomisyonPlaniFrame{\n"
"background:rgb(230,230,230);\n"
"border-radius: 16px;\n"
"}")
        self.HesaplarimInfoFrame2.setFrameShape(QFrame.Shape.StyledPanel)
        self.HesaplarimInfoFrame2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.HesaplarimInfoFrame2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.HesapAcilisFrame = QFrame(self.HesaplarimInfoFrame2)
        self.HesapAcilisFrame.setObjectName(u"HesapAcilisFrame")
        self.HesapAcilisFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HesapAcilisFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.HesapAcilisFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.HesapAcilisLabel = QLabel(self.HesapAcilisFrame)
        self.HesapAcilisLabel.setObjectName(u"HesapAcilisLabel")
        self.HesapAcilisLabel.setStyleSheet(u"background:transparent")

        self.verticalLayout_7.addWidget(self.HesapAcilisLabel)

        self.HesapAcilisLabel1 = QLabel(self.HesapAcilisFrame)
        self.HesapAcilisLabel1.setObjectName(u"HesapAcilisLabel1")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.HesapAcilisLabel1.setFont(font5)
        self.HesapAcilisLabel1.setStyleSheet(u"background:transparent")

        self.verticalLayout_7.addWidget(self.HesapAcilisLabel1)


        self.horizontalLayout_2.addWidget(self.HesapAcilisFrame)

        self.KomisyonPlaniFrame = QFrame(self.HesaplarimInfoFrame2)
        self.KomisyonPlaniFrame.setObjectName(u"KomisyonPlaniFrame")
        self.KomisyonPlaniFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.KomisyonPlaniFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.KomisyonPlaniFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.KomisyonLabel = QLabel(self.KomisyonPlaniFrame)
        self.KomisyonLabel.setObjectName(u"KomisyonLabel")
        self.KomisyonLabel.setStyleSheet(u"background:transparent")

        self.verticalLayout_9.addWidget(self.KomisyonLabel)

        self.KomisyonLabel1 = QLabel(self.KomisyonPlaniFrame)
        self.KomisyonLabel1.setObjectName(u"KomisyonLabel1")
        self.KomisyonLabel1.setStyleSheet(u"background:transparent")

        self.verticalLayout_9.addWidget(self.KomisyonLabel1)


        self.horizontalLayout_2.addWidget(self.KomisyonPlaniFrame)

        self.HesapDurumFrame = QFrame(self.HesaplarimInfoFrame2)
        self.HesapDurumFrame.setObjectName(u"HesapDurumFrame")
        self.HesapDurumFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HesapDurumFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.HesapDurumFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, -1, -1, -1)
        self.DurumLabel = QLabel(self.HesapDurumFrame)
        self.DurumLabel.setObjectName(u"DurumLabel")
        self.DurumLabel.setStyleSheet(u"background:transparent")

        self.verticalLayout_8.addWidget(self.DurumLabel)

        self.DurumLabel1 = QLabel(self.HesapDurumFrame)
        self.DurumLabel1.setObjectName(u"DurumLabel1")
        self.DurumLabel1.setMinimumSize(QSize(50, 0))
        self.DurumLabel1.setMaximumSize(QSize(50, 16777215))
        self.DurumLabel1.setStyleSheet(u"background:transparent;\n"
"background-color: rgb(170, 255, 127);       /* A\u00e7\u0131k sar\u0131 zemin */\n"
"    color: rgb(0, 170, 0);                  /* Koyu sar\u0131/turuncu yaz\u0131 */\n"
"    border-radius: 12px;             /* Tam yuvarlak kenarlar */\n"
"    padding: 4px 12px;               /* \u0130\u00e7eriden bo\u015fluk (Yaz\u0131 kenara yap\u0131\u015fmas\u0131n) */\n"
"    font-weight: bold;               /* Kal\u0131n yaz\u0131 */\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"border-radius: 9px;")

        self.verticalLayout_8.addWidget(self.DurumLabel1)


        self.horizontalLayout_2.addWidget(self.HesapDurumFrame)


        self.verticalLayout_6.addWidget(self.HesaplarimInfoFrame1)

        self.frame = QFrame(self.HesaplarimInfoFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(780, 370))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(774, 150))
        self.frame_4.setMaximumSize(QSize(774, 170))
        self.frame_4.setStyleSheet(u"background-color: #FFFFFF;       /* Beyaz arka plan */\n"
"    border: 1px solid #E0E0E0;       /* \u0130nce gri \u00e7er\u00e7eve */\n"
"    border-radius: 12px;             /* K\u00f6\u015feleri yumu\u015fatma */")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.RiskProfiliFrameLabel = QLabel(self.frame_4)
        self.RiskProfiliFrameLabel.setObjectName(u"RiskProfiliFrameLabel")
        sizePolicy.setHeightForWidth(self.RiskProfiliFrameLabel.sizePolicy().hasHeightForWidth())
        self.RiskProfiliFrameLabel.setSizePolicy(sizePolicy)
        self.RiskProfiliFrameLabel.setMinimumSize(QSize(0, 30))
        self.RiskProfiliFrameLabel.setMaximumSize(QSize(16777215, 20))
        self.RiskProfiliFrameLabel.setStyleSheet(u"font-weight: bold;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"border: transparent")

        self.verticalLayout_11.addWidget(self.RiskProfiliFrameLabel)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setStyleSheet(u"background-color: #F8F9FA;       /* \u00c7ok a\u00e7\u0131k gri arka plan */\n"
"    border: 1px solid #EAEAEA;       /* Daha da ince \u00e7er\u00e7eve */\n"
"    border-radius: 8px;              /* \u0130\u00e7 k\u00f6\u015fe yuvarlama */")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet(u"border:transparent")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_8.setLineWidth(1)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 211, 31))
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"background-color: #FFF9C4;       /* A\u00e7\u0131k sar\u0131 zemin */\n"
"    color: #FBC02D;                  /* Koyu sar\u0131/turuncu yaz\u0131 */\n"
"    border-radius: 12px;             /* Tam yuvarlak kenarlar */\n"
"    padding: 4px 12px;               /* \u0130\u00e7eriden bo\u015fluk (Yaz\u0131 kenara yap\u0131\u015fmas\u0131n) */\n"
"    font-weight: bold;               /* Kal\u0131n yaz\u0131 */\n"
"    font-family: \"Segoe UI\", sans-serif;")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 50, 201, 16))
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(u"color: #666666;\n"
"    font-size: 12px;\n"
"border:transparent")

        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet(u"border:transparent")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 10, 101, 20))
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet(u"border:transparent")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(280, 30, 51, 20))
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet(u"font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #2c3e50;\n"
"border:transparent")

        self.horizontalLayout_3.addWidget(self.frame_9)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(774, 150))
        self.frame_5.setMaximumSize(QSize(16777215, 175))
        self.frame_5.setStyleSheet(u"background-color: #FFFFFF;      /* Beyaz zemin */\n"
"    border: 1px solid #E0E0E0;      /* \u0130nce gri \u00e7er\u00e7eve */\n"
"    border-radius: 15px;            /* Yuvarlak k\u00f6\u015feler */")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 30, 121, 16))
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet(u"border:transparent;\n"
"color: #212121;\n"
"    font-size: 16px;\n"
"")
        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 50, 51, 51))
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet(u"background-color: #007BFF;      /* D\u00fcz Mavi Renk (\u0130stersen #2196F3 de yapabilirsin) */\n"
"    color: #FFFFFF;                 /* Yaz\u0131 rengi beyaz */\n"
"    border-radius: 14px;            /* K\u00f6\u015feleri yuvarlatma */\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    font-family: 'Segoe UI', sans-serif;")
        self.YatrmcSorumluBrokerLabel = QLabel(self.frame_5)
        self.YatrmcSorumluBrokerLabel.setObjectName(u"YatrmcSorumluBrokerLabel")
        self.YatrmcSorumluBrokerLabel.setGeometry(QRect(70, 50, 161, 31))
        sizePolicy.setHeightForWidth(self.YatrmcSorumluBrokerLabel.sizePolicy().hasHeightForWidth())
        self.YatrmcSorumluBrokerLabel.setSizePolicy(sizePolicy)
        self.YatrmcSorumluBrokerLabel.setStyleSheet(u"color: #212121;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"border:transparent;")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(70, 80, 301, 80))
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"background-color: #F8F9FA;      /* \u00c7ok a\u00e7\u0131k gri zemin */\n"
"    border-radius: 8px;             /* K\u00f6\u015feleri yumu\u015fat */\n"
"    /* Kenarl\u0131k istersen: border: 1px solid #EEEEEE; */")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 10, 49, 16))
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setStyleSheet(u"color: #888888;\n"
"    font-size: 11px;\n"
"    font-weight: normal;\n"
"border:transparent;")
        self.YatrmcBrokerTelLabel = QLabel(self.frame_6)
        self.YatrmcBrokerTelLabel.setObjectName(u"YatrmcBrokerTelLabel")
        self.YatrmcBrokerTelLabel.setGeometry(QRect(20, 40, 91, 16))
        sizePolicy.setHeightForWidth(self.YatrmcBrokerTelLabel.sizePolicy().hasHeightForWidth())
        self.YatrmcBrokerTelLabel.setSizePolicy(sizePolicy)
        self.YatrmcBrokerTelLabel.setStyleSheet(u"color: #333333;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"border:tranparent;")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(380, 80, 371, 80))
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet(u"background-color: #F8F9FA;      /* \u00c7ok a\u00e7\u0131k gri zemin */\n"
"    border-radius: 8px;             /* K\u00f6\u015feleri yumu\u015fat */\n"
"    /* Kenarl\u0131k istersen: border: 1px solid #EEEEEE; */")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 10, 49, 16))
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setStyleSheet(u"color: #888888;\n"
"    font-size: 11px;\n"
"    font-weight: normal;\n"
"border:transparent;")
        self.yatrmcBrokerEpostaLabel = QLabel(self.frame_7)
        self.yatrmcBrokerEpostaLabel.setObjectName(u"yatrmcBrokerEpostaLabel")
        self.yatrmcBrokerEpostaLabel.setGeometry(QRect(20, 40, 151, 16))
        sizePolicy.setHeightForWidth(self.yatrmcBrokerEpostaLabel.sizePolicy().hasHeightForWidth())
        self.yatrmcBrokerEpostaLabel.setSizePolicy(sizePolicy)
        self.yatrmcBrokerEpostaLabel.setStyleSheet(u"color: #333333;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"border:tranparent;")

        self.verticalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.HesaplarimInfoFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.frame_3 = QFrame(self.investorPage)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(800, 200))
        self.frame_3.setMaximumSize(QSize(800, 500))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.StackWidget.addWidget(self.investorPage)
        self.IslemGecmisiScene = QWidget()
        self.IslemGecmisiScene.setObjectName(u"IslemGecmisiScene")
        self.verticalLayout_20 = QVBoxLayout(self.IslemGecmisiScene)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea_2 = QScrollArea(self.IslemGecmisiScene)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(795, 0))
        self.scrollArea_2.setStyleSheet(u"scrollArea {\n"
"    background-color: transparent; /* Kendisi \u015feffaf olsun */\n"
"    border: none;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 822, 846))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(0, 80))
        self.widget_3.setMaximumSize(QSize(16777215, 85))
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 10, 49, 16))
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 10, 91, 71))
        self.label_15.setPixmap(QPixmap(u"../../../../Desktop/Yeni klas\u00f6r/QT projects/VTYS/proje ad\u0131mlar/Ekran g\u00f6r\u00fcnt\u00fcs\u00fc 2025-12-08 152749.png"))
        self.KullaniciAdiLabel_2 = QLabel(self.widget_3)
        self.KullaniciAdiLabel_2.setObjectName(u"KullaniciAdiLabel_2")
        self.KullaniciAdiLabel_2.setGeometry(QRect(120, 50, 91, 16))
        self.KullaniciAdiLabel_2.setStyleSheet(u"color: rgb(0,0,0)\n"
"")
        self.YatirimciPaneliLabel_2 = QLabel(self.widget_3)
        self.YatirimciPaneliLabel_2.setObjectName(u"YatirimciPaneliLabel_2")
        self.YatirimciPaneliLabel_2.setGeometry(QRect(100, 20, 141, 16))
        self.YatirimciPaneliLabel_2.setFont(font1)
        self.YatirimciPaneliLabel_2.setStyleSheet(u"color : rgb(150,150,150)\n"
"")
        self.ExitButton_2 = QPushButton(self.widget_3)
        self.ExitButton_2.setObjectName(u"ExitButton_2")
        self.ExitButton_2.setGeometry(QRect(660, 25, 131, 31))
        self.ExitButton_2.setStyleSheet(u"color: rgb(0,0,0)\n"
"")
        self.ExitButton_2.setIcon(icon)
        self.ExitButton_2.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.widget_3)

        self.SekmeGecisFrame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.SekmeGecisFrame_2.setObjectName(u"SekmeGecisFrame_2")
        self.SekmeGecisFrame_2.setMinimumSize(QSize(0, 90))
        self.SekmeGecisFrame_2.setMaximumSize(QSize(16777215, 90))
        self.SekmeGecisFrame_2.setStyleSheet(u"/* 1. \u00dc\u00c7 BUTON \u0130\u00c7\u0130N ORTAK TEMEL AYARLAR */\n"
"QPushButton#HesaplarimveBakiyeButon_2,\n"
"QPushButton#IslemGecmisiButon_2,\n"
"QPushButton#PortfoyDurumuButon_2 {\n"
"    border: none;\n"
"	background:none;\n"
"    background-color: transparent; /* Normal halde \u015feffaf */\n"
"    color: rgb(129, 129, 129);\n"
"	color:rgb(0,0,0);\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    padding-bottom: 15px;\n"
"    padding-top: 15px;\n"
"    border-bottom: 3px solid transparent;\n"
"    text-align: left;\n"
"}\n"
"\n"
"/* 2. MOUSE \u00dcZER\u0130NE GEL\u0130NCE (HOVER) */\n"
"QPushButton#HesaplarimveBakiyeButon_2:hover,\n"
"QPushButton#IslemGecmisiButon_2:hover,\n"
"QPushButton#PortfoyDurumuButon_2:hover {\n"
"    color: #101828;\n"
"    background-color: transparent; /* Hover'da da arka plan gelmesin */\n"
"}\n"
"\n"
"/* 3. BUTONA BASILI TUTULDU\u011eUNDA (PRESSED) - Sorunu \u00c7\u00f6zen K\u0131s\u0131m */\n"
"QPushButton#HesaplarimveBakiyeButon_2:pressed,\n"
"QPushButton#I"
                        "slemGecmisiButon_2:pressed,\n"
"QPushButton#PortfoyDurumuButon_2:pressed {\n"
"    background-color: transparent; /* Bas\u0131nca mavi kutu \u00e7\u0131kmas\u0131n\u0131 engeller */\n"
"}\n"
"\n"
"/* 4. BUTON SE\u00c7\u0130L\u0130 OLDU\u011eUNDA (CHECKED) - Sorunu \u00c7\u00f6zen K\u0131s\u0131m */\n"
"QPushButton#HesaplarimveBakiyeButon_2:checked,\n"
"QPushButton#IslemGecmisiButon_2:checked,\n"
"QPushButton#PortfoyDurumuButon_2:checked {\n"
"    color: #2b5cff;\n"
"    border-bottom: 3px solid #2b5cff;\n"
"    background-color: transparent; /* Se\u00e7iliyken arka plan\u0131 \u015feffaf zorla */\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.SekmeGecisFrame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.HesaplarimveBakiyeButon_2 = QPushButton(self.SekmeGecisFrame_2)
        self.HesaplarimveBakiyeButon_2.setObjectName(u"HesaplarimveBakiyeButon_2")
        self.HesaplarimveBakiyeButon_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.HesaplarimveBakiyeButon_2.setStyleSheet(u"")
        self.HesaplarimveBakiyeButon_2.setCheckable(True)
        self.HesaplarimveBakiyeButon_2.setChecked(False)
        self.HesaplarimveBakiyeButon_2.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.HesaplarimveBakiyeButon_2)

        self.IslemGecmisiButon_2 = QPushButton(self.SekmeGecisFrame_2)
        self.IslemGecmisiButon_2.setObjectName(u"IslemGecmisiButon_2")
        self.IslemGecmisiButon_2.setStyleSheet(u"")
        self.IslemGecmisiButon_2.setCheckable(True)
        self.IslemGecmisiButon_2.setChecked(True)
        self.IslemGecmisiButon_2.setAutoExclusive(True)
        self.IslemGecmisiButon_2.setFlat(True)

        self.horizontalLayout_4.addWidget(self.IslemGecmisiButon_2)

        self.PortfoyDurumuButon_2 = QPushButton(self.SekmeGecisFrame_2)
        self.PortfoyDurumuButon_2.setObjectName(u"PortfoyDurumuButon_2")
        self.PortfoyDurumuButon_2.setStyleSheet(u"")
        self.PortfoyDurumuButon_2.setCheckable(True)
        self.PortfoyDurumuButon_2.setAutoExclusive(True)
        self.PortfoyDurumuButon_2.setFlat(True)

        self.horizontalLayout_4.addWidget(self.PortfoyDurumuButon_2)


        self.verticalLayout_12.addWidget(self.SekmeGecisFrame_2)

        self.IslemGecmisiFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.IslemGecmisiFrame.setObjectName(u"IslemGecmisiFrame")
        sizePolicy.setHeightForWidth(self.IslemGecmisiFrame.sizePolicy().hasHeightForWidth())
        self.IslemGecmisiFrame.setSizePolicy(sizePolicy)
        self.IslemGecmisiFrame.setMinimumSize(QSize(813, 0))
        self.IslemGecmisiFrame.setStyleSheet(u"/* ANA KART (Beyaz alan) */\n"
"QFrame#HaplarimInfoFrame {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #eaecf0;\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"/* \u00dcst ikon alan\u0131 */\n"
"QFrame#IconFrame {\n"
"    background-color: #eef4ff;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* GENEL YAZI AYARI */\n"
"QLabel {\n"
"    background: transparent;\n"
"    color: #101828;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"/* Hesap No */\n"
"QLabel#HesapNoLabel1 {\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Yat\u0131r\u0131m Hesab\u0131 alt yaz\u0131 */\n"
"QLabel#YatirimHesabiLabel {\n"
"    font-size: 13px;\n"
"    color: #667085;\n"
"}\n"
"\n"
"/* Sa\u011fdaki Bakiye Ba\u015fl\u0131\u011f\u0131 */\n"
"QLabel#BakiyeBaslikLabel {\n"
"    font-size: 12px;\n"
"    color: #667085;\n"
"}\n"
"\n"
"/* Sa\u011fdaki Bakiye De\u011feri */\n"
"QLabel#BakiyeLabel1 {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #101828;\n"
"}\n"
"\n"
"/* \u00dc"
                        "\u00c7 ALT KART (A\u00e7\u0131l\u0131\u015f Tarihi, Komisyon, Durum) */\n"
"QFrame#HesaplarimInfoFrame1,\n"
"QFrame#HesaplarimInfoFrame2,\n"
"QFrame#HesaplarimInfoFrame3 {\n"
"    background-color: #f9fafb;\n"
"    border-radius: 12px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Alt Kart Ba\u015fl\u0131klar\u0131 (A\u00e7\u0131l\u0131\u015f Tarihi \u2014 Komisyon Plan\u0131 \u2014 Durum) */\n"
"QLabel#HesapAcilisBaslik,\n"
"QLabel#KomisyonBaslik,\n"
"QLabel#DurumBaslik {\n"
"    font-size: 13px;\n"
"    color: #667085;\n"
"    font-weight: normal;\n"
"}\n"
"\n"
"/* \u0130\u00e7 de\u011ferler */\n"
"QLabel#HesapAcilisDeger,\n"
"QLabel#KomisyonDeger,\n"
"QLabel#DurumDeger {\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"    color: #101828;\n"
"}\n"
"\n"
"/* Komisyon alt a\u00e7\u0131klama (Min \u20ba50 - %1) */\n"
"QLabel#KomisyonAltYazi {\n"
"    font-size: 12px;\n"
"    color: #667085;\n"
"}\n"
"\n"
"/* ye\u015fil Aktif Rozeti */\n"
"QLabel#DurumLabel1 {\n"
"    background-color: #d1fadf;\n"
"    color: #0"
                        "27a48;\n"
"    border-radius: 12px;\n"
"    padding: 4px 12px;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.IslemGecmisiFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.IslemGecmisiFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.IslemGecmisiFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.ToplamBilgilerFrame = QFrame(self.IslemGecmisiFrame)
        self.ToplamBilgilerFrame.setObjectName(u"ToplamBilgilerFrame")
        sizePolicy.setHeightForWidth(self.ToplamBilgilerFrame.sizePolicy().hasHeightForWidth())
        self.ToplamBilgilerFrame.setSizePolicy(sizePolicy)
        self.ToplamBilgilerFrame.setMinimumSize(QSize(803, 100))
        self.ToplamBilgilerFrame.setMaximumSize(QSize(16777215, 120))
        self.ToplamBilgilerFrame.setStyleSheet(u"")
        self.ToplamBilgilerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToplamBilgilerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.ToplamBilgilerFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_10 = QFrame(self.ToplamBilgilerFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;   /* \u0130nce gri \u00e7er\u00e7eve */\n"
"    border-radius: 12px;")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 20, 41, 41))
        self.label_16.setStyleSheet(u"border-radius: 8px;       /* \u0130kon kutusunun k\u00f6\u015feleri */\n"
"    padding: 10px;            /* \u0130konun kenarlara yap\u0131\u015fmamas\u0131 i\u00e7in */\n"
"    qproperty-alignment: AlignCenter;\n"
"background-color: #E8F5E9;  /* \u00c7ok a\u00e7\u0131k ye\u015fil zemin */\n"
"    /* \u0130kon rengi i\u00e7in SVG kullanmak en iyisidir, ama border ile yaparsan: */\n"
"    border: 1px solid #C8E6C9;")
        self.ToplamAlisLabel = QLabel(self.frame_10)
        self.ToplamAlisLabel.setObjectName(u"ToplamAlisLabel")
        self.ToplamAlisLabel.setGeometry(QRect(60, 20, 91, 16))
        self.ToplamAlisLabel.setStyleSheet(u"color: #757575;          /* Gri renk */\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"border:transparent;")
        self.ToplamAlisLabel_1 = QLabel(self.frame_10)
        self.ToplamAlisLabel_1.setObjectName(u"ToplamAlisLabel_1")
        self.ToplamAlisLabel_1.setGeometry(QRect(60, 40, 101, 31))
        self.ToplamAlisLabel_1.setStyleSheet(u"color: #212121;          /* Koyu siyah */\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"border:transparent;")

        self.horizontalLayout_5.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.ToplamBilgilerFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;   /* \u0130nce gri \u00e7er\u00e7eve */\n"
"    border-radius: 12px;")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.ToplamSatisIconLabel = QLabel(self.frame_12)
        self.ToplamSatisIconLabel.setObjectName(u"ToplamSatisIconLabel")
        self.ToplamSatisIconLabel.setGeometry(QRect(10, 20, 41, 41))
        self.ToplamSatisIconLabel.setStyleSheet(u"border-radius: 8px;       /* \u0130kon kutusunun k\u00f6\u015feleri */\n"
"    padding: 10px;            /* \u0130konun kenarlara yap\u0131\u015fmamas\u0131 i\u00e7in */\n"
"    qproperty-alignment: AlignCenter;\n"
"background-color: #FFEBEE;  /* \u00c7ok a\u00e7\u0131k k\u0131rm\u0131z\u0131 zemin */\n"
"    border: 1px solid #FFCDD2;")
        self.ToplamSatisLabel = QLabel(self.frame_12)
        self.ToplamSatisLabel.setObjectName(u"ToplamSatisLabel")
        self.ToplamSatisLabel.setGeometry(QRect(60, 20, 101, 16))
        self.ToplamSatisLabel.setStyleSheet(u"color: #757575;          /* Gri renk */\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"border:transparent;")
        self.ToplamSatisLabel_1 = QLabel(self.frame_12)
        self.ToplamSatisLabel_1.setObjectName(u"ToplamSatisLabel_1")
        self.ToplamSatisLabel_1.setGeometry(QRect(60, 40, 111, 31))
        self.ToplamSatisLabel_1.setStyleSheet(u"color: #212121;          /* Koyu siyah */\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"border:transparent;")

        self.horizontalLayout_5.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.ToplamBilgilerFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;   /* \u0130nce gri \u00e7er\u00e7eve */\n"
"    border-radius: 12px;")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.ToplamKomisyonIconLabel = QLabel(self.frame_11)
        self.ToplamKomisyonIconLabel.setObjectName(u"ToplamKomisyonIconLabel")
        self.ToplamKomisyonIconLabel.setGeometry(QRect(10, 20, 41, 41))
        self.ToplamKomisyonIconLabel.setStyleSheet(u"border-radius: 8px;       /* \u0130kon kutusunun k\u00f6\u015feleri */\n"
"    padding: 10px;            /* \u0130konun kenarlara yap\u0131\u015fmamas\u0131 i\u00e7in */\n"
"    qproperty-alignment: AlignCenter;\n"
"background-color: #E3F2FD;  /* \u00c7ok a\u00e7\u0131k mavi zemin */\n"
"    border: 1px solid #BBDEFB;")
        self.ToplamKomisyonLabel = QLabel(self.frame_11)
        self.ToplamKomisyonLabel.setObjectName(u"ToplamKomisyonLabel")
        self.ToplamKomisyonLabel.setGeometry(QRect(60, 20, 111, 16))
        self.ToplamKomisyonLabel.setStyleSheet(u"color: #757575;          /* Gri renk */\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"border:transparent;")
        self.ToplamKomisyonLabel_1 = QLabel(self.frame_11)
        self.ToplamKomisyonLabel_1.setObjectName(u"ToplamKomisyonLabel_1")
        self.ToplamKomisyonLabel_1.setGeometry(QRect(60, 40, 111, 31))
        self.ToplamKomisyonLabel_1.setStyleSheet(u"color: #212121;          /* Koyu siyah */\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"border:transparent;")

        self.horizontalLayout_5.addWidget(self.frame_11)


        self.verticalLayout_13.addWidget(self.ToplamBilgilerFrame)

        self.FltrelemeFrame = QFrame(self.IslemGecmisiFrame)
        self.FltrelemeFrame.setObjectName(u"FltrelemeFrame")
        sizePolicy.setHeightForWidth(self.FltrelemeFrame.sizePolicy().hasHeightForWidth())
        self.FltrelemeFrame.setSizePolicy(sizePolicy)
        self.FltrelemeFrame.setMinimumSize(QSize(0, 130))
        self.FltrelemeFrame.setMaximumSize(QSize(16777215, 130))
        self.FltrelemeFrame.setStyleSheet(u"QFrame#FltrelemeFrame{	\n"
"background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 12px;\n"
"}\n"
"QLabel[class=\"inputLabel\"] {\n"
"    color: #666666;        /* Gri yaz\u0131 */\n"
"    font-size: 11px;       /* K\u00fc\u00e7\u00fck punto */\n"
"    font-weight: normal;\n"
"    margin-bottom: 2px;    /* Kutuyla yaz\u0131 aras\u0131na hafif bo\u015fluk */\n"
"}\n"
"\n"
"\n"
"/* \u00dczerine gelince (Hover) rengi koyula\u015fs\u0131n */\n"
"QComboBox:hover, QDateEdit:hover {\n"
"    border: 1px solid #BDBDBD;\n"
"}\n"
"\n"
"/* TIKLANDI\u011eINDA (FOCUS) - Resimdeki Mavi Kenarl\u0131k */\n"
"QComboBox:focus, QDateEdit:focus {\n"
"    border: 2px solid #2196F3;     /* Qt Designer mavisi */\n"
"    color: #000000;\n"
"}")
        self.FltrelemeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FltrelemeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_17 = QLabel(self.FltrelemeFrame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 10, 61, 31))
        self.label_17.setStyleSheet(u"font-size: 14px;\n"
"    color: #333333; /* Koyu gri/siyah metin */\n"
"    margin-bottom: 8px; /* Giri\u015f kutusu ile aras\u0131na bo\u015fluk */\n"
"    font-weight: 500; /* Orta kal\u0131nl\u0131k */")
        self.label_18 = QLabel(self.FltrelemeFrame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(34, 50, 49, 16))
        self.label_19 = QLabel(self.FltrelemeFrame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(274, 50, 81, 16))
        self.label_20 = QLabel(self.FltrelemeFrame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(474, 50, 49, 16))
        self.label_21 = QLabel(self.FltrelemeFrame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(644, 50, 49, 16))
        self.comboBox_2 = QComboBox(self.FltrelemeFrame)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(30, 80, 231, 37))
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet(u"color:grey\n"
"")
        self.comboBox_3 = QComboBox(self.FltrelemeFrame)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(270, 80, 191, 37))
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setStyleSheet(u"color:grey")
        self.dateEdit = QDateEdit(self.FltrelemeFrame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(470, 80, 161, 37))
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setStyleSheet(u"/* --- 1. G\u0130R\u0130\u015e KUTUSU (INPUT) --- */\n"
"QDateEdit {\n"
"    /* Hafif gri arka plan (G\u00f6z\u00fc yormaz, modern durur) */\n"
"    background-color: #F3F4F6;\n"
"    /* \u00c7er\u00e7eve yok, sadece zemin rengi var (Unstyled look) */\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;           /* Daha oval k\u00f6\u015feler */\n"
"    padding: 10px 15px;            /* Geni\u015f i\u00e7 bo\u015fluk */\n"
"    color: #1F2937;                /* Koyu antrasit yaz\u0131 */\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* \u00dczerine gelince (Hover) */\n"
"QDateEdit:hover {\n"
"    background-color: #E5E7EB;     /* Biraz daha koyula\u015f\u0131r */\n"
"}\n"
"\n"
"/* T\u0131klay\u0131nca (Focus) */\n"
"QDateEdit:focus {\n"
"    background-color: #FFFFFF;     /* Beyaz olur */\n"
"    border: 1px solid #3B82F6;     /* Modern Mavi \u00c7er\u00e7eve */\n"
"    /* \u0130stersen border yerine sadece renk de\u011fi\u015fi"
                        "mi de yapabilirsin */\n"
"}\n"
"\n"
"/* --- 2. SA\u011eDAK\u0130 OK BUTONU --- */\n"
"QDateEdit::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 30px;\n"
"}\n"
"\n"
"/* Ok \u0130konu: Bunu daha minimalist yapal\u0131m */\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/icons/calendar_modern.png); /* Kendi ikonun yoksa standart ok \u00e7\u0131kar */\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"/* --- 3. POP-UP TAKV\u0130M (EN \u00d6NEML\u0130 KISIM) --- */\n"
"\n"
"/* Takvim Ana \u00c7er\u00e7eve */\n"
"QCalendarWidget QWidget {\n"
"    background-color: #FFFFFF;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Takvim \u00dcst Ba\u015fl\u0131k (Ay Y\u0131l Se\u00e7imi) */\n"
"QCalendarWidget QToolButton {\n"
"    color: #374151;\n"
"    font-weight: bold;\n"
"    icon-size: 24px;\n"
"    background-color: transparent;\n"
"    margin: 5px;\n"
"    border-radius: 5px"
                        ";\n"
"}\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #F3F4F6;\n"
"}\n"
"\n"
"/* Takvimdeki G\u00fcnler Tablosu (Gridleri yok ediyoruz) */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    background-color: white;\n"
"    color: #4B5563;             /* G\u00fcnlerin yaz\u0131 rengi */\n"
"    selection-background-color: #3B82F6; /* Se\u00e7ili g\u00fcn MAV\u0130 */\n"
"    selection-color: white;\n"
"    font-size: 13px;\n"
"    outline: 0;                 /* Se\u00e7imdeki kesik \u00e7izgiyi kald\u0131r */\n"
"}\n"
"\n"
"/* Se\u00e7ili G\u00fcn\u00fcn Yuvarlak Olmas\u0131 \u0130\u00e7in (Qt'de hile yapmak gerekir) */\n"
"/* Maalesef Qt Designer CSS ile tam daire (border-radius) tablolarda zor \u00e7al\u0131\u015f\u0131r */\n"
"/* Ama renk ve font ile o modern havay\u0131 veririz */\n"
"\n"
"/* Hafta G\u00fcnleri Ba\u015fl\u0131\u011f\u0131 (Pzt, Sal...) */\n"
"QCalendarWidget QAbstractItemView:enabled::section {\n"
"    color: #9CA3AF;            /* Soluk gri ba\u015fl\u0131klar */\n"
""
                        "    background-color: white;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u00dcst Navigasyon \u00c7ubu\u011fu Rengi */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: white;\n"
"    border-bottom: 1px solid #E5E7EB; /* Ba\u015fl\u0131k ile g\u00fcnler aras\u0131na ince \u00e7izgi */\n"
"}")
        self.dateEdit_2 = QDateEdit(self.FltrelemeFrame)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(640, 80, 151, 37))
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        self.dateEdit_2.setStyleSheet(u"/* --- 1. G\u0130R\u0130\u015e KUTUSU (INPUT) --- */\n"
"QDateEdit {\n"
"    /* Hafif gri arka plan (G\u00f6z\u00fc yormaz, modern durur) */\n"
"    background-color: #F3F4F6;\n"
"    /* \u00c7er\u00e7eve yok, sadece zemin rengi var (Unstyled look) */\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;           /* Daha oval k\u00f6\u015feler */\n"
"    padding: 10px 15px;            /* Geni\u015f i\u00e7 bo\u015fluk */\n"
"    color: #1F2937;                /* Koyu antrasit yaz\u0131 */\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* \u00dczerine gelince (Hover) */\n"
"QDateEdit:hover {\n"
"    background-color: #E5E7EB;     /* Biraz daha koyula\u015f\u0131r */\n"
"}\n"
"\n"
"/* T\u0131klay\u0131nca (Focus) */\n"
"QDateEdit:focus {\n"
"    background-color: #FFFFFF;     /* Beyaz olur */\n"
"    border: 1px solid #3B82F6;     /* Modern Mavi \u00c7er\u00e7eve */\n"
"    /* \u0130stersen border yerine sadece renk de\u011fi\u015fi"
                        "mi de yapabilirsin */\n"
"}\n"
"\n"
"\n"
"/* Ok \u0130konu: Bunu daha minimalist yapal\u0131m */\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/icons/calendar_modern.png); /* Kendi ikonun yoksa standart ok \u00e7\u0131kar */\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"/* --- 3. POP-UP TAKV\u0130M (EN \u00d6NEML\u0130 KISIM) --- */\n"
"\n"
"/* Takvim Ana \u00c7er\u00e7eve */\n"
"QCalendarWidget QWidget {\n"
"    background-color: #FFFFFF;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Takvim \u00dcst Ba\u015fl\u0131k (Ay Y\u0131l Se\u00e7imi) */\n"
"QCalendarWidget QToolButton {\n"
"    color: #374151;\n"
"    font-weight: bold;\n"
"    icon-size: 24px;\n"
"    background-color: transparent;\n"
"    margin: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #F3F4F6;\n"
"}\n"
"\n"
"/* Takvimdeki G\u00fcnler Tablosu (Gridleri yok ediyoruz) */"
                        "\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    background-color: white;\n"
"    color: #4B5563;             /* G\u00fcnlerin yaz\u0131 rengi */\n"
"    selection-background-color: #3B82F6; /* Se\u00e7ili g\u00fcn MAV\u0130 */\n"
"    selection-color: white;\n"
"    font-size: 13px;\n"
"    outline: 0;                 /* Se\u00e7imdeki kesik \u00e7izgiyi kald\u0131r */\n"
"}\n"
"\n"
"/* Se\u00e7ili G\u00fcn\u00fcn Yuvarlak Olmas\u0131 \u0130\u00e7in (Qt'de hile yapmak gerekir) */\n"
"/* Maalesef Qt Designer CSS ile tam daire (border-radius) tablolarda zor \u00e7al\u0131\u015f\u0131r */\n"
"/* Ama renk ve font ile o modern havay\u0131 veririz */\n"
"\n"
"/* Hafta G\u00fcnleri Ba\u015fl\u0131\u011f\u0131 (Pzt, Sal...) */\n"
"QCalendarWidget QAbstractItemView:enabled::section {\n"
"    color: #9CA3AF;            /* Soluk gri ba\u015fl\u0131klar */\n"
"    background-color: white;\n"
"    font-weight: bold;\n"
"    font-size: 11px;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u00dcst Nav"
                        "igasyon \u00c7ubu\u011fu Rengi */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: white;\n"
"    border-bottom: 1px solid #E5E7EB; /* Ba\u015fl\u0131k ile g\u00fcnler aras\u0131na ince \u00e7izgi */\n"
"}")
        self.dateEdit_2.setMinimumDateTime(QDateTime(QDate(1791, 9, 14), QTime(20, 0, 0)))
        self.dateEdit_2.setMinimumDate(QDate(1791, 9, 14))

        self.verticalLayout_13.addWidget(self.FltrelemeFrame)

        self.HistoryFrame = QFrame(self.IslemGecmisiFrame)
        self.HistoryFrame.setObjectName(u"HistoryFrame")
        sizePolicy.setHeightForWidth(self.HistoryFrame.sizePolicy().hasHeightForWidth())
        self.HistoryFrame.setSizePolicy(sizePolicy)
        self.HistoryFrame.setMinimumSize(QSize(0, 400))
        self.HistoryFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HistoryFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.HistoryFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_22 = QLabel(self.HistoryFrame)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_6.addWidget(self.label_22)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.HistoryFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_6)

        self.tableWidget = QTableWidget(self.HistoryFrame)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(800, 140))
        self.tableWidget.setMaximumSize(QSize(800, 16777215))
        self.tableWidget.setStyleSheet(u"/* 1. Tablonun Genel G\u00f6r\u00fcn\u00fcm\u00fc */\n"
"QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: none;              /* Tablonun d\u0131\u015f \u00e7izgisini kald\u0131r */\n"
"    gridline-color: #E0E0E0;   /* E\u011fer grid a\u00e7arsan rengi bu olsun */\n"
"}\n"
"\n"
"/* 2. S\u00fctun Ba\u015fl\u0131klar\u0131 (En \u00dcstteki Gri Yaz\u0131lar) */\n"
"QHeaderView::section {\n"
"    background-color: #FFFFFF; /* Ba\u015fl\u0131k arka plan\u0131 beyaz */\n"
"    color: #757575;            /* Yaz\u0131 rengi gri */\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"    border: none;              /* Kutucuk \u00e7izgilerini kald\u0131r */\n"
"    border-bottom: 1px solid #E0E0E0; /* Sadece alta \u00e7izgi \u00e7ek */\n"
"    padding: 10px 5px;         /* Biraz bo\u015fluk ver */\n"
"    text-align: left;\n"
"}\n"
"\n"
"/* 3. Sat\u0131rlar ve H\u00fccreler */\n"
"QTableWidget::item {\n"
"    padding: 10px 5px;         /* H\u00fccre i\u00e7i bo\u015fluk (Ferah g\u00f6r\u00fcn\u00fcm)"
                        " */\n"
"    border-bottom: 1px solid #F5F5F5; /* Her sat\u0131r\u0131n alt\u0131na ince \u00e7izgi */\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* 4. Se\u00e7ili Sat\u0131r Rengi */\n"
"QTableWidget::item:selected {\n"
"    background-color: #F5F7FA; /* Se\u00e7ilince \u00e7ok a\u00e7\u0131k mavi/gri olsun */\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* 5. D\u0131\u015fa Aktar Butonu (Mavi) */\n"
"QPushButton {\n"
"    background-color: #0055FF;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0044CC;\n"
"}")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.verticalHeader().setVisible(True)

        self.verticalLayout_14.addWidget(self.tableWidget)


        self.verticalLayout_13.addWidget(self.HistoryFrame)


        self.verticalLayout_12.addWidget(self.IslemGecmisiFrame)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_20.addWidget(self.scrollArea_2)

        self.StackWidget.addWidget(self.IslemGecmisiScene)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_16 = QVBoxLayout(self.page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_3 = QScrollArea(self.page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(823, 0))
        self.scrollArea_3.setMaximumSize(QSize(823, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -315, 807, 900))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(0, 900))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_17.setSpacing(8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy)
        self.frame_41.setMinimumSize(QSize(0, 80))
        self.frame_41.setMaximumSize(QSize(16777215, 85))
        self.label_23 = QLabel(self.frame_41)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 10, 49, 16))
        self.label_24 = QLabel(self.frame_41)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 10, 91, 71))
        self.label_24.setPixmap(QPixmap(u"../../../../Desktop/Yeni klas\u00f6r/QT projects/VTYS/proje ad\u0131mlar/Ekran g\u00f6r\u00fcnt\u00fcs\u00fc 2025-12-08 152749.png"))
        self.KullaniciAdiLabel_3 = QLabel(self.frame_41)
        self.KullaniciAdiLabel_3.setObjectName(u"KullaniciAdiLabel_3")
        self.KullaniciAdiLabel_3.setGeometry(QRect(120, 50, 91, 16))
        self.KullaniciAdiLabel_3.setStyleSheet(u"color: rgb(0,0,0)\n"
"")
        self.YatirimciPaneliLabel_3 = QLabel(self.frame_41)
        self.YatirimciPaneliLabel_3.setObjectName(u"YatirimciPaneliLabel_3")
        self.YatirimciPaneliLabel_3.setGeometry(QRect(100, 20, 141, 16))
        self.YatirimciPaneliLabel_3.setFont(font1)
        self.YatirimciPaneliLabel_3.setStyleSheet(u"color : rgb(150,150,150)\n"
"")
        self.ExitButton_3 = QPushButton(self.frame_41)
        self.ExitButton_3.setObjectName(u"ExitButton_3")
        self.ExitButton_3.setGeometry(QRect(660, 25, 131, 31))
        self.ExitButton_3.setStyleSheet(u"color: rgb(0,0,0)\n"
"")
        self.ExitButton_3.setIcon(icon)
        self.ExitButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout_17.addWidget(self.frame_41)

        self.SekmeGecisFrame_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.SekmeGecisFrame_3.setObjectName(u"SekmeGecisFrame_3")
        sizePolicy.setHeightForWidth(self.SekmeGecisFrame_3.sizePolicy().hasHeightForWidth())
        self.SekmeGecisFrame_3.setSizePolicy(sizePolicy)
        self.SekmeGecisFrame_3.setMinimumSize(QSize(0, 90))
        self.SekmeGecisFrame_3.setMaximumSize(QSize(16777215, 90))
        self.SekmeGecisFrame_3.setStyleSheet(u"/* 1. \u00dc\u00c7 BUTON \u0130\u00c7\u0130N ORTAK TEMEL AYARLAR */\n"
"QPushButton#HesaplarimveBakiyeButon_3,\n"
"QPushButton#IslemGecmisiButon_3,\n"
"QPushButton#PortfoyDurumuButon_3 {\n"
"    border: none;\n"
"	background:none;\n"
"    background-color: transparent; /* Normal halde \u015feffaf */\n"
"    color: rgb(129, 129, 129);\n"
"	color:rgb(0,0,0);\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    padding-bottom: 15px;\n"
"    padding-top: 15px;\n"
"    border-bottom: 3px solid transparent;\n"
"    text-align: left;\n"
"}\n"
"\n"
"/* 2. MOUSE \u00dcZER\u0130NE GEL\u0130NCE (HOVER) */\n"
"QPushButton#HesaplarimveBakiyeButon_3:hover,\n"
"QPushButton#IslemGecmisiButon_3:hover,\n"
"QPushButton#PortfoyDurumuButon_3:hover {\n"
"    color: #101828;\n"
"    background-color: transparent; /* Hover'da da arka plan gelmesin */\n"
"}\n"
"\n"
"/* 3. BUTONA BASILI TUTULDU\u011eUNDA (PRESSED) - Sorunu \u00c7\u00f6zen K\u0131s\u0131m */\n"
"QPushButton#HesaplarimveBakiyeButon_3:pressed,\n"
"QPushButton#I"
                        "slemGecmisiButon_3:pressed,\n"
"QPushButton#PortfoyDurumuButon_3:pressed {\n"
"    background-color: transparent; /* Bas\u0131nca mavi kutu \u00e7\u0131kmas\u0131n\u0131 engeller */\n"
"}\n"
"\n"
"/* 4. BUTON SE\u00c7\u0130L\u0130 OLDU\u011eUNDA (CHECKED) - Sorunu \u00c7\u00f6zen K\u0131s\u0131m */\n"
"QPushButton#HesaplarimveBakiyeButon_3:checked,\n"
"QPushButton#IslemGecmisiButon_3:checked,\n"
"QPushButton#PortfoyDurumuButon_3:checked {\n"
"    color: #2b5cff;\n"
"    border-bottom: 3px solid #2b5cff;\n"
"    background-color: transparent; /* Se\u00e7iliyken arka plan\u0131 \u015feffaf zorla */\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.SekmeGecisFrame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.HesaplarimveBakiyeButon_3 = QPushButton(self.SekmeGecisFrame_3)
        self.HesaplarimveBakiyeButon_3.setObjectName(u"HesaplarimveBakiyeButon_3")
        self.HesaplarimveBakiyeButon_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.HesaplarimveBakiyeButon_3.setStyleSheet(u"")
        self.HesaplarimveBakiyeButon_3.setCheckable(True)
        self.HesaplarimveBakiyeButon_3.setChecked(False)
        self.HesaplarimveBakiyeButon_3.setAutoExclusive(True)

        self.horizontalLayout_7.addWidget(self.HesaplarimveBakiyeButon_3)

        self.IslemGecmisiButon_3 = QPushButton(self.SekmeGecisFrame_3)
        self.IslemGecmisiButon_3.setObjectName(u"IslemGecmisiButon_3")
        self.IslemGecmisiButon_3.setStyleSheet(u"")
        self.IslemGecmisiButon_3.setCheckable(True)
        self.IslemGecmisiButon_3.setChecked(False)
        self.IslemGecmisiButon_3.setAutoExclusive(True)
        self.IslemGecmisiButon_3.setFlat(True)

        self.horizontalLayout_7.addWidget(self.IslemGecmisiButon_3)

        self.PortfoyDurumuButon_3 = QPushButton(self.SekmeGecisFrame_3)
        self.PortfoyDurumuButon_3.setObjectName(u"PortfoyDurumuButon_3")
        self.PortfoyDurumuButon_3.setStyleSheet(u"")
        self.PortfoyDurumuButon_3.setCheckable(True)
        self.PortfoyDurumuButon_3.setChecked(True)
        self.PortfoyDurumuButon_3.setAutoExclusive(True)
        self.PortfoyDurumuButon_3.setFlat(True)

        self.horizontalLayout_7.addWidget(self.PortfoyDurumuButon_3)


        self.verticalLayout_17.addWidget(self.SekmeGecisFrame_3)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QSize(0, 110))
        self.frame_13.setMaximumSize(QSize(16777215, 110))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;    /* \u0130nce gri \u00e7er\u00e7eve */\n"
"    border-radius: 12px;          /* K\u00f6\u015feleri yuvarla */\n"
"}\n"
"\n"
"/* \u00dczerine gelince hafif g\u00f6lge efekti (Opsiyonel) */\n"
"QFrame:hover {\n"
"    border: 1px solid #BDBDBD;\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.label_25 = QLabel(self.frame_16)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 10, 31, 31))
        self.label_25.setStyleSheet(u"/* ORTAK \u0130KON KUTUSU AYARI */\n"
"QLabel {\n"
"    border-radius: 10px;       /* Hafif yuvarlak k\u00f6\u015feler */\n"
"    padding: 10px;             /* \u0130konun kenarlara yap\u0131\u015fmamas\u0131 i\u00e7in */\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"/* 1. MAV\u0130 KUTU (Pozisyon Say\u0131s\u0131) */\n"
"QLabel{\n"
"color:blue;\n"
"    background-color: #E3F2FD; /* A\u00e7\u0131k Mavi */\n"
"    /* \u0130kon rengini kodla veremezsin, ikonun kendisi mavi olmal\u0131 */\n"
"}\n"
"")
        self.PozisyonSayisiLabel = QLabel(self.frame_16)
        self.PozisyonSayisiLabel.setObjectName(u"PozisyonSayisiLabel")
        self.PozisyonSayisiLabel.setGeometry(QRect(60, 10, 101, 16))
        self.PozisyonSayisiLabel.setStyleSheet(u"QLabel {\n"
"    color: #757575;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"border:transparent;\n"
"}")
        self.PozisyonSayisiabel_1 = QLabel(self.frame_16)
        self.PozisyonSayisiabel_1.setObjectName(u"PozisyonSayisiabel_1")
        self.PozisyonSayisiabel_1.setGeometry(QRect(60, 30, 49, 16))
        self.PozisyonSayisiabel_1.setStyleSheet(u"/* Alttaki Siyah De\u011fer (4, \u20ba517.530 vb.) */\n"
"QLabel{\n"
"	border:transparent;\n"
"    color: #212121;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.label_28 = QLabel(self.frame_17)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 10, 31, 31))
        self.label_28.setStyleSheet(u"/* ORTAK \u0130KON KUTUSU AYARI */\n"
"QLabel {\n"
"    border-radius: 10px;       /* Hafif yuvarlak k\u00f6\u015feler */\n"
"    padding: 10px;             /* \u0130konun kenarlara yap\u0131\u015fmamas\u0131 i\u00e7in */\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"/* 2. MOR KUTU (Toplam Maliyet) */\n"
"QLabel {\n"
"color:rgb(85, 0, 255);\n"
"    background-color: rgb(170, 170, 255); /* A\u00e7\u0131k Mor */\n"
"}\n"
"\n"
"")
        self.ToplamMaliyet_1 = QLabel(self.frame_17)
        self.ToplamMaliyet_1.setObjectName(u"ToplamMaliyet_1")
        self.ToplamMaliyet_1.setGeometry(QRect(60, 30, 71, 16))
        self.ToplamMaliyet_1.setStyleSheet(u"/* Alttaki Siyah De\u011fer (4, \u20ba517.530 vb.) */\n"
"QLabel{\n"
"	border:transparent;\n"
"    color: #212121;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"")
        self.ToplamMaliyetLabel = QLabel(self.frame_17)
        self.ToplamMaliyetLabel.setObjectName(u"ToplamMaliyetLabel")
        self.ToplamMaliyetLabel.setGeometry(QRect(60, 10, 101, 16))
        self.ToplamMaliyetLabel.setStyleSheet(u"QLabel {\n"
"    color: #757575;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"border:transparent;\n"
"}")

        self.horizontalLayout_8.addWidget(self.frame_17)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.label_31 = QLabel(self.frame_14)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 31, 31))
        self.label_31.setStyleSheet(u"/* ORTAK \u0130KON KUTUSU AYARI */\n"
"QLabel {\n"
"    border-radius: 10px;       /* Hafif yuvarlak k\u00f6\u015feler */\n"
"    padding: 10px;             /* \u0130konun kenarlara yap\u0131\u015fmamas\u0131 i\u00e7in */\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"/* 3. PEMBE KUTU (G\u00fcncel De\u011fer) */\n"
"QLabel {\n"
"	color:rgb(170, 0, 127);\n"
"    background-color: #F8BBD0; /* Veya #F3E5F5 tonlar\u0131 */\n"
"    /* Resimde \u00e7ok a\u00e7\u0131k lila duruyor: */\n"
"    background-color: #F3E5F5; \n"
"}\n"
"\n"
"")
        self.GuncelDegerLabel_1 = QLabel(self.frame_14)
        self.GuncelDegerLabel_1.setObjectName(u"GuncelDegerLabel_1")
        self.GuncelDegerLabel_1.setGeometry(QRect(60, 30, 81, 16))
        self.GuncelDegerLabel_1.setStyleSheet(u"/* Alttaki Siyah De\u011fer (4, \u20ba517.530 vb.) */\n"
"QLabel{\n"
"	border:transparent;\n"
"    color: #212121;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.GuncelDegerLabel = QLabel(self.frame_14)
        self.GuncelDegerLabel.setObjectName(u"GuncelDegerLabel")
        self.GuncelDegerLabel.setGeometry(QRect(60, 10, 101, 16))
        self.GuncelDegerLabel.setStyleSheet(u"QLabel {\n"
"    color: #757575;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"border:transparent;\n"
"}")

        self.horizontalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.label_34 = QLabel(self.frame_15)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 10, 31, 31))
        self.label_34.setStyleSheet(u"/* ORTAK \u0130KON KUTUSU AYARI */\n"
"QLabel {\n"
"    border-radius: 10px;       /* Hafif yuvarlak k\u00f6\u015feler */\n"
"    padding: 10px;             /* \u0130konun kenarlara yap\u0131\u015fmamas\u0131 i\u00e7in */\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"/* 4. YE\u015e\u0130L KUTU (Kar/Zarar) */\n"
"QLabel {\n"
"color:green;\n"
"    background-color: #E8F5E9; /* A\u00e7\u0131k Ye\u015fil */\n"
"}")
        self.label_35 = QLabel(self.frame_15)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(60, 30, 81, 16))
        self.label_35.setStyleSheet(u"/* Alttaki Siyah De\u011fer (4, \u20ba517.530 vb.) */\n"
"QLabel{\n"
"	border:transparent;\n"
"    color: #212121;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Sadece Kar/Zarar k\u0131sm\u0131ndaki ye\u015fil yaz\u0131 i\u00e7in \u00f6zel durum */\n"
"QLabel {\n"
"    color: #2E7D32;       /* Koyu Ye\u015fil Yaz\u0131 */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        self.label_36 = QLabel(self.frame_15)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(60, 10, 71, 16))
        self.label_36.setStyleSheet(u"QLabel {\n"
"    color: #757575;\n"
"    font-size: 12px;\n"
"    font-weight: normal;\n"
"border:transparent;\n"
"}")

        self.horizontalLayout_8.addWidget(self.frame_15)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.PortfoyFrame = QFrame(self.scrollAreaWidgetContents_3)
        self.PortfoyFrame.setObjectName(u"PortfoyFrame")
        sizePolicy.setHeightForWidth(self.PortfoyFrame.sizePolicy().hasHeightForWidth())
        self.PortfoyFrame.setSizePolicy(sizePolicy)
        self.PortfoyFrame.setMinimumSize(QSize(0, 300))
        self.PortfoyFrame.setMaximumSize(QSize(16777215, 300))
        self.PortfoyFrame.setStyleSheet(u"background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-bottom: 3px solid #E0E0E0; /* Alt tarafa hafif derinlik katar */\n"
"    border-radius: 16px;")
        self.PortfoyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PortfoyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.PortfoyFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_18 = QFrame(self.PortfoyFrame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 30))
        self.frame_18.setStyleSheet(u"background:transparent;\n"
"border:transparent;")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.label_26 = QLabel(self.frame_18)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 0, 211, 41))
        self.label_26.setStyleSheet(u"color: #212121;          /* Koyu siyah/gri */\n"
"    font-size: 18px;         /* Okunakl\u0131 b\u00fcy\u00fck punto */\n"
"    font-weight: bold;       /* Kal\u0131n yaz\u0131 */\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    margin-bottom: 10px;\n"
"border:transparent;")

        self.verticalLayout_18.addWidget(self.frame_18)

        self.tableWidget_2 = QTableWidget(self.PortfoyFrame)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(750, 300))
        self.tableWidget_2.setMaximumSize(QSize(790, 16777215))
        self.tableWidget_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tableWidget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget_2.setStyleSheet(u"/* Tablo Genel */\n"
"QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"    gridline-color: transparent;\n"
"}\n"
"\n"
"/* S\u00fctun Ba\u015fl\u0131klar\u0131 */\n"
"QHeaderView::section {\n"
"    background-color: #FFFFFF;\n"
"    color: #757575;             /* Gri Ba\u015fl\u0131klar */\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"    border: none;\n"
"    border-bottom: 2px solid #F5F5F5; /* Ba\u015fl\u0131k alt\u0131 kal\u0131n \u00e7izgi */\n"
"    padding: 15px 5px;          /* Geni\u015f bo\u015fluk */\n"
"    text-align: left;\n"
"}\n"
"\n"
"/* Sat\u0131r H\u00fccreleri */\n"
"QTableWidget::item {\n"
"    border-bottom: 1px solid #F9F9F9; /* Sat\u0131r alt\u0131 ince \u00e7izgi */\n"
"    padding: 10px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* Toplam Sat\u0131r\u0131 (Bunu kodla \u00f6zel isimlendirece\u011fiz) */\n"
"QTableWidget::item[isTotal=\"true\"] {\n"
"    font-weight: bold;\n"
"    background-color: #FAFAFA;\n"
"}")
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.verticalLayout_18.addWidget(self.tableWidget_2)


        self.verticalLayout_17.addWidget(self.PortfoyFrame)

        self.DagilimFrame = QFrame(self.scrollAreaWidgetContents_3)
        self.DagilimFrame.setObjectName(u"DagilimFrame")
        self.DagilimFrame.setMinimumSize(QSize(0, 200))
        self.DagilimFrame.setMaximumSize(QSize(16777215, 200))
        self.DagilimFrame.setStyleSheet(u"background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-bottom: 3px solid #E0E0E0; /* Alt tarafa hafif derinlik katar */\n"
"    border-radius: 16px;")
        self.DagilimFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.DagilimFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.DagilimFrame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_19 = QFrame(self.DagilimFrame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 30))
        self.frame_19.setMaximumSize(QSize(16777215, 30))
        self.frame_19.setStyleSheet(u"background:transparent;\n"
"border:transparent;")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.label_27 = QLabel(self.frame_19)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 0, 211, 41))
        self.label_27.setStyleSheet(u"color: #212121;          /* Koyu siyah/gri */\n"
"    font-size: 18px;         /* Okunakl\u0131 b\u00fcy\u00fck punto */\n"
"    font-weight: bold;       /* Kal\u0131n yaz\u0131 */\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    margin-bottom: 10px;\n"
"border:transparent;")

        self.verticalLayout_19.addWidget(self.frame_19)

        self.DagilimListesiFrame = QFrame(self.DagilimFrame)
        self.DagilimListesiFrame.setObjectName(u"DagilimListesiFrame")
        self.DagilimListesiFrame.setStyleSheet(u"border:transparent\n"
"/* --- PROGRESS BAR TASARIMI --- */\n"
"QProgressBar {\n"
"    border: none;\n"
"    background-color: #F1F3F5;  /* Bar\u0131n bo\u015f (gri) arka plan\u0131 */\n"
"    border-radius: 4px;         /* Kenarlar\u0131 yuvarlak olsun */\n"
"    min-height: 8px;            /* Resimdeki gibi incecik olsun */\n"
"    max-height: 8px;\n"
"    text-align: center;         /* Yaz\u0131y\u0131 ortala (ama biz yaz\u0131y\u0131 gizleyece\u011fiz) */\n"
"}\n"
"\n"
"/* Bar\u0131n Dolu K\u0131sm\u0131 (Mavi Alan) */\n"
"QProgressBar::chunk {\n"
"    background-color: #4C6EF5;  /* Ana renk (Mavi) */\n"
"    border-radius: 4px;\n"
"}")
        self.DagilimListesiFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.DagilimListesiFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.DagilimListesiFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_2 = QSpacerItem(20, 117, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_2)


        self.verticalLayout_19.addWidget(self.DagilimListesiFrame)


        self.verticalLayout_17.addWidget(self.DagilimFrame)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_15.addWidget(self.scrollArea_3)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.StackWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.StackWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 872, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.StackWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Logo.setText("")
        self.Baslik.setText(QCoreApplication.translate("MainWindow", u"                         Yat\u0131r\u0131m Takip Sistemi", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Giri\u015f Tipi", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Yat\u0131r\u0131mc\u0131 Hesab\u0131", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Broker Hesab\u0131", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Yeni \u00dcye Kayd\u0131", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Kullan\u0131c\u0131 Ad\u0131n\u0131z", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"kullanici.Adi", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Kullan\u0131c\u0131 \u015eifreniz", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"kullanici.sifre", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Giri\u015f Yap", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.KullaniciAdiLabel.setText(QCoreApplication.translate("MainWindow", u"Kullan\u0131c\u0131 ad\u0131", None))
        self.YatirimciPaneliLabel.setText(QCoreApplication.translate("MainWindow", u"Yat\u0131r\u0131mc\u0131 Paneli", None))
        self.ExitButton.setText(QCoreApplication.translate("MainWindow", u"\u00c7\u0131k\u0131\u015f", None))
        self.HesaplarimveBakiyeButon.setText(QCoreApplication.translate("MainWindow", u"Hesaplar\u0131m ve Bakiye", None))
        self.IslemGecmisiButon.setText(QCoreApplication.translate("MainWindow", u"\u0130\u015flem Ge\u00e7mi\u015fi", None))
        self.PortfoyDurumuButon.setText(QCoreApplication.translate("MainWindow", u"Portf\u00f6y Durumu", None))
#if QT_CONFIG(whatsthis)
        self.infoOfInvestor.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toplambakiye.setText(QCoreApplication.translate("MainWindow", u"Toplam Bakiye", None))
        self.toplambakiye1.setText(QCoreApplication.translate("MainWindow", u"825.000\u20ba", None))
        self.riskprofili.setText(QCoreApplication.translate("MainWindow", u"Risk Profili", None))
        self.riskprofili1.setText(QCoreApplication.translate("MainWindow", u"Dengeli", None))
        self.sorumlubroker.setText(QCoreApplication.translate("MainWindow", u"Sorumlu Broker", None))
        self.sorumlubroker1.setText(QCoreApplication.translate("MainWindow", u"Mehmet", None))
        self.HesapSayisi.setText(QCoreApplication.translate("MainWindow", u"Hesap Say\u0131s\u0131", None))
        self.HesapSayisi1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.HesaplarimInfo.setText(QCoreApplication.translate("MainWindow", u"Hesaplar\u0131m", None))
        self.HesapNoLabel.setText(QCoreApplication.translate("MainWindow", u"Hesap No", None))
        self.HesapNoLabel1.setText(QCoreApplication.translate("MainWindow", u"HESAPNO", None))
        self.BakiyeLabel.setText(QCoreApplication.translate("MainWindow", u"Bakiye", None))
        self.YatirimHesabiLabel.setText(QCoreApplication.translate("MainWindow", u"Yat\u0131r\u0131m Hesab\u0131", None))
        self.BakiyeLabel1.setText(QCoreApplication.translate("MainWindow", u"800000\u20ba", None))
        self.HesapAcilisLabel.setText(QCoreApplication.translate("MainWindow", u"Hesap A\u00e7\u0131l\u0131\u015f Tarihi", None))
        self.HesapAcilisLabel1.setText(QCoreApplication.translate("MainWindow", u"10.12.2025", None))
        self.KomisyonLabel.setText(QCoreApplication.translate("MainWindow", u"Komisyon Miktar\u0131", None))
        self.KomisyonLabel1.setText(QCoreApplication.translate("MainWindow", u"Standart Plan", None))
        self.DurumLabel.setText(QCoreApplication.translate("MainWindow", u" Durum", None))
        self.DurumLabel1.setText(QCoreApplication.translate("MainWindow", u"Aktif", None))
        self.RiskProfiliFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Risk Profili", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Risk Profili T\u00fcr\u00fc Buraya Yaz\u0131lcak", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Risk Profili A\u00e7\u0131klama", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Maks Hisse Oran\u0131", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"%80", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sorumlu Broker", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"  M", None))
        self.YatrmcSorumluBrokerLabel.setText(QCoreApplication.translate("MainWindow", u"SorumluBroker ismi", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.YatrmcBrokerTelLabel.setText(QCoreApplication.translate("MainWindow", u"05*********", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"E-posta", None))
        self.yatrmcBrokerEpostaLabel.setText(QCoreApplication.translate("MainWindow", u"mehmet y\u0131ld\u0131rr@gmail.com", None))
        self.label_13.setText("")
        self.label_15.setText("")
        self.KullaniciAdiLabel_2.setText(QCoreApplication.translate("MainWindow", u"Kullan\u0131c\u0131 ad\u0131", None))
        self.YatirimciPaneliLabel_2.setText(QCoreApplication.translate("MainWindow", u"Yat\u0131r\u0131mc\u0131 Paneli", None))
        self.ExitButton_2.setText(QCoreApplication.translate("MainWindow", u"\u00c7\u0131k\u0131\u015f", None))
        self.HesaplarimveBakiyeButon_2.setText(QCoreApplication.translate("MainWindow", u"Hesaplar\u0131m ve Bakiye", None))
        self.IslemGecmisiButon_2.setText(QCoreApplication.translate("MainWindow", u"\u0130\u015flem Ge\u00e7mi\u015fi", None))
        self.PortfoyDurumuButon_2.setText(QCoreApplication.translate("MainWindow", u"Portf\u00f6y Durumu", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0130con", None))
        self.ToplamAlisLabel.setText(QCoreApplication.translate("MainWindow", u"Toplam Al\u0131\u015f", None))
        self.ToplamAlisLabel_1.setText(QCoreApplication.translate("MainWindow", u"8562\u266647\u20ba", None))
        self.ToplamSatisIconLabel.setText(QCoreApplication.translate("MainWindow", u"\u0130con", None))
        self.ToplamSatisLabel.setText(QCoreApplication.translate("MainWindow", u"Toplam Sat\u0131s", None))
        self.ToplamSatisLabel_1.setText(QCoreApplication.translate("MainWindow", u"8562\u266647\u20ba", None))
        self.ToplamKomisyonIconLabel.setText(QCoreApplication.translate("MainWindow", u"\u0130con", None))
        self.ToplamKomisyonLabel.setText(QCoreApplication.translate("MainWindow", u"Toplam Komisyon", None))
        self.ToplamKomisyonLabel_1.setText(QCoreApplication.translate("MainWindow", u"8562\u266647\u20ba", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Filtrele", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Hesap", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0130\u015flem Tipi", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ba\u015flang\u0131\u00e7", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Biti\u015f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u00fcm Hesaplar", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Al\u0131\u015f", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Sat\u0131\u015f", None))

        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d.MM.yyyy", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0130\u015flem Ge\u00e7mi\u015fi", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"D\u0131\u015fa Aktar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Yeni S\u00fctun", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tarih & Saat", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0130\u015flem", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Miktar", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birim Fiyat", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Tutar", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Komisyon", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Net Tutar", None));
        self.label_23.setText("")
        self.label_24.setText("")
        self.KullaniciAdiLabel_3.setText(QCoreApplication.translate("MainWindow", u"Kullan\u0131c\u0131 ad\u0131", None))
        self.YatirimciPaneliLabel_3.setText(QCoreApplication.translate("MainWindow", u"Yat\u0131r\u0131mc\u0131 Paneli", None))
        self.ExitButton_3.setText(QCoreApplication.translate("MainWindow", u"\u00c7\u0131k\u0131\u015f", None))
        self.HesaplarimveBakiyeButon_3.setText(QCoreApplication.translate("MainWindow", u"Hesaplar\u0131m ve Bakiye", None))
        self.IslemGecmisiButon_3.setText(QCoreApplication.translate("MainWindow", u"\u0130\u015flem Ge\u00e7mi\u015fi", None))
        self.PortfoyDurumuButon_3.setText(QCoreApplication.translate("MainWindow", u"Portf\u00f6y Durumu", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.PozisyonSayisiLabel.setText(QCoreApplication.translate("MainWindow", u"Pozisyon Say\u0131s\u0131", None))
        self.PozisyonSayisiabel_1.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToplamMaliyet_1.setText(QCoreApplication.translate("MainWindow", u"18265\u20ba", None))
        self.ToplamMaliyetLabel.setText(QCoreApplication.translate("MainWindow", u"Toplam Maliyet", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GuncelDegerLabel_1.setText(QCoreApplication.translate("MainWindow", u"189565\u20ba", None))
        self.GuncelDegerLabel.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncel De\u011fer", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"+%6.45", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Kar/Zarar", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Portf\u00f6y Pozisyonlar\u0131", None))
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Yeni S\u00fctun", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Miktar", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Ort. Maliyet", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Toplam Maliyet", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncel Fiyat", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u" G\u00fcncel De\u011fer", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Kar/Zarar", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"%", None));
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Portf\u00f6y Da\u011f\u0131l\u0131mlar\u0131", None))
    # retranslateUi

# Bu kodları dosyanızın EN ALTINA yapıştırın (girintilere dikkat edin, en solda olmalı)

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    # 1. Uygulamayı yarat
    app = QApplication(sys.argv)

    # 2. Ana pencere çerçevesini oluştur
    MainWindow = QMainWindow()

    # 3. Sizin UI dosyanızdaki tasarımı çağır (Sınıf adını kontrol edin!)
    # Eğer dosyanızdaki sınıf adı 'Ui_Form' ise burayı Ui_Form() yapın.
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow)

    # 4. Pencereyi ekranda göster
    MainWindow.show()

    # 5. Uygulama döngüsünü başlat (Pencere kapanana kadar bekle)
    sys.exit(app.exec())