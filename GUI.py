import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
from PyQt5 import QtCore
import demineur as d
import numpy as np
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

class basicWindow(QWidget):
    def __init__(self,shape,grille):
        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        # self.setLayout.setGeometry(QtCore.QRect(-75, -25, 2000, 2000))
        
        
        for x in range(shape):
            for y in range(shape):
                button = Bouton(x,y,grille)
                print(type(grille))
                # button.clicked.connect(partial(grille.suppression,x,y))
                grid_layout.addWidget(button, x, y)
                grille.grid_button[x,y] = button
                print("le bouton est créé à la case : " + str(x) + " " + str(y))
        # grid_layout.setColumnStretch(0,0)
        self.setWindowTitle("Basic Grid Layout")
        
class Bouton(QPushButton):
    
    def __init__(self,x,y,grille):
        
        super().__init__()
        self.x = x
        self.y = y
        self.grille = grille
        
    def ajout_drapeau(self):
        
        pixmap = QPixmap("drapeau.png")
        icon = QIcon(pixmap)
        self.setIcon(icon)
        self.setIconSize(QSize(30, 30))
        print("ok")
        
    def mousePressEvent(self, event):
        # Récupérer la position de clic
        # item = self.itemAt(event.pos())
    
        if event.button() == Qt.LeftButton:
            self.grille.suppression(self.x,self.y)
    
        elif event.button() == Qt.RightButton:
            self.ajout_drapeau()
    
        # Appeler le comportement par défaut
        super().mousePressEvent(event)



if __name__ == "__main__":
    
    pass
    

    # G = d.Grille((10,10),25)
    # G.play()