from data import data
from bokeh.plotting import figure
from bokeh.plotting import show
from bokeh.io import curdoc

with open("birthday.json","r") as bd:
    a=[1,2,3,4,5,6,7,8,9,10,11,12] #months per number
    b=[]#number of data
    dictionary = data(bd)
    for i in dictionary["lista"]:
        b.append(i)

    curdoc().theme = "dark_minimal"
    sqare = figure(title= "birthday chart", x_axis_label ="month", y_axis_label ="time per month")
    sqare.line(a,b, legend_label="Temp", line_width=3)
    show(sqare)
