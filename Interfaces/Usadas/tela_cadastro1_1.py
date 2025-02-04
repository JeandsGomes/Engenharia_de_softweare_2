# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Cadastro_funcionario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_Cadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 404))
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 243);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_cabecalho = QtWidgets.QFrame(self.centralwidget)
        self.login_cabecalho.setMinimumSize(QtCore.QSize(0, 40))
        self.login_cabecalho.setMaximumSize(QtCore.QSize(16777215, 30))
        self.login_cabecalho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_cabecalho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_cabecalho.setObjectName("login_cabecalho")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.login_cabecalho)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.login_cabecalho)
        self.label.setMinimumSize(QtCore.QSize(180, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.login_cabecalho)
        self.login_conteudo = QtWidgets.QFrame(self.centralwidget)
        self.login_conteudo.setMaximumSize(QtCore.QSize(16777215, 600))
        self.login_conteudo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_conteudo.setObjectName("login_conteudo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.login_conteudo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cadastro_lineEdit_nome_completo = QtWidgets.QLineEdit(self.login_conteudo)
        self.cadastro_lineEdit_nome_completo.setMinimumSize(QtCore.QSize(0, 30))
        self.cadastro_lineEdit_nome_completo.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.cadastro_lineEdit_nome_completo.setObjectName("cadastro_lineEdit_nome_completo")
        self.verticalLayout_3.addWidget(self.cadastro_lineEdit_nome_completo)
        self.cadastro_lineEdit_cpf = QtWidgets.QLineEdit(self.login_conteudo)
        self.cadastro_lineEdit_cpf.setMinimumSize(QtCore.QSize(0, 30))
        self.cadastro_lineEdit_cpf.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.cadastro_lineEdit_cpf.setObjectName("cadastro_lineEdit_cpf")
        self.verticalLayout_3.addWidget(self.cadastro_lineEdit_cpf)
        self.frame_4 = QtWidgets.QFrame(self.login_conteudo)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cadastro_lineEdit_data_nascimento = QtWidgets.QDateEdit(self.frame_4)
        self.cadastro_lineEdit_data_nascimento.setObjectName("cadastro_lineEdit_data_nascimento")
        self.horizontalLayout_2.addWidget(self.cadastro_lineEdit_data_nascimento)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.cadastro_lineEdit_email = QtWidgets.QLineEdit(self.login_conteudo)
        self.cadastro_lineEdit_email.setMinimumSize(QtCore.QSize(0, 30))
        self.cadastro_lineEdit_email.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.cadastro_lineEdit_email.setObjectName("cadastro_lineEdit_email")
        self.verticalLayout_3.addWidget(self.cadastro_lineEdit_email)
        self.cadastro_lineEdit_telefone = QtWidgets.QLineEdit(self.login_conteudo)
        self.cadastro_lineEdit_telefone.setMinimumSize(QtCore.QSize(0, 30))
        self.cadastro_lineEdit_telefone.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.cadastro_lineEdit_telefone.setObjectName("cadastro_lineEdit_telefone")
        self.verticalLayout_3.addWidget(self.cadastro_lineEdit_telefone)
        self.frame_5 = QtWidgets.QFrame(self.login_conteudo)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.cadastro_lineEdit_telefone_2 = QtWidgets.QComboBox(self.frame_5)
        self.cadastro_lineEdit_telefone_2.setObjectName("cadastro_lineEdit_telefone_2")
        self.cadastro_lineEdit_telefone_2.addItem("")
        self.cadastro_lineEdit_telefone_2.addItem("")
        self.horizontalLayout_4.addWidget(self.cadastro_lineEdit_telefone_2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.cadastro_lineEdit_senha = QtWidgets.QLineEdit(self.login_conteudo)
        self.cadastro_lineEdit_senha.setMinimumSize(QtCore.QSize(0, 30))
        self.cadastro_lineEdit_senha.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 5px;")
        self.cadastro_lineEdit_senha.setObjectName("cadastro_lineEdit_senha")

        # ocultar senha
        self.cadastro_lineEdit_senha.setInputMask("")
        self.cadastro_lineEdit_senha.setText("")
        self.cadastro_lineEdit_senha.setObjectName("login_lineEdit_senha")
        self.cadastro_lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.verticalLayout_3.addWidget(self.cadastro_lineEdit_senha)
        self.verticalLayout.addWidget(self.login_conteudo)
        self.login_confirmacao = QtWidgets.QFrame(self.centralwidget)
        self.login_confirmacao.setMinimumSize(QtCore.QSize(0, 105))
        self.login_confirmacao.setMaximumSize(QtCore.QSize(16777215, 150))
        self.login_confirmacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_confirmacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_confirmacao.setObjectName("login_confirmacao")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.login_confirmacao)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.login_confirmacao)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.login_confirmacao)
        self.frame_2.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cadastro_pushButton_cadastrar = QtWidgets.QPushButton(self.frame_2)
        self.cadastro_pushButton_cadastrar.setMinimumSize(QtCore.QSize(230, 50))
        self.cadastro_pushButton_cadastrar.setMaximumSize(QtCore.QSize(230, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cadastro_pushButton_cadastrar.setFont(font)
        self.cadastro_pushButton_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastro_pushButton_cadastrar.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(255, 144, 14);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(207, 110, 0);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.cadastro_pushButton_cadastrar.setObjectName("cadastro_pushButton_cadastrar")
        self.verticalLayout_2.addWidget(self.cadastro_pushButton_cadastrar)
        self.pushButton_cadastro_entrar_login = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_cadastro_entrar_login.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_cadastro_entrar_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cadastro_entrar_login.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"    \n"
"    color: rgb(0,127,255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_cadastro_entrar_login.setObjectName("pushButton_cadastro_entrar_login")
        self.verticalLayout_2.addWidget(self.pushButton_cadastro_entrar_login)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.login_confirmacao)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.login_confirmacao)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cadastrar Funcionario"))
        self.cadastro_lineEdit_nome_completo.setPlaceholderText(_translate("MainWindow", "Nome completo"))
        self.cadastro_lineEdit_cpf.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.label_2.setText(_translate("MainWindow", "Data de Nascimento:"))
        self.cadastro_lineEdit_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.cadastro_lineEdit_telefone.setPlaceholderText(_translate("MainWindow", "Telefone"))
        self.label_3.setText(_translate("MainWindow", "Cargo:"))
        self.cadastro_lineEdit_telefone_2.setItemText(0, _translate("MainWindow", "Caixa"))
        self.cadastro_lineEdit_telefone_2.setItemText(1, _translate("MainWindow", "Estoque"))
        self.cadastro_lineEdit_senha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.cadastro_pushButton_cadastrar.setText(_translate("MainWindow", "Cadastrar funcionario"))
        self.pushButton_cadastro_entrar_login.setText(_translate("MainWindow", "Já possui cadastro ? Entrar."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())