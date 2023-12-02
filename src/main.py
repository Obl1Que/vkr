from PyQt5 import QtWidgets
from auth import Authorization
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Authorization()
    sys.exit(app.exec_())
