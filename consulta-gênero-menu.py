import sys
from non_binary_data import ImageMenu
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    menu = ImageMenu()
    menu.show()

    sys.exit(app.exec_())
