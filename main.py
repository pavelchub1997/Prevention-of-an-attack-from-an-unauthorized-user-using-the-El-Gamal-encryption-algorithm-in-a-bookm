#!"C:\Program files\Python36\python.exe"

import sys, class_auth
from PyQt5 import QtWidgets

def main():

    app = QApplication(sys.argv)
    window = class_auth.Authorization_User()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()