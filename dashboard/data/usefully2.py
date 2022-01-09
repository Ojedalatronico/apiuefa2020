import matplotlib.pyplot as plt
from data.get import *
import numpy as np
import streamlit as st


def possession(home,away,team,team2):
    numero = [int(home),int(away)]
    nombres = [str(team),str(team2)]
    plt.pie(numero, labels=nombres, autopct='%1.1f%%')
    plt.title('Possession Match')
    fig2=plt
    return  fig2