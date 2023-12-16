from PyQt5 import QtWidgets


class Workspace(QtWidgets.QWidget):
    def __init__(self):
        super(Workspace, self).__init__()
        self.label = QtWidgets.QLabel('Work Widget')
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)