import matplotlib.pyplot as plt

def plotit(x,y, fig, xlabel, ylabel, title):
    plt.figure(1)
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
        

count = 100
r = 1

x_array = [0]*count
y_array = [0]*count
x = 0.1000000001
y = 0.1

#print x1, x2

for i in range(count):
    x_array[i] = x
    y_array[i] = y    
    x = r*x*(1-x)
    y = r*y*(1-y)
    print i, ": ", x, y

plotit(range(count), x_array, 1, "iteration", "value", "logistic map")
plotit(range(count), y_array, 1, "iteration", "value", "logistic map")
plt.show()
