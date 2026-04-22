import sys
from PyQt5.QtWidgets import QApplication
from .widgets import build_window

# intentar importar recursos compilados si existen
try:
    import exercises.gui_pyqt5.resources_rc  # noqa: F401
except Exception:
    pass

def main():
    app = QApplication.instance() or QApplication(sys.argv)

    # cargar stylesheet
    try:
        with open("exercises/gui_pyqt5/styles.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass

    window = build_window()
    window.show()

    try:
        return_code = app.exec_()
    except AttributeError:
        return_code = app.exec()
    sys.exit(return_code)

if __name__ == "__main__":
    main()
