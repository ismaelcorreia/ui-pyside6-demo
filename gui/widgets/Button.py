# 1ST TEST🚀
# By Ismael Clever

import os

# Importação dos components Gráficos
from qt_design import *


class SideMenuButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 40,
        minimum_width = 50,
        text_padding=55,
        text_color = "#97cabf",
        icon_path = "",
        icon_color = "#97cabf",
        bg_color = "#1b824f",
        bg_hover = "#1e6757",
        bg_pressed = "#1c2433",
        is_active = False
    ):
        super().__init__()
        # Definir configurações
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Definir variáveis locais
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.bg_color = bg_color
        self.bg_hover = bg_hover
        self.is_active = is_active
        self.bg_pressed = bg_pressed
        

        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            icon_path = self.icon_path,
            icon_color = self.icon_color,
            bg_color = self.bg_color,
            bg_hover = self.bg_hover,
            bg_pressed = self.bg_pressed,
            is_active = self.is_active
        )

    def set_style(
        self,
        text_padding=55,
        text_color = "#97cabf",
        icon_path = "",
        icon_color = "#97cabf",
        bg_color = "#1e6757",
        bg_hover = "#1b824f",
        bg_pressed = "#97cabf",
        is_active = False
    ): 
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {bg_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {bg_hover};
        }}
        QPushButton:pressed {{
            background-color: {bg_pressed};
        }}
        """
        active_style = f"""
        QPushButton {{
            background-color: {bg_hover};
            border-right: 5px solid {bg_pressed};
        }} 
        """ 
        if is_active:
            self.setStyleSheet(style + active_style)
        else:
            self.setStyleSheet(style)

    def set_active(self, active):
        self.is_active = active
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            icon_path = self.icon_path,
            icon_color = self.icon_color,
            bg_color = self.bg_color,
            bg_hover = self.bg_hover,
            bg_pressed = self.bg_pressed,
            is_active = self.is_active
        )
    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)

        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0,0, self.minimum_width, self.height())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()


    def draw_icon(self, qp, image, rect, color):

        abs_path = os.path.abspath(os.getcwd())
        path = os.path.join(abs_path, "gui/images/icons/"+image)

        icon = QPixmap(path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) /2,
            (rect.height() - icon.height()) /2,
            icon
        )
        painter.end()