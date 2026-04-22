from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


def build_window() -> QWidget:
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
    close_btn.setObjectName("closeBtn")
    close_btn.clicked.connect(window.close)

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(name_input)
    layout.addWidget(button)
    layout.addWidget(close_btn)
    window.setLayout(layout)

    # Exponer widgets útiles para tests
    window._label = label
    window._name_input = name_input
    window._saludar_btn = button
    window._close_btn = close_btn

    return window
