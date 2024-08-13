import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from main_window import MainWindow
from variables import WINDOW_ICON_PATH

def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet('font-size: 50px;')
    return label1

if __name__ == '__main__':
    #Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    #Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Executa tudo
    window.show()
    app.exec()