from PyQt5 import QtWidgets
import class_auth, class_coeff, Error

class Error_Input(QtWidgets.QMainWindow, Error.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.psh_btn)
        self.pushButton_2.clicked.connect(self.psh_btn_1)

    def psh_btn(self):
        self.window = class_coeff.Coeff(bool_shit=False)
        self.window.show()
        self.close()

    def psh_btn_1(self):
        self.window = class_auth.Authorization_User()
        self.window.show()
        self.close()