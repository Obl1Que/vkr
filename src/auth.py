from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class Authorization(QtWidgets.QWidget):
    def __init__(self):
        super(Authorization, self).__init__()
        desktop = QtWidgets.QApplication.desktop().size()

        self.WIN_WIDTH = 1200
        self.WIN_HEIGHT = 800
        self.CENTER_HOR = (desktop.width() - self.WIN_WIDTH) // 2
        self.CENTER_VER = (desktop.height() - self.WIN_HEIGHT) // 2
        self.CHOOSE = False

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Программа генерации тестовых запросов')
        self.setGeometry(self.CENTER_HOR, self.CENTER_VER, self.WIN_WIDTH, self.WIN_HEIGHT)

        self.labels = {
            'Адрес:': {
                'label': 'laAddress',
                'input': 'inAddress',
                'visible': True
            },
            'Порт:': {
                'label': 'laPort',
                'input': 'inPort',
                'visible': True
            },
            'Путь к файлу:': {
                'label': 'laChoose',
                'input': 'inChoose',
                'visible': False
            },
            '': {
                'label': 'laStretch',
                'visible': False
            },
            'Имя пользователя:': {
                'label': 'laUsername',
                'input': 'inUsername',
                'visible': True
            },
            'Пароль:': {
                'label': 'laPassword',
                'input': 'inPassword',
                'visible': True
            },
            'Название БД:': {
                'label': 'laDatabaseName',
                'input': 'inDatabaseName',
                'visible': True
            },
        }

        buttons = {
            'Подключиться': 'btnConnect',
            'Формат DB': 'btnFormatDB',
            'Очистить': 'btnClear'
        }

        layout = QVBoxLayout(self)
        layout.addStretch(1)

        for label_text, input_name in self.labels.items():
            setattr(self, input_name['label'], QLabel(self))
            getattr(self, input_name['label']).setMinimumWidth(100)
            getattr(self, input_name['label']).setText(label_text)

            try:
                setattr(self, input_name['input'], QLineEdit(self))
                getattr(self, input_name['input']).setMinimumWidth(200)
            except:
                getattr(self, input_name['label']).setFixedHeight(20)

            layoutInp = QHBoxLayout()
            layoutInp.addStretch(5)
            layoutInp.addWidget(getattr(self, input_name['label']))
            layoutInp.addStretch(1)
            try:
                layoutInp.addWidget(getattr(self, input_name['input']))
            except:
                pass
            layoutInp.addStretch(5)

            layout.addLayout(layoutInp)

        self.laChoose.setVisible(False)
        self.laStretch.setVisible(False)
        self.inChoose.setVisible(False)

        layoutBtn = QHBoxLayout()
        layoutBtn.addStretch(100)

        for btn_text, btn_name in buttons.items():
            setattr(self, btn_name, QPushButton(self))
            getattr(self, btn_name).setText(btn_text)
            getattr(self, btn_name).setMinimumWidth(125)
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
                if not self.CHOOSE:
                    if not item['visible']:
                        continue
                    if not getattr(self, item['input']).text():
                        in_labels = False
                        break
                else:
                    if item['visible'] and item['label'] not in ['laUsername', 'laPassword', 'laDatabaseName']:
                        continue
                    if _ and not getattr(self, item['input']).text():
                        in_labels = False
                        break
            if in_labels:
                print('Connecting!')
        elif sender == self.btnClear:
            for _, item in self.labels.items():
                if item['label'] != 'laStretch':
                    getattr(self, item['input']).setText('')
        elif sender == self.btnFormatDB:
            if self.inAddress.isVisible():
                self.inAddress.setVisible(False)
                self.laAddress.setVisible(False)
                self.inPort.setVisible(False)
                self.laPort.setVisible(False)
                self.laChoose.setVisible(True)
                self.inChoose.setVisible(True)
                self.laStretch.setVisible(True)
                self.CHOOSE = True
            else:
                self.inAddress.setVisible(True)
                self.laAddress.setVisible(True)
                self.inPort.setVisible(True)
                self.laPort.setVisible(True)
                self.laChoose.setVisible(False)
                self.inChoose.setVisible(False)
                self.laStretch.setVisible(False)
                self.CHOOSE = False
