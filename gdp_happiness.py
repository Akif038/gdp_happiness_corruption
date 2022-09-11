# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:55:14 2022

@author: Mehmet Akif
"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import dataframe_image as dfi

happy = pd.DataFrame(pd.read_csv("C:/Users/Mehmet Akif/OneDrive/Masaüstü/2019.csv"))

def gdp_happ():
    #the relationship between GDP and happiness
    sns.jointplot(x="Score",y="GDP per capita",data=happy,kind="reg")
    plt.savefig("GDP_Happiness.pdf", format="pdf", bbox_inches="tight")
    
def corr_happ():
    #the relationship between GDP and perception of corruption
    sns.jointplot(x="Score",y="Perceptions of corruption",data=happy,kind="reg",color="purple")
    plt.savefig("GDP_corruption.pdf", format="pdf", bbox_inches="tight")

def get_data():
    #getting an outlook from the DataFrame
    smp = happy.sample(n=20)
    smp_t = smp.style.background_gradient() #adding a gradient based on values in cell
    dfi.export(smp_t,"mytable_happy.png")
    
    
