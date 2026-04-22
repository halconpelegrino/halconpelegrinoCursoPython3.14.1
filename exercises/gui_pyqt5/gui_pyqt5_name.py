import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("La Rata Audaz aprende PyQt5")
    window.resize(500, 200)

    label = QLabel("¡La Rata Audaz te da la bienvenida a PyQt5!")
    label.setAlignment(Qt.AlignCenter)

    name_input = QLineEdit()
    name_input.setPlaceholderText("Escribe tu nombre aquí")

    def saludar():
        nombre = name_input.text().strip() or "amigo"
        label.setText(f"Hola, {nombre} — ¡bienvenido a PyQt5!")
        name_input.clear()
        name_input.setFocus()

    button = QPushButton("Saludar")
    button.clicked.connect(saludar)

    close_btn = QPushButton("Cerrar")
    close_btn.clicked.connect(app.quit)

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(name_input)
    layout.addWidget(button)
    layout.addWidget(close_btn)
    window.setLayout(layout)

    window.show()
    try:
        return_code = app.exec_()
    except AttributeError:
        return_code = app.exec()
    sys.exit(return_code)


if __name__ == "__main__":
    main()
