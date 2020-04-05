# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:17:44 2020

@author: Bill
"""
#passi come parametro il nome del file da modificare e quello nuovo che vai a creare
def  convert_to_csv(filename,rename):
    f = open(filename)


    a = f.read()


    x = a.replace(" ",",")

    f1 = open(rename,"w")
    y = f1.write(x)
    return y

    #f1 = open("dataset.csv","r")
    #print(f1.read())