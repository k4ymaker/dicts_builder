from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from function import *
import sys
import re

class Ui_Form(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.Mainfunc = MainFunctions()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 700)
        Form.setMinimumSize(QtCore.QSize(850, 700))
        Form.setMaximumSize(QtCore.QSize(850, 700))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        Form.setPalette(palette)
        self.A_title = QtWidgets.QTextBrowser(Form)
        self.A_title.setEnabled(True)
        self.A_title.setGeometry(QtCore.QRect(50, 120, 200, 30))
        self.A_title.setMinimumSize(QtCore.QSize(200, 30))
        self.A_title.setMaximumSize(QtCore.QSize(200, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.A_title.setPalette(palette)
        self.A_title.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.A_title.setObjectName("A_title")
        self.A_content = QtWidgets.QPlainTextEdit(Form)
        self.A_content.setGeometry(QtCore.QRect(50, 150, 200, 500))
        self.A_content.setMinimumSize(QtCore.QSize(200, 500))
        self.A_content.setMaximumSize(QtCore.QSize(200, 500))
        self.A_content.setObjectName("A_content")
        self.B_title = QtWidgets.QTextBrowser(Form)
        self.B_title.setGeometry(QtCore.QRect(280, 120, 200, 30))
        self.B_title.setMinimumSize(QtCore.QSize(200, 30))
        self.B_title.setMaximumSize(QtCore.QSize(200, 30))
        self.B_title.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.B_title.setObjectName("B_title")
        self.C_title = QtWidgets.QTextBrowser(Form)
        self.C_title.setGeometry(QtCore.QRect(510, 120, 200, 30))
        self.C_title.setMinimumSize(QtCore.QSize(200, 30))
        self.C_title.setMaximumSize(QtCore.QSize(200, 30))
        self.C_title.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.C_title.setObjectName("C_title")
        self.B_content = QtWidgets.QPlainTextEdit(Form)
        self.B_content.setGeometry(QtCore.QRect(280, 150, 200, 500))
        self.B_content.setMinimumSize(QtCore.QSize(200, 500))
        self.B_content.setMaximumSize(QtCore.QSize(200, 500))
        self.B_content.setPlainText("")
        self.B_content.setObjectName("B_content")
        self.C_content = QtWidgets.QPlainTextEdit(Form)
        self.C_content.setGeometry(QtCore.QRect(510, 150, 200, 500))
        self.C_content.setMinimumSize(QtCore.QSize(200, 500))
        self.C_content.setMaximumSize(QtCore.QSize(200, 500))
        self.C_content.setObjectName("C_content")
        self.combination_content = QtWidgets.QTextBrowser(Form)
        self.combination_content.setEnabled(True)
        self.combination_content.setGeometry(QtCore.QRect(60, 20, 120, 30))
        self.combination_content.setMinimumSize(QtCore.QSize(120, 30))
        self.combination_content.setMaximumSize(QtCore.QSize(120, 30))
        self.combination_content.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.combination_content.setObjectName("combination_content")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 50, 91, 66))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.AC_combination = QtWidgets.QCheckBox(self.widget)
        self.AC_combination.setObjectName("AC_combination")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.AC_combination)
        self.ABC_combination = QtWidgets.QCheckBox(self.widget)
        self.ABC_combination.setObjectName("ABC_combination")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ABC_combination)
        self.ACB_combination = QtWidgets.QCheckBox(self.widget)
        self.ACB_combination.setObjectName("ACB_combination")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ACB_combination)
        self.AB_combination = QtWidgets.QCheckBox(self.widget)
        self.AB_combination.setObjectName("AB_combination")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.AB_combination)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 30, 324, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.file_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.file_name.setMinimumSize(QtCore.QSize(150, 25))
        self.file_name.setMaximumSize(QtCore.QSize(150, 25))
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 0, 1, 1, 1)
        self.start = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start.setMinimumSize(QtCore.QSize(80, 25))
        self.start.setMaximumSize(QtCore.QSize(80, 25))
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 0, 2, 1, 1)
        self.name = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.name.setEnabled(True)
        self.name.setMinimumSize(QtCore.QSize(70, 25))
        self.name.setMaximumSize(QtCore.QSize(70, 25))
        self.name.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)

        self.retranslateUi(Form)        
        self.show_A_list()
        self.show_B_list()
        self.show_C_list()
        self.start.clicked.connect(self.generate_dictionary)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "字典生成器"))
        self.A_title.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">A项</span></p></body></html>"))
        self.B_title.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">B项</span></p></body></html>"))
        self.C_title.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">C项</span></p></body></html>"))
        self.combination_content.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">字典组合方式</span></p></body></html>"))
        self.AC_combination.setText(_translate("Form", "AC"))
        self.ABC_combination.setText(_translate("Form", "ABC"))
        self.ACB_combination.setText(_translate("Form", "ACB"))
        self.AB_combination.setText(_translate("Form", "AB"))
        self.start.setText(_translate("Form", " 开始生成"))
        self.name.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">文件名称：</p></body></html>"))

    def show_A_list(self):
        try:
            show_content = self.Mainfunc.read_dict(".\\db\\A.txt")
            self.A_content.setPlainText(show_content)
        except Exception as e:
            print(e)

    def show_B_list(self):
        try:
            show_content = self.Mainfunc.read_dict(".\\db\\B.txt")
            self.B_content.setPlainText(show_content)
        except Exception as e:
            print(e)

    def show_C_list(self):
        try:
            show_content = self.Mainfunc.read_dict(".\\db\\C.txt")
            self.C_content.setPlainText(show_content)
        except Exception as e:
            print(e)

    def generate_dictionary(self):
        try:
            self.start.setEnabled(False)
            tmp_A_content = self.A_content.toPlainText()
            tmp_B_content = self.B_content.toPlainText()
            tmp_C_content = self.C_content.toPlainText()
            tmp_file_name = self.file_name.text()
            file_name = re.sub(r"[\./\\]", "", tmp_file_name)
            if(file_name.strip()==""):
                file_name = "passwordFile"
            tmp_A = tmp_A_content.split("\n")
            tmp_B = tmp_B_content.split("\n")
            tmp_C = tmp_C_content.split("\n")

            A_content = [i for i in tmp_A if i != '']
            B_content = [i for i in tmp_B if i != '']
            C_content = [i for i in tmp_C if i != '']

            Options_AB = 0
            Options_AC = 0
            Options_ABC = 0
            Options_ACB = 0
            if(self.AB_combination.isChecked()):
                Options_AB = 1
            if(self.AC_combination.isChecked()):
                Options_AC = 1
            if(self.ABC_combination.isChecked()):
                Options_ABC = 1
            if(self.ACB_combination.isChecked()):
                Options_ACB = 1
            BIN_AllOptions = str(Options_ACB)+str(Options_ABC)+str(Options_AC)+str(Options_AB)
            DEC_AllOptions = int(BIN_AllOptions,2)

            if(DEC_AllOptions != 0):
                QMessageBox.about(self, "提醒", "即将开始生成字典，请耐心等待......    ")
                self.Mainfunc.select_method(A_content, B_content, C_content, str(BIN_AllOptions), file_name)
                QMessageBox.about(self, "运行成功", "文件 "+file_name+".txt 已保存在当前目录    ")
            elif(DEC_AllOptions == 0):
                QMessageBox.about(self, "运行失败", "未检测到字典组合方式，生成字典失败。    ")
            self.start.setEnabled(True)

        except Exception as e:
            print(e)
        
if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Form()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)