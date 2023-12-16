# Create graphical user interfaces with Python and PyQt
# Connect the user's events on the app's GUI with the app's logic
# Organize a PyQt app using a proper project layout
# Create a fully functional GUI application with PyQt 

'''
PyQt is a Python binding for Qt, which is a set of C++ libraries and development tools providing platform-independent abstractions for graphical user interfaces (GUIs). Qt also provides tools for networking, threads, regular expressions, SQL databases, SVG, OpenGL, XML, and many other powerful features.
'''

'''import sys 
from PyQt6.QtWidgets import QApplication, QLabel, QWidget 

app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)#x, y, width, height
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)
window.show()
sys.exit(app.exec())'''

'''
- Widgets
- Layout managers
- Dialogs
- Main windows
- Applications 
- Event loops
- Signals and slots
'''

'''
Common and useful PyQt widgets:
- buttons
- labels
- line edits
- combo boxes
- radio buttons
'''

'''
PyQt provides four basic layout manager classes:

1. QHBoxLayout
2. QVBoxLayout
3. QGridLayout
4. QFormLayout
'''

'''import sys 

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QHBoxLayout")

layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())'''

# Here's how you can create a QVBoxLayout object containing three buttons:

'''import sys 

from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QVBoxLayout")

layout = QVBoxLayout()
layout.addWidget(QPushButton("Top"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Bottom"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())'''

# Here's how to create a grid layout arrangement in your GUI:

'''import sys 

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QGridLayout")

layout = QGridLayout()
layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
layout.addWidget(
    QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2
)
window.setLayout(layout)

window.show()
sys.exit(app.exec())'''

# Form layout example 

'''import sys 

from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QFormLayout")

layout = QFormLayout()
layout.addRow("Name:", QLineEdit())
layout.addRow("Age:", QLineEdit())
layout.addRow("Job:", QLineEdit())
layout.addRow("Hobbies:", QLineEdit())
window.setLayout(layout)

window.show()
sys.exit(app.exec())'''

# Dialog-style application 

'''import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())'''


'''
QMainWindow framework graphical components:

Component       Position on Window      Description

One menu bar        Top             Holds the application's main menu

One or more 
toolbars            Sides           Hold tool button and other
                                    widgets, such as QComboBox,
                                    and more

One central widget   Center         Holds the window's central
                                    widget, which can be of any
                                    type, including a composite
                                    widget.

One or more 
dock widgets        Around the      Are small, movable, and hidable
                    central widget    windows.

One status bar      Bottom          Holds the application's status
                                    bar.

'''

# You can set the window's central widget with the .setCentralWidget() method
# The main window's layout will allow you to have only one central widget
# but it can be a single or a composite widget.
# The following code example shows you how to use QMainWindow
# to create a main window-style application:

'''import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
    
    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):  # Corrected method name
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):  # Corrected method name
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())'''

'''
Responsabilities of QApplication class:

- Handling app's initialization and finalization 
- providing the event loop and event handling
- handling most system-wide and application-wide settings
- providing access to global information, such as the aapplication's directory, screen size, and so on
- Parsing common command-line arguments
- defining the application's look and feel 
- providing localization capabilities
'''

# signals and slots example. With Hello, World.

'''import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText("Hello, World!")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

button = QPushButton("Greet")
button.clicked.connect(greet)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())'''

'''
About Calculator MVC

1. The user performs an action or request (event) on the view (GUI).
2. The view notifies the controller about the user's action.
3. The controller gets the user's request and queries the model for a response.
4. The model processes the controller's query, performs the required computations, and returns the result. 
5. The controler receives the model's response and updates the view accordingly. 
6. The user finally sees the requested result on the view.
'''

#import sys 

#from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget 


import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")


class PyCalc:
    """PyCalc's controller class"""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def evaluateExpression(expression):
        """Evaluate an expression."""
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG
        return result

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(partial(self._buildExpression, keySymbol))
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)


def main():
    """PyCalc's main function"""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=PyCalc.evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())


if __name__ == "__main__":
    main()




