import matplotlib.pyplot as plt
from data.get import *

def bar_chart_goals(data,box):
    #Creating the dataset
    if box == "10 min":
        data=goal_each_10(data)
    elif box == "15 min":
        data=goal_each_15(data)
    data=data[0]
    Courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize = (19, 10))

    plt.bar(Courses, values)
    plt.xlabel("Total goals each 10 min")
    plt.ylabel("Time")
    plt.title("¿Cuántos goles se marcaron en qué tiempos?")
    return fig

def goles(tiros,tiros_puerta,goles):
    eje_x=["shots","shots on target","goals"]
    eje_y=[int(tiros),int(tiros_puerta),int(goles)]
    fig = plt.figure(figsize = (15, 10))
    plt.bar(eje_x, eje_y)
    plt.xlabel('Cantidad')
    plt.title('efficacy shots')
    return fig

def possession(home,away,team,team2):
    numero = [int(home),int(away)]
    nombres = [str(team),str(team2)]
    plt.pie(numero, labels=nombres, autopct='%1.1f%%')
    plt.title('Possession Match')
    fig2=plt
    return  fig2

def bar_shots(lst1,lst2):
    ## Declaramos valores para el eje x
    eje_x = lst2
    
    ## Declaramos valores para el eje y
    eje_y = lst1
    
    ## Creamos Gráfica
    plt.figure(figsize = (40, 20))
    plt.bar(eje_x, eje_y)
    
    ## Legenda en el eje y
    plt.ylabel('Shots')
    
    ## Legenda en el eje x
    plt.xlabel('Partido')
    
    fig=plt
    ## Mostramos Gráfica plt.show()
    return fig

def sumalista(lista1, lista2):
    resultado=[]
    for i in range(0, len(lista1)):
        resultado.append (int(lista1[i])+int(lista2[i]))
    return resultado

def partido(lista1, lista2):
    resultado=[]
    for i in range(0, len(lista1)):
        resultado.append(str(lista1[i])+ " vs " +str(lista2[i]))
    return resultado