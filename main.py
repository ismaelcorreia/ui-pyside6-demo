# 1ST TEST🚀
# By Ismael Clever


# importação dos Módulos Python
import sys
import os

# Importação dos components Gráficos
from qt_design import *
from gui.windows.main_window.ui_main_window import UI_MainWindow


# MAIN - Class Principal
class MainWindow(QMainWindow):
    # Inicializador
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.ui.toggle_buttom.clicked.connect(self.toggle_button)
        self.ui.menu_btn_1.clicked.connect(lambda: self.show_page(1))
        self.ui.menu_btn_2.clicked.connect(lambda: self.select_menu(self.ui.menu_btn_2, 2))
        self.ui.menu_btn_1.clicked.connect(lambda: self.select_menu(self.ui.menu_btn_1, 1))
        self.ui.settings_btn.clicked.connect(lambda: self.select_menu(self.ui.settings_btn, 0))
        self.show()

    def select_menu(self, btn_clicked, index):
        self.show_page(index)
        for btn_menu in self.ui.side_menu.findChildren(QPushButton):
            try:
                btn_menu.set_active(btn_menu == btn_clicked) 
            except:
                pass

    def show_page(self, index):
        self.ui.pages.setCurrentIndex(index)


    # Animação do botão do menu
    def toggle_button(self):
        menu_width = self.ui.side_menu.width()

        width = 240 if  menu_width == 50 else 50

        self.animation = QPropertyAnimation(self.ui.side_menu,b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())