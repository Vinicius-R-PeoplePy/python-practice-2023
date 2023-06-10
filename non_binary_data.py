import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QDialog
from PyQt5.QtGui import QPixmap, QFont, QColor, QPalette

class ImageMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu de consulta de identidade de gênero')
        self.setFixedSize(600, 600)

        # Set window background color
        self.set_background_color(31, 0, 90)

        # Set font properties
        self.set_font_properties(25, 'Mondwest NeueBit', 'rgb(17, 245, 0)')

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.menu_label = QLabel('Menu:')
        self.menu_label.setFont(self.font)
        self.menu_label.setStyleSheet('color: rgb(17, 245, 0)')

        self.menu_text = QTextEdit()
        self.menu_text.setReadOnly(True)
        self.menu_text.setFont(self.font)
        self.menu_text.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(31, 0, 90)')
        self.menu_text.setText("Digite 1 para consultar tipos de identidades não-binárias\n\n" 
                                "Digite 2 para identificar com qual gênero você se identifica e por quê.\n\n"  
                                "Digite 3 para carregar e mostrar a resposta salva.") 

        self.input_label = QLabel('Digite a opção escolhida:')
        self.input_label.setFont(self.font)
        self.input_label.setStyleSheet('color: rgb(17, 245, 0)')

        self.input_text = QLineEdit()
        self.input_text.setFont(self.font)
        self.input_text.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(31, 0, 90)')

        self.input_button = QPushButton('Submit')
        self.input_button.clicked.connect(self.process_choice)
        self.input_button.setStyleSheet('background-color: rgb(31, 0, 90); color: rgb(17, 245, 0)')

        self.layout.addWidget(self.menu_label)
        self.layout.addWidget(self.menu_text)
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.input_button)

        self.setLayout(self.layout)

        self.saved_text = ""

    def set_background_color(self, r, g, b):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(r, g, b))
        self.setPalette(palette)

    def set_font_properties(self, font_size, font_type, font_color):
        self.font = QFont(font_type, font_size)
        self.setStyleSheet(f"color: {font_color};")

    def process_choice(self):
        choice = self.input_text.text()
        if choice == '1':
            self.show_image_dialog()
        elif choice == '2':
            self.show_text_input_dialog()
        elif choice == '3':
            self.show_saved_text_dialog()

    def show_image_dialog(self):
        image_dialog = QDialog(self)
        image_dialog.setWindowTitle('Non-Binary People')
        image_dialog.setFixedSize(700, 1000)

        image_label = QLabel(image_dialog)
        pixmap = QPixmap('C:\\Users\\ovni\\Documents\\Python\\consulta-gênero\\tipos-de-pessoas-nao-binarias.jpg')
        image_label.setPixmap(pixmap.scaled(700, 1000))

        close_button = QPushButton('Close', image_dialog)
        close_button.clicked.connect(image_dialog.close)
        close_button.setStyleSheet('background-color: rgb(31, 0, 90); color: rgb(17, 245, 0)')

        dialog_layout = QVBoxLayout(image_dialog)
        dialog_layout.addWidget(image_label)
        dialog_layout.addWidget(close_button)
        image_dialog.setLayout(dialog_layout)

        image_dialog.exec_()

    def show_text_input_dialog(self):
        text_input_dialog = QDialog(self)
        text_input_dialog.setWindowTitle('Text Input')
        text_input_dialog.setFixedSize(400, 200)
        text_input_dialog.setStyleSheet('background-color: rgb(31, 0, 90)')

        text_label = QLabel('Digite a opção escolhida:', text_input_dialog)
        text_label.setFont(self.font)
        text_label.setStyleSheet('color: rgb(17, 245, 0)')

        text_input = QLineEdit(text_input_dialog)
        text_input.setFont(self.font)
        text_input.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(31, 0, 90)')

        save_button = QPushButton('Save', text_input_dialog)
        save_button.clicked.connect(lambda: self.save_text(text_input.text(), text_input_dialog))
        save_button.setStyleSheet('background-color: rgb(31, 0, 90); color: rgb(17, 245, 0)')

        dialog_layout = QVBoxLayout(text_input_dialog)
        dialog_layout.addWidget(text_label)
        dialog_layout.addWidget(text_input)
        dialog_layout.addWidget(save_button)
        text_input_dialog.setLayout(dialog_layout)

        text_input_dialog.exec_()

    def show_saved_text_dialog(self):
        saved_text_dialog = QDialog(self)
        saved_text_dialog.setWindowTitle('Saved Text')
        saved_text_dialog.setFixedSize(400, 200)
        saved_text_dialog.setStyleSheet('background-color: rgb(31, 0, 90)')

        saved_text_label = QLabel('Saved Text:', saved_text_dialog)
        saved_text_label.setFont(self.font)
        saved_text_label.setStyleSheet('color: rgb(17, 245, 0)')

        saved_text_display = QTextEdit(saved_text_dialog)
        saved_text_display.setReadOnly(True)
        saved_text_display.setFont(self.font)
        saved_text_display.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(31, 0, 90)')
        saved_text_display.setText(self.saved_text)

        close_button = QPushButton('Close', saved_text_dialog)
        close_button.clicked.connect(saved_text_dialog.close)
        close_button.setStyleSheet('background-color: rgb(31, 0, 90); color: rgb(17, 245, 0)')

        dialog_layout = QVBoxLayout(saved_text_dialog)
        dialog_layout.addWidget(saved_text_label)
        dialog_layout.addWidget(saved_text_display)
        dialog_layout.addWidget(close_button)
        saved_text_dialog.setLayout(dialog_layout)

        saved_text_dialog.exec_()

    def save_text(self, text, dialog):
        self.saved_text = text
        QMessageBox.information(dialog, 'Salvo!', 'Texto salvo com sucesso!')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    menu = ImageMenu()
    menu.show()

    sys.exit(app.exec_())










