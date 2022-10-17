#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from interface import Ui_MainWindow
from interface import *
import requests
import string
import json
from datetime import datetime


from PyQt5.QtWidgets import QMainWindow, QApplication

class Covid(QMainWindow, Ui_MainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.label_infectados.setText((str(self.get_info()[0])))
        self.label_recuperados.setText((str(self.get_info()[1])))
        self.label_obitos.setText((str(self.get_info()[2])))
        self.label_data.setText((str(self.get_info()[3])))
        self.label_data_2.setText((str(self.get_info()[3])))
        self.label_data_3.setText((str(self.get_info()[3])))

        
        self.combo.addItems(["Brazil","Estados Unidos", "França","Japão"])
        pais = self.combo.currentText()
        self.combo.activated[str].connect(self.get_info)
        
        print(str(pais))
        
        #return str(pais)
        
        
        

    def get_info(eventObejct):

        

        #resposta = requests.get("https://covid19.mathdro.id/api/countries/{}".format())

        resposta = requests.get("http://covid19.mathdro.id/api")
        dados = resposta
        dados = json.loads(dados.text)

        confirmados = dados["confirmed"]["value"]
        recuperados = dados["recovered"]["value"]
        obitos      = dados["deaths"]["value"]
        data        = dados["lastUpdate"]
        data_frm    = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.000Z")
        data_frm = data_frm.strftime("%c")



        
    
        
        return confirmados, recuperados, obitos, data_frm

        print(confirmados)
        print(recuperados)
        print(obitos)
        print(data)
    
        




if __name__=='__main__':
    qt = QApplication(sys.argv)
    covid = Covid()
    covid.show()
    qt.exec_()