from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from db import Connect


class Authorization(QtWidgets.QWidget):
    def __init__(self):
        super(Authorization, self).__init__()
        desktop = QtWidgets.QApplication.desktop().size()

        self.WIN_WIDTH = 1200
        self.WIN_HEIGHT = 800
        self.CENTER_HOR = (desktop.width() - self.WIN_WIDTH) // 2
        self.CENTER_VER = (desktop.height() - self.WIN_HEIGHT) // 2

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Программа генерации тестовых запросов')
        self.setGeometry(self.CENTER_HOR, self.CENTER_VER, self.WIN_WIDTH, self.WIN_HEIGHT)

        self.labels = {
            'Адрес:': {
                'label': 'laAddress',
                'input': 'inAddress'
            },
            'Порт:': {
                'label': 'laPort',
                'input': 'inPort'
            },
            'Имя пользователя:': {
                'label': 'laUsername',
                'input': 'inUsername'
            },
            'Пароль:': {
                'label': 'laPassword',
                'input': 'inPassword'
            },
            'Название БД:': {
                'label': 'laDatabaseName',
                'input': 'inDatabaseName'
            },
        }

        buttons = {
            'Подключиться': 'btnConnect',
            'Очистить': 'btnClear'
        }

        layout = QVBoxLayout(self)
        layout.addStretch(1)

        for label_text, input_name in self.labels.items():
            setattr(self, input_name['label'], QLabel(self))
            getattr(self, input_name['label']).setMinimumWidth(100)
            getattr(self, input_name['label']).setText(label_text)
            setattr(self, input_name['input'], QLineEdit(self))
            getattr(self, input_name['input']).setMinimumWidth(200)

            layoutInp = QHBoxLayout()
            layoutInp.addStretch(5)
            layoutInp.addWidget(getattr(self, input_name['label']))
            layoutInp.addStretch(1)
            layoutInp.addWidget(getattr(self, input_name['input']))
            layoutInp.addStretch(5)
            layout.addLayout(layoutInp)

        layoutBtn = QHBoxLayout()
        layoutBtn.addStretch(100)

        for btn_text, btn_name in buttons.items():
            setattr(self, btn_name, QPushButton(self))
            getattr(self, btn_name).setText(btn_text)
            getattr(self, btn_name).setMinimumWidth(190)
            getattr(self, btn_name).clicked.connect(self.btnClicked)

            layoutBtn.addWidget(getattr(self, btn_name))
            layoutBtn.addStretch(1)

        layoutBtn.addStretch(100)
        layout.addLayout(layoutBtn)
        layout.addStretch(1)

        self.show()

    def btnClicked(self):
        sender = self.sender()

        if sender == self.btnConnect:
            in_labels = True
            for _, item in self.labels.items():
                if not getattr(self, item['input']).text():
                    in_labels = False
                    break
            if in_labels:
                print('Connecting!')

        elif sender == self.btnClear:
            for _, item in self.labels.items():
                getattr(self, item['input']).setText('')
