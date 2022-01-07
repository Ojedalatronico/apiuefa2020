import matplotlib.pyplot as plt
from data.get import goal_each_10,goal_each_15




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