#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Janelão')
        self.setFixedSize(1200,600)
        
        

        self.window = QWidget()
        self.window.setStyleSheet("background-color: #B0C4DE;")
        self.setCentralWidget(self.window)

        self.topo = QLabel("COVID-19",self)
        self.topo.resize(1200,150)
        self.topo.setStyleSheet('*{background-color: #4169E1; font-size: 25px; padding: 10px;}')

        self.cb = QComboBox(self)
        self.cb.resize(300,35)
        self.cb.move(440,480)
        self.cb.addItem('Teste')
        self.cb.addItems(["Brasil","Estados Unidos", "França","Japão"])

        
        self.infectado = QLabel("XX XXX XXX",self)
        self.infectado.resize(400,200)
        self.infectado.move(0,200)
        self.infectado.setStyleSheet('*{background-color: #D3D3D3; font-size: 25px; padding: 10px;}')
        
        self.recuperado = QLabel("XX XXX XXX",self)
        self.recuperado.resize(400,200)
        self.recuperado.move(402,200)
        self.recuperado.setStyleSheet('*{background-color: #D3D3D3; font-size: 25px; padding: 10px;}')
        
        self.morto = QLabel("XX XXX XXX",self)
        self.morto.resize(400,200)
        self.morto.move(804,200)
        self.morto.setStyleSheet('*{background-color: #D3D3D3; font-size: 25px; padding: 10px;}')


    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
