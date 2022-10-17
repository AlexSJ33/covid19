#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from interface import Ui_MainWindow
from interface import *
import requests


import json
from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL,'')




from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

class Covid(QMainWindow, Ui_MainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        self.combo.addItems(
            ["Todo Brasil","São Paulo","Minas Gerais","Paraná","Rio Grande do Sul","Rio de Janeiro","Santa Catarina",
            "Goiás","Bahia","Ceará","Espírito Santo","Pernambuco","Pará","Distrito Federal","Mato Grosso","Paraíba",
            "Amazonas","Mato Grosso do Sul","Rio Grande do Norte","Maranhão","Rondônia","Piauí","Tocantins",
            "Sergipe","Alagoas","Amapá","Roraima","Acre"])
        
        self.pais = str(self.combo.currentText())
        self.combo.activated.connect(self.get_info)
        pixmap = QPixmap("covid19/virus.png")
        self.label_6.setPixmap(pixmap)
        

    def get_info(self):

            resposta = requests.get("https://covid19-brazil-api.vercel.app/api/report/v1/")
            dados = resposta
            dados = json.loads(dados.text)

            pais = str(self.combo.currentText())
            total_con = []
            total_rec = []
            total_obt = []

            for estados in dados["data"]:
                if estados["state"] == pais:
                    confirmados = estados["cases"]
                    recuperados = estados["suspects"]
                    obitos      = estados["deaths"]
                    data        = estados["datetime"]
                    data_strp   = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.850Z")
                    data_frm    = data_strp.strftime("%A, %d, de %B de %Y")


                elif pais == 'Todo Brasil':
                        total_con.append(estados["cases"])
                        total_rec.append(estados["suspects"])
                        total_obt.append(estados["deaths"])

                        confirmados = sum(total_con)
                        recuperados = sum(total_rec)
                        obitos      = sum(total_obt)
                        data        = estados["datetime"]
                        data_strp   = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.850Z")
                        data_frm    = data_strp.strftime("%A, %d, de %B de %Y")


            self.label_infectados.setText(str(confirmados))
            self.label_recuperados.setText(str(recuperados))
            self.label_obitos.setText(str(obitos))
            self.label_data.setText(data_frm)
            self.label_data_2.setText(data_frm)
            self.label_data_3.setText(data_frm)


if __name__=='__main__':
    qt = QApplication(sys.argv)
    covid = Covid()
    covid.show()
    qt.exec_()