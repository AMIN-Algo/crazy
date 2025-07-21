from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QRadioButton

def show_win():
    win = QMessageBox()
    win.setText('Правилно\nВы выйграли героскутер')
    win.exec()

def show_lose():
    win = QMessageBox()
    win.setText('Не правилно\nВы выйграли плакат')
    win.exec()


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(400, 200)


question = QLabel('когда был создан канал?')
answer_1 = QRadioButton('2010')
answer_2 = QRadioButton('2013')
answer_3 = QRadioButton('2015')
answer_4 = QRadioButton('2009')
answer_5 = QRadioButton('2000')
answer_6 = QRadioButton('2012')

line = QVBoxLayout()
lineH_1 = QHBoxLayout()
lineH_2 = QHBoxLayout()
lineH_3 = QHBoxLayout()
lineH_4 = QHBoxLayout()

lineH_1.addWidget(question, alignment=Qt.AlignCenter)
lineH_2.addWidget(answer_1, alignment=Qt.AlignCenter)
lineH_2.addWidget(answer_2, alignment=Qt.AlignCenter)
lineH_3.addWidget(answer_3, alignment=Qt.AlignCenter)
lineH_3.addWidget(answer_4, alignment=Qt.AlignCenter)
lineH_4.addWidget(answer_5, alignment=Qt.AlignCenter)
lineH_4.addWidget(answer_6, alignment=Qt.AlignCenter)



line.addLayout(lineH_1)
line.addLayout(lineH_2)
line.addLayout(lineH_3)
line.addLayout(lineH_4)
main_win.setLayout(line)

answer_1.clicked.connect(show_lose)
answer_2.clicked.connect(show_lose)
answer_3.clicked.connect(show_lose)
answer_4.clicked.connect(show_lose)
answer_5.clicked.connect(show_win)
answer_6.clicked.connect(show_lose)

main_win.setStyleSheet('''background-color: green;
                       font-size: 15px''')
answer_1.setStyleSheet('''color: red''')
answer_2.setStyleSheet('''color: orange''')
answer_3.setStyleSheet('''color: blue''')
answer_4.setStyleSheet('''color: black''')
answer_5.setStyleSheet('''color: brown''')
answer_6.setStyleSheet('''color: yellow''')


main_win.show()
app.exec()
