from class_coeff import *
from PyQt5 import QtWidgets
import authorization, class_Error, MySQLdb

class Authorization_User(QtWidgets.QMainWindow, authorization.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_Btn)
        self.pushButton_2.clicked.connect(self.push_Btn_2)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def value(self):

        log = self.lineEdit.text()
        pswd = self.lineEdit_2.text()
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        return log, pswd

    def push_Btn(self):
        log, pswd = self.value()
        db = con()
        cursor = db.cursor()
        try:
            cursor.execute('insert into authorization_user (log_in, password) values ("%s", "%s")' % (log, pswd))
            db.commit()
        except: db.rollback()
        db.close()

    def push_Btn_2(self):
        log, pswd = self.value()
        db = con()
        bool_shit = true_or_false(log, pswd, db)
        db.close()
        if bool_shit == True:
            self.window = Coeff(bool_shit)
            self.window.show()
            self.close()
        else:
            self.window = class_Error.Error_Input()
            self.window.show()
            self.close()

def con():

    return MySQLdb.connect(host='localhost', database='nir', user='root', password='12345678')

def true_or_false(log, pswd, db):

    crs, cursor, cursor_1 = db.cursor(), db.cursor(), db.cursor()
    crs.execute('SELECT id FROM authorization_user')
    st = [item[0] for item in crs.fetchall()]
    elem, k = st[-1], 1
    bool_shit = True
    while k != elem + 1:
        cursor.execute('SELECT log_in FROM authorization_user WHERE id = %s' % k)
        cursor_1.execute('SELECT password FROM authorization_user WHERE id = %s' % k)
        status = [item[0] for item in cursor.fetchall()]
        stat = [elem[0] for elem in cursor_1.fetchall()]
        status = ''.join(str(e) for e in status)
        stat = ''.join(str(e) for e in stat)
        if status == log and stat == pswd:
            bool_shit = True
            break
        else:
            bool_shit = False
            k += 1
    return bool_shit