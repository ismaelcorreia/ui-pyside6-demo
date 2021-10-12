# 1ST TEST🚀
# By Ismael Clever

# Importação dos components Gráficos
from qt_design import *

class DemoPages(object):
    def setup_page(self, parent, totalPage):
        if not parent.objectName():
            parent.setObjectName("NÓS Interface")
        parent.resize(1070,664)
        index = 0
        while index < totalPage:
            parent.addWidget(self.drawPage(index))
            index = index +1

    def drawPage(self, index):
        self.page = QWidget()
        self.page.setObjectName(str(index)+" page")
        self.verticalLayout = QVBoxLayout(self.page)
        if index != 0:
            self.labelNamePage = QLabel("Página "+str(index)) 
            self.labelNamePage.setStyleSheet("font-weight: bold")  
        else:
            self.labelNamePage = QLabel() 
            self.labelNamePage.setStyleSheet("font-weight: bold;font-size: 16pt")  
            self.labelNamePage.setText("{NÓS}")

        self.labelNamePage.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.labelNamePage)
        return self.page