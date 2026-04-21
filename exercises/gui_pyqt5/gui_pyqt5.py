from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

def main():
    app= QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Hola la Rata Audaz trata de aprender PyQt5")
    window.resize(700, 900)

    label = QLabel(" ¡ La Rata Audaz te da la bienvenida a PyQt5 ! ")
    label.setAlignment(Qt.AlignCenter)
    
    button = QPushButton("¡ Cerrar Ventana de La Rata Audaz !")
    button.clicked.connect(app.quit)

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()