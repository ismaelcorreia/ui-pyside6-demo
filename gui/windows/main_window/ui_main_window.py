# 1ST TEST🚀
# By Ismael Clever

# Importação dos components Gráficos
from qt_design import *

# Importação das páginas (Demo)
from gui.windows.pages.demo_pages import DemoPages
from gui.widgets.Button import SideMenuButton
# Class Principal dos componentes da janela
class UI_MainWindow(object):
    def setup_ui(self,parent):
        if not parent.objectName():
            parent.setObjectName("NÓS Interface")
        
        # Tamanho padrão
        parent.resize(1200,720)
        parent.setMinimumSize(960, 540)
        
        # Frame Central
        self.central_frame = QFrame()

        # Conteúdo
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #1c2433")

        # Menu Lateral
        self.side_menu = QFrame()
        self.side_menu.setMaximumWidth(50)
        self.side_menu.setMinimumWidth(50)
        self.side_menu.setStyleSheet("background-color: #1b824f")

        ## Layout do menu lateral
        self.side_menu_layout = QVBoxLayout(self.side_menu)
        self.side_menu_layout.setContentsMargins(0,0,0,0)
        self.side_menu_layout.setSpacing(0)

        ## Layout dos menus, top 
        self.side_menu_layout_buttons_top = QVBoxLayout()
        self.side_menu_layout_buttons_top.setContentsMargins(0,0,0,0)
        self.side_menu_layout_buttons_top.setSpacing(0)

        self.toggle_buttom = SideMenuButton("Menu",icon_path="icon_menu.svg")
        self.menu_btn_1 = SideMenuButton("Home",is_active=True,icon_path="icon_home.svg")
        self.menu_btn_2 = SideMenuButton("Pesquisar",icon_path="icon_search.svg")

        self.side_menu_layout_buttons_top.addWidget(self.toggle_buttom)         
        self.side_menu_layout_buttons_top.addWidget(self.menu_btn_1)      
        self.side_menu_layout_buttons_top.addWidget(self.menu_btn_2)    
        ## Espacamemto
        self.side_menu_layout_spaceBetween = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)
 

        ## Layout dos menus, rodapé 
        self.side_menu_layout_buttons_bottom = QVBoxLayout()
        self.side_menu_layout_buttons_bottom.setContentsMargins(0,0,0,0)
        self.side_menu_layout_buttons_bottom.setSpacing(0)

        ## botão de configuração
        self.settings_btn = SideMenuButton("settings",icon_path="icon_config.svg")

        ## Label de versão
        self.label_version = QLabel("{NÓS}v1.0.0") 
        self.label_version.setStyleSheet("font-size: 7pt;")
        self.label_version.setMaximumHeight(30)
        self.label_version.setMinimumHeight(30)

        # Adicionar itens, rodapé
        self.side_menu_layout_buttons_bottom.addWidget(self.settings_btn)
        self.side_menu_layout_buttons_bottom.addWidget(self.label_version)


        ## Adicionar os layouts ao layout menu
        self.side_menu_layout.addLayout(self.side_menu_layout_buttons_top)
        self.side_menu_layout.addItem(self.side_menu_layout_spaceBetween)
        self.side_menu_layout.addLayout(self.side_menu_layout_buttons_bottom)
        # Layouts da aplicação 

        ## Layout principal
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        ## Layout de conteúdo
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)


        # Adicionar Widgets ao layout
        self.main_layout.addWidget(self.side_menu)
        self.main_layout.addWidget(self.content) 

        # Barra de topo
        self.top_bar = QFrame()
        self.top_bar.setStyleSheet("background-color: #1e6757; color: #97cabf")
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setMinimumHeight(30)
        
        ## Layout para Barra de topo
        self.layout_top_bar = QHBoxLayout(self.top_bar)
        self.layout_top_bar.setContentsMargins(20,0,20,0)

        ## Label para Barra de Topo, lado esquerdo
        self.label_tp_bar_left = QLabel("Seja bem-vindo ao {NÓS}") 

        ## Label para Barra de Topo, lado esquerdo
        self.top_spaceBetween = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        ## Label para Barra de Topo, lado direito
        self.label_tp_bar_rigth = QLabel("Feito por Ismael Clever") 

        ## Adicionar os Itens ao layout da barra de topo
        self.layout_top_bar.addWidget(self.label_tp_bar_left)
        self.layout_top_bar.addItem(self.top_spaceBetween)
        self.layout_top_bar.addWidget(self.label_tp_bar_rigth)
 
        # Páginas
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #1b824f") 
        self.ui_pages = DemoPages()
        self.ui_pages.setup_page(self.pages, 5)

        # Rodapé
        self.bottom_bar = QFrame()
        self.bottom_bar.setStyleSheet("background-color: #1e6757; color: #97cabf")
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setMinimumHeight(30)

        # Adicionar Widgets ao layout do conteúdo
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages) 
        self.content_layout.addWidget(self.bottom_bar) 


        # Adicionar Widgets ao Window
        parent.setCentralWidget(self.central_frame)